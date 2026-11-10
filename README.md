# Is One Number Enough? Hidden skill dimensions in Codeforces ratings

CS 328 project — Vishnu Sinha & Bhavay Goyal. Code, data and results: https://github.com/BhavayGoyal/cf-skill-dimensions . Report: `report/report.pdf`.

Codeforces compresses every contestant into one Elo-style rating. We ask: once
rating is accounted for, is there any *consistent* structure left in who solves
what? If so, what are the hidden skill axes, do they match the setters' tags,
and who are your "skill twins"?

The pipeline is built so the answer can be **no**: the headline test (D1)
compares the spectrum of the surprise matrix against a permutation null that
could sit right on top of it.

## Pipeline

| step | command | output | deliverable |
|---|---|---|---|
| 1 | `make fetch` | `data/raw/` — API pull, cached, resumable | — |
| 2 | `make matrix` | `data/processed/S.npz` surprise matrix | — |
| 3 | `make svd` | `outputs/D1_spectrum.*`, `outputs/D2_axes.md` | D1, D2 |
| 4 | `make cluster` | `outputs/D3_*` | D3 |
| 5 | `make lsh` | `outputs/D4_*`, `outputs/twins.json.gz` | D4 |
| 6 | `make demo H=<handle>` / `make app` | fingerprint + twins | D5 |

```bash
make setup                 # venv + editable install
make test                  # unit tests on synthetic data (planted structure is found, noise is not)
make quick                 # end-to-end on 25 contests (~3 min) to check everything before the big pull
make fetch                 # ~600 rounds, ~7 s per contest => ~75 min, resumable
make all                   # matrix svd cluster lsh
make demo H=tourist
make extras                # residualised SVD, k=60 spectrum, silhouette clustering, robustness checks
make plots                 # redraw all report figures -> outputs/report_figs/
make report                # build report/report.pdf (pdflatex or tectonic)
```

On Windows run `make` from Git Bash (the Makefile picks `.venv/Scripts` automatically), or call
the modules directly, e.g. `python -m cfskills.svd`.

Every module is also a CLI: `python -m cfskills.svd --help`, etc.

## Method in one screen

* **Surprise.** For user *i* with pre-contest rating *R_i* and problem *j* of
  difficulty *r_j*, Elo gives `p_ij = 1 / (1 + 10^((r_j - R_i)/400))`. The surprise
  is `s_ij = y_ij - p_ij` (y = solved in-contest). Unobserved pairs are 0. `S` is a
  sparse users × problems matrix; `M` is the observed mask.
* **D1.** Truncated SVD (top 20). Null: shuffle observed surprises within each
  problem column (keeps each problem's distribution and sparsity, destroys
  user-level consistency), 20 times. Component *k* is significant if σ_k beats
  every null σ_k.
* **D2.** For each significant axis: top/bottom loading problems with tags, and a
  tag-enrichment z-score (mean loading of tagged vs untagged problems).
* **D3.** Problem coordinates `V Σ` on significant axes → k-means (k by
  silhouette; spectral clustering on a kNN graph as extension). Cluster × tag
  Jaccard; agreement = mean best-match Jaccard; baseline = random partitions
  with the same cluster sizes (mean, std, empirical p).
* **D4.** Tokens `hit:j` (solved with p < 0.3 ⇔ s > 0.7) and `miss:j` (missed
  with p > 0.7 ⇔ s < −0.7). MinHash (256 hashes), banding b × r, candidates
  verified with exact Jaccard (buckets with > 2,000 users are skipped). Recall@10 vs. brute force on a 3,000-user sample
  across band settings, plus a full-population run timed against a chunked exact
  baseline.
* **D5.** `python -m cfskills.demo <handle>`: z-scored score on each axis next to
  the rating, plus top skill twins. `streamlit run app.py` for the UI.

## Results snapshot (full run, 589 rounds, 36,519 users × 3,773 problems)

See `report/report.md` for the full write-up with file references.

* **D1** — all 60 tested components beat every within-column shuffle; biggest gap at
  components 4–9 (σ/σ_null ≈ 1.5). Survives removing per-user-per-round form
  (`make svd-resid`). One number is not enough.
* **D2** — axis 1 ≈ easy-implementation vs. hard-graph/DP (corr with rating −0.47,
  i.e. mostly "solving above your weight"); the recurring topical contrast is
  constructive/greedy/math vs. dp/data-structures/trees/graphs.
* **D3** — cluster × tag agreement is only 1–2 Jaccard points above random
  (k-means 0.097 vs 0.094; spectral 0.131 vs 0.108); clusters follow difficulty /
  division, not tags.
* **D4** — nearest-neighbour Jaccard is small (median top-1 ≈ 0.12), so 32×4 banding
  finds nothing; 128×2 with 256 hashes examines 1.4 % of pairs at recall@10 = 0.84
  on the full population. Wall-clock speed-up is < 1 because sparse BLAS brute force
  is already fast at n = 36k.
* **D5** — `make demo H=tourist`: tourist's top twins are jiangly, Radewoosh, ksun48, …

Robustness / extra runs: `make extras` (residualized SVD, k = 60 spectrum,
clustering on the residualized axes).

## Layout

```
src/cfskills/
  api.py       polite Codeforces client (1 req / 2 s, retries)
  fetch.py     contest selection + slim caching           -> data/raw
  matrix.py    surprise matrix S, mask M, users, problems -> data/processed
  svd.py       SVD, permutation null, axis tables         -> D1, D2
  cluster.py   k-means / spectral, Jaccard vs tags        -> D3
  lsh.py       MinHash LSH, evaluation, twins             -> D4
  demo.py      handle -> fingerprint + twins              -> D5
  robust.py    held-out prediction, split-half stability, Elo-model null,
               rating-band re-runs, tag prediction        -> outputs/R_*
  plots.py     redraws every figure used in the report   -> outputs/report_figs
  paths.py     file locations (override with CFSKILLS_DATA / CFSKILLS_OUT)
app.py         streamlit demo
tests/         synthetic-data unit tests
report/        report.tex (IEEE, 4 pages) -> report.pdf, and a short report.md
```

## Notes / gotchas

* `contest.standings` is only served to anonymous callers with `contestId` as the
  *sole* parameter (API change). The default already hides unofficial participants.
* Only official single-member `CONTESTANT` rows with a rating change are used;
  team rounds and unrated rounds are skipped automatically (see `data/raw/manifest.json`).
* Problem ratings/tags come from `problemset.problems`; problems without a
  rating are dropped.
* SVD/BLAS may hang inside heavily sandboxed shells; run the pipeline from a
  normal terminal.

## Known limitations (stated upfront in the proposal)

* Filling unobserved pairs with 0 biases towards finding *no* structure.
* Problem ratings are themselves estimated from solve data (mild circularity).
* Div. 3/4 and Educational rounds are rated only for lower-rated users.
* Only in-contest solves are used, so every surprise is measured under the same
  time pressure.
* The first component often captures "form" (a user being systematically
  above/below their rating in the sampled window) rather than a topical skill;
  `--center` in `cfskills.svd` removes per-problem means, and the D2 tables let
  you check what each axis is.
