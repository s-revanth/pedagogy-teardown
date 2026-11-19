# 3blue1brown: Linear combinations, span, and basis vectors | Chapter 2, Essence of linear algebra

- channel: 3blue1brown
- id: k7RM-ot2NWY
- title: Linear combinations, span, and basis vectors | Chapter 2, Essence of linear algebra
- duration: 599 s (9:59)
- condition: v1
- recall: vague

## Content skeleton

- Hook: two arrows on a grid, and the question of which points you can reach by stretching and adding them.
- Roadmap with a one-line caveat that the pictures are two-dimensional while the algebra is not.
- Vectors as arrows from the origin; coordinates read as a recipe along two default arrows.
- A brute-force sampling of combinations that scatter with no visible pattern.
- Linear combinations named; sliding the two scalars sweeps out the whole plane, which is the span.
- The wall: two parallel arrows collapse the span to a line; basis vectors defined as a minimal spanning set.
- Coordinates depend on the chosen basis while the point stays put; a brief 3D extension; a teaser about transformations.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Two arrows on a grid. If you can only stretch each one and add them, which points can you reach? |
| 0:35 | roadmap | Plan: arrows, scaling and adding, the reachable set, then the case that collapses it. Caveat: 2D drawings, algebra in any dimension. |
| 1:05 | toy-world | Vectors as arrows from the origin. A point read as steps along two default arrows, on a grid. |
| 2:10 | brute-force | Pause to guess where the points land. Then try many pairs of multiples by hand. The points scatter with no pattern. |
| 3:20 | definition | Linear combination named: scale each vector, then add. Scalars as the knobs. Notation written after the picture. |
| 4:20 | demo-sim | Sliders for the two scalars. Sweeping one traces a line; sweeping both fills the plane. The span is the whole plane. |
| 5:40 | wall | Two parallel arrows. Every combination lands on one line. The second arrow added nothing new. |
| 6:40 | definition | Span as the set of all reachable points. Basis as a minimal set that spans with no waste. |
| 7:50 | generalize | Three vectors in space: the span is a plane or all of space, depending on whether one sticks out. Count of independent directions. |
| 8:40 | caveat | The picture is 2D; the algebra is the same in any dimension. The default basis is a choice of labels, not of points. |
| 9:10 | recap | Linear combination, span, basis, one sentence each. |
| 9:35 | teaser | Next: transformations that move the whole grid at once while keeping lines straight, using the same two arrows. |

## Narration

<<<NARRATION
Start with two arrows on a grid. One points right, and one points up and to the right at an angle. Here's a question. Suppose you can only do two things with them: stretch an arrow by any amount, including flipping it around, and then add the results together. Which points can you reach?

Think about it before we answer. Here's the plan. We'll treat vectors as arrows, see what it means to scale and add them, collect everything we can reach, and then find the one situation where that collection collapses. There's also one honest caveat coming. Everything here is drawn in two dimensions. The algebra doesn't care how many dimensions you have, but my pictures can only show so much.

Let's set up the world. Each arrow starts at the origin, the point where the axes cross. Its tip tells you a point. Say the first arrow ends at the point three, one, and the second ends at one, two. Those coordinates are a shorthand for a recipe, and the recipe is what matters here. Move three steps along the first arrow and one step along the second, and you land at a point.

Now try the naive thing. Pick a few multiples. Take the first arrow twice and the second arrow once, and add them tip to tail. Look at where you land. Try a negative multiple of the first arrow plus a positive multiple of the second. Try half of one plus three times the other. Each time you get a point. A dozen of them scatter across the grid, and there's no pattern you can see yet. You could keep going all day and still not know the full answer.

That's the brute-force approach. It finds points, but it doesn't say which points are possible. We need a better way to talk about the process.

So let's name it. Scaling each arrow and adding the results is called a linear combination. Given two vectors, v and w, a linear combination is a times v plus b times w, where a and b are any numbers you like. The numbers a and b are scalars, and they're the knobs.

Watch what happens when you slide them. Fix b and sweep a from very negative to very positive. The landing point moves along a straight line. Now hold a fixed and sweep b. The landing point traces a second straight line, in a different direction. Sweep both at once, and the lines fill out a grid. Turn the knobs slowly and the grid covers the whole plane. Every point on the grid is a reachable point.

So here is the answer to the question. For these two arrows, the set of all reachable points is the entire plane. Mathematicians call this set the span. The span of two vectors is everything you can reach by taking linear combinations of them.

Now the wall. Suppose the second arrow points in exactly the same direction as the first, only twice as long. Sweep the knobs. Every combination lands on that single line. Sweeping a and b does nothing new. The grid collapses into a stripe, and the span is a line, not a plane.

Here's the reason. The second arrow added nothing new. It was already a stretched copy of the first, so any combination of the two is just a multiple of the first. The arrows are redundant.

This tells us what we need. A basis is a set of vectors that spans the whole space, and does so with no waste. Remove any one of them and you lose some reachable points. Two arrows in the plane that point in different directions form a basis for the plane. Two parallel arrows span only a line, so they aren't a basis for the plane at all.

Now notice the default. When we write a point as three, one, we're secretly using the standard basis: one unit to the right, and one unit up. Those are the arrows we call the basis vectors. But they aren't special. Any pair of arrows pointing in different directions gives a basis, and it gives different coordinates for the same point. The point stays put in space. The labels change with the basis. That's one of the most important lessons in this topic, and we'll use it again.

Let's move up one dimension, lightly. Take three arrows in space. If they all lie in a single plane and none of them is redundant within it, the span is that plane. If one of them sticks out of the plane, the span grows to fill all of space. So the count of independent directions decides the size of the span. The algebra here is exactly the same as in two dimensions. Only the pictures get harder to draw, which is the caveat I mentioned earlier.

Let's recap in three sentences. A linear combination scales vectors and adds them. The span is the set of everything you can reach that way. A basis is a minimal set that spans the space with no wasted arrows.

And here's a teaser for the next step. So far we've only moved points around. What happens when a rule moves the whole grid at once, bending and stretching every point in the same way while keeping the lines straight? Those rules are called linear transformations, and the two arrows we've been using will become the way to describe them.
NARRATION>>>

## Slots

```json
{
 "format_class": "arrows-to-span proof tour, hook question, collapse case, basis",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.33,
 "first_notation_frac": 0.38,
 "payoff_frac": 0.67,
 "misconception": "none",
 "brute_force_first": true,
 "examples_count": 4,
 "example_growth": "two arrows -> parallel pair -> three vectors",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.22,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the two default arrows, reused in every example",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 55,
 "beat_sequence": ["hook","roadmap","toy-world","brute-force","definition","demo-sim","wall","generalize","caveat","recap","teaser"],
 "top5_moves": ["toy-world","brute-force-first","notation-after-concept","special-case-first","teaser-next"],
 "absent3_moves": ["humor","running-character","rule-list"]
}
```
