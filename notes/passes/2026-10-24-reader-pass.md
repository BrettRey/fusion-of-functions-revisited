# Reader pass (24 Oct 2026)
<!-- SUMMARY: in-order read of the built PDF by a fresh read-only agent (32 findings); Claude checked each against the text, applied 21 pointer/cross-reference fixes (three of them go beyond a pointer and are marked for Brett), and proposes the structural ones with exact wording; biggest: "ordinary Head" names two things in §7, §3's signpost vs its one positive fact, §4's third-question result missing from the summaries · status: fixes applied; structural proposals await Brett · updated: 2026-10-24 -->

**Who and how.** A fresh-context read-only agent (`responsibility-reader`) read the built PDF in order, after tonight's source corrections. It wasn't told what had changed. Its report is saved verbatim in `reviews/reader-pass-20261024/REPORT.md` (private; the manifest has the PDF and report hashes). Claude checked every finding against the source and sorted them:
- **Applied:** a pointer with no antecedent or the wrong one, a term used before its introduction, a wrong cross-reference, or a small-caps duplicate. In each case the fix names the referent and changes no claim.
- **Proposed:** anything that changes an argument, a summary, or the paper's layout.

## Applied (21)

Marked † are the fixes that go beyond naming a referent. They're listed so Brett can revert them in one look.

