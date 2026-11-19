# Simulating the Evolution of Rock, Paper, Scissors (PrimerBlobs, tCoEYFbDVoI)

## Structure arc
Hook with a game everyone knows (0:00), honest caveat plus real-world anchor in side-blotched lizards (0:15-1:05), rules and a reward table (1:05-1:57), then a long experiment ladder: pure strategies -> bigger world -> mutation -> softer payoffs -> tie cost -> mixed strategies -> mixed plus tie cost -> special starting populations. Ends on naming the evolutionarily stable strategy (14:26), then Patreon. No recap.

## Strongest moves
1. **Predict before every run (1:57, 4:53, 6:15, 8:42, 9:38, 11:43, 12:51, 13:54).** Eight-plus commit-to-answer prompts. At 9:38 the narrator coaches the viewer directly: passive watching teaches less than predicting.
2. **Interface earned by pain (2:45-4:37).** The bar graph shows one instant and runs look "random"; the ternary plot is then built from a Cartesian paper-vs-scissors graph (corners, edges, interior, outside), then rotated 30 degrees. The presenter admits it first felt like cheating (3:01).
3. **One-knob ladder.** Each simulation changes exactly one variable, so each outcome is attributable. Repeated outward spirals let the viewer infer that matrix *structure*, not magnitude, matters, which is then stated at 9:06.
4. **Theory after the fact (6:50, 7:06, 12:34, 14:10).** "You could have seen this in the matrix" comes after the sim, and Nash, weak Nash, and ESS each arrive as labels for something already observed. Nash is explicitly flagged as optional jargon.
5. **Presenter was wrong (12:51).** He expected browns to dominate with tie penalty, was confused live on Twitch, and the sim showed whole-population balance instead.

## Unusual vs other explainers
Almost no equations. The simulation is the argument, and the viewer is cast as an experimenter. The lizard callback (10:22) closes the opening hook with field data, and notes honestly that the real matrix is asymmetric.

## Principle verdicts
Confirmed: 1, 2, 3, 5, 6, 7, 9, 10, 11, 12. Partly: 4 (the analogy grounds the idea but never bridges to formalism), 8 (the ternary segment slows idea rate, about 95 s on one interface), 13 (tool choice justified at 2:45, but the calculation is skipped at 10:05).

## Velocity implications
- The orchestrator should run one-knob ladders and tell the learner model which variable changed.
- The voice layer needs a built-in predict-pause before each sim; evals should score whether predictions were collected.
- The scene builder should animate interface upgrades (Cartesian -> ternary rotation) instead of cutting to a new chart.
- Withhold formal names until after the phenomenon. Mark them optional for novices.
- Script occasional presenter-was-wrong beats to normalize being wrong.
