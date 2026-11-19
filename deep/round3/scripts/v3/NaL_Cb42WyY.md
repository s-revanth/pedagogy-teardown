# Header
- channel: 3blue1brown
- id: NaL_Cb42WyY
- title: Pi hiding in prime regularities
- duration: 1783 s
- condition: v3
- recall: none
- exemplars read: deep/corpus/compact/QJYmyhnaaek.txt, deep/corpus/compact/BLkz5LGWihw.txt

## Content skeleton
- Claim up front: pi, the circle constant, is hidden inside the arithmetic of the primes.
- Toy world: the primes and their apparent randomness; sorting odd primes by remainder mod four.
- Chebyshev's bias: remainder-three primes lead early on, for a long stretch.
- A sign pattern: plus one, zero, minus one, zero, repeating every four steps.
- Leibniz sum over that pattern equals pi over four, via the arctangent series at one.
- Euler's idea: a sum over all integers rewritten as a product over primes gives pi over four.
- Caveat on convergence; Dirichlet's theorem on the long-run sharing of primes between remainder classes.
- Close: other characters give other constants; the primes carry hidden signals.

## Beat sheet (about 2200 spoken words across 1783 s)
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Premise: pi lives in geometry, yet it turns up in the primes |
| 1:00 | toy-world | The first primes and their irregular gaps |
| 2:30 | definition | Odd primes split by remainder on division by four |
| 4:00 | viewer-turn | Guess which family gets ahead as we count upward |
| 5:00 | derivation | Count the primes below twenty; the early lead of the threes |
| 8:00 | definition | Chebyshev's bias and the character: plus one, zero, minus one, zero |
| 9:30 | derivation | The alternating sum over that character |
| 12:00 | derivation | Leibniz series and the arctangent of one |
| 14:00 | derivation | Euler's idea: sum over integers becomes product over primes |
| 17:00 | payoff | Pi over four equals a product over odd primes |
| 19:00 | analogy | The primes as a bookkeeping device for multiplication |
| 21:00 | caveat | Convergence is slow and delicate; the rigorous version takes work |
| 23:00 | generalize | Dirichlet's theorem and other characters, other constants |
| 26:00 | generalize | Why a circle constant shows up in counting |
| 28:30 | coda | Pi is built into the arithmetic of the integers |

<<<NARRATION
Pi is usually introduced as the ratio of a circle's circumference to its diameter, which means it lives in geometry, a long way from the whole numbers. Yet the same constant turns up inside the primes, the numbers that cannot be divided evenly by anything except one and themselves. You might find that connection strange, and you would be right to. Here we will build it up step by step, so that the strangeness gives way to understanding.

Start with the primes themselves. The first few are two, three, five, seven, eleven, thirteen, seventeen, nineteen, and twenty-three, and after that they keep appearing with no obvious rule. Their gaps grow and shrink irregularly, and it is tempting to conclude that they are simply random. In one sense they are not random at all, and the regularities hiding in them are what this video is about.

Let's begin with a simple sorting trick. Every odd prime leaves a remainder of either one or three when divided by four. Five leaves one, since five is four plus one. Seven leaves three. Eleven leaves three, thirteen leaves one, and seventeen leaves one again. So the odd primes split naturally into two families, and we can ask whether those families are equally common as we count upward.

Before you read on, guess which family you think gets ahead. Many people guess that the two should be roughly even, since nothing in the definition of a prime seems to favor either remainder. Keep that guess in mind, because the real answer is more interesting than an even split, and it will tell you something about how the primes are arranged.

If you want to test your guess, you do not need a computer for the first stage. Write down the odd numbers up to a modest limit, cross out the composites, and sort what remains by remainder. You will see the threes stay ahead for a while, and you can watch the lead shrink and grow as you go. Suppose you did this by hand. You would be running a small version of the experiment that made this bias famous, which is a satisfying thing to do with a pencil.

Count the primes below twenty. The family with remainder three contains three, seven, eleven, and nineteen, which makes four members. The family with remainder one contains five, thirteen, and seventeen, which makes three. So far the threes are ahead, and this lead is not a fluke of the very first numbers. Mathematicians call this a bias, and it persists for a surprisingly long stretch of the number line.

This bias is known as Chebyshev's bias, after the nineteenth century mathematician who noticed it. Careful counting shows that the remainder-three primes lead for most of the range we can check. The lead does flip at times, in a way that is still an active area of research, so you should not expect it to be a simple rule. For our purposes the important point is that the primes are not perfectly balanced, and the imbalance follows a pattern we can describe.

