# Vsauce: How Much Is A Bird in The Hand Worth? (hup_8uDXJx8)

- channel: Vsauce
- id: hup_8uDXJx8
- title: How Much Is A Bird in The Hand Worth?
- duration: 355 s (5:55)
- condition: base
- recall: vague

## Content skeleton

- Opens on the old proverb about a bird in the hand versus two in the bush, and asks how to put a number on it.
- Turns the saying into a decision with two options: one certain bird, or two birds that may or may not be caught.
- Models each bush bird as caught with probability p, so the expected count is two times p.
- Break-even at p equal to one half; below that the hand wins, above it the bush wins.
- Adds time: a bird later is worth less because it can be used or invested now, so the bush value is discounted.
- Generalises the same logic to investing and interest rates: a payoff far away is worth less than the same payoff today.
- Caveats: the model ignores risk, needs and the chance the hand bird gets away too; a hungry person values the sure bird more.
- Closes by returning to the proverb with a number attached.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Quote the proverb; ask how much a bird in the hand is actually worth |
| 0:25 | definition | Treat the saying as a bet: one sure bird against two birds that might be caught |
| 0:50 | toy-world | Set up the choice with simple rules: one bird now, two in the bush, each caught with chance p |
| 1:30 | derivation | Expected number of bush birds is two times p; compare it to the one sure bird |
| 2:20 | demo-sim | Table of p values 0.2, 0.5 and 0.8 showing the bush value rising and the hand winning or losing |
| 3:10 | derivation | Break-even at p equal to one half; the hand wins below it and the bush wins above it |
| 3:50 | generalize | Time: a bird later is discounted by the rate it could earn; the bush value shrinks with waiting |
| 4:30 | caveat | Model ignores risk and needs; a hungry person values the certain bird more |
| 5:10 | callback | Return to the proverb and attach a number to it |
| 5:40 | coda | Close on the idea that the sure thing is a price, and the bush is a bet |

## Narration

<<<NARRATION
You've probably heard the saying that a bird in the hand is worth two in the bush. It sounds like folk wisdom, the sort of thing a grandparent says over breakfast. But it's also a claim you can test. How much is a bird in the hand actually worth? Let's put numbers on it and see when the saying holds up.

Think of the saying as a bet. On one side, you have a sure thing. One bird is in your hand, and you can keep it. On the other side, there are two birds in the bush. They might fly off, or you might catch them, and you don't know in advance. So the question is which choice is better, and that depends on how likely it is that you'll catch the birds in the bush.

Let's set the rules simply. You have one bird now, and its value is one. Ignore everything else for the moment. There are two birds in the bush. Each one has some chance p of being caught, and the chances are independent. If p is zero, the bush is worthless. If p is one, you're guaranteed two birds. Everything in between is the interesting part.

Now the calculation. The expected number of birds from the bush is the sum of the chances of catching each one. Each bird contributes p, so the total is two times p. That's the expected value of the bush, written as a single expression: two p. Compare it to the bird in your hand, which is worth exactly one. The saying is saying that the bush is worth less than two birds, which is true in general, but the real comparison is between two p and one.

Let's check it with some numbers. Suppose p is 0.2, meaning you have a one in five chance of catching each bush bird. Then the bush is worth 0.4, which is much less than the sure bird. Hold the bird in your hand, obviously. Now suppose p is 0.5, a coin flip for each bird. The bush is worth exactly one. The two options tie. And if p is 0.8, which means you're very good at catching birds, the bush is worth 1.6. That's more than the bird in your hand, so the bush wins.

This gives us the break-even point. The bush and the hand are equal when two p equals one, which means p equals one half. Below a fifty-fifty chance per bird, the bird in the hand wins. Above it, the bush wins. So the proverb is only a good rule if you're pretty sure you'll catch the bush birds, and not sure at all if you're not.

There's a second effect that the proverb ignores, and it's time. A bird in the hand is available now. A bird in the bush might take a long time to catch, and the longer you wait, the less that future bird is worth to you. Economists handle this with discounting. The idea is simple. A payoff in the future is worth less than the same payoff today, because you could have used the money or the bird in the meantime, and earned something from it.

Let's put a rate on it. Suppose the rate you could earn is ten per cent a year. Then a bird that arrives one year from now is worth about ninety-one per cent of a bird today. Divide by 1.1 once. If it arrives in three years, you divide by 1.1 three times, and the value drops to about seventy-five per cent. Apply that to the bush. With p equal to 0.8, the bush is worth 1.6 if you could catch the birds immediately. Wait one year, and it's about 1.45. Wait three years, and it's about 1.2. Wait five years, and it's roughly 1.0, which is the same as the bird in your hand. So a bush that's far away has to be much more likely to pay off before it's worth taking.

This same logic runs through much more than birds. Investing is a version of it. When you decide between money now and money later, the discount rate is the price of waiting. Loans and mortgages are the same story from the other side. A payoff that's certain and immediate can be worth more than a larger payoff that's uncertain and far away, and the math tells you exactly where the trade-off sits.

Now a caveat, because the model leaves things out. It ignores risk. Some people hate the chance of coming away with nothing, even if the expected value is higher. It ignores needs, too. If you're hungry tonight, a sure bird in the hand is worth much more than the expected value suggests, because you can't survive on expected birds. And the model assumes the bird you're holding will stay with you. In real life, the bird in your hand can escape as well. So the numbers are a guide, not a rule that applies in every case.

Let's go back to the proverb now that we've done the work. A bird in the hand is worth one bird. Two birds in the bush are worth two times the chance of catching each one, reduced by how long you have to wait. If the catch chance is high and the wait is short, the bush can beat the hand. If it's low or far away, the hand wins easily. So the saying is right, sometimes, and the reason is a bet on probability and time.

That's the real lesson. The sure thing is a price you pay for certainty, and the bush is a bet you make on yourself. Which one is worth more depends on how good you are at catching birds, and how long you're willing to wait for them.
NARRATION>>>

## Slots

```json
{
 "format_class": "proverb-to-expected-value derivation",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.07,
 "first_notation_frac": 0.25,
 "payoff_frac": 0.84,
 "misconception": "none",
 "brute_force_first": false,
 "examples_count": 4,
 "example_growth": "p 0.2 -> p 0.5 -> p 0.8 -> discounted wait",
 "roadmap": "none",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.02,
 "caveat_type": "approximation",
 "recurring_anchor": "the one sure bird, compared to the bush value at every step",
 "sponsor_frac": null,
 "ending_type": "hook-callback",
 "teaser": false,
 "wpm": 170,
 "median_beat_s": 30,
 "beat_sequence": ["hook", "definition", "toy-world", "derivation", "demo-sim", "generalize", "caveat", "callback", "coda"],
 "top5_moves": ["hook-question", "toy-world", "build-and-verify", "generalize-to-other-domains", "honest-caveat"],
 "absent3_moves": ["brute-force-first", "story", "running-character"]
}
```
