# Header
- channel: 3blue1brown
- id: HZGCoVF3YvM
- title: Bayes theorem, the geometry of changing beliefs
- duration: 911 s
- condition: v3
- recall: vague (the title is recognised; the script is written from the v3 rules and general subject knowledge, not from the video)
- exemplars read: deep/corpus/compact/U_85TaXbeIo.txt, deep/corpus/compact/EK32jo7i5LQ.txt

## Content skeleton
- Claim up front: updating a belief has an exact answer that can be drawn as an area.
- Toy world: a driver who is either careful (prior three tenths) or reckless, and a braking-early observation.
- Picture: a unit square split into strips whose widths are the priors.
- Shade each strip by the likelihood of the evidence, discard the unshaded part, rescale.
- Worked result: twenty-four over thirty-eight, about sixty-three percent. Contrast case: late braking gives about one tenth.
- Second observation reuses the posterior as the next prior (about eighty-seven percent).
- Base-rate check: a rare condition, a sensitive test and false positives give about eight percent.
- Close: Bayes' theorem as bookkeeping of surviving proportions.

## Beat sheet (about 2200 spoken words, about 750 s of speech inside 911 s)
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Premise: an exact answer exists for how much a belief should move, and it is a picture |
| 0:20 | toy-world | Careful or reckless driver; prior about thirty percent; early braking on a corner |
| 1:10 | viewer-turn | Rhetorical: how much should that one observation move you |
| 1:40 | definition | Unit square; vertical strips are the hypotheses, widths are priors |
| 2:50 | derivation | Shade the careful strip and the reckless strip; areas twenty-four and fourteen hundredths |
| 4:20 | payoff | Discard the unshaded part; twenty-four over thirty-eight is about sixty-three percent |
| 5:30 | analogy | The conditional bar read as "within the region" |
| 6:20 | derivation | Late braking case: about one tenth |
| 7:10 | generalize | Strength of the difference between groups equals the likelihood ratio |
| 8:00 | derivation | Second corner: yesterday's posterior becomes the prior; about eighty-seven percent |
| 9:00 | caveat | Likelihoods are estimates; the picture makes the inputs explicit |
| 9:30 | misconception-defuse | Rare condition and a positive test: about eight percent, not eighty |
| 11:30 | generalize | Many hypotheses, then a continuum; same logic, smoother edge |
| 12:40 | coda | Geometry of changing beliefs: carve, discard, rescale |
| 13:20 | coda | Closing line pointing at where the hypotheses go next |

<<<NARRATION
There is an exact answer to how much a belief should change when new evidence arrives, and that answer can be drawn as a picture. The picture is simple, yet it hides more structure than most people expect, and once you can see it, a lot of everyday reasoning begins to look different. Nothing about it requires special talent, only a willingness to keep track of areas carefully.

Consider a concrete situation, because the abstract version is easy to nod along to without really following. Imagine a friend who is either a careful driver or a reckless one, and suppose you honestly have no idea which. You might begin with a hunch that roughly thirty percent of the drivers you could meet are careful, which is a sensible place to start before any evidence arrives. Then you watch her take a sharp corner on a rainy road, and she brakes early, well before the bend. How much should that single observation move you?

Most people's first instinct is that braking early is good evidence for careful driving, so the belief should nudge upward a little. That instinct points in the right direction, but a nudge is not an answer. We want a specific number, and more importantly we want to know exactly where that number comes from, so that we can check it and argue about it. So let's build a picture that makes every piece of the calculation visible at once.

I like to start with a square whose area is one. Think of the whole square as the full set of possibilities you are currently willing to entertain, with each point standing for one way the world could turn out. The horizontal direction will track the type of driver, and the vertical direction will track what she does at the corner, which for now is still unknown to us.

Next, split the square with a vertical line into two strips. The left strip has width three tenths and represents the careful drivers, while the right strip has width seven tenths and represents the reckless drivers. The area of each strip is exactly your prior belief in that hypothesis. Together they fill the whole square, which is exactly what we want, because one of the two must be true.

Now comes the evidence, and this is where the geometry starts doing real work. Suppose careful drivers brake early eighty percent of the time. Inside the careful strip, we shade a horizontal band covering eighty percent of its height, leaving the bottom fifth unshaded. For the reckless drivers, they brake early only one time in five. So inside the reckless strip, we shade a band covering a fifth of its height. Every shaded point now represents a possibility in which the evidence we observed actually happened.

Let's compute the areas of those shaded regions. The careful shaded region has area three tenths times four fifths, which works out to twenty-four hundredths. The reckless shaded region has area seven tenths times one fifth, which is fourteen hundredths. Adding them gives a total shaded area of thirty-eight hundredths. That total is the probability of seeing her brake early in the first place, given everything we currently believe about drivers.

Here is the key move, and it is almost embarrassingly simple. Once you observe the evidence, you can throw away everything that did not happen. All of the unshaded area is gone, because it describes worlds in which she did not brake early, and those worlds are no longer on the table. What remains is only the shaded region, and that shaded region becomes your entire universe of possibilities, so we rescale it to have total area one.

