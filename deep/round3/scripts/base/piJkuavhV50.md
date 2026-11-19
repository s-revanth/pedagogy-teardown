channel: 3blue1brown
id: piJkuavhV50
title: Solving problems by adding a dimension
duration: 1782 s (29:42)
condition: base
recall: none

## Content skeleton
- A hard-looking flat problem where direct coordinates and integrals become a mess.
- Thesis: lift the problem into one more dimension, where a symmetry becomes visible, then project back.
- Shadow analogy: a flat shape is the projection of a solid, and the solid can be easier to reason about.
- Archimedes' sphere, cylinder, and double cone, compared slice by slice at each height.
- Cavalieri's principle: equal cross-sectional areas at every height give equal volumes; the sphere volume follows.
- Misconception cleared: lifting is not always harder; here the extra dimension removes the hardest step.
- Generalization to higher dimensions and to other fields where slicing helps.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | A flat figure on screen; question: is there a way to find its area without heavy algebra? |
| 1:00 | answer-statement | Yes: add a dimension, find the hidden symmetry, slice, and project back. |
| 1:30 | toy-world | The planar figure drawn with a circle inside and its boundary labeled. |
| 4:00 | brute-force | Set up coordinates and integrals; the algebra grows with each added boundary. |
| 7:00 | wall | The integral is correct but gives no reason for why the answer has its form. |
| 8:30 | analogy | A three-dimensional solid casts a flat shadow; lifting a flat problem means finding a solid whose slices are easy. |
| 11:00 | story-rung | Archimedes: a sphere inside a cylinder, with a double cone carved out of the cylinder. |
| 13:00 | demo-sim | Horizontal slices at each height: the sphere's ring and the cylinder-minus-cones ring have the same area. |
| 17:00 | derivation | Cavalieri's principle: equal slices at every height give equal volumes; compute the volume. |
| 21:00 | misconception-defuse | Lifting does not always make problems harder; here the extra dimension removes the hard step. |
| 22:30 | derivation | Project the three-dimensional argument back to the plane; the flat answer comes with its reason. |
| 26:00 | generalize | The same slicing works in four dimensions and beyond; a habit for other fields. |
| 28:00 | recap | Lift, find symmetry, slice, project. |
| 29:10 | coda | Return to the opening figure. Ends at 29:42. |

## Narration
<<<NARRATION
Here is a puzzle that looks like it should require a lot of algebra. Work in a flat plane. Draw a shape, and ask for its area. The obvious method is to set up coordinates, write an integral, and grind through the calculus until a number falls out. Sometimes that works. Often it becomes a mess of nested expressions, and the picture stops helping you. Is there a better way?

The answer is yes, and it is a little counterintuitive. Add a dimension. Lift the problem into three-dimensional space, where a symmetry you could not see in the plane becomes obvious. Then slice the three-dimensional object, and project the answer back down. The extra room is not a complication. It is where the structure lives.

Let's start with the flat version. Take a circle and ask for its area. You can cut it into thin vertical strips, each almost a rectangle, and add the areas of all the strips. That is the honest calculation. Write the strip height in terms of the horizontal position, set up the integral, and simplify. You can do it, but notice how much bookkeeping you need, and how little the picture tells you while you do it.

Let's try the brute-force route in earnest. Place the center at the origin, so the circle's equation is x squared plus y squared equals r squared. The height of a strip at position x is two times the square root of r squared minus x squared. Integrate that from negative r to r, and out comes pi r squared, but only after a substitution or a trig identity. Now change the shape a little. Add a second boundary, or a tilted cut, and the integral grows. The algebra becomes a wall, and you have no sense of why the answer should be what it is.

That is the wall. The integrals are correct, but they hide the reason. A slice of a disk with a formula for its height gives no hint about why pi appears, or why the number has the form it does. We need a view in which the answer is visible before the algebra.

Here is an analogy that helps. Think about the shadow a three-dimensional object casts on a wall. The shadow is a flat shape, and the flat shape can be surprisingly hard to describe directly. But if you know the object, you can figure out the shadow with ease. In the other direction, lifting a flat problem into three dimensions means finding a solid whose shadow is the flat shape you care about, and whose structure is easier to reason about. The shadow is the problem. The solid is the solution's home.

