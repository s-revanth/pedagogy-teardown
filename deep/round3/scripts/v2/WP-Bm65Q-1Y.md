# SebastianLague | WP-Bm65Q-1Y | Procedural Landmass Generation (E02: Noise Map)

- channel: SebastianLague
- id: WP-Bm65Q-1Y
- title: Procedural Landmass Generation (E02: Noise Map)
- duration: 914 s (15:14)
- condition: v2
- recall: vague (I recognise the series and the subject (procedural terrain, Perlin-style noise), not this episode's content)
- class (step 0): over-10 min; format = designed-lesson tutorial (E02 series label); answer not stated up front; solved technique; topic = procedural generation / graphics code
- exemplars read: deep/compact/-L-WgKMFuhE.txt (A* Pathfinding E01, 11:38) read in full for series structure

## Content skeleton
- Opens on a question: why does a random map look like nothing, and why is it static rather than terrain.
- A 200 by 200 grid of random values, shown as grey; the failure is visible at once.
- Minimal definition of noise as a smooth function sampled per cell, credited to Perlin's gradient-noise work at the choice.
- Scale knob swept alone on a fixed seed; counts of hills called approximate.
- Octaves added one per pass on the same seed; persistence and lacunarity swept as sliders.
- Code described as steps; a normalisation failure (values outside zero to one) found and fixed.
- Edge seams noted as a later problem; the same noise reused for moisture and temperature maps.
- Histogram check as the payoff, then a teaser for turning the height map into a mesh.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Question on screen: why does a random map look like nothing? Static, not terrain. |
| 0:40 | toy-world | 200 by 200 grid, each cell a grey value between 0 and 1; the map from the last episode. |
| 1:30 | brute-force | Every cell gets its own random value; the screen fills with flicker; failure is expected and shown. |
| 2:20 | definition | Noise defined minimally: a smooth function returning a random-looking value at any position. |
| 3:10 | definition | Perlin's original gradient noise credited at the choice; gradients blended between cell corners. |
| 3:50 | demo-sim | Noise switched on: static gone, soft blobs that change gently from cell to cell. |
| 4:30 | demo-sim | Scale swept from 0.5 to 20 on one fixed seed; only the scale changes between runs. |
| 5:50 | caveat | Hill counts are rough, counted by eye; the same seed gives the same layout at every scale. |
| 6:40 | definition | Octave defined: double the frequency, half the strength; one overlay per pass. |
| 7:20 | demo-sim | One, two and four octaves on the same seed; big shapes stay put, detail adds texture. |
| 8:30 | demo-sim | Persistence then lacunarity swept; the viewer is asked to guess each effect before it shows. |
| 9:40 | caveat | Cost: four octaves take about four times as long; flagged as a trade to come back to. |
| 10:10 | demo-sim | Loop described in plain steps: position, scale, sample, amplitude, sum, then divide by total amplitude. |
| 11:20 | demo-sim | Failure: values above 1 and below 0 at the edges; the missing normalisation found and added. |
| 12:30 | caveat | Edge seams between side-by-side chunks noted for later, not solved here. |
| 13:00 | generalize | Second and third maps from new seeds drive moisture and temperature; grassy, sandy, and so on. |
| 13:50 | payoff | Histogram and range check: minimum near 0, maximum near 1, average near 0.5. |
| 14:30 | teaser | Next part turns the height map into a mesh the camera can fly over. |

## Narration
<<<NARRATION
Why does a random map look like nothing at all? That's the question for this episode, because if we fill a grid with random numbers and draw it, the screen fills with television static, and static is not terrain. So the job for this part is to turn random numbers into something that changes gently from place to place, the way hills and valleys actually do. We'll keep the map and the drawing code from the last episode as our starting point, and we'll change only what we need to, which is three numbers and one loop.

Let's start with the grid itself. Each cell holds a single number between zero and one, and we draw that number as a shade of grey, so white is high and black is low. The map is 200 cells by 200 cells, which gives 40,000 values in total, and each one is drawn with 8 bits of grey, so 256 possible shades, and right now every one of them is unrelated to its neighbours. I want to see that clearly before we change anything, so we'll generate it and look at it properly.

The first thing we tried was the obvious approach, which is to give every cell a random value. We generate the grid, draw it, and the screen fills with a flicker of random grey dots. That's exactly what we expected, and it's a useful failure, because it tells us that random values alone don't give us terrain. A hill needs its neighbours to be at a similar height, and random values can't do that at all, no matter how many times we regenerate them.

So we need noise, and I'll define it minimally before we refine it. Noise is a function that returns a random looking value for any position, and it changes smoothly as the position moves. We're not picking a random number per cell any more. We're sampling a smooth function at each cell's position, and that's the smallest definition that does the job. We'll upgrade it in a moment, once we've seen it working on screen.

The smooth noise I'm using comes from Ken Perlin's original gradient noise, which he developed for procedural textures in film, and it's worth reading his paper if you want the full details. The idea is simple to state. We place a random gradient at each lattice point, then blend the gradients smoothly between the four corners of each cell. We don't need the mathematics to see the result, so we'll look at the result first and come back to the detail later.

Let's switch it on. The static is gone, and in its place we get soft blobs of light and dark that flow from one cell into the next. Nothing jumps, and two neighbouring cells always have close values, which is the property we were missing. This is the moment the map starts to look like a landscape, even though it's still just flat grey, and we can already see where a valley might sit.

Next is the scale knob. The scale sets how far apart the sample positions are, so a small scale packs many features into the map and a large scale stretches each feature out. I'll sweep the scale from 0.5 up to 20, and I'll keep the same seed for every run, so the only thing that changes is the scale. At a small scale the blobs are tiny and dense, and at a large scale we see one or two broad shapes. One knob, one visible effect, and that's the whole point of the sweep.

For example, at a scale of 2 the map has about 6 major hills, and at a scale of 10 it has roughly 40 smaller ones. These counts come from looking at the dark and light regions by eye, so treat them as rough. What matters is that the same seed gives the same layout at every scale, which keeps the comparison fair. We'll keep that rule for every pass from here on, because a changed seed would hide the effect we're trying to see.

Now a single layer of noise looks like rolling hills, but it's too smooth, and real terrain has big shapes and small detail at the same time. So the next step is to add layers, and each layer is called an octave. The second octave is sampled at twice the frequency and blended in at half the strength, which adds finer bumps on top of the big shapes. We'll add one octave per pass, on the same seed and the same starting map, so each layer's contribution is easy to see on its own.

With one octave the map is smooth. With two, every hill gets a rougher edge. With four, the coastline looks like something a geologist might sketch, and every hill has smaller hills on its flanks. The overall shape doesn't change, though. The big hills stay where they were, and the new detail only adds texture on top, which is exactly the behaviour we want from layering in the first place.

There are two more knobs for the layers. Persistence controls how much each extra octave contributes, so a persistence of 0.5 halves the strength with each new octave, and a higher value makes the fine detail stand out more. Lacunarity controls how fast the frequency grows between octaves, and a value of 2 doubles it each time. I'll sweep persistence first and then lacunarity, and I'll describe what I'm looking at before I change anything else, so that you can follow along and guess what each change will do.

I want to be honest about the cost here. Each octave adds another noise sample for every cell, so four octaves take roughly four times as long as one. On a 200 by 200 map that's still fast, but on a larger terrain the cost adds up quickly, and that's a problem we'll come back to in a later part. For now it's a trade worth making, because the detail is what makes the map convincing enough to believe.

Now the code. Here is the loop, written out in plain steps. For each cell we compute its position, scale that position by the frequency, sample the noise, multiply the result by the amplitude, and add it to a running total. After the loop we divide by the sum of the amplitudes, so the final value stays between zero and one. That last step is the part I got wrong first, and the next section is about exactly that mistake.

When I first ran the loop, some cells came out above one and some came out below zero. The middle of the map looked fine, but the edges turned into bright and dark patches that didn't match the colour scale at all. The cause was that I forgot to divide by the sum of the amplitudes, so the total grew with every octave we added. Once the normalisation step was in place, every value stayed in range, and the colours made sense again.

There's a second problem I noticed at the edges. Two maps that sit side by side don't line up, because each one was sampled from a different origin. That doesn't matter yet, since we're only drawing a single map for now. It will matter as soon as we tile several chunks together, and I'd rather mention it now than discover it later, when the world is much bigger and the seams are much harder to find.

The same noise can drive more than height. If we sample a second map with a different seed, we can use it for moisture, and a third map for temperature. Then we can decide that a cell is grassy when it's wet and cool, and sandy when it's dry and warm. That's the same operation as before, applied to a different question, so the code barely changes. It's the generalisation I like most about noise, because the building block is so small and it does so much.

So where are we. We have a grid, a smooth noise function, a scale knob, and a stack of octaves with two more knobs on top. We also have one failure that we fixed, and one edge problem that we haven't dealt with yet. Every one of these steps came from something we saw on screen, rather than from a formula we were asked to believe on trust.

Before we finish, let me check the output against what we expect, using the same seed number 12345 that we've used on every pass so far. The lowest value on the map should be near 0, the highest near 1, and the average should sit close to 0.5, which is the middle of the scale. With the normalisation in place, that is what the numbers show, and the histogram looks like a soft bell rather than a spike at one end. If that had come out lopsided, we would have had a bug somewhere, and the picture alone would not have told us.

Next episode we'll turn this height map into an actual mesh, so the hills become real geometry that the camera can fly over. We'll look at how the surface normals change when the mesh gets steep, and how the colours map onto height. That's where this map finally becomes a landscape you can walk through, and I'll show you the first version of it then. Thanks for watching, and we'll see you in the next part.
NARRATION>>>

## Slots
```json
{
 "format_class": "designed-lesson tutorial series: question hook, one knob per pass, one overlay per octave, teaser",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.04,
 "first_new_idea_frac": 0.15,
 "first_notation_frac": 0.11,
 "payoff_frac": 0.91,
 "misconception": "none",
 "brute_force_first": true,
 "examples_count": 4,
 "example_growth": "random cells -> smooth noise -> octaves -> moisture maps",
 "roadmap": "none",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": null,
 "caveat_type": "approximation",
 "recurring_anchor": "the 200 by 200 noise map on one fixed seed, reused in 6+ passes",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "beat_sequence": [
  "hook",
  "toy-world",
  "brute-force",
  "definition",
  "demo-sim",
  "caveat",
  "demo-sim",
  "definition",
  "demo-sim",
  "caveat",
  "generalize",
  "payoff",
  "teaser"
 ],
 "top5_moves": [
  "toy-world",
  "visible-repetition",
  "design-it-yourself",
  "minimal-definition-then-refine",
  "brute-force-first"
 ],
 "absent3_moves": [
  "hook-paradox",
  "commit-to-answer",
  "expert-dialogue"
 ],
 "wpm": 105,
 "median_beat_s": 50
}
```

```json
{"rule_trace": {
 "U1": "applied: series label (E02) gate; under-10 items n/a at 15:14; roadmap, recap and callback withheld",
 "U2": "n/a: neither the title nor the first 40 s states the answer; the answer comes after the failure",
 "U3": "applied: teaser only, because the video is in a series; no hook callback since the hook question is answered mid-video",
 "U4": "applied: the 200 by 200 map on one fixed seed is reused in 6+ passes, each adding a knob or a layer",
 "U5": "applied: the only notation is code, introduced after the grid and noise are on screen; no formulas are spoken",
 "U6": "applied: narration is normal speech; beats of 25-40 s with silent screen runs, not a fixed 20-25 s grid",
 "U7": "applied: no roadmap, no vote, no planted misconception; the random-grid failure is shown rather than announced",
 "U8": "applied: approximation caveats on hill counts made by eye and on the cost of octaves",
 "U9": "n/a: no binary decision or absurd magnitude to pause on",
 "U10": "n/a: not a history-of-invention or escalating-antagonist video",
 "U11": "n/a: title names the topic (procedural landmass), not an application or an end state",
 "C1": "applied: designed-lesson tutorial format, not impersonal lecture and not devlog",
 "C2": "applied: one example (the same seed map) rerun with one overlay per octave pass; the starting picture is unchanged",
 "C3": "n/a: not lecture format; no pause-the-video quiz",
 "C4": "applied: Perlin's gradient-noise work cited at the moment noise is chosen over random cells",
 "C5": "n/a: series tutorial opens on a question, not a devlog problem",
 "D1": "applied: failure on screen (values outside 0 to 1 at the edges); normalisation fixes it",
 "D2": "n/a: the repair is named by its function (normalisation), not after the failure",
 "D3": "applied: scale knob swept alone on a fixed seed; persistence and lacunarity swept one at a time",
 "D4": "n/a: no honest-close bundle; the ending is a payoff check and a teaser",
 "D5": "n/a: no equation revealed after behaviour; the code is described as plain steps",
 "N1": "n/a: under-10 band rule; this video is over-10 min",
 "N2": "broken: 105 words per minute (measured), outside p25-p75 137-158; the 1,594 words over 15:14 give about 105 wpm; the narration is normal speech but the video carries silent screen runs, which lowers the full-runtime rate",
 "N3": "applied: 0.31 you/your per 100 words (measured), inside p25-p75 0.23-0.78",
 "N4": "applied: 1.13 I/me/my per 100 words (measured), inside p25-p75 0.94-2.81",
 "N5": "applied: 3.58 we/us/let's per 100 words (measured), inside p25-p75 2.55-5.7",
 "N6": "applied: 1.19 numbers per 100 words (measured), inside p25-p75 0.95-2.12",
 "N7": "applied: 0.06 question marks per 100 words (measured), inside p25-p75 0.0-0.09",
 "N8": "applied: 19.7 words per sentence (measured), inside p25-p75 19-25",
 "N9": "applied: 0.25 hedges per 100 words (measured), inside p25-p75 0.11-0.35",
 "N10": "applied: 0.06 example cues per 100 words (measured), inside p25-p75 0.03-0.18",
 "B1": "applied: no sponsor read",
 "B2": "applied: one-line teaser, because the video is in a series",
 "B3": "n/a: roadmap withheld; the video type does not call for one",
 "B4": "applied: no spoken recap"
}}
```
