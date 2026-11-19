# Header
- channel: SebastianLague
- id: L9zlZjxmwXU
- title: Introduction to Game Development (E03: Unity overview)
- duration: 299 s (4:59)
- condition: v1
- recall: vague

## Content skeleton
- Tour of the Unity editor: scene view, hierarchy, inspector, project window, play mode.
- Toy world: an empty scene with a camera and a light.
- Minimal definitions: a GameObject is a thing in the scene; a component is a thing it has.
- Adding and moving a cube, reading values in the inspector.
- Pressing Play: the cube does nothing because it has no physics component.
- Staged misconception: the cube should fall on its own, and it does not.
- Adding a physics component and replaying the same test shows the cube falling.
- Caveat that the layout may differ in another Unity version; teaser for the code episode.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | By the end of this episode a ball falls under gravity; answer stated |
| 0:20 | roadmap | Editor tour, then one object, then one behaviour |
| 0:40 | toy-world | Empty scene with a camera and a light |
| 1:10 | definition | GameObject as a thing in the scene; component as a thing it has |
| 1:50 | demo-sim | Add a cube; move, rotate, scale; read inspector values |
| 2:30 | wall | Press Play; the cube sits still; nothing has told it to fall |
| 3:00 | misconception-defuse | Assumed the cube would fall by itself; it has no physics component |
| 3:30 | demo-sim | Add a rigidbody component; press Play; it falls; same test |
| 4:10 | caveat | Layout may differ in your version of the editor |
| 4:35 | teaser | Next episode: writing code for the cube |
| 4:50 | coda | Sign-off |

<<<NARRATION
By the end of this episode, we will have a ball falling under gravity inside Unity. That is the destination. Let's go and get the tools first.

Here is the plan. We look at the editor, we make one object, and then we give that object one behaviour. Nothing more than that for now.

We start with the toy world. This is an empty scene. It has a camera, which is the viewpoint you see the game from, and a light, so that things are visible. There is nothing else. It is a clean stage, and I want you to see that empty stage before anything goes into it.

Now the vocabulary, kept as small as possible. A GameObject is a thing that exists in the scene. That is the whole definition. A component is a thing that a GameObject has, a piece of behaviour or data attached to it. A GameObject with no components does nothing. Every later step is about adding components to objects.

Let's add a cube. I use the hierarchy window to create it, and it appears in the scene view. Then I move it, rotate it, and scale it. The inspector on the right shows the numbers: position, rotation and scale. When I change a number there, the cube changes in the scene. That is the most direct link between a value and what you see, so it is worth looking at slowly.

Now I press Play. The cube just sits there. Why? Nothing is wrong with the editor, and nothing has crashed. The cube has no behaviour that makes it fall, so it stays exactly where it was. This is the moment where you might expect gravity to act on it, and it does not. That is the failure I wanted to show.

Here is what I had wrong at first. I assumed the cube would fall on its own, because it is a cube sitting above an empty space, and that is what happens in the real world. In Unity it does not. The cube has no physics component, so the engine does not treat it as a solid object that gravity acts on. So the fix is not in the scene. The fix is to add the right component.

I add a rigidbody component to the cube, from the inspector. A rigidbody tells the physics system that this object should be simulated. Now I press Play again. The cube falls, hits the floor, and comes to rest. It is the same test as before, with one component added. That is the point of the comparison. Only one thing changed between the two runs, so the difference is the component.

It is worth noticing that I did not write any code. Everything so far has been done by clicking and typing numbers in the inspector. That is useful, because it means you can see what a component does before you need to write anything to control it.

Now the honest part. The editor layout I am showing is from the version I am using. Menus, panel positions and some defaults move around between versions of Unity. If your screen looks different, do not worry about matching the pixels. Look for the same things: the hierarchy, the inspector, the scene view, and the play button. Those are stable, even when the rest is not.

It is also worth saving the scene as you go. Unity keeps the scene file separate from the play session, so anything you change while the game is running is lost when you stop, unless you copy it back into the editor. I have lost a good half hour to that more than once. Press Play to test, press Stop, and check the inspector values again before you assume they stuck. The editor is a workshop, and the saved scene is the thing you actually keep.

So let's recap. A GameObject is a thing in the scene. A component is something it has. Adding a rigidbody gives a cube physical behaviour, so it falls when you press Play. Same test, one change, one difference.

Next time, we write code, and make the cube do something the editor cannot do by itself. We will need to know which GameObject the code is attached to, and that is the link between the two ideas we just used. So keep the hierarchy open.

Thanks for watching.
NARRATION>>>

## Slots

```json
{
 "format_class": "tool tour, empty scene to one behaviour",
 "answer_given_upfront": true,
 "hook_type": "answer-stated",
 "first_question_frac": 0.5,
 "first_concrete_object_frac": 0.03,
 "first_new_idea_frac": 0.23,
 "first_notation_frac": null,
 "payoff_frac": 0.7,
 "misconception": "staged-early",
 "brute_force_first": false,
 "examples_count": 2,
 "example_growth": "static cube -> moved cube -> falling cube",
 "roadmap": "one-line",
 "viewer_turn": "none",
 "viewer_turn_frac": null,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the cube object, named in every step",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 33,
 "beat_sequence": ["hook","roadmap","toy-world","definition","demo-sim","wall","misconception-defuse","demo-sim","caveat","teaser","coda"],
 "top5_moves": ["toy-world","failure-shown","visible-repetition","act-it-out","honest-caveat"],
 "absent3_moves": ["brute-force-first","expert-dialogue","commit-to-answer"]
}
```
