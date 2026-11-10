"""Step 5 - skill twins with MinHash LSH.

Each user becomes a set of tokens
    hit:j   solved problem j although p_ij < 1 - THR   (i.e. s_ij >  THR)
    miss:j  missed problem j although p_ij >     THR   (i.e. s_ij < -THR)
with THR = 0.7 by default (so hits need p < 0.3 and misses need p > 0.7, as in
the proposal). Two users are skill twins if these token sets have high Jaccard
similarity.

MinHash: ``n_hashes`` universal hash functions h(x) = (a x + b) mod P; the
signature of a set is the element-wise minimum over its tokens. Banding with
b bands of r rows (b*r = n_hashes) puts the similarity threshold near
(1/b)^(1/r)  (32 x 4 -> 0.42). Candidate pairs sharing a band bucket are
verified with exact Jaccard.

D4  On a sample of users we compute exact top-10 neighbours by brute force and
    report recall@10 and speed-up for several (bands, rows) settings.
Then the chosen setting is run on all users and the top-10 twins per user are
saved for the demo (D5).

Writes outputs/{D4_lsh_eval.csv, D4_lsh_eval.png, twins.json.gz}.
"""

from __future__ import annotations

import argparse
import gzip
import json
import logging
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.sparse as sp

from . import paths
from .matrix import load as load_matrix

log = logging.getLogger(__name__)

MERSENNE = (1 << 31) - 1  # prime modulus for the universal hash family


# ------------------------------------------------------------------ tokens
def build_tokens(S: sp.csr_matrix, thr: float = 0.7, min_tokens: int = 5) -> tuple[sp.csr_matrix, np.ndarray]:
    """Binary users x tokens matrix (token 2j = hit:j, 2j+1 = miss:j) and the
    indices of users that have at least ``min_tokens`` tokens."""
    C = S.tocoo()
    hit = C.data > thr
    miss = C.data < -thr
    rows = np.concatenate([C.row[hit], C.row[miss]])
    cols = np.concatenate([2 * C.col[hit], 2 * C.col[miss] + 1])
    X = sp.csr_matrix((np.ones(len(rows), np.int8), (rows, cols)), shape=(S.shape[0], 2 * S.shape[1]))
    X.data[:] = 1
    keep = np.flatnonzero(np.diff(X.indptr) >= min_tokens)
    return X, keep


# ----------------------------------------------------------------- minhash
def minhash_signatures(X: sp.csr_matrix, n_hashes: int = 128, seed: int = 0) -> np.ndarray:
    """(n_users, n_hashes) uint64 signatures. Rows with no tokens get all-max."""
    rng = np.random.default_rng(seed)
    # a, b, token ids < P = 2^31 - 1  =>  a*t + b < 2^63: no uint64 overflow, and the
    # modulus actually wraps so each hash is a different pseudo-random permutation
    a = rng.integers(1, MERSENNE, size=n_hashes, dtype=np.uint64)
    b = rng.integers(0, MERSENNE, size=n_hashes, dtype=np.uint64)
    n_users, n_tokens = X.shape
    assert n_tokens < MERSENNE
    tokens = np.arange(n_tokens, dtype=np.uint64)
    P = np.uint64(MERSENNE)
    sig = np.full((n_users, n_hashes), np.iinfo(np.uint64).max, dtype=np.uint64)
    nonempty = np.diff(X.indptr) > 0
    starts = X.indptr[:-1][nonempty]
    for h in range(n_hashes):
        hv = (a[h] * tokens + b[h]) % P
        vals = hv[X.indices]
        sig[nonempty, h] = np.minimum.reduceat(vals, starts)
    return sig


