"""cfskills: hidden skill dimensions in Codeforces ratings (CS 328 project).

Pipeline (each module is runnable with ``python -m cfskills.<module>``):

    fetch   -> data/raw/           (Codeforces API pull, cached to disk)
    matrix  -> data/processed/     (users x problems surprise matrix S)
    svd     -> outputs/            (D1 spectrum vs null, D2 skill-axis tables)
    cluster -> outputs/            (D3 cluster x tag agreement)
    lsh     -> outputs/            (D4 MinHash LSH evaluation + skill twins)
    demo    -> stdout              (D5 handle -> fingerprint + twins)
"""

__version__ = "0.1.0"
