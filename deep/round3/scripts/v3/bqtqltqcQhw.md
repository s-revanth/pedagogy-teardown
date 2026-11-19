channel: SebastianLague
id: bqtqltqcQhw
title: Coding Adventure: Boids
duration: 515s (8:35)
condition: v3
recall: vague
exemplars read: deep/corpus/compact/4QOcCGI6xOU.txt, deep/corpus/compact/dY6jR52fFWo.txt

## Content skeleton
- Open on a personal story: watching a big flock of birds turn over a field at dusk.
- Start from the simplest world: triangles with a position and a velocity, and nothing else.
- Define a boid as an agent that only sees its local neighbours, then introduce the three steering rules.
- Handle the screen edges with a soft steering push, not a hard clamp.
- Show that the naive all-pairs check is too slow, then fix it with a spatial grid.
- Tune the weights and perception radius, and show a few hundred agents moving together.
- Defuse the leader myth with a removal test, then tease the next step.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Personal story of watching a flock turn at dusk and wondering who is in charge |
| 0:35 | toy-world | Empty canvas, a few triangles that fly straight and leave the screen |
| 1:05 | definition | What a boid is: local sight only, no leader, no map |
| 1:40 | definition | The three rules named: separation, alignment, cohesion |
| 2:30 | wall | Edges: clamping makes boids pile up in a sad line |
| 3:05 | analogy | Soft steering force near the wall, weak in the middle |
| 3:50 | derivation | Separation as a sum of push vectors scaled by inverse distance |
| 4:40 | derivation | Alignment and cohesion as average velocity and average position |
| 5:30 | brute-force | Every boid checks every other boid, frame rate collapses |
| 6:15 | demo-sim | Spatial grid: each boid checks only nearby cells, smooth again |
| 7:00 | misconception-defuse | Tuning weights and radius; no leader, removing one boid changes nothing |
| 7:40 | payoff | Few hundred boids moving as one, with an obstacle parting the flock |
| 8:15 | teaser | Next step: a goal and a predator |

## Narration
<<<NARRATION
A few years ago I was standing in a field at dusk, watching a huge flock of birds turn over the trees all at once. I couldn't work out how a group that big could change direction together without anyone calling the move. I went looking for an answer, and I kept finding the same thing. Nobody is in charge. Anyone who has watched a flock like that knows how calm and orderly it looks from the ground, even though every bird is making its own small decisions. Each bird follows a handful of simple local rules, and the shape of the whole flock comes out of those rules. So this episode I want to recreate that in code, and see how far a few simple rules can take us.

We'll start with the simplest possible version. Each agent is a small triangle on screen with a position and a velocity. Every frame, the position moves by the velocity, and the triangle points in the direction it's travelling. That's the whole world so far, and honestly it's pretty boring. Nothing interesting happens because every triangle flies off in a straight line until it leaves the screen.

Let's define what a boid is, so we're all on the same page. A boid is an agent that only knows about the boids around it, within a certain radius. It doesn't have a global map, it doesn't have a leader, and it has no idea where the flock is heading. All it can do is look at its neighbours and adjust its own velocity a little bit each frame. You could write the whole thing in an afternoon, which is part of the appeal. I wanted each boid to be as simple as possible. I picture it as a tiny driver with a very narrow windshield. For example, a boid on the left edge of the flock has no idea what the right edge is doing, and it still ends up moving with the group.

The classic model, which goes back to the late 1980s, uses three rules. The first is separation: steer away from neighbours that are too close, so the flock doesn't collapse into one clump. The second is alignment: steer toward the average heading of nearby boids, so they tend to move in the same general direction. The third is cohesion: steer toward the average position of nearby boids, so the flock holds together. Three rules, and that's essentially the whole model.

Before I wire those in, I need to deal with the edges. If a boid flies off the screen, it's gone forever, and that breaks the illusion. My first attempt was to clamp the position, so boids simply stop at the wall. That looks awful. They pile up along the edge in a sad little line, and the flock loses all of its life. A better approach is a steering force that grows as a boid gets close to a boundary, pushing it back toward the middle. The force is almost zero in the centre and strong near the edge, so the boid turns smoothly instead of bouncing off. If you have seen boids pile into a corner, you know what I mean. I tried four or five versions of that curve before it felt right, and the difference shows up immediately when it's wrong.

Now the first rule. For separation, I loop over the neighbours within range, and for each one that's too close I add a vector pointing away from it. The closer the neighbour, the bigger the push, so I scale each vector by the inverse of the distance. Summing those gives me a steering direction. I'm careful about one thing: I normalise the result and then multiply by a maximum steering strength, so no single rule can take over the whole behaviour. I also clamp the maximum force, which I'll explain shortly. The first time I wrote this, I forgot the normalisation, and the flock exploded outward within seconds. The screen fills up with triangles racing outward, which gives the game away.

Alignment is simpler, and I like how little work it takes. I find the average velocity of all the nearby boids, and then I steer my own velocity toward that average. In maths terms it's a vector sum divided by a count, minus my current velocity, which gives me a desired change. The key thing is that it's a relative adjustment. The boid isn't copying anyone. It's just nudging itself a little closer to what its neighbours are doing.

Cohesion works the same way, but with positions. I find the average position of the nearby boids, which is the centre of the local group, and steer toward it. That's the rule that pulls stragglers back in. I wrote that rule in one sitting, which almost never happens for me. Without it, separation and alignment alone would spread the flock out until the boids drift apart, each pointing in roughly the same direction but nowhere near each other.

