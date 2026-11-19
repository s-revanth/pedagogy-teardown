channel: SebastianLague
id: XT_CtYN1OOU
title: Introduction to Game Development (E02: classes)
duration: 510s (8:30)
condition: v3
recall: vague
exemplars read: deep/corpus/compact/jitkNxnn-s8.txt, deep/corpus/compact/m7VY1T6f8Ak.txt

## Content skeleton
- Open on the gap: the last script spun one cube, but it only ever had one object in mind.
- Introduce the class as a blueprint, with instances built from it.
- Declare fields for health and name, and show that each instance gets its own copy.
- Write a TakeDamage method that changes health and destroys the object at zero.
- Explain MonoBehaviour as the base class that connects the script to the engine.
- Drag the script onto three cubes with different starting health and test damage.
- Show the static mistake, then close on the blueprint idea and tease the next episode.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Last script spun one cube; the goal is to describe a whole kind of thing |
| 0:40 | definition | A class is a blueprint, and each object made from it is an instance |
| 1:30 | derivation | Fields hold per-object data: health and name |
| 2:20 | derivation | A method is a function that belongs to the class: TakeDamage |
| 3:20 | definition | MonoBehaviour is the base class that connects the script to the engine |
| 4:10 | demo-sim | Three cubes with different starting health from the same script |
| 5:20 | demo-sim | Calling TakeDamage on one cube and watching the others stay put |
| 6:30 | failure-shown | Marking a field static, so every instance shares one number |
| 7:30 | payoff | Blueprint and instances: shared behaviour, separate data |
| 8:00 | teaser | In the next episode, objects start talking to each other |

## Narration
<<<NARRATION
Last time we wrote a script that spins a cube, and it worked, but it only ever had one object in mind. I wanted a way to describe a whole kind of thing, like an enemy with health and a name, and then reuse that description for every enemy in a scene. That description is called a class. So this is where the first class gets written, and the objects that come from it appear in the game. If you already know what a class is, the examples are still worth a quick look.

Think of a class as a blueprint. The blueprint says what an enemy has and what it can do, but it isn't an enemy by itself. We can build several enemies from the same blueprint, and each one can have its own health and its own position. A blueprint is written once, and we create as many instances from it as we need. We might write a second blueprint for a different kind of enemy, such as a slow one with more health. Both blueprints can live in the same project without any trouble. We keep them in separate scripts, because a clean file is easier to navigate. We also find that the names of the classes matter more than we expect, so we choose them carefully from the start. Each object made from the class is called an instance, and that word comes up constantly from here on.

Inside the class, we declare fields. A field is a variable that belongs to the object, so each enemy keeps its own copy. We add an int called health, and we set it to 100 by default. We add a string called name as well. I like to name fields clearly, because the name is what I read first when I come back to the code. If you change the health on one enemy, the others don't change. That separation is the entire point, and we rely on it everywhere in Unity. We can test this separation quickly, and the test takes only a few seconds. We change one value, look at the others, and confirm they stayed put. Each time we run that check, we gain more confidence in the design. I should have spelled this out earlier, because it's the idea everything else depends on.

Fields hold data, and methods hold behaviour. A method is a function that belongs to the class. We write a method called TakeDamage, which takes an int amount and subtracts it from health. Inside that method, we check whether health has dropped to 0 or below, and if it has, we call Destroy on the game object. You can read that method from top to bottom, and it tells the whole story of what happens when an enemy is hit. I like that kind of readability.

In Unity, our class inherits from MonoBehaviour, which is the base class that connects a script to the engine. That's why Start and Update exist in the first place. I think of it as a contract with the engine. The engine calls Update on every instance of our class each frame, and we don't need to call it ourselves. We only write the parts we care about, and the base class supplies everything else. For example, the lifecycle methods are already wired up for us. We can see them in the editor as soon as the script is attached. We don't need to register anything manually, and we don't need a separate setup step. The engine already knows about our class, and it calls the right method at the right time. It's a convenient arrangement, and it's one reason Unity scripts feel so direct.

