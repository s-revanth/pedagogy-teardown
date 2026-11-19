# Reducible: how the channel teaches

Data note: all 12 Reducible videos in the tracker now have analyses (FFT h7apO7q16V0, recursion ngCos392W4w, DP aPQY__2H3tE, JPEG 0me3guauqOU, graph theory LFKZLXVO-Dg, PNG EFUYNoFRHQI, Hanoi rf6uf3jNjbo, DFS PMMc4VsIacU, collisions eED4bSkYCB8, marching squares 6oMZb3yP_H8, BFS xlVX7dXLS64, GJK ajv46BSqcK4). This replaces an earlier 7-video report; all counts are n/12. Eleven of twelve have automatic captions (only graph theory is manual), so timestamps are approximate (about 15 s) and visuals are inferred from narration. Annotation is single-rater, and move counts come from beat tags the annotators applied unevenly (see section 6).

## 1. Bottom line
Reducible teaches an algorithm as a chain of forced moves. It starts from a concrete problem the viewer half-knows, runs the obvious slow approach, lets that approach fail or become visibly expensive, and mines the failure for the next idea. Names, notation and code arrive last, as a receipt for something the viewer has already watched work. Speech rate is not the pacing tool: the channel slows down with staged pauses, hand-worked small cases, repeated examples and occasional spoken permission to be confused.

## 2. Signature arc
Hook or goal, then roadmap, then home problem in a minimal definition, then brute force, then failure or cost, then special-case ladder, then the insight (often derived from a constraint), then notation and code, then verify or trace, then recap and callback. No video has every stage. The three non-core variants are listed after the main arc.

Core-arc videos:
- Hanoi (rf6uf3jNjbo): hook 0:00, rules 0:13, roadmap 0:57, random guessing fails 1:52, stuck state yields constraint 2:46, n=3 3:26, n=4 reuses n=3 4:32, notation 8:01, dominoes 11:03, code 14:07, call trace 16:13, recap 20:05.
- FFT (h7apO7q16V0): reframe as polynomial multiplication 1:24, brute force O(d^2) 2:05, plan with a "magic box" 6:55, naive evaluation fails again 8:02, x^2 then x^3 8:44-10:10, planted trap 12:29, roots found by hand 13:34, omega 16:21, code 20:46, interpolation twist 24:10, recap 26:48.
- Marching squares (6oMZb3yP_H8): hook 0:00, "I have no clue either" 1:47, easy frames 2:30, harder general problem 4:48, sampling game 5:55-7:34, one cell 10:04, 16-case quiz 12:22, interpolation 15:30, name formalised 17:16, back to the hook 20:09.
- JPEG (0me3guauqOU): 15 MB vs 0.8 MB gap 1:11, illusion 3:36, toy images 6:03, probe the DCT as a black box 11:27-17:00, formula as receipt 18:03, whole-image rebuild 27:17.
- DFS (PMMc4VsIacU): roadmap 0:00, invent your own walk 1:25-4:11, second ordering 4:39, buggy recursion 7:09-8:33 then fix, traced 8:47-10:52, iterative stack 11:05, post-order 14:58, applications 17:02.
- PNG (EFUYNoFRHQI): promise of a 50x faster rival 0:00, Huffman 2:04, RLE breaks 4:37, LZSS by hand 6:44-12:18, gradient image defeats everything 13:13, filtering 13:41, deflate recap 21:00, QOI as five rules 23:44, moral.
- Collisions (eED4bSkYCB8): finished sim 0:00, frames 1:13, one particle 2:40, tunneling 6:50, continuous detection 10:03, two particles 11:39, cost 13:31, then sweep and prune, grid, kd-tree, BVH to 25:24, recap 27:05.
- GJK (ajv46BSqcK4): hook 0:00, "roller coaster" promise 1:36, reframing chain 3:15-5:38, support functions 8:51, bird's-eye pass 13:29-16:45, five open questions 17:14-26:06, recap of three shifts 29:24.

Variants:
- Ritual (ngCos392W4w recursion, aPQY__2H3tE DP): a numbered five-step procedure run on problems of rising difficulty (3 in recursion, 2 in DP). The habit is the product.
- Physical model plus diff (xlVX7dXLS64 BFS): balls on strings 0:34, then stack-to-queue diff 2:30, then flood fill in disguise 6:13-9:58.
- Guided tour (LFKZLXVO-Dg graph theory): motivate 1:22-4:30, define, vocabulary 5:20-9:56, representations 10:14, open problem 12:35. No discovery arc.

