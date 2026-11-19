# Gap analysis: 3Blue1Brown, "Why is pi here? And why is it squared? A geometric answer to the Basel problem" (d-o3eB9sfls, 1028 s)

Recall caveat: the generator had a faint recall of "light". Credit for the lamp/brightness/inverse-square idea is discounted. It was a choice the report alone could not have forced. The generator's own rationale (toy-world, Home-first) is plausible but not unique. Hits below are marked where they depend on that. Real transcript is manual-caption; about 3,030 words, roughly 177 wpm over the 1,028 s runtime. The predicted narration is 2,465 words, about 144 wpm over the same runtime, so it is under-filled by about 19%.

## 1. Real beat sheet (compact)

| m:ss | Lvl | Tags | Paraphrase |
|---|---|---|---|
| 0:00 | H | hook-question, story | Pose the sum of reciprocal squares, ask what it approaches; note it stood unsolved about 90 years |
| 0:19 | N | hook-paradox | Euler's answer is pi squared over six; "isn't that crazy", why pi, why squared |
| 0:36 | B | roadmap, misconception-first (partial) | Names it the Basel problem; this proof differs from Euler's; restates that pi implies a circle somewhere and rebuts the "pi isn't about circles" stance |
| 1:08 | B | roadmap, honest-caveat | Whatever your view, some path back to circles exists; the only question is how long; here it is short and "starts with light" |
| 1:24 | H | toy-world, analogy | Lighthouses on every positive integer; the first has apparent brightness 1 |
| 1:56 | N | claim-before-derivation, commit-to-answer | 2nd and 3rd have 1/4 and 1/9 ("reasons shortly"); total brightness is the Basel sum; restate target as pi²/6 times the first |
| 2:28 | B | design-it-yourself, honest-caveat | This looks useless (same question), but it raises a new one: can lighthouses be rearranged, same total, into an easier setup? |
| 3:03 | N | minimal-definition | Define apparent brightness by a screen, angle, solid angle |
| 3:38 | N | analogy, act-it-out | Inverse-square law via screens at distance 1, 2, 3: 4 and 9 copies of the screen |
| 4:41 | B | generalize-to-other-domains, recap | Same law for sound, heat, radio; restate that the lighthouse row implements Basel |
| 5:13 | N | special-case-first | Key building block: turn one lighthouse into two (observer, lighthouse, perpendicular line, points A and B on axes) |
| 5:45 | N | commit-to-answer | Claim: brightness of the one equals the sum of the two ("you'll see why in a minute"); all bulbs identical |
| 6:17 | I | notation | 1/a² + 1/b² = 1/h², the inverse Pythagorean theorem; nod to another channel (6:33) |
| 6:49 | N | build-and-verify, simulation-as-argument | Prove it via a shrunken triangle as a screen and similar triangles; offered as the briefly outlined alternative to an area proof; GeoGebra link |
| 8:11 | N | honest-caveat | Similar-triangle argument holds only for a tiny screen |
| 8:28 | B | roadmap, humor | "Buckle up": the lemma lets one lighthouse become two; now build the infinite array |
| 8:46 | H | toy-world, special-case-first | Lake with circumference 2, observer on the shore, lighthouse opposite; brightness = pi²/4 (pi enters here) |
| 9:18 | N | visible-repetition (1) | Double the circle, tangent line, 1 lighthouse becomes 2; Thales right-angle fact |
| 10:07 | N | visible-repetition (2) | Circumference 8, 2 become 4, spacing 1,2,2,2,1 |
| 11:35 | N | visible-repetition (3) | "One more step": circumference 16, 8 lighthouses |
| 12:26 | N | build-and-verify | Prove even spacing via the inscribed-angle theorem (45 degrees) |
| 13:16 | N | simulation-as-argument, generalize | Imagine the doubling continuing; limit is a line of lighthouses spaced 2, brightness stays pi²/4 |
| 14:07 | N | payoff | Sum of 1/n² over odd integers, positive and negative, equals pi²/4 ("the core") |
| 14:24 | H | callback-to-hook, awe | Step back: fractions with no apparent geometry now visibly are geometry; number line as limit of ever larger circles |
| 15:14 | B | second-person-role (voiced objection) | "But wait, that's not the promised sum" |
| 15:14 | N | special-case-first | Positive odd only gives pi²/8 |
| 15:32 | N | recap-lite | Even terms are a copy of the full sum scaled by 1/4 |
| 16:05 | N | notation-compaction, humor | Odds are 3/4 of total, so multiply pi²/8 by 4/3 to get pi²/6; one joking sign-off |
| 16:35 | N/A | admin | Credit to the team member who wrote and animated it; Patreon thanks |

