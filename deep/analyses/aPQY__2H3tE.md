# Reducible: 5 Simple Steps for Solving Dynamic Programming Problems (aPQY__2H3tE)

## Arc
Roadmap first (0:00): five steps, two problems, a closing discussion. Problem 1, longest increasing subsequence (0:49 to 9:15), runs the steps slowly; problem 2, box stacking (9:15 to 18:52), runs them again faster on a harder case. Close with a catalogue of common subproblem shapes (19:20) and advice to practice.

## Strongest moves
1. **One picture does the work (1:59, 10:56).** Casting both problems as a DAG makes "increasing subsequence" and "stack" both equal "path." Introducing it on the easy problem and reusing it on the hard one removes the cost of a new interface.
2. **Ask what a concrete target needs (4:20, 13:02).** Pick index 4 or the red box, ask which subproblems are required, and read them off the graph. The relation is formed from instances, then generalized on a second example (5:42, 14:11).
3. **Defer the side question (1:45, 7:50).** Length first; recovering the sequence is a separate beat with prev-pointers traced by hand.
4. **Dependency order as a stepping stone (14:40).** Sorting by length is introduced as the thing that makes left-to-right solving valid.
5. **Exit with a map (19:20).** A catalogue of recurring subproblem shapes lets the learner transfer.

## Unusual
No naive recursion or exponential blowup is shown, so the reason to use DP is never felt. The subproblem is stated rather than discovered, apart from a short "I find end-point more intuitive" choice (3:37). It also admits plainly that the subproblem step takes creativity and practice (19:06).

## Principle verdicts
Confirmed: 3, 9, 10, 11. Contradicted: 6 (no brute force first). Partly: 1, 2, 4, 5, 7, 8, 12, 13. Evidence for 8 is only indirect: the second trace is long and slow, and code appears after the relation.

## Velocity implications
- Keep a persistent graph model in the scene; light up predecessors for "needed subproblems."
- Show a step tracker for the pipeline.
- Learner model should check whether naive recursion was seen; if not, add it before DP (a gap here).
- Reuse the first problem's representation in the second to lower novelty.
- Close with a pattern catalogue after two worked cases.
