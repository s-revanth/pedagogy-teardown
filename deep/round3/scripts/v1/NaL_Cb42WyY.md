# 3blue1brown: Pi hiding in prime regularities

- channel: 3blue1brown
- id: NaL_Cb42WyY
- title: Pi hiding in prime regularities
- duration: 1783 s (29:43)
- condition: v1
- recall: vague

## Content skeleton

- Hook: two random whole numbers, and the chance they share no factor; why would pi, a circle constant, appear?
- Roadmap: a sieve picture of primes, sampled pairs, a precise definition, a per-prime product, an Euler identity, a caveat about averages.
- A sieve grid where each prime removes a fixed share of the numbers, leaving the primes.
- Sampling random pairs gives a steady fraction near six tenths, which looks promising but is not an explanation.
- Each prime blocks a pair with chance one over p squared; the coprime probability is the product of one minus one over p squared.
- Euler's identity equates that product with the sum of one over n squared, which equals pi squared over six, so the probability is six over pi squared.
- Misconception defused: primes are irregular in detail but regular in averages.
- Generalization to the zeta function, and a caveat that the result describes averages, not individual primes.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Pick two whole numbers at random. What is the chance they share no factor besides one? And why would pi show up? |
| 0:45 | roadmap | Plan: a sieve picture, sampled pairs, a precise definition, a product over primes, an identity, and a caveat about averages. |
| 1:20 | toy-world | A board of whole numbers with multiples crossed out, one prime at a time. The survivors are the primes. |
| 3:00 | brute-force | Sample random pairs and check for a common factor. The coprime fraction settles near six tenths. Promising, but not an explanation. |
| 4:40 | wall | Nothing in the setup mentions circles. The factors are integers, so a constant that measures roundness needs a reason. |
| 6:00 | definition | The coprime probability defined as a limit over growing ranges, so we can ask about its structure factor by factor. |
| 7:20 | derivation | For one prime, a pair is blocked with chance one over p squared. Coprime means no prime blocks, so the probability is a product over primes of one minus one over p squared. |
| 10:30 | demo-sim | Multiply the factors one prime at a time. The running product drops from three quarters, to two thirds, and settles near six tenths. |
| 12:30 | definition | The sum of one over n squared over all whole numbers, named. Euler's identity links it to the product over primes. |
| 15:00 | derivation | Each whole number factors uniquely into primes, so expanding the product of geometric series over primes gives back the sum. Both equal pi squared over six. |
| 18:00 | misconception-defuse | Primes look too random to hold any constant. Individual primes are irregular; the averages are structured. |
| 19:00 | demo-sim | A grid of pairs, shaded when they share a factor. The unshaded share approaches six over pi squared as the grid grows. |
| 21:00 | generalize | The Euler product underlies the zeta function, which packs the same prime information into one sum with a parameter. |
| 23:30 | caveat | The result is about averages over all pairs. It gives density, not positions. The rigorous limit arguments are the next layer. |
| 24:30 | viewer-turn | Pause. Guess whether the coprime probability is a simple fraction like one half, or something involving pi. |
| 25:15 | recap | The coprime probability is a product over primes of one minus one over p squared. Euler turns it into six over pi squared. |
| 27:00 | callback | Back to the opening. The primes are the atoms of multiplication, and the sum over squares is the bridge. Teaser: the zeta function and its zeros. Ends at 29:43. |

## Narration

<<<NARRATION
Here's a question that seems to mix two unrelated worlds. Pick two whole numbers at random. What's the chance they have no common factor other than one? And why on earth would the answer involve pi, the constant that lives in circles?

Let's find out, and along the way we'll see what primes are doing. Primes look random. They don't follow a simple rule, and a pattern that seems to hold for the small ones can fall apart later. That makes them a good place to look for the regularities that do exist, especially the ones that hold on average.

Here's the plan. We'll start with a grid of numbers and watch how multiples cover it, then sample random pairs to get an estimate. We'll see why a circle constant should be hard to expect, then define the quantity precisely. Next we'll compute it using the primes one at a time, which gives a product. Then we'll match that product to a famous sum over squares, and pi appears. At the end there's a caveat: this result is about averages, and it doesn't tell you where any single prime sits.

Start with the grid. Write the whole numbers across a board, and cross out multiples. Cross out every multiple of two. Then every multiple of three. Then five. The numbers that survive are the primes, the ones with no factor other than one and themselves. Notice that the crossing-out is a rule applied to each prime in turn. Each prime removes a fixed share of the numbers, and the survivors are what's left.

Now the question about pairs. Pick two numbers at random and ask whether they share a factor. If they're both even, they share two. If they share a factor of three, they share three. The question is whether they share any factor at all. The pairs that share none are called coprime, and the question is how often that happens.

Try it by sampling. Take random pairs of whole numbers, say from one to a thousand, and check each pair for a common factor. Keep a tally. The fraction of coprime pairs settles near a value around six tenths. You can repeat it with bigger ranges, and the number stays steady. That's the brute-force estimate, and it's promising. But a sample is not an explanation. I want to know why the number isn't just close to six tenths, but equal to something exact.

