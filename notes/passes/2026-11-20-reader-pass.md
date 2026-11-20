# Reader pass, 20 November 2026
<!-- SUMMARY: straight-through read of the built PDF after the November genitive, length, outside-read and privileged-few edits; 6 proposed edits (2 seams from today's edits, 1 repetition, 1 citation example, 2 optional rewordings) · status: batch approved by Brett and applied, 14,993 words · updated: 2026-11-20 -->

**What was read.** The built PDF (27 pages, 14,999 words by `pdfwords.py`, sha256 5ecae4c341d1086a…), uncommitted on top of 6b19d1f. It includes:
- the outside-read batch (`reviews/reader-read-20261120/batch/`);
- the *privileged few* update to §4 and its footnote.

I read it in order, from the title page through the Conclusion, in one sitting, by Claude Opus 5.5. The previous straight-through read was 24 October (`2026-10-24-reader-pass.md`). Since then, two November batches and today's fixes have changed prose in every section.

**Mechanical pre-pass.**
- No `make check` target.
- `pointer_check.py`, on the main file and each section file: flags only for the paper's defined term "the second function" and its ordinals ("the second departure", "the first sentence"). Each resolves within its paragraph, so there's nothing to fix.
- `refcheck.py` reads only the main file. Its findings are model names in the AI-use statement and macros used in the section files.

## By section

- **Front matter and §1.** The abstract and introduction now match the body on fused relatives (*whoever*'s case answers to both functions). The introduction's "Fusion gets all three from the rules for relative clauses with a relative phrase" is discussed under finding 5.
- **§2.** The order holds: categories and functions, Figure 1, fusion's two departures, ordinary Head, the three commitments, the criterion, then data and methods. "With two mothers" now sits beside PHP's quotation, and the Mod–Head qualification follows. The methods paragraph now runs to November and says "105 labels".
- **§3.** The preview names three places (correspondence, morphological forms, case), and the order fact is "taken up below". It arrives under "Second, form", which is broader than the preview's "morphological forms". A reader can resolve that, because the preview says one fact of order favours fusion, so I left it (Grok raised the same point).
  - The genitive section reads in order: the CGEL claim, the singulars in edited prose, *all*/*many*/*some* in NOW, *many people's* against *many's*, *few* left open, the compounds, the dilemma, what each analysis lists, number.
  - **Finding 1**: the dilemma's first horn opens "If *many's* is out because…", two paragraphs after the paper shows *many's* in edited news and calls *to many's surprise* fine. Batch 1 created this when it added the *many's* evidence and left the horn's premise as it was.
  - **Finding 2**: "As stated, neither analysis predicts the division" repeats the previous paragraph's last sentence.
- **§4.** The *lucky few* determiner sentence and footnote 18 carry the *privileged few* counts.
  - **Finding 3**: my cut of "searched for" this afternoon left the footnote opening "COCA, *lucky*, *chosen*, …", which reads as a list that includes COCA.
  - **Finding 4**: "*we*, *us*, and *you* are determinatives in *we students*" gives an example with only *we*. CGEL p. 412 covers *what*, *we* and *you*; p. 422 calls it "the *we/you students* construction".
  - The three questions on pronouns and proper nouns are posed, answered first, second, third, and summed up. The summary skips the second because it found no advantage.
- **§5.** It holds; "(1b)" refers back correctly to the bare count noun.
- **§6.** "Below the line is the trade" comes before Table 1, which floats to p. 19 after the §7 heading. I tested two other placements in a scratch build: `[H]` left p. 18 nearly empty and made 28 pages, and `[t]` before the heading deferred the table to p. 25 because it's too tall. Under the current `[tp]`, p. 18 (§6) and p. 19 (Table 1) face each other in print, so the placement stays. The closing sentence on what ordinary Head saves now agrees with footnote 30 (inner fusion removed, outer kept).
- **§7.** The order holds: examples, the head analysis, Figure 3, the shared NP evidence, then the three properties with (5), Figure 4, (6) and Table 2, then PP fused relatives and the summary.
  - The "capped frequency list" qualifier sits on the 2,458 alone, which is right: the 17 Oct record shows the pronoun list complete and the verb list capped at 1,000 types.
  - **Finding 5**: the closing "Fusion gets all three from the rules for relative clauses that have a relative phrase" and its twin in the introduction. Two outside readers took them to mean fusion derives the whole case profile. The claim is that the rules are already in the grammar for ordinary relatives. That's Brett's call: a rewording is proposed for his explicit yes, and it's held without one.
- **§8.** It matches the body, including "Noun-phrase fused relatives" (§7 extends only the subject property to PP ones).

## Sweeps

- **Places that still treat *many's* as excluded in the paper's own voice.** I checked every `\mention{many's|few's|all's|some's}` in `drafts/`. The only one is the dilemma (finding 1). The others are CGEL's claim reported, its starred *many's expenses*, or *many's* as the rare side of the division.
- **Places listing the personal determiners before *few*.** Only the §4 sentence and footnote 18, and both are updated. Row 27 of `EVIDENCE.md` is updated too.
- **Footnotes that open with a query description.** The others open with a `\texttt` query string, so only footnote 18 had the problem.

## Proposed

Batch `reviews/reader-pass-20261120/batch/` (gitignored), 6 edits, 14,999 → 14,992 words with all of them. Edits 5 and 6 need Brett's explicit yes.

**Applied (20 Nov).** Brett approved the batch as sent ("approved"), which covers rp5 and rp6. After his review, on an advisor check, rp1 was narrowed: "a fused word's case" became "a fused determiner–head's case", because §4 says CGEL states no case requirement for modifiers. Build clean, 27 pages, 14,993 words.
