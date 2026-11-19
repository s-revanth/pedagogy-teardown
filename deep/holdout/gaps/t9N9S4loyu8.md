# Gap analysis: How I deceived myself (t9N9S4loyu8, 511 s)

Channel report tested: `deep/reports/PrimerBlobs.md`. Predicted script: `deep/holdout/scripts/t9N9S4loyu8.md`. Real transcript: `deep/holdout/compact/t9N9S4loyu8.txt`.

**Topic mismatch is scored separately as generator-error.** The generator guessed "simulation bias: peeking and p-hacking with identical red and blue blobs". The real video is an on-camera apology and retraction: Hamilton's rule was misstated in an earlier video, taken down, and the presenter lists five reasoning mistakes. The generator was warned of this risk in its recall note. Scoring below is on structure; items driven only by the wrong topic are flagged.

## 1. Real beat sheet

| m:ss | Lvl | Tags | Paraphrase |
|---|---|---|---|
| 0:01 | H | admin, humor | Unusual on-camera video. Opens with plush-blob pre-orders; physical prototype in hand. |
| 0:20 | H | story, hook-confession | Prototype's eyes are slightly off, "not everything comes out right the first time". Segue to the main topic: he made a mistake. |
| 0:37 | H | roadmap, teaser-next | A bold claim ("Hamilton's rule is a lie") was wrong. The old video is down; two replacements are coming (green-beard, and Hamilton's rule done right). This video is the reflection. |
| 1:10 | H | honest-caveat, second-person-role | Embarrassing, but he can't learn without owning it. Others learn best from someone else's mistakes. |
| 1:25 | N | minimal-definition-then-refine, honest-caveat | One-sentence statement of the biology error. Says confusion is fine, and defers the detail to the dedicated video. |
| 1:57 | B | roadmap, rule-list | "Five things wrong with my thinking, maybe more." Numbered list begins. |
| 2:14 | N | minimal-definition-then-refine, presenter-was-wrong | Mistake 1: logical fallacy, defined in one line. He thought he'd found a flaw in a 40-year-old rule. |
| 2:33 | N | dignify-dismiss | Appeal-to-authority concern is real. He resisted it, "which I guess is good". |
| 3:05 | N | notation-after-concept (named term), humor | Then used it as a reason never to change his mind: the "fallacy fallacy". A bad argument for a true claim doesn't make it false. But when you don't know, it feels false. |
| 3:21 | N | misconception-first (own) | Mistake 2: absolutes instead of probabilities. Authority is evidence, not proof. |
| 3:54 | N | honest-caveat | Weigh the odds that he's wrong against the odds that four decades of research is wrong. No numbers possible. |
| 4:30 | I | notation-after-concept | Named: Bayesian reasoning. Warning lights were there, but he ignored the unease. |
| 5:02 | N | story, failure-shown | Mistake 3: confirmation bias. Picked sympathetic, uninformed conversation partners. Never sought a "no, you're wrong". |
| 5:50 | N | story, presenter-was-wrong | Mistake 4: impatience. Experts disagreed; he argued, then realised he was wrong. This happened after publishing. |
| 6:22 | N | story | Mistake 5: overconfidence. Sharing a wrong idea is fine in conversation, not when publishing. |
| 6:57 | N | analogy, commit-to-answer | Saved for last as most important. Knowing the traps is not enough ("walking into a minefield"). Must be methodical. |
| 7:13 | N | commit-to-answer, recap-lite | Next time: slow down, check the known mistakes systematically. |
| 7:47 | H | honest-caveat | Glad it happened publicly; otherwise easy to avoid confronting it. |
| 8:04 | H | admin, callback-to-hook, humor | Apology and thanks. Plush plug again ("weird to promote in an apology video"). Ends 8:31. |

Key metrics: first question to viewer none. First notation none (named terms only: fallacy fallacy 3:05, Bayesian 4:30). Misconception: his own, five times. Brute force none. Examples: 5 numbered mistakes. Ending: commitment, apology, self-aware plug.

## 2. Prediction scorecard (script section 4)

| Prediction | Predicted | Actual | Verdict |
|---|---|---|---|
| First question time | about 1:10 predict pause; rhetorical opener possible by 0:30 | No question or pause anywhere | miss (format-driven) |
| First notation | about 5:40 (p-value), "possibly none" | None. Named terms at 3:05 and 4:30 (35% and 54%) instead. | near (hedged) |
| Misconception | yes, held first by the presenter as a confession | Yes in structure (the presenter's own wrong belief, first). Wrong content (sim luck vs authority and Hamilton's rule). | near (content is generator-error) |
| Brute-force-first | yes: 100 batches of 5 runs | No sim, no repetition | miss (generator-error plus format) |
| Examples | 3-4 growing: 5 runs, 100 batches, stop chart, 200 runs | 5 numbered mistakes. Grows by importance (overconfidence saved last), not by scale. | near |
| Hook type | confession or paradox, a story not a quiz | Confession, but after a 20 s merch cold open | hit |
| Ending type | scope recap, callback to opening claim, then short teaser and admin; ends on a limit | No recap. Commitment, apology, then admin. Callback is to the plush joke. No teaser. | near |
| Five confident moves | honest-caveat, presenter-was-wrong, simulation-as-argument, failure-shown, toy-world | honest-caveat hit; presenter-was-wrong hit (it is the whole video); the last 3 absent | near (2 of 5) |

Hit rate: 1 hit, 5 near, 2 miss of 8. Hit+near = 75%. Weighted = 44%. If the rows driven only by the wrong topic are dropped (first question, brute-force, and 2 of the 5 moves), the remaining rows are 1 hit and 4 near, so the hypothesis' honesty DNA holds. The scaffolding does not.

## 3. Structural alignment

**Predicted and present:**
- Confession hook.
- Honest-caveat throughout (hedges at 1:57, 3:54, 4:12).
- Presenter-was-wrong.
- Dignify-then-dismiss, applied to his own reasoning (2:33-3:05).
- Named concepts after the idea is shown (3:21-4:30).
- Admin at the end.
- Callback to an opening beat (to the plush, not the claim).

**Predicted but absent (false positives):**
- Toy-world setup and rule list.
- Predict pause.
- 5-run sim and 100-batch brute force.
- Stop-when-ahead chart.
- p-value patch.
- Design-the-rule and the 200-run verification.
- Recap card.
- Scope-the-claim.
- Teaser at the end.

**Present but unpredicted (false negatives):**
- On-camera, no sim, blob only as a physical prop.
- Merch promo as cold open, bridged by a prototype joke (0:01-0:37).
- Teaser/replacement pointer placed at the front (0:37), not the end.
- Deferral of the technical detail with permission to be confused (1:25-1:41).
- Count roadmap: "five, maybe more" (1:57).
- Each item introduced with a one-line lay definition (2:14).
- Meta-joke ("fallacy fallacy", 3:05).
- Bayesian reasoning named but explicitly unquantified (3:54-4:30).
- Escalation: strongest item last (6:57).
- Closing analogy as a capstone (minefield, 6:57-7:13).
- Commitment to a future checklist (7:13).
- "Glad it was public" reframe (7:47).
- Deadpan plug in an apology video (8:04).

**Timing drift:**

| Moment | Predicted | Actual | Drift |
|---|---|---|---|
| Hook | 0:00 | 0:20 | +20 s |
| First new idea | 1:10-1:45 | 1:25 (error stated), 2:14 (mistake 1) | +15 s to +1:00 |
| Named term or notation | 5:40 | 3:05, 4:30 | -1:10 to -2:35 |
| Payoff (the main lesson) | 7:00 | 6:57 | about 0 (coincidence of shape) |
| Ending | 7:40-8:10 | 7:13-8:30 | within 30 s |

## 4. Gap taxonomy

| Gap | Class | Note |
|---|---|---|
| Wrong subject (sim peeking, p-values) | generator-error | The generator disclosed its recall risk. Not scored against the report. |
| Whole format: on-camera, no sim, numbered-lessons list | missing-rule | The report's 12 are all model-centered. Its variants cover only Logistic Growth and Cheater. Nothing covers talk-to-camera reflection. |
| No predict pause, no toy-world, no sim (the report's 11/12 and 12/12 moves) | topic-conditional | The report gives base rates, not conditions. A generator cannot know when the 12/12 does not apply. |
| Numbered list, one lesson per 60-70 s, strongest last | underspecified | The report has "add one thing at a time" and "rule-list" only for sims. No count-roadmap rule, no escalation rule. |
| Closing analogy as capstone | missing-rule | The report says only "analogy first, then rigor" (partial 8/12). Here the analogy comes at the climax to compress the lesson. |
| Admin at the start, plus a joke on the end plug | missing-rule | The report puts "teaser then admin" at the end only. |
| Teaser at the front as a replacement pointer; deferral of detail | missing-rule | The report knows teaser-next only at the end. |
| No recap card, no callback to a claim; ends on a commitment | wrong-rule (soft) | The report's recap 7/12 and scope-the-claim ending. Real is a commitment plus apology. This is a format shift, so close to topic-conditional. |
| Voice: deadpan, hedging, self-deprecating, plain ("I guess", "I don't know what to tell ya") | voice/craft | The script was polished and aphoristic ("stories are free; noise looks like signal"). |
| Named term after plain description (Bayesian, fallacy fallacy) | hit | The report's notation-after-concept generalises to vocabulary. |

## 5. Overfit check

- Bottom line says the channel teaches by running a world. This video teaches by narrative and a list.
- Move frequency table (toy-world 12/12, predict pause 11/12, simulation-as-argument 11/12, failure-shown 11/12) is treated as universal priors. Here 4 of the 4 are absent.
- "Teaser then admin" ordering and "6/12 teasers".
- "All 12 videos are model-centered" is a property of the sample, not the channel. The channel evidently also publishes reflective uploads.
- "Principle 4 partial, sim is the analogy": here a real analogy appears, at the end.
- "Honesty is the connective tissue" generalises strongly and is the best part of the report.
- Theory 4 (dignify-dismiss) generalises, and in a wider form: it applies to the presenter's own past reasoning.

## 6. Proposed rule changes

1. **Format switch (on-camera, first-person titles such as "How I ...").** Trigger: title is first-person or reflective. Action: drop sim, toy-world and predict pauses. Use: confession in the first 30 s, a pointer to the fix at about 0:37, a count roadmap ("N things, maybe more") at about 22%, one lesson per 60-90 s, strongest last, a commitment ending. Evidence: 0:20, 0:37, 1:57, 6:57, 7:13. Primer-specific format, but the numbered-lessons-with-escalation structure is likely cross-channel.
2. **Dignify-then-dismiss applies to your own reasoning.** Trigger: the presenter defends or explains his old belief. Action: first concede the true premise in one line ("that's all true", 2:49), then name the step that went wrong (3:05). Replaces the "human intuition" scope in theory 4. Cross-channel.
3. **Lay definition, then label.** Trigger: a named concept (fallacy, bias, Bayesian) enters. Action: give a one-line plain definition before the label (2:14), show the instance, then give the term (3:05, 4:30). If it can't be quantified, say so before the term (3:54). Cross-channel.
4. **Late analogy as capstone.** Trigger: the lesson is a gap between knowing and doing, not a mechanism. Action: one analogy at the final, most important item (minefield, 6:57-7:13), not at the start. Evidence: 6:57-7:13. Likely cross-channel, but one instance only.
5. **Defer detail with permission.** Trigger: correcting a technical error would need background the video doesn't cover. Action: state the error in one sentence (1:25), say confusion is fine and the detailed video is coming (1:41), move on. Cross-channel.
6. **Admin placement and tone for off-format videos.** Trigger: merch or a plug is attached to a non-lesson upload. Action: put a 15-20 s admin item first, with a prop joke bridging into the topic (0:01-0:37). Call it back with a deadpan line at the end (8:04). Channel-specific.

## 7. Scores (1-5)

- **Arc fidelity: 2.** Confession hook and honest ending-spirit match. The 70% middle (sim, batches, p-value, design-the-rule) is wrong. Topic-adjusted: 3.
- **Move-inventory recall: 2.** About 5 of 15 real moves were predicted. The numbered list, count roadmap, deferral, escalation, late analogy, front teaser and commitment ending were all missed.
- **Move precision: 2.** About a third of the predicted moves occur. The rest belong to the wrong topic or the wrong format. Topic-adjusted: 3.
- **Pacing/timing: 3.** The payoff and ending land within about 30 s, but the hook slips 20 s and the named terms come 1-2.5 min earlier. Much of this is luck from the target duration.
- **Voice: 2.** The script is polished and dramatic. The real voice is hesitant, deadpan and self-deprecating.
- **Overall, could the hypothesis regenerate this video: 2.** The honesty DNA is right. The report has no format for non-sim uploads, so the arc can't be generated. Topic-adjusted: 3.
