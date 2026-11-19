# Header
- channel: SebastianLague
- id: bqtqltqcQhw
- title: Coding Adventure: Boids
- duration: 515 s (8:35)
- condition: v1
- recall: vague

## Content skeleton
- Flocking simulation (boids): each agent follows three local rules, with no leader.
- Toy world: one triangle with a position, a velocity, and wrap-around edges.
- All-pairs neighbour check first, then the cost of it at scale.
- Separation, alignment and cohesion, each defined minimally as a steering vector.
- Cohesion first fails (one blob) because the neighbour radius is too large.
- Repeatable test: same random seed, one weight swept at a time.
- Speed fix with a spatial grid, timed before and after on the same scene.
- Honest caveat about how well this matches real birds or fish; teaser for the next step.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Flock of triangles wheeling on screen; no leader, so how is it made? |
| 0:25 | roadmap | One boid, three rules, then the speed fix |
| 0:45 | toy-world | One triangle at fixed speed, wrapping at the screen edge |
| 1:30 | brute-force | Each boid loops over every other boid; a neighbour radius is added |
| 2:40 | wall | Frame rate collapses at a few thousand boids; the all-pairs loop is the cost |
| 3:20 | definition | Separation as one minimal steering vector: push away from close neighbours |
| 4:10 | demo-sim | Separation alone; boids spread out; weight slider |
| 4:45 | definition | Alignment: steer toward the average heading of neighbours |
| 5:30 | demo-sim | Alignment alone; small groups with matching headings |
| 6:05 | misconception-defuse | Cohesion makes one blob; the radius was far too large, so every boid saw the whole flock |
| 6:50 | demo-sim | Cohesion weight swept with the same seed on every run |
| 7:30 | payoff | All three rules together; the flock holds shape |
| 7:50 | analogy | Walking through a crowd and keeping an arm's length |
| 8:00 | caveat | Not sure how close this is to real birds or fish |
| 8:15 | teaser | Next: a spatial grid and more boids |
| 8:28 | coda | Sign-off; suggestion to change one number at a time |

<<<NARRATION
This is a flock of boids. Each triangle is one boid, and nobody is steering the whole group. There is no leader and no script for the shape. So how do you get something like this? That is what we are going to work out.

Here is the plan. We start with a single boid, add three simple rules, and then deal with the speed problem that shows up as soon as there are a lot of them.

Let's start with one triangle. It has a position and a velocity, it moves at a fixed speed, and when it reaches the edge of the screen it wraps around to the other side. That is the whole toy world. It is a bit boring, but it means that every later bug will be about the rules and not about the setup.

Now the boids need to notice each other. The simplest way I can think of is to make each boid check every other boid, and if another one is close enough, it counts as a neighbour. That is a double loop over every pair. For a hundred boids that is ten thousand checks per frame, and it runs fine. I am not proud of it, but we will get to that.

Each neighbour gives a small vector, and each rule turns those vectors into a steering push. We add the pushes up, cap the speed so nothing goes crazy, and move on. Every rule is just a different way of summing up the neighbours.

The first rule is separation. If a neighbour is too close, steer directly away from it. That is the entire definition: add a little push away from anything nearby, weighted by how close it is. Here is what it does on its own.

Okay, the boids spread out. They do not overlap, and each one keeps a little personal space. If I turn the separation weight down to zero, they go back to clumping. If I turn it way up, they become jittery, because they are constantly dodging. The slider does exactly what it says, and that is the nice thing about one slider per rule. You can tell which rule did what.

The second rule is alignment. Look at your neighbours and steer toward their average heading. Again, that is the definition. On its own it makes small groups that all point the same way. They look like a school of fish that has lost its nerve, but they are clearly paying attention to each other.

The third rule is cohesion. Steer toward the average position of your neighbours. This is the one I expected to make a nice flock. The first time I turned it on, everything collapsed into one big blob in the middle of the screen, and I spent a while staring at it, wondering what I had broken.

