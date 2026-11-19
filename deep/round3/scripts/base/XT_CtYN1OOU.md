# SebastianLague / XT_CtYN1OOU

- Channel: SebastianLague
- ID: XT_CtYN1OOU
- Title: Introduction to Game Development (E02: classes)
- Duration: 510 s (8:30)
- Condition: base
- recall: vague

## Content skeleton

- Question: why does every object in a game seem to have its own rules, and how does code express that?
- A class is a blueprint; a cookie cutter is the everyday picture of one blueprint making many objects.
- Terms defined: class, object (instance), fields for data, methods for behaviour.
- A simple class for an enemy is written in code, with its own health and movement.
- Brute force: copy-pasting the same class for each enemy works at first.
- Wall: changing a rule means editing every copy, which is where the approach breaks.
- Misconception: a class is a template, not an object sitting in the scene.
- Public versus private fields; public fields appear in the inspector. Closes by generalising to other software.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Question: why does each object in a game feel like it has its own rules? |
| 0:30 | roadmap | Blueprints first, then the enemy example, then public and private. |
| 0:55 | analogy | A cookie cutter: one shape, many cookies, each one a separate object. |
| 1:40 | definition | Class, object, field and method defined in one line each. |
| 2:25 | toy-world | A small scene with a few plain objects, each one a placeholder for an enemy. |
| 3:10 | demo-sim | Enemy class written in code; instances created and each given its own health. |
| 4:00 | brute-force | Copy the enemy code for each new enemy; it works for a few. |
| 4:45 | wall | Change the speed rule and every copy needs editing; the approach collapses. |
| 5:30 | misconception-defuse | A class is a template, not an object in the scene; the scene only holds instances. |
| 6:00 | demo-sim | Public fields appear in the inspector; private fields do not; different values per object. |
| 7:10 | generalize | Same idea in other programs: one definition, many instances. |
| 7:50 | recap | Blueprint, instance, fields, methods, and why one definition is enough. |

## Narration

<<<NARRATION
Here is a question that is worth asking early. Why does every object in a game seem to have its own rules? A coin spins, an enemy chases you, a door opens when you approach it, and each of those things behaves differently, even though they are all just objects on the screen. How does the code keep track of that? The answer is an idea called a class, and it is one of the most useful ideas you will meet in this series.

The plan for today is simple. We start with the blueprint idea, then write a small enemy in code, then look at what goes wrong when we copy it by hand, and then fix that. There are a few new words along the way, and I'll define each one as it comes up.

Let's start with an everyday picture. Imagine a cookie cutter. It has one shape, and you press it into dough again and again. Each cookie comes out the same shape, but each one is a separate cookie. You can put different icing on each one, and one can burn while another does not. The cutter is the class. Each cookie is an object. The cutter describes what a cookie should look like, and the cookies are the things you actually have on the table.

Now let's make that concrete. A class is a definition, a description of the kind of thing we want. An object is a single instance of that definition, made from it. The word instance is just the technical name for one of those cookies. You can make as many instances as you like from one class, and each one has its own separate copy of its data. That separation is the important part, so keep it in mind.

Two more words. A field is a piece of data that belongs to an object, like its health or its speed. A method is a piece of behaviour, a thing the object can do, like move or take damage. So a class puts fields and methods together into one definition. The enemy has a health field, a speed field, and a method for taking damage. Everything about the enemy is written in one place.

Let's write one. Here is a class for an enemy. It has a field for health, which I set to a starting value, and a field for speed. It has a method called take damage, which reduces health and checks whether the enemy is dead. And it has a method that moves the enemy toward the player each frame. I'm writing this in a plain file for now, and I will explain the Unity parts as we go.

Now I'll create some enemies from it. I make one, and it has its own health. I make a second one, and it also has its own health, separate from the first. When I damage the first enemy, the second one does not change at all. That is the cookie cutter at work. They share a shape, but each instance keeps its own numbers. The class is the shared definition, and the objects are where the state lives.