| Finding | Where | Was | Now |
|---|---|---|---|
| 4 | §5 | "the adjective under the trade counted for *few*" ("trade" arrives only in §6) | "the adjective under the comparison Section 4 made for *few*" |
| 8b | §1 | "Fusion derives that from adjacency" (explained only in §3) | "… from the adjacency of the two fused functions" |
| 9 | §7 | "*CGEL* drew this analogy itself." (no analogy stated before it) | "*CGEL* itself links this case requirement to the genitive." |
| 10 (pointer part) | §3, end | "Section 6 weighs the pre-head adjective …" | "Sections 4 and 6 weigh …" (§4 weighs it first) |
| 11 † | §4 | "The compounds are clearer." (clearer than what?) | "With the compounds, the line follows category." A new summary sentence, not just a pointer repair. |
| 12 | §3 | "an analysis that gives no reason for the gap" (the referent of "gap" had just changed) | "… for the genitive gap" |
| 13 | §4 | "Other partitives are untested. Five are attested" (read as five partitives) | "Five such exclamations are attested" |
| 14 | §4 | "fusion's derivation saves only that one" | "… saves only that difference". **Superseded 24 Oct** by the review Brett pasted: "though fusion's derivation saves the additional condition on determinatives" |
| 15 | §8 | Pointers had shifted: "(Sections 4 and 5)" hung on *once* alone | First sentence "(…; Sections 2 and 4)", second "(Section 5)" |
| 16 † | §3 | "where plural heads take the genitive (*the poor's*, *the two's*; Section 4)" (§4 shows *the few's* almost never) | "where plural heads differ (*the poor's* and *the two's*, but hardly ever *the few's*; Section 4)". This adds content to the hedge, from §4's own figures. |
| 17a | §2 | `\term{fusion of functions}` reintroduced in small caps | plain (small caps only at first use, §1) |
| 17b | §2 | `\term{Ordinary Head}` reintroduced | plain |
| 18a | §3 | "(Table 1)" eleven pages early | "(Table 1, Section 6)" |
| 18b | §6 | "the results of Sections 3–5" (the table includes §2's *nylon*) | "Sections 2–5" |
| 19 | §7 | (4c) reintroduced as new: "PP fused relatives (*I'll go wherever you go*, p. 1068)" | "PP fused relatives, as in (4c)" |
| 20 | §5 | "the link … that Section 4 examined for *few*" | "… examined for determinatives" |
| 24 † | §3 | "The gap favours it:" ("it" unclear) | "The gap favours determiner over modifier:". The sentence is from option (b), which Brett chose on 23 Oct; same meaning, but revert if he prefers his wording. |
| 25 | §4, opening | A colon hung examples (3) on the *nylon* clause | full stop |
| 26 | §4 | "Their main Mod–Head case" (nearest plural: "both functions") | "PHP's main Mod–Head case" |
| 31 | §5 | "Their further example" (PHP a paragraph back) | "PHP's further example" |
| 32 | §2, first sentence | "The framework keeps categories apart" | "*CGEL*'s framework keeps …" |

Not changed:
- **Finding 27.** "both functions here belong to the same nominal". *Here* refers to the trees just cited (PHP pp. 579–580, 588), which do have one nominal, so the sentence is accurate. §2 carries the general hedge.
- **Findings 32b, 32c.** "sidestep it" (= the question just asked) and "both lines" (= the two restrictions just stated) resolve.

## Proposed (Brett to decide)

**Brett's decisions, 24 Oct.** Applied: R1 (revised form), R2 (short form), R3 (revised form), R7, R8, R9, R11, R12. Not taken: R4, R6, R10. R13 left as is. R5 settled by the review. F11, F16, F24 kept. Build after: 14,996 words.

**R1 (finding 1, structural): "ordinary Head" names two things.**
- §7 introduces the head analysis by applying ordinary Head to fused relatives ("Ordinary Head is available here too …"). So that's ordinary Head extended, which §7 argues against.
- But footnote 28 and Table 1 use "ordinary Head" for the paper's grammar, which keeps the outer fusion in fused relatives ("Ordinary Head removes the inner fusion … and keeps the outer one").
- Proposed wording:
  - §1: "On the alternative, the head analysis, which extends ordinary Head to fused relatives, the relative word simply heads the nominal …"
  - §2: "For the heads *CGEL* fuses in a noun phrase without a relative clause, ordinary Head keeps the second departure and drops the first."
  - §7: "A one-function analysis is available here too." Since 24 Oct the next sentence is the review's "*Whomever I see* could be an NP headed by *whomever*, …", so only the subject of the first sentence changes. and "… and that condition. It's the head analysis of Section 1 (Figure 3b)." The second replaces "and I'll call it the head analysis", which also re-introduces the term (finding 17).
  - Footnote 28: "The analysis favoured here removes the inner fusion …".
- About +20 words. The terminology pass traced ordinary Head against the head analysis and missed this. It shows only in order.

- **Revised 24 Oct, after the review Brett pasted.** The review restored "Ordinary Head is available here too", so the §7 change above would undo its wording. A check of every use of "ordinary Head" shows that only two places use it to mean the paper's whole grammar rather than the one-function analysis: the *whichever* footnote ("Ordinary Head removes the inner fusion … and keeps the outer one") and Table 1's cell "None outside fused relatives (Section 7)". Revised proposal: the footnote becomes "The grammar defended here removes the inner fusion …" (§8's phrase; +3), and the cell becomes "None (for fused relatives, see Section 7)" (+1), since the cell continues "; term-of-office *once* a modifier …". §7 stays as the review has it. Optional: §1's "the head analysis, which extends ordinary Head to fused relatives" (+7).

**R2 (finding 2, structural): §3's signpost against its one positive fact.**
- "The function shows in none of them" (the three places), then two pages later "The pre-head side does favour fusion, and it's the only fact … that does".
- Proposed: "The function shows in none of them, though the compounds lead to one fact of order that favours it, the missing pre-head adjective." (+18 words.)
- Brett cut an earlier §3 signpost (second-round triage, "not taken"), so this is his call.

**R3 (finding 3, structural): §4's third question went fusion's way, and the summaries drop it.**
- §4 finds that nothing about proper nouns or *the real me* predicts \**Remaining few were the hangers-on*: "fusion's adjacency does".
- The next summary ("So ordinary Head's condition is of a kind the grammar already has …") and §6 and §8 carry only the first question's result.
- Proposed §4 summary: "So on the first question, ordinary Head's condition is of a kind the grammar already has; on the third, only adjacency derives the gap, and a semantic motivation would only motivate it. Fusion's derivation, the one fact of form that favours the determiner function (Section 3), saves less than PHP suggest, but not nothing." A matching clause would follow in §6's verdict paragraph.
- This touches D1's balance, so it's Brett's.
- **Revised 24 Oct.** The review's §4 repair now ends the first-question paragraph "though fusion's derivation saves the additional condition on determinatives", so "but not nothing" would say it twice. Trimmed §4 summary: "So on the first question, ordinary Head's condition is of a kind the grammar already has, but on the third, only fusion's adjacency predicts the gap. Fusion's derivation, the one fact of form that favours the determiner function (Section 3), saves less than PHP suggest." (+8.) Matching §6 clause, after "(*CGEL*, p. 430": ", except that only adjacency predicts \**Remaining few were the hangers-on*" (+10).

**R4 (finding 5): *%the both of us* against "CGEL gives determinatives no use as the pure head".**
- The negative holds: CGEL calls *the both of us* one of the "Fused-head NPs of this kind" (p. 377, checked tonight).
- But §4's wording ("heads a nominal after *the*", "words that head without modifying") reads as a pure head.
- Proposed §4 clause: "… heads a nominal after *the* in *%the both of us*, still a fused head for *CGEL* (p. 377)." (+8 words.)

**R5 (finding 6): "fusion, movement, and multidominance".** *Settled 24 Oct:* the review Brett pasted made the same point, and its wording was applied ("they don't uniquely determine how that relation is represented").
- §2 has already described fusion as giving one constituent two parents ("a directed acyclic graph"), so fusion is itself a kind of multidominance. The list reads as three rivals when the first is a case of the third.
- Proposed (keeping Brett's three-way point): "… but they don't choose between fusion and its rivals, such as a null head with a fronted relative phrase (PHP, p. 578), as ways of giving it one."
- Or keep the list and add a footnote saying which multidominance analyses are meant.
- Brett asked for this sentence on 23 Oct.

**R6 (finding 7): the paper's own analysis of fused relatives is only in footnote 28 and Figure 4.**
- Proposed body sentence in §7's summary paragraph, after "So a second function is favoured here, though not forced": "On the grammar favoured here, the fused element keeps both functions, and only the inner Det–Head of a word like *whichever* goes (Figure 4)." (+25 words.)

**R7 (finding 10, the move): §4's closing line.**
- "Nothing in the form of Mod–Head expressions, then, shows the modifier function" closes two and a half pages about the Det–Head gap.
- Proposed: move it to just before "Mod–Head is also where the advantage …", where it closes the Mod–Head material it summarises.

**R8 (finding 21): the data note comes after examples that rely on it** (the COCA line in (1d), and the COCA search in the *double* footnote).
- Proposed: move "Examples are *CGEL*'s or PHP's where cited …" to just before "The criterion answers *CGEL*'s objection …".

**R9 (finding 23, clarity).**
- Proposed §3: "Bare determinatives take no pre-head adjective (\**nice anyone*, \**Lucky few escaped*), apart from a few exclamations in which the compounds and partitive *all* and *both* take one (*Poor everybody!*, *Poor all of us!*; Section 4)."

**R10 (finding 28).**
- Abstract: "the case of *whoever* answers to its function inside the clause" could add "as well as to the whole phrase's" (+7), matching §1 and §8.
- §8's "Noun-phrase fused relatives" is accurate, since case applies only to NPs. Keep.

**R11 (finding 29).**
- §6's last sentence names the saving "for each determinative or adjective that heads a nominal". That leaves out the *nylon*-type nouns and *once*.
- Proposed: "for each word *CGEL* fuses in a noun phrase without a relative clause".

**R12 (finding 30): the footnote on the 52% check.**
- "about 200 lines of each form … 131 of the 148 *whoever* lines" looks inconsistent. The 148 are the lines not before *it*.
- Proposed: "A check of about 200 displayed lines of each form found, among those not before *it*, non-subject relativization in 181 of 182 *whomever* lines and 131 of 148 *whoever* lines." Figures from the gaps-and-matrix record, confirmed by the Codex audit.

**R13 (finding 8a): *ultimate head* in §1 before §2 defines it.**
- Tonight Claude changed it to "lowest head", then reverted that, because it put an undefined synonym beside a defined term.
- Options: leave the forward use, which a reader can follow from context; or gloss it inline at first use ("the ultimate head of a noun phrase, the word its head relations lead down to") and make §2's definition a reminder.

**Not proposed: finding 22** (two routes named for three commitments). §1 and §2 say each route gives up one commitment, not that every commitment has a named route. The pronoun analysis is taken up where it matters (§3).

## Word budget

The final build after these fixes counted 14,955 words, 45 under the limit. The revert of 8a since then is net zero. Proposals R1–R12 together would add about 110. Something would have to give: the redundancy pass's restatements are already cut, so the candidates are the optional proposals themselves (R6, R10, R2).
