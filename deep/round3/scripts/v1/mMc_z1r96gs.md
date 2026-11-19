# PrimerBlobs: How life grows exponentially

- channel: PrimerBlobs
- id: mMc_z1r96gs
- title: How life grows exponentially
- duration: 528 s (8:48)
- condition: v1
- recall: none

## Content skeleton
- Opens with one blob that splits on every tick, and asks how big the pile gets after a day.
- Counts the first few doublings by hand, then runs the dish for ten steps to show the crowding.
- A prediction pause at twenty steps; the reveal shows the gap between the guess and the doubling.
- Names the exponential as the count after t steps, then generalizes to a growth rate r and a doubling time.
- Log scale turns the curve into a straight line; examples from money and rumors.
- Admits the dish has unlimited food and blobs never die, and teases the next video on the food limit.

## Beat sheet

| Time | Beat type | What is said or shown |
|---|---|---|
| 0:00 | hook | Question: one blob splits every tick; how many after a day? |
| 0:20 | roadmap | Count by hand, run longer, then find the single number that sets the growth. |
| 0:45 | toy-world | A dish with one blob and unlimited food; every blob splits on each tick. |
| 1:20 | brute-force | Counting by hand: one, two, four, eight, sixteen; each row is double the last. |
| 2:00 | demo-sim | Run ten steps: 1,024 blobs, and the dish is visibly crowded. |
| 2:50 | viewer-turn | Pause: guess the count after twenty steps. |
| 3:20 | demo-sim | Reveal at twenty steps: 1,048,576 blobs. |
| 3:50 | misconception-defuse | The linear intuition, a fixed number added per step, is set up and then broken. |
| 4:30 | analogy | Compound interest and spreading rumors: each grows by a fixed fraction of its current size. |
| 5:10 | derivation | Count after t steps is the start times two to the power t; a rate r multiplies by one plus r. |
| 6:10 | demo-sim | Plot the logarithm of the count: the same data becomes a straight line. |
| 6:50 | generalize | The doubling time depends only on the rate, not on the size, in money, ideas and populations. |
| 7:20 | caveat | Food is unlimited and blobs never die; real populations do neither, so the curve must bend later. |
| 7:50 | payoff | Three ideas: fixed-fraction growth is exponential; doubling time depends only on rate; linear intuition misleads. |
| 8:20 | teaser | Next: a ceiling on the dish, and what happens when the food runs out. |

<<<NARRATION
Imagine a single blob in a dish. Every tick of the clock, it splits in two. So after one tick there are two blobs, after two there are four, and after three there are eight. How many are there after a day? Make your guess before you keep reading.

Here's what I want to do in this video. We'll count the blobs by hand for a few steps, then let the simulation run for longer, and then find the one number that describes how fast the pile grows. Once we have that number, we can predict the pile without counting every blob in it.

Let's set up the dish. It starts with one blob and an unlimited supply of food. Each tick, every blob splits. That's the entire rule. Nothing else changes, and nothing dies.

Let's count by hand first, because the first few steps are the most useful. After zero steps, one blob. After one step, two. After two steps, four. After three, eight. After four, sixteen. Each row is double the one before it. Nothing about this is hard, and that is what makes it deceptive. The doubling looks like a simple pattern that is easy to extend in your head, and most people extend it wrongly.

Watch the simulation for ten steps. There are one thousand twenty-four blobs. In ten steps the pile grew by a factor of a thousand, and the dish is already crowded enough that the blobs have started to pile up on the screen.

Now the prediction. Pause here and guess how many blobs there will be after twenty steps. Write a number down. If you have a feeling for doubling, you may be close. If your gut says the pile will be roughly twice the size it is at ten steps, or a few hundred thousand, that's worth testing.

Here's the run. After twenty steps there are one million forty-eight thousand five hundred seventy-six blobs. Look at the gap between that and a guess of a few hundred thousand. If you guessed that way, you were treating growth as if each step added a fixed number of blobs. That's the intuition the simulation is built to break. Every step adds the current pile again, so the amount added keeps growing.

This is worth stating plainly, because the intuition is strong. People often picture growth as steady: a fixed number added per step. That's linear growth. The blob pile is not linear. At step one it adds one blob. At step ten it adds five hundred twelve. At step twenty it adds about half a million. The same rule gives a different increment at every step, because the increment depends on how big the pile already is.

Let's make that precise. If we call the starting count N-zero, and the number of steps t, then the count after t steps is N-zero times two to the power t. That's the first symbol in this video, and I didn't introduce it until the pile had been counted. You've already seen what it summarizes: the table of doublings, and the run that confirmed it.

Now a different angle that makes the growth easier to see. A straight-line graph of the count against time bends upward so sharply that the early steps look flat, and the later steps look like a wall. Plot the logarithm of the count instead, and the same data becomes a straight line. A straight line on a log scale is the signature of exponential growth. Its slope tells you the rate, and here the line is steep, because each step doubles the pile.

It helps to state the rate in a more general way. Suppose each blob, in each step, produces r new blobs on average. Then the pile is multiplied by one plus r at each step. A rate of one means doubling. A rate of a tenth means the pile grows ten percent per step. The bigger the rate, the faster the pile grows, and the time it takes to double is the same at any size. That's the important part. The doubling time depends only on the rate.

The same pattern shows up outside the dish. A bank account earning interest compounds the same way. A rumor passed on by each listener to a few new listeners spreads the same way at first. Any quantity that grows by a fixed fraction of its current size grows exponentially. So whenever someone tells you something grows at a fixed percentage per year, the first number to ask for is the doubling time.

Now I want to be honest about something. The dish has unlimited food, and the blobs never die. Real populations do neither. If the food runs out, splitting slows down, and the curve has to bend over. The exponential picture is correct for the early steps, while food is plentiful, and it is wrong for the later steps. Whether that matters depends on what you're trying to predict.

I'm going to leave the food limit for the next video. For this one, the claim is narrow. While a population has room to grow, its size doubles at a constant rate, and that doubling time is the quantity that matters most.

Here's a quick check you can apply to any growth claim. Take the count at one moment, and the count one doubling time later. If the second is twice the first, the growth is exponential at that stage. Many curves look fast without being exponential at all, so this check is worth running before you trust a claim about speed.

So let me compress the whole video into three ideas. A fixed fraction of growth gives an exponential curve. The doubling time depends only on the rate and not on the size. And the early intuition of linear growth will mislead you every time, unless you count.

Next time, we'll put a ceiling on the dish and see what happens to the exponential when the food runs out. Before then, try the table yourself. Start with one blob, double it ten times, and see whether your number matches the simulation.
NARRATION>>>

```json
{
 "format_class": "build the dish, count by hand, then name the rate",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.0,
 "first_concrete_object_frac": 0.0,
 "first_new_idea_frac": 0.09,
 "first_notation_frac": 0.59,
 "payoff_frac": 0.89,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 4,
 "example_growth": "one blob, two to the ten, twenty, money and rumors",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.32,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the dish and its single splitting blob",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 30,
 "beat_sequence": ["hook","roadmap","toy-world","brute-force","demo-sim","viewer-turn","misconception-defuse","analogy","derivation","demo-sim","generalize","caveat","payoff","teaser"],
 "top5_moves": ["toy-world","brute-force-first","simulation-as-argument","notation-after-concept","generalize-to-other-domains"],
 "absent3_moves": ["humor","story","running-character"]
}
```
