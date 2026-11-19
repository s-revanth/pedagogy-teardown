# Gap analysis: Reducible, "PageRank: A Trillion Dollar Algorithm" (JGQe4kiPnrU, 25:26)

Note: the script's explicit predictions are in its section 4 (the brief says section 5). Script length shortfall is ignored.

## 1. Real beat sheet (compact)

| m:ss | Lvl | Tags | Paraphrase |
|---|---|---|---|
| 0:00 | H | hook-question, roadmap | Users wander a web of pages; how should we rank pages using a Markov chain model? Promise a discovery-oriented build to PageRank. |
| 0:41 | H | minimal-definition-then-refine, toy-world | Markov chain: pages are states, links carry transition probabilities (0.5, 100%, 1/3 per outlink); probabilities can be altered. |
| 1:57 | H | hook-question | Problem restated: four search-result pages, how to rank? What is "importance" of a state? |
| 2:41 | B | analogy, simulation-as-argument, commit-to-answer | One user wanders forever, counters per state; long-run proportions settle; shown at state 2 = 26%; named stationary distribution at 3:22. |
| 3:35 | N | roadmap | Three open questions: how to find it, when does it exist, how to compute efficiently. |
| 4:04 | I | notation-after-concept | State distribution as a probability vector, uniform start. |
| 4:57 | I | notation-after-concept, build-and-verify | One-step probability for state 0 as a weighted sum, a dot product, stacked into a transition matrix; update is a vector-matrix product. |
| 6:19 | I | minimal-definition-then-refine | Stationary: distribution unchanged by a step; users move but proportions stay. |
| 7:04 | N | design-it-yourself, special-case-first | Does a unique one exist? Challenge with hint (two states); identity chain gives many. |
| 8:28 | N | notation-after-concept, humor | Name: reducible chains; want irreducible; unique solution follows ("I did not make that name up"). |
| 9:09 | N | simulation-as-argument, visible-repetition | Convergence: uniform start settles in about 20 steps; concentrated start in about 25. |
| 10:04 | N | design-it-yourself, failure-shown | Second challenge: find a chain that never converges; two-state flip oscillates (80/20 start). |
| 11:03 | I | notation-after-concept | Name: periodic, period 2; aperiodic otherwise. |
| 12:09 | N | callback, generalize | Irreducible + aperiodic gives guaranteed convergence (ergodic theorem); applies to web whatever the start. |
| 13:16 | N | honest-caveat | Proof needs probability background; linked in description. |
| 13:30 | N | brute-force-first, multiple-decompositions | Method 1: iterate multiplication until change below tolerance. |
| 14:11 | N | failure-shown, build-and-verify | Method 2: solve pi P = pi directly; equations redundant, fix by adding sum-to-one. |
| 14:53 | I | analogy, generalize-to-other-domains | Method 3: transpose to column vectors, fixed vector is eigenvector for eigenvalue 1; personal favorite; links to linear algebra. |
| 17:35 | H | recap, inline-quiz | Take stock; which of three methods wins on hundreds of millions of pages? |
| 18:04 | N | honest-caveat, cost | Cubic time kills methods 2 and 3; iterating converges in about 50 steps, approximate ("cheating a bit"); engineering-mindset moral. |
| 19:28 | N | failure-shown | PageRank complications: dead-end pages absorb everything; closed cycles trap users. |
| 20:37 | N | roadmap | Our tools need irreducible and aperiodic; idea: turn the hard case into a solved case. |
| 20:51 | B | analogy, build-and-verify | Bored surfer jumps to a random page; add alpha/n teleport; rows no longer sum to one so damp the original by 1-alpha. |
| 22:31 | I | notation-compaction | Damped matrix plus alpha/n matrix of ones; PageRank is the stationary distribution of this chain. |
| 23:11 | - | admin | Sponsor read (about 70 s). |
| 24:22 | H | recap | Recap: web as chain, modify, iterate to tolerance, rank. |
| 25:03 | H | story | Closing note on the founders; no teaser. |

## 2. Prediction scorecard (script section 4)

