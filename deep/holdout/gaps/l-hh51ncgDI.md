# Gap analysis: Algorithms Explained, minimax and alpha-beta pruning (l-hh51ncgDI)

Real length 661 s (about 10:46 of speech). Captions automatic (some mis-heard words). Format: the older "Algorithms Explained" series, not a Coding Adventure. Predicted script: `scripts/l-hh51ncgDI.md`. The script's "explicit predictions" are in its section 4 (brief says section 5); I scored those.

## 1. Real beat sheet (compact)

| m:ss | Type | Tags | Paraphrase |
|---|---|---|---|
| 0:00 | H | roadmap | Hypothetical: a program that plays a turn-based game; one part is the search that looks ahead. No intro, no hook beyond the framing |
| 0:15 | H | toy-world, minimal-definition-then-refine | White dot is a position; simplify to two moves per position; the branches become a tree |
| 0:28 | N | minimal-definition-then-refine | Expand to the end or a depth limit; leaves need a static evaluation |
| 0:42 | N | analogy, minimal-definition-then-refine | Static evaluation defined; crude chess version is material count; high favours white, low favours black, so white maximises, black minimises |
| 1:10 | N | act-it-out, special-case-first | Walks the first leaves (-1, 3), parent takes 3; then 5 and 1; black takes the lowest; the other half quickly; root value +3 |
| 2:22 | I | notation-after-concept | Code for minimax: position, depth, maximizing flag; base case; max variable starts at negative infinity, loop over children, recursive call flips the flag |
| 3:45 | I | notation-after-concept | Minimising branch mirrors it; return the value |
| 3:56 | N | visible-repetition | Steps the same tree again with the code on screen: recursion down, values passed up; stops the blow-by-blow early |
| 5:06 | N | visible-repetition, minimal-definition-then-refine | Same tree a third time for pruning; after the first leaf of a branch, a bound "at least 5" appears; the rest can be ignored, pruned |
| 5:47 | N | visible-repetition | A second prune on the other side from a bound "at most -4"; result identical to the unpruned run |
| 6:12 | N | design-it-yourself | Deeper tree; half of it passes with nothing pruned; pruning is not guaranteed and depends on move order; best-first ordering; chess capture example |
| 7:06 | N | inline-quiz | Asks the viewer to pause and decide whether the second leaf can be pruned; answer at 7:20 with the bound reasoning |
| 7:49 | N | visible-repetition | Finishes the tree: another bound "at most 2", prune; final best path |
| 8:02 | I | notation-after-concept | Alpha-beta in code: add two parameters tracking each side's best guarantee; update alpha for max, beta for min; break when beta is at most alpha |
| 8:44 | N | visible-repetition | Final trace of the same tree with alpha and beta values passed down, starting at negative and positive infinity; prune when the bounds cross; second side of the tree |
| 10:18 | N | recap | One-sentence recap: minimax, sped up by pruning branches a side will never allow |
| 10:31 | H | callback-to-hook | Closing: last moves of the game where a computer first beat a reigning world champion at classical time controls (no sign-off, no teaser) |

The same 8-leaf tree is walked four times, each with one extra overlay: values only (1:10), code recursion (3:56), prune marks (5:06), alpha and beta numbers (8:44). A second, deeper tree is used 6:12-8:02.

## 2. Prediction scorecard (script section 4)

| # | Prediction | Predicted | Actual | Verdict |
|---|---|---|---|---|
| 1 | First viewer question | none | a direct "pause the video" question at 7:06 | miss |
| 2 | First self-directed question about skipping | about 6:10 | 7:06 (the prune-or-not question) | near |
| 3 | Pseudocode on screen | 4:35 (42% of runtime) | 2:22 (22%) | miss |
| 4 | Alpha and beta named | about 7:40 | 8:02-8:15 (bounds in words from 5:21) | near |
| 5 | Algebraic formula | none | none (code and bound marks only) | hit |
| 6 | Misconception | none; he states pruning does not change the answer | none; states result is identical at 6:12 | hit |
| 7 | Dumb bot (random move) at 1:00 | present | absent; opens straight into tree | miss |
| 8 | Full minimax before pruning, about 5:20 | yes | yes, 1:10-5:06 | hit |
| 9 | Example count | 3-4 | 2 trees and 4-5 passes; no board game | near |
| 10 | Growth | tiny to bigger on the same tree, only the rule changes | 8-leaf tree reused four times, then a deeper tree | hit |
| 11 | Hook | project statement, no question or paradox | a hypothetical project statement, no question or paradox | hit |
| 12 | Ending | honest close, callback to trap, teaser, no recap | one-sentence recap, then a famous chess game; no caveat, no trap, no teaser | miss |
| 13 | Move: toy-world (tiny game and tiny tree) | both | tiny tree only | near |
| 14 | Move: act-it-out | present | present (1:10-2:22, prune walk-through) | hit |
| 15 | Move: notation-after-concept | present | present, earlier than predicted | hit |
| 16 | Move: visible-repetition with build-and-verify | rerun, leaf counts, same root | rerun four times, identical result stated at 6:12; no leaf counters | hit |
| 17 | Move: failure-shown (trap, explosion, bad ordering) | three failures | only bad ordering (6:26-6:39) | near |

