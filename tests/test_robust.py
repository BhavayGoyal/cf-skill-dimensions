import numpy as np
import pandas as pd
import scipy.sparse as sp

from cfskills import robust
from cfskills.matrix import elo_prob


def _simulated(n_users=600, n_problems=150, n_groups=3, strength=1.2, seed=0):
    """Users with a latent group skill; y ~ Bernoulli(sigmoid(elo logit + group effect))."""
    rng = np.random.default_rng(seed)
    R = rng.integers(1000, 2200, n_users)
    r = rng.integers(800, 2400, n_problems)
    ug = rng.integers(0, n_groups, n_users); pg = rng.integers(0, n_groups, n_problems)
    p = elo_prob(R[:, None], r[None, :])
    logit = np.log(p / (1 - p)) + strength * np.where(ug[:, None] == pg[None, :], 1, -0.5)
    p_true = 1 / (1 + np.exp(-logit))
    y = rng.random(p.shape) < p_true
    mask = rng.random(p.shape) < 0.6
    S = sp.csr_matrix(np.where(mask, y - p, 0).astype(np.float32))
    contests = np.repeat(np.arange(n_problems // 5), 5)
    problems = pd.DataFrame({"col": np.arange(n_problems), "contestId": contests, "rating": r, "tags": [f"g{g}" for g in pg]})
    return S, problems


def test_p_from_s_roundtrip():
    s = np.array([0.3, -0.8, 0.95, -0.05])
    y, p = robust._p_from_s(s)
    assert y.tolist() == [1, 0, 1, 0]
    assert np.allclose(p, [0.7, 0.8, 0.05, 0.05])


def test_biases_fit_additive_model():
    rng = np.random.default_rng(0)
    bu, bp = rng.normal(0, 0.2, 200), rng.normal(0, 0.1, 50)
    mask = rng.random((200, 50)) < 0.7
    S = sp.csr_matrix(np.where(mask, bu[:, None] + bp[None, :], 0).astype(np.float32))
    bu_hat, bp_hat = robust._biases(S, n_iter=20)
    # identifiable up to a constant shift between user and problem biases
    assert np.corrcoef(bu, bu_hat)[0, 1] > 0.99
    assert np.corrcoef(bp, bp_hat)[0, 1] > 0.99


def test_heldout_rank_k_beats_elo_when_structure_is_planted(tmp_path):
    S, problems = _simulated()
    for mode in ("entries", "user_contest"):
        df = robust.heldout(S, problems, ks=(1, 2, 3, 5), mode=mode, out=tmp_path)
        elo = df[df.model == "Elo only"].iloc[0]
        ranked = df[df.model == "Elo + biases + rank-k"].set_index("k")
        best_k = ranked["logloss"].idxmin()
        assert ranked.loc[best_k, "logloss"] < elo["logloss"] - 0.01
        assert ranked.loc[best_k, "auc"] > elo["auc"] + 0.005
        assert best_k in (2, 3)  # 3 planted groups -> 2 contrasts (+ maybe 1 for the mean)


def test_heldout_no_gain_when_elo_is_true_model(tmp_path):
    S, problems = _simulated(strength=0.0, seed=1)
    df = robust.heldout(S, problems, ks=(1, 3, 10), out=tmp_path)
    elo = df[df.model == "Elo only"].iloc[0]
    ranked = df[df.model == "Elo + biases + rank-k"]
    # high rank should overfit and *not* beat Elo by a meaningful margin
    assert (ranked["logloss"] > elo["logloss"] - 0.01).all()


def test_tag_matrix_and_offsets_recover_planted_tag_skill():
    """A user who over-performs on every 'a'-tagged problem gets a positive offset on tag 'a'."""
    import scipy.sparse as sp
    problems = pd.DataFrame({"tags": ["a"] * 120 + ["b"] * 120 + ["a;b"] * 20})
    T, names = robust._tag_matrix(problems, min_problems=100)
    assert list(names) == ["a", "b"] and T.shape == (260, 2)
    rng = np.random.default_rng(0)
    n_u = 30
    S = rng.normal(0, 0.05, (n_u, 260))
    S[0, :120] += 0.5                      # user 0 is good at 'a'
    S[1, 120:240] += 0.5                   # user 1 is good at 'b'
    S = sp.csr_matrix(S)
    offs = robust._tag_offsets(S, S, T, lam=1.0)
    assert offs[0, 0] > 0.3 > abs(offs[0, 1]) and offs[1, 1] > 0.3 > abs(offs[1, 0])
    f = robust._tag_feature(offs, T, np.array([0, 1]), np.array([0, 130]))
    assert f[0] > 0.3 and f[1] > 0.3
