"""Step 2 - build the users x problems *surprise* matrix S.

For user i (pre-contest rating R_i) and problem j (difficulty r_j):

    p_ij = 1 / (1 + 10 ** ((r_j - R_i) / 400))      Elo expected solve prob.
    s_ij = y_ij - p_ij                               surprise (y = solved in-contest)

Pairs the user never faced are 0 ("no evidence"). We also store the observed
mask M so later steps can tell "unobserved" from "s happened to be ~0".

Because y in {0,1} and p in (0,1), p is recoverable from s:
    s > 0  =>  y = 1, p = 1 - s
    s < 0  =>  y = 0, p = -s

Writes data/processed/{S.npz, M.npz, users.csv, problems.csv}.
"""

from __future__ import annotations

import argparse
import logging
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.sparse as sp
from tqdm import tqdm

from . import paths
from .fetch import load_gz

log = logging.getLogger(__name__)


def elo_prob(user_rating: np.ndarray | float, problem_rating: np.ndarray | float) -> np.ndarray:
    """Elo expected solve probability."""
    return 1.0 / (1.0 + 10.0 ** ((np.asarray(problem_rating, float) - np.asarray(user_rating, float)) / 400.0))


def surprise(solved: np.ndarray, user_rating: np.ndarray, problem_rating: np.ndarray) -> np.ndarray:
    return np.asarray(solved, float) - elo_prob(user_rating, problem_rating)


def load_problem_meta(problems_json: Path = paths.PROBLEMS_JSON) -> dict[tuple[int, str], dict]:
    """(contestId, index) -> {rating, tags, name}; only problems with a rating."""
    data = load_gz(problems_json)
    meta = {}
    for p in data["problems"]:
        if "rating" not in p or "contestId" not in p:
            continue
        meta[(p["contestId"], p["index"])] = {
            "rating": int(p["rating"]),
            "tags": list(p.get("tags", [])),
            "name": p.get("name", ""),
        }
    return meta


def iter_contest_files(raw_dir: Path = paths.RAW_CONTESTS):
    for f in sorted(raw_dir.glob("*.json.gz"), key=lambda f: int(f.stem.split(".")[0])):
        yield load_gz(f)