| # | Prediction | Predicted | Actual | Verdict |
|---|---|---|---|---|
| 1 | First question | 0:00-0:50 rhetorical question | 0:14 states the question (how to rank pages) | hit |
| 2 | First genuine pause or commit prompt | ~19:00 (patch a trap); small prompt at 4:30 | 7:46 (challenge with hint), 10:04, 17:50 (which method wins?) | miss |
| 3 | Notation: equations | ~6:30 | 6:19 stationary equation (pi P = pi); full system 14:11 | near |
| 4 | Notation: matrix M | ~12:10 | 5:52 transition matrix | miss |
| 5 | Notation: damping formula | ~19:30 | 22:44 | near |
| 6 | Misconception | yes: more in-links = more important; broken ~4:15 | none; no in-link counting anywhere | miss |
| 7 | Brute-force-first | yes: count in-links, direct solve | brute force is method 1 of 3 (13:30), and it wins at scale (18:31) | near |
| 8 | Examples | 3 toy webs, one failure each, then real web via sparse storage | 4-5 state chain, two 2-state counterexamples, dead-end and trap graphs; no sparse storage | near |
| 9 | Hook type | paradox/question around a trillion-dollar idea | scenario plus question; no paradox, no money framing in the narration | near |
| 10 | Ending | recap + callback; pointer to code and proof, no teaser | recap, founders note, proof link earlier (13:16); no teaser; no code | near |
| 11 | Move: failure-shown with each repair | present | 10:34 flip chain, 14:26 unsolvable system, 19:42 absorbing and trap, 22:02 sums break | hit |
| 12 | Move: roadmap with open slots | present | 3:35 three questions answered in turn | hit |
| 13 | Move: special-case-first | present | two-state examples, 4-5 state network | hit |
| 14 | Move: notation-after-concept | present | stationary distribution named after simulation; matrix after dot product | hit |
| 15 | Move: honest-caveat | present | 13:16, 18:58 | hit |
| 16 | Sixth: simulation-as-argument | present | 2:41-3:35, 9:24-9:51 | hit |

Hit rate: 7 hit, 6 near, 3 miss of 16 = 44% strict, 62% with near at half credit.

## 3. Structural alignment

Predicted arc: search-junk paradox hook, define importance, roadmap with two slots, circles and arrows, count in-links, spam failure, circular-definition insight, 3-page hand solve, random surfer, simulation, matrix, three views, power iteration, dead end, trap, teleport, cost at web scale, code, applications, recap + callback.

Real arc: scenario hook, Markov chain model, single-user simulation reveals the stationary distribution, three open questions, vectors and matrix, stationary definition, uniqueness (challenge), convergence (challenge), theorem, three computation methods, cost verdict, then PageRank problems and teleport fix, sponsor, recap.

- Predicted and present: roadmap (3:35 vs 1:35), toy world, simulation-as-argument (2:41 vs 11:00), matrix (5:52 vs 12:10), multiple decompositions (three methods vs three views), power iteration (13:30 vs 15:00), two start vectors (9:24), dead end and trap (19:28 vs 16:50), teleport (21:05 vs 19:30), caveat, recap (24:22 vs 24:50).
- Predicted but absent: junk-search hook, in-link counting, spam farm, circular-definition insight and hand-solved 3-page system, analogy-breakpoint, sparse-storage cost, code, applications montage, callback to a trillion dollars.
- Present but unpredicted: Markov chain definition as the starting object (about 20% of runtime on model and notation); existence and uniqueness question (7:04-9:09) with a hint-led counterexample challenge; convergence question with a second challenge (10:04-12:09); named properties (reducible, periodic) coined from the counterexamples; the ergodic theorem with a linked proof; eigenvector method and enthusiasm about it (14:53-17:35); "which method wins at scale" quiz and verdict that approximate brute force beats exact methods (17:50-19:28); sponsor block; humor on the name "reducible".

Timing drift: hook 0:00 vs 0:00 (0). First new idea: predicted in-link counting 3:20, real stationary distribution via simulation 2:41 (-0:39). Payoff: fixed-point formulation predicted 14:00, real 6:19 (-7:41); teleport and damping predicted 19:30, real 21:05-22:58 (+1:35 to +3:28). Ending: recap 24:50 vs 24:22 (-0:28).

Large-scale shape: PageRank itself occupies only 19:28-22:58 (14% of runtime). Roughly 77% is Markov chain theory. The generator built a PageRank-discovery video; the real video is a Markov-chain video that ends in PageRank.

## 4. Gap taxonomy