It turns out the code was not broken. The neighbour radius was far too big. Every boid could see almost the whole flock, so its average neighbour position was roughly the centre of the screen, and everyone steered there. I had the radius set too large. When I shrink it, the flock holds together without collapsing. The fix is simple, but I should have checked the radius before blaming the rule. When something collapses, check what each agent can actually see.

Now I want to see the cohesion weight across a range, and I want the test to be the same every time. I fix the random seed, so every run starts with the same boids in the same places. Then I sweep the weight from low to high and watch the shape change. At low values the flock falls apart. At high values it becomes a blob again. In the middle you get something that looks like a flock.

That repetition is what I trust here. If the starting positions change every time, I cannot tell whether a change came from the rule or from the random start. Same start, same sweep, and the only thing changing is the one number. You can diff two runs by eye, and that is much more convincing than me telling you what to look for.

Here is what it looks like with all three rules at once. Separation keeps them apart, alignment makes them point the same way, and cohesion keeps them together. Nobody tells any boid to join a flock. The shape comes from three local decisions, made over and over, by every boid, every frame.

It is a bit like walking through a crowded train platform. You do not plan a route. You keep a comfortable arm's length from the people near you, you drift in the general direction they are moving, and you lean slightly toward the group. Nobody is in charge, and yet there is a shape.

Now, the speed problem. With all-pairs checks, a thousand boids means about a million comparisons every frame, and the frame rate falls off a cliff. I tried a few thousand and the simulation basically stopped. That is the cost of the dumb version, and I wanted to show it to you before fixing it, so you can see why the fix matters.

The fix is a spatial grid. Put each boid into a cell of a grid, and only check boids in the nearby cells. Most of the comparisons disappear, because most boids are far away from any given boid. I am going to time the same scene before and after, with the same count, so that the change is not just a feeling. Before, the frame time is in the tens of milliseconds. After, it is a small fraction of that. The numbers are on screen, so you can check them yourself.

One more thing I got wrong on the way. Early on I forgot that a grid cell must be at least as wide as the neighbour radius, otherwise you miss boids on the far side of a cell boundary. The flock still looked okay, which is the dangerous part. A wrong result that looks plausible is much harder to catch than a crash. So after the grid went in, I compared the neighbour counts from the brute-force loop and the grid on the same frame. They matched, and only then did I trust the speed number.

Now the honest bit. I do not know how close this is to how real starlings or fish behave. I took three rules that are easy to describe, and they produce a shape that looks right. I have not measured birds, and I am not claiming that is how they do it. It is a model that makes a flock. That is all I have shown.

The next step is to make the neighbour search fast enough for a lot more boids, and then to see what the rules do when the flock hits the edges and does not simply wrap. We will see how far the grid gets us.

So that is the flock. Three rules, one radius, one seed, and a sweep. If you want to try it, change one number at a time and watch what moves. Thanks for watching.
NARRATION>>>

## Slots

```json
{
 "format_class": "build-break-fix devlog, rule by rule",
 "answer_given_upfront": true,
 "hook_type": "spectacle-demo",
 "first_question_frac": 0.02,
 "first_concrete_object_frac": 0.01,
 "first_new_idea_frac": 0.17,
 "first_notation_frac": 0.52,
 "payoff_frac": 0.8,
 "misconception": "mid-video-correction",
 "brute_force_first": true,
 "examples_count": 4,
 "example_growth": "one boid -> 100 -> thousands with grid",
 "roadmap": "one-line",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.02,
 "caveat_type": "epistemic",
 "recurring_anchor": "the boid count and frame time shown in the corner, checked after each change",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 35,
 "beat_sequence": ["hook","roadmap","toy-world","brute-force","wall","definition","demo-sim","misconception-defuse","demo-sim","payoff","analogy","caveat","teaser","coda"],
 "top5_moves": ["toy-world","brute-force-first","failure-shown","visible-repetition","honest-caveat"],
 "absent3_moves": ["hook-paradox","inline-quiz","expert-dialogue"]
}
```
