channel: SebastianLague
id: WP-Bm65Q-1Y
title: Procedural Landmass Generation (E02: Noise Map)
duration: 914s (15:14)
condition: v3
recall: vague
exemplars read: deep/corpus/compact/COmtTyLCd6I.txt, deep/corpus/compact/MRNFcywkUSA.txt

## Content skeleton
- Open on a personal story: early terrain attempts with random heights looked like static, and that failure is the reason for this episode.
- Set up the map: a two-dimensional float grid, and a generator script that returns it.
- Introduce smooth noise and why neighbouring samples must give neighbouring values.
- Show the scale parameter live in the editor, from broad hills to a busy texture.
- Stack octaves for detail, with persistence and lacunarity, and compare one octave with four.
- Normalise the result into the zero to one range, with the reset bug as the honest mistake.
- Close with where the map goes next, and a teaser.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Story: random heights looked like a bowl of static, so the terrain did not read as land |
| 0:50 | toy-world | Empty grid and a generator script that returns a 2D array |
| 1:40 | definition | Smooth noise: nearby inputs give nearby outputs |
| 2:30 | derivation | Nested loops and dividing coordinates by a scale |
| 3:20 | demo-sim | Scale 50 versus scale 5 in the editor preview |
| 4:20 | visible-repetition | Greyscale preview, updating as the slider moves |
| 5:10 | definition | Octaves: broad shape plus finer layers |
| 6:10 | derivation | Amplitude and frequency per octave, with persistence and lacunarity |
| 7:20 | demo-sim | One octave versus four octaves |
| 8:10 | derivation | Normalising the map into zero to one |
| 9:00 | failure-shown | The min and max were not reset, and the preview washed out |
| 10:10 | generalize | Noise appears in clouds, textures and fire, not only terrain |
| 11:00 | definition | Seeds and offsets give different landscapes from the same code |
| 12:20 | payoff | The map now looks like a plausible landscape |
| 13:30 | teaser | Next episode: displace a mesh and add colour bands |

## Narration
<<<NARRATION
When I first started making terrain for a little game, I did what seemed obvious at the time. I placed random heights on a grid, and I got something that looked like a bowl of static. It was technically a landscape, but nobody would ever want to walk across it. So in this episode we're going to build the thing that makes terrain look like terrain, which is a noise map. If you've ever used random values for anything visual, you'll notice the difference right away. We'll start with a flat grid, fill it with values that are smooth rather than random, and then show the result as a picture so we can see what we've made.

Alright, so the first thing we need is somewhere to store our values. We're going to make a two-dimensional float array, and for now let's say its width and height are both 256. Inside Unity we'll create a new script, and we'll call it map generator. We'll add a public method that takes a width, a height and a scale, and returns the finished map. We want the map to be a grid of numbers, where each number represents the height of the land at that point. That's all a heightmap really is. We'll also mark the width, the height and the scale as serialised fields, so we can change them in the inspector without recompiling. We can see the grid size, the scale and the seed all in one place, and we can compare results side by side. We also want a clear split between the generator, which only knows about numbers, and the display, which only knows about pixels. Keeping those apart makes both of them easier to test, and I found that out the hard way.

Next we need the actual noise function. Unity gives us Mathf dot PerlinNoise, which takes an x and a y coordinate and returns a value between zero and one. We'll wrap that call so the rest of the code stays clean. The important property is that nearby inputs give nearby outputs. That smoothness is exactly what we're after, because real hills don't jump from one height to another between neighbouring squares. If two points are close together, their heights should be close too, and Perlin noise gives us that for free. It's easy to think random values would do the job. I tried that first, and I remember staring at the preview and thinking it was broken. If we used random values for every cell, each neighbour would be independent, and the map would flicker from pixel to pixel. We'd get noise, but not terrain. Perlin noise blends smoothly between gradients, so we get structure instead. I probably spent an hour on that before the penny dropped.

