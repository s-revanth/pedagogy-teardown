# PrimerBlobs: How many people might ever exist, calculated

- channel: PrimerBlobs
- id: r6sa_fWQB_4
- title: How many people might ever exist, calculated
- duration: 591 s (9:51)
- condition: v1
- recall: none

## Content skeleton
- Opens on a question that looks like it needs a population forecast, then promises a firm answer with almost no forecasting.
- Counts the past first: roughly 100 billion humans have been born, with the estimate depending on how far back you count.
- Shows the naive forecast (today's birth rate times a million years) and why it is a forecast in disguise.
- Builds a toy line of every birth in order and asks where a randomly chosen person sits in it.
- Derives a 95 percent range for the total from one person's position, then checks it with simulated worlds.
- Discusses the assumption that you are a typical draw, flips the total to test sensitivity, and ends with a range and a teaser on population growth.

## Beat sheet

| Time | Beat type | What is said or shown |
|---|---|---|
| 0:00 | hook | Question: how many people will ever exist? |
| 0:25 | roadmap | One-line plan: a count of the past plus one assumption, not a forecast. |
| 0:50 | definition | Count people born so far: roughly 100 billion, depending on the estimate and how far back it counts. |
| 1:50 | toy-world | A line of every person ever born, in birth order; pick one position at random. |
| 2:40 | brute-force | Naive forecast: about 130 million births a year for another million years, giving about 130 trillion. |
| 3:30 | demo-sim | Simulated worlds with known totals; sample a random person's position in each. |
| 4:40 | derivation | Position gives a bound: 95 percent range from about 100 billion to about 4 trillion. |
| 5:50 | viewer-turn | Pause: if you are the 100 billionth person, what is the largest total you would claim? Decide. |
| 6:30 | demo-sim | Ten thousand worlds: the true total lands inside the bound about 95 percent of the time. |
| 7:20 | caveat | The bound assumes you are a typical random draw; that assumption is contested. |
| 7:50 | misconception-defuse | The naive forecast is set up and broken: the bound is a range for the total, not a doom prediction. |
| 8:20 | demo-sim | Parameter flip: a total of 200 billion keeps the bound; 10 quadrillion rejects it. |
| 8:50 | generalize | Same reasoning from one sample: wartime estimates of tank production from captured serial numbers. |
| 9:10 | payoff | Final answer: probably between about 100 billion and a few trillion, under the assumption. |
| 9:25 | recap | Three points restated: the past is counted, the position is sampled, the forecast is separate. |
| 9:40 | teaser | Next: how fast a population can grow, and why that decides whether forecasts are possible. |

<<<NARRATION
How many people will ever exist? It sounds like a question that needs a forecast: birth rates, medicine, climate, and whatever happens over the next few centuries. But there is a way to get a surprisingly firm answer with almost no forecasting at all, and it starts with counting the past.

Let's begin with what we know. Roughly how many people have ever been born? Demographers' estimates land near 100 billion. The exact figure depends on how far back you count, and the earliest records are thin, so the number is not precise. But it is solid enough to work with. Call it 100 billion, and count yourself as one of them if you're reading this.

Here is the naive approach, and it's the one most people reach for first. Take the rate of births today, which is about 130 million a year. Assume it continues for another million years. Multiply. You get about 130 trillion people. That's a clean answer, and it is almost certainly wrong, because it rests on a million years of unchanged births. Nobody can defend that. It looks precise because the arithmetic is precise, but the assumption carries the whole result, and the assumption is a forecast.

So let me try a different kind of reasoning. Imagine every human who will ever live, lined up in order of birth. Each one is a block in a very long row. Now pick a block at random. Where are you likely to land? Most of the time you won't be at the very start, and you won't be at the very end. You'll be somewhere in the middle, because the middle holds most of the blocks.

Here is the claim, stated carefully. Suppose you are a typical block. Then your position is not extreme. If your position were in the first 2.5 percent of the whole row, that would be unusual, because only 2.5 percent of random picks land there by chance. So with 95 percent confidence, you are not in the first 2.5 percent. That single fact puts a bound on the total.

Let's write it out. Say you are person number n, and the total is N. Your position is not in the first 2.5 percent, so n is at least 2.5 percent of N. Turn that around, and N is at most 40 times n. With n around 100 billion, the total comes out below about 4 trillion. You are also not in the last 2.5 percent, which means N is at least about n, so it is at least around 103 billion. The 95 percent range runs from about 100 billion to about 4 trillion.

Before you trust that, let's check it. I'll write a simulation in which the total is known. Each world holds some number of people, anywhere from a thousand to a trillion. We pick one person at random, compute the bounds from their position, and then see whether the true total falls inside the range. Run it ten thousand times. In about 95 percent of the worlds, the true total falls inside the bound. The method works, at least in worlds built to match its assumption.

Now here's where I'll commit to a guess. Make the call before you read on. If you were the 100 billionth person born, what is the largest total you would feel safe claiming? Think about the 40 in the formula, and then decide.

Here's the answer. Forty times 100 billion is 4 trillion. Did you get there, or did you guess something bigger, because the naive answer felt more natural? That gap between the two answers is the point of this section. The naive method runs on a guess about the future. The bound runs on a guess about where you sit in the row. Both are guesses, but they fail in different ways.

Let's be honest about what the bound assumes. It assumes that you are a random pick from everyone who will ever live. That is a choice, and a contested one. Some people argue that the present is special, that you happen to be living at a moment when the population is unusually large, and that the random-pick assumption therefore misleads. I'm not claiming the bound is right. I'm claiming it is the argument you get when you take the sampling assumption seriously, and I'd rather show you its edges than hide them.

Here's a test of sensitivity. Suppose the true total is only 200 billion. Then your position of 100 billion is not extreme at all. It sits about halfway along the row, and the bound still includes it. Now suppose the total is 10 quadrillion. Then your position is a tiny fraction of the row, and the bound rejects it. So the method is telling you something about the total, and the total is what decides the verdict. That is the sense in which the argument is a bound rather than a prediction.

The same kind of reasoning has been used in practice. During the Second World War, analysts estimated how many tanks a country was producing from the serial numbers on the few that had been captured. The principle is the same: a sample of one or a few numbers gives you a rough upper estimate for the whole set, and the estimate gets tighter as the sample grows. It's a useful idea, and it's a crude one, and both of those things are true at once.

So what's the answer? If you want one number to carry out of this video, it's this. The total number of people who will ever exist is probably between about 100 billion and a few trillion, if you accept the assumption that you are a typical draw. The naive answer, 130 trillion, requires a million years of unchanged births. That's a forecast, not a count, and a forecast needs its own defense.

Next time we'll go the other way and look at how fast a population can grow. The growth rate is what decides whether a forecast like that is even possible. Before then, try the sim yourself. Change the number of worlds, change the range of totals, and watch how often the bound holds.
NARRATION>>>

```json
{
 "format_class": "thought experiment, bound from one sampled position",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.0,
 "first_concrete_object_frac": 0.19,
 "first_new_idea_frac": 0.19,
 "first_notation_frac": 0.47,
 "payoff_frac": 0.93,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 4,
 "example_growth": "naive forecast, sim check, parameter flip, tank serials",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.59,
 "caveat_type": "epistemic",
 "recurring_anchor": "the numbered row of births and your own position in it",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 30,
 "beat_sequence": ["hook","roadmap","toy-world","brute-force","demo-sim","derivation","viewer-turn","demo-sim","caveat","misconception-defuse","generalize","payoff","recap","teaser"],
 "top5_moves": ["hook-question","brute-force-first","simulation-as-argument","honest-caveat","generalize-to-other-domains"],
 "absent3_moves": ["act-it-out","humor","running-character"]
}
```
