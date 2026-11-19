# OverSimplified: v2 rulebook (round 3)

This rulebook OVERRIDES `deep/reports/OverSimplified.md` wherever they conflict. Read the report for the channel's moves and voice, then apply these rules.
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
- **C1** (missing-rule) Defer the title object to ~30% (pig) or ~80% (kingdoms); open upstream  _evidence: QLq6GEiHqR8 12:00; 26EivpCPHnQ 14:17_
- **C2** (underspecified) Verbatim gag of 8-15 words reused 2-3 times with the last beat changed  _evidence: QLq6GEiHqR8 1:52, 2:57; 5:05, 15:50_
- **C3** (wrong-rule) Full-complexity map montage when actors exceed ~6, then one thread to keep  _evidence: 26EivpCPHnQ 9:33-12:11_
- **C4** (missing-rule) Perspective replay of one event from both sides with an adjudicator's repeated verdict  _evidence: QLq6GEiHqR8 30:24-32:25_
- **C5** (voice/craft) Humour is anachronistic, crude and voiced with stingers, not gentle analogy  _evidence: 26EivpCPHnQ 3:14; QLq6GEiHqR8 12:16_

## D: corrections to the v1 report and storyboard
- **D1** CONDITIONAL, use only when the video clearly calls for it: Cold open: sponsor, then a cheeky modern joke. Mixed evidence: Sponsor tag 0:00-0:15 in both, but the skit is in-period, not modern (26EivpCPHnQ 0:15; QLq6GEiHqR8 0:16)
- **D2** CONDITIONAL, use only when the video clearly calls for it: Flip: state the comfortable belief, then say wrong. Mixed evidence: 26EivpCPHnQ Han golden age flipped 1:21; QLq6GEiHqR8 uses false resolution instead at 1:52, 2:24, 8:58
- **D3** DO NOT default to: Roadmap: one-line cause chain. It failed on held-out videos: Absent in both videos
- **D4** DO NOT default to: Tonal pivot or flagged fabrication. It failed on held-out videos: No pivot; Civil War delivered flat at QLq6GEiHqR8 34:20; only legend hedges at 26EivpCPHnQ 8:24

## N: numeric targets fitted on 22 training transcripts from this channel
Aim for the median, and stay inside the p25-p75 range. Use the duration-band row that matches the video.

| ID | measure | band | p25 | median | p75 | n |
|---|---|---|---|---|---|---|
| N1 | words per minute | under10min | 200 | 200 | 200 | 3 |
| N2 | words per minute | over10min | 186 | 191 | 218 | 19 |
| N3 | "you/your" per 100 words | all | 0.90 | 1.43 | 1.73 | 22 |
| N4 | "I/me/my" per 100 words | all | 0.63 | 1.07 | 1.40 | 22 |
| N5 | "we/us/let's" per 100 words | all | 0.39 | 0.57 | 0.69 | 22 |
| N6 | numbers per 100 words | all | 1.04 | 1.26 | 1.55 | 22 |
| N7 | question marks per 100 words | all | 0.65 | 0.78 | 1.10 | 20 |
| N8 | mean words per sentence | all | 12 | 12 | 13 | 20 |
| N9 | hedges (probably/maybe/roughly...) per 100 words | all | 0.09 | 0.15 | 0.19 | 22 |
| N10 | example cues (for example/imagine/let's say...) per 100 words | all | 0.00 | 0.03 | 0.05 | 22 |

## B: default switches (training base rates)
- **B1** a sponsor read: seen in 77% of training videos → default ON.
- **B2** a teaser for a next video in the last 12%: seen in 0% of training videos → default OFF.
- **B3** a spoken roadmap in the first 12%: seen in 0% of training videos → default OFF.
- **B4** a spoken recap in the last 20%: seen in 0% of training videos → default OFF.
  - If there is a sponsor read, place it at about 0% of runtime (p25-p75 0-0%).

## E: exemplars (training transcripts you may read to copy rhythm and structure, not content)
Pick the 1-2 closest to the test video by format and duration, read them, and name them in your header.
- `deep/compact/_uk_6vfqwTA.txt` (13 min): WW2 - OverSimplified (Part 1)
- `deep/compact/I79TpDe3t2g.txt` (16 min): The Cold War - OverSimplified (Part 1)
- `deep/compact/tsxmyL7TUJg.txt` (29 min): The American Civil War - OverSimplified (Part 1)
- `deep/compact/zqllxbPWKNI.txt` (29 min): The Napoleonic Wars  - OverSimplified (Part 1)
- `deep/compact/fo2Rb9h788s.txt` (15 min): WW2 - OverSimplified (Part 2)
- `deep/compact/gzALIXcY4pg.txt` (15 min): The American Revolution  - OverSimplified (Part 1)
- `deep/compact/AAGIi62-sAU.txt` (33 min): Prohibition - OverSimplified
- `deep/compact/dHSQAEam2yc.txt` (6 min): WW1 - Oversimplified (Part 1)
- `deep/compact/8qRZcXIODNU.txt` (17 min): The French Revolution - OverSimplified (Part 1)
- `deep/compact/ewLpXw6uN28.txt` (26 min): Henry VIII - OverSimplified
- `deep/compact/Cqbleas1mmo.txt` (21 min): The Russian Revolution - OverSimplified (Part 1)
- `deep/compact/OIYy32RuHao.txt` (17 min): The Cold War - OverSimplified (Part 2)
- `deep/holdout/compact/26EivpCPHnQ.txt` (17 min): Three Kingdoms - OverSimplified
- `deep/holdout/compact/QLq6GEiHqR8.txt` (38 min): The Pig War - OverSimplified
