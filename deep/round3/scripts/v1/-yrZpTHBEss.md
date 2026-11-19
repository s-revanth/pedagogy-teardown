# Header

- channel: Vsauce
- id: -yrZpTHBEss
- title: What Color Is A Mirror?
- duration: 301 s (5:01)
- condition: v1
- recall: vague

## Content skeleton

- Opens on "What color is a mirror?" with a mirror reflecting a red apple
- Sets up the common answer (silver) and holds it open
- Defines colour as the light an object sends back to the eye
- Explains a mirror's behaviour with a reflectance curve, flat for a good mirror and warm for gold
- Uses a ball-catcher analogy for a mirror that returns nearly all the light
- Generalises the reflection idea to walls, water and painted surfaces
- Adds the caveat that coatings tarnish, then returns to the question with a stated answer

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | "What color is a mirror?" Shows a mirror reflecting a red apple. |
| 0:18 | misconception-defuse | Most people say silver; hold that answer for a minute. |
| 0:35 | roadmap | Three questions: why any colour at all, what the mirror sends back, how coatings change it. |
| 0:55 | toy-world | A white flashlight on a red apple; the apple keeps red and sends it back. |
| 1:40 | definition | Colour is the light an object sends back to your eye. |
| 2:05 | demo-sim | Reflectance curve drawn: a flat high line for a good mirror; a warm tilt for gold. |
| 2:50 | analogy | A mirror as a ball-catcher that throws back almost every ball at the same speed. |
| 3:20 | generalize | White wall, pool of water, painted car: the same reflection idea, scattered in all directions. |
| 3:50 | caveat | Coatings oxidise at the edges; a bathroom mirror and a museum mirror can differ. |
| 4:30 | callback | Back to the question: the answer is "neutral, plus a faint tint from the metal." |
| 4:50 | coda | Sign-off. |

## Narration

<<<NARRATION
What color is a mirror? If you answered silver, you're in good company. Most people do. But hold that answer for a minute, because a mirror is one of the strangest objects to ask about.

Here's the plan. We'll look at what makes a mirror look like anything at all, why a mirror seems to have a colour of its own, and what happens when you change the coating.

Start with a simple setup. Shine a white flashlight at a red apple. The apple looks red because it absorbs most of the light that hits it, but it reflects the red part back toward your eye. The light that bounces off is what you see. So colour isn't really a property sitting inside the object. It's the leftover light the object sends back.

Now put the apple in front of a mirror. Look in, and you see a red apple. The mirror is sending back the apple's light. So the question becomes what the mirror itself sends back. If it reflected only some colours, it would look tinted. If it reflected every colour evenly, it would look like a neutral, bright surface.

Here's the key idea, and it's a measurement, not a feeling. Every surface has a reflectance curve. Take each colour of light, from red to blue, and ask what fraction bounces off. A good mirror has a curve that stays high and flat across the whole range. That's why a mirror doesn't look like it has a hue. It returns nearly the same amount of every colour, so the colours you see are the colours that were in front of it.

Look at the coatings. A typical mirror is a sheet of glass, and the reflecting layer is a thin metal film on the back. Silver is common, and it reflects most visible light very well. Aluminium is another common choice, and it reflects evenly and reliably. Gold tints the reflection warm, because it reflects red and yellow better than blue. That's why a gold-coated mirror makes a cold white wall look warm.

So what is the mirror's colour? The honest answer is that it doesn't have one. It has a reflectance curve, and for the good ones that curve is almost flat. If you want a single word, the closest is neutral, which means it's the colour of whatever you put in front of it, plus a little of the metal's own tint.

Here's a useful way to picture it. Think of a mirror as a ball-catcher that throws almost every ball straight back. A good one catches every ball and throws it back at the same speed. A bad one drops some balls. A tinted one throws red balls back better than blue ones. That's what a mirror does to light: it returns the light, with a small bias set by the metal.

Now test the idea on other things. A white wall looks white because it reflects nearly everything evenly, the same trick as a mirror but scattered in every direction. A pool of water, a car's paint, a painted sign: all of them reflect light, and the colour you see depends on what gets reflected and how it's scattered or aimed. The mirror is just the most direct case, because it aims everything back at you.

Mirrors also age. Coatings can oxidise at the edges, and a mirror in a steamy bathroom can grow dark spots. When that happens, the reflectance curve changes, and the mirror looks dimmer or slightly tinted. That's the caveat: the colour of a mirror is a property of its coating, and the coating changes over time. A mirror in a museum and a mirror in a shower might have quite different colours, even if they look the same from across the room.

So go back to the question. What colour is a mirror? It's not silver in the way a spoon is silver. It's a surface built to send back almost all the light that reaches it. The colour you see is the colour that was already in front of it, with a faint tint from the metal and a little bit of wear. Next time you catch your reflection, you're looking at light that has been carefully returned, not at the mirror's own colour at all.

Thanks for watching. Keep an eye on the light.
NARRATION>>>

## Slots

```json
{
 "format_class": "everyday object, misconception then mechanism, answer at end",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.00,
 "first_new_idea_frac": 0.18,
 "first_notation_frac": 0.42,
 "payoff_frac": 0.90,
 "misconception": "planted-myth-defused",
 "brute_force_first": false,
 "examples_count": 4,
 "example_growth": "red apple to walls and water",
 "roadmap": "one-line",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.06,
 "caveat_type": "approximation",
 "recurring_anchor": "the red apple",
 "sponsor_frac": null,
 "ending_type": "hook-callback",
 "teaser": false,
 "wpm": 170,
 "median_beat_s": 27,
 "beat_sequence": ["hook", "misconception-defuse", "roadmap", "toy-world", "definition", "demo-sim", "analogy", "generalize", "caveat", "callback", "coda"],
 "top5_moves": ["hook-question", "misconception-first", "toy-world", "analogy", "generalize-to-other-domains"],
 "absent3_moves": ["brute-force-first", "learner-discovers", "inline-quiz"]
}
```
