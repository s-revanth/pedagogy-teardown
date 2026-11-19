# Sebastian Lague: how he teaches (12 videos)

Data note: tracker.csv marks three analyses "pending" (QZwneRb-zqA, UXD97l7ZT0w, PGk0rnyTa1U), but all 12 json and md files exist and parse. All 12 are used. Captions are manual throughout. Move counts below come from a script over the beat tags; principle counts from the verdict prefix of each analysis.

## 1. Bottom line
Lague teaches by build-break-fix in public. Each concept enters as the smallest repair for a failure the viewer watched one beat earlier, so the vocabulary (clock, bias, pruning, hash grid) feels necessary before it is named. Correctness is made visible by re-running the same test on every variant, by timing before and after, and by sliders and toggles, not by argument. The tone is a plain-spoken devlog with unusual honesty: he shows the bug, the cheat, the skipped hard part, and the thing he does not understand. The cost is that the "lesson" is often a side effect of a project, and the weaker videos (geography, vacuum, console) barely teach at all.

## 2. Signature arc
1. Roadmap and tiny toy world (first minute). One circle (fluids 0:01), one bunny (ecosystem 0:15), board and FEN (chess 0:01-1:44), lamp and switch (computers 0:38), an empty grid (A* 0:21), a one-bit circuit (memory 0:35).
2. Dumb version first, run it. Naive all-pairs loops (fluids 1:33), play-every-move-then-filter (chess 6:23), 35+7 added by hand in binary (computers 6:17), nudge each weight (neural net 14:54).
3. It fails visibly. Particles collapse (fluids 2:10), density explodes with radius (5:40), runaway overwrite in the ALU loop (memory 5:46-11:13), only-rotating boundary (neural net 5:25), cable looks bad with FABRIK (vacuum 4:14).
4. Name the minimal concept, notation only now. Kernel graph (fluids 4:13), bias and activation (neural net 5:48, 9:46), clock (memory 11:13), FEN (chess 1:44). The big equation comes after the code works (fluids 11:07; Navier-Stokes 33:50).
5. Verify immediately, with a repeatable test. Same input sweep on each circuit (memory, computers), perft depths and timings (chess 15:45-16:16), uniform-grid check with constant 187 (fluids 6:13).
6. Next failure triggers the next concept. Loop steps 3-5 four to ten times (memory about six circuits; chess pruning, quiescence, hashing, deepening).
7. Honest close. Admits limits, lists a wishlist, teases the next episode or calls back to the opening (memory 16:40-18:35, fluids 46:31, chess 28:15). Rarely recaps lessons.

Videos that follow it closely: memory, chess, fluids, neural net, computers, ecosystem (a compressed form), A* (a variant: three reruns with scaffolding removed). Videos that are plain devlogs and only fragments of it: geography x3, vacuum, console.

## 3. Move frequency (n/12 videos with at least one beat tagged)
| Move | n/12 | Best example |
|---|---|---|
| toy-world | 12 | Fluids 0:01: one circle under gravity |
| build-and-verify | 11 | Chess 15:45: timed run before and after each optimisation |
| visible-repetition | 11 | Computers 7:56: same all-off/one-on sweep on each circuit |
| failure-shown | 11 | Memory 5:46: unclocked store fails, motivating the clock |
| honest-caveat | 10 | Memory 4:19: admits he only roughly understands |
| simulation-as-argument | 10 | Fluids 29:41: parameter grid of sims side by side |
| design-it-yourself | 10 | Neural net 3:40: hand-tune sliders, ask what knob is missing |
| roadmap | 9 | Fluids 8:04: liquids need a gradient, so build one |
| humor | 9 | Ecosystem 1:03: "avert your eyes" |
| notation-after-concept | 9 | Fluids 11:07: core SPH equation shown after the code runs |
| minimal-definition-then-refine | 8 | Computers 0:55 |
| callback-to-hook | 8 | Memory 16:40: rebuilt runaway ALU now works |
| generalize-to-other-domains | 8 | Vacuum 7:30: same Point/Stick for rope, cable, cloth |
| analogy | 7 | Chess 14:29: garden shears for pruning |
| learner-discovers (staged) | 7 | Computers 12:22: solve "what adds to give zero" for two's complement |
| brute-force-first | 7 | Neural net 20:24: nudge every weight before backprop |
| special-case-first | 7 | A* 2:50: empty grid first |
| recap, teaser-next | 7 each | Neural net 51:54: colour images fail, convolution next |
| story | 7 | Vacuum 0:01 |
| commit-to-answer | 4 | A* 5:27 (weak, rhetorical) |
| misconception-first | 4 | Chess 26:11: his own horror at repeated searches |
| presenter-was-wrong | 2 | Fluids 15:02: forgot to cache density |
| hook-question | 4 | Computers 0:03 |
| act-it-out | 4 | Fluids 41:41: bitonic sort pair by pair |

