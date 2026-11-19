# Held-out test, phase 2: gap analysis (critic)

A generator wrote `deep/holdout/scripts/<id>.md` without seeing the real video. It worked only from the channel hypothesis `deep/reports/<channel>.md`. Your job is to compare that predicted script with the REAL video, `deep/holdout/compact/<id>.txt`, which is a timestamped transcript of about 15 s per line. Then find where the hypothesis fails. The aim is to judge the hypothesis, not the generator's writing.

Read: `deep/BRIEF.md` (taxonomy and 13 principles), `deep/reports/<channel>.md`, `pedagogy-teardown.md`, both scripts and both real transcripts. Paraphrase. Use at most one real quote per video, under 15 words.

## For EACH video, write `deep/holdout/gaps/<id>.md`
1. **Real beat sheet** (compact): m:ss | H/B/N/I | tags | one-line paraphrase.
2. **Prediction scorecard**: for every explicit prediction in section 5 of the script, give the predicted value, the actual value, and a verdict of hit, near or miss. Then give an overall hit rate.
3. **Structural alignment**: compare the predicted arc with the real arc, step by step. Name the beats that were predicted and present, predicted but absent (false positives), and present but unpredicted (false negatives). Give timing drift for the big moments: the hook, the first new idea, the payoff and the ending.
4. **Gap taxonomy**: classify each important miss as one of:
   - `missing-rule`: the report has no rule that would produce it.
   - `wrong-rule`: the report states a rule the real video contradicts.
   - `underspecified`: the rule exists but is too vague to generate the right choice (for example "uses analogy" without saying when, how many, or what kind).
   - `topic-conditional`: the channel behaves differently because of topic or format, and the report doesn't say how to condition on it.
   - `generator-error`: the report was fine; the generator misapplied it. These don't count against the hypothesis.
   - `voice/craft`: humour, pacing, sentence-level texture or visual craft the report doesn't capture.
5. **Overfit check**: name claims the report makes that look like overfitting to the 12 training videos and don't hold here.
6. **Proposed rule changes**: 3-6 concrete additions or edits to the channel report. Write each one so a generator could act on it (a trigger, an action and a parameter). Each needs evidence with m:ss. Mark whether it is channel-specific or likely universal (cross-channel).
7. **Scores, 1-5 each**: arc fidelity, move-inventory recall, move precision, pacing/timing, voice, and overall "could the hypothesis regenerate this video". Give a one-line justification for each.

## Then also write `deep/holdout/gaps/<channel>_summary.md` (300-500 words)
This merges both videos. Cover the recurring gaps, the strongest proposed rules ranked, which report sections are most wrong or most vague, and your verdict on whether the hypothesis generalises.

Do not edit any other file.
