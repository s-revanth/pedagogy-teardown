channel: 3blue1brown
id: O85OWBJ2ayo
title: How (and why) to raise e to the power of a matrix | DE6
duration: 1627 s (27:07)
condition: base
recall: vague

## Content skeleton
- Opening on a flow field of arrows, and the question of what e to the power of a matrix could mean.
- Answer stated early: it is the solution operator for a linear flow, x prime equals A x.
- Definition by the power series, extended from the scalar exponential to matrices.
- Brute-force term-by-term computation with matrix powers, which converges but explains little.
- Misconception: e to the A is not computed entry by entry.
- Derivative check: the derivative of e to the At is A times e to the At, so the series solves the flow.
- Diagonal case as the easy analogy; diagonalization as the general computing method.
- Shear matrix where diagonalization fails; domain limits and closing generalization.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | A grid of flow arrows on screen; question: e to the x is familiar, so what would e to a matrix mean? |
| 1:00 | answer-statement | It is the solution of a linear flow: position at time t is e to the At times the starting point. |
| 1:40 | toy-world | A dot pushed around the plane by a matrix; the velocity at each point is A times the position. |
| 4:30 | definition | The scalar exponential as the power series; its derivative is itself. |
| 7:00 | brute-force | Plug the matrix into the series; compute A squared, A cubed, and sum term by term. |
| 10:00 | misconception-defuse | Entry-by-entry exponentiation is not the matrix exponential; the powers mix the entries. |
| 11:40 | demo-sim | Partial sums drawn as flow pictures; they settle as more terms are added. |
| 14:30 | derivation | Differentiate the series: each term brings down an A; the derivative equals A times the exponential. |
| 18:00 | analogy | A diagonal matrix: each axis scales on its own, so its exponential is entrywise on the diagonal. |
| 20:30 | derivation | Write A as P D P inverse; e to the At equals P e to the Dt P inverse; compute for real eigenvalues. |
| 24:00 | wall | A shear has no full set of eigenvectors; the diagonal trick breaks. |
| 25:30 | caveat | The series always converges, but closed forms are not always available. |
| 26:20 | generalize | Any linear system, in any dimension, has the same solution form. |
| 26:50 | coda | Return to the opening question. Ends at 27:07. |

## Narration
<<<NARRATION
Start with a number you already know how to exponentiate. e to the x, where e is about 2.718, is the function whose growth rate equals its current size. Its derivative is itself. That property is why it shows up whenever something grows or decays in proportion to how much is there. Now here is a question that sounds almost silly: what would e to the power of a matrix possibly mean? You can't raise a number to a matrix. So why would anyone try?

Here is the answer, stated up front, and then we'll earn it. Suppose a point moves in the plane, and at every moment its velocity is determined by where it is, through a matrix. Written out, the velocity equals A times the position. Then the position at time t is e to the power of A times t, applied to the starting point. The matrix exponential is the object that tells you where a linear flow carries things after a given amount of time.

Let's build that picture. Imagine a grid of tiny arrows covering the plane. Each arrow shows the velocity of a point at that location, and that velocity is the matrix times the position. Drop a dot anywhere and let it go. It follows the arrows, moving smoothly. The matrix decides the entire pattern. Some matrices make the dots spiral, some stretch them apart, some squash them along a line. Once you see the flow, the question about e to the A becomes a question about where the dots end up.

Now we need to define e to the power of something, and the cleanest way is the one we use for ordinary numbers. For a scalar x, e to the x is the sum of x to the n over n factorial, from n equals zero to infinity. The first few terms are one, plus x, plus x squared over two, plus x cubed over six, and the sum keeps going. For any x, the partial sums settle to a definite value. That infinite sum is the definition, and it explains why the derivative of e to the x is e to the x: differentiating the series shifts every term down by one.

Here is the important move. The same power series makes sense if x is replaced by a matrix, provided we know how to multiply a matrix by itself and divide by a number. We can square a matrix, cube it, and so on. So we write e to the A as the identity matrix, plus A, plus A squared over two, plus A cubed over six, and so on.

Let's try it, and let's be brute force about it. Take a simple matrix and compute its powers: the square, the cube, the fourth power. Each term is a matrix, and you add them entry by entry. The first few sums look messy, but they are concrete, and they converge. If you keep adding terms, the result stabilizes, and you get a matrix. That matrix is e to the A. This is a legitimate definition, and in principle it is a complete answer. But it doesn't tell you much about the flow, and summing thousands of terms is not how anyone wants to live.

Now a common misunderstanding needs clearing up before we go further. Some people guess that e to the A means you take e to the power of each entry of A separately. That is not what it means. The matrix exponential does not act entry by entry. The entries of e to the A are mixed together in a complicated way, because the matrix powers mix them. If you exponentiate entries individually, you get a different matrix, and it generally does not solve the flow. The series is the definition, and the series does the mixing.

