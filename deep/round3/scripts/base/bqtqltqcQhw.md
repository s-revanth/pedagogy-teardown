# SebastianLague / bqtqltqcQhw

- Channel: SebastianLague
- ID: bqtqltqcQhw
- Title: Coding Adventure: Boids
- Duration: 515 s (8:35)
- Condition: base
- recall: vague

## Content skeleton

- Premise: a flock of simple agents with no leader, where three local rules produce lifelike group movement.
- Starts from one moving triangle in an empty box, with edge wrapping, as the building block.
- Each boid has a position, a velocity and a perception radius; only neighbours inside the radius count.
- Separation, alignment and cohesion each give a steering vector; a weighted sum of them drives the boid.
- Debug drawings of radii and steering arrows are used to show what each boid responds to.
- Weight tuning produces failure modes (scattering, clumping), each shown on screen.
- The naive all-pairs neighbour check gets slow; a spatial grid limits the comparisons; thousands of boids at the end.
- Closes on the full flock with a short recap of the three rules.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Finished flock already moving as a group; claim that three simple rules produce it. |
| 0:22 | toy-world | One triangle in an empty box at constant velocity; wraps at the edges. |
| 0:58 | definition | Define a boid by position, velocity and perception radius; only neighbours inside the radius matter. |
| 1:40 | brute-force | First attempt: every boid checks every other boid. Fine for twenty, expensive later. |
| 2:22 | demo-sim | Separation alone: boids push away from crowded neighbours; push arrows drawn on screen. |
| 2:55 | wall | Separation dominates; the flock scatters into lone boids drifting apart. |
| 3:30 | demo-sim | Add alignment: each boid steers toward the average heading of its neighbours; small groups start moving together. |
| 4:10 | analogy | Drivers on a busy road matching the car ahead, with no one in charge. |
| 4:45 | demo-sim | Add cohesion: boids steer toward the centre of their neighbours; the flock forms and holds shape. |
| 5:25 | wall | Frame rate falls as the count rises; the all-pairs loop is the cost. |
| 6:02 | derivation | Divide space into cells; each boid checks only its own and adjacent cells. Cost follows local density. |
| 6:50 | demo-sim | Thousands of boids with the grid running; weights change the character from tight to loose. |
| 7:35 | recap | The three rules again, one line each. |
| 8:05 | coda | Wide shot of the flock; closing thought on how little code this takes. |

## Narration

<<<NARRATION
So here is the goal. We want a whole flock of these little triangles moving around like birds or fish, and nobody is steering the group. There is no leader. Every boid just looks at its neighbours and does something simple. The surprising part is how much of the flock's behaviour falls out of three rules.

Let's start with just one of these things. Here is a single triangle in an empty box. It has a position and a velocity, and every frame we move it by that velocity. When it reaches an edge it wraps around to the other side. That is it. Nothing interesting yet, but this is going to be the starting point for everything, so it is worth getting it working properly before we add anything.

Now, what is a boid? Really it is three things. A position, a velocity, and a perception radius. The radius is the important bit. A boid can only see the other boids that are inside a circle around it. Anything outside that circle simply does not matter to it. Keep that in mind, because the whole idea of flocking depends on local information. No boid knows what the whole flock is doing.

The obvious first approach is brute force. For each boid, loop over every other boid, check the distance, and if it is close enough, use it. I'll be honest, this is the first thing I tried, and it works fine for a small number. Twenty boids, no problem. But it is going to cost us later, so let's note that and move on for now.

Next up is the first rule, separation. If two boids get too close, they should push apart. So for each neighbour that is too near, we compute a vector pointing away from it, and we add those up. I have drawn the push vectors on screen as little arrows so you can see what each boid is responding to. If you watch the arrows, you can see the boids spreading out from one another, which is exactly what we asked for.

But now here is the problem. If we only use separation, the boids just run away from each other. They don't flock at all. Each one is more interested in its personal space than in the group, and the whole thing scatters. Look at that. Single boids drifting off on their own, never meeting again. That is a useful failure, because it tells us we need something else pulling them together.

So the second rule is alignment. Each boid looks at its neighbours, works out their average heading, and steers a little toward that. Now a boid that is heading left will gradually turn if the boids around it are heading right. The moment we add this, the flock starts to behave like a group. Small clusters begin to move in the same direction, and you can see them forming and dissolving as boids drift in and out of range.