## 3. Move frequency (n/12 videos, from beat tags)
| Move | Videos | Best example |
|---|---|---|
| roadmap | 12 | FFT 6:55 plan with a missing box |
| minimal-definition-then-refine | 12 | Graph theory 0:00 circles and lines before "vertex" |
| honest-caveat | 11 | PNG 3:28 1.89 bits misleading; tree must be stored |
| build-and-verify | 11 | Recursion 9:20 "is that coincidence?" on 3x4 |
| recap | 11 | GJK 29:24 three shifts |
| visible-repetition | 10 | DFS 1:39 long literal walk |
| humor (light, dry) | 10 | Recursion 14:30 "crazy sorcery" |
| hook-question | 9 | FFT 3:32 can we do better? |
| special-case-first | 9 | FFT 8:44 x^2 then x^3 |
| notation-after-concept | 9 | FFT 16:21 omega after roots found by hand |
| callback-to-hook | 9 | Hanoi 15:29 opening line lands |
| toy-world | 9 | Marching squares 5:55 mystery-function game |
| generalize-to-other-domains | 8 | Marching squares 22:12 electric potential |
| learner-discovers | 8 | JPEG 15:18 predict next frequency index |
| inline-quiz (pause) | 8 | Recursion 2:19 relate n=5 to n=4 |
| analogy | 8 | BFS 0:34 balls and strings; Hanoi 11:03 dominoes |
| brute-force-first | 6 | FFT 2:05 and 8:02 "our old foe" |
| failure-shown | 6 | PNG 13:13 gradient image defeats both tools |
| multiple-decompositions | 6 | FFT 22:50 evaluation as matrix product |
| design-it-yourself | 6 | FFT 13:34 solve n=4 for the points |
| rule-list | 6 | PNG 23:44 QOI as five rules |
| hook-paradox | 5 | JPEG 1:11 file-size gap |
| commit-to-answer | 5 | Marching squares 12:22 draw the other 12 cases |
| simulation-as-argument | 5 | Marching squares 6:51 1k, 10k, 20k samples |
| act-it-out | 4 | Recursion 3:53 trace |
| analogy-breakpoint | 3 | Hanoi 11:58 dominoes that fail |
| second-person-role | 2 | DFS 4:25 explorer persona |

Rare: running-character (1, FFT "old foe" 8:16), presenter-was-wrong (1), teaser-next (3), story (3).

## 4. Principle scorecard (12 videos)
| # | Principle | Verdict | Count (conf / partly / contra / not obs.) | Evidence |
|---|---|---|---|---|
| 1 | Start from the familiar | Confirmed | 10 / 2 / 0 / 0 | Paint bucket (BFS 6:13), maps and friends (graph 1:22), polynomial multiplication instead of frequency language (FFT 1:24). |
| 2 | Every symbol costs effort | Mostly confirmed | 7 / 5 / 0 / 0 | Omega held back to 16:21 (FFT), JPEG formula at 18:03, DFS notation at 6:57. Graph theory's 15 terms in 4 minutes is the counterexample. |
| 3 | Interfaces become comfortable through habit | Weak | 1 / 5 / 0 / 6 | Only DP (reused DAG, 10:56) and the ritual videos show it; most videos never reuse an interface long enough to test. |
| 4 | Analogy first, then rigor | Partly | 2 / 7 / 0 / 3 | Real analogies are rare (BFS balls, Hanoi dominoes). The familiar anchor is usually a problem, not an analogy. |
| 5 | Act out the problem literally | Partly | 5 / 5 / 0 / 2 | DFS 1:39 literal walk, PNG 6:44 hand LZSS, Hanoi by hand. |
| 6 | Brute force first, neat scratch pad | Confirmed | 8 / 1 / 1 / 2 | FFT 2:05, Hanoi 1:52, collisions 13:31. DP contradicts: naive recursion never shown. |
| 7 | Learner discovers via repetition | Mostly confirmed | 7 / 4 / 1 / 0 | JPEG 15:18, recursion pauses, DFS 1:25. Graph theory contradicts (terms are told). |
| 8 | Pace by novelty (flat speech, idea-rate slowing) | Partly, consistent | 1 / 11 / 0 / 0 | No video shows speech slowing. Slowing is long literal walks (DFS 2.5 min), hand-worked n=4 (FFT), "take your time" (FFT 20:32, GJK 29:09). |
| 9 | Repeat across examples | Confirmed | 10 / 2 / 0 / 0 | Three problems in recursion; two in DP; x^2, x^3, degree 5 in FFT. |
| 10 | Tiny to bigger | Confirmed | 11 / 1 / 0 / 0 | Hanoi n=3 to n=4; one particle to many (collisions 2:40-13:02). |
| 11 | Dependency order, invent stepping stones | Confirmed | 12 / 0 / 0 / 0 | The only unanimous principle: magic box (FFT), reframing chain (GJK), tool stack (PNG). |
| 12 | Connect everything incl. outside | Partly | 5 / 7 / 0 / 0 | Sudoku as graph coloring, electric potential, QOI creator story; physics derivation skipped with a link (collisions 12:35). |
| 13 | Simple for a 12-year-old, expert depth, say why a tool | Partly | 3 / 9 / 0 / 0 | Strong "why this tool": adjacency list for sparse graphs (graph 12:00), recursive vs iterative DFS (14:03). Proofs often skipped. |

