# 3blue1brown: Bayes theorem, the geometry of changing beliefs

- channel: 3blue1brown
- id: HZGCoVF3YvM
- title: Bayes theorem, the geometry of changing beliefs
- duration: 911 s (15:11)
- condition: v1
- recall: vague

## Content skeleton

- Hook: a positive result on a test for a rare condition, and the question of how worried to be.
- Roadmap: try the quick answer, draw the population, write the picture as a formula, flag the model's simplifications.
- The quick answer treats test accuracy as the probability of being sick. The gap between those two is the lesson.
- A square population picture with the sick strip and the test results shaded; the positive column turns out to be half sick.
- Conditional probability as a ratio of areas, then Bayes' rule as a rearrangement, with prior, likelihood and posterior named after the pieces.
- A base-rate slider and a second independent test that reuses the same rescaling; generalization to any hypothesis and evidence.
- Caveat about equal accuracy and independence, then a callback to the opening number and a teaser for beliefs as a continuous range.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | A test for a condition one person in a hundred has is 99 percent accurate. You test positive. How worried should you be? |
| 0:40 | roadmap | Plan: try the quick answer, draw the population, write it as a formula, flag where the model is simplified. |
| 1:10 | brute-force | Pause to guess. Then the quick answer: accuracy equals the chance of being sick. Labelled on screen as the trap. |
| 2:20 | toy-world | A square of ten thousand people. The sick strip is one percent of the area. Positives shaded on both parts of the square. |
| 3:50 | wall | The positive column is mostly healthy people in count. The quick number cannot be the answer. |
| 4:40 | derivation | Zoom into the positive column. Sick share is the sick part over the whole column: 99 sick, 99 healthy, so one half. |
| 6:20 | definition | Name the ratio as conditional probability. Rearrange into Bayes' rule. Prior, likelihood and posterior pointed at in the picture. |
| 9:00 | demo-sim | Base-rate slider: one in ten gives a high belief, one in ten thousand gives about one percent. Same test each time. |
| 10:10 | derivation | Second independent positive test: the positive column becomes the new population. Sick share near 99 percent. |
| 11:30 | generalize | Any hypothesis and any evidence: a region of possibilities, evidence cuts it, belief is the share left. |
| 12:20 | caveat | Assumes equal accuracy for everyone and independent tests. Real numbers have to come from data. |
| 13:10 | recap | Prior times likelihood over the total. The four pieces in one picture. |
| 13:50 | callback | Back to the opening 99 percent. The gap to the answer is the base rate doing its job. |
| 14:30 | teaser | Next: beliefs as a continuous range, a curve that shifts with each flip. Ends at 15:11. |

## Narration

<<<NARRATION
Imagine a test for a condition that about one person in a hundred has. The test is quite good. If you have the condition, it comes back positive 99 times out of 100. If you don't, it still comes back positive once in every hundred healthy people. Now you take it, and it says positive. How worried should you be?

Take a moment with that. Most people's gut says something like 99 percent, or at least very high. The test really is accurate, after all. So where would the doubt even come from?

Here's the plan. First, we'll try the quick answer and see where it goes wrong. Then we'll draw a picture of the population that makes the right answer visible. After that, we'll write the picture as a formula. And at the end, I'll point out where this simple model is cheating a little, because every model is.

Let's start with the quick answer. The test is 99 percent accurate, so the chance I'm sick is 99 percent. That line of thinking treats the accuracy as if it were the probability of being sick, given a positive result. Those are not the same thing. The gap between them is the whole lesson.

So let's build the picture. Imagine ten thousand people, with the area of a big square standing for all of them. The sick people are a narrow strip, one percent of the area, along one edge. Now the test. Among the sick, 99 percent come back positive, so we shade almost all of that strip. Among the healthy, one percent come back positive, which is a thin sliver across the rest of the square. Let's shade that too, in a different color.

Look at what's shaded in total. The positive results are the sick strip, mostly, plus that thin sliver across the healthy region. And the healthy region is huge, so even a sliver of one percent holds about as many people as the sick strip does.

This is the wall. A positive result is a mixture. If you pick a random person from the positive group, you are not picking from the sick region. You are picking from all the positives, and in this setup, half of them are healthy.