So what is your new belief that she is careful? It is the portion of the surviving shaded area that sits inside the careful strip. That portion is twenty-four divided by thirty-eight, which comes out to sixty-three hundredths. So a single corner has moved you from thirty percent up to around sixty-three percent. I think that is the moment most people first feel the picture click. That is a large jump from one observation, and the picture shows exactly why. The careful drivers were already the group more likely to brake early, and most of the reckless drivers were eliminated by what you saw.

Let me say the same thing in a form that is easy to remember. Your new belief is the fraction of the evidence region that comes from the hypothesis you care about. The denominator is the total chance of the evidence, adding up over every hypothesis. The numerator is the chance that the hypothesis and the evidence are both true together. That ratio is Bayes' theorem, and as we have seen, it is really just a statement about areas in a picture.

Now notice something that often surprises people when they first meet the formula. It is usually written with conditional probabilities, with a little vertical bar that seems to carry no meaning at all. But the bar simply means restricting attention to a region. The probability of careful given brake is the area of the overlap divided by the area of the brake region. If you read the bar as the word within, the whole formula starts to read like a sentence about a picture rather than a string of symbols.

Let's push the example further, because the reverse case is instructive. What if she had instead braked late, well after the bend began? Then the surviving region would be the unshaded parts of each strip. Careful drivers would contribute three tenths times one fifth, which is six hundredths, and reckless drivers would contribute seven tenths times four fifths, which is fifty-six hundredths. The total is sixty-two hundredths, so the chance of careful given late braking is six divided by sixty-two, about one tenth. I find this case more striking than the first, honestly. Your belief has dropped from thirty percent to roughly ten percent. Same picture, opposite conclusion, and nothing new had to be invented to reach it.

This also tells us how strongly evidence ought to move us. The bigger the difference between the two groups' behavior, the more the shading separates them, and the larger the update. If both groups braked early equally often, the shaded bands would have the same height in both strips, and the posterior would simply equal the prior. Evidence that fails to discriminate between hypotheses should not change your mind at all, and the picture shows that immediately, without any algebra.

I want to dwell on that point, because it is easy to overlook in practice. People often treat a piece of evidence as informative just because it is vivid, surprising, or emotionally loaded. The picture asks a sharper question instead: how much more likely is this observation under one hypothesis than under the other? That ratio, which statisticians call the likelihood ratio, controls the size of the update. An observation that is equally likely under both hypotheses is noise, however striking it may feel when you encounter it.

Now let's bring in a second observation. Suppose you watch her take another corner, and once again she brakes early. You can simply repeat the same procedure, but this time you use your new belief of about sixty-three percent as the prior. The careful strip is now sixty-three hundredths of the width, and the reckless strip is thirty-seven hundredths. Shading again with the same eighty and twenty percent bands gives a careful area of sixty-three times eighty hundredths, which is about fifty hundredths, and a reckless area of thirty-seven times twenty hundredths, which is about seven and a half hundredths.

Two observations have taken us from thirty percent to about eighty-seven percent, and we never had to start over. Yesterday's posterior became today's prior, and the geometry kept working without any modification. I think this is the most useful habit to take away from the whole topic. It is a very natural way to think about learning from a stream of evidence, and it is exactly how a careful reasoner should behave when new information keeps arriving over time.

Here is a question I like to ask at this point. Does the order of the observations matter? If you had first seen late braking and then early braking, would you end up in the same place? The answer is yes, and the reason is that the likelihood factors simply multiply, and multiplication does not care about order. In the end, the final belief depends only on the total evidence, which is a comforting property for anything that is supposed to count as rational updating.

Let's think about where the picture could mislead us, because every model has a failure mode. The biggest trap sits in the prior. If your starting belief was very wrong, the evidence has to work much harder to correct it, and the picture makes that effort visible as a narrow strip being overwhelmed by a wide one. People who begin with extreme priors, such as being completely certain of something, will never move at all, because a strip of width zero stays zero no matter what gets shaded. That is a striking consequence, and it helps explain why some beliefs are so resistant to change.

Now for a caveat. The whole picture assumes that you can state the likelihoods, the eighty percent and the twenty percent, with reasonable accuracy. In real life those numbers are often rough guesses, and the geometry is only as good as the inputs you feed into it. Garbage in still means garbage out. I can't stress this enough, though. The real value of the picture is that it forces the inputs into the open, so that you can argue about them directly, instead of letting a vague feeling quietly set the answer behind your back.

Let me test the picture on a case where intuition really goes wrong. Imagine a rare condition that affects one person in a hundred. Suppose a test catches ninety percent of the true cases, but it also falsely flags ten percent of the healthy people who take it. You test positive, and most people instinctively feel the chance that they have the condition must be quite high, perhaps above eighty percent. Now draw the picture. The sick strip has width one hundredth, and ninety percent of it is shaded, which gives nine thousandths. The healthy strip has width ninety-nine hundredths, and ten percent of it is shaded, which is about ninety-nine thousandths. The total shaded area is about one hundred eight thousandths.