It reminds me of driving on a busy motorway. Nobody tells you your speed. You just match the car in front, roughly, and somehow the whole lane flows. That is basically alignment. I like this rule a lot, because it does not need anyone to be in charge, and it is very easy to explain to someone who has never written any code.

The third rule is cohesion. Each boid finds the centre of its neighbours and steers toward that point. Separation keeps them apart, alignment keeps them moving the same way, and cohesion keeps them from wandering off on their own. Add it, and suddenly you get a flock that holds together and turns as a unit. This is the first moment where I actually stopped and watched, because it looked like something real.

What really matters here is the weights. Each rule gives a steering vector, and we add them up with a multiplier on each one. Crank up separation and you get the scattering again. Crank up cohesion and the boids clump into a dense ball that barely moves. The good looking flocks are a balance between the three. I spent a while going back and forth with these numbers, and I would encourage you to do the same, because the right values are not obvious from reading the code.

There is also a limit on how hard a boid can turn in one frame. Without it, the steering vectors can spin a boid around almost instantly, and the motion looks twitchy and unnatural. So we clamp the steering force to a maximum, and we clamp the speed too. Those two numbers do more for the feel of the flock than almost anything else, which is a good reminder that the look of a simulation often lives in the constraints rather than the rules.

Now, there is a cost I have been quietly ignoring. Every boid checks every other boid, every frame. That is a number of comparisons that grows with the square of the count. Double the boids and you quadruple the work. And that is exactly what happens here. The frame rate starts dropping once we get into the hundreds. Watch the counter in the corner. It is not pretty, and it is a bit of a shock after how smooth things looked with twenty.

So the fix is to stop checking everything. Imagine dividing the space into a grid of cells. Each boid only needs to look at boids in its own cell and the cells touching it. Most of the far away boids never even get considered. The work now depends on how many boids are around you, which is what we actually care about, not on the total number in the whole world.

Let me be clear that this is an approximation of the full neighbour search. A boid that sits just over a cell boundary still has to check the cell next door, so the bookkeeping has to be right. Get that wrong and boids seem to ignore their neighbours at the edges of cells. I did get that wrong at first, and you can see the flock visibly split along the grid lines for a moment. Fixing it was just a matter of looking at the neighbouring cells properly, and then the split was gone.

With the grid in place, the frame rate is back. Now let's go big. Thousands of boids, all moving, all following the same three rules. The flock flows like a fluid. There are ridges and streams and splits and merges, and none of it is scripted anywhere. Change the weights and you get a totally different character. Tight and busy, or loose and calm, or something in between that I did not expect at all.

So to recap. Separation keeps boids apart. Alignment makes them match direction. Cohesion pulls them toward the middle of their neighbours. Each rule only looks at what is nearby. The speed trick is a grid, so each boid only compares against its own neighbourhood. And the look of the whole thing depends on the weights and the limits you give it.

That's pretty much it. Three simple rules, a bit of tuning, and some careful bookkeeping. Here is the whole flock one more time, because it still looks good to me after all this time. Thanks for watching, and I will see you in the next one.
NARRATION>>>

## Slots

```json
{
 "format_class": "build-along simulation, rules then optimisation",
 "answer_given_upfront": true,
 "hook_type": "spectacle-demo",
 "first_question_frac": 0.04,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.04,
 "first_notation_frac": 0.11,
 "payoff_frac": 0.8,
 "misconception": "staged-early",
 "brute_force_first": true,
 "examples_count": 4,
 "example_growth": "one boid -> dozens -> thousands",
 "roadmap": "one-line",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.28,
 "caveat_type": "approximation",
 "recurring_anchor": "the single triangle boid, reused in every rule demo",
 "sponsor_frac": null,
 "ending_type": "impact-coda",
 "teaser": false,
 "wpm": 170,
 "median_beat_s": 37,
 "beat_sequence": ["hook", "toy-world", "definition", "brute-force", "demo-sim", "wall", "demo-sim", "analogy", "demo-sim", "wall", "derivation", "demo-sim", "recap", "coda"],
 "top5_moves": ["simulation-as-argument", "brute-force-first", "failure-shown", "analogy", "build-and-verify"],
 "absent3_moves": ["inline-quiz", "expert-dialogue", "second-person-role"]
}
```
