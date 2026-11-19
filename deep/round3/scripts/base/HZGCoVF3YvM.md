channel: 3blue1brown
id: HZGCoVF3YvM
title: Bayes theorem, the geometry of changing beliefs
duration: 911 s (15:11)
condition: base
recall: vague

## Content skeleton
- A diagnostic-test scenario where a positive result is less conclusive than the accuracy suggests, because the condition is rare.
- The base rate (prior) as the hidden input most people drop when they hear "99 percent accurate".
- Counting a concrete population of 10,000 people as a brute-force check before any formula.
- Geometry: a unit square split by prevalence and then by test result; the posterior is the share of the positive area that is true positives.
- Bayes' rule written as a ratio, introduced only after the picture.
- Generalization to a continuous range of possible values, and repeated updates from a second test.
- Callback to the opening person at the end.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Question: a test is 99 percent accurate and you test positive, so how likely are you sick? One person with a positive result on screen. |
| 0:40 | answer-statement | The answer is far below the accuracy; the missing ingredient is how rare the condition is. |
| 1:30 | roadmap | One line: count people, then draw a picture, then write the rule. |
| 2:10 | toy-world | A grid of 10,000 small people, about 100 shaded as sick. |
| 3:40 | brute-force | Test everyone: 99 sick people test positive, about 495 healthy people also do. Count the positives. |
| 5:00 | wall | Counting people gets clumsy and cannot hold a continuous prior. |
| 5:50 | analogy | Turn the population into a unit square: width is sickness, height is the test; areas are proportions of people. |
| 7:10 | derivation | Chance is the sick-and-positive rectangle over the total positive area; Bayes' rule appears as that ratio. |
| 8:40 | demo-sim | Slide prevalence from 1 in 100 to 1 in 10 and then 1 in 1,000; the posterior moves on screen. |
| 10:00 | generalize | Two hypotheses become a curve of possible values, and the same ratio reweights each one. |
| 11:20 | viewer-turn | Pause and guess: a second independent positive test is taken. How far does the belief move? |
| 12:10 | callback | Back to the first person: the second positive result pushes belief toward sick. |
| 13:40 | recap | Prior times likelihood, divided by the total. |
| 14:30 | coda | Evidence moves beliefs, but only from where they started. Ends at 15:11. |

## Narration
<<<NARRATION
Imagine a test for a condition that about one person in a hundred has. The test is pretty good. If you are sick, it catches it 99 percent of the time. If you are healthy, it still flags you about 5 percent of the time. Now you take it, and it comes back positive. How worried should you be?

Most people hear "99 percent accurate" and assume the answer is something close to 99 percent. It is not. The real answer is closer to one in six. That gap is the subject of today, and what fills it is a quantity that is easy to forget: how common the condition was before you ever took the test.

Here is the plan. We will count people, then draw a picture, then write down the rule. Let's make it concrete. Imagine ten thousand people, and suppose they all take the test. Roughly one percent of them, about a hundred people, are actually sick. Those hundred are our main characters. Let's shade them in. The rest, around nine thousand nine hundred, are healthy.

Now run the test on everyone. Of the hundred sick people, the test catches 99, and misses one. That part behaves well. But look at the healthy group. Five percent of nine thousand nine hundred is roughly four hundred and ninety five. Those people are healthy, and the test calls them positive anyway.

So count every positive result. There are 99 sick people who tested positive, and about 495 healthy people who tested positive too. That makes around 594 positive results in total. Out of those 594, only 99 are actually sick. Divide 99 by 594 and you get about one sixth. That is the chance that a positive result means you are sick.

Notice what happened. The test was never wrong about the sick people, and it was only wrong about five percent of the healthy ones. But the healthy group is so large that its false alarms swamp the true alarms. The rarity of the condition did the damage, not the accuracy.

Counting people works, but it becomes clumsy fast. Let's try a different picture. Take a square with side length one. Its width will stand for how sick a person is, so the thin left strip is the sick group and the wide right part is the healthy group. Its height will be the test result. A point in the square is a person, and areas are proportions of the population.

The width gets split at one percent. Now the test cuts each strip horizontally. In the sick strip, ninety-nine percent of the height is positive. In the healthy strip, only five percent of the height is positive.

Now look at the region that is positive. It is made of two pieces. One is a tall thin rectangle on the left, the sick and positive people. The other is a short but very wide rectangle on the right, the healthy and positive people. The wide one is wide because the healthy group is wide, and short because the false positive rate is small. But its area is still big.

