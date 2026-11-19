# SebastianLague: v3 rulebook (round 4)

This replaces the v2 rulebook and the prose report. Everything here comes from training data only.

## 1. Structure: how this channel opens and closes (hand-labelled training videos, n=12)
Hook (the first spoken content after any sponsor/admin cold open): story-anecdote 3, premise-claim 3, confession 3, spectacle-demo 2, question 1
Ending (the last CONTENT beat before any sponsor/Patreon outro): teaser-next 5, credits-after-result 4, human-pivot 3

Definitions (use these exact meanings in your slots):
- premise-claim: the first sentence states a striking fact, claim or set-up. It is NOT a question.
- question: the first spoken sentence IS a question to the viewer. Uncommon: 18 of 106 training hooks (17%).
- scenario-you: "Imagine you..." / "You are..." puts the viewer in a situation.
- story-anecdote: opens on a dated event or a person's story. gag-skit: a comic scene/dialogue. confession: the presenter talks about himself.
- phrase-mirror: the close returns to the opening's image, phrase or question (this is the whole "callback to the hook" family; do not use hook-callback).
- impact-coda: closes on a widening takeaway or consequence. teaser-next: names what the next video/part covers. credits-after-result: the result lands, then the video just stops.

**Use the card's `hook_default` and `ending_default` unless the title or topic clearly demands otherwise.** Do not open with a question just because the topic is a mystery: the channels state a premise first far more often.

## 2. Style notes for this channel (from round-2 held-out videos; guidance, not scored)
- **S1** (topic-conditional) Format gate: impersonal lecture series vs devlog vs designed-lesson adventure  _evidence: l-hh51ncgDI 0:15-10:46 vs X-iSQQgOd1A_
- **S2** (missing-rule) Layered reruns of one example, one overlay per pass, answer unchanged  _evidence: l-hh51ncgDI 1:10, 3:56, 5:06, 8:44_
- **S3** (wrong-rule) Pause-the-video quiz at ~65% of runtime in lecture format  _evidence: l-hh51ncgDI 7:06_
- **S4** (underspecified) Cite the design source (paper, video) at the moment of choice  _evidence: X-iSQQgOd1A 6:19, 6:37, 7:10_
- **S5** (missing-rule) Open a devlog with an adjacent classic problem and a human-scale blow-up number  _evidence: X-iSQQgOd1A 0:02-4:28_

## 3. Numbers and switches come from your per-video card
Your card `deep/round3/cards/<id>.json` has p25/median/p75 targets for this specific video (from its 20 nearest training videos by date and title), the sponsor/teaser/roadmap/recap defaults, a target word count and 2 exemplar transcripts. Aim for the median, stay inside p25-p75.

## 4. Verify, do not self-report
After drafting, run `python3 deep/round3/tools/check.py deep/round3/scripts/v3/<id>.md`. It measures your narration with the same code that scores it and prints PASS/FAIL per target. Revise the narration until at least 7 of the measured targets pass, then paste the checker's final JSON line into the file as the last ```json block. Never write a trace by hand.
