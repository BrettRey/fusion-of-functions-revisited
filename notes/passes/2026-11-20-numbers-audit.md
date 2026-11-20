# Numbers audit, 20 November 2026
<!-- SUMMARY: Codex (GPT-6.2 Sol) checked the paper's counts against the evidence records before LingBuzz v2; the new NOW and lucky-few counts reconcile; 8 manuscript and 6 index corrections applied, 4 findings declined or verified · status: applied · updated: 2026-11-20 -->

**Who ran it, on what.**
- The audit was by OpenAI Codex (`gpt-6.2-sol`, per its run log) through the read-only wrapper, as the registry asks: a second model, not the one that wrote the numbers.
- Its input was a public-only copy: the manuscript source, the built PDF's text, `EVIDENCE.md`, the 31 records EVIDENCE.md links to, and the previous audit (2026-10-23). Private folders were left out.
- The text audited is the build after the reader pass (14,993 words).
- The raw report, prompt and logs are kept in the gitignored `reviews/numbers-audit-20261120/`.
- Claude (Opus 5.5) checked each finding against its record before any change.

**Result.**
- The NOW genitive counts in §3 (39/3/2/0; 2,264 against 6) reconcile with the 20 Nov record, and so do the merged *lucky few* counts in §4 (420; 260, 113, …).
- Arithmetic is correct throughout: every percentage agrees with its count at the stated rounding.

## Findings and dispositions

1. **§2: "The genitive lines in Section 3 were labelled in two runs."** Only the October COCA lines were. The November NOW lines were labelled once and recounted by a second run (NOW record, l. 6). *Applied*: "The COCA genitive lines…", and the same distinction in EVIDENCE.md's methods paragraph.
2. **§4 footnote 21: "*the two's* in 21 of 34 lines."** The query was `those|the two 's`, and the 21 include *those two's* (record ll. 58–63). *Applied*: "*the two's* or *those two's*", in the paper and in EVIDENCE.md.
3. **§4: "Five such exclamations are attested … four come just after …"**, and later "five attestations". The record (adj-compound-exclamatives, ll. 28–36) has seven more in NOW and iWeb: NOW 4, iWeb 3, with a repeated line set aside. The paper has been undercounting since 19 Oct, when a footnote mentioning them was cut.
   - Codex proposed "Five attested examples are given here". *Applied instead*, recounted from the record: "Twelve such exclamations are attested, one of them from 1884, and eight come just after the same exclamation with a proper noun or a pronoun, as in…", and "twelve attestations" later.
   - The eight are COCA 2, NOW 2, iWeb 2 and the two web partitives. The iWeb series after common nouns (*Poor girl, poor husband, poor everybody*) is left out of the eight because the sentence says "proper noun or pronoun".
   - EVIDENCE.md's "six more in NOW and iWeb, four closing a series" disagreed with its own record, and now reads "seven more …, five closing a series after a name or noun".
4. **§4 footnote 24.** Its description of the other 26 COCA lines left out two (a list and a depictive). *Applied*: the footnote now says "none with *somebody* or *someone* in the use; the same query finds seven more in NOW and iWeb". The full breakdown stays in the record. This saves 7 words, which pays for items 1, 2, 3 and 6.
5. **§4 EVIDENCE row: "nothing in 4".** The October web line has *other* before the adjective. *Applied*: "no determiner in 4", as the paper says.
6. **§7 Table 2: "about 37% (206 of 562)".** Both counts are scaled estimates (gaps-and-matrix record: "about 206 *whomever* and 356 *whoever*"). *Applied*: "about 206 of about 562", in the paper and in EVIDENCE.md.
7. **§7 footnote 32: "Of all 802 tokens before a pronoun".** Codex read this as possibly including *it*. The 802 already excludes *it*, and the sentence before says so. *Applied*, at no word cost: "Of the 802 tokens".
8. **§7: 352 of 2,458 presented as a preposition-object count.**
   - *Declined in part.* The paragraph already says the matrix function is the same "in nearly every token", and the caption defines the search frames. The record gives the sensitivity check (excluding the 43 clause-taking cases found: 350/2,399, about 15%).
   - *Applied*: Codex's narrower point that the caption "counts frequency-list rows" when 2,458 is a sum of token frequencies. The caption now says "sums".
9. **§4: CGEL's "one or two nouns formed by conversion".** *Verified, no change.* CGEL p. 423 n. 43 reads "There are one or two nouns formed by conversion from compound determinatives".
10. **§7 footnote 29: "CGEL gives two less certain cases".** *Verified, no change.* CGEL p. 1055 [68 i–ii] gives the *it*-cleft and existential examples, "at the boundary between very informal and non-standard", and the "could not be misconstrued as predicate of the matrix clause" clause.
11. **EVIDENCE.md's publication note.** It said the NOW record's link wouldn't resolve until the next push. *Updated*: that link has resolved since this morning (HTTP 200), and every linked record is on the evidence repo's `master` once the *privileged few* record is cherry-picked there.

**After.** The build has no errors, 27 pages and 14,996 words (`pdfwords.py`). Batch record: `reviews/numbers-audit-20261120/batch/`, applied unseen on Brett's instruction ("Deal with all the rest of this as best you can. I'm going to the gym").

The paper is quantitative but stays in LaTeX. Its figures come from hand-run corpus queries rather than computed analyses, so Quarto inline code would have nothing to compute; this pass and the evidence records are the drift check.
