# Overnight passes, 23–24 Oct 2026
<!-- SUMMARY: index of the unattended pass run after Brett's "push on as much as you can without me"; four lists (applied, proposed, checked clean, deferred), updated after each pass · status: done; 38 corrections and fixes applied, proposals await Brett; nothing committed · updated: 2026-10-24 -->

Run by Claude (Opus 5.5) after Brett's 22:40 sign-off. Text baseline: the working tree after the terminology repairs and redundancy cuts (uncommitted; last commit `26ecc10`).

**Rules for the run.**
- **Applied:** wording changed only where a source or record contradicts the text, where an edit already applied broke a cross-reference or transition, or where a term breaks a rule Brett approved today.
- **Added during the reader pass (a fourth condition):** an objective in-order defect (a pointer with no antecedent or the wrong one, a term used before its introduction, a wrong cross-reference, a small-caps duplicate), fixed by naming the referent.
  - Three of those fixes go further and are marked † in the reader-pass report for Brett to keep or revert: F11 (a new summary sentence in §4), F16 (content added to §3's number hedge), F24 (rewords a sentence from Brett's option (b)).
  - A fourth, F8a ("lowest head" for *ultimate head*), was reverted. It's now proposal R13.
- **Proposed:** everything else, with exact wording.
- No commits, no pushes.
- Codex ran on Claude's judgment, since Brett hadn't answered whether to use it. It ran read-only, in a staging copy holding only public inputs.

