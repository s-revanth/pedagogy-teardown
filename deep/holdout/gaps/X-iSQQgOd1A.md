# Gap analysis: Coding Adventure: Ant and Slime Simulations (X-iSQQgOd1A)

Real length 1073 s (17:53). Captions manual. Predicted script: `scripts/X-iSQQgOd1A.md`. Note: the script's "explicit predictions" are in its section 4 (the brief says section 5); I scored those.

## 1. Real beat sheet (compact)

| m:ss | Type | Tags | Paraphrase |
|---|---|---|---|
| 0:02 | H | roadmap, second-person-role, story, humor | Today: ant and slime sims, but first a role-play as a cabbage merchant touring towns |
| 0:17 | H | brute-force-first, toy-world | Shows (admittedly confusing) recursive code that enumerates every route; 12 towns solve in about a second |
| 0:51 | B | failure-shown | Add a 13th town, runtime balloons; route count is (n-1)!/2, 20 towns means about 60 quadrillion |
| 1:27 | B | roadmap, generalize-to-other-domains | Approximate methods exist; he got curious about Ant Colony Optimization |
| 1:43 | N | analogy, minimal-definition-then-refine, notation | One virtual ant picks the next town; desirability is 1 over distance to a power; power sets how greedy it is |
| 2:28 | N | build-and-verify | Replays one ant's tour: poor, so add more ants |
| 3:04 | N | analogy | Score every ant's path; scores act as pheromone trails to bias the next round |
| 3:21 | N | build-and-verify, visible-repetition | Re-run the same 20 towns, slowed to show trails; about 50 ants find a good path in a split second versus centuries |
| 3:53 | N | honest-caveat, humor | No optimality guarantee; scales to 100 towns; shows best-so-far path |
| 4:10 | B | honest-caveat | Many parameters, trial and error to tune |
| 4:28 | H | story, failure-shown, humor | Pivots to a lighter, more visual ant sim: draws an ant, imports to Unity, something goes wrong, looks terrifying |
| 4:47 | N | build-and-verify | Ant follows a green dot (food) |
| 5:05 | I | brute-force-first, design-it-yourself | Ant code on screen; random nudge to heading for wandering; too indecisive so lower wander strength |
| 5:40 | N | build-and-verify | Add food sensing and pickup; test with one ant, then a bunch |
| 6:00 | B | generalize-to-other-domains, honest-caveat | Researches how real ants navigate home (desert species, polarised light, pedometer) but keeps it simple |
| 6:37 | N | design-it-yourself | Two pheromones, blue out and red home, idea taken from someone else's video |
| 6:54 | N | honest-caveat, failure-shown | Ants perform badly because following is not yet written |
| 7:10 | N | I | Three sample regions in front, turn left, straight or right plus noise; scheme borrowed from a slime-mould paper (foreshadows slime) |
| 7:28 | I | notation-after-concept | Code shown; pheromones decay for evaporation; wishes for diffusion but unsure how |
| 7:44 | N | build-and-verify | Quick trial run with a handful of ants, works roughly |
| 8:04 | N | failure-shown, humor | Obstacles via collision code he calls dubious; map generator rewritten from scratch, hours lost, own old code is bad too |
| 9:02 | N | humor, build-and-verify | Could have drawn the map in Paint; spawner for food; releases 500 ants |
| 9:46 | N | honest-caveat, generalize-to-other-domains | Cluster is harvested, trail lingers until it evaporates; real ants more sophisticated (pharaoh ants leave repellent) |
| 10:05 | B | story | Distracted by slime mould; second paper on pattern formation |
| 10:40 | N | roadmap, brute-force-first | Will do the slime as a GPU compute shader for scale |
| 10:58 | I | build-and-verify | Hash function as pseudo-random numbers; per-pixel test as brightness noise; checks bigger texture for repeating patterns |
| 11:48 | I | minimal-definition-then-refine, toy-world | Agent is only position plus angle; move, bounce at edge, write white pixel to trail texture |
| 12:27 | N | build-and-verify | Dull as expected; adds per-pixel evaporation, saying the viewer can guess the look but he shows it anyway |
| 12:44 | N | notation-after-concept | Diffusion as per-frame blur, crude average-of-neighbours code; easy because the map is an image |
| 13:21 | I | notation-after-concept | Three-sensor steering plus randomness; sense function sums texture values |
| 14:00 | N | build-and-verify, simulation-as-argument | First experiment at 320x180 with 250 agents, started in a circle facing inward; then about 2 minutes (to 15:59) with no narration while sims run |
| 15:59 | N | generalize-to-other-domains | Species mask in the agent struct; write to one colour channel per species; other species' trail counts as negative |
| 16:45 | N | humor | Third species, mutates a third of the agents; reflects on organic patterns from simple rules |
| 17:03 | H | honest-caveat, teaser-next | Much more to explore, other projects calling; links to others' work; cheers |

