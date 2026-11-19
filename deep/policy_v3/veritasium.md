# veritasium: v3 rulebook (round 4)

This replaces the v2 rulebook and the prose report. Everything here comes from training data only.

## 1. Structure: how this channel opens and closes (hand-labelled training videos, n=12)
Hook (the first spoken content after any sponsor/admin cold open): premise-claim 4, spectacle-demo 3, story-anecdote 3, question 1, scenario-you 1
Ending (the last CONTENT beat before any sponsor/Patreon outro): phrase-mirror 5, teaser-next 3, credits-after-result 1, advice 1, human-pivot 1, impact-coda 1

Definitions (use these exact meanings in your slots):
- premise-claim: the first sentence states a striking fact, claim or set-up. It is NOT a question.
- question: the first spoken sentence IS a question to the viewer. Uncommon: 18 of 106 training hooks (17%).
- scenario-you: "Imagine you..." / "You are..." puts the viewer in a situation.
- story-anecdote: opens on a dated event or a person's story. gag-skit: a comic scene/dialogue. confession: the presenter talks about himself.
- phrase-mirror: the close returns to the opening's image, phrase or question (this is the whole "callback to the hook" family; do not use hook-callback).
- impact-coda: closes on a widening takeaway or consequence. teaser-next: names what the next video/part covers. credits-after-result: the result lands, then the video just stops.

**Use the card's `hook_default` and `ending_default` unless the title or topic clearly demands otherwise.** Do not open with a question just because the topic is a mystery: the channels state a premise first far more often.

## 2. Style notes for this channel (from round-2 held-out videos; guidance, not scored)
- **S1** (underspecified) Win-then-wall relay ladder: person, year, blocker solved, new wall; countdown climax  _evidence: 88bMVbx1dzM 14:18-17:38_
- **S2** (missing-rule) Impact and legacy coda before the close, then hook reprise  _evidence: HeQX2HjkcNo 30:09-32:07; 88bMVbx1dzM 20:13_
- **S3** (missing-rule) Running toy object introduced in 90 s and returned to 3+ times as the climax  _evidence: HeQX2HjkcNo 0:51, 10:43, 29:42_
- **S4** (missing-rule) Impossibility theorem followed by a loophole in its hidden assumption  _evidence: 88bMVbx1dzM 14:01_
- **S5** (topic-conditional) Notation by formula type: governing relation early, symbol systems late  _evidence: 88bMVbx1dzM 1:26 vs HeQX2HjkcNo 12:13_

## 3. Numbers and switches come from your per-video card
Your card `deep/round3/cards/<id>.json` has p25/median/p75 targets for this specific video (from its 20 nearest training videos by date and title), the sponsor/teaser/roadmap/recap defaults, a target word count and 2 exemplar transcripts. Aim for the median, stay inside p25-p75.

## 4. Verify, do not self-report
After drafting, run `python3 deep/round3/tools/check.py deep/round3/scripts/v3/<id>.md`. It measures your narration with the same code that scores it and prints PASS/FAIL per target. Revise the narration until at least 7 of the measured targets pass, then paste the checker's final JSON line into the file as the last ```json block. Never write a trace by hand.
