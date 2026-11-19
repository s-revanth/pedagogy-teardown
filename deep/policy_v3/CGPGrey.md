# CGPGrey: v3 rulebook (round 4)

This replaces the v2 rulebook and the prose report. Everything here comes from training data only.

## 1. Structure: how this channel opens and closes (hand-labelled training videos, n=12)
Hook (the first spoken content after any sponsor/admin cold open): premise-claim 5, scenario-you 4, question 2, gag-skit 1
Ending (the last CONTENT beat before any sponsor/Patreon outro): phrase-mirror 5, impact-coda 3, other 2, advice 1, credits-after-result 1

Definitions (use these exact meanings in your slots):
- premise-claim: the first sentence states a striking fact, claim or set-up. It is NOT a question.
- question: the first spoken sentence IS a question to the viewer. Uncommon: 18 of 106 training hooks (17%).
- scenario-you: "Imagine you..." / "You are..." puts the viewer in a situation.
- story-anecdote: opens on a dated event or a person's story. gag-skit: a comic scene/dialogue. confession: the presenter talks about himself.
- phrase-mirror: the close returns to the opening's image, phrase or question (this is the whole "callback to the hook" family; do not use hook-callback).
- impact-coda: closes on a widening takeaway or consequence. teaser-next: names what the next video/part covers. credits-after-result: the result lands, then the video just stops.

**Use the card's `hook_default` and `ending_default` unless the title or topic clearly demands otherwise.** Do not open with a question just because the topic is a mystery: the channels state a premise first far more often.

## 2. Style notes for this channel (from round-2 held-out videos; guidance, not scored)
- **S1** (topic-conditional) Title carries the thesis: plain premise or question in 3 s, through-line analogy by ~0:20  _evidence: boezS4C_MFc 0:00-0:16; 7Pq-S557XQU 0:03_
- **S2** (missing-rule) Ladder of exemptions: surely-X-is-safe, broken with named instances and a number, title card each  _evidence: 7Pq-S557XQU 7:00, 9:03, 11:06_
- **S3** (missing-rule) Reverse the analogy when the viewer's intuition about the familiar case is right  _evidence: 7Pq-S557XQU 4:08-4:24_
- **S4** (missing-rule) Ambiguity shown as two parses, then a worst case that exploits it  _evidence: boezS4C_MFc 4:21, 8:26_
- **S5** (voice/craft) Beats ~21 s at 176-187 wpm with bracketed rapid-list asides  _evidence: boezS4C_MFc 6:47-7:33; 7Pq-S557XQU whole_

## 3. Numbers and switches come from your per-video card
Your card `deep/round3/cards/<id>.json` has p25/median/p75 targets for this specific video (from its 20 nearest training videos by date and title), the sponsor/teaser/roadmap/recap defaults, a target word count and 2 exemplar transcripts. Aim for the median, stay inside p25-p75.

## 4. Verify, do not self-report
After drafting, run `python3 deep/round3/tools/check.py deep/round3/scripts/v3/<id>.md`. It measures your narration with the same code that scores it and prints PASS/FAIL per target. Revise the narration until at least 7 of the measured targets pass, then paste the checker's final JSON line into the file as the last ```json block. Never write a trace by hand.
