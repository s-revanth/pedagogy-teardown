# Header
- channel: 3blue1brown
- id: 8idr1WZ1A7Q
- title: Binomial distributions | Probabilities of probabilities, part 1
- duration: 754 s
- condition: v3
- recall: vague (the topic is recognised; the script is written from the v3 rules and general subject knowledge, not from the video)
- exemplars read: deep/corpus/compact/ZA4JkHKZM50.txt, deep/corpus/compact/Kas0tIxDvrg.txt

## Content skeleton
- Claim up front: the number of heads in repeated flips follows an exact, computable pattern.
- Toy world: ten flips of a coin with heads probability p; count the outcomes with seven heads.
- Counting: n choose k arrangements, read off Pascal's triangle; 120 arrangements for ten flips and seven heads.
- Two numbers: fair coin gives about 11.7 percent; a 70 percent coin gives about 26.7 percent.
- Shape: mean n p, variance n p (1 minus p), a bell-like shape for large n.
- Flip the question: observing k heads as evidence about p, the seed of probabilities of probabilities.
- Caveat: the model assumes independent flips with one fixed p.
- Coda: the binomial as an accounting of paths.

## Beat sheet (about 2200 spoken words across 754 s)
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Premise: the count of heads follows an exact pattern |
| 0:30 | definition | Coin with heads probability p; n flips; what exactly k heads means |
| 1:20 | toy-world | Ten flips and seven heads; the sequences that qualify |
| 2:20 | derivation | Counting arrangements: n choose k |
| 3:10 | demo-sim | Pascal's triangle row for ten flips |
| 4:00 | derivation | Fair coin: 120 over 1024, about 11.7 percent |
| 4:40 | viewer-turn | Pause and guess which coin makes seven heads more likely |
| 5:10 | derivation | A 70 percent coin: about 26.7 percent |
| 6:00 | payoff | The comparison: the biased coin wins for this count |
| 6:30 | generalize | Mean n p and variance n p (1 minus p) |
| 7:10 | generalize | Shape of the distribution as n grows |
| 8:00 | analogy | Flipping the question: the count as evidence about p |
| 9:30 | caveat | Independence and a single fixed p are assumptions |
| 10:20 | generalize | Yes-or-no trials everywhere: surveys, defects, clinical outcomes |
| 11:10 | coda | The binomial as an accounting of paths |

<<<NARRATION
If you flip a fair coin ten times, you will almost never get exactly five heads, and yet the count of heads follows a precise and beautiful pattern. That pattern is the binomial distribution, and it is one of the most useful tools in all of probability. Over the next several minutes we will see where its formula comes from, what it says about different coins, and why it leads to a much deeper question about the probabilities themselves.

Let's set up the situation carefully. Imagine a coin that lands heads with some probability p, which might be one half for a fair coin but could be anything between zero and one. You flip it n times, and each flip is independent of the others. The question we ask is how likely it is that you get exactly k heads. Pinning down the words matters here, because the answer depends on exactly which outcomes we count.

Take a concrete case. Suppose you flip the coin ten times and want exactly seven heads. Many different sequences of heads and tails would produce that count. One sequence is seven heads followed by three tails. Another is three tails first and then seven heads. Every sequence with seven heads and three tails qualifies, and each one has the same probability, because the flips are independent and identical.

So the probability splits into two pieces. The first piece is the probability of one particular sequence with seven heads and three tails, which is p to the seventh times one minus p to the third. The second piece is how many such sequences there are. Multiplying the two gives the probability of exactly seven heads. You can see that the structure is simple, but the counting part deserves real attention, because it is where most people get stuck.

How many sequences have seven heads among ten flips? You are choosing which seven of the ten positions get heads, and the order of choosing does not matter. That number is written as ten choose seven, and it equals ten factorial divided by seven factorial times three factorial. If you compute it, you get 120. So there are 120 distinct sequences, and each carries the same weight.

I would encourage you to test this counting idea on a smaller case before trusting it. Take three flips and two heads. The sequences are heads heads tails, heads tails heads, and tails heads heads, which makes three. The coefficient three choose two gives three as well, and the pattern holds. Once you have checked a few small cases by listing them out, the general formula will feel much less like an external rule and much more like something you could have discovered yourself.