The question, once you see it this way, is simple. Given that a person is in the positive region, what fraction of that region sits on the left? The answer is the area of the left rectangle divided by the total area of both. The left rectangle has area 0.01 times 0.99. The right rectangle has area 0.99 times 0.05. Add them, divide, and you get the same one sixth.

Written in symbols, this is Bayes' rule. The chance of being sick given a positive test equals the chance of a positive test given you are sick, times the chance you were sick to begin with, all divided by the chance of a positive test overall. The top is the sick and positive rectangle. The bottom is the sum of both positive rectangles. We did not start with the symbols. We started with the picture, and the symbols name the ratio of areas we already saw.

I want to pause on the word prior, because it is doing the heavy lifting. The prior is what you believed before the test. Here it was one in a hundred. The test does not produce a belief from nothing. It moves the prior. The likelihood is how strongly the evidence points in each direction. Bayes' rule is the instruction for combining those two, and then dividing by the total so the answer is a proper probability.

Here is an experiment you can run in your head. Imagine the same test, but the condition is much more common, say one in ten. Now the sick strip is wide, and the positive region is dominated by sick people. The chance of being sick given a positive result jumps up sharply. Slide the prevalence down to one in a thousand and the picture reverses: the thin sick strip nearly disappears under the wide healthy one, and a positive result is far less decisive. The test is identical in every case. Only the prior changed, and the posterior changed with it.

This is the part that feels strange at first. People tend to focus on the likelihood, the test's accuracy, and ignore the prior. The geometry makes the imbalance obvious. The sick group is a sliver. Any error rate that applies to the big healthy group produces a big pile of false positives, and those can easily outnumber the true positives.

Now let's generalize, because the square was a choice, not a law. Instead of two possibilities, imagine a whole range of them. Maybe the unknown is how biased a coin is, and the bias could be any value from zero to one. You no longer have two strips. You have a curve, a continuous spread of prior belief over all possible biases. The same logic holds. You multiply the prior curve by how well each bias explains what you observed, and then rescale so the total area is one. The new curve is the posterior.

Here is a question to pause on. Suppose the first test is positive, and then you take a second, independent test, and that one is also positive. Before I continue, guess: will the chance of being sick be near ninety-nine percent, or still far from that? Think about what the second test does to the picture you already have.

Let's find out. The posterior after the first test becomes the new prior for the second. Start from the odds: after one positive test, the odds of sick to healthy are one to five. Each positive result multiplies the odds by its likelihood ratio, which is 99 divided by 5, roughly twenty. So after the second positive test the odds are about twenty to five, or roughly four to one. That means a chance of around 80 percent. Far from 99, but a big jump from one in six.

Go back to the first person, the one who tested positive once. After the second positive result, their belief should move dramatically toward sick. This is the payoff of thinking in updates. A single test does not settle things, but two independent tests combined can. Each piece of evidence changes the prior for the next piece.

To tie it together, here is the recipe in plain words. Start with what you believed before. Ask how likely the new evidence would be under each possibility. Multiply those two things for each possibility, and compare the results. Then divide by the total, so that everything adds up to one. Those are the three moves. They are the same three moves whether you are counting people, cutting a square, or sliding a curve.

So the first positive result was never a verdict. It was a reason to move from one in a hundred toward something larger, and the size of the move depended on the test and on the prior together. Accuracy alone never gives you the answer. Accuracy plus the base rate does.

That is what it means to change beliefs with a geometric picture. The rectangles are not decoration. They are an honest accounting of who is in the positive group, and the answer falls out of comparing their areas.
NARRATION>>>

## Slots
```json
{
 "format_class": "counting-then-geometry explainer, answer stated early",
 "answer_given_upfront": true,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.04,
 "first_notation_frac": 0.47,
 "payoff_frac": 0.8,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "10,000 people -> prior curve -> repeated tests",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.75,
 "caveat_type": "epistemic",
 "recurring_anchor": "the first positive-test person, returns at three points",
 "sponsor_frac": null,
 "ending_type": "hook-callback",
 "teaser": false,
 "wpm": 165,
 "median_beat_s": 65,
 "beat_sequence": ["hook","answer-statement","roadmap","toy-world","brute-force","wall","analogy","derivation","demo-sim","generalize","viewer-turn","callback","recap","coda"],
 "top5_moves": ["hook-question","toy-world","brute-force-first","notation-after-concept","callback-to-hook"],
 "absent3_moves": ["running-character","humor","failure-shown"]
}
```
