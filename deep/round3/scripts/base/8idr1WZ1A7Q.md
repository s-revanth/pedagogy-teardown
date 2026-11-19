channel: 3blue1brown
id: 8idr1WZ1A7Q
title: Binomial distributions | Probabilities of probabilities, part 1
duration: 754 s (12:34)
condition: base
recall: vague

## Content skeleton
- A coin-flip question: the chance of exactly six heads in ten flips.
- Small case first: all strings of five flips, counting the ones with three heads.
- The binomial coefficient as a count of positions, named after the binomial expansion.
- The binomial formula: count times p to the k times one minus p to the n minus k.
- A slider on the coin's bias p, showing how the histogram shifts and always sums to one.
- Probability as a function of the unknown bias: the same formula, a different variable.
- Teaser toward part two, where the unknown bias gets a distribution of belief.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Question: ten fair flips, chance of exactly six heads? Then what if the coin is biased? |
| 0:55 | roadmap | One line: count strings, write the formula, then let the bias vary. |
| 1:15 | toy-world | Strings of H and T for five flips; thirty-two equally likely strings. |
| 2:30 | brute-force | List the strings with three heads out of five; viewer pauses and counts; the answer is ten. |
| 4:10 | definition | The count is n choose k: the number of ways to choose k positions; the binomial name explained. |
| 5:20 | derivation | Each string has probability p to the k times one minus p to the n minus k; multiply by the count. |
| 7:00 | demo-sim | A slider for p; the bars shift left or right and always sum to one. |
| 8:40 | generalize | Fix the outcome, vary p: the chance of six heads becomes a curve over the bias. |
| 10:10 | misconception-defuse | The curve is the same binomial formula, not an exotic object; only the variable changed. |
| 10:50 | teaser | Part two: treat the unknown bias as something we hold beliefs about. |
| 11:50 | coda | Summary of counting, formula, and the curve over p. Ends at 12:34. |

## Narration
<<<NARRATION
Suppose you flip a fair coin ten times. What is the chance of getting exactly six heads? You might guess it is small, and you would be right, but the exact number has a clean structure, and that structure is the subject today. Along the way we are going to meet a strange-sounding idea, which is a probability of a probability. Let's build up to it slowly.

Start with a short example, just five flips. Each flip is either heads or tails, so a sequence of five flips is a string of five letters, each H or T. There are thirty-two possible strings, since each flip doubles the count. If the coin is fair, every string is equally likely, so the question becomes a counting question. How many strings have the number of heads you care about?

Let's do that count by hand. Suppose you want exactly three heads out of five flips. You can list the strings. Heads, heads, heads, tails, tails. Heads, heads, tails, heads, tails. Heads, tails, heads, heads, tails. And so on. I'd like you to pause here and try it yourself. Write out the strings with three heads in five flips, and count them. You should get ten. If you get a different number, go back and check which positions you forgot.

Ten is right, and the way you found it is the important part. You are choosing which three of the five positions get heads. The other two get tails. Once you think of it that way, you don't need to list anything. You only need to count how many ways there are to choose three positions out of five.

That count has a name. It is written as n choose k, meaning the number of ways to choose k things from n, and it is the binomial coefficient. For five flips and three heads, it is five choose three, which equals ten. The name binomial comes from this same coefficient appearing when you expand a sum of two terms raised to a power, and that connection is why the whole distribution gets its name.

Now let's turn counting into probability. If the coin is fair, each specific string of five flips has probability one half to the fifth, which is one thirty-second. The probability of exactly three heads is the number of favorable strings times the probability of each string. That is ten times one thirty-second, which is about thirty percent. So the most likely outcomes sit near the middle, and the extremes are rare.

Let's write it in general. For n flips, with k heads, and with the chance of heads on each flip equal to p, every specific string with k heads has probability p to the k times one minus p to the n minus k. There are n choose k such strings. So the probability of exactly k heads is n choose k, times p to the k, times one minus p to the n minus k. That is the binomial distribution.

Look at what we just did. The formula came after the strings. The strings came after the counting. The symbols are a summary of things you can already see. If the formula ever feels like it came from nowhere, go back to the strings and check.

Now let's make p adjustable. Imagine a slider from zero to one, controlling the bias of the coin. At p equal to one half, the bars of the histogram are centered on five heads out of ten flips and fall off symmetrically. Drag the slider toward zero, and the bars shift left, because the coin is landing tails more often. Drag toward one, and they shift right. Notice that the bars always add up to one. Whatever p is, some number of heads must occur, so the total probability is conserved.

Here is where the idea of a probability of a probability comes in. Look at the probability of getting exactly six heads out of ten flips, and treat p as the variable. For each value of p, you get a number. As p changes, the number changes too. So the probability of six heads is itself a function of p. It rises to a peak and falls away again. That curve is a probability, but it is a probability as a function of the unknown bias.

This is the step that often feels strange. Probability usually takes an event and gives you a number. Here the event is fixed, six heads out of ten, and the input is the coin's bias. Each bias gives a different chance for the same event. So when you hear probability of a probability, what it means is this: the chance of an observation, viewed as a function of a hidden parameter.

I want to address a common misunderstanding. Some people think this curve is a different kind of thing from ordinary probability, something exotic. It is not. The formula is the same binomial formula. The only change is which quantity you choose to vary. Keep the coin's bias fixed, and you have a distribution over outcomes. Fix the outcome, and you have a curve over biases. Same formula, different question.

That shift from "given the bias, what outcome?" to "given the outcome, what bias?" is the most important move in this subject. It is the bridge from counting coins to learning from data, because in real life we see the outcome and want to infer the hidden parameter. That is where the next part of this series picks up.

Let me say what comes next. In part two, we are going to treat the unknown bias as something we can have beliefs about, a distribution over possible values, instead of a fixed number we are trying to pin down. That leads to a new family of curves, and to the question of how a belief should change after you see flips. Everything we built here, the counting, the formula, and the curve over p, is the foundation for that.

So for now, here is the summary. The number of ways to get k heads is a choose count. The probability of each string is p to the k times one minus p to the n minus k. Multiply them to get the binomial distribution. And when you fix the outcome and vary the bias, the same formula becomes a curve that tells you how plausible each bias is.

Thanks for watching, and I'll see you in part two.
NARRATION>>>

## Slots
```json
{
 "format_class": "coin-flip counting, formula after strings, teaser to part two",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.1,
 "first_notation_frac": 0.33,
 "payoff_frac": 0.56,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "five flips -> ten flips -> unknown coin bias",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.2,
 "caveat_type": "none",
 "recurring_anchor": "the H and T strings, reused in the count and the formula",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 165,
 "median_beat_s": 70,
 "beat_sequence": ["hook","roadmap","toy-world","brute-force","definition","derivation","demo-sim","generalize","misconception-defuse","teaser","coda"],
 "top5_moves": ["hook-question","toy-world","brute-force-first","notation-after-concept","teaser-next"],
 "absent3_moves": ["humor","running-character","failure-shown"]
}
```