This counting problem has a beautiful geometric home. Arrange the binomial coefficients in rows, with each entry the sum of the two above it, and you get Pascal's triangle. The row for ten flips is one, ten, forty-five, one hundred twenty, two hundred ten, two hundred fifty-two, and then the mirror image. The entry for seven heads sits in that row, and you can read off the count of 120 directly, without any factorials at all.

Now let's put numbers on it. Suppose the coin is fair, so p equals one half. Each sequence of ten flips has probability one over two to the tenth, which is one over 1024. Multiply by the 120 favorable sequences and you get 120 over 1024, which is 11.7 percent. So seven heads from a fair coin is not especially rare, but it is also far from the most likely outcome.

Before reading on, pause and guess. Which is more likely, seven heads from a fair coin, or seven heads from a coin that lands heads seventy percent of the time? Many people guess the fair coin, because it seems more natural. Keep your guess in mind, because the calculation will tell you whether your intuition was right.

Let's compute the biased case. With p equal to seven tenths, each specific sequence with seven heads and three tails has probability seven tenths to the seventh, times three tenths to the third. That product is 0.00222. Multiply by the same 120 sequences, and you get 0.267, or 26.7 percent. So the biased coin makes seven heads considerably more likely, which may have surprised you.

The comparison teaches something important. The count of arrangements is the same in both cases, but the weight of each arrangement changes with p. When p moves toward the value that matches the observed outcome, the probability of that outcome rises. That is why the choice of p matters so much, and it is the first hint that p itself might be something we need to infer from data.

I want to point out a subtle feature here. The biased coin does not win because it is more interesting, but because the observed outcome is closer to what it predicts. Many people reverse this reasoning and assume that the outcome must reflect the coin they expected. Probabilities do not work that way. They tell you how likely a result is given a hypothesis, and that is a different question from how likely a hypothesis is given a result.

The distribution also has a clear center and spread. The mean number of heads in n flips is n times p, so for ten flips with a fair coin the mean is five. The variance is n times p times one minus p, which for the fair coin gives two and a half, and the standard deviation is 1.58. Those two numbers summarize the whole distribution in a compact way, and they are worth remembering as you read on.

As the number of flips grows, the shape of the distribution settles into the familiar bell curve. For ten flips the bars are still lumpy, but for a hundred flips they begin to look smooth and symmetric around the mean. This is a reflection of the central limit theorem, which says that sums of independent variables tend toward a normal shape. You can see the transformation happen by plotting the distribution for increasing n, and I recommend doing that yourself.

The most striking thing about the bell curve is how little the details matter. Whether the coin is fair or biased, the count of heads eventually looks normal after enough flips, once you shift and scale appropriately. I find that surprising, because the early shapes look so different from one another. The convergence is gradual, but it is reliable, and it is one reason the normal distribution appears everywhere.

Now comes the turn that gives this subject its name. So far we have treated p as known and asked about the counts. But in real life we usually observe the counts and want to learn about p. If you flip a coin ten times and get seven heads, what does that tell you about p? The formula still applies, but now we read it differently, as a function of p with the observed count held fixed. That function is the likelihood, and it is the seed of probabilities of probabilities.

Here is the idea in plain terms. Suppose you have no strong prior opinion about the coin. The observed data then favors some values of p over others, and the binomial formula tells you exactly how strongly. Values near seven tenths gain support, while values near zero or one lose it. This is a remarkable shift in viewpoint, because the same expression that predicted counts now measures how plausible each underlying probability is.

Let me illustrate with a quick thought experiment. Suppose you watch someone flip a coin three times and see three heads. Would you bet heavily that the coin is biased toward heads? Most people hesitate, and the hesitation is wise, because three flips carry little information. Yet the same logic is at work. The likelihood of three heads grows as p approaches one, but the data are weak, and the formula tells you that the evidence is modest. The strength of an inference depends on how many flips you have, not only on the pattern you see.

I want to be careful about the assumptions, since they matter a great deal. The binomial model assumes that each flip is independent and that the probability p stays the same from flip to flip. Real coins can wobble, real people can change their behavior, and real experiments can drift over time. When those assumptions fail, the formula can give confident answers that are simply wrong, so you should always ask whether the model fits the situation.

