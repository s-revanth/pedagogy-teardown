# Header
- channel: 3blue1brown
- id: piJkuavhV50
- title: Solving problems by adding a dimension
- duration: 1782 s
- condition: v3
- recall: none
- exemplars read: deep/corpus/compact/LPZh9BOjkQs.txt, deep/corpus/compact/rbu7Zu5X1zI.txt

## Content skeleton
- Claim up front: a stubborn one-dimensional problem can become easy once you add a second dimension.
- Toy world: the Gaussian integral of e to the minus x squared, which has no ordinary antiderivative.
- Trick: square the integral, turn it into a double integral over the plane, switch to polar coordinates.
- Result: the Gaussian integral equals the square root of pi.
- Second example: a random point in a square lands in the unit circle with probability pi over four.
- Third example: the volume of a ball from circular cross-sections, four pi over three.
- Lesson and caveat: the extra dimension exposes symmetry, but only when the problem has it.
- Generalisation to n dimensions and a closing thought about where the trick fails.

## Beat sheet (about 2200 spoken words across 1782 s)
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Premise: a hard one-dimensional problem can be easy in two dimensions |
| 1:00 | toy-world | The integral of e to the minus x squared, with no ordinary antiderivative |
| 2:30 | viewer-turn | Pause: can you see why squaring might help |
| 3:30 | derivation | Square the integral; write it as a double integral over the plane |
| 5:30 | definition | The exponent depends only on distance from the origin: polar coordinates |
| 7:00 | derivation | Evaluate: the angle gives two pi, the radial part gives one half, the result is root pi |
| 9:00 | payoff | The Gaussian integral equals root pi; a surprising constant appears |
| 10:30 | analogy | Adding a dimension as viewing a shadow from a different angle |
| 12:00 | derivation | Random point in a square lands in the unit disk: probability pi over four |
| 14:00 | derivation | Volume of a ball from circular cross-sections: four pi over three |
| 15:30 | generalize | The lesson: the extra dimension exposes symmetry |
| 17:00 | caveat | The trick fails when the problem has no symmetry to exploit |
| 17:30 | coda | Closing thought on n dimensions and where the trick leads |

<<<NARRATION
A hard problem in one dimension is often an easy problem in two, and that surprising fact is the subject of this video. You might expect that adding a dimension makes everything harder, since there are more variables to juggle. Sometimes it does. But many of the most elegant solutions come from doing exactly the opposite, which is why this idea deserves a careful look.

We begin with a famous integral. The function e to the minus x squared produces a smooth bell-shaped curve, and you may well want to know the total area under it from negative infinity to positive infinity. The strange thing is that this function has no antiderivative that you can write down with the usual toolkit. If you try the standard methods, you will find yourself stuck, and that frustration is exactly the reason we need a new idea.

So here is the new idea. Pause for a moment and ask yourself whether there is a way to make the problem look nicer. Can you see why squaring the integral might help? I want you to sit with that question before we continue, because the answer is not obvious until you have looked at the shape of the problem from a fresh angle.

Let's call the integral I. Then I squared is the product of two copies of the same integral, one with the variable x and one with the variable y. Multiplying them out turns the single-variable problem into a double integral over the whole plane, with the integrand e to the minus x squared times e to the minus y squared. We can combine those exponentials into one, so the integrand becomes e to the minus the quantity x squared plus y squared.

Now the problem has become geometric, and that is the crucial shift. The exponent depends only on x squared plus y squared, which is the squared distance from the origin. Any function that depends only on distance is naturally described in polar coordinates, where the position is a radius r and an angle theta. In those coordinates, the tiny area element dx dy becomes r dr d theta, and the r factor is the thing that makes the whole calculation work.

So we rewrite I squared as an integral over the angle from zero to two pi and over the radius from zero to infinity. The integrand is e to the minus r squared, multiplied by r. Notice that nothing in the integrand depends on the angle, so the angular integral is just the full turn, which gives two pi. You can verify that with a quick sketch of a circle and a glance at the angle.

The radial integral is the one that rewards a little patience. Consider the integral of r times e to the minus r squared from zero to infinity. Substitute u equal to r squared, so that du equals two r dr, and the integral becomes one half times the integral of e to the minus u from zero to infinity. That integral equals one, so the radial part is one half. Multiplying the two pieces gives two pi times one half, which is simply pi.