So we loop over every cell in the grid. We'll use two nested for loops, one for the x coordinate and one for the y coordinate. For each cell we compute a sample coordinate, and we pass that to the noise function. We set the sample x to be x divided by the scale, and the sample y to be y divided by the scale. That division is the bit that controls how zoomed in we are. We have to cast the scale to a float first, otherwise the division rounds down and everything goes wrong. Let me walk through that line by line, because it's where most of the confusion comes from. We take the cell x, we divide it by the scale, and we get a fractional coordinate. We do the same for y. Then we hand those coordinates to the noise function, which returns a height between zero and one. Repeat that for every cell, and we have a full grid of heights. If the output looks wrong, the first place we look is always that division, and it has caught me out more times than I'd like to admit. If we choose a big scale, we get broad, slowly changing hills, while a small scale gives us a jittery mess.

Let's see that in action. With a scale of 50, the whole map looks like one smooth bump with a few gentle dips. Now I'll drop the scale to 5, and the same map becomes far busier, with lots of little peaks and valleys. Nothing about the algorithm changed. We only changed how far apart the samples are. That's the whole job of the scale parameter, and once you see it, it's hard to forget.

Okay, so we have a noise map, but right now it's just a grid of numbers. To look at it, we'll draw it as a greyscale texture. White is the highest value, black is the lowest, and each pixel is one cell from our grid. We can add a preview in the editor and scrub the scale slider, and we'll watch the texture update live. That kind of quick feedback is what makes this so enjoyable to tweak. We can change a single value and see the terrain respond immediately. The preview is also a debugging tool, not just a pretty picture. When the map looks strange, we can see exactly where the problem is, because each pixel maps directly to a cell. We can spot a seam, a flat stripe, or a corner that's too bright. Those things are almost impossible to notice by reading numbers in a list. So we keep the preview on while we work, and we treat it as the ground truth.

Now here's the problem. If we use a single layer of noise, it looks too smooth. Real terrain has big features, like mountain ranges, and small features, like rocks and bumps on the slopes. We can get both by stacking several layers of noise on top of each other. We call each layer an octave. We get the broad shape from the first octave, and each later octave adds finer detail. For example, the second octave might sample at twice the frequency and contribute a smaller amount. Stacking is what turns a soft blob into something that looks like ground.

We'll add three new parameters to the generator. The first is an integer for the number of octaves. The second is a persistence value, which controls how quickly the amplitude drops with each octave. The third is a lacunarity value, which controls how quickly the frequency rises. Persistence should sit between zero and one, so each octave contributes less than the one before it. Lacunarity is usually above one, so each octave samples more finely. In the inspector I'll set octaves to 4, persistence to 0.5, and lacunarity to 2.

Inside the loop over the cells, the noise height starts at zero. Then, for each octave, we sample the noise at that octave's frequency, multiply the result by the current amplitude, and add it to the noise height. After that we update the amplitude and frequency for the next pass. We multiply the amplitude by persistence, and we multiply the frequency by lacunarity. That's the whole inner loop, and it's only a few lines of code, but it does a lot of work. We end up with one height value per cell that combines every octave we asked for. It's worth pausing on why this works. Each octave is the same smooth function, just sampled more finely and scaled down. So every layer looks like the one below it, only busier. When we add them up, the big shapes are preserved and the small ones sit on top. We aren't inventing new kinds of detail. We're repeating one kind of detail at several sizes, which is why the result looks natural. That's satisfying, because the code stays so small while the output gets so rich.

Let's compare the results. With one octave, we get a map that is smooth and rounded, almost a soft pillow. With two octaves, small bumps start to appear along the ridges. With four, we get terrain that looks like something we'd actually want to walk on. Each extra octave costs us a bit more computation, so we don't want to go much higher than necessary. On a grid of 256 by 256, four octaves still runs comfortably, and I didn't notice any stutter while I was tuning.

We have one more problem to deal with, and it's a numerical one. Because we're adding several layers together, the noise height can fall outside the range we expect. The amplitudes shrink with each octave, so the sum stays in a known band, but it isn't exactly zero to one. So we need to find the smallest and largest values across the whole map, and then remap every cell into the range zero to one. We track those two numbers as we go, and then we run one more pass at the end. That final pass is what gives us a clean map that we can colour predictably later.