def build(
    min_participations: int = 40,
    raw_dir: Path = paths.RAW_CONTESTS,
    problems_json: Path = paths.PROBLEMS_JSON,
    min_old_rating: int = 1,
):
    """Return (S, M, users_df, problems_df)."""
    meta = load_problem_meta(problems_json)
    contests = list(iter_contest_files(raw_dir))
    log.info("%d contests, %d rated problems in problemset", len(contests), len(meta))

    # pass 1: how often does each handle appear as a rated official contestant?
    counts: Counter[str] = Counter()
    last_rating: dict[str, tuple[int, int]] = {}  # handle -> (startTime, oldRating)
    for c in contests:
        old = c["old_rating"]
        t = c["contest"].get("startTimeSeconds") or 0
        for handle, _ in c["rows"]:
            r = old.get(handle)
            if r is None or r < min_old_rating:
                continue
            counts[handle] += 1
            if handle not in last_rating or t > last_rating[handle][0]:
                last_rating[handle] = (t, r)
    handles = sorted(h for h, n in counts.items() if n >= min_participations)
    uid = {h: i for i, h in enumerate(handles)}
    log.info("%d users with >= %d participations (of %d rated participants)", len(handles), min_participations, len(counts))

    # pass 2: assign columns and fill the matrix
    prob_rows: list[dict] = []
    pid: dict[tuple[int, str], int] = {}
    rows_i, cols_j, vals_s = [], [], []
    rating_sum_arr = np.zeros(len(handles), dtype=float)

    for c in tqdm(contests, unit="contest", disable=len(contests) < 50):
        cid = c["contest"]["id"]
        old = c["old_rating"]
        # columns for this contest's rated problems
        col_of_local: dict[int, int] = {}
        prating: dict[int, int] = {}
        for local_j, p in enumerate(c["problems"]):
            m = meta.get((cid, p["index"]))
            if m is None:
                continue
            key = (cid, p["index"])
            if key not in pid:
                pid[key] = len(prob_rows)
                prob_rows.append({
                    "col": pid[key], "contestId": cid, "index": p["index"], "name": m["name"],
                    "rating": m["rating"], "tags": ";".join(m["tags"]),
                    "contest_name": c["contest"]["name"],
                })
            col_of_local[local_j] = pid[key]
            prating[local_j] = m["rating"]
        if not col_of_local:
            continue
        local_js = np.array(sorted(col_of_local), dtype=np.int64)
        cols = np.array([col_of_local[j] for j in local_js], dtype=np.int64)
        prs = np.array([prating[j] for j in local_js], dtype=float)

        sel = [(uid[h], old[h], solved) for h, solved in c["rows"]
               if h in uid and old.get(h) is not None and old[h] >= min_old_rating]
        if not sel:
            continue
        ids = np.array([t[0] for t in sel], dtype=np.int64)
        Rs = np.array([t[1] for t in sel], dtype=float)
        Y = np.zeros((len(sel), len(c["problems"])), dtype=bool)
        for r, (_, _, solved) in enumerate(sel):
            Y[r, solved] = True
        Sblk = surprise(Y[:, local_js], Rs[:, None], prs[None, :])   # rows x contest problems
        rows_i.append(np.repeat(ids, len(cols)))
        cols_j.append(np.tile(cols, len(sel)))
        vals_s.append(Sblk.ravel().astype(np.float32))
        rating_sum_arr[ids] += Rs

    I = np.concatenate(rows_i)
    J = np.concatenate(cols_j)
    V = np.concatenate(vals_s)
    n_u, n_p = len(handles), len(prob_rows)
    S = sp.csr_matrix((V, (I, J)), shape=(n_u, n_p), dtype=np.float32)
    M = sp.csr_matrix((np.ones(len(V), dtype=np.int8), (I, J)), shape=(n_u, n_p))
    S.sum_duplicates(); M.sum_duplicates()
    M.data[:] = 1

    users = pd.DataFrame({
        "uid": np.arange(n_u),
        "handle": handles,
        "n_participations": [counts[h] for h in handles],
        "last_rating": [last_rating[h][1] for h in handles],
        "mean_rating": rating_sum_arr / np.array([counts[h] for h in handles], dtype=float),
    })
    problems = pd.DataFrame(prob_rows)
    log.info("S: %d users x %d problems, %d observed entries (density %.4f)", n_u, n_p, S.nnz, S.nnz / (n_u * n_p))
    return S, M, users, problems


def save(S, M, users, problems, out_dir: Path = paths.PROCESSED) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    sp.save_npz(out_dir / "S.npz", S)
    sp.save_npz(out_dir / "M.npz", M)
    users.to_csv(out_dir / "users.csv", index=False)
    problems.to_csv(out_dir / "problems.csv", index=False)


def load(processed_dir: Path = paths.PROCESSED):
    S = sp.load_npz(processed_dir / "S.npz").tocsr()
    M = sp.load_npz(processed_dir / "M.npz").tocsr()
    users = pd.read_csv(processed_dir / "users.csv")
    problems = pd.read_csv(processed_dir / "problems.csv", keep_default_na=False)
    return S, M, users, problems


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--min-participations", type=int, default=40)
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(levelname)s %(message)s")

    S, M, users, problems = build(min_participations=args.min_participations)
    save(S, M, users, problems)
    log.info("saved to %s", paths.PROCESSED)
    # a few sanity numbers for the report
    obs = S.data
    log.info("mean surprise %.4f (should be ~0 if ratings are calibrated), std %.3f", obs.mean(), obs.std())
    log.info("fraction solved among observed: %.3f", (obs > 0).mean())


if __name__ == "__main__":
    main()
