# Gap analysis: Overexplaining the binomial distribution (6YzrVUVO9M0, 918 s)

Channel report tested: `deep/reports/PrimerBlobs.md`. Predicted script: `deep/holdout/scripts/6YzrVUVO9M0.md`. Real transcript: `deep/holdout/compact/6YzrVUVO9M0.txt`.

Short verdict: the opening 5 minutes were predicted well (small blob ladder, enumerate by hand, formula decoded after). Everything after 5:40 differs. The real video is a derivation explainer with two acts. The script was a simulation exploration with a surprise and a model break.

## 1. Real beat sheet

| m:ss | Lvl | Tags | Paraphrase |
|---|---|---|---|
| 0:00 | H | hook-question, notation-first | Concrete question: a 60% free-throw shooter takes 10 shots, chance of exactly 7? The full binomial formula is named right away as the tool. |
| 0:15 | H | generalize-to-other-domains, minimal-definition-then-refine | Applies to any repeated yes/no process; explains "bi" in binomial. |
| 0:30 | H | roadmap, toy-world, special-case-first | Promises the formula will make sense by the end. Starts with one blob programmed to make 60% of shots. |
| 0:46 | N | special-case-first, honest-caveat | 1 shot: 60% / 40%, admitted to be silly. 60% recast as 3 of 5 blobs. |
| 1:02 | N | visible-repetition, build-and-verify, honest-caveat | 2 shots on a 5x5 blob square. 4 of 25 miss both = 16% = 40% x 40%. Flags "not exactly random". |
| 2:09 | N | visible-repetition, build-and-verify | The one-make groups: 6/25 each = 24% = 0.6 x 0.4. Total 48%; all outcomes sum to 100% as a sanity check. |
| 2:41 | N | inline-quiz | Pause: guess the pattern for 3 shots. |
| 2:57 | N | visible-repetition, act-it-out | 3 shots on a 5x5x5 cube of 125 blobs, pulled apart by outcome. 8/125 = 6.4% for no makes; each count checked by multiplying. |
| 3:45 | N | learner-discovers (narrator states) | The three orderings of 1-of-3 all have the same probability. Order doesn't matter, so compute one and multiply by 3. |
| 4:33 | I | notation-after-concept | Names the formula pieces: the binomial coefficient (counts ways), p and 1-p, exponents. Says the coefficient method is deferred. |
| 5:40 | N | inline-quiz (checkpoint), honest-caveat | Formula may feel overwhelming. Invites a pause to plug the numbers in on paper. |
| 5:57 | N | honest-caveat, dignify-dismiss, minimal-definition | Independence caveat: a nervous shooter breaks it. Blobs "forget like goldfish". Justifies simple model first, test, add complexity later. |
| 6:27 | B | roadmap | Original 7-of-10 isn't answerable yet because the arrangements aren't countable. Restart with counting only. |
| 6:43 | N | brute-force-first, notation-compaction | Branching tree doubles each shot. Lumped into a count table: 1-2-1, 1-3-3-1, 1-4-6-4-1. |
| 8:20 | N | callback-to-hook, commit-to-answer | Payoff for the hook: 120 ways x 0.6^7 x 0.4^3, about 21.5%. Then Pascal's triangle named. |
| 8:54 | B | pain-driven-shortcut (new) | Table works but doesn't scale. Wants a faster way. |
| 9:09 | I | notation-after-concept, rule-list, connect-outside | Closed form with factorials ("bad news"). Factorials defined by examples. 0! = 1 flagged and linked out. |
| 10:14 | N | you-could-invent-it, visible-repetition | Why n!? Arrange 1, 2, 3, 4 objects; each new object multiplies the count by n. |
| 11:19 | N | inline-quiz (checkpoint) | Pause: make sure n! makes sense, because the next part depends on it. |
| 11:34 | N | tiny-to-bigger, toy-world, visible-repetition | Divide by arrangements within each category. Hats: 3 blobs (2 hats), 4 blobs (2 hats), 4 blobs (3 hats). |
| 13:11 | B | connect-outside | Names combinatorics as where to learn more. |
| 13:28 | N | build-and-verify, simulation-as-argument | 10,000 blobs vs the formula. "Pretty close, not exact" is fine. Silent run about 40 s (13:46-14:27). |
| 14:27 | N | recap | Scope: repeatable, independent, yes/no events; needs per-trial p. |
| 14:58 | N | admin | Patreon. No teaser. Ends 15:14. |

Key metrics: first question 0:00. First formula 0:00 (shown, undecoded). Decoded notation 4:33 (30%). Hook payoff 8:20 (55%). Simulation 13:28 (88%).

## 2. Prediction scorecard (script section 5)

