# Header
- channel: SebastianLague
- id: WP-Bm65Q-1Y
- title: Procedural Landmass Generation (E02: Noise Map)
- duration: 914 s (15:14)
- condition: v1
- recall: vague

## Content skeleton
- Goal: generate a height map that looks like natural terrain from a seed.
- Toy world: a 2D grid of cells, each shown as a grey value.
- Naive version: a random value per cell, which gives static, not hills.
- Smooth noise: random values on a coarse grid, blended between neighbours.
- Interpolation formula introduced only after the blended map is on screen.
- Octaves: layering noise at doubling frequency; persistence and lacunarity as knobs.
- More octaves is not always better; too much high-frequency detail reads as spikes.
- Honest caveat that this is a shape generator, not a geology model; teaser for the mesh step.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Flat grid on screen; how do you get hills that look natural? |
| 0:25 | roadmap | A noise map first, then shaping it with layers |
| 0:50 | toy-world | 2D grid of cells, each a grey value |
| 1:40 | brute-force | Random value per cell; this is the first thing I tried |
| 3:00 | wall | Result looks like TV static, not terrain |
| 3:50 | definition | Smooth noise: random values on a coarse grid, blended between them |
| 5:00 | demo-sim | 4x4 coarse grid blended into smooth hills |
| 6:30 | demo-sim | Same grid at 256 cells; scale slider changes the feature size |
| 7:20 | derivation | Blend formula shown only now, as a name for what the sim already does |
| 8:00 | generalize | Same smoothing idea for sound, temperature, wind |
| 9:00 | demo-sim | Octaves: sum layers at 1, 2, 4, 8 frequency; sweep |
| 11:00 | demo-sim | Persistence and lacunarity sliders; one knob, one visible cause |
| 12:00 | payoff | Layered map reads as a landscape |
| 12:30 | misconception-defuse | More octaves is not always more detail; past a point it is only spikes |
| 13:30 | caveat | Shape generator, not geology; no erosion modelled |
| 14:20 | teaser | Next: mesh and colours from the height values |
| 14:40 | coda | Sign-off and seed suggestion |

<<<NARRATION
Here is a flat grid. Our job is to turn it into something that looks like a landscape, with hills and valleys, and to do it from a number called a seed. So how do you get hills that look natural? That is the question for this episode.

The plan is simple. First we make a noise map, which is a grid of values that look random but are not. Then we shape it by layering that noise, and check each change as we go.

Let's start with the toy world. It is a two-dimensional grid of cells. Each cell holds one number, and I draw that number as a grey value. Dark means low, light means high. That is all we need. A grid of grey squares is not a landscape, but it is a height map, and that is enough to start.

The first thing I tried is the dumbest one I can think of. Give every cell a random number. That is it. No planning, no structure, just a random value per cell. I wanted to see what randomness looks like before I try to make it nice, because the failure tells you what to fix.

The result is a wall. It looks like the static on an old television. Every cell is independent of its neighbours, so there are no hills, only speckles. A terrain has to be continuous. If one point is high, the points next to it should be roughly high too. Random per cell throws that away. So the first version is wrong in a way I can point at, and that is useful.

The fix is what I call smooth noise. Instead of giving every cell its own random value, choose random values on a much coarser grid. Four by four is enough to show the idea. Then, for any point in between, blend the nearby coarse values. Near one corner the value is mostly that corner's number. Halfway between two corners it is the average. That is the whole definition: random values on a coarse grid, blended between them.

Here is what the blend does with a four-by-four grid. The random speckles disappear, and the map becomes soft, with broad bumps and valleys. The shape is still random, because the coarse values are random, but now neighbouring points agree with each other. That agreement is exactly what the random-per-cell version was missing.

Now the same coarse grid, drawn at full resolution. This is two hundred and fifty-six cells across. The scale slider controls how big each feature is. A small scale packs many bumps into the map. A large scale spreads them out. The noise is the same, and only the feature size changes. That is a good thing to check, because if the slider does something else, the design is wrong.

