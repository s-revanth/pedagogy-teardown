# 3blue1brown: Pi hiding in prime regularities

- channel: 3blue1brown
- id: NaL_Cb42WyY
- title: Pi hiding in prime regularities
- duration: 1783 s (29:43), band over10min
- condition: v2
- recall: none
- rulebook step 0: duration 29.7 min (>=10); no series label; topic is number theory; the title states a thesis (pi in the primes), so U2 applies.
- class chosen: thesis-first number-theory explainer: thesis and exception stated early, a grid picture, the sieve, the guess ladder at about 45 percent, Euler's product, the density caveat, generalisation, phrase-mirror close
- exemplars read: deep/holdout/compact/d-o3eB9sfls.txt (Basel, 17 min; read in full: the pi-and-zeta link and the geometric build); deep/compact/r6sGWTCMz2k.txt (Fourier series, DE4; read through about 9 KB, the opening and first derivation only)
- note: the video's real content is not known to me; the skeleton uses general facts (coprime density 6 over pi squared, Euler's product, 1 over zeta of three), which I have checked by hand

## Content skeleton
- Thesis: two random whole numbers share no common factor with probability 6 over pi squared, about 61 percent
- Exception stated early: a long-run density, so small grids wobble around it
- Grid of number pairs; shade the coprime pairs; the pattern is structured, not random
- Sieve: each prime p removes the share of pairs both divisible by p, which is 1 over p squared
- Product over primes of one minus one over p squared gives the coprime fraction
- Guess ladder (one tenth, one third, one half); the answer is about 39 percent for sharing a factor
- Euler's identity: the sum of one over n squared equals the product over primes; pi enters through that sum
- Generalisation: three numbers give 1 over zeta of three, about 83 percent; exponents set the constants

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Claim: two random whole numbers share no factor with probability 6 over pi squared |
| 0:40 | answer-statement | Thesis stated: about 61 percent coprime |
| 1:10 | caveat | Exception stated early: a long-run density, small grids wobble |
| 1:15 | toy-world | Grid of number pairs, one number along each edge |
| 2:00 | definition | What sharing a factor means: one prime in both numbers |
| 2:45 | demo-sim | Shade the coprime pairs; the pattern has structure |
| 3:30 | derivation | Prime two removes a quarter of the pairs; prime three removes a ninth |
| 4:50 | demo-sim | Sieve: each prime removes one over p squared of what remains |
| 6:00 | derivation | Product over primes of one minus one over p squared |
| 7:00 | viewer-turn | Guess: sharing a factor about one tenth, one third, or one half? |
| 8:00 | payoff | Answer: about 39 percent share a factor; about 61 percent do not |
| 9:20 | derivation | Euler: the sum of one over n squared equals the product over primes |
| 11:00 | derivation | Expanding the product gives the sum over all whole numbers |
| 12:40 | caveat | Density limit in full: small boxes wobble; large grids settle |
| 14:00 | generalize | Three numbers: one over zeta of three, about 83 percent |
| 15:40 | generalize | The exponent sets the constant; pi belongs to the squares |
| 17:00 | demo-sim | Sieved grid with each prime's share removed; the circle arrives through arithmetic |
| 18:20 | tangent | Why the result feels like magic: a grid, a sieve, and pi |
| 20:00 | tangent | Other constants from other exponents of the same family of sums |
| 22:00 | caveat | Second caveat: the primes do not think about circles |
| 24:00 | generalize | Where the same method turns up in other sums |
| 26:00 | tangent | Sanity check: fractions over growing boxes approach the limit |
| 28:00 | coda | Phrase mirror: where pi hides |
| 29:00 | coda | Closing line: point at the grid and the sieve |
| 29:43 | end | Stop |

<<<NARRATION
Here is a claim that sounds like it belongs to geometry. Pick two whole numbers at random. The chance that they share no common factor greater than one is six divided by pi squared, which is about sixty-one percent. The circle number is hiding inside a question about how primes divide numbers.

There's a caveat I'll come back to, so let me flag it now. This is a long-run fraction. It describes what happens over a large range of numbers, and small examples will wobble around it. I'll show you why it settles down, but keep that in mind.

