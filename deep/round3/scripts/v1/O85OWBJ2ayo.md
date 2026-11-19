# 3blue1brown: How (and why) to raise e to the power of a matrix | DE6

- channel: 3blue1brown
- id: O85OWBJ2ayo
- title: How (and why) to raise e to the power of a matrix | DE6
- duration: 1627 s (27:07)
- condition: v1
- recall: vague

## Content skeleton

- Hook: e to the x is its own derivative; what could e to a matrix possibly mean?
- Roadmap: a linear system of rates, the power series, a diagonal check, the wall of messy matrices, an eigenvector basis, a rotation example, and a convergence caveat.
- A two-quantity system where a matrix gives the rates, and the flow as the answer after time t.
- The naive entrywise exponential tried and shown to fail on a non-diagonal system.
- The power series, substituted with the matrix, shown to satisfy the flow equation by differentiation.
- Change of basis to eigenvectors makes the matrix diagonal; the exponential is computed in that basis and mapped back.
- Rotation matrix: the exponential is a rotation whose angle grows with time; generalization to cosine and sine of matrices.
- Caveat: convergence for all matrices is stated, and the rigorous proof is linked rather than fully shown.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | E to the x is its own derivative. What could e to a matrix mean? The question sounds like nonsense, so there must be a sensible definition. |
| 0:50 | roadmap | Plan: a system of rates, the naive attempt, the power series, eigenvectors, a rotation, and a convergence caveat. |
| 1:30 | toy-world | Two quantities whose rates depend on each other. The matrix gives the rates; the flow says where you are after time t. Arrows on a plane. |
| 3:30 | brute-force | The obvious definition: apply e to each entry. Tidy, and wrong. Test it on a system with a known flow and the arrows disagree. |
| 5:00 | derivation | The single-number case: the solution is e to the rate times t. So e to the matrix times t is the conjecture to test. |
| 7:00 | definition | The power series of e to the x, with the matrix substituted. Each term is a matrix; each factorial is a plain number. |
| 9:00 | demo-sim | Partial sums of the series for a small matrix settle after about a dozen terms. Each term named as multi-step effects. |
| 11:00 | derivation | Differentiate the series: the derivative equals A times the series again. The series satisfies the flow equation. |
| 12:30 | wall | For a general matrix the series term by term is painful, and the structure is hidden in the numbers. |
| 13:40 | definition | Eigenvectors are directions the matrix only stretches. Change basis so the matrix is diagonal, which makes the exponential easy. |
| 15:40 | derivation | Write A as P times D times P inverse. The exponential of At becomes P times e to the Dt times P inverse, each step on screen. |
| 18:00 | demo-sim | Rotation matrix: the eigenvalues are complex, the answer is real, and the flow is a rotation that grows with time. |
| 20:30 | misconception-defuse | The entrywise exponential is correct only for diagonal matrices. The power series is the real definition. |
| 21:30 | generalize | Cosine and sine of a matrix are defined by their series. The recipe is always: write the series, substitute, use the eigenvector basis. |
| 23:00 | caveat | Convergence for every matrix is stated, not fully proved here. The rigorous argument is linked for later reading. |
| 24:00 | recap | A system of rates has a matrix. Its flow is e to the matrix times time. The series defines it, the eigenvectors compute it, the rotation shows it. |
| 25:00 | callback | Back to the derivative of e to the x. The flow is the solution, the same derivative rule holds, and the work is in finding the basis. |
| 26:20 | teaser | Next: complex eigenvalues with a real part, where the flow spirals in or out. Stability. Ends at 27:07. |

## Narration

<<<NARRATION
Here's a question that sounds like nonsense. You know what e to the x means: the number e raised to a power x. You know its special property: e to the x is its own derivative, so its slope at every point equals its height. Now replace x with a matrix. What could e to the matrix possibly mean? A matrix is not a number, and you can't raise a number to a grid of entries in any obvious way. So either the question is meaningless, or there's a sensible definition that matches what we already know.

There is, and it's useful, because it solves a whole class of problems. Let's build toward it.