Hook-paradox appears once (memory 0:35). Hooks are mostly a project statement, not a question.

## 4. Principle scorecard (confirmed / partly / contradicted / not observed)
| # | Principle | Tally | Verdict and evidence |
|---|---|---|---|
| 1 | Start from the familiar | 8 / 4 / 0 / 0 | Confirmed. Lamp and switch (computers 0:38), one circle, one bunny. "Partly" in the geography and vacuum devlogs, which assume graphics literacy. |
| 2 | Every symbol costs effort | 7 / 5 / 0 / 0 | Confirmed. Weight, bias named only after failures (neural net 5:48); G/H/F one at a time (A* 1:12-2:11). |
| 3 | Habit makes interfaces comfortable | 1 / 5 / 0 / 6 | Weak. The recurring sim window and sliders (fluids) and constant corner numbers (A* 6:01) act as habit, but never taught deliberately. |
| 4 | Analogy first, then rigor | 2 / 6 / 2 / 2 | Mostly contradicted as a rule. Lague goes physical or concrete, not analogical; analogies are brief (shears, finger-as-switch 2:03). |
| 5 | Act out the problem literally | 9 / 3 / 0 / 0 | Confirmed. The particles are the fluid; he drags the chain, flies the plane, plays the engine (chess 21:42). |
| 6 | Dumb way first, neat scratch pad | 8 / 2 / 0 / 2 | Confirmed, the strongest fit. Said out loud: "a little gross" (chess 6:23). |
| 7 | Learner discovers via repetition | 7 / 5 / 0 / 0 | Confirmed in form: the failure runs before the explanation. Still staged: he asks and answers. |
| 8 | Pace by novelty | 0 / 8 / 1 / 3 | Partly. Transcripts show steady speech; idea rate drops through testing and retesting (memory 13:28-14:02) and rises through code he calls boring. Cannot test wpm here. |
| 9 | Repeat across examples | 9 / 2 / 0 / 1 | Confirmed. Same test sweep, same Point/Stick, same loop (try, observe, patch, rerun). |
| 10 | Tiny to bigger | 10 / 1 / 0 / 1 | Confirmed. 1 particle to 40k to 3D; 1 bit to 4 bits to ALU. |
| 11 | Dependency order | 9 / 3 / 0 / 0 | Confirmed, but the order is dictated by failure, not by a textbook. Stepping stones invented freely (meaningless function, fluids 8:42). |
| 12 | Connect to outside sources | 7 / 4 / 0 / 1 | Confirmed. Papers, Stockfish as oracle, Ben Eater, real NAND chips, cyclone direction by hemisphere. |
| 13 | Simple for 12-year-old, expert depth, say why each tool | 0 / 11 / 1 / 0 | Partly. Plain words, expert content, reasons given in the build series; maths in the geography devlog is one sentence (0:49 of the polish video). |

## 5. New theories
1. **Failure-gated vocabulary.** A new term is learned faster and held better if the learner has just watched the specific failure it repairs. Evidence: memory (clock at 11:13, mux at 15:09), neural net (bias 5:48, activation 9:46, minibatch 21:57), chess (pruning, quiescence 17:38-20:07). Falsifiable: if a term is taught after a one-minute-earlier shown failure vs. before it, learners will recall its purpose more often and need fewer re-explanations on a transfer item.
2. **The equation is a label for something already working.** Show the code or behaviour first, then reveal the formula and check it with a special case. Evidence: fluids 11:07-11:57 (substitute density for A and it collapses to the earlier formula), neural net 15:31 and 26:15 (nudge, then derive and confirm they match), computers 7:56 (table first, chip named after). Falsifiable: if the formula is revealed after the learner has produced its behaviour, then symbol-to-meaning errors drop versus formula-first.
3. **Fixed test choreography as a trust device.** Re-running the identical input sequence on every variant lets viewers diff outputs without being told what to look for. Evidence: memory (same pattern on each circuit), computers (all-off, one-on, two-on sweep), chess (perft depths and timed positions 15:45), A* (three reruns, 6:01). Falsifiable: learners who see the same sequence across variants will spot a regression faster than those who see varied tests.
4. **Honesty as pacing.** Saying "I do not understand this part" or "this is gross" at a hard step buys attention and lowers the bar to follow, without slowing speech. Evidence: memory 4:19 and 15:09, fluids 2:29 and 8:42, vacuum 8:39, geography 8:20. Falsifiable: a tutor that flags its own uncertainty at the hardest beat will keep more novice learners through that beat than one that does not, if the following step is then clearly resolved.
5. **Scaffolding removal across reruns.** Show the same scene again with a previously visible number hidden or swapped, forcing use of the model just built. Evidence: A* 6:01 (G and H hidden, arrows shown), computers (chips sealed into named packages at 4:06, 10:39, 17:47), vacuum 5:18-7:49 (one primitive reused). Falsifiable: if the third pass hides the labels, learners predict the next selection more accurately than when labels stay.
6. **One knob, one cause.** A slider or toggle attributes each visual effect to a single parameter. Evidence: fluids 29:41 and 35:53 parameter grids, geography 28:16 ablation by toggle, polish video 14:17-14:49 sweeps, neural net 5:25 hand-dragged boundary. Falsifiable: if a concept is shown with one adjustable parameter, then learners can state its effect and predict an unseen setting.

