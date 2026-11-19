# Collision simulations (Reducible, 28 min)

## Arc
Show the finished 250-particle sim (0:00) and roadmap, then frames (1:13), one particle (2:40), tunneling and continuous detection (6:50-11:27), two particles (11:39), scaling (13:02) with all-pairs, sweep and prune, uniform grid, kd-tree, BVH, then recap (27:05).

## Strongest moves
1. **Frames first (1:13).** Two animations at 15 and 60 fps are compared; the whole video's frame-by-frame view is justified experientially.
2. **Smallest world first (2:40-5:39).** One particle in a box; each of dynamics, detection, response gets one short beat, and caveats (elastic, infinite wall mass at 4:57) are stated openly.
3. **Failure then two fixes plus a hard one (6:50-7:57).** Tunneling is shown ("pretty ugly"), cheap fixes are named, then continuous detection is set up by parameterising with t and solving to tc=0.23 (10:03).
4. **Cost made felt (13:31-14:26, 18:24-18:51).** All pairs means 5000 tests per frame, 18M per minute, and 1h40m on the author's laptop; sweep and prune brings it to 3 minutes.
5. **Chain of tradeoffs (19:06-25:24).** Grid (memory versus checks), kd-tree (balanced, but objects span cells), BVH (no overlap of objects, boxes may overlap). Each structure ends with its weakness, and the next begins from it.

## Unusual
Admits skipping the two-particle derivation and says physics is rusty (12:35-12:48), linking an external source instead. A long list of structures is made coherent by the broad/narrow/solve frame (14:55), after which the video says which phases are already covered.

## Principles
Confirmed: 1, 5, 6, 9, 10, 11, 12. Partly: 2, 7, 8, 13. Not observed: 3, 4.

## Velocity
- Show naive cost as a counter on screen, then re-run per optimisation.
- Keep the same scene across techniques.
- Template: technique, when it wins, when it fails.
- Allow "skip derivation with link" for low-math learners.

Skeptical note: the strongest claims here rest on automatic captions at roughly 15 s granularity, so exact beat boundaries are approximate, and visuals (which carry much of the teaching) are inferred from narration only.