**Hit rate:** 8 hit, 5 near, 4 miss of 17 = 47% strict, 61% counting near as half. Part of this is topic-driven (the algorithm dictates tree, walk, code, prune, ordering), not report-driven.

## 3. Structural alignment

Predicted and present: tiny abstract tree (0:15 vs 2:10 predicted); min-then-max walk with values bubbling up (1:10 vs 3:00); pseudocode after the walk (2:22 vs 4:35); pruning shown by a bound on a concrete branch (5:21 vs 6:50, the generator used 5 and 3, real used 5 and -4); alpha and beta named (8:15 vs 7:40); reruns of the same tree (3:56, 5:06, 8:44); move ordering matters, with chess captures as the example (6:26-6:53 vs 9:15); identical answer stated (6:12).

Predicted but absent (false positives): tic-tac-toe opening and trap position; dumb random-move bot; "it did not think about the reply" failure; trap replay; tree-size explosion with counters; evaluation-function skip caveat (real gives a one-line definition at 0:42); two bots head to head with timings; honest-caveat endings; teaser; callback to opening.

Present but unpredicted (false negatives): code walked in a second pass as recursion trace (3:56-5:06); a deeper second tree; the explicit pause-the-video quiz (7:06); automatic hand-off from "at least" and "at most" bounds before alpha and beta are named; a code diff framing for alpha-beta ("start from the original and add two parameters"); a final trace with infinity initial values; a one-sentence recap; an unrelated historic-game closer; no sign-off; no first-person devlog voice.

Timing drift on the big moments:
- Hook: predicted 0:00 roadmap with tic-tac-toe; real 0:00 hypothetical and white dot at 0:15. Hit.
- First new idea (minimal tree, evaluation): predicted 0:30; real 0:28. Hit.
- Payoff (root value then pruning): predicted root value at 3:55, pruning rerun at 8:30; real root 2:08, pruning 5:21. Early by 1:47 and 3:09.
- Code: 4:35 predicted, 2:22 real (-2:13).
- Ending: predicted 10:30; real 10:31. Hit on time, miss on content.

## 4. Gap taxonomy

| Miss | Class | Reasoning |
|---|---|---|
| Whole arc built on break-fix (dumb bot, trap, explosion) that never occurs | topic-conditional | The report is built from Coding Adventures plus A* E01 and treats the break-fix arc as the signature. The Algorithms Explained format is pure lecture: no first person, no failure, no humor. The report says nothing about how to condition on format. |
| Viewer question at 7:06 | wrong-rule | Section 6 says no real viewer question and no learner turn at all, and 9 of 12 videos have none. True for Coding Adventures; false here. A* E01 also had none, so n=1 of 2 for the lecture format. |
| Code at 2:22, before any failure | topic-conditional | Report's A* data point has code at 7:45 (70% runtime); here 22%. The report gives no way to choose. Underspecified for lecture format. |
| Recap at 10:18 | wrong-rule (mild) | Report says few recaps and honest wishlist closings; lecture format recaps and ends on content. |
| Ending is a historic chess game, no teaser | topic-conditional | Report's "honest close" does not apply. |
| Four passes over one tree, each adding one overlay | underspecified | Report mentions A* three reruns and "scaffolding removal"; real is scaffolding addition: values, then code, then bounds, then alpha-beta numbers. |
| Bounds stated as "at least"/"at most" before names | missing-rule | Report has "label for something already working" but no rule for introducing a quantity in words first, name second. Partly consistent with rule 2 of principle verdicts. |
| Tic-tac-toe, trap, head-to-head timings | generator-error | Report does not endorse concrete game picks or a head-to-head; the generator invented them from chess-video memory. |
| No humor, impersonal voice | voice/craft | The generator wrote a chatty first-person voice. Report does not distinguish voice by format. |
| Auto-caption noise | not a gap | Transcript artefacts, ignored. |

