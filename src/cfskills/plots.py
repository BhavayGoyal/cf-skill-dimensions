"""Redraw every figure used in the report from the files in outputs/ and data/processed/.

    python -m cfskills.plots            # writes outputs/report_figs/*.pdf and *.png

Nothing here recomputes the analysis; it only reads results written by the other
modules (svd, cluster, lsh, robust, demo).
"""

from __future__ import annotations

import argparse
import json
import logging

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

from . import paths  # noqa: E402

log = logging.getLogger(__name__)

BLUE, ORANGE, GRAY, DARK, LIGHT = "#2F6DB5", "#D8672B", "#8A8F98", "#222831", "#E9ECF1"
SHORT = {"constructive algorithms": "constructive", "dfs and similar": "dfs", "data structures": "data structures",
         "divide and conquer": "divide & conquer", "meet-in-the-middle": "meet-in-middle", "suffix structures": "suffix structures",
         "number theory": "number theory", "binary search": "binary search", "graph matchings": "matchings"}
ALGO = {"dp", "data structures", "trees", "graphs", "dfs and similar", "binary search", "divide and conquer", "dsu"}
ADHOC = {"math", "constructive algorithms", "greedy", "number theory", "geometry"}

FIG = paths.OUT / "report_figs"


def _style() -> None:
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 8, "axes.titlesize": 8.5, "axes.titleweight": "bold", "axes.titlelocation": "left",
        "axes.labelsize": 8, "xtick.labelsize": 7.5, "ytick.labelsize": 7.5, "legend.fontsize": 7.5, "legend.frameon": False,
        "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": GRAY, "axes.labelcolor": DARK, "text.color": DARK,
        "xtick.color": DARK, "ytick.color": DARK, "axes.grid": True, "grid.color": LIGHT, "grid.linewidth": 0.7, "axes.axisbelow": True,
        "figure.dpi": 150, "savefig.dpi": 300, "pdf.fonttype": 42,
    })


def _save(fig, name: str) -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    for ext in ("pdf", "png"):
        fig.savefig(FIG / f"{name}.{ext}", bbox_inches="tight", pad_inches=0.03)
    plt.close(fig)
    log.info("wrote %s", FIG / name)


def _tag(t: str) -> str:
    return SHORT.get(t, t)


def _panel(ax, letter: str) -> None:
    ax.text(-0.02, 1.13, letter, transform=ax.transAxes, fontsize=10, fontweight="bold", va="bottom", ha="right")


# ------------------------------------------------------------------ pipeline
def fig_pipeline() -> None:
    fig, ax = plt.subplots(figsize=(7.1, 2.55))
    ax.set_xlim(0, 100); ax.set_ylim(0, 36); ax.axis("off"); ax.grid(False)

    def box(x, y, w, h, title, body, color, tag=None):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=1.2", fc="white", ec=color, lw=1.6))
        ax.text(x + w / 2, y + h - 2.1, title, ha="center", va="top", fontsize=8.2, fontweight="bold", color=color)
        ax.text(x + w / 2, y + h - 6.3, body, ha="center", va="top", fontsize=7.1, color=DARK, linespacing=1.35)
        if tag:
            ax.text(x + w - 0.8, y + 0.9, tag, ha="right", va="bottom", fontsize=7, fontweight="bold", color=color)

    def arrow(x0, y0, x1, y1):
        ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=9, lw=1.3, color=GRAY,
                                     connectionstyle="arc3,rad=0"))

    box(0.5, 21, 26, 14, "1  Codeforces API", "589 rounds, 36,519 users,\n3,773 problems\nwho solved what, in contest", GRAY)
    box(37, 21, 28, 14, "2  Surprise matrix  S", "s = solved − Elo expectation\n+ : solved something hard\n− : missed something easy", BLUE)
    box(74, 21, 25, 14, "3  Any structure?", "SVD of S vs. shuffled\nnulls, held-out prediction,\nsplit-half reliability", BLUE, "D1")
    box(0.5, 0.5, 26, 15.5, "4  What are the axes?", "problems at each end of an\naxis and their tags;\ncorrelation with difficulty", ORANGE, "D2")
    box(37, 0.5, 28, 15.5, "5  Do tags match?", "cluster problems by user\nbehaviour, compare with the\nsetters' tags vs. random", ORANGE, "D3")
    box(74, 0.5, 25, 15.5, "6  Skill twins", "MinHash + LSH on hit/miss\nsets; fingerprint and twins\nfor any handle", ORANGE, "D4 D5")
    arrow(27.2, 28, 36.4, 28); arrow(65.7, 28, 73.4, 28)
    ax.plot([86.5, 86.5], [20.4, 18.3], color=GRAY, lw=1.3, solid_capstyle="butt")
    ax.plot([13.5, 86.5], [18.3, 18.3], color=GRAY, lw=1.3, solid_capstyle="butt")
    for xx in (13.5, 51, 86.5):
        arrow(xx, 18.3, xx, 16.9)
    _save(fig, "fig_pipeline")


