# BFS visualized (Reducible, 11 min)

## Arc
Goal (0:00) is shortest paths from a start. Then the balls-and-strings analogy (0:34), a general definition (1:32), queue implementation as a variation on iterative DFS (2:30), a queue trace (3:25), then flood fill as a graph problem in disguise (5:15-9:58).

## Strongest moves
1. **Physical model before rules (0:34-1:18).** Vertices are balls, edges are strings; pull the start vertex up and the levels appear. The narrator says this visual made it click for them. The shortest-path guarantee (2:01) falls out of "visit closer things first".
2. **Diff against a known algorithm (2:30).** BFS is introduced as the earlier iterative DFS with the stack replaced by a queue, so almost no new interface is learned.
3. **Short, complete trace (3:25-5:02).** Includes popping already-marked vertices (4:48), which is where learners often get confused.
4. **Familiar tool, then disguise (6:13-7:38).** The paint bucket in MS Paint is the problem; the reveal at 6:57 is a joke about this being a graph video. Pixels become vertices and the edge model is built literally.
5. **Honest scoping.** Edge-weight caveat (2:16), orders are not unique (2:30), DFS also works (7:38).

## Unusual
Short and light. No misconception stage, no brute force, and one analogy only. The takeaway is about perspective, not the algorithm.

## Principles
Confirmed: 1, 2, 4, 10, 11, 12. Partly: 3, 5, 7, 8, 9, 13. Not observed: 6.

## Velocity
- Build a reusable "pull taut" animation for BFS levels.
- Introduce new algorithms as a diff on prior ones the learner already did.
- Treat applications as an end-of-lesson transfer check: let the learner model the problem as a graph before the reveal.

Skeptical note: the strongest claims here rest on automatic captions at roughly 15 s granularity, so exact beat boundaries are approximate, and visuals (which carry much of the teaching) are inferred from narration only.

The strongest evidence for the video's pacing claim is in the beat list: note that the short runtime means principle verdicts for 6 to 9 are thin, with only one or two instances each.