**Pass order:** contribution-alignment, level-category-audit, negative-claims-audit, numbers-audit (Codex), source-reread as a claim ledger (Claude read all 206 pairs; the second-model judgment the plan proposed didn't run overnight, see Deferred), reader-pass (a fresh read-only agent), then the prose passes as reports only, then the mechanics passes.

## Applied

Tally: negative claims 1 (two parents), numbers 3, source reread 12, mechanics 1, reader pass 21. Total 38.

- **Mod–Head can have two parents** (negative-claims pass, `2026-10-23-negative-claims.md`).
  - PHP's tree (24) on p. 590 (*the more than once which would have been permitted*) gives the fused DP a parent in each of two nominals. Checked in the page image.
  - §2's new convention sentence said "not in Mod–Head", and §4 said "both functions belong to the same nominal". Both are corrected: §2 says "usually … though in their tree for *the more than once* …, the fused DP has a parent in each of two nominals (p. 590). So two functions don't always mean two parents", and §4 says "both functions here".
  - The verdict is unaffected. Logged in DECISIONS.
- **Numbers audit by Codex** (`2026-10-23-numbers-audit.md`): 93 numeric claims, 88 match, and all Table 2 cells match. Three fixes:
  - "three nothing" becomes "three no determiner (… a web post with only *other* before the adjective)";
  - *a certain someone special* "twice" credits both sources;
  - "about 65% against 58%".
- **Source reread** (`2026-10-23-source-reread.md`, done): all 206 page-cited claims read against their pages. 12 corrections:
  - **Wrong pages:**
    - CGEL's classification by function is on p. 410 (interpretation, pp. 333 and 411);
    - *all*/*both* in partitives, p. 413;
    - *main* attributive-only, p. 529;
    - §1's analysis of *whoever*, pp. 1073 and 1076.
  - **Six CGEL examples restored verbatim** in eight places, about +11 words: "I didn't like it *myself*", "How will *the new system* affect", "Kim*, as always,* chose", "would agree *with you*" (twice), "can't have read the report *carefully*" (three times).
  - **§5's sequential *once* example** is now PHP's own (*once you have finished*).
  - **§2's Wu footnote** adds pp. 184–185.
  - Charitable engagement was checked in the same read, with nothing to change.

- **Reader pass** (`2026-10-24-reader-pass.md`). A fresh read-only agent read the PDF in order and found 32 issues. 21 fixes were applied (a pointer, a term used before its introduction, a wrong cross-reference, or a small-caps duplicate). Three go beyond a pointer and are marked † (F11, F16, F24). F8a was reverted.
- **Mechanics:** one trailing-whitespace line.
- **Final build:** clean, 27 pages, 14,955 words (45 under JL's limit).

## Proposed (Brett to decide)

- **contribution-alignment** (`2026-10-23-contribution-alignment.md`):
  - A1, say in the abstract that the result is conditional ("Holding the grammar's other commitments fixed, I argue …").
  - A2, "ordinarily" becomes "outside a few exclamations".
- **level-category-audit** (`2026-10-23-level-category-audit.md`):
  - L1, "In usage, the form answers to both functions" (§7).
  - L2, "The uses PHP analyse with fusion" (§5).
  - L3, "points to", not "reflects" (§7).
- **Reader pass, structural** (`2026-10-24-reader-pass.md`), most consequential first:
  - R1, "ordinary Head" names two things in §7, footnote 28, and Table 1;
  - R2, §3's signpost against its one positive fact;
  - R3, the summaries leave out §4's third question;
  - R4, *%the both of us* reads as a pure head;
  - R5, "fusion, movement, and multidominance" overlap;
  - R6, the paper's fused-relative analysis appears only in a footnote;
  - R7–R12, a moved sentence, a moved data note, and four wording points.
  - Together about +110 words. Budget: 45.
- **Prose passes** (`2026-10-24-prose-passes.md`), all reports:
  - **Scar tissue:**
    - S1, cut "So two functions don't always mean two parents." (§2, −8 words);
    - S2, optionally shorten the *whichever* footnote's "since" clause (§7).
  - **Rhetoric and humour**, ranked:
    - H1, use the attested racing line *He's gone well the last twice* (*Racing Post*) in §5;
    - H2, optional "once or twice over" echo at the end of §5;
    - H4, a flagged closing joke for §8. The Lakoffian check advises against it.
  - **Lakoffian:** M1, the §7 heading becomes "Fused relatives: evidence for a second function". "Shows" presupposes the function, which §7 only favours.
  - **De-AI:** clean. Paragraphs opening "The X …" are noted for cadence only.

## Checked clean

- **contribution-alignment:** title, introduction, conclusion, and heading sequence.
- **level-category-audit:** target before mechanism, mereology. The corpus tables are used as tests, not as explanations.
- **negative-claims-audit:**
  - The paper makes no novelty claims.
  - Every corpus negative has its search in EVIDENCE.md or the text.
  - The source negatives are narrow and page-cited. "CGEL gives determinatives no use as the pure head" survives *the both of us*, which CGEL calls fused-head (p. 377).
- **numbers-audit:** 88 of 93 claims match, including every Table 2 cell. Several counts were reproduced independently from the labels files. The four "no source" flags were a staging artifact.
- **source-reread:**
  - 195 of 206 page references support the text as worded.
  - The quotation ledger still passes 69/69.
  - A whole-book search confirms that "CGEL mentions the genitive only for reciprocal *one another's*" holds.

- **build-integrity and validate-bib** (`2026-10-23-mechanics.md`):
  - clean build, 27 pages, 14,932 PDF words;
  - includes, symlink, and log clean;
  - one trailing-whitespace line fixed;
  - all 23 cited keys resolve.
- **de-ai-prose:** no structural tics; high-signal words rare and justified.

## Deferred or not run

- **density-leavening:** it conflicts with redundancy (run 23 Oct), and the registry says Brett reads one before the other runs.
- **proofread:** after Brett's decisions on the proposals above, so it reads the final wording.
- **bib-central-merge (`/push-bib`):** it edits the central bibliography, which is hook-protected and done at polish time with Brett.
- **review-board:** not wanted. Two referee simulations ran on 23 Oct.
- **plan-figures:** the figures are settled.
- **Venue decision record** (CLAUDE.md gate before submission). It needs Brett's alternatives and risk acceptance, plus a same-day check of JL's pages. Two fit signals are already known: PHP 2007 is a JL article, and Gisborne 2026 (cited in §7) is a JL article on mutual dependency in wh-clauses.
- **Second-model judgment of the claim ledger.** The plan Brett saw on 23 Oct said a model from another family would judge each claim–page pair, with Claude checking its flags. Overnight, Claude judged all 206 pairs alone and Codex checked only the numbers. The 12 citation corrections and the 195 supported verdicts are therefore one model's reading, the same model that wrote much of the paraphrase (the *up to twice* error was its own). A side agent caught the gap on 24 Oct. **Done that morning:** Codex judged all 206 pairs blind (`reviews/claim-ledger-codex-20261024/`). It flagged 11, none of them a page contradicting the text, and none of the overnight corrections. Six hold, as five word-neutral or near-neutral proposals (P1–P5 in the source-reread report); three were rejected against the page.
- **Anonymizing the evidence index** (the link names Brett) and archiving it with a DOI: a submission-package task, for Brett.

## Morning, 24 Oct: Brett's pasted review

Brett pasted an outside comparison of this draft with the previous PDF, with no comment of his own. It keeps the revision and asks for four local repairs, all applied:
- **§4:** "and fusion's derivation saves only that difference" becomes "though fusion's derivation saves the additional condition on determinatives". This replaces reader-pass fix F14, which the review called a regression.
- **§7:** the verbless *with* sentence is split back into two: "Ordinary Head is available here too. *Whomever I see* could be an NP headed by *whomever*, with a bare relative …".
- **§1 and §8:** "*CGEL* states that function as fusion" becomes "*CGEL* represents the two functions as fused".
- **§7:** "they don't choose among fusion, movement, and multidominance as ways of giving it one" becomes "they don't uniquely determine how that relation is represented". **This replaces wording Brett dictated on 23 Oct**, so it's flagged for him. It also settles reader-pass proposal R5.

Build: 27 pages, no undefined references, 14,954 words by the PDF count. JL's limit is 15,000 "including references, footnotes and any appendices", and the PDF count includes everything on the page, so it errs high.

**Later, 24 Oct.** Brett: "apply P1 through P5". All five Codex proposals are applied (details in the source-reread report). P1 took the longer form, naming PHP's null-head note. P5 restored Glass's full examples. Build: 27 pages, 14,968 words, 32 under the limit.

**Brett's decisions on the proposals, 24 Oct.** Applied: the P1 follow-on, R1, R2 (short), R3, R7, R8, R9, R11, R12, A2, L1–L3, S1, H1, M1, and the cut of §1's any-analysis clause. Kept: F11, F16, F24, S2, the review's §7 sentence, the *dog* examples. Not taken: R4, R6, R10, A1, H2, H4; R13 left. Build: 14,996 words, 4 under the limit. Full list in DECISIONS.
