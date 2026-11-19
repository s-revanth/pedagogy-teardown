# 3blue1brown: Binomial distributions | Probabilities of probabilities, part 1

- channel: 3blue1brown
- id: 8idr1WZ1A7Q
- title: Binomial distributions | Probabilities of probabilities, part 1
- duration: 754 s (12:34)
- condition: v1
- recall: vague

## Content skeleton

- Hook: flip ten fair coins and get seven heads. Is that surprising?
- Roadmap: count sequences rather than list them, look for the pattern in the counts, turn it into a bell, then a twist about the coin itself.
- Three flips laid out in full: eight equally likely sequences, and the counting shortcut for each number of heads.
- Choosing which flips are heads gives the count; the binomial coefficient names it, and rows of the counts form Pascal's triangle.
- Bar charts for growing numbers of flips show the bell shape.
- Worked answer for seven heads in ten flips, with a pause to guess first; generalization to polls and repeated yes-or-no trials.
- Caveat about independent identical flips, then a teaser: the coin's own chance of heads is unknown and must be learned.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Flip a fair coin ten times and get seven heads. Is that surprising? Your gut has an opinion. Let's check. |
| 0:50 | roadmap | Plan: count sequences instead of listing them, find the pattern, make the bell, then a twist for next time. |
| 1:20 | toy-world | Three flips: eight equally likely sequences in a small grid. Exactly two heads gives three sequences, so three eighths. |
| 2:40 | brute-force | Ten flips give 1024 sequences. Listing them is not a good use of an afternoon. The wall: we need counting. |
| 3:30 | derivation | Seven heads means choosing seven of the ten positions. Ten choose seven counts them. Check on the three-flip case. |
| 5:00 | definition | The binomial coefficient named. Rows of counts are Pascal's triangle, since each entry is the sum of the two above. |
| 6:10 | demo-sim | Bar charts of head counts for ten flips, then more flips. The bars rise to a peak and the bell takes shape. |
| 7:40 | viewer-turn | Pause. Guess whether the chance of exactly seven heads is about one percent, ten percent or fifty percent. |
| 8:00 | derivation | 120 sequences over 1024 gives about twelve percent. A quick check: each row adds to two to the n, so the chances total one. |
| 9:00 | generalize | Any repeated yes-or-no trial with the same chance: polls, quality control, free throws. Same counts, same bell. |
| 9:50 | caveat | The formula needs independent, identical flips. Real coins wear and people influence each other. Check the assumptions. |
| 11:20 | recap | Count by choosing positions, read the table as Pascal's triangle, divide by the total, and the counts form a bell. |
| 11:20 | teaser | Next part: the coin's chance of heads is itself unknown and has to be learned from flips. Probabilities of probabilities. Ends at 12:34. |

## Narration

<<<NARRATION
Flip a fair coin ten times. You get seven heads. Is that surprising? Your gut might say no, because ten flips is a small sample and seven isn't far from five. But your gut also tends to read a streak as the coin getting lucky. Let's find out what the numbers actually say, because this question has a clean answer, and it leads somewhere more interesting.

Here's the plan. We'll start with three flips so that we can see every possibility. We'll find that counting is the right tool, not listing. Then we'll name the counting, see a pattern emerge in a table, and turn that table into a picture. Then we'll compute the probability of seven heads in ten flips. And at the end, there's a twist about the coin itself that we'll save for the next part.

Start small. Flip a coin three times. There are eight possible sequences, and each one is equally likely: heads heads heads, heads heads tails, and so on. Lay them out in a grid and you can see everything at once. Each sequence has a probability of one eighth. Now ask how many of them have exactly two heads. There are three: heads heads tails, heads tails heads, and tails heads heads. So the chance of exactly two heads is three eighths.

Now try ten flips. There are two to the ten, which is 1024, sequences. You could write them all out, but that's not a good use of anyone's afternoon. What we need is a way to count the sequences with seven heads without listing them. This is the wall, and it's the reason we need counting.