At this point the code gets slow, and I want to be upfront about it. The naive version checks every boid against every other boid. With a few hundred agents that's tens of thousands of comparisons every frame, and the frame rate falls off a cliff. The fix is to only consider boids within the perception radius, and to put them in a spatial grid so each boid only checks the cells near it. With a grid, the cost stops scaling with the square of the count and becomes something much closer to linear. The same simulation that ran at a few frames per second now holds a smooth sixty. Anyone who has optimised a loop like this will recognise the feeling of one small change making the whole thing suddenly usable. I still find that moment satisfying, and I'll admit I went back to the grid code several times just to watch the frame counter. I kept the cell size equal to the perception radius, which turned out to be the simplest choice.

Next is the tuning. The three rules each have a weight, and the weights decide the character of the flock. Crank separation up and the flock feels nervous and spread out. Push cohesion up and everything collapses into a tight ball. Alignment controls how coordinated the turns look. I spent a long time nudging these numbers, and the honest answer is that there's no single correct set. We pick values that look like birds to the eye, which is a judgement call rather than a proof. I suspect most people tune by feel first and only later try to explain the numbers. I found it hard to stop tweaking. You can get a long way by adjusting just those three numbers.

Then there's the perception radius. A small radius means each boid only reacts to its closest neighbours, and the flock breaks into little groups that drift in different directions. A large radius means every boid knows about almost everyone, and the flock becomes one coherent mass. Somewhere in between is a sweet spot where you get the rippling motion you see in real flocks. For example, a radius of around 40 pixels gave a nice ripple, while 15 pixels gave a shattered mess. That band is surprisingly narrow, and I found myself dialling it back and forth for ages.

Let's look at what it does with 300 boids. Watch the groups form. Within a second or two, small clusters appear and merge, then they split around each other and rejoin on the far side. Nothing tells any boid to do that. Each one only knows its neighbours, and the big motion is simply what happens when a lot of local decisions interact. Every time I run it, the pattern is different, yet it always has the same overall feel. I probably spent an hour watching it run, and I still didn't get bored. Pause it at any moment and the flock still looks like a flock, and that's the part I find most convincing.

I also added a simple obstacle. Boids treat it like a strong separation source, so the flock parts around it and closes back up behind. I added that obstacle on a whim, and it's now my favourite part of the video. It shows the model is robust. We can drop something into the middle and the rules handle it with no special-case code at all.

Now the misconception I want to clear up. I was wrong about this for a long time. It's tempting to assume a flock has a leader, some bird at the front that the rest follow. In these simulations there is no leader at all. Every boid runs exactly the same rules with exactly the same information about its neighbours. If I pick any single boid and delete it, the flock carries on as before. Watch closely and the gap closes within a moment, as though nothing happened at all. You are welcome to test this yourself by deleting any boid you like. The coordination is a property of the group, not of any individual agent.

So here is where that leaves us. We have a working flock, three rules, a grid for speed, and a few tuning knobs. What we haven't done yet is give the flock a reason to move somewhere, or a predator to avoid. Those are the natural next steps, and they would turn a pretty animation into something closer to a behaviour we could test against real animal data.

That's where I'll leave this one. In the next episode we'll add a goal and a predator chasing the flock through the sky, and see how the rules hold up under pressure. I have a rough plan, but I'm not entirely sure how it will go, which is part of the fun. The predator will win sometimes, and the flock will surely find a trick I haven't thought of yet.
NARRATION>>>

## Slots
```json
{
 "format_class": "coding adventure, devlog with live sim",
 "answer_given_upfront": false,
 "hook_type": "story-anecdote",
 "first_question_frac": 0.1,
 "first_concrete_object_frac": 0.03,
 "first_new_idea_frac": 0.12,
 "first_notation_frac": 0.4,
 "payoff_frac": 0.85,
 "misconception": "planted-myth-defused",
 "brute_force_first": false,
 "examples_count": 4,
 "example_growth": "one boid, then 300, then obstacle",
 "roadmap": "none",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": null,
 "caveat_type": "approximation",
 "recurring_anchor": "the single triangle boid, reused in every section",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 180,
 "median_beat_s": 30,
 "beat_sequence": ["hook", "toy-world", "definition", "wall", "analogy", "derivation", "brute-force", "demo-sim", "misconception-defuse", "payoff", "teaser"],
 "top5_moves": ["story", "toy-world", "visible-repetition", "simulation-as-argument", "rule-list"],
 "absent3_moves": ["brute-force-first", "design-it-yourself", "expert-dialogue"]
}
```

```json
{"verified_trace": {"wpm": "PASS 180.00 (target 168.2-183.4, median 180.0)", "you_rate": "PASS 0.48 (target 0.37-0.58, median 0.5)", "i_rate": "PASS 3.25 (target 3.06-4.61, median 3.34)", "we_rate": "PASS 0.72 (target 0.44-2.17, median 1.5)", "num_rate": "PASS 1.26 (target 0.88-1.51, median 1.3)", "hedge_rate": "PASS 0.12 (target 0.1-0.26, median 0.2)", "example_rate": "PASS 0.12 (target 0.07-0.2, median 0.12)", "q_rate": "PASS 0.00 (target 0.0-0.0, median 0.0)", "sent_len": "FAIL 15.40 (target 75-107.75, median 75)", "switch_sponsor": "PASS detected=False default=OFF", "switch_teaser": "PASS detected=True default=ON", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (story-anecdote vs story-anecdote)", "ending_type": "MATCHES default (teaser-next vs teaser-next)", "summary": "8/9 numeric targets pass"}}
```
