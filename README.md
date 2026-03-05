# NonlinearCorr SoftwareX Submission Package

This folder is a GitHub-upload-ready bundle for the SoftwareX submission of `acedcor`.

## 1) What this package contains

- `paper/swx.tex`: main SoftwareX manuscript source
- `assets/img/`: figures used by the manuscript
- `data/v3/`: A1/A2 summary CSV outputs
- `code/v3_scripts/scripts/generate_weekly_assets.py`: weekly asset generation utility
- `docs/`: change reports and weekly addendum notes
- top-level reproducibility/config files: `REPRODUCIBILITY.md`, `requirements.txt`, `setup.py`, `LICENSE`

## 2) Suggested GitHub location

Upload this folder at repository root as:

`github_release_package/`

Example URL after push:

`https://github.com/ssangmin-junior/acedcor-softwarex/tree/main/github_release_package`

## 3) Minimal reproducibility flow

From repository root:

```bash
python -m pip install -r requirements.txt
# (If needed) regenerate selected figures / assets
python V3/scripts/generate_weekly_assets.py
```

Main manuscript source:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error swx.tex
```

## 4) SoftwareX review-facing files

- `docs/SOFTWAREX_REVIEW_CHECKLIST.md`: line-by-line revision checklist for manuscript updates
- `docs/CHANGE_REPORT_2026-03-03.md`: tracked change summary
- `docs/WEEKLY_REPORT_2026-03-03_ADDENDUM.md`: high-order extension write-up

## 5) Notes

- This package includes the high-order heteroscedasticity extension (`x^5`, `x^7`, `x^9`) reflected in manuscript tables and narrative.
- For transparent review, table values and scenario assumptions are documented directly in `swx.tex` and linked change reports.