"""Step 3 - hidden skill axes: truncated SVD of S against a permutation null.

D1  Spectrum vs. null. Singular values of the real S against ``n_perm`` copies
    in which the observed surprises are shuffled *within each problem column*
    (each problem keeps its own surprise distribution and sparsity pattern, but
    any user-level consistency is destroyed). Component k is "significant" if
    its singular value exceeds the k-th singular value of every shuffled copy.

D2  Skill-axis table. For each significant component: highest / lowest loading
    problems with their tags, and a tag-enrichment score (mean loading of
    problems carrying the tag vs. the rest, as a z-score).

Writes outputs/{svd.npz, D1_spectrum.csv, D1_spectrum.png, D2_axes.md, D2_axis_k.csv}.
"""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.sparse as sp
from scipy.sparse.linalg import svds

from . import paths
from .matrix import load as load_matrix

log = logging.getLogger(__name__)


def truncated_svd(S: sp.spmatrix, k: int, seed: int = 0):
    """Top-k SVD, singular values sorted descending. Returns (U, s, Vt)."""
    k = min(k, min(S.shape) - 1)
    rng = np.random.default_rng(seed)
    v0 = rng.standard_normal(min(S.shape))
    U, s, Vt = svds(sp.csr_matrix(S, dtype=np.float64), k=k, v0=v0)
    order = np.argsort(s)[::-1]
    return U[:, order], s[order], Vt[order]


def permute_within_columns(S: sp.spmatrix, rng: np.random.Generator) -> sp.csc_matrix:
    """Shuffle the observed values inside each column, keeping the sparsity pattern."""
    C = S.tocsc(copy=True)
    nnz = C.nnz
    col_of_entry = np.repeat(np.arange(C.shape[1]), np.diff(C.indptr))
    order = np.lexsort((rng.random(nnz), col_of_entry))  # sort by column, random within
    C.data = C.data[order]
    return C


