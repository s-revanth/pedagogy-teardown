# Script v3: Vsauce, -yrZpTHBEss

- channel: Vsauce
- id: -yrZpTHBEss
- title: What Color Is A Mirror?
- duration: 301 s (5:01)
- condition: v3
- recall: vague
- exemplars read: zRP82omMX0g, F981CD-8YEg

## Content skeleton

- Premise: a mirror seems to have no color, and that is only half true.
- A mirror is clear glass over a thin metal layer; the metal does the reflecting.
- Silver and aluminum reflect nearly every color about equally, so the reflection keeps its colors.
- A mirror in a dark room looks black because it has no light to return.
- Gold-coated mirrors are the exception: they do have a color, and it is yellow.
- Each bounce loses a little light, which is why mirror tunnels fade.
- Caveat: the reflectance figures are typical values, not exact for every mirror.
- Payoff: the color belongs to the light, not to the glass.

## Beat sheet

| m:ss | beat | what is said or shown |
|---|---|---|
| 0:00 | hook | Premise: a mirror seems to have no color, and that is only half true. |
| 0:20 | definition | Clear glass over a thin metal layer; the metal does the reflecting. |
| 0:55 | toy-world | Red flashlight, blue flashlight: the mirror looks like the light you give it. |
| 1:30 | misconception-defuse | In an empty dark room, the mirror looks black; it is not hiding a color. |
| 2:05 | story | Gold-coated telescope mirrors: the one that chooses a color. |
| 2:40 | demo-sim | Two mirrors facing each other: each bounce loses a little light. |
| 3:20 | caveat | Typical reflectance figures; the numbers are rounded. |
| 3:50 | generalize | Your brain makes the final call on the color you see. |
| 4:15 | advice | Test your assumption: turn the light up and try a colored bulb. |
| 4:40 | coda | A mirror is a way of returning light; the color belongs to the light. |

## Narration

<<<NARRATION
A mirror seems to have no color at all; that is only half true, and the other half is more interesting. Look into one and you see the room, your face, and the lamp behind you. So what color is it? We can only answer that by asking what the mirror does with light. Let's take the question seriously, because the answer says a lot about light.

Start with the glass. Plain glass is clear, which means it lets most visible light pass through; a mirror is not just glass with a shine on it. The shine comes from a thin layer of metal on the back, usually silver or aluminum, far thinner than a sheet of paper. The glass is only a protective window. You can see the metal if you have ever broken a mirror and looked at the back.

Think about what that metal does; it reflects a large share of the visible light that hits it. Silver reflects most of the light across the whole visible range, which is why it looks almost neutral. Aluminum does something similar. So the mirror returns nearly every color about equally; that is why the reflection looks like the real world, colors and all.

Here is the tricky part; a mirror does not have a color of its own the way paint does. Paint absorbs some colors and reflects others, and that is why a red wall looks red. A mirror absorbs only a small share of light, so it hands almost everything back. What you see is the light coming in, not a color stored in the glass.

Try it yourself. Shine a red flashlight at a mirror in a dim room, and the mirror looks red. Switch to a blue flashlight, and it looks blue; you will notice that the mirror never picks a color on its own. It only borrows what you give it. Try three bulbs, red, green, and blue, and the mirror follows each one in turn. I find that simple result surprisingly satisfying; that is the whole idea in one small experiment.

So what color is a mirror in an empty, dark room? Turn off the lights, and the answer changes; a mirror with no light to reflect looks black. It is not hiding a color; it is simply reflecting nothing at all.

Now the question gets more interesting; some mirrors are not silver at all. Telescope mirrors are often coated in gold, because gold reflects infrared light very well; look at one in daylight, and it will look golden. Gold absorbs more blue light than the other colors, so the reflected light takes on a yellow cast. A gold mirror is a mirror that chose a color, and I find that fun.

Let's put numbers on it; the best silver mirrors reflect around 95 percent of visible light. Each time light bounces off, a small share disappears. That is probably why a mirror looks slightly darker than the scene it reflects, and we notice it more in a dim room. Two mirrors facing each other can send light back and forth many times, and the image fades. Why does the tunnel fade? Each bounce costs a little light.

There is one more step between the mirror and the color you see. Your eyes receive a pattern of light that bounced off the surface, and your brain builds the picture from that pattern. We can test that idea with almost any shiny object, from a spoon to a car door. In a sense, your brain makes the final call. We rarely think about this, but it is part of why colors look so stable even when the lighting changes. I like that the mirror is so honest about it; you may find that surprising.

So, what color is a mirror? Here is the honest answer; a mirror is nearly colorless, because it reflects nearly every color about equally. A mirror in the dark is black; a gold mirror is yellow; a mirror in a red room is red. The color you see depends on the light, the coating, and your eyes; the mirror is not a color; it is a way of returning light.

I like that answer, because it turns a simple question into a lesson about light. You can test your own assumptions whenever you look at a reflection. Ask what the light is doing and where it came from.

Here is a quick challenge; look at a mirror in a dim room, then turn the light up slowly. Watch how the reflection changes as the light grows. Then try a colored bulb; you will see that the mirror never adds a color of its own. We can check this every morning in the bathroom, and it is a good excuse to look again.
NARRATION>>>

## Slots

```json
{
 "format_class": "premise-claim physics explainer with two demos and a reflection tip",
 "answer_given_upfront": true,
 "hook_type": "premise-claim",
 "first_question_frac": 0.12,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.03,
 "first_notation_frac": null,
 "payoff_frac": 0.93,
 "misconception": "planted-myth-defused",
 "brute_force_first": false,
 "examples_count": 3,
 "example_growth": "red flashlight -> dark room -> gold telescope mirror",
 "roadmap": "none",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.9,
 "caveat_type": "approximation",
 "recurring_anchor": "the light that the mirror borrows",
 "sponsor_frac": null,
 "ending_type": "impact-coda",
 "teaser": false,
 "wpm": 146,
 "median_beat_s": 30,
 "beat_sequence": ["hook","definition","toy-world","misconception-defuse","story","demo-sim","caveat","generalize","advice","coda"],
 "top5_moves": ["toy-world","misconception-first","demo-sim","honest-caveat","generalize-to-other-domains"],
 "absent3_moves": ["build-and-verify","inline-quiz","teaser-next"]
}
```

```json
{"verified_trace": {"wpm": "PASS 146.00 (target 138.69-153.51, median 145.81)", "you_rate": "PASS 2.37 (target 2.01-4.3, median 3.62)", "i_rate": "PASS 0.50 (target 0.45-0.97, median 0.65)", "we_rate": "PASS 0.87 (target 0.83-1.25, median 0.99)", "num_rate": "PASS 1.37 (target 1.26-2.11, median 1.76)", "hedge_rate": "PASS 0.12 (target 0.12-0.21, median 0.16)", "example_rate": "PASS 0.00 (target 0.0-0.27, median 0.12)", "q_rate": "PASS 0.50 (target 0.42-0.94, median 0.58)", "sent_len": "PASS 14.85 (target 13.27-15.14, median 13.71)", "switch_sponsor": "PASS detected=False default=OFF", "switch_teaser": "PASS detected=False default=OFF", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (premise-claim vs question or premise-claim)", "ending_type": "MATCHES default (impact-coda vs impact-coda)", "summary": "9/9 numeric targets pass"}}
```