So we need a question with the right population. The question is not what fraction of sick people test positive. That's the accuracy, and it divides by the sick people. The question we actually want is what fraction of the positive people are sick. That divides by the positives. Two different denominators, and two very different answers.

Let's zoom into the positive region and ignore everything that tested negative. What's left is a column of positive people, some sick, some healthy. The probability that you're sick, given a positive result, is the area of the sick part of that column, divided by the area of the whole column.

Now do the arithmetic on the picture. Ten thousand people, one hundred of them sick. Of those hundred, ninety-nine test positive. Of the nine thousand nine hundred healthy people, one percent, which is ninety-nine, test positive. So the positive column holds ninety-nine sick people and ninety-nine healthy people. The sick share of the column is one half.

One half, not ninety-nine percent. That is the surprise. The test is accurate, and yet, starting from a rare condition, a positive result leaves you at a coin flip.

Now let's write this as a formula, and notice that nothing new has happened. We wrote a probability as a ratio of areas, with the column as the thing we condition on. In symbols, the probability of A given B is the probability of A and B together, divided by the probability of B. That's conditional probability, and it's the same ratio we just drew.

Bayes' rule is what you get when you rearrange it. The probability that you are sick, given a positive result, equals the probability of a positive result given sickness, times the probability of sickness before the test, divided by the overall chance of a positive result. Each factor points at a region on the picture. The first is the test's accuracy. The second is the base rate. The denominator is the size of the positive column.

And there are names for these pieces. The base rate is the prior, what you believed before any evidence. The accuracy is the likelihood, how well the evidence fits each possibility. The answer is the posterior, what you believe after. The formula is just the picture, compressed.

Here's a slider to play with the base rate. Drag it up, so one person in ten is sick, and the answer jumps to something like 92 percent. Drag it down, to one in ten thousand, and that same accurate test leaves you barely worried, around one percent. Same test, same accuracy, completely different belief. The prior matters as much as the evidence.

Now let's test the picture on something harder. Suppose you take a second test, independent of the first, and it also comes back positive. What should you believe now?

The clean move is to treat your current belief as the new prior. After the first test, you were at one half. So the population for the second test is the positive column from the first. Zoom into that column and run the same ratio again. The sick share jumps to about 99 percent. The second test shrinks the column down to the people who are very likely sick.

Notice what happened. We didn't learn a new rule. We applied the same rescaling twice. Each new piece of evidence cuts the picture down to the region it supports, and then asks what fraction of the survivors are the thing you care about.

This works for any hypothesis and any evidence, not just sickness and tests. A hypothesis could be a theory, a suspect, a claim about the world. The evidence could be a fossil, a message, a measurement. There's a region of possibilities. Evidence cuts it. The belief is the share of what's left.

Now the honest caveat. This whole calculation assumes the test's accuracy is the same for everyone, and that the two tests are independent. In real medicine, neither assumption is guaranteed. A test can behave differently in different groups, and two tests on the same person can share the same kind of error. The picture is still the right way to think, but the numbers you plug in have to come from data, not from assumptions.

Let's close the loop. The number at the start, ninety-nine percent, was the accuracy. The answer, one half, was the posterior. Once you've seen the column, the distance between those numbers stops feeling like a trick. It's just the base rate, doing its job.

In the next part, we'll ask what happens when beliefs aren't just yes or no, but a whole range, like the unknown rate of a coin. That turns the picture into a curve, and the update into a shape that shifts with every flip.
NARRATION>>>

## Slots

```json
{
 "format_class": "geometric proof tour, quick answer first, then picture and formula",
 "answer_given_upfront": false,
 "hook_type": "scenario-you",
 "first_question_frac": 0.0,
 "first_concrete_object_frac": 0.15,
 "first_new_idea_frac": 0.31,
 "first_notation_frac": 0.42,
 "payoff_frac": 0.35,
 "misconception": "staged-early",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "one test -> two tests -> general evidence",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.08,
 "caveat_type": "approximation",
 "recurring_anchor": "the square population with the sick strip shaded, reused four times",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 50,
 "beat_sequence": ["hook","roadmap","brute-force","toy-world","wall","derivation","definition","demo-sim","generalize","caveat","recap","callback","teaser"],
 "top5_moves": ["special-case-first","toy-world","brute-force-first","notation-after-concept","callback-to-hook"],
 "absent3_moves": ["running-character","humor","rule-list"]
}
```
