# Coding Adventure: Simulating Fluids (SebastianLague, 48 min)

## Arc
One circle falling under gravity (0:01), then a grid of particles that collapse (2:10). Problem named, goal deliberately lowered to a rough starting point (2:44). Density via smoothing kernel (3:05), kernel volume fix (6:13), abstract-function detour (8:42), gradient by brute force (11:57), fast gradient, caching (15:02), pressure (15:40), debugging, Newton's third law (21:08), spatial hash (22:36), look-ahead (28:21), viscosity (33:50), near pressure (37:27), GPU and bitonic sort (39:56), 3D (44:37), wishlist (46:51). It is a build diary where every concept appears because a visible failure demands it.

## Strongest moves
1. **Failure as the motivator (2:10, 5:57, 21:08).** Collapse, density explosion when the radius grows, and the sim getting worse over time. Each shows the symptom, then derives the fix. The radius test is a misconception-first beat: he states blur should not change density, shows it does, then reasons with a heights-times-area picture to normalise the kernel (6:31-7:26), and verifies with a constant 187.
2. **Abstract test-bed detour (8:42-11:57).** When confused he steps away from the fluid to a meaningless 2D function approximated by particles. The core SPH equation (11:07) arrives after the code has already produced it, and is then sanity-checked by substituting density for the property (11:39).
3. **Brute force first, then speed-up with timing (11:57-15:21).** Finite-difference gradient takes 20 s, analytic slope 5 s, cached densities 18 ms. He says he should have cached first. Honest, and the numbers are the argument.
4. **Hash grid on a ten-slot example (23:48-26:24).** Tiny worked array, key, sort, start indices, one lookup walkthrough, then admitted collision cost.
5. **Parameter grids as evidence (29:41, 35:53).** Side-by-side runs across timestep and viscosity values let the learner see the trend rather than being told.

## Unusual
Narrates his own confusion (maths over his head, trial-and-error with signs). Sign errors are left in. Navier-Stokes appears only at 33:50 as a map of work already done, the opposite of the usual order. Caveats are constant (gas-like pressure, jelly bounce, finicky settings).

## Principle verdicts
1 confirmed. 2 confirmed (notation after working code). 3 partly (recurring UI). 4 partly (blur and heights-as-volume analogies). 5 confirmed (ball of water; sorting acted pair by pair). 6 confirmed. 7 confirmed. 8 partly: idea rate, not speech rate, varies; transcript cannot show wpm. 9 confirmed. 10 confirmed. 11 confirmed. 12 confirmed. 13 partly.

## Velocity implications
- Scene builder: a break-it-first mode where the failing sim is kept for before/after comparison.
- Orchestrator: stepping-stone detour (abstract function) when the real problem tangles, with a callback.
- Voice: allow "should have done this first" admissions; tag them for evals.
- Ghost hands: drive sliders and side-by-side parameter grids.
- Learner model: show the equation only after the learner has seen it work; verify with a special case.
- Evals: notation after visual; every simplification paired with a caveat.
