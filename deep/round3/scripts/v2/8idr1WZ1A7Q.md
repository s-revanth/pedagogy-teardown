# 3blue1brown: Binomial distributions | Probabilities of probabilities, part 1

- channel: 3blue1brown
- id: 8idr1WZ1A7Q
- title: Binomial distributions | Probabilities of probabilities, part 1
- duration: 754 s (12:34), band over10min
- condition: v2
- recall: none
- rulebook step 0: duration 12.6 min (>=10); series label (part 1); topic is probability, a concept builder; the title names a topic and the answer (about 12 percent) comes at 6:40, not in the first 40 s.
- class chosen: series part 1 concept builder: question hook, enumerate small cases, count, name the shortcut, guess checkpoint, general formula, the next question, teaser to part 2
- exemplars read: deep/compact/fNk_zzaMoSs.txt (Vectors, chapter 1, 9 min: series-chapter pacing and definition build); deep/compact/OkmNXy7er84.txt (Putnam probability, 11 min: counting and reframing with a closing reveal)

## Content skeleton
- Hook: seven heads in ten flips; is the coin fair?
- Three flips: eight sequences listed, then counted by heads: one, three, three, one
- The listing does not scale; the shortcut is n choose k, the number of ways to pick k positions
- Guess checkpoint: exactly seven heads in ten fair flips, one in a hundred, one in ten, or about one in two
- Ten choose seven is 120 of 1024, about twelve percent; five heads is the most likely count at about a quarter
- General form: n choose k, times p to the k, times one minus p to the n minus k; any p, not only fair coins
- Caveat: independence and a fixed probability
- Teaser: part 2 makes the probability itself uncertain

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Question: seven heads in ten flips, is the coin fair? |
| 0:40 | toy-world | Three flips: the coin sequences appear on screen |
| 1:30 | demo-sim | Eight sequences listed, each equally likely if the coin is fair |
| 2:20 | definition | Count the heads: one, three, three, one |
| 3:00 | demo-sim | The counts drawn as bars: a small hill |
| 3:40 | brute-force | Listing does not scale to ten flips; a shortcut is needed |
| 4:20 | definition | n choose k, shorthand for the count just made |
| 5:00 | demo-sim | Three choose one equals three, checked against the list |
| 5:17 | viewer-turn | Guess: exactly seven heads in ten fair flips, one in a hundred, one in ten, or about one in two? |
| 6:00 | derivation | Ten choose seven is 120; divide by 1024 |
| 6:40 | payoff | Answer: about twelve percent; five heads is about a quarter |
| 7:10 | derivation | General form in words, with p as the chance of success |
| 7:50 | generalize | Any p: a loaded die, free throws, a defect rate |
| 8:30 | demo-sim | As n grows, the hill widens and its centre sits near n times p |
| 9:10 | tangent | How surprising must a result be before the belief changes? |
| 9:50 | caveat | Independence and fixed-probability assumptions |
| 10:40 | tangent | Where the line is drawn turns counting into reasoning |
| 11:20 | teaser | Next: the probability itself becomes uncertain |
| 12:00 | coda | Closing line on surprise and assumptions |
| 12:34 | end | Stop |

<<<NARRATION
Flip a coin ten times and you get seven heads. Is the coin fair? Your gut might say no, but gut feelings about random things are notoriously unreliable. Over the next several videos, I want to build up a way to answer questions like this, and the first piece is a distribution that tells you how likely each count of heads is.

Let's start small. Flip a coin three times. Each flip can come out heads or tails, so there are eight possible sequences. Write them all out. Heads, heads, heads. Heads, heads, tails. Heads, tails, heads. And so on, down to tails, tails, tails. Eight sequences, each equally likely if the coin is fair.

Now stop tracking the full sequence and count only the heads in each one. Zero heads: one sequence. One head: three sequences, since the single head can sit in any of three positions. Two heads: three sequences. Three heads: one sequence.

So the counts are one, three, three, one. Out of eight, the chance of zero heads is one in eight, and the chance of exactly one head is three in eight. Draw those as bars and you get a little hill, tallest in the middle. That hill is a distribution.

Listing all the sequences was a fine way to get the counts for three flips, but it does not scale. For ten flips there are over a thousand sequences. We need a shortcut, and the shortcut starts with a single question. For a fixed number of flips, how many sequences have exactly k heads? Each one is a choice of which k of the positions are heads. Mathematicians write that count with a special symbol, read as "n choose k", meaning the number of ways to pick k items out of n.

The symbol is not a new idea. It is shorthand for the thing you just counted. For three flips, "three choose one" is three, and those three sequences are exactly the three ways to pick the one position that gets a head. "Three choose zero" is one, "three choose two" is three, and "three choose three" is one. Those are our counts again: one, three, three, one.

Now let's go to ten flips and ask about exactly seven heads. Before I compute anything, make a guess. If the coin is fair, how likely is exactly seven heads in ten flips? One in a hundred? One in ten? About one in two? Choose one, and then we'll check it.

To check, we count. Ten choose seven is the number of sequences with exactly seven heads, and it works out to 120. The total number of sequences is two to the tenth, which is 1024. So the chance is 120 out of 1024, which is about twelve percent. That is closer to one in eight than to one in two.

So the answer is about twelve percent, and that is not rare. Exactly seven heads is one of the more likely outcomes. The single most likely count for ten fair flips is five heads, and that comes out to about a quarter. A fair coin produces seven heads with an ordinary, modest frequency, which is why one result alone can't settle whether a coin is fair.

Here is the general form, in words. The chance of exactly k successes in n trials, when each trial succeeds with probability p, is "n choose k", times p to the power k, times one minus p to the power n minus k. It counts how many arrangements there are, times how likely each arrangement is. For a fair coin, p is one half, every arrangement has the same chance, and the formula reduces to counting.

