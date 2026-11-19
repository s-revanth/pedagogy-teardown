# Polishing and Releasing My Tiny Geography Game (Sebastian Lague, 26 min)

## Arc
A devlog. Feedback list (0:01), compass maths (0:17-3:59), map detour (3:59-6:05), globe and Antarctica reprojection (6:05-10:13), terrain rewrite (10:52-13:09), lights, stars, rim light (13:09-17:02), balloons, speed, Paris experiment (17:21-23:51), release. Not a lesson.

## Strongest moves
1. **Build-and-verify (1:58).** He says he trusts his code little and his maths less, so builds a test with arrows pointing at a target. The learner sees correctness checked, not asserted.
2. **Curious detour with payoff (4:15, 10:13).** The flat-map shortest-path experiment is introduced as a sidetrack, then reused for the landing arc.
3. **Shown failure (8:20, 14:01).** A radians bug gives a nauseating view; the lights parameter was 10 not 100. Failures are narrated as normal.
4. **Parameter sweep (14:17-14:49).** Iteration count 0, 10, 200 side by side makes the effect of one number visible.
5. **Slider-driven reprojection (6:36-7:49).** Antarctica splits, climbs and reforms; the sliders explain the shader better than words.

## Unusual
- Aimed at viewers who follow the project, so little new vocabulary is introduced.
- Cross product and Slerp get one sentence each (0:49, 4:35). The maths is the weakest teaching here.
- Humour as pacing; the sidetrack at 21:40 invites viewer ideas.

## Principle verdicts
Confirmed: 1, 5, 12. Partly: 2, 4, 7, 8, 9, 11. Contradicted: 13 (maths). Not observed: 3, 6, 10. Principle 8: speech steady, ideas dense in maths (0:49) and sparse in demos.

## Velocity implications
- Offer "test it visibly" and "sweep the parameter" scenes as stuck-learner remedies.
- Orchestrator: support detours that are tagged and called back.
- Do not copy the one-sentence cross-product treatment; stepping stones missing.
- Failure narration is a cheap trust-builder in voice scripts.
