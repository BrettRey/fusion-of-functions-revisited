# Numbers audit (23 Oct 2026)
<!-- SUMMARY: second-model numbers audit by Codex (read-only, staged public inputs): 93 numeric claims, 88 match, all Table 2 cells match; three real defects corrected (a mislabelled "three nothing", a wrong single attribution for two lines, two scaled percentages without "about"); four "no source" flags were a staging artifact · status: done · updated: 2026-10-23 -->

**Who ran it.** The house rule requires a second model family, so Codex ran the audit (codex-cli 0.163.0, through `tools/codex/bin/codex-readonly`: read-only sandbox, ephemeral, user configuration ignored). Claude chose Codex during the unattended run; Brett hadn't answered the question.
- **Inputs:** a staging copy holding only `drafts/*.tex`, `EVIDENCE.md`, the 29 records it links from the evidence repo, and three labels files. All are public.
- **Archive:** prompt, report (saved verbatim by Claude), trace, input hashes, and manifest are in `reviews/numbers-audit-codex-20261023/` (private).

**Result.** 93 numeric claims: 88 MATCH, 1 DERIVED-INCONSISTENT, 4 NO SOURCE.
- Every Table 2 cell matches its record, and each percentage agrees with its count at the precision given.
- No numbers are stated more finely than their denominators support.
- No two sections disagree.
- Codex reproduced several counts independently from the labels files (the 321 *lucky few* lines and every category, the genitive counts, the 94 and 82 *few would* lines).

## Defects found, checked by Claude against the records, and corrected

| # | Where | Was | Now | Record |
|---|---|---|---|---|
| N1 | §4 footnote on *lucky few* | "and three nothing (a headline, a fragment, and a web post)" | "and three no determiner (a headline, a fragment, and a web post with only *other* before the adjective)" | The adj-few record's own list gives the third line as *other less fortunate few* (l. 103), labelled OTHER. A correction note is appended to the record. |
| N2 | §3 footnote on the restrictor | "*a certain someone special* twice (*Independent Online*, 2013)" | "… twice (*Independent Online*, 2013; hindustantimes.com, 2025)" | The a-adj-someone record, ll. 12: two different publications. |
| N3 | §7, register split | "narrows to 65% against 58%" | "narrows to about 65% against 58%" | Gaps-and-matrix record, ll. 100–110: scaled estimates, not sample ratios. The paper marks estimates with "about". |

## Flags that aren't defects

- **"Five are attested", "one of them from 1884", "four come just after", "five attestations" (§4).** Codex found no local record for three of the five: *lucky both of us*, *Poor all of us*, and Anstey's *Poor somebody!*. Their sources are the evidence-index rows (rows 37–38): web URLs and the Project Gutenberg text, checked on the pages by Claude on 23 Oct. The staging copied only the evidence repo's records, so Codex didn't see them. Sourced.
- **"labelled in two runs" (§2 data note).** Codex notes that the double labelling is documented for the seven-word genitive batch, and that the later *another's* figures are chart counts, which were never labelled line by line. The data note says "the genitive lines", which fits that scope.
- **Codex's human-oversight caveat.** The audit shows the paper agrees with its records. It can't authenticate the human checks the records report, or the classifications behind them, since the raw lines are private. That's accurate and stays as a limit.

## Quarto note

The paper has few computed numbers outside §7's table, so moving to Quarto isn't worth it at this stage. The table's estimates come from scaling in the record, and the audit found them consistent.
