# SebastianLague | L9zlZjxmwXU | Introduction to Game Development (E03: Unity overview)

- channel: SebastianLague
- id: L9zlZjxmwXU
- title: Introduction to Game Development (E03: Unity overview)
- duration: 299 s (4:59)
- condition: v2
- recall: vague (I recognise that a Unity beginner series exists, not this episode's content)
- class (step 0): under-10 min; format = designed-lesson series lesson (E03 label); answer not stated; topic = game engine basics (editor, objects, camera)
- exemplars read: deep/compact/r_It_X7v-1E.txt (Coding Adventure: Ecosystem, 6:40) read in full for under-10 rhythm; deep/compact/-L-WgKMFuhE.txt (A* Pathfinding E01, 11:38) read in full for series voice

## Content skeleton
- Premise: this episode is about the editor only; no code yet.
- An empty scene with one camera; the camera's view decides what appears on screen.
- One cube added; minimal definition: a game object is anything in the scene.
- Hierarchy, inspector, and the position, rotation and scale triplets.
- Move, rotate and scale the cube, typing exact values so they can be repeated.
- Failure on screen: the scene view looks fine, the game view is empty because the camera points at nothing; fixed by copying the view.
- Pressing play shows nothing yet; a three-item closing list of what to remember.
- Teaser: next episode starts the code that makes the cube move.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Premise: this episode is about the Unity editor, not code; the window and its panels. |
| 0:25 | toy-world | Empty scene with only a camera; the camera is the viewpoint and sets what can be seen. |
| 0:50 | definition | Cube added; minimal definition of a game object as anything that exists in the scene. |
| 1:20 | definition | Hierarchy and inspector introduced; position, rotation and scale as three numbers each. |
| 1:50 | demo-sim | Cube dragged along x, then a typed value jumps it to an exact spot. |
| 2:15 | demo-sim | Rotation by 45 degrees on y and reset; scale doubled on one axis from 1 to 2; reset habit. |
| 2:35 | demo-sim | Camera moved back and up; the scene view looks fine but the game view is empty (failure on screen). |
| 3:05 | demo-sim | Fix: copy the scene view onto the camera; the game view now shows the cube. |
| 3:35 | demo-sim | Pressing play: the cube does nothing yet; edits made in play mode are reset on stop. |
| 4:05 | coda | Three things to remember: hierarchy, inspector, camera. |
| 4:40 | teaser | Next episode starts writing code to make the cube move. |

## Narration
<<<NARRATION
Let's start with the editor, because everything else in this series happens inside it. This episode is about Unity itself, what the window contains, and what each panel is for. We won't write any code yet, and that's deliberate, because we'll spend most of our time in this window, so it's worth knowing where things are.

When Unity opens a new project, we get a scene. A scene is the space where our game lives, and right now it's empty except for a camera. The camera is the viewpoint we see the game from, so anything the camera doesn't point at simply won't show up in the picture. Keep that in mind, because we're about to hit exactly that problem in a few minutes.

Let's add a cube, and from the menu we choose a 3D object, then a cube, so it appears in the middle of the scene. This cube is a game object, and the minimal definition is this: a game object is anything that exists in the scene. For example, a cube, a light, a camera and an empty container are all game objects, and they all appear in the same list.

That list is called the hierarchy, and it sits on the left, showing every object in the scene. Clicking an object in the hierarchy selects it, and the inspector on the right shows everything about that object. We see its position, its rotation and its scale, and each of those is a set of three numbers, one for each axis. Position is where it sits, rotation is how it's turned, and scale is how big it is. The default cube is 1 unit on each side, so a scale of 1 means one unit in every direction, and we'll use that number as our reference for the rest of the series.

Let's move the cube, and i'll drag it along the x axis, and the position value changes as we go. Then I'll type a value straight into the box, and the cube jumps to exactly that spot. Dragging is fine for a rough placement, but typing gives us a number we can repeat, and that matters later, when we write code that needs the same spot every time.

Rotation works the same way, and i'll turn the cube 45 degrees around the y axis, and then reset it to zero, which takes about 2 seconds with the keyboard shortcut. Scale works the same way too, and I'll double it along one axis, from 1 to 2, so it becomes a long bar. You can see the change immediately in both the scene view and the inspector. A useful habit is to reset a value once we've finished, so the original state is always one click away.

Now the camera. It's still pointing at the origin, which is the point at 0, 0, 0 in the middle of the scene, but the cube is now off to one side, so I'll move the camera back and up until the cube sits in the middle of the view. Let's check that in the game view, which shows what the player would actually see. The scene view looks fine, but the game view is empty, because the camera points at nothing. That's the failure we wanted to see, and it's a small one, probably the smallest failure we'll see all series.

The fix is to rotate the camera so it looks at the cube. We can set the camera's rotation directly in the inspector, or we can move the scene view until it matches the angle we want and then copy that view onto the camera. I'll use the second method this time, because it's quicker to see what we're doing. Now the game view shows the cube, and the problem is gone.

Pressing play starts the game, and the cube does nothing yet, which is what we should expect at this stage, because we haven't told it to do anything. That's exactly where we are. The editor gives us the objects and the views, and the next episode gives the cube its first behaviour through a script. Anything we change while playing is reset when we stop, so we'll keep our edits outside of play mode for now.

I'll stop there. The three things to remember from this part are the hierarchy, the inspector, and the camera, and we'll come back to each of them as we need them. Every object we make will live in the hierarchy, its values will live in the inspector, and what we see on screen depends entirely on where the camera points. Next time we'll start writing code, and we'll make that cube move.

Thanks for watching, and I'll see you in the next one.
NARRATION>>>

## Slots
```json
{
 "format_class": "designed-lesson series lesson: toy world, minimal definition, one failure on screen, teaser",
 "answer_given_upfront": false,
 "hook_type": "premise-claim",
 "first_question_frac": 0.05,
 "first_concrete_object_frac": 0.08,
 "first_new_idea_frac": 0.17,
 "first_notation_frac": null,
 "payoff_frac": 0.87,
 "misconception": "none",
 "brute_force_first": false,
 "examples_count": 2,
 "example_growth": "empty scene -> one cube -> camera view fix",
 "roadmap": "none",
 "viewer_turn": "none",
 "viewer_turn_frac": null,
 "caveat_type": "none",
 "recurring_anchor": "the cube, moved, rotated, scaled and shown in the game view",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "beat_sequence": [
  "hook",
  "toy-world",
  "definition",
  "demo-sim",
  "demo-sim",
  "payoff",
  "coda",
  "teaser"
 ],
 "top5_moves": [
  "toy-world",
  "minimal-definition-then-refine",
  "failure-shown",
  "visible-repetition",
  "special-case-first"
 ],
 "absent3_moves": [
  "hook-paradox",
  "commit-to-answer",
  "expert-dialogue"
 ],
 "wpm": 160,
 "median_beat_s": 30
}
```

```json
{"rule_trace": {
 "U1": "applied: under-10 band and series label; roadmap, recap and callback dropped; no symbols; the fixed 20-25 s beat grid is dropped and beats follow the lesson template",
 "U2": "n/a: the title and first 40 s do not state an answer or thesis",
 "U3": "applied: teaser only (series label); no hook callback because there is no hook question",
 "U4": "applied: the cube is the recurring object, moved, rotated, scaled and shown in the game view (4+ uses)",
 "U5": "n/a: no symbols or formulas; axis names x, y and z are interface labels",
 "U6": "applied: 162 wpm on 809 words over 4:59, beats of about 25-40 s",
 "U7": "applied: no roadmap, no vote, no planted misconception",
 "U8": "n/a: no open or approximate claim needing a caveat",
 "U9": "n/a: no binary decision or absurd magnitude to pause on",
 "U10": "n/a: not a history-of-invention or escalating-antagonist video",
 "U11": "n/a: title names a lesson topic (Unity overview), not an application or end state",
 "C1": "applied: designed-lesson series format (beginner series), not impersonal lecture and not devlog",
 "C2": "applied: the same cube is reshown after each edit (move, rotate, scale, camera), one change per pass",
 "C3": "n/a: not lecture format; no pause-the-video quiz",
 "C4": "n/a: no design source needed; the editor interface is shown directly",
 "C5": "n/a: series lesson, not a devlog opening",
 "D1": "applied: failure on screen (empty game view because the camera points at nothing), then fixed",
 "D2": "n/a: the repair is named by its function (point the camera), not after the failure",
 "D3": "applied: one property changed per pass (position, then rotation, then scale) to isolate its effect",
 "D4": "n/a: no honest-close bundle; the ending is a three-item list and a teaser",
 "D5": "n/a: no equation",
 "N1": "applied: 160 words per minute (measured), inside p25-p75 141-180",
 "N2": "n/a: over-10 band rule; this video is under-10 min",
 "N3": "applied: 0.25 you/your per 100 words (measured), inside p25-p75 0.23-0.78",
 "N4": "applied: 1.01 I/me/my per 100 words (measured), inside p25-p75 0.94-2.81",
 "N5": "applied: 5.03 we/us/let's per 100 words (measured), inside p25-p75 2.55-5.7",
 "N6": "applied: 1.26 numbers per 100 words (measured), inside p25-p75 0.95-2.12",
 "N7": "applied: 0.00 question marks per 100 words (measured), inside p25-p75 0.0-0.09",
 "N8": "applied: 19.9 words per sentence (measured), inside p25-p75 19-25",
 "N9": "applied: 0.13 hedges per 100 words (measured), inside p25-p75 0.11-0.35",
 "N10": "applied: 0.13 example cues per 100 words (measured), inside p25-p75 0.03-0.18",
 "B1": "applied: no sponsor read",
 "B2": "applied: one-line teaser, because the video is in a series",
 "B3": "n/a: roadmap withheld; a short lesson does not call for one",
 "B4": "applied: no spoken recap; the three-item close names the objects, it does not recap the lesson"
}}
```
