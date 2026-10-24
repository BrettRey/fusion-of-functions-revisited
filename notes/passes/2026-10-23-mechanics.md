# Build integrity and bibliography (23–24 Oct 2026)
<!-- SUMMARY: build-integrity and validate-bib run overnight on the working tree: clean build (14,932 PDF words, 27 pp.), includes resolve, no pinned TeX Live path, references.bib is the central symlink, no biber warnings, one 4 pt overfull box, one trailing-whitespace line fixed; all 23 cited keys resolve with author/title/year · status: done · updated: 2026-10-24 -->

Run by Claude (Opus 5.5), overnight, after the source-reread corrections.

## build-integrity

1. **Includes resolve.** `manuscript_fingerprint.py` reports no unresolved `\input`.
2. **No pinned TeX Live path** in `.house-style/preamble.tex` or the main file.
3. **`references.bib` is the symlink** to `../../../.house-style/references.bib`. Additions are in `references-local.bib`.
4. **Full build** (`make`: XeLaTeX, biber, two more passes). Exit 0, 27 pages, 14,932 words by the PDF-text count (references and running heads included).
5. **Log.** No undefined citations or references, no LaTeX or package errors, and no biber warnings. One overfull hbox of 4.2 pt is too small to see.
6. **`git diff --check`.** One trailing-whitespace line (`drafts/fused-relatives.tex:114`) was fixed. Now clean.

## validate-bib

- 23 distinct citation keys across the main file and `drafts/`.
- All resolve to the central bibliography or `references-local.bib`, and none is defined in both.
- Every cited entry has an author (or editor or organization), a title, and a year (or date).
- Not checked here: whether the entries' details match the published works. The central bibliography's own workflow covers that (`/push-bib` at polish time, needed before submission).