Proportions: Travelling-salesman / ACO opener 0:02-4:28 (25%), ant game 4:28-10:21 (33%), slime 10:21-17:20 (39%).

## 2. Prediction scorecard (script section 4)

| # | Prediction | Predicted | Actual | Verdict |
|---|---|---|---|---|
| 1 | First viewer question | none | none; opens with an a second-person role prompt (0:02) | hit |
| 2 | Self-directed rhetorical questions from about 3:10 | present | essentially none; narration is first-person "did X, then Y" devlog | miss |
| 3 | First code on screen | about 5:00, sensing | video's first code is TSP enumeration at 0:17; ant-sim code appears 5:05 (wander, not sensing) | near |
| 4 | Formulas | none | two: route count (n-1)!/2 at 1:06; desirability 1/d^power at 1:43 | miss |
| 5 | Misconception | none | none | hit |
| 6 | Brute-force-first | yes | yes: enumerate-all-routes 0:17, random wander 5:05 | hit |
| 7 | Dumb random-wander ant at 1:10 that fails to find food | 1:10 | wander at 5:05, one ant, tuned by a strength knob, not shown as a failure | near |
| 8 | CPU first, then GPU at 9:50 and 14:25 | CPU then GPU | slime is GPU from the start (10:40); no CPU version shown | miss |
| 9 | Example count | 4-5 | roughly 9 distinct setups (12/13/20/100 towns, 1 then many TSP ants, 1 then many game ants, 500 ants on map, noise texture, 250 agents, 2 then 3 species) | miss |
| 10 | Growth | tiny to bigger, one rule at a time | 12 to 100 towns, 1 to 500 ants, 250 agents, 2 then 3 species | hit |
| 11 | Hook type | project statement plus single toy dot | project statement then a second-person role scenario about an adjacent problem; no dot | near |
| 12 | Ending | wishlist, callback to ecosystem and opening dot, thanks to supporters, no recap | short note that there is more to explore, links to others' work, plain cheers; no callback, no thanks, no recap | near |
| 13 | Move: toy-world in first minute | one ant or agent | towns-on-a-map toy in first minute; first ant is virtual at 1:43 | near |
| 14 | Move: failure-shown | random wander fails, trails saturate | failures shown are factorial blow-up (0:51), Unity bug (4:47), own bad code (8:40); no saturation | hit (move), miss (instances) |
| 15 | Move: build-and-verify | same seed rerun | same 20 towns reused at 3:21; trial runs after each feature; hash noise check at 11:48 | hit |
| 16 | Move: design-it-yourself plus simulation-as-argument (slider grid) | grid of settings | only one knob (wander strength, 5:23); no slider grid; the parameter exploration is unnarrated (14:15-15:59) | miss |
| 17 | Move: honest-caveat | present | 3:53, 4:10, 7:44, 9:46, 12:44 | hit |

**Hit rate:** 7 hit, 5 near, 5 miss of 17 = 41% strict, 56% counting near as half.

## 3. Structural alignment

