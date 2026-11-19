# I Spent a Week Making a Game about Vacuuming (Sebastian Lague, PGk0rnyTa1U)

## Arc
This is a devlog, not an explainer. A confession about unfinished projects (0:01) -> a rule of one week then publish (1:25) -> game idea from GPT-3 (1:42) -> vacuum hose with FABRIK (2:41) -> cable fails with the same method (4:14) -> Points-and-Sticks rope (4:43) -> cloth cape (7:30) -> dust with GPU instancing (8:55) -> compute shader suction and density map (10:11) -> floorboards, models, ghosts (11:21-13:28) -> commissioned song (13:46) -> over-scoping postmortem (15:47).

## Strongest moves
1. **Reuse a tool, show it fail, then replace it (4:14-4:58).** FABRIK works on the hose, looks bad on the cable, so he introduces a different structure. The learner sees what FABRIK is bad at before meeting the alternative.
2. **Tiny primitives, built in order (4:58-6:52).** Point (position, previous position, lock), then Stick (keep two points at their starting distance), then a per-frame step (keep moving, add gravity, record previous), then the constraint pass. Each piece gets one reason before the next.
3. **Fix by repetition (6:14-6:29).** Correcting one stick breaks its neighbour, so run the constraints many times. The insight is stated in one breath and confirmed by running the simulation.
4. **Same primitive, new domain (5:18, 7:13, 7:49).** Rope, power cable, then cloth grid with deletable sticks. The generality of the idea is shown by reuse.
5. **Radical honesty (3:38, 8:39, 15:47).** Code he admits is unoptimised, built-in cloth swapped in at the end, and a game that is fun for two minutes. It keeps scope believable.

## Unusual
FABRIK is introduced (2:59) as a ready definition and code with no analogy; the pedagogy is much weaker there than in the rope. The long song and art segments (13:46-17:39) are essentially entertainment and take about a fifth of runtime. It stays easy to follow because each section is a single small problem with a visible result.

## Principle verdicts
Confirmed: 9, 10, 12. Partly: 1, 2, 5, 6, 7, 11, 13. Contradicted: 4 (no analogy before FABRIK or instancing). Not observed: 3, 8.

## Velocity implications
- Playbook candidate: "try it with last tool, watch fail, introduce new tool".
- Hold one primitive on screen and vary the scenario to teach transfer.
- Add explicit scope-skip lines in the tutor's voice.
- Evals: flag code-first explanations lacking an analogy or brute-force lead-in.
- Learner model: remember where a primitive was first seen to schedule transfer examples.