# ------------------------------------------------------------------ evidence
def fig_evidence() -> None:
    d1 = pd.read_csv(paths.OUT / "D1_spectrum.csv")
    pn = pd.read_csv(paths.OUT / "R_paramnull.csv")
    ho = pd.read_csv(paths.OUT / "R_heldout_entries.csv")
    sh = json.loads((paths.OUT / "R_splithalf.json").read_text())

    fig, axes = plt.subplots(1, 3, figsize=(7.1, 2.25), gridspec_kw={"wspace": 0.42})
    ax = axes[0]
    ax.plot(d1["component"], d1["sigma"], "-o", ms=3.2, color=ORANGE, lw=1.6, label="real matrix")
    ax.plot(d1["component"], d1["null_max"], "--", color=GRAY, lw=1.3, label="shuffled columns")
    ax.plot(pn["component"], pn["elo_null_max"], ":", color=BLUE, lw=1.6, label="Elo-only simulation")
    ax.legend(loc="upper right", handlelength=1.8)
    ax.set_xlim(0.5, 20.5); ax.set_ylim(0, 160)
    ax.set_xlabel("component"); ax.set_ylabel("singular value")
    ax.set_title("Real spectrum clears\nboth nulls"); _panel(ax, "a")

    ax = axes[1]
    b = ho[ho["model"] == "Elo + biases + rank-k"]
    base = ho[ho["model"] == "Elo + problem + user bias"]["logloss_gain_vs_elo_pct"].iloc[0]
    ax.axhline(base, color=GRAY, ls="--", lw=1.2)
    ax.text(1.05, base - 0.25, "Elo + user/problem\nbias only", color=GRAY, fontsize=7, va="top")
    ax.plot(b["k"], b["logloss_gain_vs_elo_pct"], "-o", ms=3.5, color=ORANGE, lw=1.6)
    ax.set_xscale("log"); ax.set_xticks([1, 3, 10, 40]); ax.set_xticklabels(["1", "3", "10", "40"])
    ax.set_ylim(3, 8.4)
    ax.set_xlabel("rank k added"); ax.set_ylabel("log-loss gain over Elo (%)")
    ax.set_title("Structure predicts\nhidden solves"); _panel(ax, "b")

    ax = axes[2]
    x = np.arange(1, 11)
    ax.bar(x, sh["canonical_corr_real"], color=BLUE, width=0.68, label="real")
    ax.plot(x, sh["canonical_corr_null"], "-", color=GRAY, lw=1.4, marker="s", ms=2.5, label="users shuffled")
    ax.legend(loc="upper right", handlelength=1.4)
    ax.set_xticks([1, 3, 5, 7, 10]); ax.set_ylim(0, 1.25); ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xlabel("dimension"); ax.set_ylabel("odd vs even rounds: correlation")
    ax.set_title("About six dimensions\nreproduce"); _panel(ax, "c")
    _save(fig, "fig_evidence")


# ----------------------------------------------------------------------- axes
def _enrichment(Vt_row: np.ndarray, problems: pd.DataFrame) -> pd.DataFrame:
    from .svd import tag_enrichment, tag_sets
    return tag_enrichment(Vt_row, tag_sets(problems))


def _bars(ax, enr: pd.DataFrame, n: int, title: str, plus_label: str, minus_label: str) -> None:
    top = enr.head(n); bot = enr.tail(n)
    d = pd.concat([top, bot]).iloc[::-1]
    colors = [BLUE if z > 0 else ORANGE for z in d["z"]]
    ax.barh([_tag(t) for t in d["tag"]], d["z"], color=colors, height=0.68)
    ax.axvline(0, color=DARK, lw=0.8)
    ax.set_xlabel("tag enrichment (z)"); ax.set_title(title)
    lim = max(abs(d["z"]).max() * 1.12, 3)
    ax.set_xlim(-lim, lim); ax.grid(axis="y", visible=False)
    ax.text(1.0, -0.27, plus_label + " →", transform=ax.transAxes, ha="right", color=BLUE, fontsize=6.8, fontweight="bold")
    ax.text(0.0, -0.27, "← " + minus_label, transform=ax.transAxes, ha="left", color=ORANGE, fontsize=7, fontweight="bold")


