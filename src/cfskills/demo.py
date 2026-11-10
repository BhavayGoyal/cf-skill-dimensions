"""Step 6 (D5) - handle -> skill fingerprint + skill twins.

    python -m cfskills.demo tourist
    python -m cfskills.demo tourist --json

Fingerprint: the user's score on each significant axis (row of U Sigma),
reported as a z-score across all users together with the percentile. Twins:
top-k users by exact Jaccard of hit/miss token sets, read from
outputs/twins.json.gz if present, otherwise computed on the fly.
"""

from __future__ import annotations

import argparse
import json
import logging
from dataclasses import asdict, dataclass, field

import numpy as np
import pandas as pd

from . import paths
from .lsh import build_tokens, exact_jaccard_pairs, load_twins
from .matrix import load as load_matrix

log = logging.getLogger(__name__)


@dataclass
class Fingerprint:
    handle: str
    rating: int
    n_participations: int
    axes: list[dict] = field(default_factory=list)   # [{axis, score, z, percentile, plus_tags, minus_tags}]
    twins: list[dict] = field(default_factory=list)  # [{handle, jaccard, rating}]


class Explorer:
    """Loads everything once; answers queries for many handles."""

    def __init__(self, n_axes: int | None = None):
        self.S, self.M, self.users, self.problems = load_matrix()
        z = np.load(paths.SVD_NPZ)
        self.U, self.s, self.Vt, self.sig = z["U"], z["s"], z["Vt"], z["sig"]
        self.axes = np.flatnonzero(self.sig) if n_axes is None else np.arange(n_axes)
        if len(self.axes) == 0:
            self.axes = np.arange(min(3, len(self.s)))
        self.scores = self.U[:, self.axes] * self.s[self.axes]          # users x axes
        self.mu, self.sd = self.scores.mean(0), self.scores.std(0) + 1e-12
        self.uid = {h: i for i, h in enumerate(self.users["handle"])}
        self.twins = load_twins()["twins"] if paths.TWINS_JSON.exists() else None
        self.X, _ = build_tokens(self.S)
        self._axis_tags = self._describe_axes()

    def _describe_axes(self, top: int = 3) -> dict[int, tuple[str, str]]:
        from .svd import tag_enrichment, tag_sets
        tags = tag_sets(self.problems)
        out = {}
        for k in self.axes:
            enr = tag_enrichment(self.Vt[k], tags)
            if enr.empty:
                out[k] = ("", "")
                continue
            out[k] = (", ".join(enr[enr.z > 0].head(top)["tag"]) or "-",
                      ", ".join(enr[enr.z < 0].tail(top)["tag"][::-1]) or "-")
        return out

    def _twins_brute(self, i: int, k: int) -> list[tuple[int, float]]:
        n = self.X.shape[0]
        pairs = np.column_stack([np.full(n, i), np.arange(n)])
        jac = exact_jaccard_pairs(self.X, pairs)
        jac[i] = -1
        idx = np.argsort(-jac)[:k]
        return [(int(j), float(jac[j])) for j in idx if jac[j] > 0]

    def query(self, handle: str, k: int = 10) -> Fingerprint:
        i = self.uid.get(handle)
        if i is None:
            # case-insensitive fallback
            low = {h.lower(): j for h, j in self.uid.items()}
            i = low.get(handle.lower())
        if i is None:
            raise KeyError(f"{handle!r} is not in the matrix (needs enough rated participations in the sampled rounds)")
        row = self.users.iloc[i]
        fp = Fingerprint(handle=row["handle"], rating=int(row["last_rating"]), n_participations=int(row["n_participations"]))
        zs = (self.scores[i] - self.mu) / self.sd
        for a, (k_ax, zval) in enumerate(zip(self.axes, zs)):
            pct = float((self.scores[:, a] <= self.scores[i, a]).mean() * 100)
            plus, minus = self._axis_tags[k_ax]
            fp.axes.append({"axis": int(k_ax + 1), "score": float(self.scores[i, a]), "z": float(zval), "percentile": pct,
                            "plus_tags": plus, "minus_tags": minus})
        if self.twins is not None and row["handle"] in self.twins:
            tw = [(self.uid[h], j) for h, j in self.twins[row["handle"]][:k]]
        else:
            tw = self._twins_brute(i, k)
        for j, jac in tw:
            u = self.users.iloc[j]
            fp.twins.append({"handle": u["handle"], "jaccard": round(float(jac), 3), "rating": int(u["last_rating"])})
        return fp


def format_text(fp: Fingerprint) -> str:
    lines = [f"{fp.handle}  rating {fp.rating}  ({fp.n_participations} rated rounds in sample)", "", "Skill fingerprint (z-score across users, percentile):"]
    for a in fp.axes:
        bar = "#" * int(min(20, abs(a["z"]) * 5))
        side = f"-> {a['plus_tags']}" if a["z"] >= 0 else f"-> {a['minus_tags']}"
        lines.append(f"  axis {a['axis']:>2}: {a['z']:+.2f}  p{a['percentile']:5.1f}  {bar:<20} {side}")
    lines += ["", "Skill twins (Jaccard of hit/miss sets):"]
    for t in fp.twins:
        lines.append(f"  {t['handle']:<24} J={t['jaccard']:.3f}  rating {t['rating']}")
    if not fp.twins:
        lines.append("  (none above threshold)")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("handles", nargs="+")
    ap.add_argument("-k", type=int, default=10)
    ap.add_argument("--n-axes", type=int, default=None)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    ex = Explorer(args.n_axes)
    for h in args.handles:
        try:
            fp = ex.query(h, args.k)
        except KeyError as exc:
            print(exc)
            continue
        print(json.dumps(asdict(fp), indent=1) if args.json else format_text(fp))
        print()


if __name__ == "__main__":
    main()