## 5. Overfit check

- Arc step 1 (roadmap plus tiny toy in the first minute): partly holds (tree at 0:15) but the "roadmap" is absent.
- Arc steps 2, 3 and 6 (dumb version, visible failure, next failure triggers next concept): do not hold. The optimisation (pruning) is triggered by a stated observation about wasted work (5:21), not a failure.
- Principle 6 "dumb way first: strongest fit" holds only as minimax-before-pruning (1:10-5:06), not as a naive bot.
- Honest-caveat 10/12: absent here (no caveat at all in 10 minutes).
- Humor 9/12: absent.
- "First question none" (9 of 12): wrong in this video.
- Report section 6 "no learner turn at all": contradicted at 7:06.
- Theory 2 (equation as label) and notation-after-concept: holds (code only after the walk-through).
- Theory 3 fixed test choreography: holds strongly (same tree four times).

## 6. Proposed rule changes

1. **Format gate.** Trigger: title contains "Algorithms Explained" (or a short, single-algorithm, impersonal-voice video). Action: turn off break-fix, humor, honest-caveat and first-person devlog moves; use the lecture arc: tiny abstract toy at 0:15 (one dot, two branches), full numeric walk-through by 2:15, code at 20-25% of runtime, same example re-traced with code (about 70 s), optimisation introduced on the same example, viewer quiz, second larger example, code diff, final trace, one-sentence recap, content-based closer. Evidence: 0:15-10:46. Channel-specific; the gate idea is universal (condition on series format).
2. **Layered reruns of one example.** Trigger: algorithm with a core and an optimisation. Action: reuse one 8-leaf example four to five times, adding one overlay per pass (values, code recursion, prune bounds, alpha/beta numbers), stating that the answer is unchanged after each added layer. Evidence: 1:10, 3:56, 5:06, 6:12, 8:44. Likely universal (extends scaffold removal with scaffold addition).
3. **One pause-the-video quiz at about 65% runtime** in lecture format. Trigger: a binary decision on the second, deeper example (prune or not). Action: ask the viewer to pause, then give the answer about 15 s later with the bound reasoning. Evidence: 7:06-7:35. Likely universal.
4. **Introduce bounds in words before names.** Trigger: a variable that encodes a guarantee (alpha, beta). Action: show "at least n" and "at most n" marks on concrete nodes for about 2 min, then name alpha and beta in a code diff against the earlier function (about 10 s per added line). Evidence: 5:21-6:12, 8:02-8:44. Likely universal.
5. **Recap and closer rule for lecture format.** Action: one-sentence recap at about 95% runtime, then a real-world payoff clip with no teaser. Evidence: 10:18-10:46. Format-specific.
6. **Order-sensitivity beat.** Trigger: an optimisation whose gain depends on input order. Action: state it right after the first no-prune stretch (about 1 min later), give one real-domain heuristic (captures first in chess), before the quiz. Evidence: 6:26-6:53. Likely universal.

## 7. Scores (1-5)

- Arc fidelity: 3. Core concept order matches (tree, walk, code, prune, order, alpha-beta) but because the algorithm forces it; break-fix framing and ending were wrong.
- Move-inventory recall: 3. Hit act-it-out, notation-after-concept, visible repetition; missed quiz, recap, code trace pass, layered overlays.
- Move precision: 2. Eight of 14 predicted beats are false positives (dumb bot, trap, explosion, caveats, head-to-head, teaser).
- Pacing/timing: 3. Open and close hit, mid-video milestones drift 1:45-3:10 early.
- Voice: 2. Predicted a chatty devlogger with surprise and caveats; real is impersonal and neutral.
- Overall regenerate: 3. The same algorithm teaches itself in this order, but a reader would not reproduce its structure from the report alone.

Quote (7:06, 7 words): "I'd recommend pausing the video".
