# A* Pathfinding E01 (Sebastian Lague, 11 min)

## Arc
Roadmap (0:01), grid and distances (0:21-0:53), three animated runs (1:12-7:29), pseudocode (7:45-10:33), brief sign-off. No hook question, no analogy, no stakes. The video starts with the toy world and stays in it.

## Strongest moves
1. **Empty grid first (1:12-2:50).** G, H and F are introduced on a map with no obstacles. The learner sees F stay constant as G rises and H falls, so the path runs straight. This is the key to the later optimality claim.
2. **Rerun with obstacles (2:50-5:44).** The same procedure with obstacles added. F values now climb whenever the path leaves the straight line, so other nodes get explored. The video says outright that this is why the result is guaranteed shortest (5:44).
3. **Scaffold swap (6:01-7:29).** The third run hides G and H and shows parent arrows. The learner must reuse the earlier model and gets a new concept (parent pointers) for free. Arrows only repoint on a better path.
4. **Visual before code (7:45).** The pseudocode comes last, with colour references back to the animation: green means open, red means closed.
5. **Design-it-yourself numbers (0:37-0:53).** Distance 1, diagonal sqrt2, then 10 and 14 for integers. The cost units come from the learner's own geometry.

## Unusual
- Pure demonstration, no learner questions, and no analogy or misconception. Rigour comes from repeated observation.
- Honest scoping: "not much to say" during repeated steps (5:09). It lets the repetition do the teaching.

## Principle verdicts
Confirmed: 2, 3, 5, 7, 9, 10, 11. Partly: 1, 6, 8, 13. Not observed: 4, 12. Principle 8: speech steady; idea rate slows at ties and updates.

## Velocity implications
- Build scenes as run-1 trivial, run-2 with complication, run-3 with a changed overlay.
- Ghost hands should mark the next-picked node so learners predict before it moves.
- Delay code or notation until the learner can narrate a run.
- Insight placement: the "flat F" observation is a cheap, early, checkable claim; eval for it.