| Prediction | Predicted | Actual | Verdict |
|---|---|---|---|
| First question time | 0:00-0:20 direct question; formal predict-pause about 3:15 | 0:00 direct question. Pause at 2:41 (guess the 3-shot pattern). | hit |
| First notation | about 7:30 (49%) | Formula shown 0:00. Pieces decoded 4:33 (30%). Factorial formula 9:09. | miss |
| Misconception | yes: "most likely count is likely", gambler's "evens out" | No misconception set up. Only the independence caveat (5:57). | miss |
| Brute-force-first | yes: enumerate 2 and 3 flips by hand | Yes: 1, 2, 3 shots as blob grids (1:02-3:45), then tree and table (6:43). | hit |
| Examples | 6-7 settings: n=1,2,3,4,10; p=0.3; survival story; n up to 1000; dependent flips | n=1,2,3 grids, 4 table, 10 via table, hats x3, 10,000-blob check. p fixed at 0.6 throughout. | near (count and growth right; the specific cases are wrong) |
| Hook type | direct question in toy world plus a joke about overexplaining; not a paradox | Direct question in a human sports scenario, formula shown at once, blobs take over at 0:30. No joke. | near |
| Ending type | scope recap, callback, teaser, admin; ends on a limit | Scope recap (14:27), then admin. No teaser, no break. The callback fires mid-video (8:20). | near |
| Five confident moves | toy-world, simulation-as-argument, notation-after-concept, brute-force/special-case, honest-caveat (+ failure-shown) | toy-world hit; brute-force hit; honest-caveat hit; notation-after-concept hit in spirit; simulation-as-argument only as a late check (near). failure-shown absent. | near (4 hit, 1 near, 1 miss) |

Hit rate: 2 hit, 4 near, 2 miss of 8. Hit+near = 75%. Weighted (hit=1, near=0.5) = 50%.

## 3. Structural alignment

**Predicted and present:**
- Hook question at 0:00.
- Toy-world.
- Special-case-first ladder.
- Hand enumeration (brute-force).
- Visible repetition.
- Rule-ish statement of independence.
- "Blobs forget" dismissal (5:57).
- Notation after concept.
- Build-and-verify.
- Recap.
- Admin.
- Generalize (verbally only, 0:15).

**Predicted but absent (false positives):**
- "Overexplaining" joke.
- Rule list of 3.
- 1,000-blob histogram as a surprise (3:50).
- Gambler's-fallacy misconception.
- Presenter surprised.
- p = 0.3 skew, survival story, n = 10 to 1000 spread.
- Break-independence simulation (the caveat is only spoken).
- Teaser.

**Present but unpredicted (false negatives):**
- Formula shown at 0:00 as the promised destination.
- Real-world (sports) hook, then a blob stand-in at 0:30.
- 3D cube of 125 blobs, pulled apart.
- Two-method check at every outcome (count blobs vs multiply), plus the sum-to-100% check.
- Insight that order doesn't matter (4:00).
- Pause prompts used as checkpoints (5:40, 11:19), not predictions.
- Justification for starting simple (6:12).
- Tree-to-table compression, then Pascal's triangle.
- Pain-driven second act, 8:54-13:11 (28% of runtime): the closed form, built by adding one object at a time and dividing for indistinguishable categories.
- Hat toy mini-world.
- Outside pointers (0! videos, combinatorics).
- Casual jokes.

**Timing drift:**

| Moment | Predicted | Actual | Drift |
|---|---|---|---|
| Hook | 0:00 | 0:00 | 0 |
| First new idea | 1:15 | 0:46 (1 shot), 1:02 (2 shots) | -13 to -29 s |
| Decoded notation | 7:30 | 4:33 | -3:00 |
| Hook payoff | 3:50 (sim histogram) | 8:20 (table count) | +4:30 |
| Verification | 8:40 | 13:28 | +4:48 |
| Recap | 14:00 | 14:27 | +27 s |
| End | 14:40+ | 15:14 | about +30 s |

Structure was predicted as three acts: sim surprise, formula, break. The real structure is two acts: hand and table counting, then a closed-form derivation, then a short sim check.

## 4. Gap taxonomy

