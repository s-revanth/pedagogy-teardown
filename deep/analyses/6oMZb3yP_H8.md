# How Computers Draw Weird Shapes (Marching Squares) — Reducible (6oMZb3yP_H8)

## Structure arc
Hook (merging metaballs, 0:00) -> admitted confusion and easy frames (1:47-3:12) -> implicit functions via circle/ellipse (3:25) -> pivot to a *harder* general problem (4:48) -> sampling game and sign-change insight (5:55-9:37) -> grid cell cases, quiz, lookup table (10:04-14:49) -> linear interpolation (15:30) -> formal name and parallelism (17:16-20:09) -> callback to metaballs via energy fields and electric potential (20:24-24:13) -> 3D marching cubes (24:56) -> personal learning story (26:02). The algorithm is named only at 17:16, after every piece has been built.

## Strongest moves
1. **Presenter admits being stuck (2:02-2:30).** He asks viewers to study the animation, then breaks the "reveal" convention: he doesn't know either. He backs off to "which frames are easy?" This models how to work when you're stuck rather than performing mastery.
2. **Generalize to a harder problem (4:48-5:55).** He states the heuristic outright: sometimes the more general question (render any f(x,y)=c) is the one that makes progress possible. The metaball question is parked for 15 minutes.
3. **Brute force that becomes the insight (6:23-7:34).** Random threshold sampling fails. Binary coloring at 1k, 10k and 20k samples makes the contour appear without being named. The learner sees the sign-change boundary before hearing it as a principle (8:15).
4. **One idea at growing scales.** The bracket-and-bisect idea is applied to a point pair (8:30), then a cell edge (11:25), then the whole grid. Interpolation (15:30) swaps out only the bisection step. Two worked cells come before the 16-case exercise (12:35), and the symmetry grouping comes after it (13:28).
5. **Motivate before formula (21:05-23:06).** He withholds the metaball function, builds energy fields and constructive interference, links to equipotentials from physics, and only then asks "can you guess?" 1/r arrives as a confirmation.

## What's unusual
The meta-narrative is about problem-solving posture: wishful thinking is labelled as wishful thinking (4:48), and the closing story says building beats lectures (26:57). Honest caveats are frequent and well placed: sign convention (9:37), saddle ambiguity (14:07), and the polynomial approximation used in practice (24:27). Notation is light. Only three formulas appear, and the interpolation algebra is waved away (17:02).

## Principle verdicts (brief)
Confirmed: 1, 5, 6, 7, 9, 10, 11, 12. Partly: 2 (few symbols, but some algebra is skipped), 4 (the analogy comes late, as motivation rather than as an entry point), 8 (the idea rate slows at the single cell; there is no wpm evidence), 13 (it explains why interpolation, but not why the polynomial). Not observed: 3.

## Velocity implications
- A "generalize-then-return" playbook with an explicit parked-hook state and a callback recap beat.
- Progressive sampling simulations where a pattern emerges as N grows, with naming held back until after the reveal.
- Scripted "I'm stuck too" voice beats that model retreating to an easier question.
- Exercise gating: worked examples, then a learner attempt, then the symmetry compaction. If the learner struggles, reorder.
- Eval rule: formula reveals should come after an intuition beat and a guess prompt.