def fig_axes() -> None:
    z = np.load(paths.OUT / "svd.npz")
    Vt = z["Vt"]
    problems = pd.read_csv(paths.PROCESSED / "problems.csv", keep_default_na=False)
    rating = problems["rating"].to_numpy(float)
    # orient axis 1 so that "+" is the easy/implementation end and axis 8 so that "+" is ad-hoc (math/constructive)
    v1 = Vt[0].copy(); v8 = Vt[7].copy()
    e1 = _enrichment(v1, problems); e8 = _enrichment(v8, problems)
    if e1.set_index("tag").loc["dfs and similar", "z"] > 0: v1, e1 = -v1, e1.assign(z=-e1["z"]).sort_values("z", ascending=False).reset_index(drop=True)
    if e8.set_index("tag").loc["math", "z"] < 0: v8, e8 = -v8, e8.assign(z=-e8["z"]).sort_values("z", ascending=False).reset_index(drop=True)

    fig, axes = plt.subplots(1, 3, figsize=(7.1, 2.75), gridspec_kw={"wspace": 0.72, "width_ratios": [1, 1, 1.1]})
    _bars(axes[0], e1, 4, "Axis 1: difficulty slope", "easy", "hard"); _panel(axes[0], "a")
    _bars(axes[1], e8, 4, "Axis 8: ad-hoc vs. algo.", "ad-hoc", "algo."); _panel(axes[1], "b")

    ax = axes[2]
    sm = pd.read_csv(paths.OUT / "D2_axis_summary.csv").head(12)
    ax.bar(sm["axis"], sm["corr_rating"], color=[ORANGE if a == 1 else BLUE for a in sm["axis"]], width=0.7)
    ax.axhline(0, color=DARK, lw=0.8)
    ax.set_xticks([1, 3, 5, 7, 9, 12]); ax.set_ylim(-0.55, 0.3)
    ax.set_xlabel("skill axis"); ax.set_ylabel("corr. of loading with problem rating")
    ax.set_title("Only axis 1 tracks difficulty"); ax.grid(axis="x", visible=False)
    _panel(ax, "c")
    _save(fig, "fig_axes")


