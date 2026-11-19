# SebastianLague | zQPyGjPUDVE | Introduction to Game Development (E04: writing code)

- channel: SebastianLague
- id: zQPyGjPUDVE
- title: Introduction to Game Development (E04: writing code)
- duration: 756 s (12:36)
- condition: v2
- recall: vague (I recognise that a Unity beginner series exists, not this episode's content)
- class (step 0): over-10 min (12:36); format = designed-lesson series lesson (E04 label), code-along; answer not stated; topic = C# scripting basics (Start, Update, variables, input)
- exemplars read: deep/compact/-L-WgKMFuhE.txt (A* Pathfinding E01, 11:38) read in full for series structure; deep/compact/TURzbXTNaA0.txt (I Created a (terrible) Video Game Console, 9:21) read in full for the just-in-time explanation voice

## Content skeleton
- Premise: this part writes the first code, starting with one line of text in the console.
- Start runs once; Debug.Log proves the script is attached and running; the message is removed afterwards.
- Deliberate typo: red error on line 14, column 9; the fix is a capital letter.
- Variables as named boxes: float speed equals 5; printing the value, not the word, and the quotation-mark mistake.
- Update runs once per frame; the first movement works but depends on frame rate; numbers for the frame budget.
- deltaTime fix, with worked numbers at 60 and 30 frames per second; a note on clamping large steps.
- Input axes read the keys; a sign bug (cube moves the wrong way) found by hand-testing each direction.
- Generalise to rotation and vertical movement; test with speed at 10, 1 and 0; FixedUpdate teased as later; teaser on collisions.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Welcome: this part writes the first code; the cube should do something by the end. |
| 0:25 | toy-world | The cube from last time, still standing still in the scene. |
| 0:55 | demo-sim | New C# file attached to the cube; Start is the one function used for now. |
| 1:30 | definition | Debug.Log with a message; the console shows it on play; a simple proof the code runs. |
| 2:05 | demo-sim | Play pressed; message appears; message removed so the console stays clean. |
| 2:30 | demo-sim | Deliberate typo: red underline, error at line 14, column 9; capital letter fixed; failure on screen. |
| 3:10 | definition | Variable defined as a named box: float speed equals 5; one place to change a value. |
| 3:50 | demo-sim | Debug.Log of speed shows 5; the quotation-mark mistake explained and made on purpose. |
| 4:30 | definition | Naming convention: lowercase start, camel case for longer names; kept consistent from the first line. |
| 4:55 | definition | Update defined: called once per frame; about 60 times a second on a typical machine. |
| 5:30 | brute-force | First movement written the obvious way: add speed to the x position every frame; it moves to the right and does not stop. |
| 6:05 | definition | Frame budget numbers: about 16.7 ms per frame at 60 fps, about 33 ms at 30 fps. |
| 6:40 | demo-sim | Same scene on a slower laptop: the cube moves visibly slower; the failure is frame-rate dependence. |
| 7:20 | definition | Fix: multiply by Time.deltaTime, the time since the last frame, so movement per second is constant. |
| 7:55 | demo-sim | Worked numbers: 0.0167 at 60 fps and about 0.033 at 30 fps; total 5 units per second either way. |
| 8:30 | caveat | deltaTime is measured, not set; the first frame and a dragged window can make big steps; no clamp here. |
| 8:55 | demo-sim | Input.GetAxis read: left gives minus one, right gives one, release gives zero; movement while held. |
| 9:30 | demo-sim | Sign bug found by hand: the cube moves right when left is pressed; one minus sign fixes it. |
| 10:00 | generalize | Same pattern for rotation per second and for vertical movement; only the axis name changes. |
| 10:30 | tangent | FixedUpdate mentioned as a fixed-rate function for physics, to be met when collisions arrive. |
| 11:00 | payoff | Speed set to 10, then 1, then 0; each value tests one prediction; the cube behaves as predicted. |
| 11:40 | coda | Closing summary sentence: the cube responds to keys at the same speed on any machine. |
| 12:10 | teaser | Next part: give the cube something to collide with and find out what counts as touching. |

## Narration
<<<NARRATION
Hi everyone, and welcome to the part where we actually write some code. Last time we set up the editor, and the cube sat there doing nothing, so this time we're going to make it do something, starting with a single line of text. We'll go slowly, because each line we write does one small thing, and we want to see each one work before we add the next.

Let's open the script, and in Unity we make a new C# file, attach it to the cube, and double-click it to open the code editor. The file already contains a class, which is a blueprint for a component, and a couple of functions that Unity calls for us. We don't need to understand all of that yet, so we'll only use the function called Start, which runs once when the game begins.

Inside Start, we write a single line, Debug.Log, with a message in quotation marks. When we press play, that message appears in the console window at the bottom of the screen. This is our first test, and it's a useful one, because a message in the console is the simplest proof that our code runs at all. If nothing appears, we know the problem is in the setup and not in the logic, which narrows things down a lot.

Let's test it, so I press play, and the console shows the message, so the script is attached to the right object and Unity is calling Start as we expected. That's a small win, but it's enough to build on. We'll remove the message now, because we don't want it cluttering the console for the rest of the lesson, and we can always add it back if something goes wrong.

Let's make a mistake on purpose, because a typo is the most common problem you will meet. If I write Debug.Log with the wrong capitalisation, the editor underlines the line in red, and the error message points at line 14, column 9. Reading that message is a skill in itself, and the important part is the line number, which tells us exactly where to look. I fix the capital letter, the red line disappears, and we're back where we were before the mistake.

Next, a variable. A variable is a named box that holds a value, and we declare one by writing its type, a name, and an equals sign with the value. For example, we write float speed equals 5. Now the word speed refers to the number 5, and we can change it in one place rather than hunting through the code for every copy of it, which is the whole reason we use variables.

Let's print the variable to check it. We write Debug.Log with speed inside the brackets, and the console shows 5. That's the same test as before, with a value instead of a message. Notice that we don't use quotation marks this time, because we want the value stored in speed and not the word speed itself. That's the first mistake most people make, and I made it myself on the first attempt, so it's worth watching for.

Names matter here as well. By convention, variable names in C# start with a lowercase letter, so we write speed rather than Speed, and longer names use camel case, like moveSpeed. The compiler doesn't care which style we pick, but we'll be reading these scripts for a long time, so we keep the style consistent from the very first line we write.

Now the cube needs to move, and for that we need Update, which is the last piece of the setup. Update is a function that Unity calls once every frame, so it's the place where anything that changes over time belongs. The game runs at around 60 frames per second on a typical machine, which means Update runs about 60 times every second while the game is playing. Inside Update, we want to add a little to the cube's position on each frame, and that is the loop that makes things move.

Here's the first version, written the obvious way. Inside Update, we write transform dot position plus equals a vector, with speed as the amount on the x axis. The cube starts moving to the right, and it doesn't stop. That works, and it's clearly moving, but it's moving at a speed that depends on how fast the computer runs the frames. That's the failure we need to look at closely before we accept it.

Let's put some numbers on the frame rate, because the numbers make the next part much easier to follow. At 60 frames per second, each frame lasts about 16.7 milliseconds, and at 30 frames per second each frame lasts about 33 milliseconds. Those are the budgets the engine has for drawing, physics and our own code, so every line we add takes a slice out of that budget.

Here's what happens. On my main machine the cube moves at one speed, and when I run the same scene on a slower laptop, it moves visibly slower. Nothing in the code changed, but the number of frames per second did. Each frame adds the same amount, so a machine that draws twice as many frames moves the cube twice as fast. That's a classic problem, and it's the reason real games never add a fixed amount per frame without thinking about it first.

The fix is to multiply by the time since the last frame. Unity gives us that as Time dot deltaTime, which is a small number, around one sixtieth of a second on a 60 frames per second machine. If we multiply speed by deltaTime, each frame adds a smaller amount when frames are quick and a larger amount when they're slow, so the total movement per second stays the same. I'll run the test again on the same two machines, and the cube now moves at the same speed on both.

Let's put numbers on it. At 60 frames per second, deltaTime is about 0.0167, and at 30 frames per second it's roughly 0.033. Multiply speed, which is 5, by either one and we get about 0.083 or 0.167 units per frame, but the total for one second is 5 units in both cases. You can check that yourself by printing deltaTime in the console, and the arithmetic makes the fix obvious.

I want to be careful about what deltaTime really is. It is the time between the last frame and this one, measured by the engine, and it isn't a constant we set ourselves. That means the very first frame can be odd, and a long pause, such as when the window is dragged, can produce a huge jump in one step. Real projects often clamp it to a maximum, and I'm not clamping it here, so that's something to watch for in a bigger game.

Let's look at the next problem. We want the cube to move in response to the keyboard, not on its own. Unity lets us read an input axis with Input dot GetAxis, and the horizontal axis returns a value between minus one and one. Pressing left gives minus one, pressing right gives one, and letting go returns zero. We multiply that value by speed and by deltaTime, and the cube moves only while a key is held down.

The first attempt at this had a bug I didn't expect. The cube moved right when I pressed left, because I had the sign backwards in the vector. The fix was a single minus sign, but it took me longer to find than it should have, which is a reminder that the code compiles either way. The mistake only shows up on screen, so every direction needs testing by hand, one key at a time.

Now let's generalise. The same pattern works for rotation, where we use Time dot deltaTime to turn the cube by a number of degrees per second instead of per frame. We can also move the cube up and down with the vertical axis, and the logic doesn't change at all, only the name of the axis. Once the pattern is clear for one direction, the other directions are just repetition with a different name.

The input axes also have a smoothing setting, which means the value ramps up over a short time rather than snapping from zero to one. The default ramp is quick, but it's there on purpose, so a key press feels smooth rather than abrupt, and you will notice the difference right away if you remove it. I'll leave the default alone for now and come back to it when we tune the feel of the movement, probably in a later part of the series.

Unity also has a second update function called FixedUpdate, which runs at a fixed rate for physics, usually 50 times a second by default. We'll meet it when collisions arrive, because physics needs a steady step. For now Update is the right tool, since nothing about the cube's movement depends on physics yet, and we can see that clearly in the code we have so far.

Before we finish, let me check something. I'll set speed to 10, then to 1, and then to 0, and watch the cube each time. At 10 it crosses the screen quickly, at 1 it creeps along, and at 0 it doesn't move at all, which is the result we want. Each value tests one prediction, and if the cube did something else, we would know the logic was wrong somewhere. That kind of check takes seconds, and it saves a lot of guessing later.

So that's where this part ends. The cube moves when we press the keys, it moves at the same speed on every machine, and every value lives in a variable we can change. We haven't touched the physics engine yet, and we haven't handled collisions, and those will come later in the series. For now the point is that a small script can respond to the player, and that's enough to build on for the next few parts.

Next time we'll give the cube something to collide with, and we'll see what happens when two objects meet in the scene. We'll have to think carefully about what counts as touching, and that turns out to be trickier than it looks at first. Thanks for watching, and I'll see you in the next episode.
NARRATION>>>

## Slots
```json
{
 "format_class": "designed-lesson series code lesson: toy world, minimal definitions, deliberate typo failure, deltaTime fix, teaser",
 "answer_given_upfront": false,
 "hook_type": "premise-claim",
 "first_question_frac": 0.03,
 "first_concrete_object_frac": 0.03,
 "first_new_idea_frac": 0.08,
 "first_notation_frac": 0.12,
 "payoff_frac": 0.88,
 "misconception": "none",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "print text -> variable -> keyed frame-correct movement",
 "roadmap": "none",
 "viewer_turn": "none",
 "viewer_turn_frac": null,
 "caveat_type": "approximation",
 "recurring_anchor": "the speed variable, reused in 5+ passes (print, move, scale by deltaTime, input, check)",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "beat_sequence": [
  "hook",
  "toy-world",
  "demo-sim",
  "definition",
  "demo-sim",
  "definition",
  "brute-force",
  "demo-sim",
  "definition",
  "caveat",
  "demo-sim",
  "generalize",
  "payoff",
  "teaser"
 ],
 "top5_moves": [
  "toy-world",
  "failure-shown",
  "brute-force-first",
  "visible-repetition",
  "minimal-definition-then-refine"
 ],
 "absent3_moves": [
  "analogy-breakpoint",
  "commit-to-answer",
  "hook-paradox"
 ],
 "wpm": 139,
 "median_beat_s": 35
}
```

```json
{"rule_trace": {
 "U1": "applied: series label; under-10 items n/a at 12:36 (over-10); roadmap and callback withheld; recap withheld; notation limited to code lines introduced after referents",
 "U2": "n/a: the title and first 40 s do not state an answer; the method comes after the first working test",
 "U3": "applied: teaser only (series label); no hook callback because no hook question is left open",
 "U4": "applied: the speed variable is reused in print, move, deltaTime, input and check passes, each adding one layer",
 "U5": "applied: code is introduced after a visible referent (the cube and the console); the one value is spoken as a number, not a symbol list",
 "U6": "applied: 139 wpm on 1,755 words over 12:36, beats of about 25-50 s with the code screen visible",
 "U7": "applied: no roadmap, no vote, no planted misconception; inline signposts only",
 "U8": "applied: approximation caveat on deltaTime being measured and the unclamped large step",
 "U9": "n/a: no binary decision or absurd magnitude to pause on",
 "U10": "n/a: not a history-of-invention or escalating-antagonist video",
 "U11": "n/a: title names a lesson topic (writing code), not an application or end state",
 "C1": "applied: designed-lesson series format (code-along), not impersonal lecture and not devlog",
 "C2": "applied: the same moving cube is rerun with one change per pass (print, move, deltaTime, input); the starting scene is unchanged",
 "C3": "n/a: not lecture format; no pause-the-video quiz",
 "C4": "n/a: no design source named; the Unity documentation is not cited in the narration",
 "C5": "n/a: series lesson, not a devlog opening",
 "D1": "applied: two failures on screen (the red typo error; the cube moving the wrong way), each found and fixed",
 "D2": "n/a: repairs are named by function (capital letter, deltaTime, minus sign), not after the failure",
 "D3": "applied: speed set to 10, 1 and 0 with one prediction each",
 "D4": "n/a: no honest-close bundle; the close is a one-line summary and a teaser",
 "D5": "n/a: no equation revealed after behaviour; the arithmetic is shown as numbers before the check",
 "N1": "n/a: under-10 band rule; this video is over-10 min",
 "N2": "applied: 139 words per minute (measured), inside p25-p75 137-158",
 "N3": "applied: 0.34 you/your per 100 words (measured), inside p25-p75 0.23-0.78",
 "N4": "applied: 0.97 I/me/my per 100 words (measured), inside p25-p75 0.94-2.81",
 "N5": "applied: 4.16 we/us/let's per 100 words (measured), inside p25-p75 2.55-5.7",
 "N6": "applied: 1.54 numbers per 100 words (measured), inside p25-p75 0.95-2.12",
 "N7": "applied: 0.00 question marks per 100 words (measured), inside p25-p75 0.0-0.09",
 "N8": "applied: 19.7 words per sentence (measured), inside p25-p75 19-25",
 "N9": "applied: 0.11 hedges per 100 words (measured), inside p25-p75 0.11-0.35",
 "N10": "applied: 0.06 example cues per 100 words (measured), inside p25-p75 0.03-0.18",
 "B1": "applied: no sponsor read",
 "B2": "applied: one-line teaser, because the video is in a series",
 "B3": "n/a: roadmap withheld; a code lesson does not call for one",
 "B4": "applied: no spoken recap in the last 20%; the late passage is a physics aside, not a summary"
}}
```
