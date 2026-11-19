# Predicted script: Coding Adventure: Ant and Slime Simulations

- Channel: SebastianLague
- Title: Coding Adventure: Ant and Slime Simulations
- Target duration: 1074 s (17:54)
- Recall risk: vague. I know in general terms that this title exists and that "slime" probably means agents that follow a chemical trail. I do not recall its structure, order, numbers or lines. Everything below is built from the channel report plus general subject knowledge (pheromone trails, agent-based sims, GPU parallelism). Any resemblance to the real video's details is a guess.

## 1. Predicted beat sheet

| Time | H/B/N/I | Move tags | Narrator says / does | On screen |
|---|---|---|---|---|
| 0:00 | H | roadmap, story, toy-world | Project statement: ants are fascinating, today I try to simulate how a colony finds food. Starts with one ant. | A single dot (ant) on a dark canvas, a circle for the nest |
| 0:35 | H | toy-world, minimal-definition-then-refine | An ant is just a position and a direction; it walks forward each frame. Minimal definition only. | Dot with a small heading line, moving in a straight line, then bouncing off the edges |
| 1:10 | H | brute-force-first, build-and-verify | Dumbest version: each ant wanders randomly, nudging its angle a little each frame. Drops a few food blobs and runs it. | 100 dots leave the nest and drift randomly; food blobs sit unvisited |
| 1:55 | H | failure-shown, honest-caveat | They almost never find food, and when one does it has no way to tell the others. "Obviously that is not what real ants do." | Counter of food returned stays near zero; clip speeds up |
| 2:30 | B | minimal-definition-then-refine, analogy | Real ants leave chemical markers. Smallest repair: the ant drops a marker on the ground while walking. Brief mention that this is pheromone. | Ants paint a faint dot behind them on a trail layer drawn as a coloured grid |
| 3:10 | N | design-it-yourself, special-case-first | Which marker? Ant that is looking for food should leave a "path home" marker; once it has food, a "path to food" marker. Two markers, two states. | Ants change colour when carrying food; two trail colours, one per state |
| 3:55 | N | act-it-out, design-it-yourself | How does an ant read the markers? Three sensors in front (left, centre, right); it turns toward the strongest reading. Asks himself what knob is missing: sensor angle, distance. | Close-up of one ant with three circles ahead, glowing by how much marker is under each |
| 5:00 | I | notation-after-concept, build-and-verify | Only now shows the code for sensing: sum the marker values in a small area, compare three numbers, turn. Hand-sets weights to test. | A short code snippet beside the sim, three numbers updating live |
| 5:40 | N | build-and-verify, visible-repetition | First real test: one food source, same nest, same starting seed. Trails begin to form and ants start returning with food. | Lines of ants between the nest and the food; counter rises |
| 6:25 | N | failure-shown | New problem: markers never go away, so old paths stay forever and ants circle in trails of their own; the picture saturates to blobs. | Trail layer turning solid; ants spiralling in a clump |
| 7:10 | N | minimal-definition-then-refine, simulation-as-argument | Fix: markers evaporate a little every frame. Same test, slider for decay rate: too low saturates, too high loses the trail. | Evaporation slider swept while the same scene replays; side-by-side comparison |
| 8:00 | N | build-and-verify, humor | Trails now converge on the shortest path as longer ones fade. Moves the food mid-run to see the ants re-route. A little joke about ants being confused. | Food blob dragged away; old trail fades, new one grows |
| 8:50 | B | honest-caveat, roadmap | Caveat: real ants are more complicated, mine are simplified. Then pivot: stripped further, this simpler idea (just agents following a trail) makes beautiful patterns. This is the "slime" half. | Ants fade out; fresh canvas, one tiny agent |
| 9:15 | H | toy-world, minimal-definition-then-refine | Slime agent: position, angle, one trail. Every step it moves forward and leaves a deposit. No states, no food. | Single dot with a short fading smear behind it |
| 9:50 | N | brute-force-first, failure-shown | Run with a few thousand agents on the CPU. Agents steer toward the trail they sense, but the trail is never blurred, so it stays razor-thin and the pattern jams. | Noisy white speckles; framerate low in a corner counter |
| 10:35 | N | minimal-definition-then-refine, build-and-verify | Add two trail rules: diffuse (average with neighbours) and decay. After this, lines connect and form networks. | Before/after of a pixel grid with a 3x3 blur; then the first network patterns |
| 11:30 | N | simulation-as-argument, visible-repetition | Same agents, same seed, vary one setting at a time: sensor distance, sensor angle, turn speed. Each knob shown in a grid. | A grid of nine panels, each with a different slider value |
| 12:40 | N | failure-shown, honest-caveat | Setting "gross" combinations: everything collapses to a point or blobs. Admits he does not fully understand why certain regions give veins versus cells. | Collapsed blobs; stable "cell" patterns; wavering voice caveat |
| 13:30 | N | design-it-yourself, build-and-verify | Starting positions matter: random spread, all in a circle facing inward, all from one point. Same rules, different final pictures. | Three starts side by side |
| 14:25 | I | brute-force-first, build-and-verify | Performance: thousands of agents is slow on the CPU. Moves the loop to the GPU so every agent updates in parallel. Not a full tour of the shader; mentions it. | Fps number, code panel in a shader language, a leap to 100k then millions of agents |
| 15:30 | N | generalize-to-other-domains, humor | Species: two agent types, each repelled by the other's trail, and a colour per species. Quick tour of what the rules produce. | Two-colour sim; agents chasing and avoiding |
| 16:30 | N | generalize-to-other-domains | Interactive: draw food or obstacles; feed an image to turn trails into a picture; 3D idea mentioned. | A drawing cursor, a map shape the agents trace out |
| 17:10 | H | honest-caveat, callback-to-hook, teaser-next | Closing wishlist: ants are still primitive, no nest ecology; he wants to combine with the earlier ecosystem video. Callback to the single dot at the start. Thanks to supporters. | Return to the one-ant scene; fade to a showcase montage |