Let's see this with a real example, one that goes back to Archimedes. Take a sphere of radius r. Surround it with a cylinder of the same radius, and height two r, so the sphere just fits inside. Now carve a double cone out of the cylinder, with its tip at the center, and its bases at the top and bottom of the cylinder. What remains is a solid that looks like a cylinder with two cones removed.

Now slice everything horizontally, at a height h above the center. The sphere's cross-section is a circle of radius the square root of r squared minus h squared. Its area is pi times r squared minus h squared. Now look at the cylinder-minus-cones. At the same height, the cylinder's cross-section is a circle of radius r, and each cone's cross-section is a circle of radius h. The remaining region is a ring, with area pi r squared minus pi h squared. Those areas are equal, at every height.

That is the key move. If two solids have the same cross-sectional area at every height, then their volumes are equal. This principle is called Cavalieri's principle, and it does not require you to know the volume formula in advance. The sphere and the cylinder-minus-cones have equal slices everywhere, so they must have equal volume.

Now the payoff. The cylinder has volume pi r squared times two r, which is two pi r cubed. Each cone has volume one third pi r squared times r, which is one third pi r cubed, and there are two cones. Subtract, and the leftover is two pi r cubed minus two thirds pi r cubed, which is four thirds pi r cubed. That is the volume of the sphere. We found it by slicing a three-dimensional solid into flat pieces and comparing the pieces, not by solving a messy integral.

Pause here, if you like, and check the arithmetic yourself. The cylinder volume is base area times height. The cone volume is one third of base area times height. Two cones, subtracted from the cylinder, leave four thirds of pi r cubed. If you get something different, look at which cone's volume you counted twice.

Now the reverse view. The lift worked because the three-dimensional picture had a symmetry that the flat picture did not show. Each horizontal slice was a ring, and the rings matched. Adding a dimension gave us room to see the matching, and that visibility is what made the calculation short.

The misconception to clear up is that lifting always makes a problem harder. It makes some problems harder, because you have more to track. But here the extra dimension removed the hardest step, which was finding a clever way to add up strange shapes. The lift cost one extra variable, and it bought a clean comparison.

Now let's bring the answer back down to the plane. The sphere's cross-section at the middle height is a circle of radius r, the same size as the circle we started with. The slice tells us about the flat problem directly. Projecting the three-dimensional argument back to two dimensions gives a flat result with a clear reason behind it, rather than a number produced by an integral we don't understand. The answer returns to the plane, and it comes with its explanation attached.

We can push this further. The same slicing idea works in four dimensions, and beyond. A higher-dimensional ball can be compared with a higher-dimensional cylinder minus cones, and the slices again match. The principle does not depend on the number of dimensions. Whenever a problem is hard in one dimension, try lifting it, find a symmetry, and compare slices. That habit transfers to probability, to physics, and to many areas where direct computation is ugly.

Let me summarize. Lifting a problem into a higher dimension can reveal a symmetry hidden in the lower one. Slicing the higher object into cross-sections lets you compare volumes without solving a difficult integral. And projecting the answer back down gives the lower-dimensional result, with a reason attached.

So go back to the figure we started with. The shape that seemed to need heavy algebra has a home in three dimensions, where the answer is a comparison of rings. The trick was not cleverness with symbols. It was choosing a larger space in which the structure could be seen.

Thanks for watching.
NARRATION>>>

## Slots
```json
{
 "format_class": "flat puzzle lifted to 3D, Archimedes slices, projected back",
 "answer_given_upfront": true,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.03,
 "first_notation_frac": 0.13,
 "payoff_frac": 0.8,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "flat puzzle -> sliced sphere -> higher dimensions",
 "roadmap": "none",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": null,
 "caveat_type": "none",
 "recurring_anchor": "the horizontal slice at height h, reused at three points",
 "sponsor_frac": null,
 "ending_type": "hook-callback",
 "teaser": false,
 "wpm": 165,
 "median_beat_s": 135,
 "beat_sequence": ["hook","answer-statement","toy-world","brute-force","wall","analogy","story-rung","demo-sim","derivation","misconception-defuse","derivation","generalize","recap","coda"],
 "top5_moves": ["hook-question","brute-force-first","analogy","story","generalize-to-other-domains"],
 "absent3_moves": ["humor","running-character","failure-shown"]
}
```
