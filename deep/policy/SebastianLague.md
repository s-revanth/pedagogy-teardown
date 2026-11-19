# SebastianLague: v2 rulebook (round 3)

This rulebook OVERRIDES `deep/reports/SebastianLague.md` wherever they conflict. Read the report for the channel's moves and voice, then apply these rules.
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
- **C1** (topic-conditional) Format gate: impersonal lecture series vs devlog vs designed-lesson adventure  _evidence: l-hh51ncgDI 0:15-10:46 vs X-iSQQgOd1A_
- **C2** (missing-rule) Layered reruns of one example, one overlay per pass, answer unchanged  _evidence: l-hh51ncgDI 1:10, 3:56, 5:06, 8:44_
- **C3** (wrong-rule) Pause-the-video quiz at ~65% of runtime in lecture format  _evidence: l-hh51ncgDI 7:06_
- **C4** (underspecified) Cite the design source (paper, video) at the moment of choice  _evidence: X-iSQQgOd1A 6:19, 6:37, 7:10_
- **C5** (missing-rule) Open a devlog with an adjacent classic problem and a human-scale blow-up number  _evidence: X-iSQQgOd1A 0:02-4:28_

## D: corrections to the v1 report and storyboard
- **D1** CONDITIONAL, use only when the video clearly calls for it: It breaks: failure on screen. Mixed evidence: X-iSQQgOd1A factorial blow-up 0:51, Unity bug 4:47; l-hh51ncgDI only bad move ordering 6:26
- **D2** DO NOT default to: Smallest repair: term named after the failure. It failed on held-out videos: X-iSQQgOd1A evaporation 7:28 and diffusion 12:44 arrive ungated; pruning motivated by wasted work 5:21
- **D3** CONDITIONAL, use only when the video clearly calls for it: Turn one knob to isolate a cause. Mixed evidence: One knob X-iSQQgOd1A 5:23; parameter exploration left unnarrated 14:15-15:59
- **D4** DO NOT default to: Honest close: limits, wishlist, callback, teaser. It failed on held-out videos: X-iSQQgOd1A ends with links to others' work; l-hh51ncgDI one-line recap plus a chess game 10:18
- **D5** DO NOT default to: Theory: equation revealed as a label after behaviour. It failed on held-out videos: Formulas precede the demo at X-iSQQgOd1A 1:06, 1:43

## N: numeric targets fitted on 264 training transcripts from this channel
Aim for the median, and stay inside the p25-p75 range. Use the duration-band row that matches the video.

| ID | measure | band | p25 | median | p75 | n |
|---|---|---|---|---|---|---|
| N1 | words per minute | under10min | 141 | 160 | 180 | 62 |
| N2 | words per minute | over10min | 137 | 146 | 158 | 202 |
| N3 | "you/your" per 100 words | all | 0.23 | 0.42 | 0.78 | 264 |
| N4 | "I/me/my" per 100 words | all | 0.94 | 1.81 | 2.81 | 264 |
| N5 | "we/us/let's" per 100 words | all | 2.55 | 4.42 | 5.70 | 264 |
| N6 | numbers per 100 words | all | 0.95 | 1.49 | 2.12 | 264 |
| N7 | question marks per 100 words | all | 0.00 | 0.00 | 0.09 | 15 |
| N8 | mean words per sentence | all | 19 | 21 | 25 | 15 |
| N9 | hedges (probably/maybe/roughly...) per 100 words | all | 0.11 | 0.21 | 0.35 | 264 |
| N10 | example cues (for example/imagine/let's say...) per 100 words | all | 0.03 | 0.08 | 0.18 | 264 |

## B: default switches (training base rates)
- **B1** a sponsor read: seen in 9% of training videos → default OFF.
- **B2** a teaser for a next video in the last 12%: seen in 66% of training videos → default ON.
- **B3** a spoken roadmap in the first 12%: seen in 35% of training videos → CONDITIONAL: include only if the video type clearly calls for it.
- **B4** a spoken recap in the last 20%: seen in 2% of training videos → default OFF.
  - If there is a sponsor read, place it at about 55% of runtime (p25-p75 5-95%).

## E: exemplars (training transcripts you may read to copy rhythm and structure, not content)
Pick the 1-2 closest to the test video by format and duration, read them, and name them in your header.
- `deep/compact/I0-izyq6q5s.txt` (19 min): How Do Computers Remember?
- `deep/compact/sLqXFF8mlEU.txt` (31 min): I Tried Creating a Game Using Real-World Geographic Data
- `deep/compact/U4ogK0MIzqk.txt` (29 min): Coding Adventure: Chess
- `deep/compact/QZwneRb-zqA.txt` (18 min): Exploring How Computers Work
- `deep/compact/UXD97l7ZT0w.txt` (36 min): Trying to Improve My Geography Game with More Real-World Data
- `deep/compact/PGk0rnyTa1U.txt` (17 min): I Spent a Week Making a Game about Vacuuming
- `deep/compact/rSKMYc1CQHE.txt` (47 min): Coding Adventure: Simulating Fluids
- `deep/compact/TURzbXTNaA0.txt` (9 min): I Created a (terrible) Video Game Console
- `deep/compact/r_It_X7v-1E.txt` (6 min): Coding Adventure: Simulating an Ecosystem
- `deep/compact/pNp4ug5F6To.txt` (26 min): Polishing and Releasing My Tiny Geography Game
- `deep/compact/hfMk-kjRv4c.txt` (54 min): I Tried Coding a Neural Network to Identify Doodles
- `deep/compact/-L-WgKMFuhE.txt` (11 min): A* Pathfinding (E01: algorithm explanation)
- `deep/holdout/compact/X-iSQQgOd1A.txt` (17 min): Coding Adventure: Ant and Slime Simulations
- `deep/holdout/compact/l-hh51ncgDI.txt` (11 min): Algorithms Explained – minimax and alpha-beta pruning
