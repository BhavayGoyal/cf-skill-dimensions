"""Step 4 - group problems on the significant skill axes and compare with tags.

Each problem gets coordinates V_sig * sigma_sig (its row of V Sigma restricted to
significant components). We cluster with k-means (k chosen by silhouette;
spectral clustering on a kNN graph as an optional extension), then compare
clusters with the setters' tags:

    J(cluster, tag) = |C ∩ T| / |C ∪ T|
    agreement       = mean over clusters of  max_tag J(cluster, tag)

reported against random partitions of the same cluster sizes (mean, std,
empirical p-value).

Writes outputs/{D3_heatmap.png, D3_agreement.json, D3_clusters.csv}.
"""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans, SpectralClustering
from sklearn.metrics import silhouette_score

from . import paths
from .matrix import load as load_matrix
from .svd import tag_sets

log = logging.getLogger(__name__)


def problem_coords(Vt: np.ndarray, s: np.ndarray, sig: np.ndarray, n_axes: int | None = None, standardize: bool = True) -> np.ndarray:
    ks = np.flatnonzero(sig) if n_axes is None else np.arange(n_axes)
    X = (Vt[ks] * s[ks, None]).T  # problems x axes
    if standardize:
        X = (X - X.mean(0)) / (X.std(0) + 1e-12)
    return X


def choose_k_kmeans(X: np.ndarray, k_range=range(2, 13), seed: int = 0) -> tuple[int, dict[int, float]]:
    scores = {}
    for k in k_range:
        labels = KMeans(k, n_init=10, random_state=seed).fit_predict(X)
        scores[k] = float(silhouette_score(X, labels))
    best = max(scores, key=scores.get)
    return best, scores


def kmeans_labels(X: np.ndarray, k: int, seed: int = 0) -> np.ndarray:
    return KMeans(k, n_init=10, random_state=seed).fit_predict(X)


def spectral_labels(X: np.ndarray, k: int, n_neighbors: int = 15, seed: int = 0) -> np.ndarray:
    return SpectralClustering(k, affinity="nearest_neighbors", n_neighbors=n_neighbors, random_state=seed, assign_labels="discretize").fit_predict(X)


def jaccard_matrix(labels: np.ndarray, tags: dict[str, np.ndarray], n: int) -> pd.DataFrame:
    tag_names = sorted(tags)
    T = np.zeros((len(tag_names), n), bool)
    for r, t in enumerate(tag_names):
        T[r, tags[t]] = True
    ks = np.unique(labels)
    C = np.stack([labels == k for k in ks])
    inter = C.astype(int) @ T.T.astype(int)
    union = C.sum(1)[:, None] + T.sum(1)[None, :] - inter
    J = inter / np.maximum(union, 1)
    return pd.DataFrame(J, index=[f"cluster {k}" for k in ks], columns=tag_names)


def agreement_score(J: pd.DataFrame) -> float:
    """Mean over clusters of best-matching tag Jaccard."""
    return float(J.values.max(axis=1).mean())


def random_baseline(labels: np.ndarray, tags: dict, n: int, n_random: int = 200, seed: int = 0) -> np.ndarray:
    """Agreement scores for random partitions with the same cluster sizes."""
    rng = np.random.default_rng(seed)
    out = np.empty(n_random)
    for b in range(n_random):
        out[b] = agreement_score(jaccard_matrix(rng.permutation(labels), tags, n))
    return out


def plot_heatmap(J: pd.DataFrame, path: Path, title: str) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    # keep tags with some signal so the figure is legible
    keep = J.columns[(J.max(0) > 0.02)]
    Jp = J[keep]
    fig, ax = plt.subplots(figsize=(max(8, 0.45 * len(keep)), 0.6 * len(J) + 2))
    im = ax.imshow(Jp.values, cmap="viridis", aspect="auto")
    ax.set_xticks(range(len(keep))); ax.set_xticklabels(keep, rotation=70, ha="right", fontsize=8)
    ax.set_yticks(range(len(Jp))); ax.set_yticklabels(Jp.index, fontsize=8)
    for i in range(Jp.shape[0]):
        j = int(np.argmax(Jp.values[i]))
        ax.text(j, i, f"{Jp.values[i, j]:.2f}", ha="center", va="center", color="w", fontsize=7)
    fig.colorbar(im, ax=ax, label="Jaccard(cluster, tag)")
    ax.set_title(title); fig.tight_layout(); fig.savefig(path, dpi=150); plt.close(fig)


def agreement_by_k(X: np.ndarray, problems: pd.DataFrame, k_range, n_random: int, seed: int) -> pd.DataFrame:
    """Agreement vs. random for every k, so the reader is not at the mercy of the silhouette pick."""
    tags = {t: v for t, v in tag_sets(problems).items() if len(v) >= 10}
    n = len(problems)
    rows = []
    for k in k_range:
        labels = kmeans_labels(X, k, seed)
        real = agreement_score(jaccard_matrix(labels, tags, n))
        null = random_baseline(labels, tags, n, n_random, seed)
        rows.append({"k": k, "silhouette": float(silhouette_score(X, labels)), "agreement": real, "random_mean": null.mean(),
                     "random_std": null.std(), "z": (real - null.mean()) / (null.std() + 1e-12), "p_value": float((null >= real).mean())})
        log.info("k=%2d silhouette %.3f agreement %.3f vs random %.3f (z=%.1f)", k, rows[-1]["silhouette"], real, null.mean(), rows[-1]["z"])
    return pd.DataFrame(rows)