Only now do I write down the formula for the blend. It is an interpolation between the corner values, smoothed so the transitions do not show seams. I want to be clear about the order. The map was already working on screen, and the formula is just a name for what the code is doing. If I had shown you the formula first, it would have been a list of symbols with no picture behind it. Here, you already know what the symbols are doing.

This idea is not special to terrain. The same smooth random field works for sound, for temperature, for wind, for anything that changes gradually in space. So when you see the same trick somewhere else, you will recognise the shape of the solution.

But one layer of smooth noise looks like a soft blur. Real terrain has big hills and small bumps, all at once. So the next step is octaves. An octave is one layer of noise. You add a second layer at twice the frequency, a third at four times, and so on, and you sum them. I will show one octave, then two, then four, then eight, with the same sweep each time, so that the only change is the number of layers.

With one octave, you get broad shapes. With two, the shapes get bumpy. With four, you start to see detail on top of the detail. With eight, the map is busy, and the extra layers begin to look like noise again. That repetition is the part I trust most. The same sweep on each count, so you can compare the pictures side by side and see exactly what the extra layers added.

Now there are two more knobs. Persistence controls how much each extra octave contributes. A lower value makes the small layers fade quickly. Lacunarity controls how fast the frequency grows from one octave to the next. Two is the usual choice, but I want to see what happens if it changes. I sweep each slider on its own, and I change one number at a time, so each visual effect has one clear cause.

Look at the landscape now, with a few octaves, a moderate persistence and a lacunarity of two. This reads as a landscape. There are broad hills, ridges on top of them, and small bumps on the ridges. Nothing about it has been hand-drawn. It is entirely the sum of random layers, shaped by three knobs.

Here is a mistake I made. I thought that more octaves always gives more detail, so I kept adding them. Past a certain point, though, the small layers start to dominate. The map gets spikes everywhere, and the big shapes disappear under them. More layers is not the same as better terrain. The sweep showed me the crossover, and I had to back off. So when you add detail, check whether the large shapes are still there.

Now the honest part. This is a shape generator. It makes plausible hills, but it does not model geology. There is no erosion, no rock layers, no rivers carving valleys. A real mountain formed over millions of years, and this one formed in a few milliseconds from a seed. The result looks good enough for a game, and that is the only claim I am making. If you need real terrain science, this is the wrong tool.

So to recap the three ideas. The first is that a map has to be continuous, so random per cell fails. The second is that smooth noise, random values on a coarse grid blended between them, gives you that continuity. The third is that octaves, with two knobs for how they fade and how fast they grow, give you the mix of big and small shapes.

Next time we turn this height map into a mesh, a surface you can actually render, and then we add colours for water, sand, grass and rock. The height values will decide where each of those goes. For now, the map is the thing to get right.

If you want to try it, change the seed and keep everything else the same. You will see the same shapes in a different place. Thanks for watching.
NARRATION>>>

## Slots

```json
{
 "format_class": "build-break-fix devlog, layered sweeps",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.005,
 "first_concrete_object_frac": 0.01,
 "first_new_idea_frac": 0.11,
 "first_notation_frac": 0.48,
 "payoff_frac": 0.79,
 "misconception": "mid-video-correction",
 "brute_force_first": true,
 "examples_count": 4,
 "example_growth": "random static -> 4x4 blend -> 256 cells -> octaves",
 "roadmap": "one-line",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.005,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the grey-value scale and the seed, reused in every sweep",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 55,
 "beat_sequence": ["hook","roadmap","toy-world","brute-force","wall","definition","demo-sim","derivation","generalize","demo-sim","payoff","misconception-defuse","caveat","teaser"],
 "top5_moves": ["toy-world","brute-force-first","failure-shown","notation-after-concept","visible-repetition"],
 "absent3_moves": ["hook-paradox","expert-dialogue","commit-to-answer"]
}
```
