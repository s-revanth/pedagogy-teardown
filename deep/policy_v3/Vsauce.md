# Vsauce: v3 rulebook (round 4)

This replaces the v2 rulebook and the prose report. Everything here comes from training data only.

## 1. Structure: how this channel opens and closes (hand-labelled training videos, n=11)
Hook (the first spoken content after any sponsor/admin cold open): premise-claim 5, question 3, story-anecdote 1, spectacle-demo 1, scenario-you 1
Ending (the last CONTENT beat before any sponsor/Patreon outro): impact-coda 5, phrase-mirror 5, teaser-next 1

Definitions (use these exact meanings in your slots):
- premise-claim: the first sentence states a striking fact, claim or set-up. It is NOT a question.
- question: the first spoken sentence IS a question to the viewer. Uncommon: 18 of 106 training hooks (17%).
- scenario-you: "Imagine you..." / "You are..." puts the viewer in a situation.
- story-anecdote: opens on a dated event or a person's story. gag-skit: a comic scene/dialogue. confession: the presenter talks about himself.
- phrase-mirror: the close returns to the opening's image, phrase or question (this is the whole "callback to the hook" family; do not use hook-callback).
- impact-coda: closes on a widening takeaway or consequence. teaser-next: names what the next video/part covers. credits-after-result: the result lands, then the video just stops.

**Use the card's `hook_default` and `ending_default` unless the title or topic clearly demands otherwise.** Do not open with a question just because the topic is a mystery: the channels state a premise first far more often.

## 2. Style notes for this channel (from round-2 held-out videos; guidance, not scored)
- **S1** (wrong-rule) Answer first, then an exception within 20 s  _evidence: JTvcpdfGUtQ 0:18-0:34; fCn8zs912OE 0:39_
- **S2** (missing-rule) Late pivot of the title idea to the human condition, ending on a quote  _evidence: JTvcpdfGUtQ 8:53-12:57; fCn8zs912OE 18:20-20:04_
- **S3** (wrong-rule) Sanctioned 2-3 min detour (up to ~20%) joined by one pivot sentence  _evidence: JTvcpdfGUtQ 3:26-6:22; fCn8zs912OE 4:18-6:43_
- **S4** (underspecified) Barrage repetition: 8-14 one-clause instances in under 70 s  _evidence: fCn8zs912OE 3:08-3:42_
- **S5** (voice/craft) Measured pace 134-148 wpm on full runtime, not ~170  _evidence: JTvcpdfGUtQ 148; fCn8zs912OE 134 (139 over speech span)_

## 3. Numbers and switches come from your per-video card
Your card `deep/round3/cards/<id>.json` has p25/median/p75 targets for this specific video (from its 20 nearest training videos by date and title), the sponsor/teaser/roadmap/recap defaults, a target word count and 2 exemplar transcripts. Aim for the median, stay inside p25-p75.

## 4. Verify, do not self-report
After drafting, run `python3 deep/round3/tools/check.py deep/round3/scripts/v3/<id>.md`. It measures your narration with the same code that scores it and prints PASS/FAIL per target. Revise the narration until at least 7 of the measured targets pass, then paste the checker's final JSON line into the file as the last ```json block. Never write a trace by hand.