Predicted and present: single-ant-first start (loosely), random wander, two pheromones (6:37 vs 3:10 predicted), three sensors (7:10 vs 3:55), sensing code (7:28 vs 5:00), evaporation (7:28 vs 7:10), honest "real ants are more complex" aside (9:46 vs 8:50), pivot to slime (10:21 vs 8:50), minimal slime agent (11:48 vs 9:15), blur plus decay (12:44 vs 10:35), species (15:59 vs 15:30), close (17:03 vs 17:10).

Predicted but absent (false positives): "ants almost never find food" failure (1:55); marker saturation failure (6:25); moving food mid-run to show re-routing (8:00); CPU slow then GPU (9:50, 14:25); thin-trail speckle failure; collapse-to-blob and "veins vs cells" admission (12:40); slider grid for sensor distance, angle, turn speed (11:30); three start positions (13:30; only one start, circle inward); interactive image tracing and 3D mention (16:30); callback to the opening dot and ecosystem video; supporters thanks.

Present but unpredicted (false negatives): the whole 0:02-4:28 travelling-salesman and Ant Colony Optimization opener (25% of runtime), including a role-play hook, factorial cost number and the desirability formula; Unity/animation art asset and the terrifying bug; wander-strength tuning; collision code and map-generator rewrite; Paint joke; research asides on desert and pharaoh ants; ideas borrowed from a video and two papers; the hash-function RNG test; per-feature wishing for diffusion without knowing how then payoff at 12:44; about 2 minutes of unnarrated slime run; the closing links to others' work.

Timing drift on the big moments:
- Hook: predicted 0:00 one-ant project statement; real 0:02 project statement then merchant scenario. Time hit, content miss.
- First new idea: predicted pheromone marker at 2:30; real ACO virtual ant 1:43 and pheromone-as-score 3:04 (inside the TSP detour); ant-sim pheromone 6:37. Near for the first, +4:07 for the game sim.
- Payoff: predicted trails converging at 8:00; real harvested cluster 9:46 (+1:46). Slime payoff predicted at 10:35; real 14:00-15:59 (+3:25).
- Ending: predicted 17:10; real 17:03 to 17:20. Hit.

## 4. Gap taxonomy

| Miss | Class | Reasoning |
|---|---|---|
| 25% runtime opener on TSP / ACO with role-play hook, brute-force code first | missing-rule | Report says hook is a project statement and the first minute is one toy object; nothing about opening with an adjacent classic problem. |
| Failure-fix chain (saturation, CPU slow, thin trail) absent; features arrive as next step | wrong-rule | Theory 1 (failure-gated vocabulary) and arc steps 3 and 6: evaporation (7:28), diffusion (12:44), species (15:59) arrive with no preceding failure. Closer to need-gated or paper-gated. Report's own section 1 and Section 6 devlog caveat is not tied to this video type. |
| Formulas at 1:06 and 1:43 before the demo | wrong-rule | "The equation is a label for something already working" and "notation only after the behaviour". Here cost and desirability formulas precede the run. |
| Code at 0:17 before any concept | underspecified | Notation-after-concept does not say that deliberately dumb baseline code can appear first as the thing to be beaten. |
| Ant-sim ideas borrowed from papers and videos, named at the point of design | underspecified | Principle 12 (outside sources) says "confirmed" but gives no trigger or count; real use is design provenance at 6:37, 7:10, 10:21, plus fun-fact asides at 6:19 and 9:46. |
| Slider grid and start-position comparisons absent; instead a 2 min unnarrated run | topic-conditional / missing-rule | "Simulation-as-argument" is in the report with a fluids example; here the exploration is silent and visual. Report lacks "let-it-run". |
| Humor: cabbages, mock-excitement aside, Paint, terrifying ant | voice/craft | Report counts humor (9/12) but gives one example and no type. Real type is dry self-deprecation about process. |
| CPU-then-GPU | generator-error | Report gave no basis; generator invented it from general subject knowledge. |
| Teacher-voice narration and supporters thanks | generator-error / voice | Report says plain-spoken devlog; generator wrote a lesson. |
| Ending without callback | generator-error (mild) | Report says "rarely recaps"; callback present in 8/12 but optional. |

