# PrimerBlobs: Simulating a single brain cell

- channel: PrimerBlobs
- id: GkiITbgu0V0
- title: Simulating a single brain cell
- duration: 2026 s (33:46)
- condition: v1
- recall: none

## Content skeleton
- Opens on the question of how a mostly quiet cell decides the exact moment to send a spike.
- Stage one: a leaky bucket with a rim as threshold, a baseline with no rim, and a refractory period that caps the firing rate.
- Stage two: the membrane as a wall with ion gates; the resting voltage, the Nernst balance points, and why two gate types with different speeds are needed for a spike shape.
- A blocked-sodium prediction shows the threshold is the point where sodium takes over.
- Stage three: a dendritic tree in which far inputs decay, and clustered or simultaneous inputs are what fire the cell, with a caveat that the tree is a toy.
- Recap of the threshold, ion balance, two gates, distance and timing, and a teaser toward networks of cells.

## Beat sheet

| Time | Beat type | What is said or shown |
|---|---|---|
| 0:00 | hook | Question: how does a mostly quiet cell decide the exact moment to fire? |
| 0:40 | roadmap | One sentence: a bucket first, then ions and gates, then a branching tree. |
| 1:15 | toy-world | A bucket with a small hole: input drips in, charge leaks out. |
| 2:05 | definition | The water level is the cell's voltage; the rim is the threshold. |
| 2:50 | brute-force | Baseline: a leaky bucket with no rim; the level just tracks the drip. |
| 3:40 | demo-sim | Add a rim: crossing it spills a spike and resets the level. |
| 4:30 | demo-sim | Stronger drip: spikes come faster and the rate climbs. |
| 5:20 | viewer-turn | Pause: if the drip doubles, does the firing rate double? |
| 6:00 | demo-sim | Reveal: the rate rises and then flattens; the refractory period caps it. |
| 6:50 | definition | Refractory period: a short deaf window after each spike. |
| 7:40 | misconception-defuse | "A neuron is a calculator that adds inputs" is set up; the rim and refractory period break the pure-sum view. |
| 8:30 | demo-sim | Thirty drip settings: the rate curve starts at zero, climbs, and bends toward a ceiling. |
| 9:30 | derivation | Rate is one over fill time plus refractory time; the formula summarizes the curve already shown. |
| 10:20 | toy-world | Swap the bucket for the real membrane: a wall with ion gates. |
| 11:10 | definition | Sodium is outside and potassium inside; each gate lets one ion type through when it opens. |
| 12:00 | analogy | A concentration difference behaves like a slope that pushes ions downhill. |
| 12:50 | derivation | Balance voltage for potassium is near minus 90 millivolts, for sodium near plus 60; idealized numbers. |
| 13:50 | demo-sim | A resting cell sits near minus 70 millivolts, closer to the potassium balance point. |
| 14:40 | wall | One gate type can push the voltage up or down, but it cannot make a spike shape. |
| 15:30 | demo-sim | Fast sodium gates plus slower potassium gates: rise, peak near plus 30, fall, undershoot. |
| 16:30 | viewer-turn | Pause: if sodium gates are blocked completely, will the cell still spike? |
| 17:20 | demo-sim | Sodium blocked: no spike; potassium only sags the voltage slightly below rest. |
| 18:10 | payoff | The threshold is where sodium takes over; the spike is the sodium rush and the potassium reset. |
| 19:00 | demo-sim | Simulated spike compared with a recorded spike: peak, width near a millisecond, undershoot. |
| 19:50 | caveat | Gate speeds were tuned to fit the shape and the concentrations are textbook values; a match is consistency, not proof. |
| 20:40 | demo-sim | Steady current sweep: rate against current, compared with the bucket curve. |
| 21:30 | tangent | The squid giant axon is a large nerve fibre that made recordings easier than most. |
| 22:20 | demo-sim | Dendrite tree with input points at different distances from the cell body. |
| 23:10 | derivation | Signals weaken along a branch because the membrane leaks charge; distance matters. |
| 24:00 | demo-sim | Scattered inputs do not fire the cell; a nearby cluster does. |
| 24:50 | viewer-turn | Pause: is one far-off synapse enough to fire the cell? |
| 25:40 | demo-sim | Reveal: one far input does almost nothing; several together fire it. |
| 26:30 | caveat | Real neurons have thousands of inputs and more gate types; the tree is a toy. |
| 27:20 | generalize | The bucket with a rim is a threshold switch, the same shape as other leaky accumulators. |
| 28:10 | misconception-defuse | A neuron is not a logic chip; the timing of inputs matters as much as their count. |
| 29:00 | demo-sim | Timed inputs: two arriving a millisecond apart cross the threshold; spread over ten, they do not. |
| 29:50 | story-rung | Early researchers measured spikes one at a time, and each equation was checked against a recording. |
| 30:40 | recap | Threshold, ion balance, two gate types, distance and timing. |
| 31:30 | payoff | The cell is a threshold device whose spike rate encodes input strength and timing. |
| 32:20 | teaser | Next: connect many of these cells into a network. |
| 33:00 | advice | Try it: slow the sodium gates and find the speed at which spikes stop. |
| 33:30 | coda | Closing image: a spike train on the dish, one pulse after another. |

