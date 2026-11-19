# 3Blue1Brown: how the channel teaches

Scope: 12 videos (neural nets ch.1, 2, 5; Fourier series; Fourier transform; Bitcoin; Putnam sphere; collision-counting pi teaser; Vectors ch.1; essence of calculus; sphere shadow; Wordle). Data note: Wordle (v68zYyaEmEA) was read from an Arabic machine translation. Its timestamps are reliable but its wording is approximate, so I weight it lower and flag where it carries a claim.

## 1. Bottom line
3Blue1Brown teaches by making the viewer a would-be inventor. One concrete object (a circle, a ledger among friends, a handwritten 3, a Wordle board) is held on screen and morphed, and every tool arrives as the answer to a problem the viewer has just felt. Notation is held back and then framed as compression of a picture the viewer already owns. Honesty is structural: hypotheses are labelled as hopes, approximations as wrong-but-improvable, and earlier motivating stories are sometimes undercut on camera.

## 2. Signature arc
Hook (familiar object plus paradox or wow) -> roadmap with an honest caveat -> toy world with one concrete case -> brute-force or naive attempt -> a wall, or a need -> invented stepping stone (often named "almost-X" or kept thin) -> notation as shorthand -> run on 2-3 examples, growing -> failure or caveat -> callback and teaser.

- Neural net ch.1 (aircAruvnKk): hook 0:04, roadmap and caveat 1:15, neuron = number 2:39, hope for layers 5:36, weights 9:11, matrix form 13:22, redefine neuron as function 15:10.
- Calculus (WUvTyaaNkzM): you-could-invent-it 0:34, circle 1:22, rectangle brute force 2:54, dr 3:14, name the move 6:50, generalise 8:35, derivative 11:54, callback 15:07.
- Fourier transform (spUNpyF58BY): finished animation 0:04, two notes 1:15, wrap machine 3:04, "almost Fourier transform" 7:35, first symbol 12:37, decoded recap 17:11.
- Bitcoin (bBC-nXj3Ng4): ledger 2:36, then a patch chain: signatures 3:31, replay 6:40, balance rule 7:16, replicated ledger 10:05, puzzle 11:15, hashes 12:22, mining 16:04, attacker 19:38, real numbers 21:45.
- Wordle (v68zYyaEmEA, lower weight): demo 0:00, naive tries 2:48, halving to bits 8:13, entropy 10:48, bot 13:54, failure 17:25, prior 18:22, fitted metric 25:07.
- Putnam (OkmNXy7er84): 2D three points 1:51, 3D wall 4:29-5:24, what does "4" mean 5:42, coin-flip reframe 6:14, lift to 3D 7:40.
- Gradient descent (IHZwWFHWa-w): recap 0:04, cost as scolding 3:22, dimension ladder 5:06-8:33, gradient 10:17, failure of edge story 13:09.
- Also: Transformers (wjZofJX0v4M) previews the whole pipeline at 3:06 before background; Sphere shadow (GNcFjFmqEc8) sketches the proof at 1:29 first; Vectors (fNk_zzaMoSs) picks one default image at 2:04; the pi teaser (HEfHFsfGXjs) is only hook and caveat.

Arc deviations: the pi teaser is all hook; calculus is itself a teaser with permission not to fully understand (9:29); Transformers front-loads a preview and a third of the runtime is optional background.

## 3. Move frequency (n/12, from beat tags)
| Move | n/12 | Best example |
|---|---|---|
| honest-caveat | 12 | Neural net ch.1, 4:06 (layer sizes admitted arbitrary) and 7:35 |
| roadmap | 11 | Neural net ch.1, 1:15; Transformers, 3:06 |
| design-it-yourself | 10 | Neural net ch.1, 8:23 (what knobs should the neuron have) |
| notation-after-concept | 10 | Calculus, 3:14 (dr after the ring needs thickness) |
| hook-question | 9 | Calculus, 1:22 |
| special-case-first | 9 | Calculus, radius 3 before R |
| generalize-to-other-domains | 9 | Calculus, 8:35 (area to distance) |
| callback-to-hook | 9 | Sphere shadow, 10:23 |
| teaser-next | 9 | Vectors, 9:23 |
| recap | 9 | Fourier transform, 17:11 |
| toy-world | 8 | Pi teaser, 0:04 |
| analogy | 8 | Fourier transform, paint unmixing 2:10 |
| act-it-out | 8 | Fourier transform, wrap graph 3:04 |
| build-and-verify | 8 | Sphere shadow, 6:51 |
| minimal-definition-then-refine | 7 | Neural net ch.1, 2:39 -> 15:10 |
| simulation-as-argument | 7 | Pi teaser, 0:51-1:59 |
| visible-repetition | 7 | Pi teaser, masses 100, 10^4, 10^6 |
| brute-force-first | 6 | Calculus, 2:54 |
| inline-quiz / pause-prompt | 6 | Wordle, 20:28 (entropy of 4 vs 16 words) |
| failure-shown | 5 | Gradient descent, 13:09 |
| notation-compaction | 5 | Neural net ch.1, 13:22 |
| learner-discovers (staged) | 5 | Putnam, 5:42 |
| commit-to-answer (soft) | 5 | Bitcoin, 11:15 (puzzle posed aloud) |
| misconception-first | 4 | Calculus, 0:34 (calculus as memorised rules) |
| show-full-complexity-then-zoom | 3 | Gradient descent, 4:30 |
| you-could-invent-it | 2 (plus calculus 0:49, 15:44) | Bitcoin, 0:03 |

