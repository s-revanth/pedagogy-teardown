# Header
- channel: Reducible
- id: Ty0JcR6Dvis
- title: FFT Example: Unraveling the Recursion
- duration: 458 s (7:38)
- condition: v3
- recall: none
- exemplars read: xlVX7dXLS64 (full), h7apO7q16V0 (first third)

## Content skeleton
- Premise: the fast Fourier transform is a single idea, a split into two halves, applied again and again.
- Four-coefficient polynomial; evaluate at the four roots of unity.
- Squaring the roots gives only two distinct values, which means repeated work that can be shared.
- Direct evaluation as the reference: about sixteen multiplications, reference answers written down.
- Split into even-power and odd-power polynomials; evaluate each at the two squared values.
- Glue back with the twiddle factor; every answer matches the direct result.
- Each level halves the problem; n log n total; power-of-two caveat with zero padding.
- Coda on repeated splitting; sponsor read; teaser for the next video.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | premise-claim: the FFT trick is a split, solve, glue; easy to lose in formulas |
| 0:25 | roadmap | run it by hand on four coefficients and check against direct evaluation |
| 0:40 | toy-world | a four-coefficient polynomial and the four roots of unity |
| 1:30 | rhetorical | can we do better than plugging in each point one at a time |
| 1:50 | definition | squaring the roots gives only two distinct values; repeated values mean shared work |
| 2:40 | brute-force | direct evaluation, roughly sixteen multiplications; reference answers written down |
| 3:40 | demo-sim | split into even-power and odd-power polynomials |
| 4:40 | derivation | evaluate each half at the two squared values; pairs of points share them |
| 5:40 | derivation | glue with the twiddle factor; each point matches the direct answer |
| 6:20 | generalize | each level halves the problem; order n log n overall |
| 6:50 | caveat | the halving needs a power-of-two size; pad with zeros |
| 7:10 | coda | the recursion is repeated splitting, reusing work already done |
| 7:25 | sponsor | generic courses read with a link in the description |
| 7:33 | teaser | next video: the transform on a whole signal |

<<<NARRATION
The fast Fourier transform is one of the most important algorithms ever written, and the trick inside it fits in a single sentence. You split a list in two, solve each half, and glue the answers back together. That is the whole idea, and it is easy to lose inside the formulas. So in this video we will run it by hand on a small example and watch the recursion unfold. I think that is the best way to see why it works.

Here is what we will do. We start with a polynomial that has four coefficients, and we ask for its values at four special points. First we do the slow way, then the recursive way, and we check that both give the same answers. In the end we want the recursion to look less like magic and more like bookkeeping. Keep a pencil nearby, because we will write a few things down.

Take a polynomial whose coefficients run from one through four. We want to evaluate it at four points. The points we choose are not random. They are the roots of unity: one, the imaginary unit, minus one, and minus the imaginary unit. These are the points where raising to a power keeps landing back on a small set of values.

Can we do better than plugging in each point one at a time? Think about what happens when we square these points. We will see that squaring is the key.

Squaring a root of unity doubles its angle around the circle. Keep doubling, and the angles wrap around and land back on values we have already seen. Squaring the roots here gives just a couple of distinct values, and they repeat. That is a strange and useful fact. It means the squared values repeat, and whenever values repeat we can reuse work. I want you to remember this, because the whole recursion depends on it.

Let's do the direct way first, so we have something to check against. Plugging in a point takes a few multiplications and additions, and we do that for each of the four points, so the total is roughly sixteen multiplications. For the first point, the sum is ten. The other points follow the same pattern, and we will check each one as we go.

Now the recursion. Split the polynomial into two smaller ones: the even-powered terms and the odd-powered terms. The even terms are the constant term and the x squared term. Together they give a new polynomial E of y, where y stands for x squared. The odd terms give a second polynomial, O of y. The original polynomial can be written as E of x squared, plus x times O of x squared. We have replaced a big problem with a pair of smaller ones, each one half the size.

Now we only need the two smaller polynomials at the squared values. Those squared values are only one and minus one. Pairs of the original points share them, so each evaluation gets reused. For E, the first value is four and the second is minus two. For O, they are six and minus two. Each of these is a tiny calculation, and we do them once.

Consider the first point. Its square lands on a value we already have, so we take E plus the point times O at that value. That gives four plus six, which is ten, and it matches the direct answer. For the second point, we square it and then do the same gluing step, with the imaginary unit multiplying the odd part. The factor in front of the odd part is called the twiddle factor, and it is the only place where the two halves interact.

