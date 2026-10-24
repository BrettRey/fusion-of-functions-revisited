# Source reread: claim ledger (23–24 Oct 2026)
<!-- SUMMARY: every page-cited claim outside a quotation (206, from tools/claim_ledger.py) read against its page by Claude overnight, then judged blind by Codex on 24 Oct (the second-model step the plan proposed, skipped overnight); verdicts below · status: done; 12 corrections applied overnight; Codex flagged 11 of 206, none a contradiction; 6 hold, as 5 proposals for Brett · updated: 2026-10-24 -->

**Method.**
- `tools/claim_ledger.py` (new, beside `quote_ledger.py`) finds every page reference outside a quotation, attributes it with the quotation ledger's rules, and groups the citing sentences under the text of the cited page.
- Claude read each page against every claim citing it. No second model judged the pairs overnight, though the plan Brett saw proposed one; see the overnight index. Codex judged them blind on 24 Oct ("Second-model check", at the end). The working file (486 KB, page texts included) is regenerated on demand and isn't kept.
- The tool sometimes attributes a page to the wrong source when two are named nearby: "PHP p. 423" is CGEL's, and "CGEL pp. 7, 12–13" are Glass's. Those were judged against the right source.
- Charitable engagement was checked in the same read: is CGEL's and PHP's position stated as they state it, where the paper disagrees?

**Verdict key.** OK = the page supports the claim as worded. FIXED = the page contradicts the wording, and the minimal correction is applied. NOTE = supported, with a point worth Brett's attention.

## PHP (Payne, Huddleston & Pullum 2007): 57 references, pp. 565–600

All OK except:
- **FIXED.** §5, "sequential *once*, as in *once he arrived*" (pp. 584, 592–594). PHP's examples are *I will leave once you are all ready* (p. 584) and *Once you have finished, report to me!* (p. 593). In a sentence citing PHP, the constructed example read as theirs. It is now *once you have finished*.
- **FIXED earlier tonight** (negative-claims pass). §2 and §4 on Mod–Head and two parents. P. 591 confirms it in words: in (24), *more than once* "functions simultaneously as the modifier within the higher nominal, and the head of the nominal which contains the relative clause".
- **NOTE.** §4 gives PHP's adjacency example as \**the in the room very hard of hearing* (p. 580 n. 17). PHP's form has a null head, \**the Ø in the room very hard of hearing*, because the example is aimed at a silent-head analysis, which the paper's next sentence says. Fine as is.
- **NOTE.** PHP p. 575 says, of PP, AdjP and AdvP fused relatives, that "standard relative clauses are modifiers only within Nom". GPT Pro was right that this is about attachment, not subject relativization, so the cut made earlier tonight stands.
- **NOTE.** PHP p. 596 distinguishes "predeterminer" as a category name in other grammars from "predeterminer modifier" as a function "in our own usage", which supports Brett's terminology rule.

Checked OK (all others): C002, C005, C007–C011, C016–C018, C048–C049, C055, C057, C059–C060, C066–C067, C083–C084, C086, C090, C096–C098, C101, C119, C137 (apart from the example), C138–C153, C159–C160, C162, C172–C173, C178, C181, C183–C184, C191, C196, C203.

## Bresnan & Grimshaw 1978; Gisborne 2026; Glass 2019; Grosu 2003

All OK: C092, C094, C106, C167, C177, C197, C204, C205.
- **NOTE.** §7 says "on either analysis, the match with the gap comes from the relative clause". On Bresnan and Grimshaw's analysis, it comes from their agreement condition between the head and the gap (p. 353), which the paper takes up two paragraphs later. That's loose rather than wrong. Muse raised it too (§7P6).
- C095 (Glass pp. 12–13, "She derives both from the adjective's own meaning"): the tool attributed it to CGEL. Checked against Glass separately; see below.

- C095 (Glass pp. 12–13): OK. Glass derives both readings from the adjective's state denotation by two type-shifters, (34)–(36).