## 2. Full narration script

Alright, so today I would like to try simulating ants. Or at least the way that a colony of ants finds food and carries it back home. Ants are tiny and seem rather dim on their own, and yet a whole colony manages to do surprisingly clever things, and I would like to see if I can get something like that going on my computer.

I will start with the most basic version of this I can think of. Here is one ant, and for now it is just a dot. All it needs is a position and a direction it is facing. Every frame it moves a small step forward, and if it hits the edge of the screen it bounces off. That is it. That is the ant for now, and we will add to it as we go.

Over here I have a nest, and I will make a hundred of these ants spawn at the nest. Let's start with the dumbest thing I can think of, which is to have each ant just wander randomly. Every frame, it nudges its direction by a small random amount. And I will scatter some food around the map and see how they get on.

Well. You can see that they sort of drift about, and a few of them might stumble upon some food by accident, but mostly it is a lot of ants not finding anything. And even when one does find food, there is no way for it to tell any of the others. I have a little counter here for how much food has been brought back to the nest, and it is sitting at nearly zero. Not great. And this is obviously not how real ants do it.

So what do real ants do? As I understand it, they leave behind a chemical as they walk, a pheromone, and other ants can smell it and are drawn to follow it. So the smallest change I can make to my simulation is this: as an ant walks, it leaves a marker on the ground behind it. I will draw that marker on a grid, and the ants can then look at the grid. Now, I am only roughly familiar with the biology here, so take that with a pinch of salt. I am going for something that works, not something that is perfectly accurate.

Now, what should the marker mean? If an ant is out looking for food, it needs a way to get back home afterwards. And if it has found food, other ants need a way to get to it. So I will have two kinds of marker. An ant that is searching leaves a path-home marker, and an ant carrying food leaves a path-to-food marker. And a searching ant follows the path-to-food markers, while a carrying ant follows the path-home markers. I will colour the ants differently based on which state they are in, so that we can tell them apart.

Next question: how does an ant actually read the markers? One idea is to give the ant three little sensors, one pointing a bit to the left, one straight ahead, and one to the right. Each sensor looks at how much marker is at its location. If the left one reads the strongest, the ant turns left, and if the right one wins, it turns right, and otherwise it keeps going straight. Now there are a couple of knobs hiding in here: how far ahead the sensors are, and how wide the angle between them is. I will leave those as sliders for now so I can play with them.

Here is the code for that. For each sensor, we add up the marker values in a small area around the sensor position. Then we compare the three numbers and steer. It is a bit more code than I would like, but it really is just those three numbers and a decision.

Okay, so let me test it. I will place one food source, keep the same nest, and run it with the same random seed every time so that I can compare. And look at that, after a bit a trail starts to form, and the ants are marching between the food and the nest. The counter is ticking up now. That is already so much better than the random version.

