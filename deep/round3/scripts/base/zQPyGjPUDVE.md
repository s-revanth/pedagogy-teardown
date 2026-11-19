# SebastianLague / zQPyGjPUDVE

- Channel: SebastianLague
- ID: zQPyGjPUDVE
- Title: Introduction to Game Development (E04: writing code)
- Duration: 756 s (12:36)
- Condition: base
- recall: vague

## Content skeleton

- Goal: make the cube move from code the viewer can read line by line, ending with keyboard control.
- A script is a class attached to an object; it inherits from the engine base class and hooks into the frame loop.
- Start runs once and Update runs every frame; most logic goes in Update.
- First test: print a message to the console to prove the script runs.
- Brute force: add a fixed amount to position every frame; the speed depends on the frame rate.
- Fix: multiply by the time since the last frame so speed is per second; a public speed field tunes it in the inspector.
- Input: read the horizontal axis and steer the cube with the arrow keys.
- Compile error shown on purpose; reading the console message to find and fix it; recap and teaser.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Question: can a cube move because of text typed into a file? Cube sits idle in the scene. |
| 0:40 | roadmap | Goal: keyboard control by the end, with every line explained. |
| 1:10 | definition | A script is a class attached to an object; it inherits from the engine base class. |
| 2:10 | toy-world | Empty Start and Update methods; a message printed to the console on Play. |
| 3:00 | demo-sim | Console output confirms the script runs; the message is the first proof that code is alive. |
| 4:00 | brute-force | Add a fixed amount to position each frame; the cube races across the screen. |
| 5:00 | wall | Frame rate changed; the cube speeds up or slows down, so the speed is wrong on other machines. |
| 5:50 | misconception-defuse | Update does not run at a fixed rate; multiply by the time since the last frame. |
| 6:40 | demo-sim | Public speed field tuned in the inspector; the cube moves the same at high and low frame rates. |
| 7:50 | analogy | Speed like a speedometer: distance per second, not distance per glance. |
| 8:30 | demo-sim | Read the horizontal input and steer with the arrow keys; hold, release, reverse. |
| 9:40 | wall | Deliberate typo; the editor refuses to run and the console points to the line and column. |
| 10:20 | recap | Base class, Start, Update, console, delta time, input, reading errors. |
| 11:20 | teaser | Next episode: how scripts are organised and talk to one another. |

## Narration

<<<NARRATION
Up until now we have been working in the editor, dragging things around and clicking buttons. In this episode we write our first script, and get the cube to move by itself. Writing code can feel like a wall if you have never done it, so I'm going to go slowly, and show you the mistakes I make along the way. Those mistakes are part of the lesson.

Here is the goal. By the end, the cube should respond to the keyboard, and we should understand every line we wrote. The plan has four steps. Look at what a script is, write a tiny one that prints a message, make the cube move in a way that exposes a problem, and then fix that problem properly.

Let's start with what a script is. In Unity, a script is a file of code that describes behaviour. You attach it to an object in the scene, and the object runs the code while the game plays. The script is a class, which is a blueprint, and the object it sits on is one instance of that blueprint. We covered classes last time, so that part should feel familiar.

Here is the file. It is a class that inherits from something called MonoBehaviour. That is the base class Unity gives us, and it is what lets our script hook into the game loop. Inside, there are two special methods. Start runs once, when the object first becomes active. Update runs every frame. Almost all of our code will go in one of those two.

Let's try the smallest possible thing. In Start, I print a message to the console. I attach the script to the cube, press Play, and the message appears at the bottom of the editor. That is a useful first step, because it proves the code is actually running. If that message does not appear, nothing else will work, so it is worth checking before anything fancy. I always do this now, even when I think I know what I am doing.

Now let's move the cube. The obvious approach is to change its position inside Update. Each frame, I add a fixed amount to the x position. Press Play, and the cube slides across the screen. It works. It also looks very fast, much faster than I wanted. It covers a long way in a short time. That is the brute force version, and it has a problem I want to show you.