The third and fourth points come out the same way. Their squares reuse the same small values, so no new evaluations are needed. The third point's answer uses the same pair with a minus sign in front of the odd part, and the fourth uses the imaginary unit with that same minus sign. Every answer matches the brute force result. We did the same job with far fewer multiplications, because the two small evaluations were shared between pairs of points.

Look at what we just did. Each level halves the size of the problem and then does a linear amount of gluing. Repeat that split again and again, and the total work comes out to order n times log n, instead of order n squared. That is the reason the transform is so fast on the large signals that show up in audio, images and radio. I would argue the speedup matters more than any single formula in the video.

Notice what did not happen. We never evaluated a full-size polynomial more than once. The big problem became a pair of problems that are half the size, and those were solved with the same trick, which is exactly the recursion in the title. I think that observation is the heart of the whole method, and it is worth saying slowly.

If we want to try this ourselves, we pick a different polynomial and run the same steps. We will find the same pattern of reuse. Write down the direct values first, then compare them with your glued answers. If they agree, the method works for that input, and we have seen the structure rather than just the formula. That habit of checking against a slow method is worth keeping for every fast algorithm you meet.

There is a catch, and it matters. This clean halving works when the number of points is a power of two, so that every split comes out even. Suppose your input length is awkward, say a handful of samples. You pad it with zeros until it fits the pattern. That is a practical fix, and it works, but it means the method is tuned to a particular shape of problem. Use it where its assumptions hold, and check those assumptions when they do not. Probably the most common mistake is forgetting this step entirely.

So the recursion is not really a trick. It is a repeated split, and every split reuses work we have already done. Once we see the even and odd halves, the rest is bookkeeping, and that is the lesson I want you to take away. An algorithm that looks impossible at first can be a simple idea applied at many scales, and that is worth remembering the next time a problem looks too big. Image compression, audio, radar and fast multiplication of huge integers all lean on variants of the same split.

This video is sponsored by a company that makes interactive courses for maths and programming. They asked me to mention their practice problems, which you can work through at your own pace. I would encourage you to look if you are curious, and I will leave a link in the description. For example, their probability section is a good place to start if you want to practise.

In the next video, we will look at how the transform works on a whole signal, not just four points, and what the results mean. Thanks for watching.
NARRATION>>>

```json
{
 "format_class": "worked-example recursion, brute-force check then split and glue",
 "answer_given_upfront": true,
 "hook_type": "premise-claim",
 "first_question_frac": 0.12,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.2,
 "first_notation_frac": 0.05,
 "payoff_frac": 0.84,
 "misconception": "none",
 "brute_force_first": true,
 "examples_count": 2,
 "example_growth": "four points by hand -> whole signal next",
 "roadmap": "one-line",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.12,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the polynomial with coefficients one through four, checked at every step",
 "sponsor_frac": 0.98,
 "ending_type": "impact-coda",
 "teaser": true,
 "wpm": 172,
 "median_beat_s": 38,
 "beat_sequence": ["hook","roadmap","toy-world","rhetorical","definition","brute-force","demo-sim","derivation","derivation","generalize","caveat","coda","sponsor","teaser"],
 "top5_moves": ["brute-force-first","notation-after-concept","simulation-as-argument","special-case-first","visible-repetition"],
 "absent3_moves": ["humor","story","inline-quiz"]
}
```
```json
{"verified_trace": {"wpm": "PASS 172.00 (target 163.32-184.1, median 172.25)", "you_rate": "PASS 1.00 (target 0.73-1.35, median 1.05)", "i_rate": "PASS 0.67 (target 0.46-1.1, median 0.75)", "we_rate": "PASS 2.99 (target 2.46-4.0, median 3.76)", "num_rate": "PASS 2.66 (target 1.82-3.19, median 2.56)", "hedge_rate": "PASS 0.17 (target 0.1-0.24, median 0.16)", "example_rate": "PASS 0.17 (target 0.15-0.37, median 0.22)", "switch_sponsor": "PASS detected=True default=ON", "switch_teaser": "PASS detected=True default=ON", "switch_roadmap": "PASS detected=True default=ON", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (premise-claim vs premise-claim)", "ending_type": "MATCHES default (impact-coda vs impact-coda)", "summary": "7/7 numeric targets pass"}}
```
