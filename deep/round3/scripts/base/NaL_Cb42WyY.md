channel: 3blue1brown
id: NaL_Cb42WyY
title: Pi hiding in prime regularities
duration: 1783 s (29:43)
condition: base
recall: vague

## Content skeleton
- Opening question: why would pi, a circle number, show up when counting primes?
- Answer stated early: the chance that two random whole numbers are coprime is six over pi squared.
- A grid of integer pairs and a brute-force count of coprime pairs in a 10 by 10 grid (63 of 100).
- Sieve reasoning: a prime p divides both numbers with chance one over p squared, so the survival chance is a product over primes.
- Euler's product: the same product equals the sum of one over n squared, which is pi squared over six.
- Misconception cleared: primes look irregular one by one, but their collective statistics are regular.
- Wall: the prime count follows x over log x only approximately, with wiggles; zeta zeros control them.
- Generalization to other prime-pattern questions, and a recap with an honest caveat.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Question on screen: why would a circle number appear in a count of primes? |
| 0:50 | answer-statement | Two random whole numbers are coprime with chance six over pi squared. |
| 1:40 | toy-world | A grid of integer pairs; a pair fails if a shared prime divides both. |
| 4:00 | brute-force | Count coprime pairs in a 10 by 10 grid: 63 of 100, and the ratio creeps toward the target for bigger grids. |
| 7:00 | definition | A prime is a whole number whose only divisors are one and itself; coprime means no prime in common. |
| 8:30 | derivation | Sieve: a prime p divides both with chance one over p squared; survival is the product of one minus one over p squared. |
| 11:30 | demo-sim | Crossing out multiples prime by prime; the surviving fraction settles near six over pi squared. |
| 14:30 | misconception-defuse | Primes look random one by one, but the collective statistics are regular. |
| 16:00 | derivation | Euler's product: the product over primes equals the sum of one over n squared, which is pi squared over six. |
| 19:30 | wall | The prime count is about x over log x, but the actual count wiggles around that smooth curve. |
| 22:30 | story-rung | Riemann's zeta function: its zeros generate the wiggles in the prime count. |
| 25:30 | generalize | Other prime-pattern questions use the same product and sum machinery. |
| 27:30 | recap | The chain from coprime pairs to pi, in four steps. |
| 29:05 | coda | Honest caveat that the prime count is approximate; closing question about pi in unexpected places. Ends at 29:43. |

## Narration
<<<NARRATION
Here is a question that sounds unrelated to circles. Why would the number pi, the ratio of a circle's circumference to its diameter, show up when you count prime numbers? Primes are about multiplication and indivisibility. Circles are about geometry and smooth curves. There seems to be no reason for the two to meet. And yet they do, in a surprisingly clean way.

Let me state the answer up front, and then we will earn it. Pick two whole numbers at random. The chance that they share no common factor other than one is six divided by pi squared. Six over pi squared is about 0.61. So the probability that two random numbers are coprime is governed by pi, and pi sneaks into a question about primes.

Let's make that concrete. Consider the integers in a grid. Each cell is a pair of whole numbers, one across and one down. Two numbers are coprime if the only positive whole number that divides both is one. A pair like 4 and 6 fails, because both are divisible by 2. A pair like 3 and 5 succeeds, because they share nothing. We are going to count how often each happens.

Let's do the brute-force count. Take a small grid, with both numbers running from one to ten. There are one hundred pairs. Go through them one by one. Pairs like 2 and 4 share the factor 2. Pairs like 3 and 9 share 3. Pairs like 5 and 10 share 5. Count the ones that share nothing, and you get 63 coprime pairs out of 100. That is 0.63, which is already close to six over pi squared. Make the grid bigger, and the ratio creeps toward 0.608. The count works, but it doesn't say why.

So let's define our terms, minimally, and then refine. A prime is a whole number greater than one whose only divisors are one and itself. Two numbers are coprime when they have no prime in common. That is the whole definition. The important consequence is that two numbers fail to be coprime exactly when some prime divides both of them. So the question becomes: what is the chance that no prime divides both?

Now the sieve. Consider a large grid of pairs. Take the prime two. A pair fails because of two if both numbers are even. Among all pairs, the chance that both are even is one quarter. So the prime two removes a quarter of the pairs, and three quarters survive, for now. Next, the prime three. The chance both numbers are multiples of three is one ninth. The prime three removes one ninth of the pairs, but some of those were already removed by two, so we have to be careful not to double count.

Here is the trick that makes it clean. Divisibility by different primes behaves independently, so the chances multiply. The fraction of pairs that survive every prime is the product, over all primes p, of one minus one over p squared. Each factor says: the chance that a prime p divides both numbers is one over p squared, so the chance it doesn't is one minus that.

