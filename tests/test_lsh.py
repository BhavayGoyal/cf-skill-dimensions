import numpy as np
import pytest
import scipy.sparse as sp

from cfskills import lsh


def test_build_tokens_hit_miss_encoding():
    S = sp.csr_matrix(np.array([[0.9, -0.8, 0.1, 0.0], [0.0, -0.9, 0.75, -0.2]], dtype=np.float32))
    X, keep = lsh.build_tokens(S, thr=0.7, min_tokens=2)
    X = X.toarray()
    assert X.shape == (2, 8)
    assert X[0].nonzero()[0].tolist() == [0, 3]          # hit:0 -> 0, miss:1 -> 3
    assert X[1].nonzero()[0].tolist() == [3, 4]          # miss:1 -> 3, hit:2 -> 4
    assert keep.tolist() == [0, 1]


def _random_sets(n_users=300, n_tokens=2000, seed=0):
    rng = np.random.default_rng(seed)
    X = sp.random(n_users, n_tokens, density=0.02, format="csr", random_state=seed, dtype=np.float32)
    X.data[:] = 1
    # plant near-duplicate pairs
    X = X.tolil()
    for i in range(0, min(60, n_users), 2):
        X[i + 1] = X[i]
        X[i + 1, rng.integers(0, n_tokens, 2)] = 1
    return X.tocsr().astype(np.int8)


def test_minhash_estimates_jaccard():
    X = _random_sets()
    sig = lsh.minhash_signatures(X, n_hashes=256)
    J = lsh.exact_jaccard_matrix(X)
    est = (sig[0] == sig[1]).mean()
    assert abs(est - J[0, 1]) < 0.12
    est_far = (sig[0] == sig[100]).mean()
    assert abs(est_far - J[0, 100]) < 0.12


def test_lsh_finds_planted_twins_with_high_recall():
    X = _random_sets()
    J = lsh.exact_jaccard_matrix(X)
    exact = lsh.topk_from_matrix(J, k=1)
    sig = lsh.minhash_signatures(X, n_hashes=128)
    pairs = lsh.candidate_pairs(sig, bands=32, rows=4)
    jac = lsh.exact_jaccard_pairs(X, pairs)
    approx = lsh.topk_from_pairs(pairs, jac, X.shape[0], k=1)
    planted = {i: exact[i] for i in range(60)}
    assert lsh.recall_at_k(planted, approx, k=1) > 0.9
    # far fewer candidates than all pairs
    assert len(pairs) < 0.2 * X.shape[0] * (X.shape[0] - 1) / 2


def test_exact_jaccard_pairs_matches_matrix():
    X = _random_sets(n_users=50)
    J = lsh.exact_jaccard_matrix(X)
    pairs = np.array([[0, 1], [0, 2], [10, 11], [5, 40]])
    assert np.allclose(lsh.exact_jaccard_pairs(X, pairs), J[pairs[:, 0], pairs[:, 1]])


def test_chunked_brute_force_matches_dense():
    X = _random_sets(n_users=130)
    dense = lsh.topk_from_matrix(lsh.exact_jaccard_matrix(X), k=5)
    chunked = lsh.brute_force_topk_chunked(X, k=5, chunk=40)
    assert set(dense) == set(chunked)
    for i in dense:
        assert [j for j, _ in dense[i]] == [j for j, _ in chunked[i]]


def test_threshold_formula():
    assert lsh.lsh_threshold(32, 4) == pytest.approx(0.42, abs=0.01)