<<<NARRATION
How does a single cell decide when to fire? Most of the time, a neuron is quiet. Then, for a few milliseconds, it sends a sharp pulse down its long thin arm, and it might do that hundreds of times a second. What makes it pick that moment? That's the question for this video, and we'll answer it the way I've answered the others: by building the simplest version of the cell first, running it, and then adding what the simplest version cannot explain.

We'll go in three stages. First, a bucket. Then the real membrane, with its ions and gates. Then a branching tree of inputs, which is closer to what a real neuron looks like. At each stage I'll show you what the model predicts, and where it breaks.

Start with a bucket that has a small hole in the bottom. Water drips in from above. That's the input, the signal arriving from other cells. Water also leaks out through the hole. The water level in the bucket plays the role of the cell's voltage. A bucket with a hole can hold some water, but it never fills up if the drip is slow.

Here's the baseline. I'll run a bucket with a hole and no rim at all, so the level can rise as high as the input allows. Weak input makes the level climb to a steady height and stop there. Strong input makes it climb higher. Nothing dramatic happens. The bucket just has a level, and the level tracks the drip. That's a useful picture, and it's also incomplete, because a real neuron does something sharp, not something smooth.

So let's add a rim. When the water crosses the rim, the bucket spills, all at once, and the level resets to the bottom. That spill is the spike. The rim is the threshold. Run it with a moderate drip. Now the bucket fires on a regular beat, and the beat speeds up as the drip gets stronger.

Here's the prediction to commit to. If I double the drip, will the firing rate double? Look at the bucket and decide before you read on.

Here's the run. The rate goes up, but it does not double. It climbs, and then it flattens. The reason is a detail I've been ignoring: after a spike, the bucket needs a short time before it can fill again. Call that the refractory period. During it, the bucket is deaf to the drip, even when the water would otherwise be above the rim. So as the input grows, the cell hits its own speed limit.

This is where a common intuition breaks. It's tempting to think a neuron is a calculator. Add up the inputs, and fire if the total is large enough. The sum part is partly right. The threshold is real. But the refractory period means the output is not a simple function of the sum. The output is a rate, and the rate saturates. The cell can only say so much per second, however hard you push it.

Let's check the shape over a range of drips. I ran thirty settings, each with a fixed drip, and measured the firing rate. The curve starts at zero below the threshold, climbs steeply, and then bends over toward a ceiling. That ceiling is set by the refractory period. Shorten it and the ceiling rises. Lengthen it and the curve flattens sooner.

Now I'll write a formula, because the curve has a simple summary. The time between spikes is the time to fill the bucket up to the rim, plus the refractory period. So the rate is one over the sum of those two times. When the drip is strong, the fill time gets short, and the rate approaches one over the refractory period. The symbols aren't there to replace the curve. They are a shorthand for the shape you've already watched.

So far, the bucket explains a lot. But it has one big gap. In a real cell there's no water and no hole. Let's replace the bucket with the membrane itself.

A neuron's membrane is a thin wall of fatty material with proteins embedded in it. Some of those proteins act as gates. Inside the cell, potassium is concentrated, roughly 140 millimolar. Outside, it's low, around five. Sodium is the other way around: low inside, around 12, and high outside, around 145. Each gate lets one kind of ion through when it opens. Because the concentrations differ, the ions want to move. Potassium wants to leave, and sodium wants to enter.

Here's the idea that makes it all work. The membrane's voltage is the balance between those pushes. For potassium alone, there's a specific voltage at which the push from the concentration difference exactly cancels the electrical pull. That's the balance point for potassium. For potassium, with these numbers, it lands near minus 90 millivolts. For sodium, it lands near plus 60. These are idealized numbers, and a real membrane sits between them, but they tell you which way each gate pushes.

Now the resting cell. At rest, the membrane sits around minus 70 millivolts. In the sim, that's where it stays. Potassium gates leak a little, pulling the voltage down toward their balance point. Sodium gates are mostly closed, so they barely pull it up. The voltage rests closer to potassium's value than to sodium's.

