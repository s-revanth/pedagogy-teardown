# kurzgesagt: v2 rulebook (round 3)

This rulebook OVERRIDES `deep/reports/kurzgesagt.md` wherever they conflict. Read the report for the channel's moves and voice, then apply these rules.
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
- **C1** (topic-conditional) Topic and question-status switch: open question vs psychology change hook, analogy count, caveat type  _evidence: 1AElONvi9WQ 2:34; n3Xv_g3g-mA 0:00-1:23_
- **C2** (missing-rule) Advice mirrors the diagnosed loop, one question set per node, then a referral  _evidence: n3Xv_g3g-mA 7:02-9:52_
- **C3** (missing-rule) Ladder replay as test: reuse the setup's three rungs once later as evidence  _evidence: 1AElONvi9WQ 1:54, 6:11_
- **C4** (wrong-rule) Second-person self-audit contradicts 'no learner response'  _evidence: n3Xv_g3g-mA 8:27-9:52_
- **C5** (voice/craft) Pace ~146-156 wpm over speech, terse aphorism after each mechanism  _evidence: 1AElONvi9WQ 5:55; n3Xv_g3g-mA whole_

## D: corrections to the v1 report and storyboard
- **D1** CONDITIONAL, use only when the video clearly calls for it: Hook: paradox or what-if in one line. Mixed evidence: 1AElONvi9WQ 0:00 paradox as an assertion, no question; n3Xv_g3g-mA relatable list plus stats 0:00-0:34
- **D2** DO NOT default to: Scope: say what the video will and won't cover. It failed on held-out videos: No scope or roadmap beat in either video
- **D3** CONDITIONAL, use only when the video clearly calls for it: Stand-in: agent analogy or toy world. Mixed evidence: 1AElONvi9WQ four agent stand-ins; n3Xv_g3g-mA one analogy at 1:23, never reused
- **D4** CONDITIONAL, use only when the video clearly calls for it: Break it: misconception or trap. Mixed evidence: n3Xv_g3g-mA alone vs lonely at 0:34; 1AElONvi9WQ paradox named at 2:14
- **D5** CONDITIONAL, use only when the video clearly calls for it: Caveat that still commits to a direction. Mixed evidence: Caveats at 1AElONvi9WQ 3:50, 4:10, 6:29 but it refuses to commit; n3Xv_g3g-mA safety referral only 9:52
- **D6** CONDITIONAL, use only when the video clearly calls for it: Callback cashes in the hook. Mixed evidence: Closing-phrase mirror, not a return to the question: 1AElONvi9WQ 6:46; n3Xv_g3g-mA 10:28

## N: numeric targets fitted on 239 training transcripts from this channel
Aim for the median, and stay inside the p25-p75 range. Use the duration-band row that matches the video.

| ID | measure | band | p25 | median | p75 | n |
|---|---|---|---|---|---|---|
| N1 | words per minute | under10min | 150 | 156 | 163 | 129 |
| N2 | words per minute | over10min | 151 | 159 | 165 | 110 |
| N3 | "you/your" per 100 words | all | 0.48 | 0.99 | 1.96 | 239 |
| N4 | "I/me/my" per 100 words | all | 0.00 | 0.00 | 0.00 | 239 |
| N5 | "we/us/let's" per 100 words | all | 1.08 | 1.78 | 2.69 | 239 |
| N6 | numbers per 100 words | all | 1.16 | 1.72 | 2.59 | 239 |
| N7 | question marks per 100 words | all | 0.17 | 0.31 | 0.50 | 205 |
| N8 | mean words per sentence | all | 15 | 16 | 17 | 205 |
| N9 | hedges (probably/maybe/roughly...) per 100 words | all | 0.17 | 0.33 | 0.56 | 239 |
| N10 | example cues (for example/imagine/let's say...) per 100 words | all | 0.00 | 0.06 | 0.15 | 239 |

## B: default switches (training base rates)
- **B1** a sponsor read: seen in 36% of training videos → CONDITIONAL: include only if the video type clearly calls for it.
- **B2** a teaser for a next video in the last 12%: seen in 2% of training videos → default OFF.
- **B3** a spoken roadmap in the first 12%: seen in 10% of training videos → default OFF.
- **B4** a spoken recap in the last 20%: seen in 1% of training videos → default OFF.
  - If there is a sponsor read, place it at about 87% of runtime (p25-p75 82-94%).

## E: exemplars (training transcripts you may read to copy rhythm and structure, not content)
Pick the 1-2 closest to the test video by format and duration, read them, and name them in your header.
- `deep/compact/BtN-goy9VOY.txt` (8 min): The Coronavirus Explained & What You Should Do
- `deep/compact/zQGOcOUBi6s.txt` (7 min): The Immune System Explained I – Bacteria Infection
- `deep/compact/h6fcK_fRYaI.txt` (8 min): The Egg - A Short Story
- `deep/compact/9tbxDgcv74c.txt` (6 min): What If You Detonated a Nuclear Bomb In The Marianas Trench? (Science not Fantasy)
- `deep/compact/sNhhvQGsMEc.txt` (6 min): The Fermi Paradox — Where Are All The Aliens? (1/2)
- `deep/compact/YI3tsmFsrOg.txt` (7 min): The Deadliest Being on Planet Earth – The Bacteriophage
- `deep/compact/3mnSDifDSxQ.txt` (11 min): The Largest Star in the Universe – Size Comparison
- `deep/compact/yWO-cvGETRQ.txt` (10 min): Why Black Holes Could Delete The Universe – The Information Paradox
- `deep/compact/JyECrGp-Sw8.txt` (7 min): What If We Detonated All Nuclear Bombs at Once?
- `deep/compact/0FH9cgRhQ-k.txt` (13 min): The Largest Black Hole in the Universe - Size Comparison
- `deep/compact/jAhjPd4uNFY.txt` (16 min): Genetic Engineering Will Change Everything Forever – CRISPR
- `deep/compact/ulCdoCfw-bY.txt` (8 min): The Black Hole Bomb and Black Hole Civilizations
- `deep/holdout/compact/1AElONvi9WQ.txt` (7 min): Why Blue Whales Don't Get Cancer - Peto's Paradox
- `deep/holdout/compact/n3Xv_g3g-mA.txt` (13 min): Loneliness