Humor tag appears in 6, but it is light.

## 4. Principle scorecard (confirmed / partly / contradicted; unobserved counted separately)
| # | Verdict | Evidence |
|---|---|---|
| 1 Familiar start | Confirmed 10 / partly 2 / 0 | Circle, ledger, digit, game. Fourier series and Putnam are partly: hooks are spectacle or an exam story. |
| 2 Symbol cost | Confirmed 11 / 0 / 0 (1 n/a) | First symbol at 12:37 in a 19.7-min Fourier transform; dr at 3:14; log at 9:03 in Wordle. |
| 3 Habit with interfaces | Confirmed 2 / partly 3 / 0 (7 n/a) | Weak. Persistent three-panel scene (Fourier transform), colour contract (Transformers 11:57), Wordle colour patterns. Video cannot build habit. |
| 4 Analogy then rigor | Confirmed 9 / partly 2 / 0 | Ball on a hill before gradient (6:15); shadow analogy before similar triangles (3:39). Bitcoin explicitly rejects gold-mining (1:28). |
| 5 Act it out | Confirmed 7 / partly 4 | Unwrap ring (2:36), wrap graph (3:04), attacker's view (19:38). |
| 6 Brute force first | Confirmed 8 / partly 3 | Rectangles 2:54; trust-based ledger; letter-frequency guess in Wordle. |
| 7 Discovery by repetition | Confirmed 7 / partly 4 | Pi teaser shows 3 runs before naming; most others are narrated discovery. |
| 8 Pace by novelty | Partly 12 / 0 / 0 | No speech-rate data in compact transcripts for any video. Evidence is for idea rate: recaps and asides slow the beat, long runways precede symbols. |
| 9 Repeat across examples | Confirmed 7 / partly 5 | Same wrap machine on 3 Hz, 2 Hz, sum (5:38, 8:11, 8:48); Putnam construction run four times. |
| 10 Tiny to bigger | Confirmed 10 / partly 2 | 1 input -> 2 -> 13,000; 3D slice before 12,288D. |
| 11 Dependency order | Confirmed 11 / partly 1 | Bitcoin patch chain; named stepping stones. |
| 12 Connect everything | Confirmed 10 / partly 2 | Speech, velocity, Euler, guest researchers. Unanswered questions handed off with links. |
| 13 12-year-old plus expert, say why | Confirmed 8 / partly 4 | "Okay if that's all you know" (8:00, gradient descent) plus optional formula (Transformers 23:11). |

Nothing contradicted. Principle 3 is the weak one. Principle 8 needs a different knob: concepts per minute and recap density.

## 5. New principles and theories
1. **Hope before mechanism.** Ask what each component would ideally do, flagged as a hypothesis, before showing it. Evidence: neural net ch.1 (5:36-7:51, weights at 9:11 answer it); gradient descent (13:09 tests and partly breaks the hope); Bitcoin (11:15, protocol posed as a design problem). Falsifiable: if a mechanism is introduced as the answer to a stated ideal-function question, learners predict its shape in a follow-up better than learners shown the mechanism first.
2. **Patch chain.** Introduce each component as a repair for a failure just shown. Evidence: Bitcoin (3:31, 6:40, 7:16, 10:22), Wordle (naive attempts 2:48 drive bits, prior, metric; low weight), Putnam (3D wall 5:24 drives reframe). Falsifiable: if each concept is stored with the failure it patched, learners asked "what breaks without X?" answer correctly more often than learners taught X first.
3. **Named stepping stone, then diff.** Give a provisional object a name ("almost Fourier transform", "a neuron holds a number") and arrive at the true definition as one or two stated changes. Evidence: Fourier transform (7:35 -> 15:36), neural net ch.1 (2:39 -> 15:10), Wordle, Vectors (arrow default 2:04). Falsifiable: if the refinement is delivered as an explicit diff, learners who held the stepping stone retain the final formula better than learners who got it whole.
4. **Formula read as procedure.** Narrate notation as ordered actions on the object on screen. Evidence: Fourier series (18:48-20:17), Fourier transform decoded recap (17:11-18:20), calculus (11:54). Falsifiable: if each symbol is narrated as a step on a picture the learner has seen, symbol-to-meaning matching improves over symbol-first definitions.
5. **Lower the bar out loud.** Tell the learner what they need not master, and give permission to leave an idea unfinished with a promised return. Evidence: gradient descent 8:00, calculus 9:29, Bitcoin 1:46, Transformers 6:30-7:03. Falsifiable: if the tutor states skippable parts, learners with weak prerequisites continue rather than abandon, with no drop in core-idea scores.
6. **Undercut your own story.** After teaching a method, show where the motivating story fails. Evidence: gradient descent 13:09-16:17 (hidden neurons look random), neural net ch.1 7:35 and 16:48, Transformers 15:22 (queen is off), pi teaser 3:46. Falsifiable: if a failure-case beat follows the lesson, learners overclaim the model less on transfer items.
7. **Meta-lesson named at the pivot.** State the reusable heuristic before applying it. Evidence: Putnam 5:57, calculus 6:50-8:19, sphere shadow 6:14 pro tip. Falsifiable: if the technique is named at the pivot, learners apply it unprompted on a new problem more often than when only the answer is stated.

