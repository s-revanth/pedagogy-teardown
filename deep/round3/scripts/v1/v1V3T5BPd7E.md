# Header
- channel: SebastianLague
- id: v1V3T5BPd7E
- title: Kinematic Equations (E01: introduction)
- duration: 377 s (6:17)
- condition: v1
- recall: vague

## Content skeleton
- A ball on a straight line, thrown upward, under constant acceleration.
- Minimal definitions: velocity as position change per second; acceleration as velocity change per second.
- Planted myth: acceleration means speeding up; a thrown ball decelerates on the way up.
- Brute force: step the ball forward in small time steps in a loop and compare after one second.
- Smaller steps bring the simulation closer to the exact answer.
- Area under the velocity graph gives the position; the kinematic equations fall out of it.
- Formula matches the simulation; generalise to any constant-acceleration motion.
- Caveat: air resistance is ignored; teaser for the next episode.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | A ball thrown up comes back down; why is the algebra so fiddly? |
| 0:25 | roadmap | Simulate first, then derive the equations from what we saw |
| 0:50 | toy-world | Ball on a number line moving at 10 metres per second |
| 1:30 | definition | Acceleration: how much the velocity changes each second |
| 2:10 | misconception-defuse | Acceleration is not speeding up; the thrown ball slows down on the way up |
| 2:50 | brute-force | Step the ball forward in small time steps in a loop; read off the height at one second |
| 3:40 | demo-sim | Halve the step size; the answer moves closer to the exact value; sweep |
| 4:20 | derivation | Area under the velocity graph gives position; the equation appears |
| 5:20 | demo-sim | Formula and simulation agree at one second |
| 5:40 | caveat | Air resistance is ignored in this model |
| 5:55 | generalize | Same equations for any constant acceleration, not just gravity |
| 6:08 | teaser | Next episode: the equations in more detail |
| 6:17 | coda | Sign-off |

<<<NARRATION
Throw a ball straight up, and it rises, slows, stops, and falls back down into your hand. The motion is simple to watch, but the algebra for it always seemed fiddly to me. So why is it so fiddly, and can we get the equations from something we can actually see? That is what this episode is for.

Here is the plan. We simulate the ball first, with nothing more than small steps. Then we look at what the simulation is doing, and derive the equations from that. The formula comes last, once you have seen the behaviour it describes.

The toy world is a ball on a straight line. It is a single number, its position, and it moves at ten metres per second to start with. The line is enough. Everything else will just be extra bookkeeping.

Let's define the two quantities we need, as small as possible. Velocity is how far the position changes each second. That is all it is. Acceleration is how much the velocity changes each second. Those are the two definitions, and I will not add anything to them until the simulation needs it.

Now a misconception I had to get rid of myself, and I suspect you have it too. Acceleration sounds like speeding up. It does not have to be. A ball thrown upward is accelerating downward the whole time, with gravity pulling it at about nine point eight metres per second, every second. On the way up, that acceleration is slowing the ball down. The velocity goes from positive to zero to negative. Acceleration is about the change, and the sign tells you the direction of the change. It is not a synonym for going faster.

So let's simulate. The brute-force method is to step the ball forward in small time steps. At each step, subtract a little from the velocity for the gravity, then move the position by the current velocity times the step. Repeat for as many steps as needed to reach one second. It is the most literal version of the physics, and it needs no algebra at all.

I run it with steps of one tenth of a second. After one second, the ball is somewhere around five metres above where it started. That is the number I want to check, so I will check it against the formula later. For now, the simulation is the reference.

Here is the test I am interested in. How accurate is the simulation? I halve the step size and run it again, and the answer moves closer to the true value. I halve it again, and it moves closer still. I run the same sweep for each step size, so you can compare the answers directly. The error shrinks as the steps get smaller. That is the first real insight: the simulation is an approximation, and you can make it better by taking smaller steps.

Now the derivation. Plot the velocity against time. It is a straight line, starting at ten and going down by nine point eight each second. The distance the ball travels is the area under that line. The area is a rectangle plus a triangle. The rectangle is the starting velocity times the time. The triangle is the change in velocity times the time, halved. Those two pieces give the position equation.

Look at what happened there. I did not start with a formula. I started with a picture of the velocity, and the formula is a label for the area I could see. If you give someone the equation first, they have to trust it. If you show them the area, they can check it themselves, and that is much harder to argue with.

Now the check. The formula says the position after one second is the starting velocity times one, plus half the acceleration times one squared. With ten and minus nine point eight, that gives about five point one metres. The simulation with the smallest step lands on the same number. The formula and the simulation agree. That is the test I was waiting for, because the simulation was a way to see what is going on, and now I have an independent answer that matches it.

I want to be clear about what this model leaves out. Air resistance is ignored. A real ball, thrown in a real room, slows down a bit more than this, especially at higher speeds, because the air pushes back. So the numbers here are for an idealised ball in a vacuum. For a ball like this, the difference is small over one second, but it grows over longer times, and I am not modelling it in this episode.

Here is the last point, and it is the one that makes the equations worth having. Nothing in this derivation was specific to gravity. Any motion with a constant acceleration follows the same equations. A car speeding up on a straight road, a trolley rolling down a slope, a ball dropped from a height. Different numbers, same shape. Once you see the area under the velocity graph, you can apply it to anything with a steady acceleration.

One more check before we finish. If the derivation is right, the position should also be right at other times, not only at one second. At half a second the formula gives about three point seven eight metres, and the simulation with the smallest step lands close to that as well. Checking a second point is cheap, and it catches a formula that happens to match at one time but is wrong in general. I do that every time I derive something, because a single matching number can be a coincidence.

So here is the recap. Acceleration is how the velocity changes, and the sign tells you the direction, not whether it is speeding up. A small-step simulation gets better as the steps get smaller, and it gives you something to check against. And the equations are the area under the velocity line, which means they work for any constant acceleration.

Next time we look at the equations in more detail, and we check each term against a simulation run. If you want to try this yourself, simulate the ball with a few step sizes, and see how far it is from five point one metres. That gap is the lesson.

Thanks for watching.
NARRATION>>>

## Slots

```json
{
 "format_class": "simulation then derivation",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.03,
 "first_new_idea_frac": 0.24,
 "first_notation_frac": 0.45,
 "payoff_frac": 0.85,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "one ball -> smaller steps -> any constant acceleration",
 "roadmap": "one-line",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.01,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the ball's height after one second, checked against the formula",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 30,
 "beat_sequence": ["hook","roadmap","toy-world","definition","misconception-defuse","brute-force","demo-sim","derivation","demo-sim","caveat","generalize","teaser"],
 "top5_moves": ["toy-world","brute-force-first","misconception-first","visible-repetition","generalize-to-other-domains"],
 "absent3_moves": ["hook-paradox","commit-to-answer","expert-dialogue"]
}
```
