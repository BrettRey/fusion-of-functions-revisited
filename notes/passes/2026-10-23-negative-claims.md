# Negative-claims audit (23 Oct 2026)
<!-- SUMMARY: about 40 negatives found; no novelty claims; corpus negatives all have their searches in EVIDENCE.md; source negatives are narrow and page-cited; checking them found one false negative-shaped claim of today's making (Mod–Head never has two parents), corrected; nothing else to change · status: done (one correction applied) · updated: 2026-10-23 -->

Run by Claude (Opus 5.5), overnight. The search pattern covered the explicit forms ("there is no", "the first to", "novel", "to my knowledge", …) and the implicit ones ("found no", "gives no", "cites none", "never", "untested", "absent", "has no"). It returned 75 hits across the drafts; about 40 are claims rather than examples or quotations.

## Novelty claims

None. The paper doesn't claim to be first.
- It credits its alternative to precedents. §2 says ordinary Head "is close to the traditional analysis" (Quirk et al.). It also says CGEL "considers the analysis itself, as 'change of function without change of category'" (p. 421).
- §7 credits the head analysis to Bresnan and Grimshaw, and Gisborne's related line.

## Corpus negatives: all evidenced

Each has its query, corpus, and date in `EVIDENCE.md` or in the text.

| Claim | Where | Evidence |
|---|---|---|
| No adjective phrase as predeterminer modifier before a definite determiner, apart from one marginal *400-fold the amount* | §2 footnote on *double* | EVIDENCE row 2 (COCA, 17 Oct; predeterminer-adjps record) |
| No genitive for *few*; none for *all* in a capped display | §3 genitive footnote | EVIDENCE row 3 (per-word counts and the display cap) |
| *the few/many 's* gave none | §4 genitive footnote | query in the text |
| No line with *somebody*/*someone* in the exclamation use | §4 footnote | query in the text (`poor\|lucky\|silly everybody\|everyone\|somebody\|someone`) |
| No relevant *this last once* or *the last once*; *the last twice* absent from COCA | §5 | EVIDENCE rows 41–42 (plain-string controls included) |
| No genitive of *once*, *twice*, or *thrice* | §5 footnote | EVIDENCE row 43 (query `once/twice/thrice 's`; reported by Brett, no lines) |
| 82 of 94 *few would* lines have no NP or named set in the context | §3 footnote | count with its denominator |

## Negatives about named sources: narrow, page-cited

Each is already in the narrow form ("this source does not do X", with a page). Checked:
- **"CGEL gives determinatives no use as the pure head of a nominal"** (§3, §6). This was the likeliest to fail, through *%the both of us*, where *both* can't be an internal modifier. But CGEL calls it one of the "Fused-head NPs of this kind" (p. 377, checked in the PDF), so it isn't a pure head there. The claim holds.
- **"for *many*, as in *many of us*, CGEL gives no argument that picks determiner over modifier"** (§3). CGEL's only basis is the correspondence with the dependent use. That basis doesn't separate the two for a word with both dependent uses, and §6 says so ("the match is how the function is chosen, not evidence for it"). It holds as narrowed.
- **"they cite none for Mod–Head"** (§4: PHP's formal differences). Their formal differences are *none* (p. 581) and the *-ever* forms (p. 576). Their Mod–Head evidence is order (adjacency, p. 580 n. 17), which §4 takes up next. The 17 Oct PHP audit, a full read of pp. 565–600, found no Mod–Head morphology argument. Holds.
- **"CGEL … states no case requirement for modifiers"** (§4). CGEL's case argument (p. 420) is about the determiner function. Holds.
- **"the reflexive pronouns, which have no genitive either (p. 426)"**, **"*None* has no pure-head use to test (p. 410)"**, **"an analysis that gives no reason for the gap (p. 420)"**, and **"CGEL finds 'no evident explanation' (p. 1067)"**: each has a page, and the last is checked by the quotation ledger.

## The one that failed: a negative-shaped claim of today's making

§2's new convention sentence said a constituent with two functions has two parents "in Det–Head and in fused relatives, but not in Mod–Head". §4 said "Unlike Det–Head, both functions belong to the same nominal". PHP's tree (24) on p. 590 (*the more than once which would have been permitted*) gives the fused Mod–Head DP a parent in each of two nominals, as the page image shows. The 17 Oct PHP audit had noted it (row 48).

**Applied:** §2 now says "both functions usually belong to one nominal (pp. 582, 588), though in their tree for *the more than once which would have been permitted*, the fused DP has a parent in each of two nominals (p. 590). So two functions don't always mean two parents". §4 now says "both functions here belong to the same nominal". Ordinary Head's claimed saving is unaffected, since on ordinary Head two-parent constituents occur only in fused relatives.

## Open by declaration (honest, no change)

These say what wasn't tested, which is what this pass wants:
- "*Every* … whose status I leave open" (§3);
- "Other partitives are untested" (§4);
- "which I haven't tested" (§4, the article in web *select few*);
- "though I haven't tested how far that holds" (§4);
- "is untested" (§3, *scant*);
- "I leave open" (§7, how the two functions interact).
