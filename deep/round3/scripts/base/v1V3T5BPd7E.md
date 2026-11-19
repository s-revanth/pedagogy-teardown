# SebastianLague / v1V3T5BPd7E

- Channel: SebastianLague
- ID: v1V3T5BPd7E
- Title: Kinematic Equations (E01: introduction)
- Duration: 377 s (6:17)
- Condition: base
- recall: vague

## Content skeleton

- Question: how far does a dropped ball fall after two seconds, and can the answer be calculated and checked?
- Defines kinematics as describing motion without yet explaining its cause.
- Single object on a straight track; position, velocity and acceleration defined with a position-time graph.
- Constant velocity gives a straight line whose slope is the velocity.
- Naive estimate (velocity times time) fails once acceleration is constant; the simulation shows the gap.
- Derivation via the area under the velocity graph: a rectangle plus a triangle gives the standard formula.
- The formula is checked against a falling-ball simulation at one and two seconds.
- Two dimensions: a jump splits into independent horizontal and vertical parts; caveat about air resistance.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Ball dropped in a simulation; question of how far it has fallen after two seconds. |
| 0:30 | roadmap | Build the equations slowly and check each step against a simulation. |
| 0:55 | toy-world | One dot on a straight track, with a zero point and one number for its position. |
| 1:40 | definition | Position, velocity and acceleration defined; position is the where, velocity its rate of change. |
| 2:20 | demo-sim | Zero acceleration gives a straight position-time line; slope is velocity. |
| 2:55 | wall | Naive velocity-times-time estimate is wrong once velocity changes; the simulation shows the gap. |
| 3:30 | derivation | Area under the velocity graph splits into a rectangle and a triangle, giving the formula. |
| 4:20 | demo-sim | Formula predicts the falling ball at one and two seconds; simulation matches. |
| 5:00 | generalize | Closed form predicts landing time; the same tools apply to thrown objects in games. |
| 5:40 | teaser | Next episode: looking at the formulas more closely and using them in code. |

## Narration

<<<NARRATION
Kinematics sounds like a scary word, but it is just the description of how things move, without yet worrying about why. Where something is, how fast it is going, and how those change over time. If you want anything to move in a game, you will end up using these ideas, whether you know their names or not. So this episode starts the series. We build up the equations slowly, and check every step against a simulation.

Here is the question to keep in your head. If I drop a ball from a height, how far has it fallen after two seconds? You could guess. You could measure it in a simulation. But I want to calculate it, and be confident the calculation matches the simulation. That is the whole goal of this series.

Let's start with something very simple. A single object on a straight track. We only care where it is along that track. I'll represent it as a dot, and the track has a zero point. The dot's position is one number, how far it is from that point. Hold on to that, because everything else builds on it.

Now let's define the three quantities. Position is where something is. Velocity is how fast that position is changing, and in which direction. Acceleration is how fast the velocity is changing. These words get mixed up all the time, so let's pin them down. Position is the where. Velocity is the rate of change of where. Acceleration is the rate of change of that.

First, what happens when acceleration is zero? The dot moves at constant velocity. I'll plot its position against time. The line is straight, and its slope is the velocity. Make the velocity bigger and the line gets steeper. The slope of a position graph is the velocity, and that link will do a lot of work for us.

Constant velocity is not what gravity does, though. So let acceleration be nonzero, and take the simplest case, where the velocity changes at a steady rate. The position graph now curves, getting steeper as time goes on. It is not obvious what the exact formula should be, and that is where we get stuck. I think it is worth being stuck for a moment.

Let me show the problem with a simple attempt. Find the distance by multiplying velocity by time, the way you would for a car at steady speed. That works for constant velocity. But when the velocity keeps changing, the answer is wrong, and the simulation shows the gap clearly. The ball always ends up a bit further than the naive estimate. That is the wall, and it tells us we need a better formula.

So let's derive one, slowly. Velocity is the change in position over a small interval. With constant acceleration, the velocity at any moment is the starting velocity plus acceleration times time. On a velocity graph, that is a straight line. The distance travelled is the area under that graph, because position is accumulated change. Under a straight-line velocity, the area splits into two shapes. A rectangle, starting velocity times time. And a triangle, half of acceleration times time squared.

Put those together and you get the standard formula. Position equals the starting position, plus the starting velocity times time, plus one half of acceleration times time squared. The formula is not magic. It is a rectangle and a triangle under a straight line. If you can see those two shapes, you will never forget where the one half comes from.

Now test it against the simulation. The ball is dropped from rest, with acceleration set to the standard value for gravity near the surface. At one second, the formula says the ball has fallen about half of that acceleration, in metres. The simulation shows the same number. At two seconds, the formula says four times as far, because time is squared. The simulation matches again. The prediction and the measurement agree, and that agreement is what I care about most.

Why check against a simulation at all? A formula can look reasonable and still be wrong, especially when signs and directions get mixed up. The simulation is an independent check. If they disagree, one of them is wrong, and you go looking for the mistake. If they agree, you can trust the formula more, though you should still be curious about why it works.

The same formula lets a game predict where a falling object will land. If you know the height and the acceleration, you can solve for the time to reach the ground, without simulating every frame. That only holds while the acceleration really is constant.

Constant acceleration is the key assumption, and it is also the caveat. Air resistance changes the acceleration as the object speeds up, and then the formula stops being exact. In most games we ignore that or use a simpler approximation. The formula describes an ideal situation, and you should always ask whether that situation is close enough for what you need.

Now two dimensions. A jump in a platform game is a good example. Horizontally, the character might move at constant speed, with no acceleration. Vertically, gravity gives a constant acceleration downward. The two motions happen at the same time but do not affect each other. You handle each direction with the same kind of equation, then combine the results to get the path.

That idea makes the rest of the series manageable. Break a motion into directions. Treat each direction as its own one-dimensional problem. Use the same formulas on each. Then put the results back together. A curved path stops being scary and becomes a small pair of problems.

So to recap. Position is where something is, velocity is how fast that changes, and acceleration is how fast the velocity changes. With constant acceleration, position follows a formula that comes from the area under a straight-line velocity graph. A simulation is the best way to check it. And in two dimensions, you split the motion into independent parts.

In the next episode, we look at these formulas more closely and start using them in code. We also deal with cases where acceleration is not constant, which is where things get more interesting. Thanks for watching, and I'll see you there.
NARRATION>>>

## Slots

```json
{
 "format_class": "series intro, sim-then-formula",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.03,
 "first_concrete_object_frac": 0.01,
 "first_new_idea_frac": 0.08,
 "first_notation_frac": 0.27,
 "payoff_frac": 0.69,
 "misconception": "staged-early",
 "brute_force_first": false,
 "examples_count": 3,
 "example_growth": "constant speed -> falling ball -> game jump",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.27,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the falling ball, reused in three sections",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 39,
 "beat_sequence": ["hook", "roadmap", "toy-world", "definition", "demo-sim", "wall", "derivation", "demo-sim", "generalize", "teaser"],
 "top5_moves": ["simulation-as-argument", "notation-after-concept", "toy-world", "minimal-definition-then-refine", "visible-repetition"],
 "absent3_moves": ["humor", "story", "second-person-role"]
}
```
