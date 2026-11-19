# Script v3: Vsauce, _UTZDR1Go24

- channel: Vsauce
- id: _UTZDR1Go24
- title: LEGO TACO! And Other Great Images -- IMG! Episode #47
- duration: 258 s (4:18)
- condition: v3
- recall: vague
- exemplars read: _di83KPJY3s, 7c9f9sr6BPg

## Content skeleton

- Premise: the most famous photo of Earth is over fifty years old and still feels new.
- Earth from Apollo 17 in 1972: the planet looks small, soft and mostly ocean.
- Voyager 1 in 1990: a pale blue dot from billions of kilometers away.
- Odd images: a plastic model that looks like food; scale and perspective decide what the brain believes.
- A camera compresses space; two mountains can look like neighbors.
- Three tests for a great image: a true surprise, a familiar thing seen anew, or a new question.
- Caveat: captions and crops change how an image reads; check the source.
- Teaser: the next piece follows one place across decades.

## Beat sheet

| m:ss | beat | what is said or shown |
|---|---|---|
| 0:00 | hook | Premise: the most famous photo of Earth is over fifty years old and still feels new. |
| 0:20 | story | Apollo 17, 1972: the Blue Marble; the planet is mostly ocean. |
| 0:55 | story | Voyager 1, 1990: a pale blue dot from about six billion kilometers. |
| 1:30 | demo-sim | The plastic LEGO taco: a model that looks like food, shown at scale. |
| 2:00 | analogy | Scale and perspective: the brain compares the size in the photo to the size in life. |
| 2:25 | misconception-defuse | A camera compresses space; two mountains can look like neighbors. |
| 2:50 | advice | Three tests for a great image: a surprise, a familiar thing seen anew, a new question. |
| 3:15 | caveat | Captions and crops change how an image reads; check the source. |
| 3:40 | teaser-next | Next up: one place across fifty years. |

## Narration

<<<NARRATION
The most famous photo of Earth is more than fifty years old. You have probably seen it many times, and it still feels new. I think that is because it shows us something we cannot see from the ground. Begin with the big one, then wander through a few stranger images.

In December 1972, the crew of Apollo 17 took a photograph of the whole sunlit Earth. The image became known as the Blue Marble. The planet looks small, soft, and surprisingly calm. Did you notice how much of it is ocean? I did, the first time I really looked. Every border you know is invisible in that picture.

Now go much farther out. In 1990, the Voyager 1 spacecraft turned its camera back toward home, from billions of kilometers away. The result is a single speck of pale blue light, suspended in a sunbeam. Carl Sagan called it a pale blue dot. Few of us think about how small Earth looks from out there. Zoom in on it, and you will still see a speck. I find that humbling in a useful way.

Some images are stranger. Take the LEGO taco, a tiny plastic model that looks good enough to eat. Photographers love it because it plays with scale. A snack that is only a few centimeters long can fill a whole frame. Can you tell it apart from real food at first glance? Many people cannot, and that is the point. I like how quickly the eye gives up.

Here is a rule that helps with odd images. Ask what the size looks like in the photo, and then ask what the size is in real life. Your brain uses the two to guess scale. If they do not match, the image looks wrong, and you feel the tilt before you can explain it. The brain is built to compare, so that is how most tricks work. It is also why tiny things can look huge.

Some of the best images are honest about perspective. A photo of a bridge can make it look longer than it is, because the camera compresses space. Distant mountains can look like neighbors, even when they are far apart. Most people trust cameras, so when a picture bends the rules, the surprise is bigger. When you look closely, you can see the trick. I think that surprise is the best part.

So what makes an image great? I would say it does one of three things. It shows you something true that you did not expect. It shows you something familiar from a new angle. Or it makes you ask a question you had not thought of. Does your favorite picture do one of those? Mine usually does most of them.

Be careful, though. Captions, dates, and crops can all change how a picture reads. A caption can turn a harmless shot into something misleading, and the internet is full of images that have been cut, reversed, or recolored. Check the source before trusting the story. That habit matters more than any photo.

Next up, we look at how a place changes over the decades. Watch for the details that move and the ones that never do. You may be surprised which is which. And as always, thanks for watching.
NARRATION>>>

## Slots

```json
{
 "format_class": "premise-claim image tour with two space photos and a habit tip",
 "answer_given_upfront": true,
 "hook_type": "premise-claim",
 "first_question_frac": 0.3,
 "first_concrete_object_frac": 0.07,
 "first_new_idea_frac": 0.05,
 "first_notation_frac": null,
 "payoff_frac": 0.9,
 "misconception": "planted-myth-defused",
 "brute_force_first": false,
 "examples_count": 3,
 "example_growth": "Blue Marble -> pale blue dot -> plastic taco at scale",
 "roadmap": "none",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.8,
 "caveat_type": "approximation",
 "recurring_anchor": "the speck of blue; the size you expect",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": false,
 "wpm": 139,
 "median_beat_s": 30,
 "beat_sequence": ["hook","story","story","demo-sim","analogy","misconception-defuse","advice","caveat","teaser"],
 "top5_moves": ["story","demo-sim","misconception-first","honest-caveat","teaser-next"],
 "absent3_moves": ["build-and-verify","inline-quiz","generalize-to-other-domains"]
}
```

```json
{"verified_trace": {"wpm": "PASS 139.00 (target 129.14-147.37, median 138.97)", "you_rate": "PASS 3.10 (target 2.11-3.3, median 2.9)", "i_rate": "PASS 1.28 (target 0.75-1.3, median 1.03)", "we_rate": "PASS 0.73 (target 0.41-0.78, median 0.71)", "num_rate": "PASS 1.82 (target 1.14-1.87, median 1.4)", "hedge_rate": "PASS 0.18 (target 0.0-0.39, median 0.17)", "example_rate": "PASS 0.00 (target 0.0-0.0, median 0.0)", "q_rate": "PASS 0.73 (target 0.49-1.0, median 0.71)", "sent_len": "PASS 10.54 (target 10.28-12.63, median 11.41)", "switch_sponsor": "PASS detected=False default=OFF", "switch_teaser": "PASS detected=False default=OFF", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (premise-claim vs premise-claim)", "ending_type": "MATCHES default (teaser-next vs teaser-next)", "summary": "9/9 numeric targets pass"}}
```