# ----------------------------------------------------------------------- tags
def fig_tags() -> None:
    runs = [("k-means\nk=8", "D3_agreement.json"), ("spectral\nk=8", "D3_agreement_spectral.json"), ("k-means\nk=2", "D3_agreement_obs1000.json")]
    tp = pd.read_csv(paths.OUT / "R_tagpred.csv")

    fig, axes = plt.subplots(1, 2, figsize=(7.1, 2.9), gridspec_kw={"width_ratios": [0.8, 1.35], "wspace": 0.55})
    ax = axes[0]
    x = np.arange(len(runs)); w = 0.36
    real = []; rnd = []; sd = []
    for _, f in runs:
        j = json.loads((paths.OUT / f).read_text())
        real.append(j["agreement"]); rnd.append(j["random_mean"]); sd.append(j["random_std"])
    ax.bar(x - w / 2, rnd, w, yerr=np.array(sd) * 2, color=GRAY, label="random partitions", error_kw={"lw": 0.8})
    ax.bar(x + w / 2, real, w, color=BLUE, label="data-driven clusters")
    for xi, r, q in zip(x, real, rnd):
        ax.text(xi + w / 2, r + 0.006, f"+{(r - q) * 100:.1f}", ha="center", fontsize=7, color=DARK, fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels([r for r, _ in runs]); ax.set_ylabel("agreement with tags\n(mean best-match Jaccard)")
    ax.set_ylim(0, 0.37); ax.legend(loc="upper right"); ax.grid(axis="x", visible=False)
    ax.set_title("Clusters barely beat random"); _panel(ax, "a")
    ax.set_xlabel("bold numbers: Jaccard points above random", fontsize=7, color=GRAY)

    ax = axes[1]
    d = tp.assign(gain=tp["auc_rating_axes"] - tp["auc_rating"]).sort_values("gain", ascending=True)
    y = np.arange(len(d))
    for yi, (a, b) in enumerate(zip(d["auc_rating"], d["auc_rating_axes"])):
        ax.plot([a, b], [yi, yi], color=BLUE if b - a > 0.02 else GRAY, lw=2.2 if b - a > 0.02 else 1.2, solid_capstyle="round")
    ax.scatter(d["auc_rating"], y, s=14, color="white", ec=DARK, lw=0.9, zorder=3, label="difficulty only")
    ax.scatter(d["auc_rating_axes"], y, s=14, color=BLUE, zorder=3, label="difficulty + hidden axes")
    ax.set_yticks(y); ax.set_yticklabels([_tag(t) for t in d["tag"]], fontsize=6.8)
    ax.set_xlabel("cross-validated AUC for predicting the tag"); ax.axvline(0.5, color=DARK, lw=0.6)
    ax.legend(loc="upper center", bbox_to_anchor=(0.4, -0.17), ncol=2); ax.grid(axis="y", visible=False)
    ax.set_title("Axes add most for ad-hoc tags"); _panel(ax, "b")
    _save(fig, "fig_tags")


# ---------------------------------------------------------------------- twins
def fig_twins() -> None:
    ev = pd.read_csv(paths.OUT / "D4_lsh_eval.csv").sort_values("threshold")
    nn = json.loads((paths.OUT / "D4_neighbour_stats.json").read_text())
    full = json.loads((paths.OUT / "D4_full_run.json").read_text())

    fig, axes = plt.subplots(1, 2, figsize=(7.1, 2.3), gridspec_kw={"width_ratios": [1.25, 1], "wspace": 0.4})
    ax = axes[0]
    ax.axvspan(nn["top10_jaccard_median"], nn["top1_jaccard_median"], color=BLUE, alpha=0.14, lw=0)
    ax.text(0.0705, 0.2, "real\nneighbours", color=BLUE, fontsize=7, ha="left", va="center", fontweight="bold")
    ax.plot(ev["threshold"], ev["recall@10"], "-o", color=ORANGE, ms=4, lw=1.6)
    for _, r in ev.iterrows():
        if r["bands"] in (128, 32) :
            ax.annotate(f"{int(r['bands'])}×{int(r['rows'])}", (r["threshold"], r["recall@10"]), textcoords="offset points",
                        xytext=(6, 5), fontsize=7, color=DARK)
    ax.set_xscale("log"); ax.set_xticks([0.1, 0.2, 0.4, 0.65]); ax.set_xticklabels(["0.1", "0.2", "0.4", "0.65"])
    ax.minorticks_off()
    ax.set_xlabel("LSH similarity threshold"); ax.set_ylabel("recall@10 (3,000 users)"); ax.set_ylim(-0.03, 0.8)
    ax.set_title("The planned 32×4 setting looks\nfor similarity that does not exist"); _panel(ax, "a")

    ax = axes[1]
    vals = [full["time_exact_s"], full["time_lsh_s"]]
    ax.barh(["exact brute force", "MinHash LSH"], vals, color=[GRAY, ORANGE], height=0.55)
    for yi, v in enumerate(vals):
        ax.text(v + 1, yi, f"{v:.0f} s", va="center", fontsize=7.5)
    ax.set_xlim(0, 56); ax.set_xlabel("wall-clock, 35,811 users"); ax.grid(axis="y", visible=False)
    ax.set_title("Full run: 1.4% of pairs,\nrecall 0.84, but slower"); _panel(ax, "b")
    _save(fig, "fig_twins")


# ---------------------------------------------------------------- fingerprints
def fig_fingerprints() -> None:
    from .demo import Explorer
    ex = Explorer(n_axes=8)
    shown = [f"{a}" for a in range(1, 9)]

    def z(handle):
        fp = ex.query(handle, 3)
        return np.array([a["z"] for a in fp.axes]), fp

    pool = ["at2c", "AHMADUL", "amirhozaifa", "Sabbir.Hasan", "cleanser"]
    zs = {h: z(h)[0] for h in pool if h in ex.uid}
    # the three same-rating users whose profiles differ most
    best, best_d = None, -1
    import itertools
    for trio in itertools.combinations(zs, 3):
        dsum = sum(np.linalg.norm(zs[a] - zs[b]) for a, b in itertools.combinations(trio, 2))
        if dsum > best_d:
            best, best_d = trio, dsum
    pro = ["tourist", "jiangly"]
    fig, axes = plt.subplots(1, 2, figsize=(7.1, 2.4), sharey=True, gridspec_kw={"wspace": 0.12})
    x = np.arange(1, 9)
    cols = [BLUE, ORANGE, GRAY]
    for ax, names, ttl, letter in [(axes[0], pro, "Two top-rated users look alike", "a"), (axes[1], list(best), "Same rating (~1600), different profiles", "b")]:
        for i, h in enumerate(names):
            zz, fp = z(h)
            c = [BLUE, ORANGE, GRAY][i]
            ax.plot(x, zz, "-o", color=c, ms=3.5, lw=1.5, label=f"{h} ({fp.rating})")
        ax.axhline(0, color=DARK, lw=0.7)
        ax.set_xticks(x); ax.set_ylim(-4.9, 4.9); ax.set_xlabel("skill axis"); ax.set_title(ttl); ax.legend(loc="lower right" if letter == "a" else "lower left", ncol=1, handlelength=1.2)
        _panel(ax, letter)
    axes[0].set_ylabel("score vs. all users (z)")
    _save(fig, "fig_fingerprints")
    log.info("fingerprint trio: %s", best)


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("only", nargs="*", help="subset: pipeline evidence axes tags twins fingerprints")
    args = ap.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    _style()
    funcs = {"pipeline": fig_pipeline, "evidence": fig_evidence, "axes": fig_axes, "tags": fig_tags, "twins": fig_twins,
             "fingerprints": fig_fingerprints}
    for name in (args.only or funcs):
        funcs[name]()


if __name__ == "__main__":
    main()