But if I leave it running for a while, something strange happens. The markers never go away. So every route that was ever walked is still there, including all the silly wandering routes from before. The ants start following their own trails round and round, and the whole map saturates into a big blob. That is clearly not going to work.

The fix is to let the markers evaporate a little bit every frame. I have added a slider for the evaporation rate. If it is too low, the picture still saturates. If it is too high, the trail disappears before anyone can follow it. But somewhere in the middle, something really nice happens, because the short paths get walked more often and so get topped up more often, while the long ones fade away. Let me drag the food to somewhere else and watch. The old trail fades, and the ants find a new one. That is quite fun to watch.

Of course, these are very simplified ants. Real ants are a lot more complicated than this, but I think it is a pretty cute result for a few rules. And in fact what I find interesting is that the main ingredients here, agents that leave a trail and follow a trail, seem to give good results even when I strip everything else away. So let me try that.

Here is the simplest version. This agent has a position, an angle, and one kind of trail. There is no food, no nest, no states. Each step, it moves forward and leaves some trail behind it. And it senses the trail with the same three sensors as before and turns toward the strongest one.

I will start by simulating a few thousand of these on the CPU. And, well, that is not very pretty. The trail is so thin that it is only ever one pixel wide, so agents rarely sense each other, and what we get is a bunch of speckles. So we need two more rules for the trail itself. First, diffusion: each pixel is blended with its neighbours, so the trail spreads out and gets a bit blurry. Second, decay: it fades a little every frame, like the evaporation from before. Let me add those.

And now we are getting somewhere. The agents start to connect up their paths, and networks form. If you have ever seen slime mould grow, this might look a little familiar. Though I should say that I am not claiming this is how slime mould really works.

Let me see what each setting is doing. I will keep the same seed and the same number of agents, and change one setting at a time. Here are a few values of sensor distance. Small values give a fine, dense pattern, and large values give big, coarse structures. Now the sensor angle. Then the turn speed. You can see in this grid how each one changes the character of the picture.

Some of the combinations are, frankly, rubbish. Everything collapses into a single point, or it fills the screen with static. And some lovely ones look like veins, or like cells. I will be honest, I do not fully understand why a particular region of settings gives veins and not cells. I just know that they do.

Something else that makes a big difference is where the agents start. Randomly spread out gives one result. If I put them all in a circle facing inwards, I get something different, and if they all start from a point and fly outwards, something different again. Exactly the same rules, but different final pictures.

Now, this is getting slow. With a few thousand agents the CPU is struggling, and I would love to see many more. The thing is, every agent does exactly the same little job and does not depend on its neighbours within a frame, so this is a perfect fit for the GPU, where I can run all of them at the same time. I will not go through the whole shader here, but the code is almost identical, just in a different language. And, well, now I can run hundreds of thousands, even millions of agents, and it is still smooth.

With so many agents, the patterns are much finer. Let me try one more idea. Instead of one kind of agent, I will have two species, and each one is drawn to its own trail but repelled by the other. That gives some very fun chasing patterns.

I also set it up so I can draw on the map, and I tried turning an image into the thing the agents are attracted to, so that they trace out the picture.

So that is as far as I got for now. The ants are still very basic. There is no real nest, no ant that dies, nothing like that, and it would be very cool to bring them together with the ecosystem simulation from before. But for now, I think it is cool that a single dot with three sensors can grow into all of this. Thanks for watching, and thanks to everyone who supports the channel.

## 3. Rule trace

