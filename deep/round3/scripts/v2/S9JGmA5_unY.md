# 3blue1brown: How secure is 256 bit security?

- channel: 3blue1brown
- id: S9JGmA5_unY
- title: How secure is 256 bit security?
- duration: 306 s (5:06), band under10min
- condition: v2
- recall: none
- rulebook step 0: duration under 10 min (5 min); no series label; title is a question; the answer is not in the title or the first 40 s; topic is cryptography, a scale argument.
- class chosen: short scale explainer: question hook, toy key, doubling ladder, one guess checkpoint, the payoff number, the 256-bit comparison, caveats, impact coda; no roadmap, recap, callback or notation
- exemplars read: deep/compact/HEfHFsfGXjs.txt (5 min: question hook, toy setup, escalating numbers, deferred or contrasted answer)

## Content skeleton
- Hook: can someone break a 256-bit lock by simply trying keys?
- Toy key of four bits: sixteen possibilities; each extra bit doubles the work
- Real sizes: a 128-bit key and a trillion guesses per second; the time comes out to about ten to the nineteenth years
- The 256-bit comparison: the count squares, and the time is around four times ten to the fifty-seventh years
- Assumptions: keys are random, the attacker only guesses; a quantum search roughly halves the bit count
- The weak point is almost never the key length: passwords, random number generators, code bugs, stolen copies
- Impact coda: the strongest lock fails when the key is taped to the door

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Question: can someone break a 256-bit lock? |
| 0:20 | toy-world | Four-bit key: sixteen keys in a row on screen |
| 0:45 | demo-sim | Each added bit doubles the row |
| 1:10 | definition | Strength counted as the number of doublings |
| 1:35 | toy-world | A 128-bit key: sizes and the attacker's rate |
| 2:05 | demo-sim | Years counter against a trillion guesses per second |
| 2:30 | viewer-turn | Guess: hundreds of years, or millions? |
| 2:50 | payoff | Answer: about ten to the nineteenth years, far beyond the universe's age |
| 3:15 | generalize | 256-bit: the count squares; about four times ten to the fifty-seventh years |
| 3:45 | caveat | Assumptions: random keys, guessing only; a quantum search halves the bits |
| 4:15 | caveat | The weak point is elsewhere: passwords, code, stolen copies |
| 4:40 | coda | Impact coda: the strongest lock fails when the key is taped to the door |
| 5:06 | end | Stop |

<<<NARRATION
Can someone break a 256-bit lock? Before I answer that, let's think about what the number 256 is actually counting.

Start with a toy version. Imagine a key that is only four bits long. A bit is a single yes or no, a zero or a one. With four bits, you can write sixteen different keys, from zero zero zero zero up to one one one one. A patient person could try all sixteen in a few seconds.

Now add one more bit. The number of possible keys doubles, to thirty-two. Each extra bit doubles the work for the attacker, and that is the whole idea. The strength of a key is measured in how many doublings stand between a guesser and the right answer.

Here's a way to picture it. Imagine a long row of boxes, one for each possible key. Each new bit makes the row twice as long. A four-bit row fits on one screen. A 128-bit row would stretch farther than anything you could draw in this universe, and the 256-bit row would stretch farther still.

So let's look at real sizes. A 128-bit key has about three times ten to the thirty-eighth possible values. That's a number with thirty-nine digits. Suppose the attacker can test a trillion keys every second. That is already a very generous rate. Take a guess at how long it would take to try them all. Hundreds of years? Millions? Keep your number in mind, and I'll show you.

The answer is about ten to the nineteenth years. That is ten billion billion years, which is hundreds of millions of times longer than the universe has existed. No attacker is going to try every 128-bit key by brute force.

Now the 256-bit key. You might think doubling the length doubles the work, but it does not. It squares it. The number of possibilities is two to the 256th, which is the 128-bit count multiplied by itself. Two to the 256th is about one point one times ten to the seventy-seventh. At the same trillion guesses per second, the search would take roughly four times ten to the fifty-seventh years.

Those are brute-force numbers, and they are the reason people say 256-bit security is strong. But they rest on assumptions, and I want to state them plainly. The key has to be truly random. The attacker has to be limited to guessing. And if the attacker has a quantum computer, the picture changes a little.

A quantum method called Grover's algorithm can search an unstructured space in roughly the square root of the number of possibilities. For a 256-bit key, that brings the effective work down to about the level of a 128-bit classical search. That is still an astronomical amount of work, which is why people who plan for the long term choose 256 bits rather than 128.

None of this means a quantum computer is a reason to panic today. It is a reason to plan, because systems take years to migrate. The planning question is whether your data has to stay secret for longer than that migration takes. Grover's algorithm touches symmetric keys like this one. Public-key schemes face a different quantum method, which is a separate story.

