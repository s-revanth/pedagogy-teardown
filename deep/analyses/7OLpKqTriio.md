# Epidemic, Endemic, and Eradication Simulations (Primer)

## Arc
Roadmap of three phases (0:00), a toy city with SIR-colored blobs (0:15), a first run read with concrete counts (1:24), then R-naught, R, herd immunity (1:24-3:34). Parameter sweeps at 4:08 and 5:05, endemic phase via lifespans at 7:02, herd threshold formula at 8:48, vaccination test at 9:59, donation outro.

## Strongest moves
1. **Symbols as patches (2:47).** R-naught assumes everyone is susceptible. The sim visibly slows, so the factor S is added to make R. Logistic growth is named and explicitly deferred (3:02).
2. **Expected-vs-actual gap (2:14).** The R-naught prediction and one run disagree. The video says this messiness is why it likes simulations, and links it to real uncertainty about COVID.
3. **Predict then batch (5:35, 10:33).** Four variants run together after the viewer is asked for predictions. Discovery: peak and total infected barely change when only period or population change at fixed R-naught (6:14).
4. **Presenter was wrong (10:33).** He admits he expected 50% vaccination to eradicate. The gap between the vaccination floor and the herd threshold explains why it does not.
5. **Misconception near the start (3:34).** Herd immunity is not a cap: 41% infectious at peak, 85% ever infected.

## Unusual
Heavy honest-caveating (0:55, 9:20, 11:28), and formula derivation (1 - 1/R0 at 8:48) lands after the behavior is already seen. Long silent run segments carry the argument.

## Principle verdicts
Confirmed: 1, 2, 5, 6, 7, 9, 11, 12. Partly: 4, 8, 10, 13. Not observed: 3. On 8, the transcript shows no speech-rate data, but idea density visibly rises around 1:24-3:34 and falls during sims.

## Velocity implications
- Support four-run parameter grids with a prediction pause.
- Introduce a symbol only after a frame shows the prior one failing.
- Let the tutor report its own wrong expectation.
- Log predictions vs outcomes in the learner model to pick the next parameter.