Let's unpack the question. Two whole numbers share a factor when some prime divides both of them. The numbers six and four share the factor two, because both are even. So sharing a factor is really about one prime showing up in both numbers at once. The question is how often that happens.

Quick test of your intuition: take the pair four and six. They share the factor two. Take the pair three and seven. They share nothing. Most pairs you try will look random, and that is exactly why the picture helps. It shows the structure that the random-looking pairs hide.

Here's a picture that makes it visible. Draw a grid. Each cell is a pair of whole numbers, with one along one edge and the other along the other edge. Shade the cells where the two numbers share no factor other than one. Those are the coprime pairs. Then look at the pattern. It is not random at all. It has structure, and the structure is controlled by primes.

Start with the prime two. For a random pair, both numbers are even in one quarter of the cases, since each is even with probability one half. Those pairs share a factor, so we remove them from the grid. A quarter of the cells are gone, and three quarters remain. Next, the prime three. Both numbers are divisible by three in one ninth of the pairs. Remove those. Then five, which removes one twenty-fifth of the pairs.

So each prime removes a fraction of the remaining pairs equal to one over the square of that prime. What survives after all the primes have sieved the grid is the fraction of coprime pairs. Every prime contributes a factor of one minus one over its square. Multiply those factors over all the primes, and you get the probability.

Here is the shorthand for that product. We write it as a product over all primes p of one minus one over p squared. It is the one formula in this video, and notice where it came from. It is the grid, with one prime at a time removing its own share of cells. The symbol is compact notation for the sieve you can see on the screen.

Before I reveal the number, make a guess. Pick two whole numbers at random. What fraction of the time do they share some factor greater than one? About one tenth? About one third? About one half? Pick one.

The answer is about thirty-nine percent. Subtract that from one, and you get the coprime fraction of about sixty-one percent. So a random pair shares a factor about thirty-nine percent of the time, and the chance it doesn't is six over pi squared. Your guess sits on the ladder, and the true value lies between the middle choice and the top one, which is exactly the kind of result that makes this worth exploring.

Now, why does pi show up? The classic connection is Euler's sum. If you add up one over n squared over all whole numbers, you get pi squared over six. That sum has a second description. It equals the product over all primes of one over one minus one over p squared. The two descriptions are the same object, written two ways.

Let's see why. Expand the product over primes, and you get a sum over all whole numbers. Each whole number is a product of primes in a unique way, and the expansion picks out exactly one term per number. So the product over primes and the sum over integers are the same thing. That is the heart of Euler's observation, and it is why a question about primes returns an answer about circles.

Now the caveat in full. Six over pi squared is the long-run fraction of pairs in a large box. It tells you what happens as the box grows. It does not tell you that any specific pair is coprime, and small boxes will wobble around the limit. In a grid of size ten, the fraction will not match sixty-one percent exactly. Only as the grid grows does it settle. Think of it as a limit, not a property of any one example.

The same idea generalizes. Choose three whole numbers at random, and the chance that they share no common factor greater than one is one over zeta of three, about eighty-three percent. The product trick works with cubes in place of squares. The exponent controls the answer, and each exponent gives a different constant from the same family of sums. Pi belongs to the squares. Other constants belong to other exponents.

So where is pi hiding? In the primes' sieve. Each prime knocks out its share of the grid, and the cumulative effect is a clean value that looks like geometry. The primes are not thinking about circles. They are doing arithmetic, and the circle appears through Euler's sum anyway.

That is the surprising part, and it is why this result feels like a magic trick the first time you see it. A grid of number pairs, a sieve, and a product seem to have nothing to do with a circle. Then the answer arrives with pi squared in the denominator, as if the primes had been keeping a secret about the circle all along.

So the next time someone asks where pi hides, don't point at a circle. Point at the grid of numbers, and at the primes sieving it, one at a time.
NARRATION>>>