Here's the counting idea. A sequence with exactly seven heads is determined by choosing which seven of the ten flips are heads. So the number of such sequences equals the number of ways to choose seven positions out of ten. We write that as ten choose seven. The number is a whole number, and we can compute it by multiplying out the choices and dividing by the redundant orderings.

Check it on the three-flip example. Three choose two is three, which matches the three sequences we listed. Three choose zero is one, the sequence of all tails. Three choose three is one, the all-heads sequence. The formula works in every case we can check by hand, so we can trust it for the bigger ones.

Now the table. Write down the counts for every number of heads, for a given number of flips. For three flips, the counts are one, three, three, one. For four flips, one, four, six, four, one. These are the rows of Pascal's triangle, and they appear here for a reason: each entry is the sum of the two entries above it, because a new flip either adds a head or adds a tail. The triangle is not an arbitrary pattern. It's a counting table.

So the binomial coefficient, ten choose k, is the entry in row ten of that triangle, at position k. Naming it gives us a compact way to write the count. Once we have it, the probability of exactly k heads in n flips is the count divided by two to the n, since every sequence has the same chance.

Now let's look at the picture. For ten flips, plot the number of sequences for each number of heads, from zero to ten. The bars rise to a peak at five and fall off symmetrically on both sides. As a quick check, add up all the bars and you get two to the ten, so the probabilities add to one. Change the number of flips and the same shape stretches, widening and getting smoother. For a large number of flips, the bars trace out a bell. You can watch the bell form on screen as the number of flips grows.

Now the answer. The chance of exactly seven heads in ten flips is ten choose seven, which is one hundred twenty, divided by two to the ten, which is 1024. That comes out to about twelve percent. So seven heads is not common, but it's also not a freak event. Plenty of fair samples land there, and more often than a rough guess would suggest.

Pause here if you want. Before reading on, try to guess whether the chance of exactly seven heads is closer to one percent, ten percent, or fifty percent. Then compare with the answer. Most people guess too low. The bell is wider than the gut expects, and the middle has more room in it than the tails.

Now let's generalize. This counting works for any situation where you repeat a yes-or-no trial, with the same chance each time, and each trial is independent of the others. Polls are like this. A survey asks people one question, and each answer is a yes or a no. Quality checks on a factory line, and free throws in basketball, look like repeated coin flips with a chance attached to each shot. The same counts and the same bell describe all of them, as long as the assumptions hold.

And here's the caveat. The formula depends on the flips being independent and identical. Real coins can wear unevenly, and people in a survey can influence each other. Free throws depend on how the shooter feels that day. When those assumptions break, the counts are still a useful starting point, but the bell can stretch or shift. The model is a sharp tool, and you should check whether its assumptions fit the problem in front of you.

Let's recap. Count sequences by choosing positions. Those counts form Pascal's triangle. Divide by the total to get a probability. Plot them across many flips and they form a bell.

Now a teaser for the next part. So far we've assumed we know the chance of heads for the coin. We set it to one half and computed everything from there. But in practice we often don't know that chance, and we have to learn it from the flips themselves. What's the chance that the coin's chance is a particular value? That's a probability of a probability, and it's where we'll go next.
NARRATION>>>

## Slots

```json
{
 "format_class": "counting-to-picture tour, question-driven, then a teaser",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.0,
 "first_concrete_object_frac": 0.11,
 "first_new_idea_frac": 0.28,
 "first_notation_frac": 0.4,
 "payoff_frac": 0.64,
 "misconception": "none",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "three flips -> ten flips -> growing n",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.61,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the row of head counts from the ten-flip bar chart",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 50,
 "beat_sequence": ["hook","roadmap","toy-world","brute-force","derivation","definition","demo-sim","viewer-turn","generalize","caveat","recap","teaser"],
 "top5_moves": ["special-case-first","brute-force-first","notation-after-concept","visible-repetition","teaser-next"],
 "absent3_moves": ["humor","running-character","failure-shown"]
}
```
