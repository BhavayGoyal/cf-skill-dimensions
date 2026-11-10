"""Central place for file locations. Override roots with env vars
CFSKILLS_DATA and CFSKILLS_OUT."""

from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = Path(os.environ.get("CFSKILLS_DATA", ROOT / "data"))
OUT = Path(os.environ.get("CFSKILLS_OUT", ROOT / "outputs"))

RAW = DATA / "raw"
RAW_CONTESTS = RAW / "contests"          # one gz-json per contest
PROBLEMS_JSON = RAW / "problems.json.gz"  # problemset.problems
CONTEST_LIST_JSON = RAW / "contest_list.json.gz"
MANIFEST = RAW / "manifest.json"

PROCESSED = DATA / "processed"
S_NPZ = PROCESSED / "S.npz"               # surprise matrix (CSR, float32)
M_NPZ = PROCESSED / "M.npz"               # observed mask (CSR, int8)
USERS_CSV = PROCESSED / "users.csv"
PROBLEMS_CSV = PROCESSED / "problems.csv"

SVD_NPZ = OUT / "svd.npz"
TWINS_JSON = OUT / "twins.json.gz"


def ensure_dirs() -> None:
    for p in (RAW_CONTESTS, PROCESSED, OUT):
        p.mkdir(parents=True, exist_ok=True)
