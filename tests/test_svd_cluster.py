import numpy as np
import pandas as pd
import scipy.sparse as sp

from cfskills import cluster, svd


def _planted(n_users=400, n_problems=120, n_groups=3, density=0.5, strength=0.6, seed=0):
    """Users and problems split into n_groups 'skills'; users are good at problems of their own group."""
    rng = np.random.default_rng(seed)
    ug = rng.integers(0, n_groups, n_users)
    pg = rng.integers(0, n_groups, n_problems)
    mask = rng.random((n_users, n_problems)) < density
    base = rng.normal(0, 0.3, (n_users, n_problems))
    signal = strength * np.where(ug[:, None] == pg[None, :], 1.0, -1.0 / (n_groups - 1))
    S = sp.csr_matrix(np.where(mask, base + signal, 0.0).astype(np.float32))
    return S, ug, pg


def test_permutation_preserves_column_multisets():
    S, _, _ = _planted(n_users=50, n_problems=20)
    C = svd.permute_within_columns(S, np.random.default_rng(1))
    A, B = S.tocsc(), C.tocsc()
    assert (A.indptr == B.indptr).all()
    for j in range(S.shape[1]):
        assert np.allclose(np.sort(A.data[A.indptr[j]:A.indptr[j + 1]]), np.sort(B.data[B.indptr[j]:B.indptr[j + 1]]))
    assert not np.allclose(A.data, B.data)


def test_planted_structure_is_detected_and_noise_is_not():
    S, _, _ = _planted(n_groups=3)
    U, s, Vt = svd.truncated_svd(S, k=8)
    null = svd.null_spectra(S, k=8, n_perm=5, seed=1)
    sig = svd.significant_components(s, null)
    assert sig[:2].all()          # 3 groups -> at least 2 non-trivial directions beyond the mean
    assert sig.sum() <= 4

    # pure noise: nothing should survive
    rng = np.random.default_rng(3)
    noise = sp.csr_matrix(np.where(rng.random((300, 80)) < 0.5, rng.normal(0, 0.3, (300, 80)), 0.0).astype(np.float32))
    U, s, Vt = svd.truncated_svd(noise, k=5)
    null = svd.null_spectra(noise, k=5, n_perm=10, seed=2)
    assert svd.significant_components(s, null).sum() <= 1


def test_center_columns():
    S, _, _ = _planted(n_users=30, n_problems=10)
    C = svd.center_columns(S).tocsc()
    for j in range(C.shape[1]):
        vals = C.data[C.indptr[j]:C.indptr[j + 1]]
        if len(vals):
            assert abs(vals.mean()) < 1e-5


def test_residualize_user_contest_removes_round_means():
    S, _, _ = _planted(n_users=40, n_problems=12)
    contest = np.repeat([101, 102, 103], 4)  # 3 rounds x 4 problems
    R = svd.residualize_user_contest(S, contest)
    assert R.shape == S.shape and R.nnz == S.nnz
    Rd, Sd = R.toarray(), S.toarray()
    for c in np.unique(contest):
        cols = contest == c
        for i in range(S.shape[0]):
            obs = Sd[i, cols] != 0
            if obs.any():
                assert abs(Rd[i, cols][obs].mean()) < 1e-5
    # within-round *differences* are untouched
    i = 0; cols = np.flatnonzero(contest == 101)
    obs = [j for j in cols if Sd[i, j] != 0]
    if len(obs) >= 2:
        assert np.isclose(Rd[i, obs[0]] - Rd[i, obs[1]], Sd[i, obs[0]] - Sd[i, obs[1]], atol=1e-5)


def test_cluster_recovers_planted_groups_and_beats_random():
    S, ug, pg = _planted(n_groups=3, strength=0.8)
    U, s, Vt = svd.truncated_svd(S, k=5)
    sig = np.array([True, True, True, False, False])
    X = cluster.problem_coords(Vt, s, sig)
    labels = cluster.kmeans_labels(X, 3)
    # tags = the planted groups (plus a useless tag) -> agreement should be high and far above random
    problems = pd.DataFrame({"col": np.arange(len(pg)), "tags": [f"g{g};misc" if i % 2 else f"g{g}" for i, g in enumerate(pg)]})
    tags = svd.tag_sets(problems)
    J = cluster.jaccard_matrix(labels, tags, len(pg))
    real = cluster.agreement_score(J)
    null = cluster.random_baseline(labels, tags, len(pg), n_random=50)
    assert real > 0.7
    assert real > null.max()


def test_tag_enrichment_signs():
    rng = np.random.default_rng(0)
    loading = np.concatenate([rng.normal(1, 0.1, 30), rng.normal(-1, 0.1, 30)])
    tags = {"pos": np.arange(30), "neg": np.arange(30, 60), "tiny": np.arange(3)}
    enr = svd.tag_enrichment(loading, tags, min_size=15)
    assert list(enr["tag"]) == ["pos", "neg"]
    assert enr.iloc[0]["z"] > 10 and enr.iloc[1]["z"] < -10