Here's the plan. We'll start with a small system of two quantities that change together, the kind of system where a matrix is the natural description. We'll try the obvious definition, which fails. Then we'll use the power series for e to the x, which does work for matrices. We'll test it, and find that the series is painful for most matrices. So we'll change viewpoint, into a basis where the matrix does something simple. At the end, we'll see a rotation example, which shows what this object does geometrically. There's a caveat about convergence that I'll flag when we get there.

Start with a system. Imagine two quantities, call them x and y, where the rate of change of each depends on both. The rate of x depends on x and on y, and the rate of y depends on both as well. We can write the whole rule as a matrix A, which takes a pair of numbers and gives back the pair of rates. Now the question becomes: if you start at a given point, where are you after time t? Let's call that answer the flow. Given the starting point, the flow tells you where you end up.

Think of it as arrows on a plane. At every point, the matrix gives an arrow telling you which way the point will move. Follow the arrows and you trace a path. The matrix defines a whole field of arrows, and the flow is what happens when you follow them for a while.

Now the link to e to the x. For a single number with the simple rule, where the rate of x equals a times x, the solution is e to the power a t, times the starting value. The rule says the slope is proportional to the height, and e raised to the rate is exactly what produces that behavior. So if we could make sense of e to the matrix, the flow would be e to the matrix times t, applied to the starting point. That's the conjecture we want to test.

Let's try the most naive definition first. Apply e to each entry of the matrix separately. Take e to the entry in the top left, and so on, and put the results back in the same grid. It's quick and tidy, and it's wrong. Test it on a system where we know the flow. The answer doesn't match the arrows. The naive approach fails because the entries interact through the matrix in a way that a grid-by-grid exponential can't capture.

That failure tells us something. We need a definition that respects how the matrix combines its entries. So let's go back to what e to the x actually is. Its power series is one, plus x, plus x squared over two factorial, plus x cubed over six, and so on. Each term is a power of x divided by a factorial, and the sum converges for every number. The series is the definition. It doesn't care whether x is a number. As long as you can multiply, you can take powers, and the factorials are just numbers.

So define e to the matrix as the same series. One, plus A, plus A squared over two, plus A cubed over six, and so on. Each term is a matrix. Add them up and you get a matrix. Check it on a diagonal matrix, where the off-diagonal entries are zero. The powers of that matrix raise each diagonal entry to a power, so the series splits into separate series for each entry, and we get back the ordinary exponential of each diagonal number. The naive attempt was right in that special case. That's a sanity check, and it tells us the definition is consistent.

Now let's see the series at work on a small example. Pick a matrix with some off-diagonal entries. Compute its square, cube, and so on. Each power gets a bit messier. Add the terms one at a time, and watch the partial sums. The first term is the identity. Add A, and the matrix shifts. Add the A squared term over two, and it shifts again. The partial sums settle down. After about a dozen terms, adding more changes the matrix by less than you can see. The series is converging, and the limit is the matrix exponential.

Pause and think about what's happening. Each power of A says how the rules compose. A squared is what you get after two steps of the arrows, A cubed after three. The series adds up all of those multi-step effects, weighted by one over the factorial. The result is the total effect of following the arrows for a time of one.

Now let's check that the series does what we want. Differentiate it with respect to t. The derivative of A to the power n, times t to the n over n factorial, is A times A to the power n minus one, times t to the n minus one over n minus one factorial. Pull out one factor of A, and what remains is the same series again. So the derivative of e to the At is A times e to the At. That's exactly the rule for the flow: the rate of change is the matrix times the current state. The series satisfies the system, and that's the justification for the definition.

So the definition works. But here's the wall. For a general matrix, computing the series term by term is painful. The powers get messy, and it's hard to see what the answer looks like. We'd like a way to see the structure, not just to compute it numerically.

That's where the change of viewpoint comes in. A matrix describes the arrows in one set of coordinates, but the same arrows look different in other coordinates. Some directions are special. There can be directions where the matrix only stretches, without turning. Those are the eigenvectors, and the stretch factor is the eigenvalue. If you use those special directions as your basis, the matrix becomes diagonal. Diagonal matrices are easy, because the exponential acts entry by entry, as we saw before.

