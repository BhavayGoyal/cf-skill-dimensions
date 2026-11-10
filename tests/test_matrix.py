import gzip
import json

import numpy as np
import pytest

from cfskills import matrix
from cfskills.fetch import select_contests, slim_standings


def test_elo_prob_basics():
    assert matrix.elo_prob(1600, 1600) == pytest.approx(0.5)
    assert matrix.elo_prob(2000, 1600) == pytest.approx(1 / (1 + 10 ** -1))
    assert matrix.elo_prob(1200, 1600) < 0.1
    # surprise sign conventions
    assert matrix.surprise(1, 1600, 1600) == pytest.approx(0.5)
    assert matrix.surprise(0, 1600, 1600) == pytest.approx(-0.5)


def test_p_recoverable_from_s():
    s_hit = matrix.surprise(1, 1500, 1900)
    s_miss = matrix.surprise(0, 1900, 1500)
    assert 1 - s_hit == pytest.approx(matrix.elo_prob(1500, 1900))
    assert -s_miss == pytest.approx(matrix.elo_prob(1900, 1500))


def test_select_contests_filters():
    now = 1_000_000_000
    day = 86400
    contests = [
        {"id": 1, "name": "Codeforces Round 900 (Div. 2)", "phase": "FINISHED", "startTimeSeconds": now - 200 * day},
        {"id": 2, "name": "Codeforces Round 901 (Div. 1)", "phase": "FINISHED", "startTimeSeconds": now - 10 * day},   # too young
        {"id": 3, "name": "April Fools Day Contest 2024", "phase": "FINISHED", "startTimeSeconds": now - 300 * day},  # excluded
        {"id": 4, "name": "Educational Codeforces Round 150", "phase": "FINISHED", "startTimeSeconds": now - 150 * day},
        {"id": 5, "name": "Codeforces Round 800 (Div. 3)", "phase": "CODING", "startTimeSeconds": now - 150 * day},   # not finished
        {"id": 6, "name": "ICPC Team Mirror", "phase": "FINISHED", "startTimeSeconds": now - 150 * day},
    ]
    sel = select_contests(contests, n=10, min_age_days=90, now=now)
    assert [c["id"] for c in sel] == [4, 1]  # newest first
    assert [c["id"] for c in select_contests(contests, n=1, min_age_days=90, now=now)] == [4]


def test_slim_standings_keeps_official_single_contestants():
    standings = {
        "problems": [{"index": "A", "name": "a"}, {"index": "B", "name": "b"}],
        "rows": [
            {"party": {"participantType": "CONTESTANT", "members": [{"handle": "u1"}]}, "problemResults": [{"points": 500}, {"points": 0}]},
            {"party": {"participantType": "CONTESTANT", "members": [{"handle": "u2"}]}, "problemResults": [{"points": 1}, {"points": 1}]},
            {"party": {"participantType": "VIRTUAL", "members": [{"handle": "u3"}]}, "problemResults": [{"points": 1}, {"points": 1}]},
            {"party": {"participantType": "CONTESTANT", "members": [{"handle": "t1"}, {"handle": "t2"}]}, "problemResults": [{"points": 1}, {"points": 1}]},
        ],
    }
    slim = slim_standings(standings)
    assert slim["rows"] == [["u1", [0]], ["u2", [0, 1]]]
    assert slim["n_team_rows"] == 1


def _write_contest(dirpath, cid, problems, rows, old_rating, t=0):
    payload = {"contest": {"id": cid, "name": f"c{cid}", "startTimeSeconds": t}, "problems": problems, "rows": rows, "old_rating": old_rating}
    with gzip.open(dirpath / f"{cid}.json.gz", "wt") as fh:
        json.dump(payload, fh)


def test_build_matrix_end_to_end(tmp_path):
    raw = tmp_path / "contests"
    raw.mkdir()
    problems_json = tmp_path / "problems.json.gz"
    with gzip.open(problems_json, "wt") as fh:
        json.dump({"problems": [
            {"contestId": 1, "index": "A", "rating": 1000, "tags": ["math"]},
            {"contestId": 1, "index": "B", "rating": 1600, "tags": ["dp", "math"]},
            {"contestId": 2, "index": "A", "rating": 1200, "tags": ["greedy"]},
            {"contestId": 2, "index": "B", "tags": ["dp"]},  # no rating -> dropped
        ]}, fh)
    _write_contest(raw, 1, [{"index": "A"}, {"index": "B"}], [["alice", [0, 1]], ["bob", [0]], ["newbie", [0]]],
                   {"alice": 1600, "bob": 1600, "newbie": 0}, t=1)
    _write_contest(raw, 2, [{"index": "A"}, {"index": "B"}], [["alice", []], ["bob", [0, 1]]], {"alice": 1700, "bob": 1500}, t=2)

    S, M, users, problems = matrix.build(min_participations=2, raw_dir=raw, problems_json=problems_json)
    assert S.shape == (2, 3)  # alice, bob x (1A, 1B, 2A)
    assert list(users["handle"]) == ["alice", "bob"]
    assert users.set_index("handle").loc["alice", "last_rating"] == 1700
    assert M.nnz == 6
    a = users.index[users["handle"] == "alice"][0]
    col_1B = problems.index[(problems["contestId"] == 1) & (problems["index"] == "B")][0]
    assert S[a, col_1B] == pytest.approx(1 - 0.5, abs=1e-6)       # solved a 1600 at rating 1600
    col_2A = problems.index[(problems["contestId"] == 2) & (problems["index"] == "A")][0]
    assert S[a, col_2A] == pytest.approx(-matrix.elo_prob(1700, 1200), abs=1e-6)  # missed an easy one
    assert "newbie" not in set(users["handle"])
    assert set(problems["tags"]) == {"math", "dp;math", "greedy"}