That product is a famous object. It is called an Euler product. Read in reverse, the product over primes of one over one minus one over p squared is the sum over all whole numbers n of one over n squared. That sum is a known series, and Euler found that it equals pi squared over six. So the product, which is the chance of coprime pairs, equals one over pi squared over six, which is six over pi squared. The circle has entered through the back door of a sum.

Let's make sure the chain is right. Each whole number factors uniquely into primes. When you expand the product over primes of geometric series, each term corresponds to exactly one whole number, with its powers of primes matching. That unique factorization is the reason the product and the sum are the same object. Euler's identity connects the sum of reciprocal squares to the prime structure. Primes are the building blocks, and the sum is the total over all their combinations.

Now watch the sieve work. On screen, start with the full grid, and cross out pairs divisible by two. Then cross out pairs divisible by three, then by five, and so on. As you add primes, the surviving fraction drops, and it approaches six over pi squared. With only the first few primes, the estimate is rough. With many primes, it settles. The animation is a visual version of the product, and the pi is what the infinite product converges to.

It's tempting to think primes are too random to contain anything like pi. Here is the misconception. Primes look irregular when you list them one by one. But their collective behavior, when you average over many pairs, has a very clean structure. The randomness is local, and the regularity is global. Pi lives in the global statistics, not in any single prime.

Now let's do the derivation once more, slowly, because it is the heart of the matter. Start with the sum of one over n squared. Split the whole numbers by their prime factors. Every whole number is a product of primes raised to powers. So the sum factors into a product over primes of sums over powers. Each of those inner sums is a geometric series, which equals one over one minus one over p squared. That step is why the product over primes shows up, and it is what the sieve computed independently. The two calculations agree, and that agreement is the reason pi appears.

Let's pause here, because the agreement is the whole point. The sieve counted the fraction of coprime pairs, and got a product over primes. The sum of reciprocal squares, by a different route, also factors into a product over primes. The two products are equal. The sum equals pi squared over six, so the coprime fraction equals six over pi squared. Two independent views, one answer.

Now the wall. Prime counting is harder. Suppose you ask how many primes are less than or equal to some number x. The prime number theorem says this count is roughly x over the natural logarithm of x. That is a smooth approximation, and it gets better as x grows. But the actual count wiggles around the smooth curve. It does not follow it cleanly. The wiggles are the real mystery, and no simple formula captures them.

That is where the story gets deep. The wiggles in the prime count are controlled by a function called the Riemann zeta function, which is the sum of one over n to the s, extended to complex numbers. The smooth part comes from one special point of that function. The fine detail comes from its zeros, the places where it vanishes. Each zero contributes a small wave to the prime count, like a note in a chord. This connects back to pi, because the function that generates the whole structure is built from the same sum we used to find six over pi squared.

Let's generalize. The pattern here is that a simple counting question, with a probability attached, reduces to a product over primes, and the product converges to something involving pi. The same style of argument works for other questions. The chance that a number has no repeated prime factor, the frequency of certain prime patterns, and the spacing of primes all rely on related machinery. You don't need every detail to see that the tools are shared.

Let me recap the chain. Two numbers are coprime if no prime divides both. The chance of that is a product over primes of one minus one over p squared. That product equals one over the zeta value at two, and the zeta value at two is pi squared over six. So the chance of coprime pairs is six over pi squared. Pi appears because the sum of reciprocal squares is the same as the prime product.

And here is the honest caveat that remains. The smooth count of primes is only an approximation, and the wiggles around it are where the deepest open questions sit. The pi result is clean and exact. The prime count is not, and the gap between those two is what makes the subject alive.

Thanks for watching, and the next time you see pi somewhere unexpected, ask what sum or product is hiding behind it.
NARRATION>>>

## Slots
```json
{
 "format_class": "question, answer stated, sieve and Euler product proof, wall, then story",
 "answer_given_upfront": true,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.03,
 "first_new_idea_frac": 0.03,
 "first_notation_frac": 0.13,
 "payoff_frac": 0.66,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "10 by 10 grid -> sieve over primes -> full product",
 "roadmap": "none",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": null,
 "caveat_type": "approximation",
 "recurring_anchor": "the sieve grid with crossed-out multiples, reused at three points",
 "sponsor_frac": null,
 "ending_type": "hook-callback",
 "teaser": false,
 "wpm": 165,
 "median_beat_s": 130,
 "beat_sequence": ["hook","answer-statement","toy-world","brute-force","definition","derivation","demo-sim","misconception-defuse","derivation","wall","story-rung","generalize","recap","coda"],
 "top5_moves": ["hook-question","brute-force-first","notation-after-concept","misconception-first","story"],
 "absent3_moves": ["humor","running-character","inline-quiz"]
}
```
