# Terminological hygiene pass (18 Oct 2026)
<!-- SUMMARY: registered pass terminological-hygiene run by hand (passes.py crashed on this manuscript); mechanical check clean apart from source names; 11 drifts found in the paper's own contrasts, 1 canon issue (determiner as a category, in a gloss of Postal), 1 CGEL-fidelity issue in the trees; all 13 repairs applied the same evening at Brett's yes · status: applied; not in the pass ledger (passes.py crashes on this manuscript) · updated: 2026-10-18 -->

Run on the working tree after the example trims. Mechanical layer: `.house-style/check-terms.py` on the flattened manuscript. It flags *fusion of functions* as unglossed in the abstract (glossed there by the *some*/*few* examples; treat as free) and the acronyms TIME, CNN, JL, GT (source names and a quotation; free), plus tree labels. Nothing to change.

## The paper's contrasts

1. category / function (determinative / determiner; noun / head)
2. fusion (fused determiner-head, fused modifier-head) / ordinary Head; CGEL's *pure head* for a head with no second function
3. ordinary Head (determinatives, adjectives) / the head analysis (fused relatives, after Bresnan & Grimshaw)
4. licence (how fusion states a list) / permission (how ordinary Head states it), §2
5. NP / nominal / noun; immediate head / ultimate head
6. bare (no determiner before) / standing alone (no noun after) / after a determiner
7. bare relative (no relative word, CGEL's term) / relative with a relative phrase
8. function inside the relative clause / matrix function
9. derive / state; condition, list, permission, exception
10. the first departure (two functions) / the second (change of category)

## Drifts and proposed repairs

| # | Where | Drift | Repair |
|---|---|---|---|
| 1 | §2, last para of criterion | "the licences ordinary Head needs for fused relatives": contrasts 3 and 4 both slip (it's the head analysis, and its statements are permissions) | "and in fused relatives the permissions a head analysis needs count against it" |
| 2 | §1; §7 ×3 | the head analysis "needs licences no other head has" | "permissions" (contrast 4) |
| 3 | §7, subject relativization | "it heads its NP whether it's an ordinary Head … or a fused determiner-head": the analysis name used as a kind of head, and "heads its NP" where the ultimate head is meant | "it's the ultimate head of its NP on either analysis (Section 3)" |
| 4 | §1 | "I take the phrase CGEL fuses to be an ordinary head" (lower case, a common noun) | "a pure head" (CGEL's term, defined in §2) |
| 5 | §7 caption of Figure 6 | "whichever is an ordinary head" | "a pure head" |
| 6 | §7, infinitival relatives | "ordinary heads take infinitival relatives" | "other heads take …" |
| 7 | §4 | "they stand alone after *the*", the only use of *standing alone* for a word after a determiner (elsewhere it means no determiner; §6 contrasts "standing alone" with "after a determiner") | "they need no post-head modifier after *the*" |
| 8 | §6, departures; §7 footnote | "a bare fused relative", "Bare *whichever*": *bare* here means no noun, against the paper's other uses (no determiner; no relative word) | "a fused relative with *whichever* alone"; "*Whichever* alone, in …" |
| 9 | §1 | "bare relatives … can't do" and, one sentence later, "relatives without a relative word": the same notion under two names, the first unglossed | "bare relatives (those with no relative word) … though bare relatives can be" |
| 10 | §4 ×2 | "independent *few*": *independent* is CGEL's term for the genitive pronouns (*mine*) | "*few* with no noun after it"; the second becomes "Of these 321 lines" |
| 11 | §2, §3 | "its function in the main clause": wrong after a preposition inside an embedded clause; §7 says "matrix function" | "its function outside the relative clause"; gloss "matrix function" at its first use in §7 |

Canon: §2 footnote "pronouns can be analysed as determiners (Postal 1966)" uses *determiner* as a category. Postal's claim is that pronouns "are really articles, in fact types of definite article" (literature/Postal1969_On_so-called_pronouns.md). Repair: "as a kind of definite article".

CGEL fidelity: the trees for fused relatives (Figures 5a, 5b, 6) label the verb Head; CGEL's tree on p. 1073, which Figure 5a says it follows, has Predicator (checked in the PDF). Repair: Predicator. (The VP's label Predicate is CGEL's and stays.)

Checked and clean: *determiner* elsewhere always the function; no *word class*, *part of speech*, *mass*, *finite*, *mother/daughter/sister* outside quotations; *Nom* only in trees and quotations; *free relative* only in cited authors' terms (Kim, Gisborne, Grosu); *restrictor*, *peripheral modifier*, *ultimate head*, *predicand* glossed at first use; *Det–Head*, *Mod–Head* introduced with their full names.

Net words: about +10.

## Outcome

Brett: "yes" (all 13). Applied 18 Oct 2026; build clean, trees checked by eye after the Predicator relabel (pp. 22, 27). PDF-text count 16,311 (about 16,020 without tree labels). Not recorded in the ledger: `passes.py status` fails in `manuscript_fingerprint.figure_material`, which reads Figure 1's float body (`[H] \centering …`) as a file path (OSError: File name too long).