| Gap | Class | Note |
|---|---|---|
| Closed-form derivation as a second act (n!, divide by group orderings), 4+ min | missing-rule | Nothing in the report says "when the by-hand method works but scales badly, derive a compact formula one object at a time". Logistic Growth's "work backward" is the closest. |
| Formula shown at 0:00 as destination, then decoded | missing-rule / topic-conditional | The report says notation follows concept and arrives as a patch for a failure. Here the formula is the promised roadmap, and only its decoding follows the concept. |
| No surprise, no misconception; sim used only as a late check | topic-conditional | The report's "predict, surprise, lesson" is for emergent-behaviour sims. Here the answer is exact counting. The report gives no switch between exploration and derivation. |
| Sim placed at 88%, not early | underspecified | Arc step 8 (build-and-verify) exists but says nothing about when sim-before-theory flips to theory-then-sim. |
| "Ends on a parameter change that breaks the model" | wrong-rule | Real ending is a recap. The break is only mentioned (5:57, 14:43). failure-shown is 11/12 in training. |
| Pause prompts are checkpoints for symbol or dependency (5:40, 11:19), not predictions | underspecified | The report only knows "predict pause". |
| Teaser predicted, absent | underspecified | 6/12 with no trigger. Neither the generator nor the report can tell when it occurs. |
| p-change / survival / n-growth padding | generator-error | The report's "same machinery, new number" is real, but the generator invented content with no basis in the title. |
| Coin and "overexplaining" joke | generator-error | Over-read the title. |
| Human-world hook and dry casual jokes (goldfish, "say it with me", poor little blob) | voice/craft | The report has no voice section. |
| Two-method check per example and sum to 100% | underspecified | build-and-verify is described only at video level. |

## 5. Overfit check

- "Surprise then lesson", "predict, then run", "break the model on purpose": all come from the evolution, economics and epidemic sims. Not present here.
- Bottom line "builds and runs a world before any theory appears": reversed. The theory (counting by grids) is built first and the big sim is last.
- toy-world 12/12 holds only as blobs standing in for a human case. The hook itself is not a blob.
- failure-shown 11/12 as a default arc step.
- "Insight is told after the prediction, not extracted": holds, but the report never separates prediction pauses from checkpoint pauses.
- Notation-as-patch-for-failure: here notation is promised, then decoded, then a second formula is introduced because the table is laborious (9:09). The trigger is cost, not breakdown.
- Section 6 says "almost never uses outside sources": here there are two pointers. Soft, but real.

## 6. Proposed rule changes

1. **Format switch: named-formula topics.** Trigger: title names a standard result (binomial, Bayes, and so on). Action: state a concrete human question and the full formula at 0:00; say by 0:30 that it will be decoded; build n=1, 2, 3 with blob grids; name the formula's parts at about 30% of runtime; answer the hook at about 55%; run the sim only at about 85-90% as a "close, not exact" check. Evidence: 0:00, 0:30, 4:33, 8:20, 13:28. Scope: Primer-specific in the details; "formula-as-destination" is likely cross-channel.
2. **Pain-driven second act.** Trigger: a by-hand method answers the hook (the 8:20 table) but scales badly. Action: state the cost in one sentence (8:54), show the closed form as "the bad news" (9:09), then derive each factor over 3-5 minutes. Add one object at a time with n=1 to 4 (10:14), then 3 small categorized examples of 3-4 blobs (11:34). Evidence: 8:54-13:11. Cross-channel (3b1b calculus, Reducible FFT use the same shape).
3. **Checkpoint pauses, distinct from prediction pauses.** Trigger: the next beat depends on a symbol or derived fact the viewer just met. Action: say "pause and make sure X makes sense, or the next part won't"; one every 3-5 min (2:41, 5:40, 11:19). Where outcomes are guessable, call it a predict pause. Where it is a prerequisite, call it a checkpoint. Cross-channel.
4. **Two-method verify at every worked case.** Trigger: any worked case in a ladder. Action: compute the same outcome as a blob-count fraction and as a product; verify the totals sum to 100%; repeat for 3 successive cases (1:34, 2:09, 3:28). Replaces "verify only at the end". Cross-channel.
5. **Deferred-assumption caveat.** Trigger: the formula's validity condition (independence). Action: introduce it once, right after the pieces are named (5:57), with one human counterexample (a nervous shooter), justify "simple first, test, then add" in one sentence (6:12), and restate it in the recap (14:43). No demonstration. Evidence: 5:57-6:27, 14:43. Primer-specific substitute for failure-shown in formula explainers.
6. **Human hook, then blob hand-off.** Trigger: topic is not biology. Action: ask in a human scenario (0:00); within 30 s program a blob with the same parameters (0:30). Evidence: 0:00, 0:30. Primer-specific.

## 7. Scores (1-5)

- **Arc fidelity: 3.** The first 5:40 closely matches; the remaining 9:30 is a different arc (derivation, not surprise plus break).
- **Move-inventory recall: 3.** About 15 of 24 real moves were predicted. The misses are the second act, checkpoint pauses, the formula-first hook and the two-method checks.
- **Move precision: 3.** About 60% of predicted moves occur. The sim histogram, p-change, n-growth, break and teaser are false.
- **Pacing/timing: 3.** Hook, first idea and recap are within 30 s. Notation is 3 min early; the payoff and verification are 4.5-5 min late.
- **Voice: 3.** The script's earnest, dramatic "overexplaining" voice is too showy. The real one is plain with small asides; the blob ladder still matches.
- **Overall, could the hypothesis regenerate this video: 3.** A generator would get the first third and the recap but not the derivation act that fills about 30% of runtime.