- Theory-first arc: topic-conditional. The report's arcs all start from a concrete problem and a slow approach. Here the object (Markov chain) is given, then its properties are hunted. Closest report analog is GJK's five open questions, but the report does not generalise it.
- Counterexample challenges with a hint (7:46, 10:04): underspecified. Report has design-it-yourself 6/12 (FFT n=4) but no "find a case that breaks the claim" pattern with a size hint.
- Naming properties from counterexamples (8:28, 11:03): underspecified. "Invent, derive, then name" fits, but nothing says the names come from the failures.
- Brute force wins (18:31): wrong-rule. The report's brute-force-first is always followed by failure; here the verdict reverses and the approximation is defended.
- Misconception predicted: generator-error (imported from round-1; not a move in the report's table).
- Hook: wrong-rule if read as "paradox or spectacle"; real hook is a scenario question. Report's hook list lacks a rule for which type; underspecified.
- Notation timing: wrong-rule. Report says symbols arrive late; here the vector appears at 16% and the matrix at 23%, though each follows a verbal computation. Topic-conditional: when the objects are numeric, notation is the home.
- Application named late: missing-rule. Title promises PageRank; the algorithm arrives at 77% as "transform the hard case to a solved one".
- Eigenvector link and enthusiasm (14:53, 17:08): voice/craft and generalize. Report has generalize-to-other-domains but no rule for linking to a standard course concept.
- Sponsor block at 23:11: missing-rule (admin); not predictable, small.
- Spam farm, circular definition, in-link counting, sparse cost, code: generator-error (invented content not in report).
- Humor on the term "reducible" (8:41): voice/craft; report says light and dry with no placement.

## 5. Overfit check

- "Start from a concrete problem, run the obvious slow approach, watch it fail": no slow approach fails here; the first computation is a simulation that succeeds (2:41).
- "Names, notation and code arrive last": stationary distribution is named at 3:22 (13%); matrix at 23%.
- hook-paradox and callback-to-hook (9/12): the hook is a scenario; recap ends on a story coda, not a callback.
- brute-force-first as a prelude to failure (6/12): contradicted at 18:31.
- Principle 1 "failure is the stepping stone" holds in every property hunt (10:34, 14:26, 19:42, 22:02).
- Roadmap 12/12 and "open slots ticked off" hold (3:35).
- Dependency order (principle 11) holds strongly: existence before convergence before method before scale before PageRank.

## 6. Proposed rule changes

1. Property-hunt arc (channel-specific, extends GJK). Trigger: topic is a theory object with hypotheses (existence, uniqueness, convergence). Action: define the object in 3 min with one example; show the answer once by simulation; list 3 open questions; for each hypothesis, ask the viewer to find a breaking case with a hint "use two states", pause about 10 s, show the 2-state counterexample, then name the failing property. State the theorem and link the proof. Evidence: 2:41, 3:35, 7:46, 10:04, 13:16.
2. Hold the named application until the theory is in place (channel-specific). Trigger: title names an applied algorithm built on a standard math object. Action: delay the algorithm's name and its specifics to at least 70% of runtime; introduce it as "transform the hard case into the solved case", then show it as one line ("stationary distribution of the modified chain"). Evidence: 19:28-22:58.
3. Brute-force vindicated variant (likely universal). Trigger: 2-3 methods compute the same quantity and cost matters. Action: present them in order brute-force, direct algebra (with one failure and repair), conceptual link; ask which wins at scale; answer with order-of-magnitude cost (cubic vs about 50 iterations); say plainly the winner is approximate. Evidence: 13:30-19:28, 18:58.
4. Notation after one verbal computation, timing topic-dependent (likely universal). Trigger: objects are vectors or matrices. Action: compute one entry in words (weighted sum), name it (dot product), then stack into a matrix; allow this at 15-25% of runtime. Keep names for properties after their counterexample. Evidence: 4:57-6:19, 8:28.
5. Hook by scenario (channel-specific). Trigger: theory-heavy title. Action: in the first 15 s state an "imagine users doing X" scenario and the ranking question, then the promise "we will discover it" by 0:30. Do not invent a spectacle or money framing. Evidence: 0:00-0:41.
6. Sponsor slot (channel-specific, minor). Trigger: runtime over 20 min. Action: put a 60-70 s sponsor read after the last content beat and before the recap. Evidence: 23:11-24:22.

## 7. Scores (1-5)

- Arc fidelity: 2. Dependency logic and failure-driven repairs match, but the video is theory-first and PageRank appears at 77%.
- Move-inventory recall: 4. Failure-shown, roadmap, special case, notation-after-concept, caveat, simulation, multiple-decompositions, two-start learner-discovers all appear; missed counterexample challenges and name-from-failure.
- Move precision: 3. In-link counting, spam, circular insight, 3-page solve, code, sparse cost and callback are false; about 9 of 22 predicted beats exist in some form.
- Pacing/timing: 2. Hook and recap are close; payoff placement is off by 2 to 8 min and the shape (77% theory) is wrong.
- Voice: 3. Predicted narration is clear and correct but misses the personal asides, pun on the name, and the "engineering mindset" moral.
- Overall regenerate-ability: 2. A generator would get the move vocabulary but write a different video.