I'll be honest, I got this wrong at first. I forgot to reset the minimum and maximum between maps, so the second map I generated looked washed out and far too grey. We only noticed because the preview looked wrong. The fix is a single line, resetting the two values at the start of each generation, and once we did that, the whole map snapped back into range. It's a small mistake, but it's exactly the sort of thing that's easy to miss.

We can use this pattern well beyond terrain. Noise maps show up in clouds, in textures, in fire effects, and in any system where you want variation that still feels connected. The key idea is that a few layers of the same smooth function can produce detail at many scales. We'll reuse this idea across the series, and it'll come back when we start colouring the map by height. Honestly, it's one of the most useful tools in procedural generation, and it's worth understanding properly.

Before we move on, there's something I probably should have explained earlier. The seed controls where the noise starts. Two maps with the same seed look identical, because every sample is in the same place. Changing the seed shifts the offset of every sample, which gives us a completely different landscape from the same code. We'll expose that as an input in the inspector, and then we can generate a small set of maps quickly and compare them side by side. It's a very cheap way to get variety.

So here's where we are. We have a grid, a smooth noise function, four octaves of detail, and a normalised map that fits neatly into zero to one. When we look at the preview, we see something that could plausibly be a landscape. You can already imagine the next step, which is turning those values into actual height and colour. That's where the map starts to look like a world, and it's a bigger jump than it sounds. We'll need to think about how the mesh is built and how the colours are assigned.

In the next episode, we'll take this noise map and use it to displace a mesh, so the values become real hills in the scene. We'll also add colour bands for water, sand, grass and snow, and we'll see how much the scale and octave settings change the feel of the result. I have a rough idea of how to structure that code, and I think it will go smoothly, but we'll see how it goes once we start.
NARRATION>>>

## Slots
```json
{
 "format_class": "tutorial series episode, code-driven with editor preview",
 "answer_given_upfront": false,
 "hook_type": "story-anecdote",
 "first_question_frac": 0.1,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.08,
 "first_notation_frac": 0.3,
 "payoff_frac": 0.85,
 "misconception": "mid-video-correction",
 "brute_force_first": false,
 "examples_count": 4,
 "example_growth": "smooth blob, then scale 5, then four octaves",
 "roadmap": "none",
 "viewer_turn": "none",
 "viewer_turn_frac": null,
 "caveat_type": "approximation",
 "recurring_anchor": "the 256 by 256 grid preview, reused in every section",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 143,
 "median_beat_s": 40,
 "beat_sequence": ["hook", "toy-world", "definition", "derivation", "demo-sim", "visible-repetition", "definition", "derivation", "demo-sim", "derivation", "failure-shown", "generalize", "payoff", "teaser"],
 "top5_moves": ["story", "toy-world", "visible-repetition", "learner-discovers", "rule-list"],
 "absent3_moves": ["brute-force-first", "hook-question", "expert-dialogue"]
}
```

```json
{"verified_trace": {"wpm": "PASS 143.00 (target 138.51-143.59, median 142.78)", "you_rate": "PASS 0.26 (target 0.12-0.31, median 0.18)", "i_rate": "PASS 1.09 (target 0.88-1.13, median 0.94)", "we_rate": "PASS 5.20 (target 5.05-6.24, median 5.55)", "num_rate": "PASS 2.55 (target 1.52-3.68, median 1.86)", "hedge_rate": "PASS 0.16 (target 0.07-0.22, median 0.17)", "example_rate": "PASS 0.16 (target 0.06-0.18, median 0.09)", "switch_sponsor": "PASS detected=False default=OFF", "switch_teaser": "PASS detected=True default=ON", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (story-anecdote vs story-anecdote)", "ending_type": "MATCHES default (teaser-next vs teaser-next)", "summary": "7/7 numeric targets pass"}}
```