The problem is that Update runs once per frame, and the number of frames per second is not fixed. On a fast computer, Update runs many more times per second than on a slow one. So if I add the same amount every frame, the cube moves faster on a fast machine and slower on a slow one. I can show that by changing the frame rate limit. At a higher limit the cube speeds up. At a lower limit it slows down. The code is correct line by line, but the speed depends on the machine, and that is wrong.

The fix is to use the time since the last frame. Unity gives us a value called delta time, which is how long the previous frame took, in seconds. If I multiply the movement by delta time, each step gets smaller when frames are quick and bigger when they are slow. Over one second the total distance is the same, whatever the frame rate. That is the key idea. Speed should be per second, not per frame.

I want to slow down on that, because it is easy to get wrong. Think of a speedometer in a car. It tells you distance per hour, not distance per glance at the dashboard. A speed of five means five units per second. If you forget that, and write five units per frame, you get exactly the frame-rate dependence I just showed. So from now on, any movement you write should multiply by delta time.

I'll also add a public speed field to the script. Public fields show up in the inspector, so I can tune the number without editing the code and recompiling. I set it to five and leave it there. Then I test it. I change the frame rate limit to a high value, then a low one. The cube moves at the same speed both times. That is the result we wanted, and it is satisfying, because the behaviour no longer depends on the machine running it.

Now let's make the cube respond to the keyboard. Unity has an input system that lets us read whether a key is held. I'll read the horizontal axis, which gives a value between minus one and one, depending on whether the player holds the left or right key, or neither. Multiply that value by the speed and by delta time, and use the result to move the cube. Now the arrow keys steer it.

Let me check that it behaves. Hold right, and the cube moves right. Release, and it stops. Hold left, and it moves left. This is the moment the cube starts to feel like a game object. It reacts to a person, and the code is the thing deciding how it reacts. Nothing here is complicated, but the combination of input, speed and time is the basis of almost every movement in a game.

Now something went wrong on purpose, so I can show you the error. I typed a variable name slightly wrong in one line, and the editor shows a red mark. If I press Play, the editor refuses to run and says the name does not exist. The message points to the file, the line and the column. Read that message carefully. It tells you what is wrong and where, and once you learn to read these, they stop being scary.

I fix the typo, save, and the error goes away. That is the normal loop. Write a little, save, check the console, fix what it says. You do not need to write the whole program before testing. Test as you go, and let the console tell you what is wrong. The people who get stuck are usually the ones who write two hundred lines and then press Play for the first time.

I should be honest that this is still a small example. A real game has many scripts, and they need to talk to each other, which is a whole topic in itself. For now, the important point is that the cube moves because of code we wrote, and the movement does not depend on the frame rate. That is a real foundation, and most of what follows builds on it.

So to recap. A script is a class attached to an object. Start runs once and Update runs every frame. Print messages to the console to confirm the code runs. Multiply movement by delta time, so speed is per second. Read input and use it to steer. And read the console errors carefully, because they tell you exactly what to fix.

Next time, we will look at how scripts are organised and how they can talk to each other. You will see why the cube is only the beginning. Thanks for watching, and I'll see you in the next one.
NARRATION>>>

## Slots

```json
{
 "format_class": "build-along tutorial, one script",
 "answer_given_upfront": true,
 "hook_type": "question",
 "first_question_frac": 0.03,
 "first_concrete_object_frac": 0.01,
 "first_new_idea_frac": 0.09,
 "first_notation_frac": 0.09,
 "payoff_frac": 0.6,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "printed text -> fixed step -> keyboard input",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.4,
 "caveat_type": "approximation",
 "recurring_anchor": "the default cube and the speed field in the inspector, reused in every section",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 55,
 "beat_sequence": ["hook", "roadmap", "definition", "toy-world", "demo-sim", "brute-force", "wall", "misconception-defuse", "demo-sim", "analogy", "demo-sim", "wall", "recap", "teaser"],
 "top5_moves": ["build-and-verify", "brute-force-first", "failure-shown", "visible-repetition", "analogy"],
 "absent3_moves": ["inline-quiz", "expert-dialogue", "generalize-to-other-domains"]
}
```