Tally: 7 of 13 principles are confirmed or mostly confirmed (1, 2, 6, 7, 9, 10, 11); 3, 4 and 8 are weak or only indirectly supported; 5, 12 and 13 are partly.

## 5. New principles / theories
1. **Failure is the stepping stone.** Each new tool is introduced as the repair of a failure the learner just watched. Evidence: FFT 8:02 and 12:29 (naive evaluation, then squared points all positive, which forces complex numbers); PNG 4:37 and 13:13 (RLE breaks on two pixels, gradient defeats Huffman and LZSS, filtering follows); DFS 7:37 (infinite loop motivates the marked list); Hanoi 1:52 (random guessing yields the constraint). Falsifiable form: if a tool is introduced after the learner sees the previous tool fail on a tiny input, then learners can restate why the tool exists, more often than if the tool is introduced first and the failure is explained afterwards.
2. **Invent, derive, then name.** The object is produced from a constraint or a walk and labelled afterwards. Evidence: FFT 13:46-16:35 (solve x2^2=-1, then "roots of unity", then omega); DFS 1:25 (the walk is called DFS only after); JPEG 18:03 (formula arrives as a receipt for observations from 12:43-17:00); Hanoi notation 8:01. Falsifiable form: if a term or symbol is shown only after the learner has produced its referent, then they will map symbol to meaning with fewer errors than if the symbol comes first.
3. **Make the cost felt, in the learner's units.** A running quantity motivates each stage. Evidence: collisions 14:00 and 18:38 (5000 tests per frame, 1h40m versus 3 minutes); JPEG 1:41 (a 5% target meter orders the stages); FFT 8:16 (the O(d^2) "old foe" returns); PNG 18:29 (5^240 rules out brute force). Falsifiable form: if complexity is shown as a number the learner can imagine waiting for, then they rate each optimisation as more needed than if it is stated in big-O alone.
4. **A new interface is a diff on one the learner already holds.** Evidence: BFS 2:30 (queue replaces stack in the iterative DFS), FFT 26:19 (inverse code differs by one omega line), DFS 16:34 (post-order is a one-line move of the visit call), DP 10:56 (same DAG reused for a second problem). Falsifiable form: if a second algorithm or direction is presented as a highlighted change to the first, then time-to-correct-implementation falls versus presenting it fresh.
5. **A plan with named empty slots buys deferral.** The learner can wait for the hard part if it is explicit. Evidence: FFT 6:55 (magic box, revisited 22:22); GJK 17:14-26:06 (five listed open questions, each closed in order); Hanoi 0:57 and DFS 0:00 (three-phase roadmaps). Falsifiable form: if the unresolved parts of a lesson are listed as open slots and later ticked off, then learners abandon dense segments less than if the same content is delivered without the list.
6. **Say the emotional state out loud at idea-rate peaks.** The narrator names confusion or struggle and licenses persisting. Evidence: GJK 16:45 ("pat on the back") and 29:09 ("take your time"); FFT 20:32 (tricky step, pause and verify); PNG 13:13 (lingers in "so depressing"); marching squares 1:47 (presenter admits no clue). Falsifiable form: if a segment of high new-idea density includes a spoken regulation line, then learners finish it at a higher rate than the same segment without one.

