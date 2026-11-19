channel: 3blue1brown
id: k7RM-ot2NWY
title: Linear combinations, span, and basis vectors | Chapter 2, Essence of linear algebra
duration: 599 s (9:59)
condition: base
recall: vague

## Content skeleton
- Two arrows on a grid as the starting picture; the question of which points you can reach by stretching and adding them.
- Linear combination defined as scaling each vector and adding, with scalars as the knobs.
- Span as the set of all reachable points: the whole plane for two arrows pointing different ways.
- The parallel case: a second arrow along the first adds nothing, and the span collapses to a line.
- Three vectors in 3D: full space, a plane, or a line depending on redundancy.
- Basis vectors i-hat and j-hat, coordinates as the recipe of scalars, notation written only after the picture.
- Teaser toward the next chapter on transforming the grid.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Question on screen: two arrows on a grid; which points can stretching and adding reach? |
| 0:35 | answer-statement | Almost the whole plane, provided the arrows point in genuinely different directions. |
| 1:15 | toy-world | Walk along the first arrow, then the second, with counts of steps as the knobs. |
| 2:20 | definition | A linear combination is scaled copies added together; the scalars are the numbers. |
| 3:10 | demo-sim | Two sliders; the arrow tip sweeps out a region of the grid as they move. |
| 4:30 | generalize | The reachable set has a name, the span; with two independent arrows it is the whole plane. |
| 5:20 | misconception-defuse | Parallel arrows reach only a line; the second arrow was already reachable. |
| 6:20 | wall | Three vectors in 3D: which combinations of redundancy collapse the span. |
| 7:10 | analogy | A recipe: vectors are ingredients, scalars are amounts, span is the set of dishes. |
| 8:10 | derivation | A basis is the minimal spanning set; i-hat and j-hat; coordinates written as scalars. |
| 9:00 | recap | Linear combination, span, basis: three definitions. |
| 9:30 | teaser | Next time: apply a transformation to the whole grid and watch the basis arrows move. |
| 9:50 | coda | Short sign-off. Ends at 9:59. |

## Narration
<<<NARRATION
Here are two arrows on a grid. One points right, and the other points up and to the right at a diagonal. Let's ask a simple question. If you are only allowed to stretch these arrows and add them together, which points can you land on?

You probably already have a feel for this. Stretching an arrow means making it longer or shorter, or flipping it around. Adding means placing one arrow at the tip of the other. Each combination of these two moves gives you a point. So the real question becomes how much of the plane those moves can cover. The short answer is almost all of it, as long as the arrows point in genuinely different directions. Let's see why.

Start at the origin. Walk along the first arrow, once forward. Then walk along the second arrow, twice forward. You end up somewhere. Now walk the first arrow backward by one, and the second arrow forward by three. You end up somewhere else. Every choice of how far to walk along each arrow lands you at a point, and different choices land you at different points.

That kind of expression has a name. It is called a linear combination. You take each vector, multiply it by a number, which is called a scalar, and then add up the results. If the first vector is v and the second is w, a combination looks like a times v, plus b times w, where a and b are any numbers you like. Nothing fancy is happening. You only scale and add.

Now let's move those scalars around. Imagine a slider for a and another for b. As you drag them, the tip of the resulting arrow sweeps across the grid. Drag only a, and the tip slides along a line through the origin in the direction of v. Drag only b, and the tip slides along a line in the direction of w. Drag both, and the tip can go to lots of places in between, filling out more and more of the plane.

Here is the key idea with a name attached. The set of all points you can reach with linear combinations of some vectors is called their span. So the span of v and w is every point you can get by choosing a and b. For these two arrows, pointing in different directions, the span is the entire plane. Every point on the grid is reachable, if you pick the right pair of numbers.

Now there is an important exception, and it is easy to miss. Suppose the second arrow lies along the first. Maybe it is just twice as long, pointing the same way. Then combining them doesn't open up new territory. Every combination still sits on that one line through the origin. The span is only a line, not the whole plane. The second arrow added nothing, because it was already reachable by stretching the first.

So the picture is not "two vectors give you the plane." The right statement is that two vectors give you the plane when they point in genuinely different directions, and only a line when they don't. A vector is redundant if you can already reach it using the others.

Let's push this up a dimension. Take three arrows in three-dimensional space. Their span is all the points reachable by combining them. If all three point in genuinely different directions in a way that cannot be flattened, you can reach every point in space. If one of them lies in the plane spanned by the other two, then the third adds nothing new, and the span collapses to a plane. If all three are parallel, you are stuck on a single line.

This is where I want to bring in an analogy. Think of a recipe with a few base ingredients. Each recipe is a list of amounts, one per ingredient. A combination of vectors is exactly that. The scalars are the amounts, and the vectors are the ingredients. The span is the set of all dishes you can make. If two ingredients are really the same ingredient in different quantities, adding the second one never makes a new dish. That is the parallel case. What you want is a set of ingredients that can make everything.

Now let's use that. The smallest set of vectors that spans the whole plane is called a basis. For the plane, that is any two vectors that are not parallel. There is a particularly convenient basis: the unit arrow pointing right, which people call i-hat, and the unit arrow pointing up, called j-hat. Every vector in the plane can be written as some number of i-hat plus some number of j-hat. Those two numbers are the coordinates of the vector.

Here is the notation, written only after the picture. If a vector is written as x comma y, what it really means is x times i-hat plus y times j-hat. The coordinates are not arbitrary. They are the recipe. A vector given as three comma minus two is three copies of the first basis arrow, minus two copies of the second.

Why does a basis matter? Because it is the minimal set you need. One vector cannot span the plane. In the plane, any three vectors always include some redundancy. A basis is exactly the sweet spot: enough vectors to reach everything, and none wasted. That is why it appears everywhere in this subject. It is how you describe a space efficiently. This matters in practice, too. If you want to solve a system of equations, the question is whether the coefficient vectors span the space of possible outputs. If they do, every target can be reached. If they don't, some targets are out of reach no matter how you choose the numbers. The span is the language for asking whether a system has a solution at all.

So here are the three ideas. A linear combination is scaling and adding. The span is everything such combinations can reach. A basis is a minimal set whose span is the whole space. Those three definitions are all you need before we move on.

Next time, we are going to apply a transformation to the whole grid. The basis arrows will move, and every point will move with them, carried along by the same recipe. Once you know that, the grid itself starts to tell a story.

Thanks for watching, and I will see you in the next one.
NARRATION>>>

## Slots
```json
{
 "format_class": "concept-first visual intro, definitions after the demo",
 "answer_given_upfront": true,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.01,
 "first_new_idea_frac": 0.06,
 "first_notation_frac": 0.23,
 "payoff_frac": 0.85,
 "misconception": "planted-myth-defused",
 "brute_force_first": false,
 "examples_count": 3,
 "example_growth": "two arrows -> parallel pair -> three arrows in 3D",
 "roadmap": "none",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": null,
 "caveat_type": "none",
 "recurring_anchor": "the two arrows on the grid, reused at every stage",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 165,
 "median_beat_s": 50,
 "beat_sequence": ["hook","answer-statement","toy-world","definition","demo-sim","generalize","misconception-defuse","wall","analogy","derivation","recap","teaser","coda"],
 "top5_moves": ["toy-world","simulation-as-argument","misconception-first","minimal-definition-then-refine","generalize-to-other-domains"],
 "absent3_moves": ["humor","story","failure-shown"]
}
```