## 2. Prediction scorecard (script section 5)

| # | Prediction | Predicted | Actual | Verdict |
|---|---|---|---|---|
| 1 | First question to viewer | ~0:35-0:50 (why pi, why squared); second at ~3:00 | 0:00 (what does the sum approach), 0:25 (why pi, why squared); redesign question 2:43 | near (earlier; the 3:00 second question is a hit) |
| 2 | First notation/formula | 13:00-14:00 sigma, ~80% in (fallback "0:00 as object") | Series spoken from 0:00; first new formula 6:17 (~37%), inverse Pythagorean lemma; sigma never narrated | miss on time; fallback partial |
| 3 | Misconception | yes, soft: fractions unrelated to circles; Euler's algebra is "the" story | Yes, soft: the "pi isn't about circles" stance (0:52); "nothing to do with circles" (14:40). The Euler-proof half is not used | hit |
| 4 | Brute-force first | yes, 1:30-3:00 numerics (10, 100, 1000 terms) | No numeric partial sums anywhere | miss |
| 5 | Examples | ~3 numeric runs, then one running lamp object growing 1 -> few -> both sides -> odd -> circle; 3-4 observer positions | One running object (lighthouses) is right. No numeric runs. Growth is a doubling ladder 1 -> 2 -> 4 -> 8 -> infinity on circles of size 2, 4, 8, 16 plus screens at 1, 2, 3. One fixed observer | near |
| 6 | Hook type | paradox plus direct question | Question, then paradox with a short history | hit |
| 7 | Ending | callback + caveat about skipped step + teaser/hand-off | Closes on the algebra result, a joke, credits; no callback, caveat or teaser | miss |
| 8a | honest-caveat | present | 8:11 (tiny-screen limit), 0:52 | hit (small, technical) |
| 8b | roadmap | present, 0:50 | Only "it all starts with light" (1:24) and "buckle up" (8:28) | near |
| 8c | special-case-first | present | Lake of circumference 2 (8:46); positive-only/odd-only (15:14) | hit |
| 8d | notation-after-concept | present | Lemma formula follows its picture (6:17) | hit |
| 8e | callback-to-hook | present, at the end | Mid-video at 14:24, not at the end | near |
| 9a | tier-2 brute-force-first | -- | absent | miss |
| 9b | tier-2 design-it-yourself | -- | one question at 2:43; the rest presenter-driven | near |
| 9c | tier-2 generalize-to-other-domains | -- | 4:41 sound/heat/radio; 14:40 line as limit of circles | hit |
| 9d | tier-2 teaser-next | -- | absent | miss |
| 9e | tier-2 build-and-verify | -- | present as proofs of the lemma and spacing (6:49, 12:26); no numeric check | near |

Hit rate: 6 hit, 6 near, 5 miss of 17. Strict 35%; half-credit for near 53%. Core 8 items (rows 1-8, one row per move) are 5 hit, 4 near, 3 miss of 12 (42% strict, 58% weighted). Removing the "light" idea changes nothing in this scoring because no scored prediction was about the lamp.

## 3. Structural alignment

Predicted arc: hook-paradox -> roadmap/caveat -> numeric brute force -> wall -> analogy (1/d² light) -> toy lamp world -> definition -> rearrangements -> named stepping stone -> observer slide -> bend line into circle -> claim in words -> sigma -> numeric check -> odd/even algebra -> callback -> teaser.
Real arc: hook -> framing aside -> physical toy world immediately -> claim and target -> "same question" mini-wall -> brightness/inverse-square -> lemma (claim, formula, proof, caveat) -> "buckle up" -> circle construction repeated 3 times -> limit -> core payoff -> awe/callback -> voiced objection -> odd/even algebra -> credits.

