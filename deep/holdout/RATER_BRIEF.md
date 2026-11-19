# Held-out test, phase 3: final rating and synthesis

You are the final judge. Nine channel hypotheses (`deep/reports/<channel>.md`, with the matching storyboards in `deep/storyboards/<channel>.html`) were tested on 18 held-out videos, 2 per channel, listed in `deep/holdout/heldout.tsv`.
- A blind generator wrote predicted scripts from the hypothesis alone: `deep/holdout/scripts/<id>.md`.
- A critic compared each script with the real transcript, `deep/holdout/compact/<id>.txt`. Its output is `deep/holdout/gaps/<id>.md` plus `deep/holdout/gaps/<channel>_summary.md`.

Read all the gap files and summaries, all 9 reports, and the storyboard HTML. For the storyboards, extract their panels, arc steps and theory cards. Spot-check the critics against the real transcripts wherever a critic's claim drives a conclusion. Critics can be wrong too. Downgrade claims that look like generator recall or generator error rather than hypothesis signal.

## Output 1: `deep/holdout/RATING.md` (2,000-3,500 words)
1. **Bottom line**: does the teardown generalise? Give one paragraph and a headline score.
2. **Leaderboard**: a table of channel | arc fidelity | move recall | move precision | pacing | voice | regenerability | your rating 1-10 | one-line verdict. Your rating may disagree with the critics' scores; say where and why.
3. **Cross-channel failure modes of the hypotheses**: patterns in how the reports fail, such as describing averages instead of conditional rules, missing format conditioning, vague moves, overfitting to the sample, and no voice model.
4. **New universal rules** for `pedagogy-teardown.md`: rules that appear in 3 or more channels' gaps. Each has a trigger, an action, a parameter, its evidence (channel, id, m:ss) and a confidence level.
5. **Channel-specific additions**: the top 2-3 rules per channel, ranked.
6. **Principle audit**: for Velocity principles 1-13 and the round-1 claims, say which held up on held-out data, which weakened, and which need rewording.
7. **Method critique**: weaknesses of this eval (n=2 per channel, recall leakage, critic bias, generator skill confounds) and how to run round 3. Include a proposed numeric eval rubric.

## Output 2: `deep/holdout/visual_data.json`
This is the data for the final visual. Use exactly this shape:
```json
{"headline":{"score":"x/10","verdict":"one sentence"},
 "universal_new_rules":[{"rule":"","trigger":"","evidence":"","confidence":"high|med|low","channels":["..."]}],
 "channels":[{
   "channel":"3blue1brown","rating":7,"scores":{"arc":4,"recall":3,"precision":3,"pacing":3,"voice":2,"regen":3},
   "heldout":[{"id":"","title":"","hit_rate":"x/y"}],
   "initial_hypothesis":["4-6 short bullets: the report's core claims as originally stated"],
   "storyboard_claims":[{"claim":"a claim or arc step that is in the storyboard HTML","status":"confirmed|partly|contradicted|untested","evidence":"held-out id m:ss: what happened"}],
   "new_findings":[{"finding":"new rule or correction found only in this test","type":"missing-rule|wrong-rule|underspecified|topic-conditional|voice/craft","evidence":"id m:ss"}]
 }]}
```
Give 5-8 storyboard_claims and 3-5 new_findings per channel. Keep every string under 220 characters. The JSON must be valid. Paraphrase only.

Do not edit any other file.
