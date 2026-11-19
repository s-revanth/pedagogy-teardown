# GJK algorithm (Reducible, 32 min)

## Arc
Hook problem (0:00), promise of a "roller coaster" (1:36), shapes (2:04), infinite points (3:15), Minkowski difference (3:57), support functions (8:51-12:47), bird's-eye GJK (13:29-16:45), five open questions (16:59-26:06), implementation (26:06), recap of three shifts (29:24).

## Strongest moves
1. **Reframing chain (3:15-5:38).** Intersection becomes shared point, then difference at origin, then origin inside Minkowski difference. Each step is a one-line commit with a check against the definition, and the recap at 29:24 names these as the "shifts".
2. **Thought experiment as brute force (3:15).** An imagined machine with infinite point sets makes the idea natural; the infeasibility (5:52) then creates the need for sampling and support functions.
3. **Two-pass explanation (13:00-26:06).** First, a bird's-eye pass with intersecting and non-intersecting runs (13:29-16:30), then the explicit list of five unanswered questions (17:14-17:40) and each is answered in order. Learners know what they have not yet earned.
4. **Region elimination quiz (21:49-25:54).** Seven Voronoi regions; asking "how many do we need to check" and answering by reasoning from how point a was found (two) is the key insight, framed as surprising.
5. **Shape-agnostic payoff (12:33, 30:05).** Only a support function per shape is needed, so circles and polygons are handled uniformly; named as the most brilliant component.

## Unusual
Tone management: "give yourself a pat on the back" (16:45), "take your time" (29:09), and jokes about the paper being a cipher. Lengthy without a sponsor.

## Principles
Confirmed: 1, 2, 6, 7, 8, 9, 10, 11, 13. Partly: 4, 5, 12. Not observed: 3.

## Velocity
- Dense topics: bird's-eye first, open-question list, then close each.
- One reusable shape pair across scenes.
- Insert explicit regulation lines when idea rate peaks.

Skeptical note: the strongest claims here rest on automatic captions at roughly 15 s granularity, so exact beat boundaries are approximate, and visuals (which carry much of the teaching) are inferred from narration only.
