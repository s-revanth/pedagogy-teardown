# Trying to Improve My Geography Game with More Real-World Data (Sebastian Lague, UXD97l7ZT0w)

## Arc
A loosely chained devlog of about 36 minutes. Crash on other machines (0:20) -> bake and rescale textures (1:20-2:33) -> Eye of the Sahara detour (3:25) -> map tiles onto a cube-sphere (5:56) -> city lights as instanced points (8:40) -> mesh simplification (12:05-17:09) -> wind particles (17:09-20:29) -> moon, orbit maths, analemma (21:07-28:34) -> stars (28:53) -> atmosphere rewrite (29:46) -> fly-through and release plans (32:41).

## Strongest moves
1. **A single knob that shows cause (14:52).** For mesh simplification he sets error threshold to zero, then raises it a little: the ocean loses points first. Raising it more removes more. The learner sees the trade-off between detail and performance without any slide.
2. **Ablation by toggle (27:59-28:34).** Trace the sun by day to get the analemma, switch to a circular orbit and the lobes balance, set tilt to zero and the figure collapses to a point. Each cause is attributed to its visible effect.
3. **Failure first, then the clean idea (13:04-14:03).** Three attempts yield nonsense, the grind is skipped, then the working rule appears: error = height minus neighbours' average; keep the point if above threshold. A good example of dumb-first and honest storytelling.
4. **Sanity checks against reality (19:56, 29:46).** Cyclones rotate counterclockwise in the north; the north star is where it should be. This is how he builds trust in his own code.
5. **Layer-peeling (32:08-32:24).** Atmosphere light alone, transmittance alone, terrain alone, then combined.

## Unusual
Candid limits: bakes a result rather than optimizing (1:00), does not understand the camera jitter fix (8:20), skips streaming, ignores gameplay (34:14). The orbit section (23:14-25:53) is the most explainer-like: periapsis and apoapsis define the ellipse, Kepler's equal-area fact becomes an equation with no closed form, then Newton's method guesses toward zero and he points to another video for how. Rigor arrives quickly, with little concept build-up for equation notation (24:21-25:00).

## Principle verdicts
Confirmed: 6, 9, 10, 12. Partly: 1, 2, 4, 5, 7, 11, 13. Not observed: 3, 8.

## Velocity implications
- Parameter sliders with ghost hands sweeping them while the voice states the effect.
- Add external sanity-check beats after builds.
- Toggle-ablation and layer-peeling modes in the scene builder.
- Evals for term-before-use and for undisclosed skipped steps.
- Voice may say "I do not fully know why", labelled as such.
