channel: SebastianLague
id: v1V3T5BPd7E
title: Kinematic Equations (E01: introduction)
duration: 377s (6:17)
condition: v3
recall: none
exemplars read: deep/corpus/compact/phMZQNu0ZFM.txt, deep/corpus/compact/IvT8hjy6q4o.txt

## Content skeleton
- Open on a personal story: a ball in a game that fell at a speed I did not expect, because I guessed at the physics.
- Name the five quantities: displacement, initial velocity, final velocity, acceleration, and time.
- State the three kinematic equations and what each one connects.
- Work one example by hand: a ball from rest, accelerating for 3 seconds.
- Explain how to pick the equation that contains only the unknown, and why the sign convention matters.
- Show how a simulation checks the algebra, and name the constant-acceleration limit.
- Close on the next problem, a harder one with two moving objects, and a teaser.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Story: a ball in a game fell at the wrong speed, and guessing the physics was the cause |
| 0:40 | definition | Five quantities: displacement, initial velocity, final velocity, acceleration, time |
| 1:20 | definition | Three kinematic equations and what each connects |
| 2:00 | derivation | Worked example: ball from rest, accelerating for 3 seconds, find velocity and distance |
| 3:00 | derivation | Choosing the equation that contains only the unknown |
| 3:40 | caveat | Sign convention: up positive, gravity negative |
| 4:20 | demo-sim | Checking the algebra with a small simulation |
| 5:00 | caveat | Constant acceleration is the assumption behind every formula |
| 5:40 | teaser | Next episode: two moving objects and a catch |

## Narration
<<<NARRATION
A while ago I tried to make a ball drop in a game, and it fell at a speed I didn't expect. The ball looked fine, but the timing felt wrong, and no amount of tweaking fixed it. The problem was that I was guessing at the physics instead of working it out. So this first episode is about the kinematic equations, which let us describe motion precisely when the acceleration stays constant. If you have ever dropped something from a height, you already know this kind of motion. The equations let us predict where something will be, and when it will get there, before we run anything.

Let's begin with the quantities we use, because we need a shared vocabulary before any algebra. Displacement is how far something moves in a straight line, including direction. Initial velocity is the speed and direction at the start, and final velocity is what it is at the end. Acceleration is how fast the velocity changes, and time is how long the motion lasts. There are five quantities in total, and knowing a few of them is enough to find the rest. That's the whole idea behind the method. We use this trick constantly, and it works for almost every constant-acceleration problem.

The kinematic equations give us the link between these values. The first is v equals u plus a t, which says the final velocity is the starting velocity plus acceleration times time. The second is s equals u t plus half a t squared, which gives the displacement. The third is v squared equals u squared plus 2 a s, which connects velocity and displacement without needing time at all. The first and second are the ones we use most often, and the third is the one we reach for when time is unknown.

Now let's work an example by hand. Suppose a ball starts from rest and accelerates at 10 metres per second squared for 3 seconds. We set the starting velocity to rest, and we read the acceleration and time straight from the problem. We can use the first equation to find the final velocity. Plugging in gives 10 times 3, which is 30 metres per second. The second equation gives the distance covered, which is half of 10 times 9, or 45 metres. We check the answer with a quick sketch, and the numbers look sensible for a ball that has been falling for three seconds.

Choosing the right equation is the key skill. We list the known values first, and then we ask which equation contains only the unknown we want. If the time is missing, the third equation is usually the friendliest choice. We can often cut a problem down to a single line this way. Each unknown needs just a single equation, and everything after that is arithmetic. I always write the list down first, because it stops me from grabbing the wrong formula in a hurry.

Signs matter, and this is where many people get tripped up. We choose a direction as positive, usually up, and every quantity along that direction takes its sign from that choice. Gravity points down, so its acceleration is negative, about minus g, which is the value we just used. A ball thrown upward might start with a positive velocity, and its acceleration is still negative. We can see why in the sketch, because the arrows point in opposite directions. I make a small sketch every time, because a wrong sign quietly ruins the whole answer.

Here is a quick habit that saves us a lot of trouble. We write the units next to every value, so that a metre never gets mixed up with a second. We check that both sides of each equation have the same units, and we only accept an answer when it passes that check. We also keep the sign of each value in view as we go. When we follow those steps, we rarely get a surprise at the end. You can do that check on paper, and we can trust the result much more.

We can check the algebra by building a simulation, such as a small Unity scene where the ball falls under gravity. The simulated position at each time should match the value from the equation. If the numbers disagree, the simulation is a fast way to find out whether the algebra or the code is wrong. We often find that the mistake is in the setup, not in the physics. You will see that for yourself when we run it, and we can compare the two results side by side.

These equations assume constant acceleration, which is a big assumption. Air resistance changes the acceleration as speed grows, so a falling object only follows these formulas roughly over short times. We need to be honest about that limit. Within the range where acceleration is steady, the equations are exact, and they give us a precise picture. I think that's a good place to start, and it's the foundation for everything that follows. We can think of the equations as a model, and every model has a range where it works. Inside that range we can rely on them completely. Outside it, we need a better model, and we have to go back to the physics. We will return to that idea whenever the motion stops being simple.

In the next episode, a harder problem appears: two objects moving at the same time, where one has to catch the other. I'm looking forward to working through that one, and we can check the answer in code once the algebra is done. You can try it on paper before the next video, which is a good exercise.
NARRATION>>>

## Slots
```json
{
 "format_class": "tutorial series episode, worked physics example with simulation check",
 "answer_given_upfront": false,
 "hook_type": "story-anecdote",
 "first_question_frac": 0.1,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.1,
 "first_notation_frac": 0.3,
 "payoff_frac": 0.85,
 "misconception": "mid-video-correction",
 "brute_force_first": false,
 "examples_count": 2,
 "example_growth": "one ball from rest, then the sign convention, then a simulation",
 "roadmap": "none",
 "viewer_turn": "none",
 "viewer_turn_frac": null,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the falling ball, reused in every section",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 157,
 "median_beat_s": 40,
 "beat_sequence": ["hook", "definition", "definition", "derivation", "demo-sim", "derivation", "caveat", "demo-sim", "caveat", "teaser"],
 "top5_moves": ["story", "minimal-definition-then-refine", "toy-world", "simulation-as-argument", "honest-caveat"],
 "absent3_moves": ["brute-force-first", "hook-question", "expert-dialogue"]
}
```

```json
{"verified_trace": {"wpm": "PASS 157.00 (target 151.95-160.05, median 157.14)", "you_rate": "PASS 0.52 (target 0.45-0.85, median 0.53)", "i_rate": "PASS 0.84 (target 0.67-1.58, median 0.96)", "we_rate": "PASS 4.49 (target 3.45-5.4, median 4.89)", "num_rate": "PASS 1.88 (target 1.3-2.33, median 2.04)", "hedge_rate": "PASS 0.21 (target 0.13-0.36, median 0.28)", "example_rate": "PASS 0.21 (target 0.06-0.26, median 0.12)", "q_rate": "PASS 0.00 (target 0.0-0.0, median 0.0)", "sent_len": "FAIL 15.95 (target 18.62-20.56, median 20.56)", "switch_sponsor": "PASS detected=False default=OFF", "switch_teaser": "PASS detected=True default=ON", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (story-anecdote vs story-anecdote)", "ending_type": "MATCHES default (teaser-next vs teaser-next)", "summary": "8/9 numeric targets pass"}}
```