- Predicted and present: hook; light toy world (recall-discounted); inverse-square explanation; special case before general; generalisation of the law; odd/even algebra with the 3/4 and 4/3 step (the generator got this right from subject knowledge, not from the report); two-stage payoff (circle result, then algebra cleanup).
- Predicted but absent (false positives): numeric partial sums and slow-convergence beat; explicit "wall" beat; "where does 1/d² appear" question; odd/even/all layouts compared; named "almost-Basel"; observer slide and periodic brightness function; bending the line into a circle (the real video runs the opposite direction, circles growing into a line); sigma notation read as procedure; numeric check; end callback; teaser; "not a full proof" caveat framing.
- Present but unpredicted (false negatives): 48 s philosophical frame about pi and circles (0:36-1:24); target stated as a brightness claim at 2:12; screen and solid-angle definition (3:03); the whole lemma block (5:13-8:28) with claim-then-proof, an optional second proof, a link, and a cross-channel nod; "buckle up" signpost; lake special case with circumference 2 giving pi²/4 (8:46); three-times doubling with explicit "one more step", then a spacing proof; the imagine-it-forever limit; an awe beat; the voiced "but wait" objection; a joke sign-off; team-member credit.

Timing drift:
- Hook: predicted 0:00-0:50, actual 0:00-0:36 (hit; the real hook is 14 s shorter and carries a history line, not a numeric crawl).
- First new idea (light): predicted 3:40 analogy and 5:00 toy world; actual 1:24. Early by 2:16 and 3:36, because brute force and wall were not spent first.
- Pi arrives via a circle: predicted 11:30; actual 8:46-9:18 (early by about 2:20).
- Core payoff: predicted 14:40 check; actual 14:07 (about 0:30 early). Final pi²/6: predicted 15:30; actual 16:05-16:35 (0:35-1:05 late).
- Ending: predicted epilogue 16:10-17:08 (about 1:00 callback, caveat, teaser); actual ends about 0:30 after the result, with credits.

## 4. Gap taxonomy

| Miss | Class | Why |
|---|---|---|
| No brute-force numerics, no wall before the toy world | topic-conditional | The hook gave away the answer at 0:19, so numeric crawling adds nothing and the video starts building immediately. The report's arc was learned from videos where the answer was withheld or the object admits naive computation; it states no trigger. Part is generator-error: the report's arc puts toy-world before brute force, and the script reversed them. |
| Notation timing (6:17 vs predicted ~13:30) | underspecified | Report says notation is "held back" but gives no rule; the generator interpolated 80% in from two videos. Real first formula is a lemma at about 37%, and the central sum is never given sigma form. |
| Ending (callback + teaser + caveat vs result + credits) | topic-conditional | Standalone result video, written by a team member (credit at 16:35). Report has no condition for authorship or for self-contained results. |
| Lemma block: claim now, justify in 60-100 s, plus an optional second proof | missing-rule | Closest report item is "claim in words before a long derivation"; it gives no per-lemma schedule. Claims at 1:56 and 5:45 are paid at 3:38 and 6:49. |
| Triple repetition then "imagine it continuing" | underspecified | visible-repetition exists (7/12) but says nothing on count, labelling the last step, or the jump to a limit. |
| Voiced objection and awe beat before final algebra (14:24, 15:14) | missing-rule | The report has no move for the presenter voicing the viewer's objection or for a post-payoff awe pause. |
| Philosophical frame (0:36-1:24) | missing-rule | No rule for pre-empting a commenter debate before the first object. |
| Predicted "bend line into circle" vs real "circles grow into line" | generator-error | Mechanism is content knowledge. Not counted against the report. |
| Predicted "tour not a proof" caveat; real is full proof with one technical caveat | wrong-rule (soft) | Report's honest-caveat is front-loaded as a framing ("hope", "not exactly how it works"); here the caveat is a single precision limit mid-lemma (8:11). |
| Sparse "design-it-yourself", no named stepping stone | wrong-rule (soft) | Presenter drives ("no small amount of cleverness"); only one invention question (2:43). The report's "viewer as inventor" is overgeneralised for proof-tour videos. |
| Voice: "buckle up", joking sign-off ("badda boom badda bing"), shout-out, exclamatory "isn't that crazy" | voice/craft | Informal register, not captured. |
| Words and pace (177 vs 144 wpm) | voice/craft | Real script is denser and more procedural; the generator added reflective commentary ("notice what I did not do") the real video does not have. |