def null_spectra(S: sp.spmatrix, k: int, n_perm: int = 20, seed: int = 0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    out = np.empty((n_perm, min(k, min(S.shape) - 1)))
    for b in range(n_perm):
        C = permute_within_columns(S, rng)
        _, s_null, _ = truncated_svd(C, k, seed=seed + b + 1)
        out[b] = s_null
        log.info("null %d/%d: top sv %.2f", b + 1, n_perm, s_null[0])
    return out


def significant_components(s: np.ndarray, null_s: np.ndarray) -> np.ndarray:
    """Boolean mask: component k beats the k-th singular value of every null run."""
    return s > null_s.max(axis=0)


def residualize_user_contest(S: sp.csr_matrix, contest_of_col: np.ndarray) -> sp.csr_matrix:
    """Subtract, from every observed s_ij, user i's mean surprise in the contest
    problem j belongs to. Removes "good day / bad day" and "form" effects that
    are shared by all problems a user faced in one round, leaving only *which*
    problems within a round surprised relative to the user's own round average.
    Rounds with a single rated problem become all-zero for that user."""
    C = S.tocoo()
    _, cidx = np.unique(contest_of_col, return_inverse=True)
    n_c = cidx.max() + 1
    P = sp.csr_matrix((np.ones(len(cidx), np.float32), (np.arange(len(cidx)), cidx)), shape=(S.shape[1], n_c))
    M = S.copy(); M.data = np.ones_like(M.data)
    sums = (S @ P).toarray(); counts = (M @ P).toarray()
    means = np.divide(sums, counts, out=np.zeros_like(sums), where=counts > 0)
    data = C.data - means[C.row, cidx[C.col]]
    return sp.csr_matrix((data.astype(np.float32), (C.row, C.col)), shape=S.shape)


def center_columns(S: sp.csr_matrix) -> sp.csr_matrix:
    """Subtract each column's mean *over observed entries* (keeps sparsity)."""
    C = S.tocsc(copy=True)
    counts = np.diff(C.indptr)
    sums = np.add.reduceat(C.data, C.indptr[:-1]) if C.nnz else np.zeros(C.shape[1])
    means = np.where(counts > 0, sums / np.maximum(counts, 1), 0.0)
    C.data = C.data - np.repeat(means, counts).astype(C.dtype)
    return C.tocsr()


# ---------------------------------------------------------------- D2 helpers
def tag_sets(problems: pd.DataFrame) -> dict[str, np.ndarray]:
    tags: dict[str, list[int]] = {}
    for col, t in zip(problems["col"], problems["tags"]):
        for tag in str(t).split(";"):
            if tag:
                tags.setdefault(tag, []).append(int(col))
    return {t: np.array(v) for t, v in tags.items()}


def tag_enrichment(loading: np.ndarray, tags: dict[str, np.ndarray], min_size: int = 15) -> pd.DataFrame:
    """z-score of mean loading for tagged vs. untagged problems, per tag."""
    rows = []
    n = len(loading)
    for tag, idx in tags.items():
        if len(idx) < min_size or len(idx) > n - min_size:
            continue
        mask = np.zeros(n, bool); mask[idx] = True
        a, b = loading[mask], loading[~mask]
        se = np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
        rows.append({"tag": tag, "n": len(idx), "mean_in": a.mean(), "mean_out": b.mean(), "z": (a.mean() - b.mean()) / se if se > 0 else 0.0})
    return pd.DataFrame(rows).sort_values("z", ascending=False).reset_index(drop=True)


def axis_table(k: int, Vt: np.ndarray, s: np.ndarray, problems: pd.DataFrame, tags: dict, top: int = 15) -> tuple[pd.DataFrame, pd.DataFrame]:
    load_k = Vt[k]
    order = np.argsort(load_k)
    hi, lo = order[::-1][:top], order[:top]
    df = problems.iloc[np.concatenate([hi, lo])].copy()
    df["loading"] = load_k[np.concatenate([hi, lo])]
    df["end"] = ["+"] * len(hi) + ["-"] * len(lo)
    df = df[["end", "loading", "contestId", "index", "name", "rating", "tags"]]
    enr = tag_enrichment(load_k, tags)
    return df, enr


def axis_rating_profile(loading: np.ndarray, rating: np.ndarray, top: int = 15) -> dict:
    """How much of an axis is just problem difficulty / which division it was set for."""
    order = np.argsort(loading)
    return {"corr_rating": float(np.corrcoef(loading, rating)[0, 1]),
            "abs_corr_rating": float(np.corrcoef(np.abs(loading), rating)[0, 1]),
            "mean_rating_plus": float(rating[order[::-1][:top]].mean()),
            "mean_rating_minus": float(rating[order[:top]].mean())}


def write_axes_report(sig: np.ndarray, s: np.ndarray, Vt: np.ndarray, U: np.ndarray, problems: pd.DataFrame, out_dir: Path,
                      top: int = 15, max_axes: int | None = None, suffix: str = "") -> pd.DataFrame:
    tags = tag_sets(problems)
    rating = problems["rating"].to_numpy(float)
    ks = np.flatnonzero(sig)
    if max_axes is not None:
        ks = ks[:max_axes]
    lines = [f"# D2 - Skill-axis table{(' (' + suffix.strip('_') + ')') if suffix else ''}", "",
             f"{int(sig.sum())} of {len(s)} components are significant against the permutation null.", "",
             "Sign of each axis is arbitrary. `+` rows = highest loading problems, `-` rows = lowest.",
             "Tag enrichment z > 0 means problems with the tag load positively on the axis.",
             "`corr(loading, rating)` close to +-1 means the axis is mostly *difficulty* (or the division the",
             "problem was set for), not a topic; look for axes with low |corr| and strong tag enrichment.", ""]
    summary_rows = []
    for k in ks:
        df, enr = axis_table(k, Vt, s, problems, tags, top)
        df.to_csv(out_dir / f"D2_axis_{k + 1}{suffix}.csv", index=False)
        prof = axis_rating_profile(Vt[k], rating, top)
        pos = ", ".join(f"{r.tag} (z={r.z:+.1f})" for r in enr[enr.z > 0].head(5).itertuples()) or "-"
        neg = ", ".join(f"{r.tag} (z={r.z:+.1f})" for r in enr[enr.z < 0].tail(5)[::-1].itertuples()) or "-"
        summary_rows.append({"axis": k + 1, "sigma": s[k], **prof,
                             "plus_tags": ", ".join(enr[enr.z > 0].head(3)["tag"]), "minus_tags": ", ".join(enr[enr.z < 0].tail(3)["tag"][::-1])})
        lines += [f"## Axis {k + 1}  (sigma = {s[k]:.2f})", "",
                  f"- enriched at `+` end: {pos}", f"- enriched at `-` end: {neg}",
                  f"- corr(loading, problem rating) = {prof['corr_rating']:+.2f}; mean rating of `+` end {prof['mean_rating_plus']:.0f}, of `-` end {prof['mean_rating_minus']:.0f}",
                  f"- user scores: std {np.std(U[:, k] * s[k]):.3f}", "",
                  "| end | loading | problem | rating | tags |", "|---|---|---|---|---|"]
        for r in df.itertuples():
            lines.append(f"| {r.end} | {r.loading:+.4f} | {r.contestId}{r.index} {r.name} | {r.rating} | {r.tags} |")
        lines += ["", "_Plain-language reading:_ TODO", ""]
    (out_dir / f"D2_axes{suffix}.md").write_text("\n".join(lines))
    summary = pd.DataFrame(summary_rows)
    summary.to_csv(out_dir / f"D2_axis_summary{suffix}.csv", index=False)
    return summary


def plot_spectrum(s: np.ndarray, null_s: np.ndarray, sig: np.ndarray, path: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    k = np.arange(1, len(s) + 1)
    fig, ax = plt.subplots(figsize=(7, 4.2))
    for b in range(null_s.shape[0]):
        ax.plot(k, null_s[b], color="0.75", lw=0.8, label="shuffled within columns" if b == 0 else None)
    ax.plot(k, null_s.max(axis=0), color="0.4", lw=1.2, ls="--", label="null max")
    ax.plot(k, s, "o-", color="C3", label="real surprise matrix")
    ax.scatter(k[sig], s[sig], s=90, facecolors="none", edgecolors="k", label=f"significant ({sig.sum()})")
    ax.set_xlabel("component"); ax.set_ylabel("singular value")
    ax.set_title("D1 - Spectrum of S vs. permutation null")
    ax.legend(); ax.grid(alpha=0.3); fig.tight_layout(); fig.savefig(path, dpi=150); plt.close(fig)


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-k", "--components", type=int, default=20)
    ap.add_argument("--n-perm", type=int, default=20)
    ap.add_argument("--center", action="store_true", help="centre each problem column over observed entries first")
    ap.add_argument("--residualize-contest", action="store_true",
                    help="subtract each user's mean surprise per contest first (removes form / good-day effects; stricter test)")
    ap.add_argument("--suffix", default="", help="suffix for output files, e.g. _resid")
    ap.add_argument("--top", type=int, default=15, help="problems per end in D2 tables")
    ap.add_argument("--max-axes", type=int, default=None, help="cap number of axes written to D2")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(levelname)s %(message)s")
    paths.ensure_dirs()

    S, M, users, problems = load_matrix()
    if args.residualize_contest:
        S = residualize_user_contest(S, problems["contestId"].to_numpy())
        log.info("residualized per user x contest: std of surprises %.3f", S.data.std())
    if args.center:
        S = center_columns(S)
    sfx = args.suffix
    log.info("SVD of %dx%d (nnz=%d), k=%d", *S.shape, S.nnz, args.components)
    U, s, Vt = truncated_svd(S, args.components, seed=args.seed)
    null_s = null_spectra(S, args.components, args.n_perm, seed=args.seed)
    sig = significant_components(s, null_s)
    log.info("singular values: %s", np.round(s, 2))
    log.info("null max      : %s", np.round(null_s.max(axis=0), 2))
    log.info("significant components: %d  -> %s", sig.sum(), np.flatnonzero(sig) + 1)

    np.savez_compressed(paths.OUT / f"svd{sfx}.npz", U=U.astype(np.float32), s=s, Vt=Vt.astype(np.float32), null_s=null_s, sig=sig,
                        centered=args.center, residualized=args.residualize_contest)
    pd.DataFrame({"component": np.arange(1, len(s) + 1), "sigma": s, "null_max": null_s.max(0), "null_mean": null_s.mean(0),
                  "null_std": null_s.std(0), "ratio_to_null_max": s / null_s.max(0), "significant": sig}).to_csv(paths.OUT / f"D1_spectrum{sfx}.csv", index=False)
    plot_spectrum(s, null_s, sig, paths.OUT / f"D1_spectrum{sfx}.png")
    summary = write_axes_report(sig, s, Vt, U, problems, paths.OUT, top=args.top, max_axes=args.max_axes, suffix=sfx)
    if not summary.empty:
        log.info("axis summary:\n%s", summary[["axis", "sigma", "corr_rating", "plus_tags", "minus_tags"]].round(2).to_string(index=False))
    log.info("wrote D1/D2 to %s", paths.OUT)


if __name__ == "__main__":
    main()
