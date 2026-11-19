# OverSimplified: v3 rulebook (round 4)

This replaces the v2 rulebook and the prose report. Everything here comes from training data only.

## 1. Structure: how this channel opens and closes (hand-labelled training videos, n=11)
Hook (the first spoken content after any sponsor/admin cold open): gag-skit 6, question 2, premise-claim 2, story-anecdote 1
Ending (the last CONTENT beat before any sponsor/Patreon outro): teaser-next 4, impact-coda 3, credits-after-result 3, phrase-mirror 1

Definitions (use these exact meanings in your slots):
- premise-claim: the first sentence states a striking fact, claim or set-up. It is NOT a question.
- question: the first spoken sentence IS a question to the viewer. Uncommon: 18 of 106 training hooks (17%).
- scenario-you: "Imagine you..." / "You are..." puts the viewer in a situation.
- story-anecdote: opens on a dated event or a person's story. gag-skit: a comic scene/dialogue. confession: the presenter talks about himself.
- phrase-mirror: the close returns to the opening's image, phrase or question (this is the whole "callback to the hook" family; do not use hook-callback).
- impact-coda: closes on a widening takeaway or consequence. teaser-next: names what the next video/part covers. credits-after-result: the result lands, then the video just stops.

**Use the card's `hook_default` and `ending_default` unless the title or topic clearly demands otherwise.** Do not open with a question just because the topic is a mystery: the channels state a premise first far more often.

## 2. Style notes for this channel (from round-2 held-out videos; guidance, not scored)
- **S1** (missing-rule) Defer the title object to ~30% (pig) or ~80% (kingdoms); open upstream  _evidence: QLq6GEiHqR8 12:00; 26EivpCPHnQ 14:17_
- **S2** (underspecified) Verbatim gag of 8-15 words reused 2-3 times with the last beat changed  _evidence: QLq6GEiHqR8 1:52, 2:57; 5:05, 15:50_
- **S3** (wrong-rule) Full-complexity map montage when actors exceed ~6, then one thread to keep  _evidence: 26EivpCPHnQ 9:33-12:11_
- **S4** (missing-rule) Perspective replay of one event from both sides with an adjudicator's repeated verdict  _evidence: QLq6GEiHqR8 30:24-32:25_
- **S5** (voice/craft) Humour is anachronistic, crude and voiced with stingers, not gentle analogy  _evidence: 26EivpCPHnQ 3:14; QLq6GEiHqR8 12:16_

## 3. Numbers and switches come from your per-video card
Your card `deep/round3/cards/<id>.json` has p25/median/p75 targets for this specific video (from its 20 nearest training videos by date and title), the sponsor/teaser/roadmap/recap defaults, a target word count and 2 exemplar transcripts. Aim for the median, stay inside p25-p75.

## 4. Verify, do not self-report
After drafting, run `python3 deep/round3/tools/check.py deep/round3/scripts/v3/<id>.md`. It measures your narration with the same code that scores it and prints PASS/FAIL per target. Revise the narration until at least 7 of the measured targets pass, then paste the checker's final JSON line into the file as the last ```json block. Never write a trace by hand.