So far, so good. But now let's try the obvious approach for a second. Suppose I want a different kind of enemy, one that is faster and has less health. The brute force move is to copy the whole enemy code, paste it into a new file, and change the numbers. Then copy it again for the next kind. I did exactly this when I first started, and it works. For three or four enemies it is perfectly reasonable, and I would not blame anyone for doing it.

The trouble shows up later. Imagine you decide the movement logic needs to change. Maybe enemies should slow down near walls, or they should follow a path. Now you have to find that movement code in every copy and change it in every copy, and it is very easy to miss one. Two enemies behave correctly and one does not, and you spend twenty minutes wondering why. That is the wall. Copying is fine until you have to change the rule, and then the copies start fighting you.

This is the reason the class exists. You write the rule once, in one place, and every instance follows it. If you change the movement method in the class, every enemy changes with it. The copies stop being copies and become instances of the same definition. That is a huge difference, and it is what makes a game with a hundred enemies manageable instead of a nightmare.

There is a misconception I want to clear up, because it confused me at first. People often think the class is an object sitting in the scene, like a cube or a light. It is not. The class is only a template. It does not appear in the scene until you create an instance of it, and the scene holds the instances. If you delete all the instances, the class is still there in your code, ready to make more. The class is the recipe, and the scene holds the dishes.

Let's look at the fields a bit more carefully. Some fields are public, which means other code can read and change them. Some are private, which means only the class itself can touch them. Public fields have a useful side effect in Unity. They show up in the inspector, so you can tune the speed of each enemy by typing a number in, without touching the code. That is very handy for a designer who wants to try different values.

I'll show you that. The enemy has a public speed field. I select the first enemy, and the inspector shows its speed. I change it to a higher number, and that one moves faster. Then I select the second enemy and it still has the old speed, because the change only applied to the first instance. Each object carries its own values, and the inspector lets you edit them one at a time.

Private fields are for things nobody outside the class should be able to change directly. Health is a good example. If any script could set health to any number, it would be easy to break the rules. So health is private, and the only way to change it is through the take damage method, which checks the value before it changes anything. That is a small example of encapsulation, the idea that a class protects its own data.

This is also where the blueprint idea starts paying off in a deeper way. The class is responsible for its own rules. The speed rule, the damage rule and the death rule all live in one place. Anything that uses an enemy only needs to call its methods. You do not need to know how the damage is calculated to use it, and that separation keeps large projects understandable.

I'd like to point out that none of this is special to games. Ordinary software is full of classes. A window on your computer is an instance of a window class. A file in a document editor is an instance of a document class. The same pattern, one definition and many objects with their own state, shows up almost everywhere once you start looking. Games just make it very visible, because every enemy and coin is on the screen.

So to recap. A class is the blueprint. An object is an instance made from it, with its own fields. Fields hold data and methods hold behaviour. Copying a class by hand works for a while, but a rule change then needs many edits. One definition, many instances, means a change in one place reaches every object. Public fields show up in the editor for tuning, and private fields protect the rules.

Next time we will look at how these classes get attached to things in the scene, and how the scene connects to the code. For now, try writing a small class of your own, something with a field or two and a method, and make three instances of it. Change one, and notice what stays the same. That little experiment is the whole idea in practice. Thanks for watching, and I'll see you in the next one.
NARRATION>>>

## Slots

```json
{
 "format_class": "series episode, concept then code",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.04,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.11,
 "first_notation_frac": 0.37,
 "payoff_frac": 0.71,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "one cookie cutter -> many cookies -> two kinds",
 "roadmap": "one-line",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.56,
 "caveat_type": "none",
 "recurring_anchor": "the enemy class and its copies, reused in every section",
 "sponsor_frac": null,
 "ending_type": "hook-callback",
 "teaser": false,
 "wpm": 170,
 "median_beat_s": 45,
 "beat_sequence": ["hook", "roadmap", "analogy", "definition", "toy-world", "demo-sim", "brute-force", "wall", "misconception-defuse", "demo-sim", "generalize", "recap"],
 "top5_moves": ["analogy", "brute-force-first", "failure-shown", "minimal-definition-then-refine", "visible-repetition"],
 "absent3_moves": ["humor", "inline-quiz", "expert-dialogue"]
}
```