Now the second assumption, which matters most in practice. Almost no real break happens by trying every key. Attackers look for weak points around the key. A password that is easy to guess. A random number generator that repeats itself. A bug in the code that uses the key. A copy of the key left on a stolen laptop.

Compare that with a typical human password. A short password drawn from a small set of common words can fall to a dictionary attack in seconds, because the attacker is not trying every key at all. They try the likely ones first. A random 256-bit key has no such shortcut, which is why the key itself is rarely the weak point in a well-built system.

Those are the places where systems actually fail. The length of the key is rarely the thing that gives way. So is 256-bit security secure? Against guessing, yes, by a margin no attacker could ever use. The real question is whether everything around the key is just as careful. The strongest lock in the world does not help if the key is taped to the door.
NARRATION>>>

```json
{
 "format_class": "short scale explainer: question hook, toy key, doubling ladder, guess checkpoint, payoff, 256-bit comparison, caveats, impact coda",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.0,
 "first_concrete_object_frac": 0.07,
 "first_new_idea_frac": 0.07,
 "first_notation_frac": null,
 "payoff_frac": 0.56,
 "misconception": "none",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "four-bit toy -> 128-bit -> 256-bit",
 "roadmap": "none",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.49,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the trillion-guesses-per-second rate, reused three times",
 "sponsor_frac": null,
 "ending_type": "impact-coda",
 "teaser": false,
 "wpm": 173,
 "median_beat_s": 22,
 "beat_sequence": ["hook","toy-world","demo-sim","definition","toy-world","demo-sim","viewer-turn","payoff","generalize","caveat","coda"],
 "top5_moves": ["hook-question","toy-world","special-case-first","visible-repetition","honest-caveat"],
 "absent3_moves": ["roadmap","recap","callback-to-hook"]
}
```

```json
{"rule_trace": {
"U1": "applied: under 10 min (5 min); short scale arc, no roadmap, recap, callback or notation",
"U2": "n/a: title is a question; the answer is not in the title or the first 40 s",
"U3": "applied: impact-coda close; no callback to the hook, no teaser",
"U4": "applied: the trillion-guesses rate returns three times, each pass adding a number",
"U5": "n/a: no symbols; numbers are spelled out and C1 drops notation",
"U6": "applied: 173 wpm under-10 target, beats of about 22 s",
"U7": "applied: no roadmap; no planted misconception",
"U8": "applied: domain caveat on random keys, guessing-only attacker and quantum search",
"U9": "applied: magnitude guess (hundreds of years or millions) at 49 percent of runtime, answered at 2:50",
"U10": "n/a: no history-of-invention ladder",
"U11": "n/a: title names a property, not an application or trigger event",
"C1": "applied: under 10 min; roadmap, recap, callback and notation dropped",
"C2": "n/a: no lemma block",
"C3": "n/a: no iterated construction",
"C4": "n/a: no two-stage payoff with an objection",
"C5": "n/a: a single magnitude guess, not a rising ladder near 40 percent",
"D1": "applied: no roadmap up front",
"D2": "n/a: brute force is the subject itself (trying keys); no slightly wrong numeric method is shown as a default",
"D3": "n/a: no wall",
"D4": "n/a: no symbols",
"D5": "n/a: no callback or teaser to close",
"N1": "applied: 173 wpm under-10 median as the delivery target; text cannot verify pace",
"N2": "n/a: under 10 min",
"N3": "broken: measured 0.8 per 100 words (N-median 2.05, p25-p75 1.62-2.5), outside the band",
"N4": "broken: measured 0.4 per 100 words (N-median 0.93, p25-p75 0.62-1.34), outside the band",
"N5": "broken: measured 0.27 per 100 words (N-median 1.02, p25-p75 0.71-1.58), outside the band",
"N6": "broken: measured 7.73 per 100 words (N-median 2.49, p25-p75 1.62-3.7), outside the band",
"N7": "broken: measured 0.53 per 100 words (N-median 0.21, p25-p75 0.12-0.3), outside the band",
"N8": "broken: measured 11.7 per 100 words (N-median 24, p25-p75 22-27), outside the band",
"N9": "broken: measured 1.6 per 100 words (N-median 0.33, p25-p75 0.22-0.44), outside the band",
"N10": "broken: measured 0.53 per 100 words (N-median 0.26, p25-p75 0.16-0.34), outside the band",
"B1": "applied: no sponsor read",
"B2": "applied: no teaser; not a series video",
"B3": "applied: no spoken roadmap",
"B4": "applied: no spoken recap"
}}
```