## CGEL (Huddleston & Pullum 2002): 132 references, all read

**FIXED, wrong page:**
- §2, "CGEL classifies fused heads twice, by function and by interpretation (p. 333)". P. 333 classifies "according to the syntactic category of the head" and by structure and interpretation. The classification by function (determiner–head, modifier–head) is on p. 410. Now: "by function (p. 410) and by interpretation (pp. 333, 411)".
- §4, "and so are *all* and *both* in partitives (pp. 376, 412)". P. 412 doesn't discuss them. P. 413 does ("only the universal quantifiers *all* and *both* occur freely as fused head in partitives"). Now pp. 376, 413.
- §4, "*Main* is attributive-only (p. 558)". P. 558 lists *main* among the particularising attributives. The explicit statement, "restricted to attributive function (e.g. *mere*, *former*, *main*)", is on p. 529. Now pp. 529, 558.
- §1, "*whoever* is head of the subject noun phrase and also subject of the relative clause (CGEL, p. 1076)". P. 1076 has the example but not the analysis. The analysis is on pp. 1073–1074. Now pp. 1073, 1076.

**FIXED, CGEL's examples shortened.** Examples presented as CGEL's had lost words. They're restored verbatim, as the source-grounding rule asks (copy exact data). Six examples in eight places, about +11 words:

| Where | Was | CGEL |
|---|---|---|
| §4 (2b) | *I didn't like it, but I respect the views of the many who did.* | *I didn't like it **myself**, but …* (p. 416, [21iii]) |
| §4 (2e) | *How will **it** affect the very poor?* | *How will **the new system** affect the very poor?* (p. 417, [29iii]) |
| §4 (2f) | *There were two pieces left and Kim chose the larger.* | *… and Kim**, as always,** chose the larger.* (p. 419, [33ii]) |
| §2 | *Many people would agree* / *Many would agree* | *… would agree **with you*** (p. 421, [38ii]; also p. 1073) |
| §1, §7 (4b), §7 footnote | *Whoever told you that can't have read the report.* | *… the report **carefully**.* (p. 1076, [24i]) |

Checked verbatim and unchanged:
- *Four boys played croquet and two played tennis* (p. 332);
- *He made ten mistakes but most were fairly trivial* (p. 333);
- *I prefer cotton shirts to nylon* (p. 417);
- the four case examples in (5) (p. 1074);
- *I spent whatever he gave me* and *I'll go wherever you go* (p. 1068);
- the p. 1055 relative-clause examples;
- the p. 1508 *the of the missing* example.

**NOTE:**
- §3, "*all*, *much*, and *little* take a restrictor (*little new*), as they share *else* with the compounds (p. 423)". P. 423 supports the *else* clause only. That these three take a restrictor rests on Brett's judgments (19 Oct; *There's little new in the report*), and the citation sits on the *else* clause, so the sentence is accurate as written.
- §2, "In *Many would agree with you*, … *many* jointly realises the determiner and head functions" (p. 1073). This confirms that CGEL's own analysis uses the full form of the example.
- C072, "CGEL mentions the genitive only for reciprocal *one another's*". A whole-book search for *another's* finds only *one another's* (pp. 428, 1502). Holds.

**OK** (all others), including:
- C001, C003 (after the fix), C004, C006, C013–C014, C019, C021, C023–C027, C029–C032, C034–C039, C041, C043–C047, C050–C054, C056, C061–C065;
- C068–C077, C079–C082, C085, C087–C089, C091, C093, C099–C100, C102–C105, C107–C113, C115–C117, C120–C136;
- C154–C158, C163–C166, C168–C171, C174–C175, C179–C180, C182, C185–C186, C188–C195, C198–C202, C206.

## Others

