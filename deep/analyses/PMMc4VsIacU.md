# DFS explained (Reducible, 21 min)

## Arc
Roadmap (0:00), minimal definition of traversal (0:41), invent-your-own walk (1:25-4:39), second ordering (4:39), small-graph implementation with a buggy first draft (6:30-11:05), iterative stack version (11:05), post-order (14:58), applications (17:02).

## Strongest moves
1. **Invent before naming (1:25).** The narrator says the line of thought presented "is exactly the DFS algorithm" and wants it to feel like something you could do alone. Nothing is called DFS until the walk is done.
2. **Long literal walk (1:39-4:11).** Roughly 2.5 minutes of narrated stepping on a 10-vertex graph: go deeper, hit a dead end, retrace. The repetition lets the viewer notice the retrace rule themselves. A short explorer persona (4:25) summarises it.
3. **Second ordering (4:39).** Choices are changed to show validity of multiple answers, with a practical caveat about exam tie-breaking (5:22).
4. **Bug then fix (7:09-8:33).** Naive recursion is presented, viewer asked to find the problem, and the infinite loop through vertex 0 motivates the marked list. A traced recursion call by call (8:47-10:52) verifies the fix.
5. **Two implementations framed by purpose (14:03).** Recursive is cleaner, iterative generalises. Equal O(V+E). Also pre-order to post-order is shown as a one-line move of the visit call (16:34).

## Unusual
Heavily dialogue-like "let's pick vertex 6" narration with no formal notation until 6:57. Ending applications are skimmed (cycle detection in a sentence), with the topological sort proof explicitly left as homework (19:20).

## Principles
Confirmed: 1, 2, 5, 6, 7, 9, 10, 11. Partly: 4 (explorer only), 8 (flat speech, long beats), 12, 13. Not observed: 3.

## Velocity
- "Invent-then-name" playbook; delay the term until after two traces.
- Offer a "find the bug" pause with a predict prompt.
- Switch to smaller example when moving to code.
- Mark cheap applications as optional so the orchestrator can skip them.

Skeptical note: judgments rest on automatic captions only; on-screen visuals are inferred from narration, so beat boundaries are approximate.
