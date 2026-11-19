# Round 3: blind script generation

This is a frozen test set, scored like ML evaluation. You get a CONDITION (base, v1 or v2) and a channel. Your test videos are that channel's rows in `deep/round3/tests.tsv` (columns: channel, id, title, duration in seconds, captions). For EACH row, write `deep/round3/scripts/<condition>/<id>.md`. Write each file as soon as it is done.

## Inputs by condition (read ONLY these)
- **base**: `deep/round3/tests.tsv`, `deep/round3/SLOTS.md` and `deep/BRIEF.md` (taxonomy only). Use only what you already know about this channel's style.
- **v1**: the base inputs, plus `deep/reports/<channel>.md` and `pedagogy-teardown.md`.
- **v2**: the v1 inputs, plus `deep/policy/<channel>.md` (the rulebook; it overrides the report). You may also read the exemplar transcripts listed in its section E.

## Forbidden (this would leak the test set)
`deep/round3/compact/`, `deep/round3/transcripts/`, `deep/corpus/`, `deep/round3/probe/`, `deep/round3/scores/`, other conditions' scripts, and the web. Do not use any memory of the real video. If you recognise it, put `recall: vague|strong` in the header, then write from the rules and general subject knowledge only.

## Each file, in this order
1. **Header**: channel, id, title, duration, condition, `recall: none|vague|strong`. Under v2, also the class you chose in rulebook step 0 and the exemplars you read.
2. **Content skeleton**: 5-8 bullets on what the video plausibly covers.
3. **Beat sheet**: a table of m:ss | beat type (`SLOTS.md` vocabulary) | what is said or shown. It must fill the real duration.
4. **Narration**: the spoken words only, in the channel's voice. No stage directions, timestamps or headings inside it. Put a line with exactly `<<<NARRATION` before it and a line with exactly `NARRATION>>>` after it. Length: 1,000-1,800 words, or less for short videos (duration in minutes × the channel's wpm, if that is smaller). Use punctuation normally, including question marks.
5. **Slots**: one ```json block with the `SLOTS.md` keys.
6. **v2 only**: one more ```json block, `{"rule_trace": {"U1": "applied|n/a: reason|broken: reason", ...}}`, covering EVERY rule ID in the rulebook (U, C, D, N and B).

Paraphrase only. No quotes from real videos. Write only your own files. When finished, reply with one line per video: the id, the recall level and the narration word count.