Let's watch the series converge. On screen, the partial sums are drawn as flow pictures. With one term, the flow is trivial. With two terms, it starts to bend. With five or six, the picture looks much like the flow of the original matrix over a short time. As more terms are added, the picture settles, and the transformation at time t becomes stable. You can see the matrix exponential as the map that carries each starting dot to its location after time t.

Now let's check that this really solves the flow. Take the derivative of e to the At with respect to t, using the series. Each term has t to a power, and differentiating drops the power by one and brings down a factor of A. When you reassemble, you get A times e to the At. So the derivative of the transformation is the matrix A multiplied by the transformation. That is exactly the equation for a linear flow: the rate of change equals A times the current state. The series is not just a definition. It is the correct solution, and the derivative shows why.

Now let's build intuition with the simplest case. Suppose A is diagonal, with numbers on the diagonal and zeros elsewhere. Then the flow is simple: each axis is scaled independently. The x coordinate grows at its own rate, and the y coordinate grows at its own rate, with no mixing. The matrix exponential is then diagonal too, with e to the power of each diagonal entry times t on the diagonal. Each axis just gets its own exponential. This is the one case where the entrywise idea happens to work, and it is worth noticing exactly why it works here and nowhere else.

That simple case suggests a strategy. If a general matrix can be rewritten in diagonal form after a change of coordinates, you can compute its exponential by converting to the simple coordinates, exponentiating there, and converting back. Write A as P times D times P inverse, where D is diagonal and P changes coordinates. Then e to the At equals P times e to the Dt times P inverse. The hard problem becomes an easy diagonal problem, sandwiched between two changes of basis.

Let's do the computation. Take a matrix with two real eigenvalues. Find its eigenvectors, which become the columns of P. Put the eigenvalues on the diagonal of D. Then e to the Dt is the diagonal matrix with e to the lambda one t and e to the lambda two t. Multiply out with P and P inverse, and you get the transformation at time t. The payoff is a closed form. For any t, you can say exactly where each point goes.

Not every matrix can be diagonalized, and this is where the picture gets interesting. Consider a shear, a matrix that slants things without stretching them along separate axes. It has a repeated eigenvalue, and there aren't enough eigenvectors to form a full coordinate change. The diagonal trick breaks. So we need the series, or a slightly different standard form that keeps a small off-diagonal piece. The flow still exists, and the exponential still exists. The method just has to be more careful.

Let me be honest about the limits. The power series always converges for any square matrix, so the matrix exponential is always defined. But getting a closed form you can read off by eye is not always possible. For some matrices the diagonal trick gives a clean answer. For others you need the Jordan form, or you have to accept numerical methods. That is a real domain limit, and it is why computer libraries spend so much effort on this one function.

The most important thing to take away is that this is not just a fancy idea. Anything that changes linearly with its current state, in any number of dimensions, is governed by the same logic. A population model, a set of coupled springs, a simple electrical network, all reduce to some version of x prime equals A x. And the answer is always x of t equals e to the At times x zero. Once you understand the matrix exponential, you understand the whole family.

Let me step back to the question from the beginning. We asked what e to the power of a matrix could mean, and it turned out to be natural. It is the solution operator for a linear flow. It is defined by the same power series that defines the scalar exponential, and its derivative explains why it solves the flow. Diagonalizing makes it computable when the matrix is nice, and the flow picture tells you what it does.

So the next time you see e to the power of something you didn't expect, ask what process it is describing. Here, it is a flow carrying every point through the plane, and the matrix exponential is the rule that tells you where each point ends up after time t.

Thanks for watching.
NARRATION>>>

## Slots
```json
{
 "format_class": "question, answer stated, flow picture, series, derivative check",
 "answer_given_upfront": true,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.01,
 "first_new_idea_frac": 0.04,
 "first_notation_frac": 0.17,
 "payoff_frac": 0.8,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 4,
 "example_growth": "scalar -> matrix series -> diagonal -> shear",
 "roadmap": "none",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": null,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the flow arrows on the grid, reused at every stage",
 "sponsor_frac": null,
 "ending_type": "hook-callback",
 "teaser": false,
 "wpm": 165,
 "median_beat_s": 125,
 "beat_sequence": ["hook","answer-statement","toy-world","definition","brute-force","misconception-defuse","demo-sim","derivation","analogy","derivation","wall","caveat","generalize","coda"],
 "top5_moves": ["toy-world","brute-force-first","misconception-first","simulation-as-argument","notation-after-concept"],
 "absent3_moves": ["humor","running-character","inline-quiz"]
}
```