## 6. What this channel does badly or never does
- Almost no real analogy (principle 4: 2 confirmed of 12). The anchor is a problem, so learners without the problem's background (polynomial multiplication, graphs) get no easier entry.
- No ongoing spaced recall. Graph theory introduces about 15 terms in 4 minutes with no check; no video quizzes earlier material after the first third.
- Proofs and derivations are deferred or linked (FFT 5:22 and 24:10, collisions 12:35, DFS 19:20, topological sort left as homework). Honest, but a gap for learners who need the argument.
- DP (aPQY__2H3tE) never shows naive recursion, so the motivation for DP is thin; the subproblem is given, not found.
- Endings are uneven: DFS ends on an application montage with no strong recap; GJK and FFT recap well.
- Interface habit (principle 3) is untested: single-sitting videos cannot show it.
- Data caveats: the tag counts overstate some moves (roadmap and minimal-definition-then-refine at 12/12 mean the annotators used them as default labels), the DFS first_question metric (7:37) conflicts with its earlier invent-your-own prompt at 1:25, and "n/12" is per video, not weighted for length (BFS is 11 minutes, PNG and GJK 32).

## 7. Velocity translation
- **Scene builder:** add a "failure scene" template: run the naive method on a tiny input and let it visibly break, with a counter. Add a pipeline/plan scene with empty slots that fills in as segments finish. Add a side-by-side diff scene for code, highlighting only changed lines. Keep one reusable world (shape pair, graph, image) across a whole lesson.
- **Voice / beat script:** enforce notation-after-concept: a symbol line may not precede the beat that produced its referent. Add a "regulation line" slot at beats where idea density peaks. Speech stays flat (~170 wpm); slow with beat length and extra examples.
- **Orchestrator rules:** show the plan after each solved slot; offer "find the bug" pauses with a predict prompt; swap to a smaller example when moving to code; allow "skip derivation with link" for low-math learners; mark applications as optional.
- **Playbooks:** invent-then-name; stack of tools (fail, fix, recap diagram); ritual (numbered steps on rising problems); probe-the-black-box (vary one parameter at a time); reframing chain.
- **Learner model:** gate symbols behind the learner producing the referent (omega after 1, -1, i, -i); cap new terms per minute and schedule recall checks for introduced vocabulary.
- **Ghost hands:** step a sliding window or walk identically each repetition so the pattern is visible (PNG LZSS, DFS walk); support code diffs.
- **Evals:** flag any tool or symbol used without a stated reason; flag any number that could mislead without a caveat; flag a lesson lacking a naive-method failure.

## 8. Per-video one-liners
| Title | Id | Theory |
|---|---|---|
| FFT: Most Ingenious Algorithm Ever? | h7apO7q16V0 | Chain of "can we do better?" questions; each failure forces the next idea; roots of unity derived before named. |
| 5 Simple Steps for Solving Any Recursive Problem | ngCos392W4w | A five-step ritual run three times on harder problems; insight delegated through pauses. |
| 5 Simple Steps for Solving DP Problems | aPQY__2H3tE | Pipeline whose hard step (the subproblem) is made visible with a reusable DAG; weak on discovery. |
| The Unreasonable Effectiveness of JPEG | 0me3guauqOU | Probe the DCT as a black box one parameter at a time; the formula arrives as a receipt; a 5% gap meter orders stages. |
| Introduction to Graph Theory | LFKZLXVO-Dg | Motivate, then give minimum vocabulary; the strongest choice is justifying adjacency lists by sparsity. |
| How PNG Works | EFUYNoFRHQI | A tool stack where each tool fails on a tiny input; caveats buy trust. |
| Towers of Hanoi | rf6uf3jNjbo | Recursion taught twice: discovered by hand, then trusted as an abstraction, then unwound in a trace. |
| DFS Explained | PMMc4VsIacU | Invent first, name later; the buggy first draft makes the visited array a discovery. |
| Building Collision Simulations | eED4bSkYCB8 | Cost shown in wall-clock units; each structure is introduced as the fix for the last one's weakness. |
| Marching Squares | 6oMZb3yP_H8 | Staged detour; one idea (sign change brackets a contour) reused at pair, edge, cell and grid scale. |
| BFS Visualized | xlVX7dXLS64 | Balls-on-strings analogy gives the structure; implementation is a diff on DFS; paint bucket as hidden graph. |
| GJK Algorithm | ajv46BSqcK4 | Sequence of reframings; bird's-eye pass first, then five listed open questions closed in order. |