```json
{
 "format_class": "thesis-first number-theory explainer: thesis and exception early, grid picture, sieve, guess ladder, Euler product, density caveat, generalisation, phrase-mirror close",
 "answer_given_upfront": true,
 "hook_type": "answer-stated",
 "first_question_frac": 0.03,
 "first_concrete_object_frac": 0.04,
 "first_new_idea_frac": 0.05,
 "first_notation_frac": 0.12,
 "payoff_frac": 0.45,
 "misconception": "none",
 "brute_force_first": false,
 "examples_count": 4,
 "example_growth": "grid -> primes two, three, five -> three-number tuples",
 "roadmap": "none",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.39,
 "caveat_type": "approximation",
 "recurring_anchor": "the grid of number pairs, redrawn after each prime",
 "sponsor_frac": null,
 "ending_type": "phrase-mirror",
 "teaser": false,
 "wpm": 180,
 "median_beat_s": 60,
 "beat_sequence": ["hook","answer-statement","caveat","toy-world","demo-sim","derivation","viewer-turn","payoff","derivation","caveat","generalize","tangent","coda"],
 "top5_moves": ["special-case-first","visible-repetition","notation-after-concept","simulation-as-argument","generalize-to-other-domains"],
 "absent3_moves": ["brute-force-first","humor","rule-list"]
}
```

```json
{"rule_trace": {
"U1": "n/a: 29.7 min, no series label, not first-person; math topic",
"U2": "applied: the title and the first 40 s state the thesis (six over pi squared); the exception follows within 20 s at 1:10; the concrete grid arrives by 1:15; brute-force counting, wall and staged misconception are skipped",
"U3": "applied: closes on a phrase mirror of the title ('hiding'); no callback, no teaser",
"U4": "applied: the shaded grid is redrawn after each prime and returns four times",
"U5": "applied: the product symbol comes only after the sieve picture (about 4:50); each prime is tied to its removed cells",
"U6": "broken: beat rows average about 60 s, above the 15-30 s guidance; table condensed for a 30-minute runtime; pace held at the 180 wpm target",
"U7": "applied: no roadmap, vote or commit prompt in the hook; no planted misconception",
"U8": "applied: approximation caveat (long-run density, small grids wobble) stated at 1:10 and again at 12:40",
"U9": "applied: guess ladder at 7:00 (39 percent of runtime), answered at 8:00",
"U10": "n/a: no history-of-invention ladder",
"U11": "n/a: title names a thesis, not an application or trigger event",
"C1": "n/a: 29.7 min, above the 10-minute threshold",
"C2": "applied: the claim (six over pi squared) is followed by the sieve justification within about 100 s (1:15-3:30 and 3:30-6:00 as the grid is built)",
"C3": "n/a: no iterated construction taken to a limit",
"C4": "n/a: no awe-objection-algebra sequence",
"C5": "applied: rising guess ladder (one tenth, one third, one half) with the true value near 40 percent",
"D1": "applied: no roadmap; the caveat is a one-line exception early and the full caveat comes mid-video",
"D2": "applied: no brute-force box counts; the sieve is the route",
"D3": "n/a: no wall",
"D4": "applied: the product symbol follows the picture as shorthand for the sieve",
"D5": "n/a: no callback or teaser needed",
"N1": "n/a: over-10-minute video",
"N2": "applied: delivery target 180 wpm, the band median; text cannot verify pace",
"N3": "broken: measured 1.27 per 100 words (N-median 2.05, p25-p75 1.62-2.5), outside the band",
"N4": "broken: measured 0.39 per 100 words (N-median 0.93, p25-p75 0.62-1.34), outside the band",
"N5": "broken: measured 0.39 per 100 words (N-median 1.02, p25-p75 0.71-1.58), outside the band",
"N6": "broken: measured 6.91 per 100 words (N-median 2.49, p25-p75 1.62-3.7), outside the band",
"N7": "broken: measured 0.58 per 100 words (N-median 0.21, p25-p75 0.12-0.3), outside the band",
"N8": "broken: measured 11.5 per 100 words (N-median 24, p25-p75 22-27), outside the band",
"N9": "broken: measured 1.66 per 100 words (N-median 0.33, p25-p75 0.22-0.44), outside the band",
"N10": "broken: measured 0.0 per 100 words (N-median 0.26, p25-p75 0.16-0.34), outside the band",
"B1": "applied: no sponsor read",
"B2": "applied: no teaser; not a series video",
"B3": "applied: no spoken roadmap in the first 12 percent",
"B4": "applied: no spoken recap in the last 20 percent"
}}
```
