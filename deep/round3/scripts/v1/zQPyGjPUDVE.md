# Header
- channel: SebastianLague
- id: zQPyGjPUDVE
- title: Introduction to Game Development (E04: writing code)
- duration: 756 s (12:36)
- condition: v1
- recall: vague

## Content skeleton
- Continue the cube from the last episode; the goal is code that moves it.
- A script is a class file attached to a GameObject as a component; Start and Update are the two methods that matter.
- Brute force: a fixed amount moved every frame, with a hard-coded speed.
- Compiler error from a typo, shown and fixed; the error message as the teacher.
- Misconception: Update does not run at a fixed rate; it runs once per rendered frame.
- Time.deltaTime makes movement independent of frame rate; the formula for distance per step.
- Caveat about simplifying what the compiler does; teaser for the next episode.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Something has to tell the cube to move; that something is code |
| 0:30 | roadmap | One script, one moving cube, then make the speed honest |
| 1:00 | toy-world | Cube from last episode, sitting still in the scene |
| 1:40 | definition | A script is a class attached as a component; Start runs once, Update runs every frame |
| 3:00 | brute-force | Add a fixed amount to position every frame; hard-coded speed |
| 4:30 | wall | Compiler error from a typo; the message points to the line |
| 5:30 | demo-sim | Fix the typo; cube moves; log prints the position each frame |
| 7:00 | misconception-defuse | Assumed Update runs at a fixed rate; it runs once per rendered frame |
| 8:00 | demo-sim | Multiply by time since last frame; compare two frame rates |
| 9:30 | derivation | Distance equals speed times time; the step is per frame |
| 10:30 | caveat | Simplifying what the compiler and engine do with the file |
| 11:20 | recap | Start, Update, deltaTime |
| 11:50 | teaser | Next episode: more about how scripts are organised |
| 12:20 | coda | Sign-off |

<<<NARRATION
Last time we made a cube and dropped it with physics. This time, the cube is going to move because of something we write. The thing that tells the cube what to do is code. So how does Unity know when to run that code? That is the question for this episode.

Here is the plan. We write one script, we make the cube move with it, and then we fix the speed so that it does not depend on how fast the computer is running. Those three steps cover most of what you will do in Unity from here on.

The toy world is the cube from last time, sitting still in the scene. Nothing is moving it, so it is a good place to start. The first thing I need is a script, which is a class file that I attach to the cube as a component. Remember that a component is something a GameObject has. A script is just one more kind of component, written by hand.

Let's define the two methods I will use, as small as possible. Start runs once, when the object first appears in the scene. Update runs every frame, over and over, until the object is removed. Those two are enough to build most simple behaviour. Start is for setting things up, and Update is for doing things every frame.

Now the dumb version. In Update, I add a fixed amount to the cube's position, every frame. Say it is a fixed number on the x axis. That is the simplest code that could possibly move the cube, and it does move it. I press Play, and it slides across the screen. That is the working brute-force version, and I want you to see that it works before I say what is wrong with it.

Then I make a typo. I leave out a character in the name of a variable, and I press Play. The editor stops and shows a compiler error. The message gives the file and the line number, and it points at the place where the name is wrong. I like errors like this. They are not always clear, but they always tell you where to look, and that is most of the job.

The habit I try to build here is to read the first error only. Compilers often report a cascade of follow-on errors after one real mistake. If you fix the first one and run again, half of the others usually disappear. Scrolling through a wall of red text and trying to fix everything at once is the slow way, and I have done it more than once.

I fix the typo, save, and press Play again. The cube moves. To check that the code is doing what I think, I print the position every frame to the console. The numbers go up in steady steps, one step each frame. That log is the test. It is the same test every time, so if the numbers change in some unexpected way, I know the change came from the code.

Now here is a mistake I made. I assumed that Update runs at a fixed rate, say sixty times a second, because that is what I had seen in a few examples. It does not. Update runs once for every frame that the computer draws, and the frame rate changes. On a fast machine the cube moves further each second. On a slow machine it moves less. The code is correct for one frame. The problem is that the number of frames per second is not something I controlled.

So I have to fix that. The fix is to multiply the movement by the time since the last frame. The engine provides that as a value called delta time. It is the amount of time that passed since the previous frame was drawn. Multiply the speed by it, and each frame moves the cube by a little less when the frames are quick, and a little more when they are slow.

Here is the formula, and I want to show it after the code, not before. Distance equals speed times time. That is the physics you already know. If the speed is in units per second and the time is in seconds, the distance for one step is the speed times the time for that step. The code is doing exactly that. The formula is a label for what the line of code is already doing.

It is also worth checking the units. The speed I set is in units per second, and the time from delta time is in seconds, so the product is in units. If I forgot the multiplication and wrote the speed on its own, the cube would move a fixed amount per frame again, and the test would look almost right on a fast machine. That is a mistake I have made, and the two-frame-rate comparison is exactly what catches it. The same test that proves the fix also proves that the fix is in the right place.

Now the comparison. I run the same scene at two frame rates, a higher one and a lower one, and I watch the cube's position after the same number of real seconds. Without delta time, the two runs end at different places. With delta time, they end in almost the same place. That is the test I needed. The speed no longer depends on the machine.

Here is the honest part. I am simplifying what the compiler and the engine do with this file. There is a whole process that turns the script into something the computer runs, and I am not going to walk through it. I also do not cover every detail of how Update is scheduled relative to physics, because that has its own rules. For this episode, the level of detail is enough to make the cube move correctly, and that is all I am claiming.

I also want to say that you should not trust the console alone. Printing numbers is useful, but the cube on screen is the real result. If the numbers look right and the cube looks wrong, something is off in the scene, not in the maths. So I check both, every time, before I believe a change.

So let's recap. Start runs once and sets things up. Update runs every frame and does the work. Delta time turns a fixed speed into a speed in real time. Those three ideas are what the code needs in order to behave the same on any computer.

Next time, we look at how scripts are organised, because one script will not be enough for a real game. A cube that moves is a good start, but a game has many objects that need to talk to each other. That is where the structure starts to matter.

Thanks for watching.
NARRATION>>>

## Slots

```json
{
 "format_class": "build-break-fix devlog, one script",
 "answer_given_upfront": true,
 "hook_type": "question",
 "first_question_frac": 0.02,
 "first_concrete_object_frac": 0.01,
 "first_new_idea_frac": 0.13,
 "first_notation_frac": 0.24,
 "payoff_frac": 0.72,
 "misconception": "mid-video-correction",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "fixed speed -> per-frame -> time-scaled",
 "roadmap": "one-line",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.02,
 "caveat_type": "approximation",
 "recurring_anchor": "the cube's position printed to the console after each change",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 63,
 "beat_sequence": ["hook","roadmap","toy-world","definition","brute-force","wall","demo-sim","misconception-defuse","demo-sim","derivation","caveat","recap","teaser"],
 "top5_moves": ["toy-world","brute-force-first","failure-shown","visible-repetition","notation-after-concept"],
 "absent3_moves": ["hook-paradox","expert-dialogue","analogy-breakpoint"]
}
```