Why would a count of primes lean one way at all? Nothing in the definition of a prime mentions four, so the lean has to come from how primes interact with multiplication. I find that idea hard to shake. A prime is defined without any reference to remainders, and yet remainders keep leaving fingerprints on the list. As you read on, keep asking where that fingerprint comes from, because the answer is the heart of the video.

To describe that pattern cleanly, we need a little bookkeeping. Define a function, which mathematicians call a character, that assigns plus one to numbers leaving remainder one, minus one to numbers leaving remainder three, and zero to even numbers. The values run plus one, zero, minus one, zero, and then they repeat every four steps. That sequence of signs is the whole ingredient, and it contains the pattern of the two families.

Suppose you were handed this sign sequence with no context at all. You might not recognize it as a character, and you would just see a repeating pattern of plus, nothing, minus, nothing. You could then ask what happens when you weight each entry by one over its position. That single move, weighting by the reciprocal, is what turns a pattern in the integers into a number that could be an analytic constant. Imagine how strange that would look to someone who had only ever seen the integers as a plain list.

Now form a sum in which each term is that character divided by the number itself. The first few terms look like plus one, minus one third, plus one fifth, minus one seventh, and so on. Notice that every term with an even denominator has disappeared, because the character is zero there. What remains alternates in sign, with the terms shrinking as we go, which is a very familiar shape for anyone who has met an alternating series before.

This is the Leibniz series, and it has a famous value. If you add up all those alternating terms, the total approaches pi over four. You can see why from the series for the arctangent. The arctangent of x is x minus x cubed over three, plus x to the fifth over five, and so on, and when x equals one, every term matches the Leibniz sum. So the arctangent of one, which is pi over four, is exactly the total we wanted to reach.

Let me say more about why the arctangent connects to this sum. The series for the arctangent comes from the geometric series, which you may already know well. If you add up alternating powers of x, you get a rational function, and integrating that function term by term produces the arctangent series. You do not need to memorize every step. What matters is that you can rederive the result yourself, and I would encourage you to try it on paper before moving on.

Now comes the key step. The sum we just evaluated runs over all the whole numbers, not only the primes, so the primes have not entered the story yet. Here is the central idea, which goes back to Euler. Every whole number factors uniquely into primes, and a sum over all whole numbers can be rewritten as a product over the primes. Whenever a sum and a product agree like this, it is a sign that a deep structure is at work.

How would you check that a rewriting like this is legitimate? One way is to expand only a couple of factors by hand. Take the first two primes, multiply out their geometric series, and you will see products of powers of those primes appear as terms. That is unique factorization at work, and it is exactly why the bookkeeping is not an illusion. You can convince yourself of the mechanism long before you trust the full result.

Let's see how the rewriting goes, at least roughly. Each prime p contributes a factor that is a geometric series in its powers, namely one plus the character of p over p, plus the character of p squared over p squared, and so on. Summing that geometric series gives one divided by one minus the character of p over p. Multiply those factors over all the primes, and the expansion reproduces every term of the original sum, because of unique factorization. So the sum equals a product over primes.

Putting the two results together, pi over four equals the product, over all odd primes, of one divided by one minus the character of p over p. The three, the five, the seven, and so on each contribute a small correction, and the corrections multiply together to produce pi over four. In other words, the constant of circles is hiding in the way primes multiply. That is a surprising thing to see written down, and I find it remarkable every time.

Let me pause on convergence, because it deserves real care. Multiplying the factors in their natural order, prime by prime, converges only slowly, and the product is not absolutely convergent in the way that a simple sum of positive terms would be. This is exactly the kind of subtlety where a naive manipulation can mislead you. The identity is true, but the rigorous version takes more work than a slogan suggests, and you should respect that gap.

If you are worried that slow convergence invalidates the whole argument, that worry is reasonable. The fix is to order the terms in a way that makes the sums behave, or to work with the sum first and treat the product as a consequence. Either way, the lesson is that a formula can be beautiful and still require careful handling. Why should a slogan be trusted without its fine print? I would rather you learn to ask that question than accept a neat identity without it.

Let's check the sensible range numerically. The first few factors give three over four, times five over four, times seven over eight, and so on, and the partial products drift toward roughly 0.785, which is pi over four. The drift is slow, and it wobbles, which is what you would expect from a product whose terms shrink in size while the character alternates in sign. A calculator will confirm the target, but the reasons behind it are what we are really after.