I think one of the most common mistakes is to treat the independence assumption as automatic. Consider a bag of coins where you pick one at random and then flip it many times. The flips are no longer independent once you do not know which coin you picked, because each flip carries information about that coin. Ignoring this structure can make an interval look far narrower than it really is, and that is a serious error in practice.

The same structure appears far beyond coins. Surveys ask yes or no questions, manufacturing lines check whether each item is defective, and clinical trials count how many patients respond to a treatment. Each of these can be modeled as a series of independent trials with a common probability, and the binomial distribution then describes the count. Learning to recognize that structure is one of the most useful skills you can build in probability.

I think this is a natural place to start for anyone new to the subject. Let me give one more example from everyday life. Suppose a quality inspector checks twenty items from a batch and finds three defective. The binomial model says each item is defective independently with some probability p, and the count of defects follows the familiar formula. From that single count, the inspector can begin to ask whether the batch meets a standard, and you can see how the same arithmetic runs the whole process.

At its heart, the binomial coefficient is an accounting of paths. Each path through a sequence of flips is a record of heads and tails, and the coefficient counts how many of those records share the same total. Once you see that, the formula stops looking like an arbitrary recipe and starts looking like a natural tally. That shift in perspective is the real lesson of this part.

We should also notice what we did not need. We did not need calculus, we did not need to simulate thousands of flips, and we did not need to guess the answer from pictures. The whole structure came from two ideas, independence and counting. Together they produce a complete description of the count, which is a reminder that good models often rest on very few assumptions. When we add more assumptions, we should be just as explicit about them, because each one is a potential point of failure.

In the questions that come after this, we will take the step we have been circling. We will treat p as the unknown, put a probability distribution over the possible values of p, and then ask how observing data reshapes that distribution. The binomial formula will provide the update rule, and the whole idea of probabilities of probabilities will come into focus. For now, make sure that you can count arrangements, compute a single probability, and explain why the answer changes with p.
NARRATION>>>

```json
{
 "format_class": "counting toy, Pascal row, two-coin comparison, flip-the-question seed",
 "answer_given_upfront": false,
 "hook_type": "premise-claim",
 "first_question_frac": 0.20,
 "first_concrete_object_frac": 0.03,
 "first_new_idea_frac": 0.08,
 "first_notation_frac": 0.14,
 "payoff_frac": 0.44,
 "misconception": "none",
 "brute_force_first": false,
 "examples_count": 3,
 "example_growth": "ten flips -> fair coin -> seventy percent coin",
 "roadmap": "none",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.58,
 "caveat_type": "epistemic",
 "recurring_anchor": "the ten-flip, seven-heads count",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": false,
 "wpm": 176,
 "median_beat_s": 40,
 "beat_sequence": ["hook","definition","toy-world","derivation","demo-sim","derivation","viewer-turn","derivation","payoff","generalize","analogy","caveat","generalize","coda"],
 "top5_moves": ["toy-world","demo-sim","visible-repetition","notation-after-concept","generalize-to-other-domains"],
 "absent3_moves": ["act-it-out","story","failure-shown"]
}
```

```json
{"verified_trace": {"wpm": "PASS 176.00 (target 169.84-182.96, median 175.95)", "you_rate": "PASS 2.13 (target 1.53-2.2, median 1.81)", "i_rate": "PASS 0.47 (target 0.35-0.89, median 0.71)", "we_rate": "PASS 1.04 (target 0.81-1.58, median 1.26)", "num_rate": "FAIL 6.24 (target 1.83-3.76, median 2.98)", "hedge_rate": "PASS 0.42 (target 0.24-0.48, median 0.36)", "example_rate": "FAIL 0.31 (target 0.13-0.31, median 0.24)", "q_rate": "PASS 0.21 (target 0.17-0.4, median 0.28)", "sent_len": "FAIL 15.88 (target 23.09-25.29, median 24.21)", "switch_sponsor": "PASS detected=False default=OFF", "switch_teaser": "PASS detected=False default=OFF", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (premise-claim vs premise-claim)", "ending_type": "MATCHES default (teaser-next vs teaser-next)", "summary": "6/9 numeric targets pass"}}
```
