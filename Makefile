PY ?= .venv/bin/python
PIP ?= .venv/bin/pip

.PHONY: help setup fetch matrix svd cluster lsh demo all quick test app clean

help:
	@echo "make setup    create .venv and install the package (editable)"
	@echo "make fetch    pull ~600 rounds from the Codeforces API (~40 min, resumable)"
	@echo "make matrix   build the surprise matrix S"
	@echo "make svd      D1 spectrum vs null, D2 skill-axis tables"
	@echo "make cluster  D3 cluster x tag agreement"
	@echo "make lsh      D4 LSH evaluation + skill twins for D5"
	@echo "make all      matrix svd cluster lsh (assumes fetch is done)"
	@echo "make robust   held-out prediction, split-half, Elo-model null, rating bands, tag prediction"
	@echo "make extras   robustness runs used in the report (svd-resid, svd-k60, cluster-resid, robust)"
	@echo "make quick    end-to-end smoke test on 25 contests (~2 min of API time)"
	@echo "make demo H=tourist   D5 fingerprint + twins for a handle"
	@echo "make app      streamlit demo"
	@echo "make test     unit tests on synthetic data"

setup:
	python3 -m venv .venv
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev]"

fetch:
	$(PY) -m cfskills.fetch $(ARGS)

matrix:
	$(PY) -m cfskills.matrix $(ARGS)

svd:
	$(PY) -m cfskills.svd $(ARGS)

cluster:
	$(PY) -m cfskills.cluster -k 8 --min-obs 1000 --spectral $(ARGS)

lsh:
	$(PY) -m cfskills.lsh $(ARGS)

# robustness runs used in the report
svd-resid:
	$(PY) -m cfskills.svd --residualize-contest --suffix _resid $(ARGS)
svd-k60:
	$(PY) -m cfskills.svd -k 60 --n-perm 10 --suffix _k60 --max-axes 0 $(ARGS)
cluster-resid:
	$(PY) -m cfskills.cluster --svd outputs/svd_resid.npz --suffix _resid -k 8 --min-obs 1000 --spectral $(ARGS)

robust:
	$(PY) -m cfskills.robust all $(ARGS)

all: matrix svd cluster lsh
extras: svd-resid svd-k60 cluster-resid robust

# small end-to-end run to check the pipeline before the overnight pull
quick:
	$(PY) -m cfskills.fetch --max-contests 25
	$(PY) -m cfskills.matrix --min-participations 3
	$(PY) -m cfskills.svd -k 10 --n-perm 5
	$(PY) -m cfskills.cluster --n-axes 3
	$(PY) -m cfskills.lsh --n-sample 500 --min-tokens 2

H ?= tourist
demo:
	$(PY) -m cfskills.demo $(H)

app:
	.venv/bin/streamlit run app.py

test:
	$(PY) -m pytest -q

# IEEE-style PDF (uses the tectonic binary in .venv/bin; figures come from outputs/)
report:
	cd report && ../.venv/bin/tectonic report.tex

clean:
	rm -rf data/processed outputs/*.png outputs/*.csv outputs/*.md outputs/*.json outputs/*.npz outputs/*.gz
