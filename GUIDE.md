# The project from scratch — a guided walk-through

This guide explains the whole project in the order we actually did it, assuming you know
nothing about Codeforces ratings, SVD or LSH. Every number quoted here is produced by the code
in this repository (file names are given so you can check). The short formal write-up is
`report/report.pdf`; this document is the long, friendly version.

**Contents**

1. [The question](#1-the-question)
2. [The raw data: what exists on Codeforces and what we downloaded](#2-the-raw-data)
3. [Elo: turning a rating into a prediction](#3-elo-turning-a-rating-into-a-prediction)
4. [The surprise matrix S — the central object](#4-the-surprise-matrix-s--the-central-object)
5. [SVD: finding the directions in S](#5-svd-finding-the-directions-in-s)
6. [Is the structure real? (D1)](#6-is-the-structure-real-d1)
7. [What are the axes? (D2)](#7-what-are-the-axes-d2)
8. [Do the official tags match? (D3)](#8-do-the-official-tags-match-d3)
9. [Skill twins and LSH (D4, D5)](#9-skill-twins-and-lsh-d4-d5)
10. [Checking it on rounds we never used (replication)](#10-checking-it-on-rounds-we-never-used)
11. [What we can and cannot claim](#11-what-we-can-and-cannot-claim)
12. [Map of the repository and how to rerun everything](#12-map-of-the-repository)
13. [Glossary](#13-glossary)

---

## 1. The question

Codeforces is a competitive-programming website. Every few days it runs a *contest* (a "round")
in which a few thousand people try to solve 5–8 problems in two hours. After each round every
participant's **rating** (a single integer, e.g. 1500 or 2400) goes up or down. The rating is
meant to say how good you are, with one number.

Two people can both be rated 1600 and be very different: one is great at number theory and
bad at dynamic programming, the other the reverse. The one number cannot express that.

> **Is one number enough?** After we account for the rating, is there still a *consistent*
> pattern in who solves which problems? If yes: what are the hidden "skills", do the
> problem-setters' tags (dp, graphs, math, ...) describe them, and can we find people with
> similar skill profiles ("skill twins") quickly?

A good analysis must be able to answer **"no, one number is enough"**. So everything below is
built around *tests that could have failed*.

---

## 2. The raw data

Codeforces has a public web API (`https://codeforces.com/api/...`). We used three calls
(`src/cfskills/api.py`, `fetch.py`):

| API call | What it gives | What we keep |
|---|---|---|
| `contest.list` | every contest, its name, start time, phase | the list of finished rounds we want |
| `contest.standings?contestId=X` | for each participant: which problems they solved in the contest | for each official participant, the set of problems solved |
| `contest.ratingChanges?contestId=X` | each participant's rating **before** (`oldRating`) and after the round | the *pre-round* rating `old_rating` |
| `problemset.problems` | every problem's difficulty rating (800–3500) and **tags** | rating + tags per problem |

Choices we made (all in `fetch.py` / `matrix.py`):

* **Which rounds.** The 600 most recent finished *individual* rounds that are at least 90 days
  old (younger rounds have unsettled ratings). 11 of them turned out to be unrated, leaving
  **589 rounds**. Team rounds, April-fools and the like are filtered out by name.
* **Which participants.** Only *official* single-person participants in a *rated* round (so
  everyone has a pre-round rating). We keep only users who took part in **at least 40** of
  these rounds, so each user has enough data: **36,519 users**.
* **Which problems.** Only problems that have a published difficulty rating: **3,773 problems**.
* **"Solved".** Only solves *during the contest*. (Upsolving afterwards is ignored, so everyone
  is measured under the same time pressure.)
* The API is polite-rate-limited (1 request / 2 s), so the pull takes about 75 minutes. Results
  are cached in `data/raw/` (not stored in git because it is 118 MB; `make fetch` rebuilds it).

After this step the situation is:

> for each of 589 rounds, for each of the (≥40-round) participants, we know their rating before
> the round and which of the round's problems they solved. For each problem we know its
> difficulty rating and tags.

---

## 3. Elo: turning a rating into a prediction

Codeforces' rating is Elo-style. The Elo idea: if a player has rating `R` and a problem has
difficulty `r`, the **probability the player solves it** is

```
p = 1 / (1 + 10^((r - R)/400))
```

Worked examples (a 1600-rated player):

| problem difficulty r | p (chance to solve) |
|---|---|
| 1200 | 1/(1+10^(-1)) = **0.91** |
| 1400 | 1/(1+10^(-0.5)) = **0.76** |
| 1600 | **0.50** |
| 2000 | 1/(1+10^(1)) = **0.09** |

So Elo gives us, for every (user, problem) pair that actually happened, **what a pure
"one-number" world predicts**. If one number really were enough, the true solve probability
would be `p` and nothing else — the actual outcome would be `p` plus pure coin-flip noise.

---

## 4. The surprise matrix S — the central object

For every user *i* and every problem *j* they faced, define

```
y_ij = 1 if user i solved problem j in the contest, else 0
s_ij = y_ij − p_ij          ("surprise": reality minus the Elo prediction)
```

Examples (1600-rated player):

* solves a 2000 problem: `s = 1 − 0.09 = +0.91` (big positive surprise)
* fails a 1200 problem: `s = 0 − 0.91 = −0.91` (big negative surprise)
* solves a 1200 problem: `s = 1 − 0.91 = +0.09` (barely a surprise)

Arrange all of these in a table:

* one **row per user** (36,519 rows),
* one **column per problem** (3,773 columns),
* entry `s_ij` if the user faced that problem, and **0 if not**.

That is the **surprise matrix S**. Facts about it:

* It is **sparse**: a user only faces problems of the rounds they entered (~430 problems on
  average). 15.85 million cells are observed out of 137.8 million, a density of 11.5 %. We store
  it as a sparse matrix (`data/processed/S.npz`) plus a 0/1 "was observed" mask `M.npz`; the
  row/column labels are in `users.csv`, `problems.csv`.
* **Rating is removed by construction.** Since `p` already uses the user's rating, a user who
  simply performs at their rating has surprises that average ~0. What's left in S is
  *everything the rating did not explain*.
* **What a pattern in S would mean.** Suppose users A, B, C are all "good at graphs for their
  rating". Then on graph problems they all have positive surprises, and on other problems
  slightly negative ones. Their rows of S share a pattern, and the graph problems' columns
  share a pattern. A hidden skill = a pattern shared across many rows *and* many columns.
  That is exactly what "low rank" means (next section).
* **The zero-filling caveat.** Putting 0 for "didn't face it" is a modelling choice: it is
  neutral for the average but can inject structure (e.g. "which division you play in" decides
  which problems you could face). We guard against it with several checks (section 6) and state
  it as a limitation.

Code: `matrix.py` (`elo_prob`, `surprise`, `build`).

---

## 5. SVD: finding the directions in S

The **singular value decomposition** writes any matrix as a sum of simple "rank-1" pieces:

```
S  ≈  σ1 · u1 v1ᵀ  +  σ2 · u2 v2ᵀ  +  σ3 · u3 v3ᵀ  + ...
```

* each `v_k` is a vector over **problems** (3,773 numbers): the **loading** of every problem on
  axis *k*. Problems with large positive loading are one end of the axis, large negative the
  other end.
* each `u_k` is a vector over **users** (36,519 numbers): the **score** of every user on axis *k*.
* `σ_k` (singular value) says how much of S that axis explains. They come sorted, biggest first.

Interpretation of one piece: *user i's surprise on problem j is, to first order,
`σ1 · score_i1 · loading_j1`* — a user with a high score on axis 1 over-performs on problems
with high loading and under-performs on problems with negative loading. That is a "skill
axis": a user's position along it is how good they are *at that kind of problem relative to
their rating*.

We compute only the top 20 (or 60) pieces with a truncated SVD (`scipy.sparse.linalg.svds`),
which is fast on a sparse matrix (`svd.py`, `truncated_svd`).

Key point: SVD will *always* return something, even for pure noise. The whole of section 6 is
about deciding whether what it returned means anything.

---

## 6. Is the structure real? (D1)

We use three independent tests. Each is designed so that "one number is enough" would show up
as a failure.

### 6.1 A permutation null (parallel analysis)

Make a fake S where there is no user-level consistency but everything else is the same:
inside each **problem column**, shuffle the observed surprises among the users who faced it.
This keeps every problem's distribution and sparsity pattern, but destroys the idea that "the same
users over-perform on the same problems". Take the SVD of the fake matrix, 20 times.
If a real singular value σ_k is larger than the k-th singular value of *all* fakes, component k
contains something the shuffle can't produce.

Result (`outputs/D1_spectrum*.csv/png`): all 60 components tested beat the null. The gap is
largest for components 4–9 (σ is ≈1.5× the null's).

**Warning we state in the report:** with 15.8 million entries, even a tiny real effect is
"significant". So "60 significant components" does **not** mean 60 skills. We look at effect
sizes (the singular values, the held-out gain) instead.

### 6.2 An Elo simulation null

A tougher null: simulate a world where Elo is *exactly true* — each outcome is a Bernoulli coin
flip with probability `p_ij`, same users, same problems, same rating values. If the real spectrum
clears this too, the structure is not an artefact of binary outcomes or of the Elo formula's
shape (`robust.py`, `paramnull`, figure panel 2a). It does.

### 6.3 Predicting hidden outcomes (held-out test)

If the structure is real it should help **predict things the model never saw**.
`robust.py`, `heldout`:

1. Split the 15.85 M observed entries 80 % train / 10 % calibration / 10 % test.
2. Fit everything (user offsets, problem offsets, SVD) on **train only**.
3. For each model, fit a tiny logistic regression on the calibration part that combines its
   features into a probability; score it on the **test** part with *log-loss* (lower is better).

Models compared:

| model | idea | test log-loss | gain vs Elo |
|---|---|---|---|
| Elo only | the pure one-number prediction | 0.2135 | 0 % |
| + problem offset + user offset | "this problem is harder than its rating says; this user is on a hot streak" | 0.2045 | 4.3 % |
| + user × tag offsets | per-user average surprise on each of the 21 main tags | 0.2037 | 4.6 % |
| + SVD rank-10 | 10 hidden axes | **0.1970** | **7.7 %** |
| + tags + SVD rank-10 | both | 0.1968 | 7.8 % |

(three random splits give gains 7.77 ± 0.05 % for rank-10 and 4.71 ± 0.11 % for tags, 4.35 ± 0.08 % for offsets only; the table
shows seed 0; gains are rounded.)

Reading this:

* A big part of the improvement over Elo (4.3 %) is just *offsets* (a problem's real difficulty
  differs from its published rating; a user is above/below form). That is **not** hidden skill.
* The rank-10 axes add another **3.4 %-points on top of the offsets** — real, repeatable
  (±0.05), and large compared with the effect of tags (+0.4).
* The tags add almost nothing once the axes are present (0.1970 → 0.1968): whatever signal the
  tags have, the axes already contain it, and much more.
* More axes help up to ~10–20, then the model starts to overfit (k = 40 is a little worse).

### 6.4 Do the dimensions reproduce? (split-half)

Split the rounds into odd-numbered and even-numbered, compute the SVD separately in each half
(different problems, same users), and ask whether a user's scores in the two halves agree.
Because the axes could be rotated between halves, we compare using *canonical correlation*
(the best linear matching of the two score sets). For the top dimensions the correlations
are 0.90, 0.88, 0.83, 0.73, 0.67, 0.60, ... (about six are well above chance); a control with
shuffled users gives ≤ 0.03. So the user scores are a **stable trait**, not noise.

### 6.5 "Maybe it's just form": residualizing

If a user had a great day in one round, all their surprises in that round move together, and
SVD would find that as a "skill". To check, we subtract each user's average surprise *in each
round* before the SVD (`make svd-resid`). The structure remains (all 20 components still beat
the null), so it is not just good-day/bad-day.

**Verdict for D1: one number is not enough.** There are about 6–10 meaningful dimensions.

---

## 7. What are the axes? (D2)

For each axis we look at three things (`svd.py`, `write_axes_report`; results `outputs/D2_axes.md`):

1. The **problems with the most extreme loadings** at each end (with their ratings and tags).
2. **Tag enrichment z-score**: for each tag, compare the mean loading of problems with the tag
   vs without it, divided by the standard error. A large positive z means "this tag sits at
   the + end".
3. **Correlation of the loading with the problem's difficulty rating**: tells whether the axis is
   "difficulty in disguise".

What we found:

* **Axis 1 — a difficulty slope.** One end: easy implementation / strings / greedy problems.
  Other end: DFS / trees / divide-and-conquer / DP / graphs. Correlation with problem rating is
  −0.47. It mostly says *"do you over-perform on hard algorithmic problems"*. Inside one rating
  band it nearly vanishes, so part of it is a division effect (which problems you faced).
* **Axis 8 (and 2, 3, 4, 11, 12) — ad-hoc vs algorithmic.** Math / constructive / number theory
  on one end, data structures / trees / binary search / graphs on the other (axis 8: math
  z = +7.6, data structures z = −8.4) with only −0.11 correlation with difficulty. This is the
  clearest *topic* axis, and it shows up inside every rating band.
* Per-tag stability: being good at a tag relative to your rating is a stable trait mainly for
  dp (0.27), data structures (0.26), trees (0.20), and hardly for sortings/geometry/brute force.

So the "hidden skills" are mostly a **difficulty slope** and a **coarse ad-hoc ↔ algorithmic
contrast**, not 35 independent tag skills.

---

## 8. Do the official tags match? (D3)

Three different ways to ask:

### 8.1 Cluster the problems and compare with tags

Represent every problem by its coordinates on the significant axes (`V Σ`), cluster with
k-means (and spectral clustering), and compare each cluster with each tag using the **Jaccard
index** (`|cluster ∩ tag| / |cluster ∪ tag|`). A random partition into clusters of the same sizes
gives a baseline. Result: the clusters agree with tags only **0.3–2.3 Jaccard points** more than
random (e.g. k-means 0.097 vs 0.094 random). The clusters are dominated by difficulty and
division, not by topic: with k = 8, one cluster is 2,130 hard problems and the other seven are
800–1400-rated problems separated by position in the round.

### 8.2 Predict a tag from the axes

For each tag, train a classifier: "does this problem have the tag?" from (a) its difficulty
alone, (b) the 20 axes alone, (c) difficulty + axes (cross-validated AUC). The axes help only
for *ad-hoc* tags (math 0.53 → 0.62, constructive 0.52 → 0.61, games 0.46 → 0.59) and not for
dp/trees/graphs, whose tags already reveal their difficulty.

### 8.3 Head-to-head on predicting solves (new)

The sharpest test: which carries more information about **who solves what** — the setters' tags
or the SVD axes? In the held-out test (section 6.3) the **user × tag** model (one learned
offset per user per tag, 21 numbers per user) improves log-loss by 4.6 % over Elo; the **rank-10
SVD** (10 numbers per user) improves it by 7.7 %; combining them gives 7.8 %. Stronger shrinkage
of the tag offsets does not change this. So the data-driven axes contain roughly ten times the
information of the tags beyond bias terms, and the tags are almost redundant given the axes.

**Verdict for D3:** tags only weakly match the structure.

---

## 9. Skill twins and LSH (D4, D5)

### 9.1 The goal

Given a user, find the users with the most similar skill profile — quickly. With 36,519 users
there are 641 million pairs; comparing them all is the "brute force" way.

### 9.2 Turning a user into a set

For each user, make a set of tokens: `hit:j` if they solved problem *j* with a big positive
surprise (Elo predicted < 30 %), `miss:j` if they failed problem *j* with a big negative
surprise (Elo predicted > 70 %). Two users with many shared tokens fail and succeed in the same
unexpected places. The similarity between two sets is the **Jaccard index** (shared / total).

### 9.3 MinHash and LSH

* **MinHash**: compress each set into 256 small numbers such that the fraction of matching
  numbers between two users estimates their Jaccard similarity.
* **LSH banding**: split the 256 numbers into *b* bands of *r* numbers; two users become a
  *candidate pair* if they agree on all *r* numbers in at least one band. Only candidates are
  checked exactly. Choosing *b × r* sets a similarity threshold.

### 9.4 What we found

* Real nearest neighbours are *not very similar*: the median top-1 Jaccard is 0.12 (sets are small,
  median 15 tokens). So the 32 × 4 banding from our proposal (threshold ≈ 0.42) finds almost
  nothing (72 candidate pairs, recall 0.003).
* A looser 128 × 2 banding with 256 hashes finds 84 % of the true top-10 neighbours while
  examining only 1.4 % of all pairs. But it took 43 s vs 12 s for an exact sparse-matrix brute
  force — at n ≈ 36 k the exact method is already fast, so LSH saves *pairs* but not *time*.

### 9.5 The demo (D5)

`python -m cfskills.demo tourist` prints the user's score on each axis and the closest twins;
`streamlit run app.py` is the same as a web page. (tourist's closest twins: jiangly, Radewoosh,
ksun48, ...). Twins are close in rating by construction, since two users share tokens only on
problems they both faced.

---

## 10. Checking it on rounds we never used

Everything so far used one block of 589 rounds. A natural worry: *maybe we just found patterns
specific to this period.* So we downloaded a **second, older block** — the 500 qualifying rounds
just before the first block (458 usable, Aug 2016 – Mar 2021, versus Mar 2021 – Aug 2026 for the main block), with
**no problem in common**. After the same pipeline (`make earlier`) it has 14,515 users
(≥ 40 rounds *inside this block*), 2,514 problems and 5.3 M observed outcomes. Then
(`make replicate`, `robust.py: replicate`):

**(a) Does the older matrix also beat the null?** Yes: all 20 tested components beat the
within-column shuffle (ratios of real to null singular value 1.1–1.56, largest at components
2–3). So structure beyond Elo exists in both eras.

**(b) Do users keep their scores across eras?** 2,253 people appear in both blocks with enough
data (≥ 30 observed outcomes each). We compare their axis scores (top 10 dimensions) with
canonical correlation, again against a shuffled-users control:

| dimension | 1 | 2 | 3 | 4 | 5 | 6+ |
|---|---|---|---|---|---|---|
| older vs current | **0.73** | **0.49** | **0.36** | 0.19 | 0.13 | ≤ 0.10 |
| shuffled users | 0.11 | 0.09 | 0.07 | 0.07 | 0.06 | ≤ 0.05 |

Reading: the first dimension is a strong, persistent trait; dimensions 2 and 3 persist more
weakly; from dimension 4 on nothing survives. This is *lower* than the odd/even split (section 6.4),
which is expected: the two blocks are years apart, people's skills drift, and only 2,253 users
overlap. It also trims our claim: the robust core is **about three dimensions**, not ten.

**(c) Do the axes mean the same thing?** Problems differ between eras, so we cannot compare
loadings directly. Instead we compare each axis's **tag-enrichment profile** (the vector of
z-scores over the 35 common tags, section 7) between eras. For each of the ten leading current
axes, the best-matching older axis has correlation 0.53–0.81, whereas shuffling tag labels gives
at most about 0.47 (95th percentile). So every leading axis has a counterpart with the same
tag signature. *Caveat:* five of the ten current axes match the *same* older axis 1, i.e. the dominant
difficulty/division pattern recurs; this is weaker evidence for ten distinct dimensions than for
a persistent main pattern.

**Verdict:** the main finding (structure beyond one number, led by a difficulty slope and an
ad-hoc ↔ algorithmic contrast) replicates on independent rounds. The finer dimensions do not
reliably.

---

## 11. What we can and cannot claim

**Can claim**

* A single rating does not capture everything: beyond Elo, per-problem and per-user offsets, a
  rank-10 structure predicts hidden solves 3.4 %-points better, stable across random splits.
* About six user dimensions are reproducible within the data (odd/even rounds); on a second,
  older block of rounds the first dimension replicates strongly (0.73), the second and third
  weakly (0.49, 0.36), the rest not (section 10). The robust core is about **three** dimensions.
* The strongest, most interpretable dimensions are a difficulty slope and an ad-hoc ↔
  algorithmic contrast.
* The setters' tags carry little of this structure: a user × tag model adds about a tenth of
  what the axes add, and the axes make the tags redundant.

**Cannot claim**

* That there are "N true skills". The axes are mathematical directions; they are rotated mixes,
  and with 15.8 M entries every direction is statistically significant, so we judge by effect
  size and reproducibility, not p-values.
* That tags are "wrong". Tags describe the *content* of a problem; our axes describe *who solves
  it*. The two are different, only partly related.
* That the axes are pure skill. Zero-filling, division effects, problem ratings estimated from
  the same solve data, in-contest speed, and the sampled time window all leak in. We mitigate and
  report these in the limitations.

---

## 12. Map of the repository

```
src/cfskills/
  api.py      Codeforces API client (rate-limited, retrying)
  fetch.py    which rounds to pull; caching to data/raw          (section 2)
  matrix.py   Elo, surprise, build S / M / users / problems      (sections 3-4)
  svd.py      truncated SVD, permutation null, axis tables       (sections 5-7)
  cluster.py  k-means / spectral clustering, Jaccard vs tags     (section 8.1)
  robust.py   held-out prediction, split-half, Elo null, bands,
              tag prediction, replication                        (sections 6, 8.2, 8.3, 10)
  lsh.py      MinHash LSH, evaluation, twins                     (section 9)
  demo.py     handle -> fingerprint + twins                      (section 9.5)
  plots.py    all report figures
app.py        Streamlit demo
tests/        unit tests on synthetic data (planted structure is found, noise is not)
data/processed/   S.npz, M.npz, users.csv, problems.csv         (the matrix)
outputs/          every result table/figure (D1_*, D2_*, D3_*, D4_*, R_*)
report/           report.tex / report.pdf (4 pages)
```

Rerun: `make setup test` then `make fetch matrix svd cluster lsh extras plots report`
(the fetch is the slow part, ~75 min; the repo already contains the processed matrix, so
everything after it works without fetching).

---

## 13. Glossary

* **Rating** — the single integer Codeforces assigns to a user (and, as a difficulty, to a problem).
* **Elo** — the rating model above; gives the win/solve probability from a rating difference.
* **Surprise** — outcome minus Elo's predicted probability.
* **Sparse matrix** — a matrix where we only store the non-zero (observed) entries.
* **SVD** — decomposition of a matrix into ordered rank-1 pieces; the "axes".
* **Singular value (σ)** — the weight (importance) of one axis.
* **Loading / score** — an axis's value for a problem / for a user.
* **Null model** — a fake dataset in which the thing we're testing for is absent on purpose.
* **Held-out** — data hidden when fitting, used only for scoring.
* **Log-loss** — average −log of the probability a model gave to what actually happened; lower is better.
* **Canonical correlation** — how well two sets of coordinates agree after the best rotation.
* **Jaccard index** — |A ∩ B| / |A ∪ B| for two sets.
* **MinHash / LSH** — a way to find similar sets without comparing every pair.
* **Recall@10** — of a user's true 10 nearest neighbours, the fraction the method finds.