def candidate_pairs(sig: np.ndarray, bands: int, rows: int, max_bucket: int = 2000) -> np.ndarray:
    """All (i, j) with i < j that share at least one band bucket. Shape (m, 2).

    Buckets holding more than ``max_bucket`` users are skipped (they would generate
    millions of near-useless pairs). This is an approximation: it lowers the number of
    candidates and can lower recall, which is why recall is always measured against
    exact brute force."""
    assert bands * rows <= sig.shape[1], "bands*rows must be <= n_hashes"
    chunks = []
    for band in range(bands):
        block = np.ascontiguousarray(sig[:, band * rows:(band + 1) * rows])
        keys = block.view(np.dtype((np.void, block.dtype.itemsize * rows))).ravel()
        _, inv = np.unique(keys, return_inverse=True)
        order = np.argsort(inv, kind="stable")
        inv_sorted = inv[order]
        bounds = np.flatnonzero(np.diff(inv_sorted)) + 1
        for grp in np.split(order, bounds):
            if 1 < len(grp) <= max_bucket:
                grp = np.sort(grp)
                ii, jj = np.triu_indices(len(grp), 1)
                chunks.append(np.column_stack([grp[ii], grp[jj]]))
    if not chunks:
        return np.empty((0, 2), dtype=np.int64)
    pairs = np.concatenate(chunks).astype(np.int64)
    return np.unique(pairs, axis=0)


def exact_jaccard_pairs(X: sp.csr_matrix, pairs: np.ndarray, batch: int = 200_000) -> np.ndarray:
    sizes = np.diff(X.indptr)
    out = np.empty(len(pairs))
    for st in range(0, len(pairs), batch):
        P = pairs[st:st + batch]
        inter = np.asarray(X[P[:, 0]].multiply(X[P[:, 1]]).sum(axis=1)).ravel()
        union = sizes[P[:, 0]] + sizes[P[:, 1]] - inter
        out[st:st + batch] = inter / np.maximum(union, 1)
    return out


def exact_jaccard_matrix(X: sp.csr_matrix) -> np.ndarray:
    """Dense all-pairs Jaccard (only for samples of a few thousand users)."""
    Xf = X.astype(np.float32)
    inter = (Xf @ Xf.T).toarray()
    sizes = np.asarray(Xf.sum(1)).ravel()
    union = sizes[:, None] + sizes[None, :] - inter
    J = inter / np.maximum(union, 1)
    np.fill_diagonal(J, 0.0)
    return J


def brute_force_topk_chunked(X: sp.csr_matrix, k: int = 10, chunk: int = 2000) -> dict[int, list[tuple[int, float]]]:
    """Exact top-k Jaccard neighbours for every row, computed in row chunks so it
    scales to tens of thousands of users (the honest baseline for the full run)."""
    Xf = X.astype(np.float32)
    XT = Xf.T.tocsc()
    sizes = np.asarray(Xf.sum(1)).ravel()
    out = {}
    for st in range(0, X.shape[0], chunk):
        inter = (Xf[st:st + chunk] @ XT).toarray()
        union = sizes[st:st + chunk, None] + sizes[None, :] - inter
        J = inter / np.maximum(union, 1)
        for r in range(J.shape[0]):
            J[r, st + r] = 0.0
        out.update({st + i: v for i, v in topk_from_matrix(J, k).items()})
    return out


def topk_from_pairs(pairs: np.ndarray, jac: np.ndarray, n: int, k: int = 10) -> dict[int, list[tuple[int, float]]]:
    nb: dict[int, list[tuple[int, float]]] = defaultdict(list)
    for (i, j), v in zip(pairs, jac):
        if v > 0:
            nb[int(i)].append((int(j), float(v)))
            nb[int(j)].append((int(i), float(v)))
    return {i: sorted(v, key=lambda t: -t[1])[:k] for i, v in nb.items()}


def topk_from_matrix(J: np.ndarray, k: int = 10, row_offset: int = 0) -> dict[int, list[tuple[int, float]]]:
    """Top-k per row of a (possibly rectangular) similarity matrix; keys are row_offset + i."""
    out = {}
    kk = min(k, J.shape[1] - 1)
    for i in range(J.shape[0]):
        idx = np.argpartition(-J[i], kk)[:k]
        idx = idx[J[i, idx] > 0]
        idx = idx[np.argsort(-J[i, idx])]
        out[i] = [(int(j), float(J[i, j])) for j in idx]
    return out


def recall_at_k(exact: dict, approx: dict, k: int = 10) -> float:
    """Mean over users of |approx top-k ∩ exact top-k| / |exact top-k|."""
    vals = []
    for i, ex in exact.items():
        if not ex:
            continue
        e = {j for j, _ in ex[:k]}
        a = {j for j, _ in approx.get(i, [])[:k]}
        vals.append(len(e & a) / len(e))
    return float(np.mean(vals)) if vals else float("nan")


def lsh_threshold(bands: int, rows: int) -> float:
    return (1.0 / bands) ** (1.0 / rows)