So I squared equals pi, and therefore I equals the square root of pi, taking the positive root because the integrand is always positive. That is the Gaussian integral, and it is one of the most useful results in all of mathematics. It shows up in probability, in statistics, in physics, and in the normalization of the bell curve you meet everywhere. A surprising constant has appeared out of a problem that looked like it had no clean answer at all.

It is worth pausing on how unexpected this is. A bell curve has nothing obvious to do with a circle, and yet the constant that describes the circle is the one that normalizes the bell. When you first see that, it can feel like a coincidence. Once you understand the polar computation, you realize that the circle was secretly present all along, hidden inside the sum of two squares. You can take that as a general reminder: when a symmetric structure appears in a problem, expect circles, spheres, or other familiar shapes to show up nearby.

Look back at what happened here. The one-dimensional problem was stubborn because its antiderivative resisted every standard method. In two dimensions, the same function became a rotationally symmetric object, and symmetry is exactly the thing that polar coordinates expose. Adding a dimension did not make the calculation longer. It made the hidden structure visible, and that is the heart of the whole technique.

Think of it as looking at a sculpture from a different angle. From one side, the outline is confusing and no single view reveals the shape. From directly above, the form becomes obvious, with circular symmetry that you can exploit. You do not need to change the object at all, only the viewpoint, and the second dimension gives you that viewpoint for free.

I like to think of this as a small act of translation. The problem is written in one language, the language of single variables and their antiderivatives, and the solution is easier to state in another language, the language of geometry and symmetry. You translate the problem, solve it in the new language, and then translate the answer back. Many of the great techniques in mathematics follow this same pattern, and the second dimension is just one of the simplest dictionaries available.

Let's try a second example, one that connects to something you might already know. Imagine choosing a point uniformly at random inside a square of side length two, centered at the origin. What is the probability that the point lands inside the unit circle? The square has area four, and the circle has area pi. So the probability is pi over four, which is roughly 0.785. Here a two dimensional picture gives a direct meaning to pi, and no integral at all is needed to see it.

Why does that work? Because uniform random points in the square are equally likely everywhere, so the probability is simply the ratio of areas. The circle carves out a region whose area is pi, and the square's area is four. That ratio is a clean geometric fact, and it is available only because we have moved into two dimensions where both shapes live.

I want to emphasize how much this example depends on uniform randomness. If the points were clustered toward the center, the simple ratio of areas would no longer give the probability, and the calculation would need a weighting. The clean answer exists only because every point of the square is equally likely. That assumption is easy to forget, and it is worth checking every time you turn a geometric picture into a probability. If you tried to picture the same question on a line, there would be no circle to compare with.

Now let's push the idea one dimension higher, to a three dimensional ball. Suppose you want the volume of a unit ball. One way to organize the calculation is to slice the ball with horizontal planes. At height z, the cross section is a disk whose radius is the square root of one minus z squared, so its area is pi times one minus z squared. Stacking these thin disks from z equals minus one to z equals one gives an integral that evaluates to four pi over three.

That computation is a lovely example of thinking in layers. Each slice is a two dimensional problem that we already understand, and the third dimension is simply the direction along which we stack them. You can rebuild the whole volume from pieces that individually look like the circle problem we just solved. That is one of the most practical habits this technique teaches, because complicated shapes often decompose into simpler slices.

Notice also what the slicing did for us. We never had to imagine the whole ball at once. Instead we focused on one disk at a time, and each disk was a problem we had already solved. Breaking a hard object into easier pieces is a habit you can apply far beyond calculus, whether you are estimating a volume, planning a project, or reading a complicated proof. You will often find that the difficulty was never in the pieces, but in the way they were assembled.

Let me say what I think the general lesson is. Adding a dimension works best when it reveals a symmetry that was hidden in the original formulation. The Gaussian integral has rotational symmetry in the plane, and the ball has circular cross sections in space. Whenever a problem has such a symmetry, a new coordinate system can turn an intractable integral into a product of two simple ones, and you should always look for that opportunity.

