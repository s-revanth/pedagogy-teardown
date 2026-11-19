# Held-out test, phase 1: blind script generation

This is like evaluating a trained model on a held-out test set. The "model" is our written hypothesis about how a channel teaches. You must PREDICT how the channel would script a video it really made, using ONLY the hypothesis. A separate critic will then compare your script with the real transcript.

## Allowed inputs (read ONLY these)
- `deep/reports/<channel>.md`: the channel hypothesis.
- `pedagogy-teardown.md` (top-level): the round-1 cross-channel findings.
- `deep/BRIEF.md`: the move taxonomy and the 13 principles.
- `deep/holdout/heldout.tsv`: the titles and durations of your two videos.

## Forbidden (this would leak the test set)
- Anything in `deep/holdout/transcripts/` or `deep/holdout/compact/`, and any other transcript or analysis file.
- The web. Do not fetch or search for the video.
- Recalling the real video from memory. If you think you remember it, ignore that and say so in the header. Build from the hypothesis plus general subject knowledge only.

## Task, for EACH of your two videos
Write `deep/holdout/scripts/<id>.md` containing:
1. Header: channel, title, target duration, and a "recall risk" note (none / vague / strong) on whether you might know the real video.
2. **Predicted beat sheet**: a table of timestamp | H/B/N/I | move tags | what the narrator says/does | what is on screen. Make it plausibly fill the real duration (about one beat per 30-60 s).
3. **Full narration script**: written in the channel's voice, at about 160-170 wpm × duration (or less for very long videos; at least 1,200 words and complete from the opening to the ending).
4. **Rule trace**: for each beat, which specific claim, arc step or move in the report made you choose it. Also list the report claims you could NOT turn into a concrete choice because they are too vague to generate from.
5. **Explicit predictions** (these are falsifiable; the critic will score them): the first question time, the first notation/formula time (or none), the misconception (yes/no, which one), brute-force-first (yes/no), the number of examples and how they grow, the hook type, the ending type, and the 5 moves you are most confident will appear.

Write only these files. Paraphrase only, with no quotes from real videos.
