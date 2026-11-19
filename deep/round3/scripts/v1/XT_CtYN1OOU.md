# Header
- channel: SebastianLague
- id: XT_CtYN1OOU
- title: Introduction to Game Development (E02: classes)
- duration: 510 s (8:30)
- condition: v1
- recall: vague

## Content skeleton
- Why we need classes: keeping data about many similar things together.
- Toy world: a pile of paper cards, each with a name and a number.
- Brute force: one variable per card; the code is repetitive and fragile.
- Wall: a copy-paste bug where one card is updated and the others are not.
- Minimal definition: a class is a blueprint with fields and methods.
- Cookie-cutter analogy for a class and its instances.
- Constructor sets the starting values for each instance; three cubes with different colours.
- Misconception: each instance is not a copy of the code; the data is separate, the code is shared.
- Caveat: inheritance is skipped; teaser for script communication.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Why do we need classes at all? Question stated on screen |
| 0:25 | roadmap | Cards, one class, then many instances |
| 0:50 | toy-world | A pile of paper cards with a name and a number each |
| 1:30 | brute-force | One variable per card; the code is repeated by hand |
| 2:30 | wall | Copy-paste bug: one card changed, the rest not |
| 3:10 | definition | A class: a blueprint with fields and methods, minimal form |
| 4:10 | demo-sim | Class with fields; spawn three instances; each holds its own values |
| 5:20 | analogy | Cookie cutter: one shape, many cookies, each with its own icing |
| 5:50 | misconception-defuse | Instances are not copies of the code; the data is separate, the methods are shared |
| 6:30 | demo-sim | Constructor sets starting values; sweep from one to five instances |
| 7:40 | caveat | Inheritance skipped; it comes later |
| 8:00 | recap | Blueprint, fields, instances, constructor |
| 8:20 | teaser | Next episode: scripts talking to each other |
| 8:30 | coda | Sign-off |

<<<NARRATION
Why do we need classes at all? You can get a long way in a game without them. You can write a variable for every enemy, every card, every door. But the code starts to look wrong after a while, and the reasons it looks wrong are the reasons classes exist. That is the question for this episode.

Here is the plan. We start with a pile of cards, we try to keep track of them the dumb way, and then we introduce one class and make as many instances of it as we need.

The toy world is a pile of paper cards. Each card has a name and a number on it. Imagine you have six cards, and you want the code to know each card's name and number. That is all we need to model. Six cards, six names, six numbers. Nothing fancy, but it is a real problem.

The dumb version is the obvious one. Make one variable for each card. So there is a variable for the first card's name, another for its number, another for the second card's name, and so on. The code works. It stores all six cards, and I can print each one. It is the brute-force answer, and it is the one I would write first if I were in a hurry.

The trouble shows up when I change something. Say I want to add a third value to each card, a colour. Now every card needs a new variable, and I have to add it in six places. I add it to five of them and forget the sixth. The program runs, and one card has no colour, or the wrong colour, and nothing tells me why. That is the wall. The code is repetitive, and every repetition is a chance to make a copy-paste mistake.

So the problem is not that the data is hard. The problem is that the data for one card is spread across several unrelated variables, and nothing ties them together. If one card's values belong together, the code should say so.

That is what a class is for. Here is the definition, as small as I can make it. A class is a blueprint. It says what data each thing holds, which are called its fields, and what it can do, which are called its methods. That is the whole definition for now. It does not do anything by itself. It is a description of a kind of thing.

Let's make the card class. It has a name field and a number field. Then I create three instances of it, from the same blueprint. Each instance is a separate card, with its own name and its own number. Changing the number on one instance does not change the others. I print all three, and each one holds its own values. That is the first real thing a class gives you: many things, one description.

It is a bit like a cookie cutter. The cutter is the class. It defines the shape, and it is the same shape every time. Each cookie you cut is an instance. They all have the same outline, but each one can have its own icing, its own colour, its own tiny decoration. The cutter does not store the icing. The cookies do.

Now a misconception I had to clear up for myself. When I first learned this, I thought each instance was a full copy of the code. It is not. The data is separate for every instance, so each card keeps its own name and number. The methods, which are the functions attached to the class, are shared. There is one copy of the code, and many copies of the data. Once I saw that, the memory picture made sense, and I stopped worrying that every card carried a whole program around with it.

Next, the constructor. A constructor is a method that runs when you make a new instance, and its job is to set the starting values. Without it, every new card starts with empty values, and you have to set them by hand afterwards. With it, you pass in the name and number, and the card is ready to use. Forgetting to set a value in the constructor is an easy mistake, so I test it.

Here is the test. I spawn one card, then two, then three, then five, and I print the values each time with the same format. Every instance shows its own starting values, and none of them are blank. The output is the same shape for every count, so any missing field is obvious in the printout. If a value was not set, I see a blank line in exactly the same place every time.

I want to show the three cubes now, because that is the version that looks like a game. Three cubes, one class, each with a different colour. The class defines the cube's colour field and a method that applies it. The cubes all share the same code, so if I change the method, all three change in the same way. But each one keeps its own colour, so they still look different. That is the cookie cutter again, in a scene.

Here is the honest bit. I have skipped inheritance. That is the feature where one class can build on another, so that a special kind of card can reuse everything a normal card does and add its own parts. It matters a lot in larger projects, and it is easy to misuse. I am not going to cover it here, because I want the core idea to be clear first. It comes later, and it is much easier to understand once you are comfortable with the blueprint and instance split.

So let's recap. A class is a blueprint with fields and methods. An instance is one thing made from that blueprint, with its own field values. The constructor sets the starting values when an instance is made. And the code is shared, while the data is separate for each instance.

Go back to the six cards from the start. Instead of six names, six numbers and six colours scattered around the code, there is now one card class, and six instances of it. Adding a new field means changing one place, not six. That is the whole reason for the structure.

Next time we will look at scripts talking to each other, because a card on its own is not much use. A door needs to know about a switch, and a score needs to know about a coin. That is where the class structure starts to pay off in a real game.

Thanks for watching.
NARRATION>>>

## Slots

```json
{
 "format_class": "build-break-fix devlog, pile of cards to classes",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.18,
 "first_notation_frac": 0.37,
 "payoff_frac": 0.8,
 "misconception": "staged-early",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "six variables -> one class -> many instances",
 "roadmap": "one-line",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.01,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the card name printed to the console after each change",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 40,
 "beat_sequence": ["hook","roadmap","toy-world","brute-force","wall","definition","demo-sim","analogy","misconception-defuse","demo-sim","caveat","recap","teaser"],
 "top5_moves": ["toy-world","brute-force-first","failure-shown","analogy","visible-repetition"],
 "absent3_moves": ["hook-paradox","commit-to-answer","second-person-role"]
}
```