Here's a limit I want to show you. Suppose we give the cell one kind of gate, one that opens when the voltage rises. Run it. The voltage rises, and then it stays up. There's no fall. A single kind of gate can push the voltage in one direction, but it can't produce a spike, which needs a rise followed by a fall. So the membrane needs two kinds of gate, with different speeds.

Here they are. Sodium gates open fast, and their opening pushes the voltage up. Potassium gates open more slowly, and their opening pushes the voltage down. Run the sim. The voltage rises sharply, crosses zero, peaks near plus thirty millivolts, and then falls. It undershoots below rest for a moment before it recovers. That shape is the spike. Its rise is the sodium rush, and its fall is the potassium reset.

Let's test the explanation. Predict before you read on. If I block the sodium gates completely, will the cell still spike?

Here's the run. No spike. Blocking sodium removes the rush, so the voltage never crosses the threshold. The potassium gates still open, and the voltage sags a little below rest. So the threshold is the point where sodium takes over. Below it, potassium holds the cell down. Above it, sodium pushes the voltage up by itself. That's a clean way to see the threshold. It is the crossing point where one set of gates starts to win.

Now the width of the spike. The whole event takes around a millisecond or two. That's why the refractory period is so short. The gates need time to reset, and during that reset the cell can't fire again.

I checked this model against recordings. Measured spikes from real axons rise to about plus thirty, fall over roughly a millisecond, and undershoot by a few millivolts. My sim, with the speeds I picked, gets close on all three. Close is not the same as proof. I tuned the gate speeds to fit the shape, and I took the concentrations from textbook values. So the match tells you the model is consistent with the data, not that it's the only model that could be.

Here's a rate sweep, to tie this back to the bucket. I hold a steady current into the membrane and vary its strength. Below a threshold current, nothing fires. Above it, the rate climbs and then bends toward a ceiling, the same shape as before, for the same reason: a threshold and a recovery period.

Early measurements of these spikes used the squid giant axon, a large nerve fibre that was easier to record from. Each equation in the model was checked against a recording.

Now what the model leaves out. This is a single point, with one voltage for the whole cell. A real neuron is a tree of branches. Its body is small, and most of its inputs arrive far out on the branches, not at the center. A signal from far away weakens as it travels, because the membrane leaks charge along the way. So where an input lands matters.

Let's add a branch. Here's a tree of dendrites, with a few input points at different distances from the cell body. Give the cell one strong input at the tip of a far branch. Run it. Nothing happens. The signal fades before it reaches the center. Now give the cell several inputs, all at the tips, at the same time. The cell fires. So the question is not only how much input arrives, but whether it arrives together and close enough to matter.

Before we move on, one more commitment. Pause. If one far-off input fires, does the cell fire? Think about the decay, and decide.

Here's the reveal. One far input does almost nothing. It decays on the way in. Several together can push the cell over the threshold. Coincidence matters. The cell detects inputs that arrive together, not just inputs that arrive often.

Timing turns out to matter a lot. In this version, two inputs arriving a millisecond apart can cross the threshold, while the same two inputs spread over ten milliseconds do not. So the cell is not a calculator that adds up numbers. It responds to patterns in time, and that's why the same cell can produce different output depending on when its inputs arrive.

This sim leaves a lot out. Real cells have thousands of inputs, more gate types, and slow chemical changes. My tree is a toy. The point is the logic, not the count.

That logic shows up beyond neurons. Any system that accumulates something, leaks some of it, and releases it at a limit has the same shape.

Let's sum up. The threshold is a crossing point, set by the balance of ion gradients and gates. The spike is a fast sodium rush followed by a slower potassium reset. Refractoriness caps the rate. And the position of an input, along with its timing, decides whether it counts.

Next time, we'll connect many of these cells into a network and see what they do together. Before then, try a small change yourself. Slow the sodium gates a little, and see at what speed the spike stops happening.
NARRATION>>>

```json
{
 "format_class": "staged build: bucket, membrane, dendrite tree, predict pauses",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.0,
 "first_concrete_object_frac": 0.04,
 "first_new_idea_frac": 0.06,
 "first_notation_frac": 0.28,
 "payoff_frac": 0.54,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 6,
 "example_growth": "one bucket, spike rate, membrane gates, dendrite tree",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.16,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the bucket with a rim, reused as the threshold at each stage",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 50,
 "beat_sequence": ["hook","roadmap","toy-world","brute-force","demo-sim","viewer-turn","misconception-defuse","derivation","analogy","wall","demo-sim","viewer-turn","caveat","payoff"],
 "top5_moves": ["toy-world","brute-force-first","simulation-as-argument","notation-after-concept","honest-caveat"],
 "absent3_moves": ["humor","running-character","expert-dialogue"]
}
```
