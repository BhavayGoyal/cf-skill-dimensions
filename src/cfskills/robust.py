"""Robustness analyses that attack the weak points of the main pipeline.

    heldout    Does a rank-k model predict *hidden* solves better than Elo (and
               better than Elo + user/problem bias)? Log-loss, Brier, AUC by k.
    splithalf  Fit on odd and even rounds separately. Are users' axis scores and
               per-tag surprise profiles the same trait in both halves?
    paramnull  Second null for D1: simulate y_ij ~ Bernoulli(p_ij) under "rating
               is the whole story" (same mask, same Elo probabilities).
    band       Re-run SVD + permutation null inside a single rating band so that
               Div. 1 vs Div. 2 problem pools cannot create axes.
    tagpred    Can a problem's tag be predicted from its axis coordinates beyond
               its difficulty rating? Cross-validated AUC per tag.
    all        Run everything.

Outputs are written to outputs/R_*.{csv,json,png,md}.
"""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.sparse as sp

from . import paths
from .matrix import load as load_matrix
from .svd import null_spectra, permute_within_columns, significant_components, tag_enrichment, tag_sets, truncated_svd

log = logging.getLogger(__name__)
EPS = 1e-4


# --------------------------------------------------------------------------- utils
def _p_from_s(s: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Recover (y, p) from surprise s = y - p (y in {0,1}, p in (0,1))."""
    y = (s > 0).astype(np.float64)
    p = np.where(s > 0, 1.0 - s, -s).astype(np.float64)
    return y, np.clip(p, EPS, 1 - EPS)


def _logloss(y, p):
    p = np.clip(p, EPS, 1 - EPS)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def _auc(y, score):
    from sklearn.metrics import roc_auc_score
    return float(roc_auc_score(y, score))


def _biases(S: sp.csr_matrix, n_iter: int = 3) -> tuple[np.ndarray, np.ndarray]:
    """Alternating user / problem mean surprise on observed entries (simple ALS for s ~ b_u + b_p)."""
    C = S.tocoo()
    bu = np.zeros(S.shape[0]); bp = np.zeros(S.shape[1])
    cu = np.bincount(C.row, minlength=S.shape[0]).astype(float)
    cp = np.bincount(C.col, minlength=S.shape[1]).astype(float)
    for _ in range(n_iter):
        bp = np.bincount(C.col, weights=C.data - bu[C.row], minlength=S.shape[1]) / np.maximum(cp, 1)
        bu = np.bincount(C.row, weights=C.data - bp[C.col], minlength=S.shape[0]) / np.maximum(cu, 1)
    return bu, bp


def _residual(S: sp.csr_matrix, bu: np.ndarray, bp: np.ndarray) -> sp.csr_matrix:
    C = S.tocoo()
    return sp.csr_matrix((C.data - bu[C.row] - bp[C.col], (C.row, C.col)), shape=S.shape)


def _reconstruct(U, s, Vt, rows, cols, k):
    if k == 0:
        return np.zeros(len(rows))
    return np.einsum("ik,ik->i", U[rows, :k] * s[:k], Vt[:k, cols].T)


# ------------------------------------------------------------------------- heldout
def _split_mask(C: sp.coo_matrix, problems: pd.DataFrame, frac: float, mode: str, rng) -> np.ndarray:
    """Integer split label per observed entry: 0 train, 1 calibration, 2 test."""
    if mode == "entries":
        u = rng.random(C.nnz)
    else:  # whole (user, round) blocks share a fate
        contest_of_col = problems["contestId"].to_numpy()
        _, cidx = np.unique(contest_of_col, return_inverse=True)
        key = C.row.astype(np.int64) * (cidx.max() + 1) + cidx[C.col]
        uniq, inv = np.unique(key, return_inverse=True)
        u = rng.random(len(uniq))[inv]
    return np.where(u < frac, 2, np.where(u < 2 * frac, 1, 0))


def _calibrated(y_cal, feats_cal, feats_te):
    """Fit logistic regression y ~ feats on the calibration split, predict on test."""
    from sklearn.linear_model import LogisticRegression
    clf = LogisticRegression(C=1e6, max_iter=1000).fit(feats_cal, y_cal)
    return clf.predict_proba(feats_te)[:, 1], clf.coef_.ravel()


def heldout(S: sp.csr_matrix, problems: pd.DataFrame, ks=(1, 2, 3, 5, 10, 20, 40), frac=0.1, mode="entries", seed=0, out=paths.OUT) -> pd.DataFrame:
    """Hide observed entries, fit on the rest, score the hidden ones.

    Observed entries are split 80/10/10 into train / calibration / test. The SVD
    is fitted on train only; a 3-parameter logistic calibration
    (logit p_elo, bias, rank-k reconstruction) is fitted on the calibration
    split; metrics are reported on test. So "rank-k" can only win if the
    reconstruction carries information about solves it never saw.

    mode="entries":       random cells.
    mode="user_contest":  whole (user, round) blocks are hidden together, so the
                          model cannot lean on the user's other results in the
                          same round ("predict a round you didn't see").
    """
    rng = np.random.default_rng(seed)
    C = S.tocoo()
    split = _split_mask(C, problems, frac, mode, rng)
    tr, ca, te = (split == i for i in range(3))
    S_tr = sp.csr_matrix((C.data[tr], (C.row[tr], C.col[tr])), shape=S.shape)
    y_ca, p_ca = _p_from_s(C.data[ca].astype(np.float64)); r_ca, c_ca = C.row[ca], C.col[ca]
    y_te, p_te = _p_from_s(C.data[te].astype(np.float64)); r_te, c_te = C.row[te], C.col[te]
    logit = lambda p: np.log(p / (1 - p))
    log.info("heldout[%s]: %d train / %d calib / %d test entries (test base rate %.3f)", mode, tr.sum(), ca.sum(), te.sum(), y_te.mean())

    rows = []
    def add(name, k, feats_ca, feats_te):
        pred, coef = _calibrated(y_ca, feats_ca, feats_te)
        pred = np.clip(pred, EPS, 1 - EPS)
        rows.append({"model": name, "k": k, "logloss": _logloss(y_te, pred), "brier": float(np.mean((y_te - pred) ** 2)), "auc": _auc(y_te, pred),
                     "coef": np.round(coef, 3).tolist()})
        log.info("  %-28s k=%-3d logloss %.4f  brier %.4f  auc %.4f  coef %s", name, k, rows[-1]["logloss"], rows[-1]["brier"], rows[-1]["auc"], rows[-1]["coef"])

    F0_ca, F0_te = logit(p_ca)[:, None], logit(p_te)[:, None]
    add("Elo only", 0, F0_ca, F0_te)
    bu, bp = _biases(S_tr)
    add("Elo + problem bias", 0, np.c_[F0_ca, bp[c_ca]], np.c_[F0_te, bp[c_te]])
    Fb_ca, Fb_te = np.c_[F0_ca, bp[c_ca], bu[r_ca]], np.c_[F0_te, bp[c_te], bu[r_te]]
    add("Elo + problem + user bias", 0, Fb_ca, Fb_te)
    R = _residual(S_tr, bu, bp)
    kmax = max(ks)
    U, s, Vt = truncated_svd(R, kmax, seed=seed)
    for k in ks:
        add("Elo + biases + rank-k", k, np.c_[Fb_ca, _reconstruct(U, s, Vt, r_ca, c_ca, k)], np.c_[Fb_te, _reconstruct(U, s, Vt, r_te, c_te, k)])
    # the proposal's raw version: SVD of S itself with no bias terms
    U2, s2, Vt2 = truncated_svd(S_tr, kmax, seed=seed)
    for k in ks:
        add("Elo + rank-k (raw S)", k, np.c_[F0_ca, _reconstruct(U2, s2, Vt2, r_ca, c_ca, k)], np.c_[F0_te, _reconstruct(U2, s2, Vt2, r_te, c_te, k)])

    df = pd.DataFrame(rows)
    base = df.iloc[0]
    df["logloss_gain_vs_elo_pct"] = 100 * (base["logloss"] - df["logloss"]) / base["logloss"]
    df["mode"] = mode
    df.to_csv(out / f"R_heldout_{mode}.csv", index=False)
    _plot_heldout(df, out / f"R_heldout_{mode}.png", mode)
    return df


def _plot_heldout(df: pd.DataFrame, path: Path, mode: str) -> None:
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    for ax, metric in zip(axes, ["logloss", "auc"]):
        for name, g in df.groupby("model", sort=False):
            if "rank-k" in name:
                ax.plot(g["k"], g[metric], "o-", label=name)
            else:
                ax.axhline(g[metric].iloc[0], ls="--", lw=1, label=name, color={"Elo only": "k", "Elo + problem bias": "0.5", "Elo + problem + user bias": "C3"}.get(name))
        ax.set_xscale("log"); ax.set_xlabel("rank k"); ax.set_ylabel(metric); ax.grid(alpha=0.3)
    axes[0].legend(fontsize=7); fig.suptitle(f"Held-out prediction of in-contest solves ({mode})")
    fig.tight_layout(); fig.savefig(path, dpi=150); plt.close(fig)


# ----------------------------------------------------------------------- splithalf
def splithalf(S: sp.csr_matrix, problems: pd.DataFrame, k: int = 10, seed: int = 0, out=paths.OUT) -> dict:
    """Odd vs even rounds. (a) canonical correlations between users' axis scores in
    the two halves (vs. user-permuted null); (b) split-half correlation of each
    user's per-tag mean surprise (after removing the user's overall mean)."""
    from sklearn.cross_decomposition import CCA

    contests = np.sort(problems["contestId"].unique())
    half_of_contest = {c: i % 2 for i, c in enumerate(contests)}
    col_half = problems["contestId"].map(half_of_contest).to_numpy()
    SA, SB = S[:, col_half == 0], S[:, col_half == 1]
    # users must appear in both halves
    nA, nB = np.diff(SA.indptr), np.diff(SB.indptr)
    keep = (nA >= 10) & (nB >= 10)
    SA, SB = SA[keep], SB[keep]
    log.info("splithalf: %d users with >=10 obs in both halves; %d / %d problems", keep.sum(), SA.shape[1], SB.shape[1])

    UA, sA, _ = truncated_svd(SA, k, seed=seed)
    UB, sB, _ = truncated_svd(SB, k, seed=seed + 1)
    XA, XB = UA * sA, UB * sB
    rng = np.random.default_rng(seed)

    def canon(X, Y):
        cca = CCA(n_components=k, max_iter=1000).fit(X, Y)
        a, b = cca.transform(X, Y)
        return np.array([abs(np.corrcoef(a[:, i], b[:, i])[0, 1]) for i in range(k)])

    cc_real = canon(XA, XB)
    cc_null = canon(XA, XB[rng.permutation(len(XB))])
    # direct correlation of the top axes (sign-free)
    direct = np.abs(np.corrcoef(XA.T, XB.T)[:k, k:])  # k x k
    log.info("canonical correlations real: %s", np.round(cc_real, 3))
    log.info("canonical correlations null: %s", np.round(cc_null, 3))
    log.info("|corr| of axis-1 scores across halves: %.3f; best match per A-axis: %s", direct[0, 0], np.round(direct.max(1), 2))

    # (b) per-tag surprise profiles
    tags = {t: v for t, v in tag_sets(problems).items() if len(v) >= 60}
    rowsum = lambda M: np.asarray(M.sum(1)).ravel()
    def tag_profile(Sh, cols_h):
        Mh = Sh.copy(); Mh.data = np.ones_like(Mh.data)
        mean_user = rowsum(Sh) / np.maximum(rowsum(Mh), 1)
        prof, cnt = {}, {}
        col_pos = {c: i for i, c in enumerate(cols_h)}
        for t, v in tags.items():
            idx = [col_pos[c] for c in v if c in col_pos]
            if len(idx) < 20:
                continue
            sub = Sh[:, idx]; msub = Mh[:, idx]
            c = rowsum(msub)
            prof[t] = np.where(c > 0, rowsum(sub) / np.maximum(c, 1) - mean_user, np.nan)
            cnt[t] = c
        return prof, cnt
    colsA = np.flatnonzero(col_half == 0); colsB = np.flatnonzero(col_half == 1)
    pA, cA = tag_profile(SA, colsA); pB, cB = tag_profile(SB, colsB)
    rows = []
    for t in sorted(set(pA) & set(pB)):
        ok = (cA[t] >= 8) & (cB[t] >= 8)
        if ok.sum() < 200:
            continue
        a, b = pA[t][ok], pB[t][ok]
        r = float(np.corrcoef(a, b)[0, 1])
        r_null = float(np.corrcoef(a, rng.permutation(b))[0, 1])
        rows.append({"tag": t, "n_users": int(ok.sum()), "split_half_r": r, "null_r": r_null})
    tagdf = pd.DataFrame(rows).sort_values("split_half_r", ascending=False)
    log.info("per-tag split-half reliability:\n%s", tagdf.round(3).to_string(index=False))

    res = {"n_users": int(keep.sum()), "k": k, "canonical_corr_real": cc_real.tolist(), "canonical_corr_null": cc_null.tolist(),
           "axis1_abs_corr": float(direct[0, 0]), "best_match_abs_corr_per_axis": direct.max(1).tolist()}
    (out / "R_splithalf.json").write_text(json.dumps(res, indent=1))
    tagdf.to_csv(out / "R_splithalf_tags.csv", index=False)
    _plot_splithalf(cc_real, cc_null, tagdf, out / "R_splithalf.png")
    return res


def _plot_splithalf(cc_real, cc_null, tagdf, path):
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    x = np.arange(1, len(cc_real) + 1)
    axes[0].plot(x, cc_real, "o-", label="odd vs even rounds"); axes[0].plot(x, cc_null, "s--", color="0.5", label="users shuffled")
    axes[0].set_xlabel("canonical component"); axes[0].set_ylabel("canonical correlation"); axes[0].set_ylim(0, 1); axes[0].legend(); axes[0].grid(alpha=0.3)
    axes[0].set_title("Users' axis scores: are they the same trait in both halves?")
    axes[1].barh(tagdf["tag"], tagdf["split_half_r"], color="C0", label="real")
    axes[1].barh(tagdf["tag"], tagdf["null_r"], color="0.6", height=0.4, label="shuffled")
    axes[1].set_xlabel("split-half correlation of per-tag mean surprise"); axes[1].invert_yaxis(); axes[1].legend(); axes[1].grid(alpha=0.3, axis="x")
    axes[1].set_title("Is 'good at <tag> beyond rating' a stable trait?")
    fig.tight_layout(); fig.savefig(path, dpi=150); plt.close(fig)


# ----------------------------------------------------------------------- paramnull
def paramnull(S: sp.csr_matrix, k: int = 20, n_rep: int = 10, seed: int = 0, out=paths.OUT) -> pd.DataFrame:
    """Simulate the matrix under the Elo model itself: same mask, same p_ij, y ~ Bernoulli(p)."""
    rng = np.random.default_rng(seed)
    _, s_real, _ = truncated_svd(S, k, seed=seed)
    _, p = _p_from_s(S.data.astype(np.float64))
    spectra = np.empty((n_rep, len(s_real)))
    for b in range(n_rep):
        y = (rng.random(len(p)) < p).astype(np.float32)
        Sb = S.copy(); Sb.data = (y - p).astype(np.float32)
        _, sb, _ = truncated_svd(Sb, k, seed=seed + b + 1)
        spectra[b] = sb
        log.info("paramnull %d/%d top sv %.2f", b + 1, n_rep, sb[0])
    df = pd.DataFrame({"component": np.arange(1, k + 1), "sigma": s_real, "elo_null_max": spectra.max(0), "elo_null_mean": spectra.mean(0),
                       "ratio": s_real / spectra.max(0), "significant": s_real > spectra.max(0)})
    df.to_csv(out / "R_paramnull.csv", index=False)
    log.info("parametric Elo null: ratios %s", np.round(df["ratio"].to_numpy(), 2))
    perm = pd.read_csv(paths.OUT / "D1_spectrum.csv") if (paths.OUT / "D1_spectrum.csv").exists() else None
    _plot_paramnull(df, perm, out / "R_paramnull.png")
    return df


def _plot_paramnull(df, perm, path):
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.plot(df["component"], df["sigma"], "o-", color="C3", label="real")
    ax.plot(df["component"], df["elo_null_max"], "s--", color="C0", label="Elo-model simulation (max of reps)")
    if perm is not None:
        ax.plot(perm["component"], perm["null_max"], "^--", color="0.5", label="within-column permutation (max)")
    ax.set_xlabel("component"); ax.set_ylabel("singular value"); ax.legend(); ax.grid(alpha=0.3)
    ax.set_title("Two nulls for D1"); fig.tight_layout(); fig.savefig(path, dpi=150); plt.close(fig)


# ---------------------------------------------------------------------------- band
def band(S: sp.csr_matrix, users: pd.DataFrame, problems: pd.DataFrame, lo: int, hi: int, k: int = 15, n_perm: int = 10, min_obs: int = 300, seed: int = 0, out=paths.OUT) -> dict:
    """SVD + permutation null restricted to users whose mean rating is in [lo, hi)."""
    sel = ((users["mean_rating"] >= lo) & (users["mean_rating"] < hi)).to_numpy()
    Sb = S[sel]
    nobs = np.asarray((Sb != 0).sum(0)).ravel()
    pk = nobs >= min_obs
    Sb = Sb[:, pk]; pb = problems[pk].reset_index(drop=True); pb["col"] = np.arange(len(pb))
    log.info("band [%d,%d): %d users x %d problems, nnz %d", lo, hi, *Sb.shape, Sb.nnz)
    U, s, Vt = truncated_svd(Sb, k, seed=seed)
    null = null_spectra(Sb, k, n_perm, seed)
    sig = significant_components(s, null)
    tags = tag_sets(pb)
    rating = pb["rating"].to_numpy(float)
    rows = []
    for a in range(k):
        enr = tag_enrichment(Vt[a], tags)
        rows.append({"axis": a + 1, "sigma": s[a], "null_max": null.max(0)[a], "ratio": s[a] / null.max(0)[a], "significant": bool(sig[a]),
                     "corr_rating": float(np.corrcoef(Vt[a], rating)[0, 1]),
                     "plus_tags": ", ".join(f"{r.tag}({r.z:+.1f})" for r in enr[enr.z > 0].head(3).itertuples()),
                     "minus_tags": ", ".join(f"{r.tag}({r.z:+.1f})" for r in enr[enr.z < 0].tail(3)[::-1].itertuples())})
    df = pd.DataFrame(rows)
    log.info("band [%d,%d) axes:\n%s", lo, hi, df.round(2).to_string(index=False))
    df.to_csv(out / f"R_band_{lo}_{hi}.csv", index=False)
    return {"lo": lo, "hi": hi, "n_users": int(sel.sum()), "n_problems": int(pk.sum()), "n_significant": int(sig.sum()), "ratios": df["ratio"].round(3).tolist()}


# -------------------------------------------------------------------------- tagpred
def tagpred(problems: pd.DataFrame, svd_npz: Path = paths.SVD_NPZ, n_axes: int = 20, min_tag: int = 100, seed: int = 0, out=paths.OUT) -> pd.DataFrame:
    """5-fold CV AUC of logistic regression predicting each tag from (a) rating only,
    (b) axis coordinates only, (c) rating + axes; plus (b) with shuffled labels."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold, cross_val_score
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler

    z = np.load(svd_npz)
    X_axes = (z["Vt"][:n_axes] * z["s"][:n_axes, None]).T
    rating = problems["rating"].to_numpy(float)[:, None]
    X_rat = np.hstack([rating, rating ** 2])
    X_all = np.hstack([X_rat, X_axes])
    tags = {t: v for t, v in tag_sets(problems).items() if len(v) >= min_tag}
    rng = np.random.default_rng(seed)
    cv = StratifiedKFold(5, shuffle=True, random_state=seed)
    def auc(X, y):
        clf = make_pipeline(StandardScaler(), LogisticRegression(C=1.0, max_iter=2000))
        return float(cross_val_score(clf, X, y, cv=cv, scoring="roc_auc").mean())
    rows = []
    for t, idx in sorted(tags.items(), key=lambda kv: -len(kv[1])):
        y = np.zeros(len(problems), int); y[idx] = 1
        rows.append({"tag": t, "n": len(idx), "auc_rating": auc(X_rat, y), "auc_axes": auc(X_axes, y), "auc_rating_axes": auc(X_all, y),
                     "auc_axes_shuffled": auc(X_axes, rng.permutation(y))})
        log.info("  %-24s n=%4d  rating %.3f  axes %.3f  both %.3f  shuffled %.3f", t, len(idx), *[rows[-1][c] for c in ["auc_rating", "auc_axes", "auc_rating_axes", "auc_axes_shuffled"]])
    df = pd.DataFrame(rows)
    df["gain_over_rating"] = df["auc_rating_axes"] - df["auc_rating"]
    df.to_csv(out / "R_tagpred.csv", index=False)
    _plot_tagpred(df, out / "R_tagpred.png")
    return df


