# 3blue1brown: v2 rulebook (round 3)

This rulebook OVERRIDES `deep/reports/3blue1brown.md` wherever they conflict. Read the report for the channel's moves and voice, then apply these rules.
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
- **C1** (topic-conditional) Under 10 min: drop roadmap, recap, callback, notation; beats ~20-25 s  _evidence: LPZh9BOjkQs whole video_
- **C2** (missing-rule) Lemma block: claim now, justify within 60-100 s, optional second proof plus link  _evidence: d-o3eB9sfls 5:45-8:28_
- **C3** (underspecified) Iterate a construction exactly three times, label the last step, then jump to the limit  _evidence: d-o3eB9sfls 9:18-13:16_
- **C4** (missing-rule) Two-stage payoff: awe beat, voiced objection, then mechanical algebra  _evidence: d-o3eB9sfls 14:24-16:35_
- **C5** (missing-rule) Magnitude-guess quiz with a rising ladder of guesses near 40% of runtime  _evidence: LPZh9BOjkQs 3:19_

## D: corrections to the v1 report and storyboard
- **D1** DO NOT default to: Roadmap and caveat up front. It failed on held-out videos: LPZh9BOjkQs: no roadmap, inline signposts at 3:36; d-o3eB9sfls only a one-line pointer at 1:24
- **D2** DO NOT default to: Brute force: naive way, slightly wrong. It failed on held-out videos: d-o3eB9sfls: no numeric partial sums anywhere; LPZh9BOjkQs: none
- **D3** CONDITIONAL, use only when the video clearly calls for it: Wall or need posed as a design problem. Mixed evidence: d-o3eB9sfls 2:28 one redesign question; LPZh9BOjkQs 3:36 pre-training is not an assistant
- **D4** CONDITIONAL, use only when the video clearly calls for it: Notation late as shorthand for a picture. Mixed evidence: Order held but d-o3eB9sfls lemma formula at 6:17 (~37%), sums stay verbal; LPZh9BOjkQs none
- **D5** CONDITIONAL, use only when the video clearly calls for it: Callback and teaser to close. Mixed evidence: d-o3eB9sfls callback mid-video 14:24, ends on credits 16:35; LPZh9BOjkQs teaser by choice 7:08, no callback

## N: numeric targets fitted on 138 training transcripts from this channel
Aim for the median, and stay inside the p25-p75 range. Use the duration-band row that matches the video.

| ID | measure | band | p25 | median | p75 | n |
|---|---|---|---|---|---|---|
| N1 | words per minute | under10min | 164 | 173 | 184 | 22 |
| N2 | words per minute | over10min | 171 | 180 | 193 | 116 |
| N3 | "you/your" per 100 words | all | 1.62 | 2.05 | 2.50 | 138 |
| N4 | "I/me/my" per 100 words | all | 0.62 | 0.93 | 1.34 | 138 |
| N5 | "we/us/let's" per 100 words | all | 0.71 | 1.02 | 1.58 | 138 |
| N6 | numbers per 100 words | all | 1.62 | 2.49 | 3.70 | 138 |
| N7 | question marks per 100 words | all | 0.12 | 0.21 | 0.30 | 130 |
| N8 | mean words per sentence | all | 22 | 24 | 27 | 130 |
| N9 | hedges (probably/maybe/roughly...) per 100 words | all | 0.22 | 0.33 | 0.44 | 138 |
| N10 | example cues (for example/imagine/let's say...) per 100 words | all | 0.16 | 0.26 | 0.34 | 138 |

## B: default switches (training base rates)
- **B1** a sponsor read: seen in 24% of training videos → default OFF.
- **B2** a teaser for a next video in the last 12%: seen in 19% of training videos → default OFF.
- **B3** a spoken roadmap in the first 12%: seen in 20% of training videos → default OFF.
- **B4** a spoken recap in the last 20%: seen in 4% of training videos → default OFF.
  - If there is a sponsor read, place it at about 91% of runtime (p25-p75 80-96%).

## E: exemplars (training transcripts you may read to copy rhythm and structure, not content)
Pick the 1-2 closest to the test video by format and duration, read them, and name them in your header.
- `deep/compact/aircAruvnKk.txt` (18 min): But what is a neural network? | Deep learning chapter 1
- `deep/compact/r6sGWTCMz2k.txt` (24 min): But what is a Fourier series?  From heat flow to drawing with circles | DE4
- `deep/compact/bBC-nXj3Ng4.txt` (25 min): But how does bitcoin actually work?
- `deep/compact/OkmNXy7er84.txt` (11 min): The hardest problem on the hardest test
- `deep/compact/HEfHFsfGXjs.txt` (5 min): The most unexpected answer to a counting puzzle
- `deep/compact/fNk_zzaMoSs.txt` (9 min): Vectors | Chapter 1, Essence of linear algebra
- `deep/compact/spUNpyF58BY.txt` (19 min): But what is the Fourier Transform?  A visual introduction.
- `deep/compact/wjZofJX0v4M.txt` (27 min): Transformers, the tech behind LLMs | Deep Learning Chapter 5
- `deep/compact/v68zYyaEmEA.txt` (30 min): Solving Wordle using information theory
- `deep/compact/WUvTyaaNkzM.txt` (17 min): The essence of calculus
- `deep/compact/IHZwWFHWa-w.txt` (20 min): Gradient descent, how neural networks learn | Deep Learning Chapter 2
- `deep/compact/GNcFjFmqEc8.txt` (15 min): But why is a sphere's surface area four times its shadow?
- `deep/holdout/compact/d-o3eB9sfls.txt` (17 min): Why is pi here?  And why is it squared?  A geometric answer to the Basel problem
- `deep/holdout/compact/LPZh9BOjkQs.txt` (7 min): Large Language Models explained briefly