So here's the stepping stone. Find the eigenvectors, put them in a matrix P as columns, and write A as P times a diagonal matrix D times the inverse of P. Now the power series becomes simple to compute. The powers of A collapse to the powers of D, sandwiched between P and its inverse. So e to the At equals P times e to the Dt times P inverse. Each piece is simple. The exponential of a diagonal matrix is just the exponential of each diagonal entry. Then we change back to the original coordinates with P.

Let's do this on screen. Here's the matrix A. Its eigenvectors are these two arrows, with eigenvalues that show how each direction stretches. Put them into P, write D, and compute the inverse of P. Now e to the Dt is a diagonal matrix with e to the lambda t on the diagonal. Multiply the three pieces, and you get the full answer. Every step is a visible operation on the picture.

Now the example that makes this concrete. Take a rotation matrix, one that turns the plane by a fixed angle. Its eigenvalues are complex, so the diagonal form uses complex numbers, but the final answer is real. Compute the exponential, and it's a rotation again, by an angle that grows with time. Plot the flow: starting from a point, the path circles around the origin. The matrix exponential has turned an abstract series into a picture of spinning.

Here's a misunderstanding worth defusing one more time. People often expect e to the matrix to be the matrix of entrywise exponentials, because that's how a single number works. It isn't, and we just saw why. The power series is the true definition. The entrywise version is a shortcut that works only in the special diagonal case.

Now generalize. The same trick works for any function that has a power series. Cosine and sine of a matrix are defined the same way, by their series. Apply them to a rotation matrix and you get the cosine and sine of the rotation angle. So the matrix version of an ordinary function is always built from the same recipe: write the series, substitute the matrix, and use the eigenvector basis when you need to see the structure.

Now the caveat. I've shown that the series satisfies the flow equation, and I've shown it converging in the examples. But I've been loose about why it converges for every matrix. The full argument depends on how the size of a matrix controls its powers, and I've glossed over that. The linked resources have the rigorous version. What I want you to take away is the mechanism: the series is a sum of multi-step effects, and the eigenvector basis reveals its structure. The convergence proof is a separate question, and it's worth working through if you're going to rely on it.

Let's recap. A linear system of rates has a matrix. Its flow is e to the matrix times time, applied to the start. The power series defines the exponential for matrices. The eigenvector basis turns the series into a simple formula, and the rotation example shows the geometry.

Now go back to the start. We asked what e to the matrix could mean, and the derivative of e to the x gave us the clue. The answer is the flow of the system, defined by the same power series, and the same derivative rule holds. Every linear system with constant rates has this solution, and the only work left is finding the right basis.

And that leads to the next question. We've seen rotations, where the eigenvalues are complex and the flow circles. What happens when the eigenvalues are complex with a real part, so the flow spirals in or spirals out? That's a question about stability, and it's where the eigenvalues start to tell you everything about the system's long-run behavior.
NARRATION>>>

## Slots

```json
{
 "format_class": "problem-to-tool derivation, toy system first, series then eigenvector basis",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.0,
 "first_concrete_object_frac": 0.06,
 "first_new_idea_frac": 0.26,
 "first_notation_frac": 0.06,
 "payoff_frac": 0.66,
 "misconception": "staged-early",
 "brute_force_first": true,
 "examples_count": 4,
 "example_growth": "diagonal -> non-diagonal -> rotation",
 "roadmap": "one-line",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": null,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the two-quantity system and its arrows, reused in every example",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 90,
 "beat_sequence": ["hook","roadmap","toy-world","brute-force","derivation","definition","demo-sim","wall","misconception-defuse","generalize","caveat","recap","callback","teaser"],
 "top5_moves": ["toy-world","brute-force-first","special-case-first","notation-after-concept","simulation-as-argument"],
 "absent3_moves": ["humor","running-character","second-person-role"]
}
```