- C012 (Quirk et al. p. 421) is a quotation, checked by the quotation ledger.
- C040 (von Fintel p. 43): OK. "the index on the determiner, which is interpreted as the resource domain".
- C176 (van Riemsdijk p. 349) and C187 (Kim p. 364): OK.
- Matthews (C033, C114, C118): OK.
- Wu:
  - C020 **FIXED**: §2's footnote said Wu puts an empty noun "after *the rich* and after a determinative standing alone (pp. 19–20, 118, 173)". Those pages cover *the rich*; the determinative case is pp. 184–185, (44). Now pp. 19–20, 118, 173, 184–185.
  - C042 and C141: OK.

## Charitable engagement

Where the paper disagrees with CGEL or PHP, it states their position in their own terms, usually quoting them:
- the genitive argument (p. 420);
- the *nylon* objection (p. 421);
- adjacency (p. 571 and n. 5; p. 580 n. 17; p. 584);
- the compounds' morphology (pp. 565, 587–588);
- PHP's "never" (p. 588).

The paper also states where it agrees: CGEL's three commitments, the category arguments (p. 420; PHP pp. 586–589), and the pre-head adjective fact, which it concedes to fusion as "a real advantage". The one place a referee from that side might call the reading uncharitable is §5's use of PHP p. 588 n. 30 (*·ce* as a reanalysed genitive) against their noun-base reading. PHP raise it themselves as historical, and the paper reports it as their note, so it's fair.

## Totals

206 page references read:
- 12 corrected (five citation fixes: four wrong pages plus Wu's missing pages; six shortened examples restored in eight places; one example attribution in §5);
- one more corrected earlier tonight (two parents in Mod–Head);
- the rest supported.

## Second-model check (24 Oct, Codex, blind)

**Why it ran.** The plan Brett saw on 23 Oct had a model from another family judging every pair. Overnight that didn't happen: everything above is one model's reading, by the model that wrote much of the paraphrase. A side agent caught the gap on the morning of 24 Oct.

**How.**
- Codex (`gpt-6.1-sol`, codex-cli 0.163.0, read-only wrapper) judged all 206 claims on the current working tree, so the 12 corrections above were under test too.
- Four chunks: PHP 56, CGEL pp. 333–434 95, CGEL pp. 465–1518 36, other sources 19.
- **Blind:** each chunk had the claim sentences and the cited page text, with the drafts (comments stripped) for context. It had no verdicts and no word of which claims had been corrected.
- The tool's three source slips were corrected before staging (C059 is CGEL's; C095 and C096 are Glass's).
- Run record (private): `reviews/claim-ledger-codex-20261024/`, with prompt, chunks, four reports saved verbatim, traces, and manifest.
- Claim IDs below are from this run's ledger. They differ by one or two from the overnight IDs above, because the text moved.

**Result.**
- 195 SUPPORTED.
- 7 OVERSTATED or NOT SUPPORTED.
- 2 EXAMPLE ALTERED.
- 2 UNCHECKABLE, for lack of page text.
- No WRONG PAGE.
- None of the 12 overnight corrections was flagged.

Claude checked all 11 flags against the page text. None shows the page contradicting the text, so nothing was applied. Six hold, as five proposals for Brett (P1–P5); three don't; two were uncheckable for Codex and are confirmed below.

**Proposed (Codex flag holds).** *All five applied 24 Oct at Brett's word ("apply P1 through P5"); P1 in its longer form, P5 by restoring Glass's full wording. Build after: 14,968 words.*
- **P1 (C021, §2 footnote): CGEL's grounds are against ellipsis, not every silent head.**
  - The footnote separates ellipsis analyses from empty-noun analyses, then says "CGEL gives its grounds against a silent head on pp. 420–421".
  - Those pages argue that "Ellipsis does not provide a general solution either" (p. 420). The argument is that no separate head can be reinstated, and that gapping differs from the NP construction. That doesn't touch an empty noun, which needs no reinstating.
  - PHP do raise a problem for a null head licensed by an AdjP (p. 580 n. 17).
  - Proposed: "*CGEL* gives its grounds against ellipsis on pp. 420–421, and PHP note a problem for a null head (p. 580 n. 17)." About +8 words; "against ellipsis" alone is word-neutral.
  - Related question for Brett: §2's "three commitments that *CGEL* argues for" includes "no silent head noun". CGEL argues the ellipsis half.
- **P2 (C065, §3): the page reference sits on a claim it doesn't support.**
  - "*all*, *much*, and *little* take a restrictor (*little new*), as they share *else* with the compounds (p. 423)".
  - P. 423 says only that the compounds share with "the determiner-heads all, much, and little the property of taking else or … more".
  - That they take a restrictor rests on Brett's judgments (EVIDENCE row 23: *There's little new in the report*, *Not much interesting happened*, *All interesting was sold*).
  - Proposed, word-neutral: "and *all*, *much*, and *little*, which share *else* with the compounds (p. 423), take a restrictor (*little new*)".