def run(method: str, X: np.ndarray, problems: pd.DataFrame, k: int | None, n_random: int, seed: int, out_dir: Path, suffix: str = "") -> dict:
    tags = {t: v for t, v in tag_sets(problems).items() if len(v) >= 10}
    n = len(problems)
    if k is None:
        k, sil = choose_k_kmeans(X, seed=seed)
        log.info("silhouette by k: %s -> k=%d", {kk: round(v, 3) for kk, v in sil.items()}, k)
    else:
        sil = {}
    labels = kmeans_labels(X, k, seed) if method == "kmeans" else spectral_labels(X, k, seed=seed)
    J = jaccard_matrix(labels, tags, n)
    real = agreement_score(J)
    null = random_baseline(labels, tags, n, n_random, seed)
    p = float((null >= real).mean())
    z = float((real - null.mean()) / (null.std() + 1e-12))
    log.info("%s k=%d agreement %.3f vs random %.3f +- %.3f (z=%.1f, p=%.3f)", method, k, real, null.mean(), null.std(), z, p)

    best_tag = J.idxmax(axis=1)
    summary = {"method": method, "k": int(k), "silhouette_by_k": sil, "agreement": real,
               "random_mean": float(null.mean()), "random_std": float(null.std()), "z": z, "p_value": p,
               "clusters": []}
    for ci, name in enumerate(J.index):
        members = np.flatnonzero(labels == ci)
        top_tags = J.loc[name].sort_values(ascending=False).head(3)
        tag_counts = pd.Series([t for col in members for t in str(problems.iloc[col]["tags"]).split(";") if t]).value_counts().head(5)
        summary["clusters"].append({"cluster": int(ci), "size": int(len(members)), "best_tag": best_tag[name],
                                    "best_jaccard": float(J.loc[name].max()), "top_jaccard_tags": top_tags.round(3).to_dict(),
                                    "most_common_tags": tag_counts.to_dict(),
                                    "mean_rating": float(problems.iloc[members]["rating"].mean())})
    plot_heatmap(J, out_dir / f"D3_heatmap{suffix}.png", f"D3 - {method}, k={k}: agreement {real:.3f} vs random {null.mean():.3f}")
    J.to_csv(out_dir / f"D3_jaccard{suffix}.csv")
    out = problems[["col", "contestId", "index", "name", "rating", "tags"]].copy()
    out["cluster"] = labels
    out.to_csv(out_dir / f"D3_clusters{suffix}.csv", index=False)
    (out_dir / f"D3_agreement{suffix}.json").write_text(json.dumps(summary, indent=1))
    return summary


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-k", type=int, default=None, help="number of clusters (default: pick by silhouette)")
    ap.add_argument("--n-axes", type=int, default=None, help="use the top N axes instead of the significant ones")
    ap.add_argument("--n-random", type=int, default=200)
    ap.add_argument("--k-max", type=int, default=12, help="largest k in the agreement-by-k sweep")
    ap.add_argument("--min-obs", type=int, default=0, help="only cluster problems observed by at least this many users")
    ap.add_argument("--svd", default=None, help="path to an svd npz (default outputs/svd.npz)")
    ap.add_argument("--suffix", default="", help="suffix for output files")
    ap.add_argument("--spectral", action="store_true", help="also run spectral clustering on a kNN graph")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(levelname)s %(message)s")
    paths.ensure_dirs()

    _, M, _, problems = load_matrix()
    z = np.load(args.svd or paths.SVD_NPZ)
    sig = z["sig"]
    n_axes = args.n_axes
    if n_axes is None and sig.sum() < 2:
        log.warning("only %d significant axes; falling back to top 2 (set --n-axes to override)", sig.sum())
        n_axes = 2
    X = problem_coords(z["Vt"], z["s"], sig, n_axes)
    if args.min_obs > 0:
        n_obs = np.asarray(M.sum(axis=0)).ravel()
        keep = n_obs >= args.min_obs
        log.info("keeping %d/%d problems with >= %d observed users", keep.sum(), len(keep), args.min_obs)
        X = X[keep]
        problems = problems[keep].reset_index(drop=True)
        problems["col"] = np.arange(len(problems))
    log.info("problem coordinates: %s", X.shape)
    sfx = args.suffix

    by_k = agreement_by_k(X, problems, range(2, args.k_max + 1), max(50, args.n_random // 4), args.seed)
    by_k.to_csv(paths.OUT / f"D3_agreement_by_k{sfx}.csv", index=False)
    run("kmeans", X, problems, args.k, args.n_random, args.seed, paths.OUT, suffix=sfx)
    if args.spectral:
        k = args.k or json.loads((paths.OUT / f"D3_agreement{sfx}.json").read_text())["k"]
        run("spectral", X, problems, k, args.n_random, args.seed, paths.OUT, suffix=f"{sfx}_spectral")


if __name__ == "__main__":
    main()
