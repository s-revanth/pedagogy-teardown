# Round 4: blind script generation, condition v3

Frozen test set, scored by code. You get a channel. Your test videos are that channel's rows in `deep/round3/tests.tsv` (channel, id, title, duration in seconds, captions). For EACH row write `deep/round3/scripts/v3/<id>.md`, one at a time, finishing and checking each before starting the next.

## Read ONLY these
- `deep/round3/tests.tsv` (your channel's rows), `deep/round3/SLOTS.md`, the taxonomy tags in `deep/BRIEF.md` (for top5_moves / absent3_moves only).
- `deep/policy_v3/<channel>.md` (your rulebook).
- `deep/round3/cards/<id>.json` (the per-video target card) and the 2 exemplar transcripts it lists under `exemplars`. Read the exemplars for rhythm, sentence shape and how this channel talks. Copy no content.
- You may RUN (not edit) `python3 deep/round3/tools/check.py deep/round3/scripts/v3/<id>.md`.

## Forbidden (leaks the test set or other conditions)
Any other file in `deep/corpus/`, `deep/round3/compact/`, `deep/round3/eval/`, `deep/round3/test_features.json`, `deep/round3/train_feats.json`, `deep/reports/`, `deep/policy/` (old v2 rulebooks), other folders under `deep/round3/scripts/`, and the web. Do not use memory of the real video. If you recognise it, put `recall: vague|strong` in the header and write from the rules and general subject knowledge.

## Each file, in this order
1. Header: channel, id, title, duration, condition v3, `recall: none|vague|strong`, exemplars read.
2. Content skeleton: 5-8 bullets.
3. Beat sheet: a table of m:ss | beat type (SLOTS vocabulary) | what is said or shown, filling the real duration.
4. Narration: the spoken words only, in the channel's voice, between a line `<<<NARRATION` and a line `NARRATION>>>`. Length: about the card's `target_words` (within ±15%). Normal punctuation. If the card's sponsor default is ON, include a short generic sponsor read near `position_median` (no real brand names).
5. Slots: one ```json block with the SLOTS.md keys. Use `hook_default` / `ending_default` from the card unless the title clearly demands otherwise. Never use `hook-callback`; a return to the opening is `phrase-mirror`.
6. Run the checker. Revise the NARRATION (not the numbers in the slots) until at least 7 measured targets PASS, or you have made 3 revision passes. The biggest levers: sentence length, pronoun mix (I / we / you), numbers per 100 words, hedges, example cues, question marks. Then paste the checker's final `{"verified_trace": ...}` line as the last ```json block. Never write or edit a trace by hand.

Paraphrase only. Only ever create or edit your own channel's files in scripts/v3; never run scripts that touch other files. When finished, reply with one line per video: id, recall, narration words, checker summary.