Here's the wall. Nothing in the setup mentions circles. The pairs are counting objects, the factors are integers, and there's no obvious route to a constant that measures roundness. If pi shows up, we need a reason.

So let's name the quantity precisely. The chance that two random whole numbers are coprime is a limit. Take all pairs up to some size, count the coprime ones, and divide by the total. As the size grows, that fraction converges. Call the limit p. The point of this definition is that we can now ask questions about its structure, one factor at a time.

Now the key idea: handle the primes one at a time. For a single prime p, what's the chance that a pair of random numbers are both divisible by p? Each number is divisible by p with chance one over p, and the two are independent, so the chance that both are divisible by p is one over p squared. So the chance that the pair is not blocked by p is one minus one over p squared.

Here's the step that makes it work. Two numbers are coprime exactly when no prime divides both. So the chance that they are coprime is the product, over all primes, of the chance that the prime doesn't divide both. Multiply the factors together: one minus one over four, times one minus one over nine, times one minus one over twenty-five, and so on through the primes. That product is the probability we want.

Let's check the product on screen. Start with the factor for two, which is three quarters. Multiply by the factor for three, which is eight ninths. The product is two thirds. Multiply by the factor for five, which is twenty-four twenty-fifths, and it drops a bit more. Keep going, and the running product settles toward a number near six tenths. Each new prime nudges it a little, and the nudges shrink fast, because the primes are larger and their squares larger still. You can watch the product converge.

Now the reveal. A product over primes like this one has a famous partner: the sum of one over n squared, taken over all whole numbers. Euler showed that this sum equals pi squared over six. And there's a deep identity linking the sum over all whole numbers to the product over primes. Every whole number factors uniquely into primes, so expanding the product of geometric series over primes gives back the sum over all whole numbers. The two expressions are the same object, seen from two sides.

Let's make that identity visible. Expand the factor for two as a geometric series: one, plus one over four, plus one over sixteen, and so on. Multiply by the expansion for three, and the terms line up with numbers whose only prime factors are two and three. Keep multiplying over all the primes, and every whole number appears exactly once, with its factorization. That's the Euler product. The left side is the sum of one over n squared over all whole numbers. The right side is the product over primes of one over one minus one over p squared. Both sides equal pi squared over six.

Put it together. The probability that two random whole numbers are coprime is the reciprocal of that same product, which is six over pi squared. Six over pi squared is about six tenths, which is exactly the number our sampling suggested. So the pi is not a coincidence. It's the sum of reciprocal squares, reappearing through the primes.

Now a common belief to address. People often think primes are too random to have any constant at all. Individual primes are irregular, and you can't predict where the next one will land. But the averages are structured, and this result is an example: a precise number emerges from the apparent chaos. The primes are random in detail and regular in aggregate.

Let's test the idea with a picture. Count the coprime pairs in a grid, shading each pair that shares a factor. The shaded share fills in as the grid grows, and the unshaded share approaches six over pi squared. The picture makes the limit visible, even though no single pair tells you anything.

Now generalize. The same reasoning runs through much of number theory. The Euler product is the bridge for the zeta function, which takes the sum over whole numbers, with a parameter in the exponent, and encodes the same prime information in a single expression. That bridge is one of the most useful pieces of the whole subject, and it's where the deeper questions about how primes spread out begin.

Now the caveat. This result is about averages over all pairs. It says nothing precise about any given pair or any given prime. The gaps between primes stay irregular, and the average tells you the density, not the position. The full story of how primes spread out needs much more analytic machinery, and the argument I've sketched uses the product and the sum without the careful limit arguments. Treat this as the core idea, and the rigorous version as the next layer.

Pause here if you want. Before the reveal, guess whether the coprime probability should be a simple fraction, like one half, or something involving pi. Then compare it with the answer we just found. Most people expect a fraction, and the pi is the surprise.

Let's recap. The probability of coprime pairs is a product over primes of one minus one over p squared. The Euler identity turns that product into a sum over squares. The sum equals pi squared over six. So the probability is six over pi squared.

Back to the opening. Two unrelated worlds met at the Euler product. Primes are the atoms of multiplication, and the sum over squares is the bridge between them, with pi as the place where the two meet.

And if the Euler product is a bridge, the zeta function is the place where its full structure lives, including the zeros that control how the primes fluctuate around their averages. That's where we go next.
NARRATION>>>

## Slots

```json
{
 "format_class": "question-to-identity tour, sieve and sampling, then product and Euler identity",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.0,
 "first_concrete_object_frac": 0.0,
 "first_new_idea_frac": 0.04,
 "first_notation_frac": 0.2,
 "payoff_frac": 0.85,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 4,
 "example_growth": "sieve grid -> sampled pairs -> product check",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.82,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the coprime-pair probability, restated at each stage",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 100,
 "beat_sequence": ["hook","roadmap","toy-world","brute-force","wall","definition","derivation","demo-sim","misconception-defuse","generalize","caveat","viewer-turn","recap","callback"],
 "top5_moves": ["hook-question","misconception-first","brute-force-first","simulation-as-argument","visible-repetition"],
 "absent3_moves": ["second-person-role","running-character","rule-list"]
}
```
