# Vsauce: v2 rulebook (round 3)

This rulebook OVERRIDES `deep/reports/Vsauce.md` wherever they conflict. Read the report for the channel's moves and voice, then apply these rules.
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
- **C1** (wrong-rule) Answer first, then an exception within 20 s  _evidence: JTvcpdfGUtQ 0:18-0:34; fCn8zs912OE 0:39_
- **C2** (missing-rule) Late pivot of the title idea to the human condition, ending on a quote  _evidence: JTvcpdfGUtQ 8:53-12:57; fCn8zs912OE 18:20-20:04_
- **C3** (wrong-rule) Sanctioned 2-3 min detour (up to ~20%) joined by one pivot sentence  _evidence: JTvcpdfGUtQ 3:26-6:22; fCn8zs912OE 4:18-6:43_
- **C4** (underspecified) Barrage repetition: 8-14 one-clause instances in under 70 s  _evidence: fCn8zs912OE 3:08-3:42_
- **C5** (voice/craft) Measured pace 134-148 wpm on full runtime, not ~170  _evidence: JTvcpdfGUtQ 148; fCn8zs912OE 134 (139 over speech span)_

## D: corrections to the v1 report and storyboard
- **D1** DO NOT default to: Odd hook: a trick or joke, fake version first. It failed on held-out videos: JTvcpdfGUtQ 0:01 phobia statement; fCn8zs912OE 0:00 quantified trivia fact
- **D2** CONDITIONAL, use only when the video clearly calls for it: Obvious answer stated so it can be broken. Mixed evidence: JTvcpdfGUtQ gives the real answer at 0:18, then the exception at 0:34; no planted belief in fCn8zs912OE
- **D3** CONDITIONAL, use only when the video clearly calls for it: Prop or simulation carries the idea. Mixed evidence: fCn8zs912OE monkey derivation 8:07, paper clips 13:34; JTvcpdfGUtQ scissors 6:07
- **D4** DO NOT default to: Name it late, after the idea is felt. It failed on held-out videos: Zipf's law named at fCn8zs912OE 1:16; umbra and penumbra at JTvcpdfGUtQ 2:52
- **D5** CONDITIONAL, use only when the video clearly calls for it: Callback reframes the hook, then plug. Mixed evidence: JTvcpdfGUtQ valence flip of the dark at 12:57; fCn8zs912OE ends on a quote at 20:04, no callback

## N: numeric targets fitted on 322 training transcripts from this channel
Aim for the median, and stay inside the p25-p75 range. Use the duration-band row that matches the video.

| ID | measure | band | p25 | median | p75 | n |
|---|---|---|---|---|---|---|
| N1 | words per minute | under10min | 136 | 149 | 166 | 234 |
| N2 | words per minute | over10min | 133 | 138 | 149 | 88 |
| N3 | "you/your" per 100 words | all | 1.59 | 2.62 | 3.62 | 322 |
| N4 | "I/me/my" per 100 words | all | 0.58 | 1.19 | 2.40 | 322 |
| N5 | "we/us/let's" per 100 words | all | 0.61 | 1.10 | 1.79 | 322 |
| N6 | numbers per 100 words | all | 0.87 | 1.32 | 2.17 | 322 |
| N7 | question marks per 100 words | all | 0.38 | 0.57 | 0.86 | 202 |
| N8 | mean words per sentence | all | 12 | 14 | 16 | 202 |
| N9 | hedges (probably/maybe/roughly...) per 100 words | all | 0.00 | 0.19 | 0.33 | 322 |
| N10 | example cues (for example/imagine/let's say...) per 100 words | all | 0.00 | 0.03 | 0.18 | 322 |

## B: default switches (training base rates)
- **B1** a sponsor read: seen in 5% of training videos → default OFF.
- **B2** a teaser for a next video in the last 12%: seen in 3% of training videos → default OFF.
- **B3** a spoken roadmap in the first 12%: seen in 16% of training videos → default OFF.
- **B4** a spoken recap in the last 20%: seen in 0% of training videos → default OFF.
  - If there is a sponsor read, place it at about 70% of runtime (p25-p75 42-78%).

## E: exemplars (training transcripts you may read to copy rhythm and structure, not content)
Pick the 1-2 closest to the test video by format and duration, read them, and name them in your header.
- `deep/compact/QDCcuCHOIyY.txt` (28 min): The Power of Suggestion
- `deep/compact/s86-Z-CbaHA.txt` (24 min): The Banach–Tarski Paradox
- `deep/compact/jHbyQ_AQP8c.txt` (7 min): What If Everyone JUMPED At Once?
- `deep/compact/VNqNnUJVcVs.txt` (10 min): Is Earth Actually Flat?
- `deep/compact/7uiv6tKtoKg.txt` (9 min): What Will We Miss?
- `deep/compact/iqKdEhx-dD4.txt` (34 min): Isolation - Mind Field (Ep 1)
- `deep/compact/evQsOFQju08.txt` (9 min): Is Your Red The Same as My Red?
- `deep/compact/3pAnRKD4raY.txt` (10 min): Travel INSIDE a Black Hole
- `deep/compact/sHCHEykUxP4.txt` (14 min): Spooky Coincidences?
- `deep/compact/IJhgZBn-LHg.txt` (21 min): How Earth Moves
- `deep/compact/Xc4xYacTu-E.txt` (26 min): Which Way Is Down?
- `deep/compact/ixQbCXLUUj8.txt` (12 min): Why Do We Kiss?
- `deep/holdout/compact/JTvcpdfGUtQ.txt` (13 min): What Is The Speed of Dark?
- `deep/holdout/compact/fCn8zs912OE.txt` (21 min): The Zipf Mystery
