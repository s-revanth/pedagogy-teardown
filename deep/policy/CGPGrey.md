# CGPGrey: v2 rulebook (round 3)

This rulebook OVERRIDES `deep/reports/CGPGrey.md` wherever they conflict. Read the report for the channel's moves and voice, then apply these rules.
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
- **C1** (topic-conditional) Title carries the thesis: plain premise or question in 3 s, through-line analogy by ~0:20  _evidence: boezS4C_MFc 0:00-0:16; 7Pq-S557XQU 0:03_
- **C2** (missing-rule) Ladder of exemptions: surely-X-is-safe, broken with named instances and a number, title card each  _evidence: 7Pq-S557XQU 7:00, 9:03, 11:06_
- **C3** (missing-rule) Reverse the analogy when the viewer's intuition about the familiar case is right  _evidence: 7Pq-S557XQU 4:08-4:24_
- **C4** (missing-rule) Ambiguity shown as two parses, then a worst case that exploits it  _evidence: boezS4C_MFc 4:21, 8:26_
- **C5** (voice/craft) Beats ~21 s at 176-187 wpm with bracketed rapid-list asides  _evidence: boezS4C_MFc 6:47-7:33; 7Pq-S557XQU whole_

## D: corrections to the v1 report and storyboard
- **D1** DO NOT default to: Hook puts you in a situation or paradox. It failed on held-out videos: 7Pq-S557XQU 0:03 sweeping premise; boezS4C_MFc 0:00 plain question; no second-person setup
- **D2** CONDITIONAL, use only when the video clearly calls for it: Break belief: state the expected, let you commit, flip. Mixed evidence: 7Pq-S557XQU belief 0:20-0:56 broken 4:08 and per tier; boezS4C_MFc none staged; no commit in either
- **D3** DO NOT default to: Model: install 2-5 rules in under a minute. It failed on held-out videos: No rule list; paired coinage at 7Pq-S557XQU 0:20, dice gag at boezS4C_MFc 0:47
- **D4** DO NOT default to: Toy world: smallest staged case acted out. It failed on held-out videos: Absent in both; generator over-applied it
- **D5** DO NOT default to: Break and fence: fake ending, speculation fence. It failed on held-out videos: No fake ending; 7Pq-S557XQU asserts flatly at 6:04 and 12:33
- **D6** CONDITIONAL, use only when the video clearly calls for it: Callback with punchline and tease. Mixed evidence: boezS4C_MFc homework callback 9:35; 7Pq-S557XQU horse callback 13:07; no teaser

## N: numeric targets fitted on 125 training transcripts from this channel
Aim for the median, and stay inside the p25-p75 range. Use the duration-band row that matches the video.

| ID | measure | band | p25 | median | p75 | n |
|---|---|---|---|---|---|---|
| N1 | words per minute | under10min | 177 | 192 | 207 | 108 |
| N2 | words per minute | over10min | 142 | 169 | 186 | 17 |
| N3 | "you/your" per 100 words | all | 0.65 | 1.27 | 2.43 | 125 |
| N4 | "I/me/my" per 100 words | all | 0.00 | 0.27 | 1.52 | 125 |
| N5 | "we/us/let's" per 100 words | all | 0.13 | 0.34 | 0.57 | 125 |
| N6 | numbers per 100 words | all | 1.04 | 1.45 | 2.37 | 125 |
| N7 | question marks per 100 words | all | 0.23 | 0.41 | 0.73 | 110 |
| N8 | mean words per sentence | all | 13 | 17 | 20 | 110 |
| N9 | hedges (probably/maybe/roughly...) per 100 words | all | 0.13 | 0.24 | 0.43 | 125 |
| N10 | example cues (for example/imagine/let's say...) per 100 words | all | 0.00 | 0.00 | 0.10 | 125 |

## B: default switches (training base rates)
- **B1** a sponsor read: seen in 6% of training videos → default OFF.
- **B2** a teaser for a next video in the last 12%: seen in 3% of training videos → default OFF.
- **B3** a spoken roadmap in the first 12%: seen in 1% of training videos → default OFF.
- **B4** a spoken recap in the last 20%: seen in 2% of training videos → default OFF.
  - If there is a sponsor read, place it at about 87% of runtime (p25-p75 87-89%).

## E: exemplars (training transcripts you may read to copy rhythm and structure, not content)
Pick the 1-2 closest to the test video by format and duration, read them, and name them in your header.
- `deep/compact/iHzzSao6ypE.txt` (4 min): Why You Keep Just Missing the Green Light
- `deep/compact/qMkYlIA7mgw.txt` (4 min): The US-Canada Border Is 5,500 Miles of Pure Nonsense
- `deep/compact/oAHbLRjF0vo.txt` (8 min): The Fastest Way to Board a Plane Feels Like the Slowest
- `deep/compact/kF8I_r9XT7A.txt` (5 min): You Can Never Become Pope
- `deep/compact/wOmjnioNulo.txt` (6 min): The Secret Reason Horses Let Us Ride Them
- `deep/compact/rStL7niR7gs.txt` (18 min): Try to Rule Fairly and You'll Be Overthrown
- `deep/compact/rNu8XDBSn10.txt` (5 min): The UK Is a Country Made of Countries
- `deep/compact/uqH_Y1TupoQ.txt` (4 min): Watching This Video Disqualifies You From Jury Duty for Life
- `deep/compact/jNgP6d9HraI.txt` (8 min): The Royal Family Runs on Rules You've Never Heard Of
- `deep/compact/wfYbgdo8e-8.txt` (4 min): You Actually Share Your Brain With a Silent Stranger
- `deep/compact/thOifuHs6eY.txt` (9 min): Pentagons Are Terrible at One Thing
- `deep/compact/l4w6808wJcU.txt` (18 min): There's No Crying in Flag Design
- `deep/holdout/compact/7Pq-S557XQU.txt` (15 min): What Happened to Horses Is Happening to Us
- `deep/holdout/compact/boezS4C_MFc.txt` (10 min): America's Worst-Designed Backup Plan
