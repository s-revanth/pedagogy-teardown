# rf6uf3jNjbo — Towers of Hanoi: A Complete Recursive Visualization (Reducible)

## Structure arc
Cold-open hook (a clip of the later "blow your mind" moment) and a confession that the presenter needed days to solve it. Rules stated minimally, then a three-phase roadmap (0:57): puzzle, program, unravel. Phase 1 (1:38-8:01) is pure puzzle on animated rods: random guessing fails, the failure reveals the key constraint, n=3 is solved, then n=4 is reduced to n=3. Phase 2 (8:01-16:13) formalizes: spec, trivial helper, a three-step recursion recipe justified with dominoes, then the code built line by line from the puzzle strategy. Phase 3 (16:13-19:53) traces the n=3 calls synced to disc movement. A recap closes it.

## Strongest moves
1. **Brute force as constraint mining (1:52-3:26).** Three plausible random moves lead to a dead end, and the presenter draws the insight from that dead end: the largest disc must move first, so the top two must be parked. The failure is the lesson.
2. **Visible repetition, then naming it (4:32-6:08).** n=4 is solved by "ignoring the largest disc" and re-solving the 3-disc case with a different destination. At 6:08 he says outright that this is where the recursion comes from. The narration of the sub-moves is long and repetitive on purpose.
3. **Dominoes with failure mapping (11:03-12:41).** Each of the three steps maps to a domino condition, and he then shows how dropping any one step stops the chain. That justifies the recipe instead of just stating it.
4. **Invented stepping stone (13:38).** "other = 6 - start - end" is a small trick that unblocks the code. It is introduced right when it is needed.
5. **Forward abstraction, then unwind (16:13).** After the leap of faith, he admits some viewers won't trust it and traces every call on the original n=3, so the video ends where it started.

## What's unusual
The puzzle, the code, and the trace all use the same three-step strategy and the same n=3 example. No notation appears for 8 minutes. The "easy win first" helper (9:25) has a stated emotional reason, which is to beat intimidation. That reason is rarely voiced. Depth is shallow: there is no move count (2^n-1) and no complexity analysis.

## Principle verdicts (brief)
Confirmed: 1, 2, 4, 5, 6, 7, 9, 10, 11, 13. Partly: 3 (the arrow notation is reused but never drilled), 8 (the idea rate slows during the long n=4 narration, but speech rate can't be checked from a transcript), 12 (dominoes only, no outside sources).

## Velocity implications
- Recursion playbook: hand-solve small cases in the sim, then leap of faith, then trace the call stack on the first example.
- Let the learner get stuck by guessing, then pull the constraint out of their own dead end.
- When a subproblem comes back, the voice says so explicitly. Repetition alone isn't enough.
- During a trace, show each call's sub-goal next to the global state.
- Eval: no formal notation before two concrete solved cases.