Lower-weight overlap: sphere shadow's "claim the shape first" (1:29, two cancelling effects) is a sketch-before-proof move that also appears in Transformers 3:06. Candidate eighth theory.

## 6. What the channel does badly or never does
- Almost no real learner turn. Prompts are pause-and-ponder at best (gradient descent 16:33; sphere shadow hands off exercises at 11:33). No evidence of any adaptation.
- No habit building (principle 3 unobserved in 7 videos).
- Speech-rate pacing cannot be assessed here. The compact transcripts carry no usable rate signal, so principle 8 is idea-rate only.
- Long runways before payoff (Fourier series central formula near 13 min) are only sustainable for motivated viewers.
- Humor and analogy are sparse; Bitcoin rejects analogy outright. Learners who need a metaphor get none.
- Several videos defer rigor to links or sequels (Fourier series convergence, calculus rigor), so the closing is often open.
- Wordle evidence is weaker (machine translation), including its claim to fit a metric to data.

## 7. Velocity translation
- **Scene builder:** hold one object and morph it; draw parameters in the input's geometry (weight grid over pixels); persistent multi-panel scene with only data swapped; colour contract declared once; running tally widget (Transformers 18:00); dimension-ladder scene; fix-and-drag with 2D/3D toggle.
- **Voice/beat script:** hope-as-hypothesis beat; formula narrated as steps; "it's still just wrapping" reassurance when scenes get busy; "you need only know X" line; name the heuristic at the pivot; state exclusions and why.
- **Orchestrator rules:** playbooks as failure chains; "claim in words" before any long derivation; generalise-to-simplify beat with reason; failure-case beat after each method; mark ideas "seen, not mastered" with a promised return; toy parameters before real ones; gate notation on two concrete runs.
- **Playbooks:** patch-chain, dimension-ladder, wall-then-reframe (2D works, 3D fails, solve 2D a second way, verify against the known answer), stepping-stone-and-diff.
- **Learner model:** tag provisional definitions and schedule an upgrade beat; store the failure each concept patched; log deferred rigor questions and offer them later.
- **Ghost hands:** nudge dx before the ratio is named; fix two points and drag the third; sweep a parameter until alignment.
- **Evals:** every symbol follows the visual that demands it; final formula narrated term by term; failing natural route precedes the elegant one; tutor shows where its own earlier story breaks.

## 8. Per-video one-liners
| Title | ID | Theory |
|---|---|---|
| But what is a neural network? | aircAruvnKk | Reverse-engineer a hope (edges, loops, digits) so weights answer a question the viewer holds; thin definitions upgraded later. |
| Fourier series (DE4) | r6sGWTCMz2k | Each symbol gets a physical job; widen to complex functions to simplify. |
| How does bitcoin work | bBC-nXj3Ng4 | Viewer as inventor; every mechanism patches a just-shown failure. |
| Hardest problem on hardest test | OkmNXy7er84 | Hit a wall in 3D, re-solve 2D a stranger way, check against the known answer. |
| Counting puzzle and pi | HEfHFsfGXjs | Sell the question: escalating runs, caveat, deferred answer. |
| Vectors ch.1 | fNk_zzaMoSs | Pick one default picture; numbers are a translation layer; justify definitions. |
| Fourier Transform | spUNpyF58BY | Build the machine first, symbols last; named stepping stone; formula as recap. |
| Transformers | wjZofJX0v4M | Preview, dependency-ordered background, running tally, optional-depth gates. |
| Wordle and information theory (lower weight) | v68zYyaEmEA | A familiar game yields numbers; each definition built from the previous count, bot failures drive refinement. |
| Essence of calculus | WUvTyaaNkzM | One circle carries three ideas; name the move, not just the answer. |
| Gradient descent | IHZwWFHWa-w | Drop dimensions to recover intuition, then show the honest negative result. |
| Sphere shadow | GNcFjFmqEc8 | State the shape of the argument first; hand proof two to the learner. |