Why does an analytic constant appear in a question about primes? The reason is that the sum over the character is an analytic object, something that can be studied with the tools of calculus, while the product over primes is a combinatorial object, something you could compute prime by prime. The equality bridges the two worlds. If you have ever wondered how counting and calculus could ever meet, this is one of the cleanest answers available.

There is a deeper result behind all of this, due to Dirichlet. He proved that primes are shared among the remainder families that are compatible with the modulus, and in the long run each family receives the same share. The sign pattern is therefore not an accident of small numbers. The bias we saw earlier fits into this larger picture, because the families are not forced to be balanced at every finite stage, and the way they drift apart is governed by exactly this kind of sum.

You might wonder why Dirichlet's result needed a proof at all. The answer is that the sharing of primes among classes is subtle, and naive guesses about it are often wrong. Imagine trying to predict the long-run share of primes in one class by listing a few dozen of them. You would see fluctuations that look convincing and then fade. Why trust a table alone when a theorem can tell you what the table cannot?

Other characters, built from other moduli, produce other sums, and they lead to other famous constants, including logarithms and different square roots. The method generalises, and each new character gives a new window onto the primes. Pi is just the first beautiful example you meet when you choose the simplest character. That is the most important lesson, I think: the primes carry hidden signals, and the right tool reveals them.

I want to be clear that this is a research-level story, but the first steps are within reach of anyone who has seen a geometric series. Pick any character you can define, sum its values over the reciprocals, and ask whether the answer looks like a famous constant. Sometimes it will, and sometimes it will not, and both outcomes teach you something real. If you enjoy this kind of experiment, you are in good company.

Do you remember the list of primes at the start? Those numbers looked like noise, and one by one they still do. The surprise is that noise sorted in a clever way can encode geometry, and I think that is the real reason this subject keeps drawing people back.

Let me close with the picture we started with. A circle has its constant encoded in its geometry, and the primes seem to be an unrelated collection of counting numbers. Yet when we sort the primes by remainder, track a simple sign pattern, and multiply the contributions together, a circle's constant reappears. Pi is not only found in circles. It is quietly built into the arithmetic of the integers, waiting for someone to ask the right question.
NARRATION>>>

```json
{
 "format_class": "toy sorting, bias, sign pattern, Leibniz sum, Euler product, caveat, coda",
 "answer_given_upfront": true,
 "hook_type": "premise-claim",
 "first_question_frac": 0.10,
 "first_concrete_object_frac": 0.03,
 "first_new_idea_frac": 0.08,
 "first_notation_frac": 0.30,
 "payoff_frac": 0.62,
 "misconception": "planted-myth-defused",
 "brute_force_first": false,
 "examples_count": 4,
 "example_growth": "first primes -> mod four classes -> Leibniz -> product",
 "roadmap": "none",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.20,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the sign pattern plus one, zero, minus one, zero",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": false,
 "wpm": 169,
 "median_beat_s": 120,
 "beat_sequence": ["hook","toy-world","definition","viewer-turn","derivation","definition","derivation","derivation","derivation","payoff","analogy","caveat","generalize","coda"],
 "top5_moves": ["misconception-first","notation-after-concept","honest-caveat","generalize-to-other-domains","commit-to-answer"],
 "absent3_moves": ["brute-force-first","failure-shown","act-it-out"]
}
```

```json
{"verified_trace": {"wpm": "PASS 169.00 (target 160.79-174.3, median 169.42)", "you_rate": "FAIL 2.34 (target 1.76-2.09, median 1.99)", "i_rate": "FAIL 0.48 (target 0.55-0.84, median 0.67)", "we_rate": "FAIL 0.81 (target 0.82-1.09, median 0.96)", "num_rate": "FAIL 4.16 (target 2.49-3.96, median 2.97)", "hedge_rate": "PASS 0.29 (target 0.24-0.43, median 0.32)", "example_rate": "FAIL 0.19 (target 0.24-0.37, median 0.28)", "q_rate": "PASS 0.29 (target 0.17-0.35, median 0.26)", "sent_len": "FAIL 17.28 (target 22.58-24.33, median 23.66)", "switch_sponsor": "PASS detected=False default=OFF", "switch_teaser": "PASS detected=False default=OFF", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (premise-claim vs premise-claim)", "ending_type": "MATCHES default (teaser-next vs teaser-next)", "summary": "3/9 numeric targets pass"}}
```
