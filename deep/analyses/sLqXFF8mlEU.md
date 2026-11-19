# I Tried Creating a Game Using Real-World Geographic Data (Sebastian Lague)

## Arc
This is a build log, not a lesson. Hook is an old unfinished project (0:01); cube-to-sphere (0:32), heightmap and lat/long (1:57), sea level slider (4:28), player controller (6:14), culling (7:28), normal maps (8:26), country outlines (10:09) and highlighting (13:05), ocean and foam (15:42), boats (17:56), clouds (20:05), shadows (24:09), delivery gameplay (27:22), reflection (28:42). Each step is motivated by what the previous output lacked.

## Strongest moves
1. Visible debugging (1:25, 22:58, 24:26): the broken output (lumpy sphere, inverted clouds, upside-down shadows) is shown before the fix. It builds trust and shows the real texture of the work.
2. Slider as discovery (5:26): lowering sea level makes islands merge and depth emerge without explanation. The one clear learner-discovers moment.
3. Minimal definitions at point of need (1:07 normalize, 7:28 frustum culling, 8:26 normal vector): one sentence, followed immediately by a use.
4. Brute force first, honestly flagged (12:10, 17:19): slow per-pixel loops over all countries and iterative distance field, with a faster method (jump flooding) deferred.
5. Deliberate skip with pointer (0:47, 13:36, 16:13): says what he omits and where to learn more.

## Unusual
Heavy on curiosity detours (geology at 3:50, 7:12; Vostok at 11:38). Gameplay arrives last and the ending admits the game is more fun to build than play. Code is shown briefly, often skipped; explanation of how things work is thin (the shadow transform is not derived, 24:26). There is almost no repetition or analogy.

## Principle verdicts
Confirmed: 6, 11, 12. Partly: 1, 2, 5, 7, 10, 13. Contradicted or not observed: 3, 4, 8 (idea rate does not slow for hard material; 'not terribly interesting' skips), 9. Explicitly a poor model for beginner pacing.

## Velocity implications
- Voice and orchestrator can adopt the "say what I'm skipping and where to look" move for depth the learner has not asked for.
- Scene builder: expose one slider on one parameter so the learner discovers the effect (sea-level pattern).
- Show the buggy output before the fix when the bug is instructive; it lowers the learner's fear of mistakes.
- Curiosity detours tied to the visual are good for rapport but should be capped by learner state.
- Evals: do not reward build-log style as a teaching standard; it lacks repetition, analogy, and pacing control.
