# PrimerBlobs: v2 rulebook (round 3)

This rulebook OVERRIDES `deep/reports/PrimerBlobs.md` wherever they conflict. Read the report for the channel's moves and voice, then apply these rules.
Every rule has an ID. Your script must end with a `rule_trace` saying, for EVERY ID: `applied`, `n/a` (with the reason it does not apply to this video) or `broken` (with the reason).

## Step 0: classify before planning
Write down: duration band (<10 min / ≥10 min), format (from the title and series label), whether the title or opening states the answer, solved vs open question, and topic type. Rules marked IF depend on these.

## U: universal rules (from the round-2 held-out failures, seen in 3 or more channels)
- **U1** [high] IF Duration <10 min, series label, first-person title, or topic type (psychology, history-of-tech, open question, devlog) → Format gate before arc: pick an arc template per format and switch off unlicensed moves; under 10 min drop roadmap, recap, callback, notation, 20-25 s beats
- **U2** [high] IF Title or first 40 s states the answer, thesis or formula → Answer-given gate: state the answer by 0:40, an exception within 20 s, a concrete object by 1:30; skip brute-force numerics, the wall and staged misconception
- **U3** [high] IF Final 10% of runtime → Conditional ending: phrase mirror, impact coda, human pivot, applied game or credits; hook callback only if the hook question is still open, teaser only in a series
- **U4** [high] IF A cause, toy object, model or gag has been installed → Recurring anchor: reuse one object, cause tag or gag line 3-5 times, each pass adding a layer or changing the last beat
- **U5** [high] IF Any symbol or formula → Notation keyed to referent and formula kind: symbol within ~60 s of one worked referent; governing or cost formulas may be early, symbol systems late; no runtime-fraction rule
- **U6** [high] IF Writing narration → Per-channel pace: use measured channel wpm (140-191 pooled) and 15-30 s beats for fast channels, never a universal 170
- **U7** [high] IF Generator about to add roadmap, vote, commit prompt or planted misconception → Drop default up-front furniture: front roadmap only with 3+ parallel open questions; otherwise inline signposts; no vote or commit in the hook; misconception only as definition-by-contrast
- **U8** [med] IF Claim type is open, proved, approximate, advice or evidence-based → Typed caveats: epistemic per candidate for open questions, domain caveat in proofs, approximate-winner note, safety referral for advice, inline concessions for theses
- **U9** [med] IF Binary decision, absurd magnitude, or a dependent next step → One real viewer turn mid-video: pause, guess or checkpoint at 40-65% of runtime, answered within 10-30 s
- **U10** [med] IF History of invention, a thesis with exemptions, or an escalating antagonist → Ladder of named rungs: 4-6 rungs, each a named person/tier plus one number, ending in a wall or break, 1.5-3 min each
- **U11** [med] IF Title names an application, trigger event or end state → Defer the title object: open upstream; first mention at ~25-30% of runtime, or later for named applications

## C: channel rules found on round-2 held-out videos
- **C1** (topic-conditional) Three-template switch: sim exploration, named-formula derivation, on-camera reflection  _evidence: 6YzrVUVO9M0 0:00; t9N9S4loyu8 0:20_
- **C2** (missing-rule) Pain-driven second act: state the cost, show the closed form, derive it factor by factor  _evidence: 6YzrVUVO9M0 8:54-13:11_
- **C3** (underspecified) Checkpoint pauses before dependent steps, distinct from prediction pauses  _evidence: 6YzrVUVO9M0 5:40, 11:19_
- **C4** (missing-rule) Numbered lessons with a count roadmap and the strongest item last  _evidence: t9N9S4loyu8 1:57, 6:57_
- **C5** (underspecified) Dignify-then-dismiss applied to the presenter's own past reasoning  _evidence: t9N9S4loyu8 2:49-3:05_