| Beat | Report claim / arc step / move that drove it |
|---|---|
| 0:00 opening | Arc step 1: roadmap and tiny toy world in the first minute (fluids one circle, ecosystem one bunny). Hook is a project statement, not a question (section 3, "hook-paradox appears once", "hooks are mostly a project statement"). |
| 0:35 one ant | Toy-world 12/12; minimal-definition-then-refine 8/12. Principle 10 "1 particle to 40k". |
| 1:10 random wander | Arc step 2 dumb version first; brute-force-first 7/12, principle 6 "strongest fit". |
| 1:55 fails | Arc step 3 fails visibly; failure-shown 11/12; "ecosystem" compressed form. |
| 2:30 marker | Theory 1 failure-gated vocabulary: term (pheromone, marker) named only after the failure is watched. Analogy kept brief (principle 4: analogies brief and concrete). |
| 3:10 two markers | Design-it-yourself 10/12 ("what knob is missing"). Report: stepping stones invented freely. |
| 3:55 sensors | Act-it-out principle 5, 9/12: the thing on screen is the thing. One knob one cause (new theory 6). |
| 5:00 code | Arc step 4 and theory 2: notation only after behaviour is conceptually set; code before big maths. Notation-after-concept 9/12. Written as code, not as formula. |
| 5:40 first test | Arc step 5 verify immediately; build-and-verify 11/12; theory 3 fixed test choreography (same seed). |
| 6:25 saturation | Arc step 6, next failure triggers next concept; failure-shown. |
| 7:10 evaporation | Theory 1 again; theory 6 one-slider-per-concept; simulation-as-argument 10/12. |
| 8:00 move food | Build-and-verify as a repeatable test; moving the target as a robustness check (A* "scaffolding removed" analogue). |
| 8:50 caveat / pivot | Honest-caveat 10/12; roadmap 9/12; generalize-to-other-domains 8/12 via same agent core reused. |
| 9:15 slime agent | Scaffold removal across reruns (theory 5): same model, labels removed; minimal definition. |
| 9:50 CPU thousands | Brute-force-first, failure-shown. "Fluids: naive loops first". |
| 10:35 diffuse and decay | Theory 1 (blur named after the thin-trail failure). Before/after in pictures (build-and-verify). |
| 11:30 grid of sliders | Theory 6 and fluids 29:41 parameter grid; simulation-as-argument. |
| 12:40 collapse, "don't understand" | Theory 4 honesty as pacing (memory 4:19, fluids 2:29); failure-shown; humor/blunt. |
| 13:30 start positions | Visible-repetition 11/12 with same rules; special-case-first variants. |
| 14:25 GPU | Brute-force-first then optimisation with number before/after (chess 15:45 pattern); I-level because code/shader. Honest skipping of the hard part (section 1: "the skipped hard part"). |
| 15:30 species | Generalize-to-other-domains 8/12; humor 9/12. |
| 16:30 interactive | Design-it-yourself; sim as argument. |
| 17:10 close | Arc step 7 honest close: wishlist, callback, teaser; rarely recap (section 2, section 6 "few recaps"). Callback-to-hook 8/12. |

Report claims I could NOT turn into concrete choices (too vague):
- Principle 8 "pace by novelty": the report says idea rate drops in testing and rises in "boring code", with no usable numbers; I only used it to give the GPU beat a fast, mildly dismissive treatment.
- Principle 3 (habit): "never taught deliberately", so no generative content.
- Principle 13: "plain words, expert content" gives no specific wording or depth ratio.
- The report says humor is in 9/12 videos but the only example is "avert your eyes". I invented the type and placement of the jokes.
- Which analogies (if any) he picks: "brief, physical" is too vague to choose one. I used pheromone as a one-sentence biological aside.
- The report gives no count for the number of examples in a sim video, or how long the intro to a project runs, so beat length is a guess.

## 4. Explicit predictions

- First question to the viewer: none. He asks himself rhetorical questions (which marker? how does an ant read it?) first at about 3:10; no real viewer question (report: 9 of 12 have none).
- First notation/formula time: no formula. First code on screen about 5:00 (about 28% of runtime), after the sensing concept has been shown on a single ant. No equation at all, except possibly a one-line blur kernel or turn rule at about 10:35.
- Misconception: no. No planted viewer belief. Any "wrong" idea is his own failing version (random wander at about 1:10, no-evaporation at about 6:25).
- Brute-force-first: yes. Random wandering at about 1:10 (dumb ant) and CPU loop at about 9:50 before the GPU move at about 14:25.
- Examples: about 4 or 5 scenes. One ant, 100 ants with food, 1 slime agent, thousands then millions of slime agents, two species. Growth is tiny to bigger (1, 100, thousands, millions) and rules stack one at a time.
- Hook type: project statement plus a single toy object (one dot), no question and no paradox.
- Ending type: honest close with a wishlist and a link back to the ecosystem video and the opening dot; thanks to supporters; no recap of lessons.
- Five moves I am most confident will appear:
  1. toy-world (one ant or one agent on an empty canvas in the first minute)
  2. failure-shown (random wandering does not find food; trails saturate)
  3. build-and-verify (same seed, same scene re-run after each added rule)
  4. design-it-yourself and simulation-as-argument (sliders and parameter grid for sensor and evaporation settings)
  5. honest-caveat (not how real ants or real slime work; "do not fully understand why" a parameter regime gives a pattern)