But I want to be honest about the limits. The trick does not always help. If the function you are integrating has no symmetry to exploit, adding a variable can make the expression messier rather than cleaner, and you can end up with a double integral that is harder than the original single one. So the technique is not a universal key. It is a tool that rewards you for noticing the right structure, and noticing that structure is the real skill.

A useful test is to ask what symmetry you expect before you begin. If you can name a rotation, a reflection, or a scaling that leaves the problem unchanged, you have a candidate for a helpful coordinate system. If you cannot name one, you should be cautious, because the change of coordinates may simply trade one difficulty for another. Asking that question first saves a surprising amount of wasted effort.

The Gaussian integral also generalizes neatly. In n dimensions, the integral of e to the minus the squared length of a vector over all of n dimensional space equals the square root of pi, raised to the power n. The same polar-style reasoning works after you replace the circle with a sphere, and the answer comes from the same kind of computation. Seeing this pattern is a good reason to remember the trick rather than just the answer.

Some readers will be surprised that the same answer keeps returning in different guises. The point is not that every problem reduces to the Gaussian integral, but that the circle and the sphere give us reusable patterns. Once you have seen the trick in two dimensions, you can recognize it in three, and then in more dimensions than your intuition can easily hold. That recognition, more than any single formula, is the real payoff of studying the subject.

If you enjoy problems like these, I would recommend a simple exercise. Take the volume of a ball in four dimensions, and try slicing it by planes in the same spirit as the three dimensional case. You will need the volume of a three dimensional ball, which you have just computed, and you will see how the layers combine. Working through that yourself will teach you more than any summary I could offer.

So the message of this video is that dimension is not just a count of variables. It is a choice of viewpoint, and sometimes the right viewpoint makes a stubborn problem look simple. We added a dimension to the Gaussian integral and found the square root of pi. We added a dimension to a square and found pi over four. We stacked disks inside a ball and found four pi over three. In each case, the extra room gave the symmetry space to show itself.

Let me leave you with a question to carry into your own work. When you face a problem that refuses to yield, ask whether a second variable would reveal a symmetry that the first one hides. You may be surprised how often the answer is yes, and how much easier the next step becomes once you have changed the picture.
NARRATION>>>

```json
{
 "format_class": "toy integral, dimension-raising trick, geometric examples, caveat, coda",
 "answer_given_upfront": true,
 "hook_type": "premise-claim",
 "first_question_frac": 0.15,
 "first_concrete_object_frac": 0.03,
 "first_new_idea_frac": 0.08,
 "first_notation_frac": 0.20,
 "payoff_frac": 0.45,
 "misconception": "none",
 "brute_force_first": false,
 "examples_count": 4,
 "example_growth": "one integral -> square -> probability in a square -> ball",
 "roadmap": "none",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.15,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the squared distance from the origin, x squared plus y squared",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": false,
 "wpm": 190,
 "median_beat_s": 90,
 "beat_sequence": ["hook","toy-world","viewer-turn","derivation","definition","derivation","payoff","analogy","derivation","derivation","generalize","caveat","coda"],
 "top5_moves": ["toy-world","analogy","design-it-yourself","honest-caveat","generalize-to-other-domains"],
 "absent3_moves": ["act-it-out","failure-shown","inline-quiz"]
}
```

```json
{"verified_trace": {"wpm": "PASS 190.00 (target 182.6-197.1, median 190.32)", "you_rate": "FAIL 2.49 (target 1.6-2.44, median 2.1)", "i_rate": "PASS 0.70 (target 0.61-1.3, median 0.88)", "we_rate": "PASS 0.99 (target 0.82-1.61, median 1.04)", "num_rate": "FAIL 3.23 (target 1.45-2.36, median 1.79)", "hedge_rate": "PASS 0.30 (target 0.28-0.4, median 0.33)", "example_rate": "PASS 0.25 (target 0.19-0.33, median 0.27)", "q_rate": "PASS 0.15 (target 0.07-0.23, median 0.15)", "sent_len": "FAIL 17.49 (target 20.41-25.75, median 24.07)", "switch_sponsor": "PASS detected=False default=OFF", "switch_teaser": "PASS detected=False default=OFF", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (premise-claim vs premise-claim)", "ending_type": "MATCHES default (teaser-next vs teaser-next)", "summary": "6/9 numeric targets pass"}}
```