## 5. Overfit check

- "Notation is held back, first symbol around two-thirds to four-fifths in" (Fourier, NN ch.1 data): fails here. First formula at 37%, and it is a lemma.
- "Roadmap with an honest caveat at the front" (12/12 caveat, 11/12 roadmap): front has no real caveat and only a thin pointer; the one caveat is technical and mid-lemma.
- "Brute-force or naive attempt then a wall" in the arc: absent. Brute-force is 6/12 at best; the arc presents it as the default.
- "Callback and teaser" close (9/12 each): not here.
- Hope-before-mechanism and undercut-your-own-story: absent; the story gets no failure.
- "Viewer as inventor" headline: weak. Presenter-led throughout.
- Named stepping stone ("almost X"): absent by name. The odd-integers-both-sides sum is a real stepping stone but is unnamed, and the diff is delivered as "that's not the sum I promised" plus algebra.

## 6. Proposed rule changes

1. **Result-given proofs skip numerics and the wall (topic-conditional; likely universal).** Trigger: the hook states the final value. Action: no partial-sum crawl and no explicit wall; put the first concrete physical object on screen by about 1:30 (here 1:24) and restate the target as a claim about that object within another 40 s (2:12). Evidence: 0:19, 1:24, 2:12. When the answer is withheld (Fourier transform 3:04, Bitcoin 2:36), keep brute-force-first.
2. **Claim, then justify within 60-100 s, with one optional alternative (likely universal).** Trigger: any building-block lemma. Action: assert it with "you'll see why shortly", give its formula once, prove it in 60-100 s, add one caveat on its domain, and offer one other proof in under a minute with a link. Evidence: 1:56 -> 3:38; 5:45 -> 6:17 -> 6:49; caveat 8:11; link 8:11.
3. **Iterate a construction exactly three times, then jump to the limit (likely universal).** Trigger: recursive or doubling constructions. Action: step one about 50 s, step two about 90 s, step three about 50 s labelled "just one more step", one proof of the invariant (about 50 s), then "imagine it playing on" and state the limit in under 40 s. Evidence: 9:18, 10:07, 11:35, 12:26, 13:16.
4. **Two-stage payoff with a voiced objection (likely universal).** Trigger: the elegant result is not literally the quantity promised. Action: celebrate the result with a 30-45 s awe beat that restates the hook's "nothing to do with geometry" (14:24-14:57), then voice the viewer's objection ("but wait") and close with 60-80 s of mechanical algebra (15:14-16:35). End within about 30 s of the last result.
5. **Ending conditional on standalone result and author (channel-specific).** Trigger: self-contained proof or result video, or a non-lead author. Action: no recap, callback or teaser at the end; one joke, then credits. Keep the callback-to-hook at the first payoff (14:24). Keep callback and teaser for series installments. Evidence: 14:24, 16:35.
6. **Notation: formula after the picture that demands it, sums stay verbal (channel-specific).** Replace "first symbol at about 64-80%" with: introduce a formula only for a lemma, within about 60 s after its picture is complete; narrate series in words and animation without sigma. Evidence: 6:17 (about 37%), series spoken at 14:07.

## 7. Scores (1-5)

- Arc fidelity: **2**. Hook, light toy world, odd/even close are right, but brute force, wall, notation, circle mechanism and ending are wrong.
- Move-inventory recall: **3**. Roughly 3 of 5 headline moves appear; the lemma, three-step repetition, objection and awe beat are missing.
- Move precision: **2**. Many predicted beats (numeric runs, wall, observer slide, sigma, numeric check, teaser) never occur.
- Pacing/timing: **2**. First idea about 2-3.5 minutes late, notation about 7 minutes late, epilogue about 1 minute too long, narration 19% under-filled.
- Voice: **3**. The "I want to show you" register is right, but the script is reflective where the real video is procedural.
- Overall "could the hypothesis regenerate this video": **2**. The hypothesis yields a plausible video, not this one, mainly because it assumes a withheld answer and an inventor-led arc.
