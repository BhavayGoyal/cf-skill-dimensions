# Is One Number Enough? Hidden skill dimensions in Codeforces ratings

Vishnu Sinha & Bhavay Goyal — CS 328. The full 4-page write-up with figures is
`report.pdf` (source `report.tex`; `make report`). Figures live in
`outputs/report_figs/` (`make plots`). This page is the short version.

## Question
Codeforces gives every user one rating. After subtracting what Elo predicts, is there
still consistent structure in who solves what? What is it, do the setters' tags
capture it, and who are a user's "skill twins"?

## Data
589 rated rounds, 36,519 users (≥ 40 rounds), 3,773 problems, 15.8 M user–problem
outcomes from the public Codeforces API. Surprise `s = solved − Elo expectation`.

## Findings
| | result | evidence |
|---|---|---|
| **One number is not enough** | yes | singular values clear a column-shuffle null and an Elo simulation; rank-10 improves held-out log-loss 7.7 % over Elo (3.6 % beyond Elo + offsets); ~6 dimensions reproduce on odd vs. even rounds (0.90–0.60 vs. ≤ 0.03) |
| **What the axes are** | a difficulty slope (axis 1, corr. −0.47 with problem rating) and an ad-hoc (math, constructive) vs. algorithmic (data structures, trees, graphs) contrast (axis 8, corr. −0.11) | `D2_axes.md`, `fig_axes` |
| **Do tags match?** | weakly | clusters beat random by only 0.3–2.3 Jaccard points; axes help predict ad-hoc tags (math 0.53 → 0.62 AUC), not dp/trees/graphs; a user × tag model gains 4.7 % over Elo vs. 7.8 % for rank-10 SVD, and tags add 0.1 point on top of the axes |
| **Does it replicate?** | the main pattern, not the fine dimensions | on 458 older rounds (2016–21, no shared problems) all 20 components beat the null; 2,253 shared users score alike on dimension 1 (0.73), weakly on 2–3 (0.49, 0.36), not beyond; tag signatures recur (0.53–0.81 vs. ≤ 0.47) but five axes match the same older axis |
| **Skill twins / LSH** | nearest neighbours are far apart (median top-1 Jaccard 0.12) | planned 32×4 banding: 72 candidates, recall 0.003; 128×2: 1.4 % of pairs, recall@10 0.84, but 43 s vs. 12 s brute force |

## Caveats
Zero-filling unseen pairs; problem ratings estimated from solve data; most
observations are 800–1400 problems; only in-contest solves; with 15.8 M entries
even tiny effects are significant, so effect sizes matter more than the count of
significant components; LSH skips buckets > 2,000 users; users' skills drift between eras, so cross-era agreement understates true stability.

New to the project? `GUIDE.md` in the repository root explains everything from scratch.

## Reproduce
```bash
make setup && make test && make fetch && make all && make extras && make report
```