Now we can create the enemies. In the editor, we drag the script onto three cubes. Each cube gets its own copy of the fields, so one starts with 100 health, another with 50, and a third with 250. I set the second one myself, just to make the difference obvious. We could also give the third cube a name, which makes the console messages easier to follow. We check each name in the inspector before we press play. If a name is wrong, we fix it there, and the change appears straight away. We find that small habits like this save time over a whole project. We could change those values in the inspector, and each cube responds on its own. If you press play, the three cubes behave independently, even though they all share the same blueprint.

The method is ready to test. We call TakeDamage on the first cube and pass 30. Its health drops again, while the other two stay where they were. We call it again with 80, and the first cube goes below 0. The Destroy call then removes it from the scene. I like this part, because the result is so easy to read. We can watch the console as we do this, and each step gives a clear answer. We can also watch the health value in the inspector while the calls run, which gives a second view of the same numbers. Two views are better than one, because a mismatch between them points straight at the bug. We keep both windows visible for that reason. You can add a Debug.Log inside the method to make every change visible.

There's a common mistake that I see all the time. People mark a field as static, which means it belongs to the class itself, not to each object. If we make health static, all three cubes share one number, and damaging one damages all of them. I usually catch this within a minute, but it still surprises beginners. We can fix it by removing the keyword, and then each instance gets its own copy again. We probably want to double check the other fields as well, just in case the same mistake appears more than once. We look for the keyword in each class, and we confirm that each instance is separate. That quick review takes a minute, and it catches most surprises before they become bugs. It's probably the single most frequent class mistake I've seen.

So the class is the blueprint, and each object is an instance with its own data. We write the class once, and Unity creates as many instances as the scene needs. The methods are shared by all instances, but the fields are not. I find that split useful, because it tells me at a glance what is shared and what is separate. We keep coming back to that distinction, and most of the object-oriented code in Unity follows it. We use the same split for enemies, pickups and doors, because the pattern holds up in every case we have tried.

In the next episode, objects start talking to each other, which is where classes begin to feel genuinely powerful. The examples stay small, and you can follow along with three cubes on screen. I'm curious how far a simple blueprint can take us once the objects can respond to one another. Thanks for watching, and see you there.
NARRATION>>>

## Slots
```json
{
 "format_class": "tutorial series episode, code-first walkthrough with live editor",
 "answer_given_upfront": false,
 "hook_type": "story-anecdote",
 "first_question_frac": 0.5,
 "first_concrete_object_frac": 0.03,
 "first_new_idea_frac": 0.1,
 "first_notation_frac": 0.3,
 "payoff_frac": 0.88,
 "misconception": "mid-video-correction",
 "brute_force_first": false,
 "examples_count": 2,
 "example_growth": "one cube, then three cubes, then a static mistake",
 "roadmap": "none",
 "viewer_turn": "none",
 "viewer_turn_frac": null,
 "caveat_type": "none",
 "recurring_anchor": "the three cubes with different health",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 159,
 "median_beat_s": 40,
 "beat_sequence": ["hook", "definition", "derivation", "derivation", "definition", "demo-sim", "demo-sim", "failure-shown", "payoff", "teaser"],
 "top5_moves": ["toy-world", "visible-repetition", "failure-shown", "minimal-definition-then-refine", "rule-list"],
 "absent3_moves": ["brute-force-first", "hook-question", "expert-dialogue"]
}
```

```json
{"verified_trace": {"wpm": "PASS 159.00 (target 152.0-165.69, median 159.44)", "you_rate": "PASS 0.59 (target 0.45-0.85, median 0.64)", "i_rate": "PASS 1.26 (target 0.6-1.47, median 0.96)", "we_rate": "PASS 4.61 (target 3.81-5.27, median 4.85)", "num_rate": "PASS 2.18 (target 1.32-2.36, median 2.04)", "hedge_rate": "PASS 0.25 (target 0.15-0.36, median 0.32)", "example_rate": "PASS 0.25 (target 0.08-0.37, median 0.17)", "q_rate": "PASS 0.00 (target 0.0-0.0, median 0.0)", "sent_len": "FAIL 14.56 (target 19.31-20.56, median 20.56)", "switch_sponsor": "PASS detected=False default=OFF", "switch_teaser": "PASS detected=True default=ON", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (story-anecdote vs story-anecdote)", "ending_type": "MATCHES default (teaser-next vs teaser-next)", "summary": "8/9 numeric targets pass"}}
```