## 5. Overfit check

- "First minute is one circle / one bunny / one dot" (arc step 1): does not hold; first minute is a human role-play on an adjacent problem.
- "Failure-gated vocabulary" (theory 1) as a universal: holds for the memory, chess and neural-net videos; here three of five rules arrive ungated.
- "Equation is a label for something already working" (theory 2): contradicted for cost and selection formulas.
- "Fixed test choreography" (theory 3): holds only loosely (same 20 towns at 3:21).
- "One knob, one cause" (theory 6): present once (wander strength 5:23) but the slime sliders are not narrated.
- "Ecosystem as the compressed form of the arc": this video is a devlog, closer to the geography and vacuum cases (report section 2, last sentence).
- Holds well: honest-caveat, build-and-verify, hook-without-question, no misconception, toy-world loosely, no lesson recap.

## 6. Proposed rule changes

1. **Open with an adjacent classic problem when the project borrows from one.** Trigger: Coding Adventure whose method is derived from a known algorithm (ACO, here). Action: spend up to about 4.5 min (25% of runtime) on a second-person merchant scenario, a deliberately brute-force code listing that solves it for 12 items in about a second, then add one item to show the blow-up, with a stated human-scale number (60 quadrillion; centuries). Then pivot by saying the detour sparked a lighter, visual version. Evidence: 0:02, 0:17, 0:51, 3:53, 4:28. Channel-specific, with a universal sibling (quantify the blow-up with a human-scale number).
2. **Replace failure-gating with a "next feature" chain when the next rule is obvious.** Trigger: the next rule has an expected effect the viewer can guess (evaporation, blur). Action: add the rule with one sentence (a one-line aside that the viewer can guess the look), skip the failure demo; keep a visible failure only when surprising (Unity bug 4:47) or costly. Also state a deferred feature as a gap (admit he does not yet know how to do diffusion) and pay it off later (7:28 to 13:01). Evidence: 7:28, 12:27, 12:44, 13:01. Channel-specific.
3. **Cite the design source at the decision.** Trigger: a design choice not derived on screen. Action: name its origin (paper, video, tutorial) in one clause at the moment of choice, and add a real-world real-ants-are-more-complex fact after the sim works (target 2-4 per devlog). Evidence: 6:19, 6:37, 7:10, 9:46, 10:21. Likely universal (principle 12 gets a trigger).
4. **Split notation timing by kind.** Trigger: a cost or selection formula that justifies the failure or the model (factorial count, 1/d^power). Action: say it before the demo within one sentence of the concept; keep "formula after code works" for model equations. Brute-force baseline code may precede its concept as the thing to beat. Evidence: 0:17, 1:06, 1:43. Likely universal.
5. **Let-it-run payoff.** Trigger: last rule added in a sim video. Action: after one sentence setup, show 1-2 min of unnarrated runs with different settings and start states, then return with a single extension recipe (add a field, route it to a channel, flip the sign) in about 30 s. Evidence: 14:00-15:59 then 15:59-16:45. Channel-specific, plausibly cross-channel for sim-heavy videos.
6. **Humor spec.** Trigger: any hard-won or failed step. Action: one dry self-deprecating aside, about every 2-3 min (3:53, 4:28, 8:23, 9:02), never a standalone joke. Channel-specific.

## 7. Scores (1-5)

- Arc fidelity: 2. Right two-phase ant-then-slime-then-species shape and ending time; wrong opener, no failure chain.
- Move-inventory recall: 3. Common moves present; missed role-play, outside citations, silent run, deferred feature.
- Move precision: 2. About half of predicted beats are false positives (saturation, CPU-to-GPU, grid, start positions, callback).
- Pacing/timing: 2. Late events drift by 2-4 min because a 4.5 min opener was absent from the prediction.
- Voice: 2. Predicted a lecturing voice; real is dry first-person devlog.
- Overall regenerate: 2. A reader would get a plausible ant/slime video, not this one.

Quote (3:53, six words): "please try to contain your excitement".
