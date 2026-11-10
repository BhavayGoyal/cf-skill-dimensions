# Works with GNU make on Linux/macOS and on Windows (Git Bash / MSYS make).
ifeq ($(OS),Windows_NT)
BIN ?= .venv/Scripts
PYTHON ?= python
else
BIN ?= .venv/bin
PYTHON ?= python3
endif
PY ?= $(BIN)/python
PIP ?= $(BIN)/pip

.PHONY: help setup fetch matrix svd cluster lsh demo all quick test app clean robust extras plots report

help:
	@echo "make setup    create .venv and install the package (editable)"
	@echo "make fetch    pull ~600 rounds from the Codeforces API (~75 min, resumable)"
	@echo "make matrix   build the surprise matrix S"
	@echo "make svd      D1 spectrum vs null, D2 skill-axis tables"
	@echo "make cluster  D3 cluster x tag agreement (k=8)"
	@echo "make cluster-k2  D3 with k chosen by silhouette"
	@echo "make lsh      D4 LSH evaluation + skill twins for D5"
	@echo "make all      matrix svd cluster lsh (assumes fetch is done)"
	@echo "make robust   held-out prediction, split-half, Elo-model null, rating bands, tag prediction"
	@echo "make extras   robustness runs used in the report (svd-resid, svd-k60, cluster-resid, cluster-k2, robust)"
	@echo "make plots    redraw every figure used in the report from outputs/"
	@echo "make report   build report/report.pdf (needs pdflatex or tectonic)"
	@echo "make quick    end-to-end smoke test on 25 contests (~3 min of API time)"
	@echo "make demo H=tourist   D5 fingerprint + twins for a handle"
	@echo "make app      streamlit demo"
	@echo "make test     unit tests on synthetic data"

setup:
	$(PYTHON) -m venv .venv
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev,app]"

fetch:
	$(PY) -m cfskills.fetch $(ARGS)

matrix:
	$(PY) -m cfskills.matrix $(ARGS)

svd:
	$(PY) -m cfskills.svd $(ARGS)

cluster:
	$(PY) -m cfskills.cluster -k 8 --min-obs 1000 --spectral $(ARGS)

# k picked by silhouette (gives k=2); written to D3_*_obs1000*
cluster-k2:
	$(PY) -m cfskills.cluster --min-obs 1000 --suffix _obs1000 --spectral $(ARGS)

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
extras: svd-resid svd-k60 cluster-resid cluster-k2 robust

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
	$(BIN)/streamlit run app.py

test:
	$(PY) -m pytest -q

plots:
	$(PY) -m cfskills.plots $(ARGS)

# IEEE-style PDF; figures come from outputs/report_figs
report: plots
	cd report && (pdflatex -interaction=nonstopmode report.tex && pdflatex -interaction=nonstopmode report.tex || tectonic report.tex)

clean:
	rm -rf data/processed outputs/*.png outputs/*.csv outputs/*.md outputs/*.json outputs/*.npz outputs/*.gz