So the chance of being sick given a positive result is nine divided by one hundred eight, which is about one twelfth, or roughly eight percent. I'll be honest, that is the number that surprises me most, even after all these years. That is far below the intuition, and the picture makes the reason obvious the moment you look at it. The healthy strip is so wide that its small false-positive band is still bigger than the thin sick band. The real question is not how accurate the test is in the abstract. The real question is how the test's errors compare with how rare the condition happens to be in the first place.

I want to be careful about one subtle point here. The numbers in this example are chosen to be simple, and in practice you would want the best estimates you can get from data. But even with rough numbers, the shape of the reasoning stays robust. Whenever a hypothesis is rare, its prior strip is thin, and thin strips are easily swamped by false positives coming from the much wider strips next to them.

So where does this leave us? We now have a clear procedure that you can carry out on paper. Draw strips for your hypotheses with widths equal to your priors. Shade each strip by the probability of the evidence under that hypothesis. Throw away the unshaded region entirely. Then compare the shaded areas and rescale them so they sum to one. Each step is a concrete act you can perform, and each step has a meaning that you can check against your own intuition.

Why does it matter that this is a geometry problem rather than just a formula? Because geometry gives you a way to reason about the shape of uncertainty. A wide prior combined with a narrow likelihood tells a different story than a narrow prior combined with a wide likelihood, even when the final numbers happen to match. Seeing the shapes lets you ask better questions about which assumption is really doing the work in your conclusion.

Let's handle the case of many hypotheses instead of only two. I'll stick with the picture and simply add strips. Each strip gets its own width, and each strip gets its own shaded band. The posterior for each strip is its shaded area divided by the total shaded area. The denominator is the same for every strip, because it is simply the total chance of the evidence. Adding more hypotheses adds more strips, but the logic does not change at all.

Finally, imagine that instead of a finite list of hypotheses you have a continuum of them, each with its own tendency to brake early. The strips turn into a curve rather than rectangles, and the shading turns into a curve as well. The posterior is now the area under the new curve divided by the area under the old one. It is the same idea drawn with a smoother edge, and it sits at the heart of how modern statistics handles unknown parameters in a model.

If you track how those curves change as more evidence arrives, something quite beautiful happens. With many observations, the curve concentrates on a narrow region, and the posterior becomes very confident. With only a few observations, it stays broad, and you remain appropriately humble about what you know. I find that beautiful, honestly. The picture captures both the growing confidence and the lingering doubt inside one single object.

So that is the geometry of changing beliefs. You start with a region of possibilities, you carve off the parts that the evidence rules out, and then you rescale whatever survives. The probabilities you end up with are simply the proportions of what remains. Bayes' theorem is nothing more than a rule for keeping track of those proportions as the evidence accumulates.

I hope you'll try this on a belief of your own. Everything we have built here will carry over to the questions that come next, where the hypotheses are no longer drivers but entire models of how the world works.
NARRATION>>>

```json
{
 "format_class": "geometry picture, worked example, contrast case, then generalize",
 "answer_given_upfront": true,
 "hook_type": "premise-claim",
 "first_question_frac": 0.06,
 "first_concrete_object_frac": 0.03,
 "first_new_idea_frac": 0.08,
 "first_notation_frac": 0.36,
 "payoff_frac": 0.35,
 "misconception": "planted-myth-defused",
 "brute_force_first": false,
 "examples_count": 4,
 "example_growth": "one corner -> late braking -> second corner -> rare test",
 "roadmap": "none",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.06,
 "caveat_type": "epistemic",
 "recurring_anchor": "the unit square sliced into strips and shaded bands",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": false,
 "wpm": 176,
 "median_beat_s": 50,
 "beat_sequence": ["hook","toy-world","viewer-turn","definition","derivation","payoff","analogy","derivation","generalize","derivation","caveat","misconception-defuse","generalize","coda"],
 "top5_moves": ["toy-world","visible-repetition","notation-after-concept","minimal-definition-then-refine","honest-caveat"],
 "absent3_moves": ["act-it-out","learner-discovers","inline-quiz"]
}
```

```json
{"verified_trace": {"wpm": "PASS 176.00 (target 169.84-182.96, median 175.95)", "you_rate": "PASS 2.19 (target 1.53-2.23, median 1.93)", "i_rate": "PASS 0.61 (target 0.35-0.89, median 0.7)", "we_rate": "PASS 1.01 (target 0.81-1.53, median 1.11)", "num_rate": "FAIL 4.18 (target 1.83-3.76, median 3.24)", "hedge_rate": "PASS 0.36 (target 0.24-0.48, median 0.37)", "example_rate": "FAIL 0.32 (target 0.13-0.31, median 0.24)", "q_rate": "PASS 0.32 (target 0.17-0.4, median 0.28)", "sent_len": "FAIL 17.24 (target 23.09-25.4, median 24.21)", "switch_sponsor": "PASS detected=False default=OFF", "switch_teaser": "PASS detected=False default=OFF", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (premise-claim vs premise-claim)", "ending_type": "MATCHES default (teaser-next vs teaser-next)", "summary": "6/9 numeric targets pass"}}
```
