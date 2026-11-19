# 3blue1brown: v3 rulebook (round 4)

This replaces the v2 rulebook and the prose report. Everything here comes from training data only.

## 1. Structure: how this channel opens and closes (hand-labelled training videos, n=12)
Hook (the first spoken content after any sponsor/admin cold open): premise-claim 7, spectacle-demo 3, question 2
Ending (the last CONTENT beat before any sponsor/Patreon outro): teaser-next 7, impact-coda 1, advice 1, open-question 1, phrase-mirror 1, human-pivot 1

Definitions (use these exact meanings in your slots):
- premise-claim: the first sentence states a striking fact, claim or set-up. It is NOT a question.
- question: the first spoken sentence IS a question to the viewer. Uncommon: 18 of 106 training hooks (17%).
- scenario-you: "Imagine you..." / "You are..." puts the viewer in a situation.
- story-anecdote: opens on a dated event or a person's story. gag-skit: a comic scene/dialogue. confession: the presenter talks about himself.
- phrase-mirror: the close returns to the opening's image, phrase or question (this is the whole "callback to the hook" family; do not use hook-callback).
- impact-coda: closes on a widening takeaway or consequence. teaser-next: names what the next video/part covers. credits-after-result: the result lands, then the video just stops.

**Use the card's `hook_default` and `ending_default` unless the title or topic clearly demands otherwise.** Do not open with a question just because the topic is a mystery: the channels state a premise first far more often.

## 2. Style notes for this channel (from round-2 held-out videos; guidance, not scored)
- **S1** (topic-conditional) Under 10 min: drop roadmap, recap, callback, notation; beats ~20-25 s  _evidence: LPZh9BOjkQs whole video_
- **S2** (missing-rule) Lemma block: claim now, justify within 60-100 s, optional second proof plus link  _evidence: d-o3eB9sfls 5:45-8:28_
- **S3** (underspecified) Iterate a construction exactly three times, label the last step, then jump to the limit  _evidence: d-o3eB9sfls 9:18-13:16_
- **S4** (missing-rule) Two-stage payoff: awe beat, voiced objection, then mechanical algebra  _evidence: d-o3eB9sfls 14:24-16:35_
- **S5** (missing-rule) Magnitude-guess quiz with a rising ladder of guesses near 40% of runtime  _evidence: LPZh9BOjkQs 3:19_

## 3. Numbers and switches come from your per-video card
Your card `deep/round3/cards/<id>.json` has p25/median/p75 targets for this specific video (from its 20 nearest training videos by date and title), the sponsor/teaser/roadmap/recap defaults, a target word count and 2 exemplar transcripts. Aim for the median, stay inside p25-p75.

## 4. Verify, do not self-report
After drafting, run `python3 deep/round3/tools/check.py deep/round3/scripts/v3/<id>.md`. It measures your narration with the same code that scores it and prints PASS/FAIL per target. Revise the narration until at least 7 of the measured targets pass, then paste the checker's final JSON line into the file as the last ```json block. Never write a trace by hand.
