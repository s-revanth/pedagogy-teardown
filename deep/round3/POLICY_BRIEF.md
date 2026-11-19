# Round 3: rewrite a channel report as a decision-rule policy

The round-2 held-out test scored the reports 4/10. They described AVERAGES ("roadmap in 9/12 videos"), so generators applied every move to every video. The fix is to turn each report into a POLICY: classify the video, then use the template and move switches for that class. See `deep/holdout/RATING.md` and `deep/holdout/visual_data.json`.

## Inputs (all are training data now)
- `deep/reports/<channel>.md` (v1) and `pedagogy-teardown.md`.
- Every `deep/analyses/<id>.json` and `.md` for this channel (ids from `deep/tracker.csv`), and `deep/compact/<id>.txt` when you need detail.
- Round 2: `deep/holdout/gaps/<id>.md` and `<channel>_summary.md` for this channel's 2 videos (ids in `deep/holdout/heldout.tsv`), their transcripts in `deep/holdout/compact/<id>.txt`, `deep/holdout/RATING.md` and `deep/holdout/visual_data.json`.
- Vocabulary: `deep/BRIEF.md` and `deep/round3/SLOTS.md`.
- FORBIDDEN: everything in `deep/round3/` except `SLOTS.md` and `POLICY_BRIEF.md`. The test videos must stay unseen.

## Measure, don't guess
Use python3 to compute per-video wpm (words in the compact txt ÷ duration) and median beat length (from the analyses' beat timestamps). Put the numbers in the policy.

## Output 1: `deep/policy/<channel>.tags.json`
One entry per training video (all 14):
`{"id","title","duration_s","format","topic_type","answer_given_upfront":bool,"solved_or_open","wpm","median_beat_s","hook_type","ending_type","class"}`
Use the `SLOTS.md` enums for `hook_type` and `ending_type`.

## Output 2: `deep/policy/<channel>.md` (1,500-3,000 words)
1. **Classifier**: 2-5 classes for this channel. Give observable triggers for each (title words, duration, series label, topic type, answer-in-title) and the training ids in each class. Add a fallback rule for an unclear class.
2. **Per-class template**:
   - Beat sequence in the `SLOTS.md` beat vocabulary, with anchor ranges as fractions of runtime (hook, first concrete object, first new idea, first notation, payoff, ending).
   - Pace: wpm and median beat length.
   - Hook choice rule and ending choice rule.
   - **Move switches**: a table of move | ON / OFF / IF condition | parameter (count, timing, length). Include an explicit **MUST NOT** list.
   - Caveat type, recurring-anchor rule, notation rule, viewer-turn rule, sponsor placement.
3. **Voice card**: 6-10 sentence-level rules (sentence length, person, humour type and density, signposting phrases paraphrased, how numbers are said). Point to 2-3 training exemplars with m:ss ranges that show the rhythm.
4. **Exemplar index**: for each class, the 1-2 training ids a generator should imitate structurally.
5. **Confidence**: which rules rest on n < 3 videos.

Be concrete and parametric. Every rule should be usable by a generator without interpretation. Write only these 2 files.
