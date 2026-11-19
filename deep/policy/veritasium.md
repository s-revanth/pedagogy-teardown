# veritasium: v2 rulebook (round 3)

This rulebook OVERRIDES `deep/reports/veritasium.md` wherever they conflict. Read the report for the channel's moves and voice, then apply these rules.
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
- **C1** (underspecified) Win-then-wall relay ladder: person, year, blocker solved, new wall; countdown climax  _evidence: 88bMVbx1dzM 14:18-17:38_
- **C2** (missing-rule) Impact and legacy coda before the close, then hook reprise  _evidence: HeQX2HjkcNo 30:09-32:07; 88bMVbx1dzM 20:13_
- **C3** (missing-rule) Running toy object introduced in 90 s and returned to 3+ times as the climax  _evidence: HeQX2HjkcNo 0:51, 10:43, 29:42_
- **C4** (missing-rule) Impossibility theorem followed by a loophole in its hidden assumption  _evidence: 88bMVbx1dzM 14:01_
- **C5** (topic-conditional) Notation by formula type: governing relation early, symbol systems late  _evidence: 88bMVbx1dzM 1:26 vs HeQX2HjkcNo 12:13_

## D: corrections to the v1 report and storyboard
- **D1** CONDITIONAL, use only when the video clearly calls for it: Odd object or myth; popular explanation is wrong. Mixed evidence: Spectacle zoom at 88bMVbx1dzM 0:00 and hole-in-maths claim at HeQX2HjkcNo 0:00; no myth stated to the viewer
- **D2** DO NOT default to: Question backlog promised up front. It failed on held-out videos: 88bMVbx1dzM single question 0:34; HeQX2HjkcNo three questions only at 13:36 (~40%)
- **D3** CONDITIONAL, use only when the video clearly calls for it: Go there, do it: presenter acts it out with experts. Mixed evidence: 88bMVbx1dzM lab at 0:18 and 18:09; nothing similar in HeQX2HjkcNo
- **D4** DO NOT default to: Minimal block: one analogy, notation late or never. It failed on held-out videos: Formula at 88bMVbx1dzM 1:26; analogies after the formal version at HeQX2HjkcNo 9:33, 20:40
- **D5** DO NOT default to: Defuse the myth: ask for a prediction, then break it. It failed on held-out videos: No vote or commit prompt in either video
- **D6** CONDITIONAL, use only when the video clearly calls for it: Generalise, call back, then teaser or sponsor. Mixed evidence: HeQX2HjkcNo generalises 27:02-30:09, callback 32:07, sponsor last; 88bMVbx1dzM ends on lab significance

## N: numeric targets fitted on 409 training transcripts from this channel
Aim for the median, and stay inside the p25-p75 range. Use the duration-band row that matches the video.

| ID | measure | band | p25 | median | p75 | n |
|---|---|---|---|---|---|---|
| N1 | words per minute | under10min | 151 | 167 | 179 | 217 |
| N2 | words per minute | over10min | 157 | 166 | 175 | 192 |
| N3 | "you/your" per 100 words | all | 1.38 | 1.96 | 2.60 | 409 |
| N4 | "I/me/my" per 100 words | all | 0.78 | 1.37 | 2.17 | 409 |
| N5 | "we/us/let's" per 100 words | all | 0.55 | 1.04 | 1.51 | 409 |
| N6 | numbers per 100 words | all | 1.26 | 1.90 | 2.71 | 409 |
| N7 | question marks per 100 words | all | 0.29 | 0.47 | 0.81 | 313 |
| N8 | mean words per sentence | all | 14 | 15 | 18 | 313 |
| N9 | hedges (probably/maybe/roughly...) per 100 words | all | 0.10 | 0.19 | 0.32 | 409 |
| N10 | example cues (for example/imagine/let's say...) per 100 words | all | 0.00 | 0.08 | 0.15 | 409 |

## B: default switches (training base rates)
- **B1** a sponsor read: seen in 56% of training videos → CONDITIONAL: include only if the video type clearly calls for it.
- **B2** a teaser for a next video in the last 12%: seen in 4% of training videos → default OFF.
- **B3** a spoken roadmap in the first 12%: seen in 10% of training videos → default OFF.
- **B4** a spoken recap in the last 20%: seen in 1% of training videos → default OFF.
  - If there is a sponsor read, place it at about 76% of runtime (p25-p75 11-93%).

## E: exemplars (training transcripts you may read to copy rhythm and structure, not content)
Pick the 1-2 closest to the test video by format and duration, read them, and name them in your header.
- `deep/compact/uxPdPpi5W4o.txt` (12 min): Why Are 96,000,000 Black Balls on This Reservoir?
- `deep/compact/4Wrc4fHSCpw.txt` (20 min): These are the asteroids to worry about
- `deep/compact/MiUHjLxm3V0.txt` (55 min): The Closest Thing We Have to Alien Technology
- `deep/compact/AeJ9q45PfD0.txt` (12 min): World's Lightest Solid!
- `deep/compact/AF8d72mA41M.txt` (33 min): Why It Was Almost Impossible to Make the Blue LED
- `deep/compact/pir_muTzYM8.txt` (20 min): Inside The Navy's Indoor Ocean
- `deep/compact/094y1Z2wpJg.txt` (22 min): The Simplest Math Problem No One Can Solve - Collatz Conjecture
- `deep/compact/IV3dnLzthDA.txt` (24 min): The Man Who Accidentally Killed The Most People In History
- `deep/compact/GcdB5bFwio4.txt` (12 min): I Waterproofed Myself With Aerogel!
- `deep/compact/ZMByI4s-D-Y.txt` (11 min): World's Roundest Object!
- `deep/compact/OxGsU8oIWjY.txt` (6 min): How An Infinite Hotel Ran Out Of Room
- `deep/compact/SC2eSujzrUY.txt` (54 min): The Biggest Chemical Coverup In History
- `deep/holdout/compact/88bMVbx1dzM.txt` (21 min): Can You Keep Zooming In Infinitely?
- `deep/holdout/compact/HeQX2HjkcNo.txt` (34 min): Math's Fundamental Flaw
