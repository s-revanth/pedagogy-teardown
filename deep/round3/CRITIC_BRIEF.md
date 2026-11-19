# Round 3: blind critic

You are one of TWO independent critics for a channel. Do not look at the other critic's file. For each of the channel's 3 test videos, there are 3 predicted scripts written under different conditions. They are anonymised as labels in `deep/round3/scores/<channel>_blind/`, one file per script named `<id>__<label>.md`. You do not know which label is which condition. Do not try to infer it, and do not open `deep/round3/scripts/`.

## Read
- `deep/round3/SLOTS.md` and `deep/BRIEF.md`.
- The real transcripts in `deep/round3/compact/<id>.txt`.
- The anonymised scripts in `deep/round3/scores/<channel>_blind/`.
- The recall probe `deep/round3/probe/recall.md`, a blind model's memory claims about each video.

## For each video
1. **Real slots**: fill the `SLOTS.md` JSON for the REAL video from the transcript. Use the real timings as fractions, the real beat_sequence and the real top5_moves. For `absent3_moves`, list three taxonomy moves that are clearly absent. Also add `present_moves`, all taxonomy moves present at least once. Leave `wpm` as null; it is computed separately.
2. **Recall probe**: mark each probe claim about this video as correct, partly correct or wrong. Then set `recall_level` to none, weak or strong. Strong means 2 or more specific correct claims beyond the title.
3. **Per script label**:
   - `slot_verdicts`: hit / near / miss for these slots: hook_type, answer_given_upfront, misconception, brute_force_first, examples_count, example_growth, roadmap, viewer_turn, caveat_type, recurring_anchor, ending_type, teaser and sponsor_frac. Near = an adjacent category or within 30%.
   - `voice`, 1-5: how close the sentence-level texture is to the real video.
   - `quality`, 1-5: as a standalone teaching script for a curious 15-year-old, how clear, correct and engaging is it, independent of fidelity?
   - `recall_suspect`: script details that match the real video too specifically to come from a policy or from general knowledge.
   - `biggest_gap`: one sentence.

## Output: `deep/round3/scores/<channel>_<A|B>.json`
Your critic letter is in your prompt.
```json
{"channel":"","critic":"A","videos":{"<id>":{"real":{...slots + present_moves...},"recall_claims":[["claim","correct|partly|wrong"]],"recall_level":"none|weak|strong",
  "scripts":{"<label>":{"slot_verdicts":{"hook_type":"hit"},"voice":3,"quality":4,"recall_suspect":["..."],"biggest_gap":"..."}}}}}
```
Also write `deep/round3/scores/<channel>_<A|B>.md`, 300-600 words. Cover which label best captured each video and why, recurring gaps, and proposed policy fixes with m:ss evidence.

Validate the JSON with `python3 -m json.tool`. Paraphrase only. Write only these 2 files.
