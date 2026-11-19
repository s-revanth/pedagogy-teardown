# SebastianLague holdout summary (X-iSQQgOd1A, l-hh51ncgDI)

**Scores.** Ant and Slime: 7 hit, 5 near, 5 miss of 17 predictions (41% strict, 56% with near at half); overall 2/5. Minimax and Alpha-Beta: 8, 5, 4 (47%, 61%); overall 3/5, partly because the algorithm dictates its own order.

**Does the report need to condition on format? Yes.** It treats the channel as one arc: tiny toy, dumb version, visible failure, minimal concept, verify, repeat, honest close. The holdouts show three regimes:
1. Designed-lesson Coding Adventures (memory, chess, fluids, neural net), where the arc fits.
2. Project devlogs (this ant video, geography, vacuum), where features accrue as a "next step" list and designs are borrowed from papers and videos.
3. The Algorithms Explained lecture format (minimax, A* E01): impersonal voice, no break-fix, humor or caveats, a numeric toy at 0:15, code at 22-70% of runtime, layered reruns. The report filed A* as a "variant" and the generator inherited that.

## Recurring gaps
- Failure-gated vocabulary did not occur in either video. Ant evaporation (7:28), diffusion (12:44) and species (15:59) arrive ungated; pruning is motivated by wasted work on a bound (minimax 5:21).
- Notation: ant formulas precede the demo (1:06, 1:43) and baseline code appears at 0:17. "Equation after behaviour" is too blunt.
- Viewer questions: report says never; minimax asks one at 7:06.
- Big unpredicted blocks: the ant video's 4.5 min travelling-salesman opener; minimax's four-pass layered rerun.
- Voice: dry self-deprecation (ant) versus neutral (minimax). The report has no voice spec, so the generator wrote a generic chatty teacher.

## Strongest rules, ranked
1. Format gate on title and voice: lecture arc versus devlog arc (minimax 0:15-10:46; A* E01). Universal pattern.
2. Layered reruns of one example, one overlay per pass, answer stated unchanged (minimax 1:10, 3:56, 5:06, 8:44). Universal.
3. Next-feature chain: skip failure demos for guessable rules, cite each design source, defer then pay off a hard feature (ant 7:28 to 13:01). Citation trigger is universal.
4. Open devlogs with an adjacent classic problem and a human-scale blow-up number (ant 0:02-4:28).
5. Split notation by kind: cost and selection formulas before the demo, model equations after (ant 0:17, 1:06, 1:43).
6. One pause-the-video quiz at about 65% runtime in lecture format (minimax 7:06).
7. Let-it-run silent payoff, then a 30 s extension recipe (ant 14:00-16:45).

## Most wrong or vague sections
- Section 2 arc (steps 3 and 6) and Section 5 theories 1 and 2: overgeneral.
- Section 6 ("never asks the viewer", "few recaps", wishlist endings): true for Coding Adventures only.
- Section 3 move table: counts without triggers, no humor type, no density for outside sources or caveats.
- Principles 3, 8 and 13 remained unusable for generation.

## Verdict
The hypothesis generalises partially. Moves that do not conflict with format (toy-world, build-and-verify, visible-repetition, notation held back, no planted misconception, honest-caveat in devlogs) transferred, giving 56-61% credited hit rates. Arc and ordering did not: both arcs differed materially, and the lecture regime had only one training video. Fix: add a format gate and tag each training video with its regime so every rule carries a per-regime n.