- **P3 (C201, §7): "which is what *CGEL*'s question marks record".**
  - The question marks are on the *whomever* clashes (p. 1074, [18iii–iv]).
  - The other half of "no fully acceptable form" is CGEL's remark on *whoever*, which the sentence quotes next.
  - Proposed, word-neutral: "which is what *CGEL*'s judgments record".
- **P4 (C141, §5): "PHP's own note takes *·ce* to be a reanalysed genitive ending".**
  - PHP p. 588 n. 30: on the compound analysis, "This would represent a reanalysis", and the sibilant "has plausibly been reanalyzed as a lexical (derivational) formant".
  - Proposed, word-neutral: "PHP's own note suggests *·ce* is a reanalysed genitive ending".
- **P5 (C093, C095, §4): two Glass examples are cut short without a mark.**
  - Glass p. 10 has "The weak and mutated die, the healthy survive to pass on their genes"; p. 7 has "The crazy [in that academic repository] is easily detected and easily ignored".
  - The paper ends both early, and the second already marks an internal omission with an ellipsis.
  - Overnight, CGEL's shortened examples were restored in full. Here a final `\ldots{}` on each is word-neutral, and restoring them costs +9.

**Not taken:**
- **C070**, "*a lucky few*, which *CGEL*'s analyses of *a few* allow two ways (pp. 353, 392)". "Allow" is the paper's own reading of what the two analyses provide (a plural head after *a*; a modifier inside the determinative, Table 1). P. 392 lists *very*, *good*, *fair*, and the sentence doesn't claim CGEL lists *lucky*.
- **C105**, "*we* and *us* are determinatives in *we students*; *CGEL*, p. 412". P. 412 names the lexeme *we* ("What, we, you … in determiner function they are determinatives"), and *us* is a form of it. Codex's fix (drop *us*) would misstate CGEL.
- **C027**, "unlike an NP, it needn't follow the verb directly (p. 1018)". CGEL draws the contrast in these terms itself: "Content clauses, on the other hand, are not constrained to follow the verb in this way", after setting aside the special cases of NP objects.

**Uncheckable for Codex, checked by Claude:**
- **C012**, Quirk et al. p. 421 ("Adjectives can function as heads of noun phrases"). §7.23 falls between the p. 420 and p. 422 running heads in the local Markdown, so it's on p. 421. The quotation ledger had checked the wording only.
- **C041**, von Fintel p. 43: "the index on the determiner, which is interpreted as the resource domain" is on printed p. 43 (PDF p. 57).

**Dependence.** Codex saw only what Claude staged, and the claim–page attribution is Claude's tool. A claim citing the wrong source altogether would pass if the wrong source happened to support it. Codex reported no such case.

**One more, applied:** Codex's notes for the CGEL pp. 465–1518 chunk (not a table verdict) said the §7 quotation "has to satisfy the case requirements of both the relative clause and the matrix clause" crosses a page break. It does: p. 1073 ends at "…relative clause and", and p. 1074 opens with "the matrix clause". The citation is now "pp. 1073–1074". The page contradicted the text, so this falls under the overnight rule.

