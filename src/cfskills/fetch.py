"""Step 1 - pull everything we need from the Codeforces API and cache to disk.

Writes
    data/raw/problems.json.gz        problemset.problems (ratings + tags)
    data/raw/contest_list.json.gz    contest.list
    data/raw/contests/<id>.json.gz   slim standings + pre-contest ratings
    data/raw/manifest.json           which contests were fetched / skipped and why

The per-contest file is deliberately small: we keep, for each official
contestant, the handle and the list of problem indices solved in-contest, plus
the map handle -> rating before the round. Re-running is resumable: contests
that already have a file are skipped.

Usage
    python -m cfskills.fetch                       # ~600 rounds, overnight
    python -m cfskills.fetch --max-contests 25     # quick smoke test
"""

from __future__ import annotations

import argparse
import gzip
import json
import logging
import re
import time
from pathlib import Path
from typing import Iterable

from tqdm import tqdm

from . import paths
from .api import CFClient, CFError

log = logging.getLogger(__name__)

# Individual, rated rounds. Everything else (team rounds, April Fools, mirrors,
# marathons, ...) is excluded. Unrated rounds are also dropped later because
# contest.ratingChanges fails for them.
DEFAULT_INCLUDE = r"(Codeforces Round|Educational Codeforces Round|Codeforces Global Round|Div\. ?[1-4])"
DEFAULT_EXCLUDE = (
    r"(Team|Kotlin|April Fools|Unrated|Mirror|Technocup|VK Cup|Marathon|Testing|Trial|"
    r"Olympiad|School|ICPC|Qualification|Elimination|Onsite|Bubble)"
)


def dump_gz(obj, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as fh:
        json.dump(obj, fh, separators=(",", ":"))


def load_gz(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        return json.load(fh)


def select_contests(
    contests: Iterable[dict],
    n: int,
    min_age_days: float,
    include: str = DEFAULT_INCLUDE,
    exclude: str = DEFAULT_EXCLUDE,
    now: float | None = None,
) -> list[dict]:
    """Most recent ``n`` finished individual rounds at least ``min_age_days`` old."""
    now = time.time() if now is None else now
    inc = re.compile(include, re.I)
    exc = re.compile(exclude, re.I)
    out = []
    for c in contests:
        if c.get("phase") != "FINISHED":
            continue
        start = c.get("startTimeSeconds")
        if start is None or (now - start) < min_age_days * 86400:
            continue
        name = c.get("name", "")
        if not inc.search(name) or exc.search(name):
            continue
        out.append(c)
    out.sort(key=lambda c: c["startTimeSeconds"], reverse=True)
    return out[:n]


def slim_standings(standings: dict) -> dict:
    """Keep only what the pipeline needs from a contest.standings payload."""
    problems = [{"index": p["index"], "name": p.get("name", "")} for p in standings["problems"]]
    rows = []
    n_team_rows = 0
    for row in standings["rows"]:
        party = row["party"]
        if party.get("participantType") != "CONTESTANT":
            continue
        members = party.get("members", [])
        if len(members) != 1:
            n_team_rows += 1
            continue
        handle = members[0]["handle"]
        solved = [j for j, pr in enumerate(row["problemResults"]) if pr.get("points", 0) > 0]
        rows.append([handle, solved])
    return {"problems": problems, "rows": rows, "n_team_rows": n_team_rows}


def fetch_contest(client: CFClient, contest: dict, out_path: Path) -> str:
    """Fetch one contest. Returns a status string for the manifest."""
    cid = contest["id"]
    try:
        changes = client.contest_rating_changes(cid)
    except CFError as exc:
        return f"skip: ratingChanges failed ({exc})"
    if not changes:
        return "skip: no rating changes (unrated?)"
    old_rating = {ch["handle"]: ch["oldRating"] for ch in changes}

    standings = client.contest_standings(cid)
    slim = slim_standings(standings)
    if slim["n_team_rows"] > len(slim["rows"]):
        return "skip: team contest"
    payload = {
        "contest": {
            "id": cid,
            "name": contest.get("name", ""),
            "type": contest.get("type", ""),
            "startTimeSeconds": contest.get("startTimeSeconds"),
            "durationSeconds": contest.get("durationSeconds"),
        },
        "problems": slim["problems"],
        "rows": slim["rows"],
        "old_rating": old_rating,
    }
    dump_gz(payload, out_path)
    return f"ok: {len(slim['rows'])} rows, {len(slim['problems'])} problems"


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--max-contests", type=int, default=600)
    ap.add_argument("--min-age-days", type=float, default=90, help="skip rounds younger than this (ratings unsettled)")
    ap.add_argument("--include", default=DEFAULT_INCLUDE)
    ap.add_argument("--exclude", default=DEFAULT_EXCLUDE)
    ap.add_argument("--min-interval", type=float, default=2.0, help="seconds between API calls")
    ap.add_argument("--refresh-problems", action="store_true", help="re-download problemset.problems")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(levelname)s %(message)s")
    paths.ensure_dirs()
    client = CFClient(min_interval=args.min_interval)

    if args.refresh_problems or not paths.PROBLEMS_JSON.exists():
        log.info("fetching problemset.problems ...")
        dump_gz(client.problemset_problems(), paths.PROBLEMS_JSON)

    log.info("fetching contest.list ...")
    contests = client.contest_list()
    dump_gz(contests, paths.CONTEST_LIST_JSON)
    selected = select_contests(contests, args.max_contests, args.min_age_days, args.include, args.exclude)
    log.info("selected %d contests (%s .. %s)", len(selected), selected[-1]["name"] if selected else "-", selected[0]["name"] if selected else "-")

    manifest = json.loads(paths.MANIFEST.read_text()) if paths.MANIFEST.exists() else {}
    todo = [c for c in selected if not (paths.RAW_CONTESTS / f"{c['id']}.json.gz").exists()
            and not str(manifest.get(str(c["id"]), "")).startswith("skip")]
    log.info("%d already cached, %d to fetch (~%.0f min)", len(selected) - len(todo), len(todo), len(todo) * 2 * args.min_interval / 60)

    for c in tqdm(todo, unit="contest"):
        status = fetch_contest(client, c, paths.RAW_CONTESTS / f"{c['id']}.json.gz")
        manifest[str(c["id"])] = status
        paths.MANIFEST.write_text(json.dumps(manifest, indent=1, sort_keys=True))
        log.debug("%s %s -> %s", c["id"], c["name"], status)

    n_ok = sum(1 for cid in manifest if (paths.RAW_CONTESTS / f"{cid}.json.gz").exists())
    log.info("done. %d contests on disk, %d API calls this run", n_ok, client.n_calls)


if __name__ == "__main__":
    main()
