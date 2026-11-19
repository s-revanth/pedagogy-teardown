# SebastianLague | XT_CtYN1OOU | Introduction to Game Development (E02: classes)

- channel: SebastianLague
- id: XT_CtYN1OOU
- title: Introduction to Game Development (E02: classes)
- duration: 510 s (8:30)
- condition: v2
- recall: vague (I recognise that a Unity beginner series exists, not this episode's content)
- class (step 0): under-10 min (8:30); format = designed-lesson series lesson (E02 label), code-along; answer not stated; topic = C# classes, instances, fields and methods
- exemplars read: deep/compact/r_It_X7v-1E.txt (Coding Adventure: Ecosystem, 6:40) read in full for under-10 rhythm; deep/compact/TURzbXTNaA0.txt (I Created a (terrible) Video Game Console, 9:21) read in full for the just-in-time explanation voice

## Content skeleton
- Premise: more than one object must move, so the behaviour goes into a class.
- The enemy cube, painted red, with last episode's movement script attached.
- Minimal definitions: a class is a template, an instance is one object built from it.
- Enemy class with a speed field; duplicate the cube; each instance keeps its own speed (test by changing one value).
- Typo failure: Speed and speed mismatch shows as a red underline; the fix is to match the spelling.
- Brute-force first: copy and paste the script for each enemy; cost shown when one change needs three edits.
- Class fix (change once) with a cookie-cutter analogy; a Move method called from Update.
- Three enemies at speeds 2, 4 and 6 with rough timings; public versus private fields; a Player exercise; teaser on two objects talking.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Premise: more than one thing must move, so the behaviour goes into a class. |
| 0:25 | toy-world | The enemy cube, now painted red, with last episode's movement script attached. |
| 0:55 | definition | Class defined as a template; instance defined as one object built from it; minimal definition. |
| 1:30 | definition | Enemy class written with a field speed equals 2; each instance gets its own copy of the field. |
| 2:05 | demo-sim | Update uses speed; script attached; cube duplicated; both cubes move independently. |
| 2:45 | demo-sim | Test: first cube's speed set to 5 in the inspector; second cube stays at 2; static would have shared it. |
| 3:15 | demo-sim | Typo: Speed with a capital S in one place and speed in another; red underline and error on screen; fixed. |
| 3:45 | brute-force | Copy and paste the whole script for a second enemy; one change now needs edits in every copy. |
| 4:25 | demo-sim | The class fixes it: Update is changed once and every enemy picks up the change on the next play. |
| 4:55 | analogy | Cookie cutter: the cutter is the class, the dough is each object's data, each cookie is an instance. |
| 5:30 | definition | Method Move introduced; Update calls Move every frame; logic in one named place. |
| 5:55 | demo-sim | Second script finds all enemies and calls Move on each; three cubes move with their own speeds. |
| 6:25 | caveat | Speeds set to 2, 4 and 6; timings are rough and depend on view size, so only the order is checked. |
| 6:55 | demo-sim | Public field appears in the inspector for tuning; private field hidden; public kept while still tuning. |
| 7:20 | payoff | Rule of thumb: a new kind of thing in the scene becomes a class once more than one of it is needed. |
| 7:45 | advice | Exercise: make a Player class with the same Move method and a different speed; find the shared and the separate parts. |
| 8:10 | teaser | Next time two objects talk to each other, so an enemy can notice the player. |

## Narration
<<<NARRATION
Last time we made one cube move from the keyboard. This time we want more than one thing that moves, and the way to do that in C# is with classes. A class is the idea that lets us write the behaviour once and reuse it for as many objects as we like. By the end of this part we'll have three enemies moving around the scene, all driven by one script, and we'll see exactly why that's useful.

Here is the enemy cube, the one we'll use for everything in this episode. It's the same cube as before, only now it's painted red so we can tell it apart from the player. Right now it has the movement script from last time attached, and that script works, but it only moves one object. If we want a second enemy, we need a way to make another object that behaves the same way without copying the code by hand.

Let's define the terms first, because they're easy to mix up. A class is a template, a description of what an enemy is and what it can do. An object made from that template is called an instance, so one class can produce many instances. The minimal definition is this: a class describes the shape, and an instance is one real thing built from that shape. We'll refine it as we go.

So we write the class, and we name it Enemy, and inside it we declare a field called speed, with the type float and the value 2. A field is a value that belongs to each instance, so every enemy we make gets its own copy of speed. We'll see why that matters in a moment, because it's the part that makes the class useful rather than just tidy.

Now the Update function goes inside the class, and it looks almost exactly like the movement code from last time. It uses speed, multiplies by Time dot deltaTime, and moves the transform along the x axis. The only real change is that the speed now belongs to the enemy rather than to the script file as a loose variable, and that small shift is the whole point of a class.

We attach the Enemy script to the cube, press play, and the cube moves at speed 2. Then we duplicate the cube, which gives us a second object with the same script attached. Both cubes move, and they move independently, because each one has its own copy of speed. That's the first real test, and the result is what we wanted.

For the test I want to check one specific thing. If I change the speed of the first cube in the inspector to 5, the second cube should stay at 2. If it changes too, we've made a mistake, probably by declaring speed as static, which shares one value between every instance. I set the first cube to 5 and the second cube keeps moving at 2, which is the behaviour we want from an instance field.

Now a failure, because it's worth seeing what a typo does. If I write Speed with a capital S in one place and speed with a lowercase s in another, the editor underlines the mismatch in red. The error message tells us which line is wrong, and the fix is to make the spelling match. It's a small thing, but it's one of the most common mistakes, and it's exactly the kind of mistake that appears once we have several scripts that talk to each other.

Before we go further, I want to show the approach I'd used first, because it's the one most people try. I copied the whole script, pasted it into a second file, renamed the class, and tweaked the numbers. That works for two enemies, and I'd say it's fine for a quick test. But then I wanted to change how every enemy moves, and I had to edit both files, then the third copy, then remember to edit all of them the same way. That's the cost of copy and paste.

The class solves that problem, and we change the Update function once, and every enemy in the scene picks up the change on the next play. We don't have to keep several copies in sync, because there's only one copy. That's a small win for two enemies and a large win for twenty, which is the scale where copy and paste stops being a reasonable option.

It helps to have a picture for this, and for example, a cookie cutter is a class. The shape of the cutter is the template, the dough is the data each object holds, and every cookie you cut is an instance. You can cut ten cookies from one cutter and each one has the same shape, but each one can have its own icing, which is like each enemy having its own speed. That's the mental model I'd keep in your head.

Next let's add a method, and a method is a function that belongs to a class, and it's a good place to put behaviour that the instance needs to perform. I'll move the movement code into a method called Move, and Update will simply call Move every frame. The result looks the same on screen, but the logic is now in one clearly named place, which makes it easier to read and to test.

Let's test the method by calling it from somewhere else. I'll make a second script that finds all the enemies in the scene and calls Move on each of them. With three enemies, the three cubes move, and each uses its own speed value. That's the first time the scene is controlled from outside the enemies, and it's a useful pattern to know early.

We set the speeds to 2, 4 and 6, one value for each of the 3 instances, so the three enemies move at clearly different rates. The fastest reaches the edge of the view in about 3 seconds, the middle one takes about 5, and the slowest takes roughly 8. Those numbers are rough, because they depend on the size of the view, but the order is what we're checking, and the order comes out right every time.

One more thing to check is what happens when a field is public. If I make speed public, it appears in the inspector, and I can change it without opening the script. If I make it private, it's hidden from the inspector, and only code inside the class can change it. Public fields are convenient for quick tuning, and private fields are safer once the behaviour is settled. We'll use public for now, because we're still tuning.

Whenever we need a new kind of thing in the scene, we ask whether it should be a class, and the answer is usually yes once we need more than one of it, because one template keeps them all consistent.

Let's finish with one question I'd like you to try in your own project. Make a second class called Player, and give it the same Move method but a different speed. Then ask yourself which parts are the same and which parts are different, because that's the boundary between the class and the instance. Getting that boundary right is most of what object-oriented code is about.

Next time we'll make two of these objects talk to each other, so that an enemy can notice the player and react to it. That means one script will need to find another object, and it's the first step toward a real interaction in the scene. Thanks for watching, and I'll see you in the next episode.
NARRATION>>>

## Slots
```json
{
 "format_class": "designed-lesson series lesson (E02): toy world, minimal definitions, copy-paste brute force, cookie-cutter analogy, typo failure, teaser",
 "answer_given_upfront": false,
 "hook_type": "premise-claim",
 "first_question_frac": 0.05,
 "first_concrete_object_frac": 0.05,
 "first_new_idea_frac": 0.11,
 "first_notation_frac": 0.18,
 "payoff_frac": 0.86,
 "misconception": "none",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "one enemy -> two copies -> three enemies",
 "roadmap": "none",
 "viewer_turn": "none",
 "viewer_turn_frac": null,
 "caveat_type": "approximation",
 "recurring_anchor": "the enemy cube with its speed field, reused in 6+ passes",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "beat_sequence": [
  "hook",
  "toy-world",
  "definition",
  "demo-sim",
  "demo-sim",
  "brute-force",
  "demo-sim",
  "analogy",
  "definition",
  "demo-sim",
  "caveat",
  "payoff",
  "advice",
  "teaser"
 ],
 "top5_moves": [
  "toy-world",
  "analogy",
  "brute-force-first",
  "minimal-definition-then-refine",
  "failure-shown"
 ],
 "absent3_moves": [
  "hook-paradox",
  "commit-to-answer",
  "expert-dialogue"
 ],
 "wpm": 152,
 "median_beat_s": 30
}
```

```json
{"rule_trace": {
 "U1": "applied: under-10 band and series label (E02); roadmap, recap and callback dropped; fixed 20-25 s beat grid dropped; notation limited to code introduced after the enemy cube",
 "U2": "n/a: neither the title nor the first 40 s states an answer or thesis",
 "U3": "applied: teaser only (series label); no hook callback since there is no hook question",
 "U4": "applied: the enemy cube and its speed field are reused in 6+ passes, each adding one layer (class, copy, method, caller, public field)",
 "U5": "applied: the speed field is introduced after the enemy cube is on screen, within 60 s; no formulas",
 "U6": "applied: about 152 wpm on 1,288 words over 8:30 (under-10 band); beats of 25-50 s with the code screen visible",
 "U7": "applied: no roadmap, no vote, no planted misconception; the copy-paste approach is the presenter's own first try, shown, not announced",
 "U8": "applied: approximation caveat on the rough timings at 6:25",
 "U9": "n/a: no binary decision or absurd magnitude to pause on",
 "U10": "n/a: not a history-of-invention or escalating-antagonist video",
 "U11": "n/a: title names a lesson topic (classes), not an application or end state",
 "C1": "applied: designed-lesson series format (code-along), not impersonal lecture and not devlog",
 "C2": "applied: the enemy is rerun with one change per pass (copy, class, method, caller, field visibility)",
 "C3": "n/a: not lecture format; no pause-the-video quiz",
 "C4": "n/a: no design source named; the language definitions are given in the narration",
 "C5": "n/a: series lesson, not a devlog opening",
 "D1": "applied: failure on screen (Speed and speed mismatch gives a red underline and an error line), then fixed",
 "D2": "n/a: repairs are named by function (class, method, matching spelling), not after the failure",
 "D3": "applied: one speed changed (to 5) to isolate that each instance holds its own value",
 "D4": "n/a: no honest-close bundle; the close is an advice line and a teaser",
 "D5": "n/a: no equation",
 "N1": "applied: 152 words per minute (measured), inside p25-p75 141-180",
 "N2": "n/a: over-10 band rule; this video is under-10 min",
 "N3": "applied: 0.54 you/your per 100 words (measured), inside p25-p75 0.23-0.78",
 "N4": "applied: 1.40 I/me/my per 100 words (measured), inside p25-p75 0.94-2.81",
 "N5": "applied: 3.11 we/us/let's per 100 words (measured), inside p25-p75 2.55-5.7",
 "N6": "applied: 1.01 numbers per 100 words (measured), inside p25-p75 0.95-2.12",
 "N7": "applied: 0.00 question marks per 100 words (measured), inside p25-p75 0.0-0.09",
 "N8": "applied: 19.5 words per sentence (measured), inside p25-p75 19-25",
 "N9": "applied: 0.16 hedges per 100 words (measured), inside p25-p75 0.11-0.35",
 "N10": "applied: 0.08 example cues per 100 words (measured), inside p25-p75 0.03-0.18",
 "B1": "applied: no sponsor read",
 "B2": "applied: one-line teaser, because the video is in a series",
 "B3": "n/a: roadmap withheld; a short lesson does not call for one",
 "B4": "applied: no spoken recap in the last 20%; the late rule of thumb summarises a design choice, not the lesson"
}}
```