## D: corrections to the v1 report and storyboard
- **D1** CONDITIONAL, use only when the video clearly calls for it: Familiar blob world first. Mixed evidence: 6YzrVUVO9M0 blobs take over at 0:30 after a human hook; t9N9S4loyu8 has no blobs (on camera)
- **D2** CONDITIONAL, use only when the video clearly calls for it: Dumb baseline run first. Mixed evidence: 6YzrVUVO9M0 n=1,2,3 enumerated by hand 1:02-3:45; t9N9S4loyu8 none
- **D3** CONDITIONAL, use only when the video clearly calls for it: Predict pause with outcomes listed. Mixed evidence: One predict pause 6YzrVUVO9M0 2:41; others are checkpoints 5:40, 11:19; none in t9N9S4loyu8
- **D4** DO NOT default to: Run, surprise: the sim settles it. It failed on held-out videos: Sim only as a late check at 6YzrVUVO9M0 13:28 (~88%); no sim in t9N9S4loyu8
- **D5** CONDITIONAL, use only when the video clearly calls for it: Name it after the behaviour was seen. Mixed evidence: Formula shown at 6YzrVUVO9M0 0:00, decoded 4:33; t9N9S4loyu8 terms after lay definitions 3:05
- **D6** DO NOT default to: Break it with a parameter flip. It failed on held-out videos: No break in either; independence caveat only stated at 6YzrVUVO9M0 5:57
- **D7** DO NOT default to: Teaser then thanks at the end. It failed on held-out videos: Pointer to the fix at the front, t9N9S4loyu8 0:37; no end teaser in either

## N: numeric targets fitted on 14 training transcripts from this channel
Aim for the median, and stay inside the p25-p75 range. Use the duration-band row that matches the video.

| ID | measure | band | p25 | median | p75 | n |
|---|---|---|---|---|---|---|
| N1 | words per minute | over10min | 169 | 175 | 183 | 12 |
| N2 | "you/your" per 100 words | all | 0.63 | 0.78 | 1.13 | 14 |
| N3 | "I/me/my" per 100 words | all | 0.36 | 0.59 | 0.87 | 14 |
| N4 | "we/us/let's" per 100 words | all | 2.03 | 2.63 | 2.96 | 14 |
| N5 | numbers per 100 words | all | 2.24 | 2.78 | 3.68 | 14 |
| N6 | question marks per 100 words | all | 0.29 | 0.41 | 0.46 | 5 |
| N7 | mean words per sentence | all | 17 | 17 | 22 | 5 |
| N8 | hedges (probably/maybe/roughly...) per 100 words | all | 0.32 | 0.39 | 0.44 | 14 |
| N9 | example cues (for example/imagine/let's say...) per 100 words | all | 0.05 | 0.07 | 0.09 | 14 |

## B: default switches (training base rates)
- **B1** a sponsor read: seen in 50% of training videos → CONDITIONAL: include only if the video type clearly calls for it.
- **B2** a teaser for a next video in the last 12%: seen in 36% of training videos → CONDITIONAL: include only if the video type clearly calls for it.
- **B3** a spoken roadmap in the first 12%: seen in 57% of training videos → CONDITIONAL: include only if the video type clearly calls for it.
- **B4** a spoken recap in the last 20%: seen in 0% of training videos → default OFF.
  - If there is a sponsor read, place it at about 96% of runtime (p25-p75 6-97%).

## E: exemplars (training transcripts you may read to copy rhythm and structure, not content)
Pick the 1-2 closest to the test video by format and duration, read them, and name them in your header.
- `deep/compact/YNMkADpvO4w.txt` (13 min): Simulating the Evolution of Aggression
- `deep/compact/0ZGbIKd0XrM.txt` (10 min): Simulating Natural Selection
- `deep/compact/XTcP4oo4JI4.txt` (22 min): How To Catch A Cheater With Math
- `deep/compact/iLX_r_WPrIw.txt` (20 min): Simulating the Evolution of Sacrificing for Family
- `deep/compact/7OLpKqTriio.txt` (12 min): Epidemic, Endemic, and Eradication Simulations
- `deep/compact/PNtKXWNKGN8.txt` (12 min): Simulating Supply and Demand
- `deep/compact/tCoEYFbDVoI.txt` (15 min): Simulating the Evolution of Rock, Paper, Scissors
- `deep/compact/goePYJ74Ydg.txt` (13 min): Simulating Green Beard Altruism
- `deep/compact/yhO6jfHPFQU.txt` (14 min): Simulating alternate voting systems
- `deep/compact/nsVD8VPh96w.txt` (10 min): Simulating Foraging Decisions
- `deep/compact/1_JbJTeLZJs.txt` (32 min): Simulating the Evolution of Aging
- `deep/compact/uRTtlpD_U54.txt` (7 min): Simulating Competition and Logistic Growth
- `deep/holdout/compact/6YzrVUVO9M0.txt` (15 min): Overexplaining the binomial distribution
- `deep/holdout/compact/t9N9S4loyu8.txt` (8 min): How I deceived myself