# -------------------------------------------------------------- evaluation
def evaluate(X: sp.csr_matrix, keep: np.ndarray, n_sample: int, settings: list[tuple[int, int]], n_hashes: int, k: int, seed: int) -> tuple[pd.DataFrame, dict]:
    rng = np.random.default_rng(seed)
    sample = rng.choice(keep, size=min(n_sample, len(keep)), replace=False)
    Xs = X[sample]
    t0 = time.perf_counter()
    Js = exact_jaccard_matrix(Xs)
    exact = topk_from_matrix(Js, k)
    t_exact = time.perf_counter() - t0
    top_sorted = -np.sort(-Js, axis=1)
    nn_stats = {"n_sample": int(len(sample)), "median_tokens": float(np.median(np.diff(Xs.indptr))),
                "top1_jaccard_median": float(np.median(top_sorted[:, 0])), "top1_jaccard_p90": float(np.percentile(top_sorted[:, 0], 90)),
                f"top{k}_jaccard_median": float(np.median(top_sorted[:, k - 1]))}
    log.info("brute force on %d users: %.2fs; exact nearest-neighbour Jaccard median %.3f (p90 %.3f), %d-th neighbour median %.3f",
             len(sample), t_exact, nn_stats["top1_jaccard_median"], nn_stats["top1_jaccard_p90"], k, nn_stats[f"top{k}_jaccard_median"])

    t0 = time.perf_counter()
    sig = minhash_signatures(Xs, n_hashes, seed)
    t_sig = time.perf_counter() - t0
    rows_out = []
    for bands, rows in settings:
        t0 = time.perf_counter()
        pairs = candidate_pairs(sig, bands, rows)
        jac = exact_jaccard_pairs(Xs, pairs) if len(pairs) else np.empty(0)
        approx = topk_from_pairs(pairs, jac, len(sample), k)
        t_lsh = time.perf_counter() - t0 + t_sig
        rec = recall_at_k(exact, approx, k)
        n_all = len(sample) * (len(sample) - 1) // 2
        rows_out.append({"bands": bands, "rows": rows, "threshold": lsh_threshold(bands, rows), "n_candidates": len(pairs),
                         "candidate_fraction": len(pairs) / n_all, f"recall@{k}": rec, "time_lsh_s": t_lsh,
                         "time_exact_s": t_exact, "speedup": t_exact / max(t_lsh, 1e-9)})
        log.info("b=%d r=%d thr=%.2f: %d candidates (%.4f of pairs), recall@%d=%.3f, speedup x%.1f",
                 bands, rows, lsh_threshold(bands, rows), len(pairs), len(pairs) / n_all, k, rec, t_exact / max(t_lsh, 1e-9))
    return pd.DataFrame(rows_out), nn_stats


def plot_eval(df: pd.DataFrame, path: Path, k: int) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(6, 4.2))
    rec = df[f"recall@{k}"].to_numpy()
    ax.plot(df["speedup"], rec, "o-")
    for i, ((_, r), y) in enumerate(zip(df.iterrows(), rec)):
        dy = 8 + 11 * (i % 3) if i else 8   # stagger labels so dense points don't overlap
        ax.annotate(f"{int(r['bands'])}x{int(r['rows'])} (t={r['threshold']:.2f})", (r["speedup"], y), textcoords="offset points",
                    xytext=(0, dy), ha="center", fontsize=8, arrowprops=dict(arrowstyle="-", lw=0.4, color="0.6") if i else None)
    ax.set_xscale("log"); ax.set_xlabel("speed-up over brute force"); ax.set_ylabel(f"recall@{k}")
    ax.set_ylim(0, 1.05); ax.grid(alpha=0.3); ax.set_title("D4 - MinHash LSH: recall vs speed-up")
    fig.tight_layout(); fig.savefig(path, dpi=150); plt.close(fig)


