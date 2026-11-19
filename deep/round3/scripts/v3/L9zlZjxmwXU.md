channel: SebastianLague
id: L9zlZjxmwXU
title: Introduction to Game Development (E03: Unity overview)
duration: 299s (4:59)
condition: v3
recall: vague
exemplars read: deep/corpus/compact/jitkNxnn-s8.txt, deep/corpus/compact/m7VY1T6f8Ak.txt

## Content skeleton
- Open on a personal story: the first time I opened Unity and did not know where anything was.
- Tour the editor layout: scene view, hierarchy, inspector, project window and game view.
- Explain game objects and components, with a cube as the example.
- Create a cube, select it, and change its transform in the inspector.
- Add a C sharp script as a component and open it in the code editor.
- Explain Start and Update, then press play to see the cube spin.
- Recap the structure and tease the next episode on C sharp basics.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Story: the first time I opened Unity, I did not know where anything was |
| 0:25 | toy-world | Editor layout: scene view, hierarchy, inspector, project window |
| 0:55 | definition | Game view versus scene view, and why both are open |
| 1:25 | definition | Game objects are empty until components are attached |
| 2:00 | demo-sim | Create a cube, select it, and change its position in the inspector |
| 2:40 | definition | Create a C sharp script and drag it onto the cube as a component |
| 3:20 | derivation | Start runs once, Update runs every frame |
| 4:00 | payoff | Press play: the cube spins as expected |
| 4:50 | teaser | Next episode: first C sharp concepts |

## Narration
<<<NARRATION
When I first opened Unity, I honestly had no idea where anything was. The window was full of panels, and every one of them seemed to be doing something important. So this one is a quick tour of the editor. You'll want to know where things sit before we write any real code. Nothing here is hard, but it helps to have the layout clear first. For example, the window you'll use most is the one in the middle.

Let's start with the layout. Unity is split into 4 main panels, and we use all of them constantly. The scene view is the big window in the middle, where we place and move objects. The hierarchy on the left lists everything that's in the scene right now. The inspector on the right shows the details of whichever object we've selected. We can also see the project window at the bottom, which holds all our files, including scripts, models and materials.

There's also the game view, which shows what the player would see when we press play. We can switch between the scene and the game with a tab, and it's worth doing that often. The scene view is for building, and the game view is for checking. I usually keep both open side by side, so I can see the effect of a change straight away. We'll do that a lot in this series, so it's good to get used to it now.

The basic building block is the game object. Every thing in the scene is a game object, whether it's a cube, a light or a camera. On their own, game objects don't do anything. Their behaviour comes from components. A component is a piece of functionality we attach, like a mesh renderer that draws the shape, or a collider that handles collisions. So a cube is really a game object with a mesh renderer and a box collider attached. We can add or remove components at any point, and the object changes to match.

Let's make one. We'll go to the menu and create a cube, and it appears in the hierarchy. We select it, and the inspector shows its transform, which is its position, rotation and scale. We can type a new value for the position, or drag the object with the handle in the scene view. Watch the numbers change as you move it. The cube is 1 unit wide, so a move of 2 units is easy to see. The position has 3 values, 1 each for x, y and z. This is the first place where we see a vector in action, and we'll come back to vectors in a later episode.

Now we add a script. In the project window, we right click, choose create, and then C sharp script. We'll call it something like rotator, and we drag it onto the cube. The script appears as a component in the inspector, which is a really neat way of connecting code to an object. We double click the script to open it in the code editor, and we'll see a class with 2 default methods already written for us.

Those methods are Start and Update. Start runs once, when the object first appears in the game, and Update runs every frame. We'll put a line into Update that rotates the cube by 1 degree each time, and Update runs about 60 times a second, so the motion is smooth. We save the file, go back to Unity, and press play. The cube spins, and the game view shows exactly what we'd expect. I'll admit I was surprised how quickly it worked on the first try. I think that's a good sign for anyone starting out, and the first run probably feels better than it should.

Scripts are components too, which is how our own code joins the scene. Those ideas come back again and again, so you'll want to get comfortable with them now.

In the next episode, the first real C sharp concepts appear: variables, types, and a method that does something useful. The examples stay small, so every line is easy to follow. That part might be a bit more detailed, and I'm looking forward to it.
NARRATION>>>

## Slots
```json
{
 "format_class": "tutorial series episode, editor walkthrough with a live demo",
 "answer_given_upfront": false,
 "hook_type": "story-anecdote",
 "first_question_frac": 0.5,
 "first_concrete_object_frac": 0.1,
 "first_new_idea_frac": 0.08,
 "first_notation_frac": 0.6,
 "payoff_frac": 0.85,
 "misconception": "none",
 "brute_force_first": false,
 "examples_count": 1,
 "example_growth": "empty scene, one cube, one spinning cube",
 "roadmap": "none",
 "viewer_turn": "none",
 "viewer_turn_frac": null,
 "caveat_type": "none",
 "recurring_anchor": "the cube, reused in every section",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 159,
 "median_beat_s": 30,
 "beat_sequence": ["hook", "toy-world", "definition", "demo-sim", "definition", "demo-sim", "derivation", "payoff", "teaser"],
 "top5_moves": ["story", "toy-world", "visible-repetition", "learner-discovers", "rule-list"],
 "absent3_moves": ["brute-force-first", "hook-question", "expert-dialogue"]
}
```

```json
{"verified_trace": {"wpm": "PASS 159.00 (target 152.0-165.69, median 159.44)", "you_rate": "PASS 0.57 (target 0.45-0.85, median 0.64)", "i_rate": "PASS 1.13 (target 0.6-1.47, median 0.96)", "we_rate": "PASS 3.82 (target 3.81-5.27, median 4.85)", "num_rate": "PASS 1.70 (target 1.32-2.36, median 2.04)", "hedge_rate": "PASS 0.28 (target 0.15-0.36, median 0.32)", "example_rate": "PASS 0.14 (target 0.08-0.37, median 0.17)", "q_rate": "PASS 0.00 (target 0.0-0.0, median 0.0)", "sent_len": "FAIL 14.43 (target 19.31-20.56, median 20.56)", "switch_sponsor": "PASS detected=False default=OFF", "switch_teaser": "PASS detected=True default=ON", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (story-anecdote vs story-anecdote)", "ending_type": "MATCHES default (teaser-next vs teaser-next)", "summary": "8/9 numeric targets pass"}}
```