## 6. What he does badly or never does
- Almost never asks the viewer a real question: first question to the viewer is "none" in 9 of 12 videos; commit-to-answer is rhetorical.
- No misconception planting from outside: his misconceptions are his own horror (chess 26:11) or sign-bit mistake (computers 12:02).
- No deliberate analogy ladder; only 2 of 12 confirm principle 4.
- Skips and omits: geography and vacuum videos define the cross product in a sentence and show code without walking it; weak for beginners.
- Few recaps of lessons (endings are wishlists and teasers), little spaced repetition of the key term, and no practice or learner turn at all.
- Four of the 12 are not explainers (geography x3, console) and their theories are "devlog, not lesson".

## 7. Velocity translation
- **Scene builder:** a "break first" mode where the failing state is a first-class scene and is kept for later before/after comparison; "package as chip" so solved sub-scenes become one labelled block; one slider per concept with parameter-grid and layer-peeling modes; rule-stacking sims with a toggle per rule.
- **Voice and beat script:** name terms after the demo, never before; tutor may say "I am not sure why, but" or "should have done this first" at one labelled hard beat; call a result a hypothesis after the curve appears.
- **Orchestrator rules:** next concept is whichever flaw is currently visible, not textbook order; allow a capped stepping-stone detour on a meaningless toy function with a callback; hold pseudocode and formulas until the learner has seen or produced the behaviour; add an external sanity-check beat after each build.
- **Playbooks:** build-break-fix chain; oracle comparison for advanced learners (diff against a trusted system); scaffold-removal reruns; nudge-then-derive for calculus.
- **Learner model:** log which chips or components the learner has already built so later scenes can say "use the XOR you made"; insert a calculus refresher only when slope intuition is weak.
- **Ghost hands:** replay the same canonical input sequence on every variant; highlight the next candidate (lowest F node) so the learner predicts; sweep sliders while the voice names the effect.
- **Evals:** every new term must follow a shown failure within about a minute; every optimisation claim has a before/after number or visual; every code line or formula has a prior visual referent; count presenter-error and honest-caveat tags.

## 8. Per-video one-liners
| Title | id | Theory |
|---|---|---|
| How Do Computers Remember? | I0-izyq6q5s | Each component is the smallest repair for a failure just watched; same input choreography on each circuit. |
| I Tried Creating a Game Using Real-World Geographic Data | sLqXFF8mlEU | A build log; trust comes from showing bugs and skips; each feature fills a gap in the last output. |
| Coding Adventure: Chess | U4ogK0MIzqk | Dumbest version, then patch the concrete failing position; numeric before/after makes each idea undeniable. |
| Exploring How Computers Work | QZwneRb-zqA | A tower of reusable named chips found by asking what table is missing; his sign-bit mistake is refuted by the sim. |
| Trying to Improve My Geography Game with More Real-World Data | UXD97l7ZT0w | One knob turned on screen shows each cause; thin on the maths, honest about scope. |
| I Spent a Week Making a Game about Vacuuming | PGk0rnyTa1U | A progress diary whose one real sequence (Point, Stick, repeat) is tiny and immediately reused on cloth. |
| Coding Adventure: Simulating Fluids | rSKMYc1CQHE | Watch him fail forward; maths arrives as the name for something working; stepping stones invented freely. |
| I Created a (terrible) Video Game Console | TURzbXTNaA0 | Learn each component just in time, verify on the real device, self-deprecation lowers stakes. |
| Coding Adventure: Simulating an Ecosystem | r_It_X7v-1E | Add one rule, run until the consequence shows, then explain after the plot. |
| Polishing and Releasing My Tiny Geography Game | pNp4ug5F6To | Process is the lesson: test, watch it fail, sweep a parameter, fix. |
| I Tried Coding a Neural Network to Identify Doodles | hfMk-kjRv4c | Hand-tuning creates need for each part; brute-force nudging creates need for calculus. |
| A* Pathfinding (E01) | -L-WgKMFuhE | Watched execution on an empty grid, obstacles, then an overlay swap; pseudocode only after every line was seen. |
