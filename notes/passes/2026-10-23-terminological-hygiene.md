# Terminological hygiene pass (23 Oct 2026)
<!-- SUMMARY: rerun of the registered pass on the text after commit 26ecc10; mechanical layer flags only the abstract's lower-case "ordinary head" (real) plus source names and corpus short forms (free); 6 drift groups found (17 repairs), all proposed, none applied · status: awaiting Brett · updated: 2026-10-23 -->

Run by Claude (Opus 5.5) on the working tree after commit `26ecc10`, as a report only. Nothing has been applied. The 18 Oct run of this pass (`2026-10-18-terminological-hygiene.md`) is the baseline. Its 13 repairs held, except as listed below.

## Mechanical layer

`check-terms.py fusion-of-functions-revisited.tex --follow-inputs --gate`:

- **ordinary Head, unglossed in front matter.** This is real. The abstract's last sentence says "things an ordinary head can do". That is lower case and generic, and it collides with the paper's term (repair T1).
- **permission, unglossed.** It is glossed at its first use in §2, by a definition after a colon ("a word may head a nominal, with or without a determiner before it"). The checker doesn't read that as a gloss. No change.
- **Acronyms.** COCA, NOW, TIME, CNN, OC, JL, GT, API, REL, and GAP are corpus short forms (Brett's choice, 23 Oct, with URLs in the references), source names, and tree labels. Free.

## The paper's contrasts

The 18 Oct list, plus four distinctions added since then:

1. category / function (determinative / determiner; noun / head; adjective / modifier)
2. fusion (Det–Head, Mod–Head) / ordinary Head, with CGEL's *pure head* for a head with no second function
3. ordinary Head (NPs without a relative clause) / the head analysis (fused relatives)
4. licence (how fusion states a list) / permission (how ordinary Head states it)
5. NP / nominal / noun; head / ultimate head; *new:* a word stands for the phrase it heads "where nothing turns on the difference" (§2)
6. bare (no determiner) / standing alone (no determiner and no noun) / after a determiner
7. bare relative (no relative word) / relative with a relative phrase
8. the function inside the relative clause / the matrix function
9. derive / state; condition, list, permission, exception
10. the first departure (two functions) / the second (change of category)
11. *new:* two functions / two parents. Two parents occur in Det–Head and fused relatives, not in Mod–Head (§2).
12. *new:* gap (a node in one analysis) / relativization (the observable). Changed in §7 and Table 2 today.
13. *new (D2):* a second function (what the evidence favours in fused relatives) / fusion (CGEL's statement of it)
14. relative word / relative phrase (*whatever size*, §7)

## Drifts and proposed repairs

| # | Where | Current | Repair | Contrast |
|---|---|---|---|---|
| T1 | abstract, last sentence | "things an ordinary head can do" | "things a head with no second function can do" | 2 |
| T2a | abstract | "There fusion is favoured, though not forced." | "There a second function is favoured, though not forced." | 13 |
| T2b | §2, "This paper doesn't take those analyses on" | "the balance favours fusion only in fused relatives" | "the balance favours a second function only in fused relatives" | 13 |
| T2c | §7, end of the case paragraph | "So case favours fusion here rather than forcing it." | "So case favours a second function here rather than forcing it." | 13 |
| T3a | §7, last paragraph | "So the relative word's place in the clause shows in form" | "So the relative phrase's place …" (the paragraph now ends on "the relative phrase", and *whatever size* is a phrase) | 14 |
| T3b | §8 | "The relative word's function inside its clause shows" | "The relative phrase's function …" | 14 |
| T4a | §3, signpost | "the correspondence with the determiner use" | "the correspondence with the dependent use" (CGEL's term) | 1, house rule on *use* |
| T4b | §4, link paragraph | "if it licenses a fused modifier–head through the word's modifier use" | "… through the word's function as modifier" | same |
| T4c | §4, same sentence | "a word with no modifier use then can't head a nominal after a determiner" | "a word that can't function as modifier then can't …" | same |
| T4d | §4, first paragraph after Figure 2 | "don't distinguish its Det–Head use from its Mod–Head use" | "don't distinguish Det–Head *few* from Mod–Head *few*" | same |
| T4e | Table 1, second row | "A default from the modifier use" | "A default from the word's modifier function" | same |
| T4f | §5, footnote on the genitive | "Fusion predicts the gap for the Det–Head uses" | "… for the uses PHP analyse as Det–Head" | same |
| T5a | §4, PP sentence (added today) | "a position this PP can't fill" | "which this PP can't be" | house rule on *fill* |
| T5b | §4, *a few* paragraph (added today) | "*lucky* would occupy a slot inside the DP, modifying *few* rather than the nominal" | "*lucky* would be a modifier of *few* inside the DP, not of the nominal" | house rule on *slot* |
| T5c | §4, same paragraph | "or a slot after *a* inside the determinative" | "or a provision for a modifier after *a* inside the determinative" | same |
| T5d | Table 1, *a few* row | "a slot inside the determinative (p. 392)" | "a provision for a modifier inside the determinative (p. 392)" | same |
| T6 | §3, restrictor gloss | "a single post-head dependent that doesn't recur and can be a simple adjective" | "a single post-head dependent that can be a simple adjective". CGEL: "There can be no more than one" (p. 423), which "single" already says. "Doesn't recur" can be misread as non-recursive (Muse). | imported term |

Words: about +15 net.

## Checked and clean

- **Canon terms.**
  - *Determiner* is the function throughout. The new *we*/*us* gloss calls them determinatives.
  - *Part-of-speech* occurs only in a CGEL quotation, and *mothers* only in PHP's.
  - *Predicate* occurs only as CGEL's VP label and in a CGEL quotation.
  - There's no *mass*, *finite*, *word class*, or *class*.
  - *Predeterminer modifier* in full (fixed today).
- **The two senses of "gap".**
  - In §§3–6 and §8 "gap" means an absence: the pre-head gap and the genitive gap.
  - In §7 it means a node in one analysis. §7 refers to the absent adjective as "the missing pre-head adjective".
  - The two senses never share a section, so no change.
- ***Nominal base* and *noun base*.** These follow PHP exactly: "a nominal base (·body, ·one, ·thing …)" for the compounds and "a noun base ·ce" for *once* (pp. 587–588). This is an imported term in its author's sense. It sits near the paper's *nominal* (Nom), but changing it would misquote the source.
- ***Bare determinative* and *determinative standing alone*.** They are synonyms throughout and never conflict. No change.
- **Licence and permission.** They are kept apart: fusion "licenses", and ordinary Head and the head analysis state "permissions". The verb *license* for a complement licensed by an antecedent noun (§3) is the ordinary syntactic sense, and the collocation keeps it apart.
- **Two functions and two parents.** These are now consistent with §2's convention. In §1 ("the constituents with two parents it avoids"), §6 ("constituents with two parents stay in one construction"), and §8 the claim is about two parents, and it is true as stated.
- ***Fusion*, the second function, and *head analysis*.** After today's D2 edits, §1, §7's last paragraph, and §8 say "a second function", stated as fusion. The three T2 places are what remains.
