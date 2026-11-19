# Reducible: v2 rulebook (round 3)

This rulebook OVERRIDES `deep/reports/Reducible.md` wherever they conflict. Read the report for the channel's moves and voice, then apply these rules.
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
- **C1** (missing-rule) Property-hunt arc: hint-led counterexample challenges, then name the failing property  _evidence: JGQe4kiPnrU 7:46, 10:04_
- **C2** (missing-rule) Definition-decode beat at 40-55% of runtime, clause by clause on one function  _evidence: Q_1M2JaijjQ 9:01-11:44_
- **C3** (wrong-rule) Story frame with two named solvers carries a whole comparison video  _evidence: Q_1M2JaijjQ 0:59-8:44_
- **C4** (topic-conditional) Hold the named application until theory is built (~77%)  _evidence: JGQe4kiPnrU 19:28_
- **C5** (voice/craft) Dry self-aware reactions to jargon density  _evidence: Q_1M2JaijjQ 0:15, 9:31; JGQe4kiPnrU 8:41_

## D: corrections to the v1 report and storyboard
- **D1** CONDITIONAL, use only when the video clearly calls for it: Hook or goal: promise something beautiful or surprising. Mixed evidence: Hooks are a classroom anecdote (Q_1M2JaijjQ 0:00) and a user scenario (JGQe4kiPnrU 0:00-0:14); no spectacle
- **D2** CONDITIONAL, use only when the video clearly calls for it: Brute force run in full. Mixed evidence: Q_1M2JaijjQ triple loop at 0:59; JGQe4kiPnrU brute force is method 1 of 3 at 13:30 and wins at scale
- **D3** CONDITIONAL, use only when the video clearly calls for it: Name, notation, code last. Mixed evidence: Order held; position not: matrix at JGQe4kiPnrU 5:52 (~23%), Big O named 8:14 (~46%)
- **D4** CONDITIONAL, use only when the video clearly calls for it: Recap and callback. Mixed evidence: Q_1M2JaijjQ recap mirrors roadmap 16:49; no callback or teaser in either

## N: numeric targets fitted on 14 training transcripts from this channel
Aim for the median, and stay inside the p25-p75 range. Use the duration-band row that matches the video.

| ID | measure | band | p25 | median | p75 | n |
|---|---|---|---|---|---|---|
| N1 | words per minute | over10min | 165 | 172 | 184 | 12 |
| N2 | "you/your" per 100 words | all | 0.73 | 1.05 | 1.35 | 14 |
| N3 | "I/me/my" per 100 words | all | 0.46 | 0.75 | 1.10 | 14 |
| N4 | "we/us/let's" per 100 words | all | 2.46 | 3.76 | 4.00 | 14 |
| N5 | numbers per 100 words | all | 1.82 | 2.56 | 3.19 | 14 |
| N6 | hedges (probably/maybe/roughly...) per 100 words | all | 0.10 | 0.16 | 0.24 | 14 |
| N7 | example cues (for example/imagine/let's say...) per 100 words | all | 0.15 | 0.22 | 0.37 | 14 |

## B: default switches (training base rates)
- **B1** a sponsor read: seen in 86% of training videos → default ON.
- **B2** a teaser for a next video in the last 12%: seen in 71% of training videos → default ON.
- **B3** a spoken roadmap in the first 12%: seen in 86% of training videos → default ON.
- **B4** a spoken recap in the last 20%: seen in 14% of training videos → default OFF.
  - If there is a sponsor read, place it at about 99% of runtime (p25-p75 96-99%).

## E: exemplars (training transcripts you may read to copy rhythm and structure, not content)
Pick the 1-2 closest to the test video by format and duration, read them, and name them in your header.
- `deep/compact/h7apO7q16V0.txt` (28 min): The Fast Fourier Transform (FFT): Most Ingenious Algorithm Ever?
- `deep/compact/ngCos392W4w.txt` (21 min): 5 Simple Steps for Solving Any Recursive Problem
- `deep/compact/aPQY__2H3tE.txt` (21 min): 5 Simple Steps for Solving Dynamic Programming Problems
- `deep/compact/0me3guauqOU.txt` (34 min): The Unreasonable Effectiveness of JPEG: A Signal Processing Approach
- `deep/compact/LFKZLXVO-Dg.txt` (16 min): Introduction to Graph Theory: A Computer Science Perspective
- `deep/compact/EFUYNoFRHQI.txt` (32 min): How PNG Works: Compromising Speed for Quality
- `deep/compact/rf6uf3jNjbo.txt` (21 min): Towers of Hanoi: A Complete Recursive Visualization
- `deep/compact/PMMc4VsIacU.txt` (20 min): Depth First Search (DFS) Explained: Algorithm, Examples, and Code
- `deep/compact/eED4bSkYCB8.txt` (28 min): Building Collision Simulations: An Introduction to Computer Graphics
- `deep/compact/6oMZb3yP_H8.txt` (28 min): How Computers Draw Weird Shapes (Marching Squares)
- `deep/compact/xlVX7dXLS64.txt` (10 min): Breadth First Search (BFS): Visualized and Explained
- `deep/compact/ajv46BSqcK4.txt` (31 min): A Strange But Elegant Approach to a Surprisingly Hard Problem (GJK Algorithm)
- `deep/holdout/compact/Q_1M2JaijjQ.txt` (17 min): What Is Big O Notation?
- `deep/holdout/compact/JGQe4kiPnrU.txt` (25 min): PageRank: A Trillion Dollar Algorithm