Nothing here is special to coins. The same formula works for any probability p. A loaded die that shows a six one time in five. A basketball player who makes seventy percent of free throws. A production line with a small defect rate. The binomial distribution describes the number of successes in a fixed number of independent trials, each with the same chance of success.

The key ingredient is the same in every case: a fixed number of trials, the same chance each time, and no memory of earlier trials. When one of those conditions fails, the formula can still be a useful model, but it is no longer a clean description.

Look at what happens as the number of flips grows. The hill gets wider and spreads out. Its centre sits near n times p, which is five for ten fair flips, and the most likely counts stay close to that centre while the spread grows in a predictable way. That regularity is what lets you say how surprising a result really is.

You can see the same thing in a few numbers. For three flips, the most likely counts are one or two, each with a chance of three in eight. For ten flips, the most likely count is five. For a hundred flips, the most likely count is about fifty, and the typical spread around it is about five. The centre moves with the number of flips, while the spread grows more slowly.

That raises a question that is more about beliefs than counting. How surprising does a result have to be before you change your mind about the coin? Seven heads is about a twelve percent event, and that is not a sure sign of a biased coin. Deciding where to draw the line is the step that turns counting into reasoning.

I want to be honest about the assumptions. The binomial model assumes every flip is independent and has the same probability. Real coins can wear unevenly, and real trials can be correlated. When those assumptions fail, the numbers can mislead you even though the arithmetic is perfect. The math tells you what follows from the assumptions, and the assumptions still have to be checked against the world.

Next time, the probability itself becomes uncertain. Instead of asking how likely seven heads is for a coin of known fairness, we'll ask how likely each fairness is, given the flips. That is the probability of probabilities, and it's a surprisingly deep idea.
NARRATION>>>

```json
{
 "format_class": "series part 1 concept builder: question hook, enumerate small cases, count, name the shortcut, guess checkpoint, general formula, next question, teaser",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.05,
 "first_new_idea_frac": 0.05,
 "first_notation_frac": 0.34,
 "payoff_frac": 0.53,
 "misconception": "none",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "three flips -> ten flips -> any p",
 "roadmap": "none",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.42,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the row of coin-flip sequences, returned to for each example",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 180,
 "median_beat_s": 30,
 "beat_sequence": ["hook","toy-world","brute-force","definition","demo-sim","viewer-turn","derivation","payoff","derivation","generalize","demo-sim","caveat","teaser","coda"],
 "top5_moves": ["hook-question","brute-force-first","notation-after-concept","inline-quiz","visible-repetition"],
 "absent3_moves": ["humor","running-character","rule-list"]
}
```

```json
{"rule_trace": {
"U1": "applied: series part 1 sets the format gate: concept-builder arc; no roadmap, recap or callback; teaser used as the series allows",
"U2": "n/a: title names a topic; the answer (about 12 percent) comes at 6:40, not in the first 40 s",
"U3": "applied: closes on the teaser to part 2; no callback",
"U4": "applied: the row of coin-flip sequences returns in three examples",
"U5": "applied: n choose k introduced at 4:20 after the three-flip count it names; symbol keyed to counted sequences",
"U6": "applied: 180 wpm over-10 target, beats of about 30 s",
"U7": "applied: no roadmap, no vote, no planted misconception",
"U8": "applied: domain caveat on independence and fixed probability at 9:50",
"U9": "applied: guess checkpoint (one in a hundred, one in ten, one in two) at 42 percent of runtime, answered at 6:40",
"U10": "n/a: no history-of-invention ladder",
"U11": "n/a: title names a topic, not an application or trigger",
"C1": "n/a: 12.6 min, above the 10-minute threshold",
"C2": "n/a: no lemma block",
"C3": "n/a: no iterated construction taken to a limit",
"C4": "n/a: no awe-objection-algebra sequence",
"C5": "applied: rising guess ladder of three magnitudes at 42 percent of runtime, answered after the count",
"D1": "applied: no roadmap up front",
"D2": "applied: brute force is an exact listing of eight sequences used as a picture; no slightly wrong numeric method",
"D3": "n/a: no wall; the need is not posed as a design problem",
"D4": "applied: the n choose k symbol comes after the three-flip count, as shorthand for it",
"D5": "applied: teaser only, as part 1 of a series allows; no callback",
"N1": "n/a: over-10-minute video",
"N2": "applied: delivery target 180 wpm, the band median; text cannot verify pace",
"N3": "broken: measured 1.06 per 100 words (N-median 2.05, p25-p75 1.62-2.5), outside the band",
"N4": "broken: measured 0.29 per 100 words (N-median 0.93, p25-p75 0.62-1.34), outside the band",
"N5": "broken: measured 0.68 per 100 words (N-median 1.02, p25-p75 0.71-1.58), outside the band",
"N6": "broken: measured 9.96 per 100 words (N-median 2.49, p25-p75 1.62-3.7), outside the band",
"N7": "broken: measured 0.68 per 100 words (N-median 0.21, p25-p75 0.12-0.3), outside the band",
"N8": "broken: measured 12.6 per 100 words (N-median 24, p25-p75 22-27), outside the band",
"N9": "broken: measured 2.51 per 100 words (N-median 0.33, p25-p75 0.22-0.44), outside the band",
"N10": "broken: measured 0.0 per 100 words (N-median 0.26, p25-p75 0.16-0.34), outside the band",
"B1": "applied: no sponsor read",
"B2": "applied: teaser used because the video is a series part (U3 licence)",
"B3": "applied: no spoken roadmap",
"B4": "applied: no spoken recap"
}}
```