def full_run(X: sp.csr_matrix, keep: np.ndarray, bands: int, rows: int, n_hashes: int, k: int, seed: int,
             min_jaccard: float = 0.0, brute_force: bool = True) -> tuple[dict[int, list[tuple[int, float]]], dict]:
    """LSH twins for all users in ``keep``; optionally also time the exact chunked
    brute force on the same users and report recall against it."""
    Xk = X[keep]
    t0 = time.perf_counter()
    sig = minhash_signatures(Xk, n_hashes, seed)
    pairs = candidate_pairs(sig, bands, rows)
    jac = exact_jaccard_pairs(Xk, pairs)
    top = topk_from_pairs(pairs[jac >= min_jaccard], jac[jac >= min_jaccard], len(keep), k)
    t_lsh = time.perf_counter() - t0
    n_all = len(keep) * (len(keep) - 1) // 2
    stats = {"n_users": int(len(keep)), "bands": bands, "rows": rows, "n_candidates": int(len(pairs)),
             "candidate_fraction": len(pairs) / max(n_all, 1), "time_lsh_s": t_lsh}
    log.info("full run on %d users: %d candidate pairs (%.5f of all pairs) in %.1fs", len(keep), len(pairs), stats["candidate_fraction"], t_lsh)
    if brute_force:
        t0 = time.perf_counter()
        exact = brute_force_topk_chunked(Xk, k)
        stats["time_exact_s"] = time.perf_counter() - t0
        stats["speedup"] = stats["time_exact_s"] / max(t_lsh, 1e-9)
        stats[f"recall@{k}"] = recall_at_k(exact, top, k)
        log.info("full brute force: %.1fs -> speed-up x%.1f, recall@%d=%.3f", stats["time_exact_s"], stats["speedup"], k, stats[f"recall@{k}"])
    return {int(keep[i]): [(int(keep[j]), v) for j, v in nb] for i, nb in top.items()}, stats


def save_twins(twins: dict, users: pd.DataFrame, path: Path, meta: dict) -> None:
    handles = users["handle"].tolist()
    payload = {"meta": meta, "twins": {handles[i]: [[handles[j], round(v, 4)] for j, v in nb] for i, nb in twins.items()}}
    with gzip.open(path, "wt", encoding="utf-8") as fh:
        json.dump(payload, fh)


def load_twins(path: Path = paths.TWINS_JSON) -> dict:
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        return json.load(fh)


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--thr", type=float, default=0.7, help="|s| threshold for hit/miss tokens")
    ap.add_argument("--min-tokens", type=int, default=5)
    ap.add_argument("--n-hashes", type=int, default=256)
    ap.add_argument("--n-sample", type=int, default=3000)
    ap.add_argument("--settings", default="128x2,85x3,64x4,51x5,32x8",
                    help="bands x rows list for D4 (thresholds ~0.09, 0.23, 0.35, 0.46, 0.65)")
    ap.add_argument("--bands", type=int, default=128, help="setting for the full run")
    ap.add_argument("--rows", type=int, default=2)
    ap.add_argument("-k", type=int, default=10)
    ap.add_argument("--skip-full", action="store_true")
    ap.add_argument("--no-full-brute-force", action="store_true", help="skip the exact baseline on the full user set")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(levelname)s %(message)s")
    paths.ensure_dirs()

    S, M, users, problems = load_matrix()
    X, keep = build_tokens(S, args.thr, args.min_tokens)
    sizes = np.diff(X.indptr)
    log.info("%d users with >= %d tokens (median %d tokens); %d distinct tokens used",
             len(keep), args.min_tokens, int(np.median(sizes[keep])) if len(keep) else 0, int((X.sum(0) > 0).sum()))

    settings = [tuple(int(v) for v in s.split("x")) for s in args.settings.split(",")]
    df, nn_stats = evaluate(X, keep, args.n_sample, settings, args.n_hashes, args.k, args.seed)
    df.to_csv(paths.OUT / "D4_lsh_eval.csv", index=False)
    (paths.OUT / "D4_neighbour_stats.json").write_text(json.dumps({"thr": args.thr, **nn_stats}, indent=1))
    plot_eval(df, paths.OUT / "D4_lsh_eval.png", args.k)

    if not args.skip_full:
        twins, stats = full_run(X, keep, args.bands, args.rows, args.n_hashes, args.k, args.seed, brute_force=not args.no_full_brute_force)
        stats.update({"thr": args.thr, "n_hashes": args.n_hashes, "k": args.k, "n_with_twins": len(twins)})
        (paths.OUT / "D4_full_run.json").write_text(json.dumps(stats, indent=1))
        save_twins(twins, users, paths.TWINS_JSON, stats)
        log.info("saved twins for %d users to %s", len(twins), paths.TWINS_JSON)


if __name__ == "__main__":
    main()