def _plot_tagpred(df, path):
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    d = df.sort_values("auc_rating_axes", ascending=False)
    fig, ax = plt.subplots(figsize=(9, 0.32 * len(d) + 1.5))
    y = np.arange(len(d))
    ax.scatter(d["auc_rating"], y, marker="|", s=200, color="0.4", label="rating only")
    ax.scatter(d["auc_axes"], y, marker="o", color="C0", label="20 axes only")
    ax.scatter(d["auc_rating_axes"], y, marker="D", color="C3", label="rating + axes")
    ax.scatter(d["auc_axes_shuffled"], y, marker="x", color="0.7", label="axes, shuffled labels")
    ax.set_yticks(y); ax.set_yticklabels(d["tag"], fontsize=8); ax.invert_yaxis(); ax.axvline(0.5, color="k", lw=0.5)
    ax.set_xlabel("5-fold CV AUC for predicting the tag"); ax.legend(fontsize=8, loc="lower right"); ax.grid(alpha=0.3, axis="x")
    ax.set_title("Do the hidden axes carry tag information beyond difficulty?")
    fig.tight_layout(); fig.savefig(path, dpi=150); plt.close(fig)


# ----------------------------------------------------------------------------- main
def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("what", nargs="+", choices=["heldout", "splithalf", "paramnull", "band", "tagpred", "all"])
    ap.add_argument("--n-perm", type=int, default=10)
    ap.add_argument("--n-rep", type=int, default=10)
    ap.add_argument("--bands", default="1000-1400,1400-1800,1800-2400")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(levelname)s %(message)s")
    paths.ensure_dirs()
    what = set(args.what)
    if "all" in what:
        what = {"heldout", "splithalf", "paramnull", "band", "tagpred"}

    S, M, users, problems = load_matrix()
    summary = {}
    if "heldout" in what:
        for mode in ("entries", "user_contest"):
            df = heldout(S, problems, mode=mode, seed=args.seed)
            summary[f"heldout_{mode}"] = df.round(4).to_dict("records")
    if "splithalf" in what:
        summary["splithalf"] = splithalf(S, problems, seed=args.seed)
    if "paramnull" in what:
        summary["paramnull_ratios"] = paramnull(S, n_rep=args.n_rep, seed=args.seed)["ratio"].round(3).tolist()
    if "band" in what:
        summary["bands"] = []
        for b in args.bands.split(","):
            lo, hi = (int(v) for v in b.split("-"))
            summary["bands"].append(band(S, users, problems, lo, hi, n_perm=args.n_perm, seed=args.seed))
    if "tagpred" in what:
        df = tagpred(problems, seed=args.seed)
        summary["tagpred"] = {"mean_auc_rating": float(df["auc_rating"].mean()), "mean_auc_axes": float(df["auc_axes"].mean()),
                              "mean_auc_rating_axes": float(df["auc_rating_axes"].mean()), "mean_auc_shuffled": float(df["auc_axes_shuffled"].mean())}
    (paths.OUT / "R_summary.json").write_text(json.dumps(summary, indent=1, default=float))
    log.info("robustness outputs written to %s (R_*)", paths.OUT)


if __name__ == "__main__":
    main()
