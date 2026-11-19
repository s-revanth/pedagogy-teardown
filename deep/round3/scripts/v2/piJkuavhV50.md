# 3blue1brown: Solving problems by adding a dimension

- channel: 3blue1brown
- id: piJkuavhV50
- title: Solving problems by adding a dimension
- duration: 1782 s (29:42), band over10min
- condition: v2
- recall: none
- rulebook step 0: duration 29.7 min (>=10); no series label; topic is a problem-solving method in math; the title states a thesis (the method), so U2 applies.
- class chosen: method tour: method stated early with its exception, a concrete two-cylinder object, slices into flat pieces, a guess checkpoint, the worked volume, the symmetry lesson, a reframing, a sanity check, a coda
- exemplars read: deep/compact/OkmNXy7er84.txt (Putnam, 11 min: reframing by added structure, the reveal, the closing); deep/holdout/compact/d-o3eB9sfls.txt (Basel, 17 min: a lift with a worked-number setup and a geometric build)
- note: the video's real content is not known to me; the example is the classic Steinmetz solid, chosen to show lifting and slicing, and the method is generic

## Content skeleton
- Thesis stated early: when a 2D problem resists, add a third dimension, solve there, project back down
- Exception stated early: the lift only helps when the extra room carries a symmetry that matches the problem
- Concrete object: two perpendicular cylinders of equal radius and their shared solid
- Slicing: each horizontal slice is a square whose area is simple, so the stack gives the volume
- Guess checkpoint: what fraction of the enclosing cube the solid fills
- Answer: sixteen times r cubed over three, two thirds of the cube at radius one
- Reframing: when outcomes become equally likely by symmetry, a probability becomes a count
- Caveat: the lift helps only when the symmetry matches; sanity checks on scaling

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Opening: a hard 2D question can be easy in 3D |
| 0:40 | answer-statement | Thesis: lift to a bigger space, solve, project back down |
| 1:10 | caveat | Exception stated early: needs a matching symmetry |
| 1:40 | toy-world | Two crossing cylinders of equal radius |
| 2:30 | definition | The shared solid, named as a Steinmetz solid |
| 3:20 | derivation | Slice at a fixed height: a square whose side the walls set |
| 4:30 | derivation | Side and area of the slice in words; the curved boundary becomes flat pieces |
| 5:40 | derivation | Symmetry: one slice describes all of them; sum the stack |
| 6:50 | demo-sim | Stack of square slices built up on screen |
| 7:30 | viewer-turn | Guess: a quarter, a half, or two thirds of the cube? |
| 8:20 | payoff | Answer: sixteen times r cubed over three; two thirds at radius one |
| 9:40 | derivation | What the lift did: uniform cross sections make the volume a stack |
| 11:00 | generalize | The pattern: hidden symmetry visible in one more direction |
| 12:20 | demo-sim | Reframing example: fix pieces, random rest, equally likely outcomes |
| 14:00 | generalize | Why it works: the new space makes the cases look the same |
| 15:30 | demo-sim | Sanity checks: radius zero gives zero; double the radius, eight times the volume |
| 17:00 | caveat | Adding a dimension does not always help; match the symmetry |
| 18:30 | tangent | Other routes exist; the lift is one reliable route among several |
| 20:00 | generalize | Choosing the lift: ask what symmetry the bigger space gives |
| 21:30 | demo-sim | Second sanity check on a shape that scales in all directions |
| 23:00 | tangent | When the plane resists, look for the room where the structure shows |
| 25:00 | tangent | Slices and reframings as the two working tools |
| 27:00 | coda | Coda: a tangled arc becomes a stack of squares |
| 29:00 | coda | Closing line on finding the clean idea under the calculation |
| 29:42 | end | Stop |

<<<NARRATION
Here is a method that solves a surprising number of hard problems. When a question seems stuck in two dimensions, try adding a third. Lift the problem into a bigger space, where the structure becomes visible, solve it there, and then project the answer back down. Adding a dimension is not a detour. Sometimes it is the shortest route.

I want to be careful, though, because it does not always work. The trick depends on the extra room having a symmetry that matches the problem. If you add a dimension the problem does not respect, the lifted version can be just as messy as the original. So the first question to ask is not what happens if I add a dimension. It is what symmetry the bigger space gives me that the smaller one lacks.

Let's make this concrete. Take two cylinders of the same radius, one running along the x-axis and one running along the y-axis, and look at the solid they share. Each cylinder on its own is a simple tube. Together their intersection is a three-dimensional shape with the same radius in every direction. It is called a Steinmetz solid, and it has a surprisingly clean volume.

Why would a three-dimensional solid be simpler than the problem it encodes? Slice it. Cut the solid with a plane at a fixed height, and the cross section is a square. The sides of that square are set by the walls of the two cylinders, and their length depends on the height. Each slice is a square, and its area is easy to write down. The curved boundary becomes a stack of flat pieces.

The solid is symmetric, so one slice tells you about all of them. At a height x measured from the middle, the cross section is a square whose side is twice the square root of r squared minus x squared. So its area is four times r squared minus x squared. Adding up all those square slices, from one end of the solid to the other, gives the total volume.

Before I give you that total, take a guess. Suppose the radius is one. Then the solid fits inside a cube of side two, which has volume eight. What fraction of that cube do you think the Steinmetz solid fills? About a quarter? About a half? About two thirds? Pick one.

The volume of the intersection of two perpendicular cylinders of radius r is sixteen times r cubed over three. For radius one, that is sixteen thirds, about five and a third. Compared with the cube of volume eight, that is two thirds of the cube. The solid fills most of the cube, but not all of it.

Look at what the lift did. The solid's walls are curved in each direction, but the slices are flat, and the flat slices are simple. Symmetry in three dimensions made the cross sections uniform, and once the cross sections are uniform, the volume is just a stack. You never had to solve the curved boundary directly.

A useful test is whether the lifted picture is simpler to describe in words. If you can say what the slices look like in one sentence, the lift has probably helped. If each slice is itself a mess, the lift has only moved the mess somewhere else.

That is the general pattern. A problem in the plane often has a hidden symmetry that is only visible when the object is allowed to move in one more direction. The third dimension supplies room for a symmetry the plane does not have, and once the symmetry shows, the problem becomes a question about a stack of simple pieces.

Here is a second pattern, which is about reframing rather than slicing. Suppose you need the chance of some arrangement, and the arrangement depends on how a few random things line up. In the plane, the bookkeeping can be tangled. Lift the problem, fix some pieces, and let the rest be chosen at random. Often you will find that the outcomes are equally likely by symmetry, so the probability becomes a count of favourable cases over a known total.

Notice what that did. The problem did not get easier because the numbers changed. It got easier because the bigger space made every case look the same. That is the signature of a good lift. Before you compute anything, ask whether the new space makes the cases equal, or the pieces uniform, or the boundary flat.

Compare that with trying to solve the planar version directly. You would be tracking arcs, angles and overlaps all at once, and each small error would carry forward into the next step. The lifted version keeps that bookkeeping inside one symmetric picture, where each piece can be checked on its own.

Before you trust an answer, run a sanity check against a case you already understand. Set the radius to zero, and the volume goes to zero, which is what you should expect. Double the radius, and the volume goes up by a factor of eight, because the solid scales in all three directions. These checks do not prove the answer. They catch the errors that come from a careless setup, and they take a few seconds.

Sanity checks also help you choose between two competing lifts. If one lift gives an answer that fails the zero-radius test, drop it, even if its algebra looked cleaner. A method that breaks obvious cases is not telling you the truth about the hard case either.

When you meet a new hard problem, make a short list of the symmetries it has, then ask which of them a larger space would make visible. The list is often short, and one item on it is usually the whole solution.

Adding a dimension is not the only way to solve these problems. But it is one of the most reliable ways to find the clean idea underneath a messy calculation. A tangled arc can turn into a stack of squares, and a stack of squares is something you can add up.
NARRATION>>>

```json
{
 "format_class": "method tour: method and exception stated early, concrete two-cylinder object, slices into flat pieces, guess checkpoint, worked volume, symmetry lesson, reframing, sanity check, coda",
 "answer_given_upfront": true,
 "hook_type": "answer-stated",
 "first_question_frac": 0.02,
 "first_concrete_object_frac": 0.06,
 "first_new_idea_frac": 0.03,
 "first_notation_frac": null,
 "payoff_frac": 0.47,
 "misconception": "none",
 "brute_force_first": false,
 "examples_count": 3,
 "example_growth": "two cylinders -> stacked slices -> reframed probability",
 "roadmap": "none",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.42,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the square cross section at each height, reused four times",
 "sponsor_frac": null,
 "ending_type": "phrase-mirror",
 "teaser": false,
 "wpm": 180,
 "median_beat_s": 55,
 "beat_sequence": ["hook","answer-statement","caveat","toy-world","definition","derivation","demo-sim","viewer-turn","payoff","derivation","generalize","demo-sim","tangent","coda"],
 "top5_moves": ["special-case-first","design-it-yourself","visible-repetition","generalize-to-other-domains","honest-caveat"],
 "absent3_moves": ["humor","running-character","rule-list"]
}
```

```json
{"rule_trace": {
"U1": "n/a: 29.7 min, no series label, not first-person; math method, not psychology or devlog",
"U2": "applied: the title and the first 40 s state the method (the lift); the exception follows within 20 s at 1:10; the concrete object arrives by 1:40; the brute-force numerics, wall and staged misconception are skipped",
"U3": "applied: closes on a phrase mirror of the title, 'adding a dimension'; no callback, no teaser",
"U4": "applied: the square cross section at each height is reused four times, each pass adding a layer",
"U5": "applied: formulas are narrated in words after the slice picture; no symbols are needed",
"U6": "broken: beat rows average about 55 s, above the 15-30 s guidance; table condensed for a 30-minute runtime; pace held at the 180 wpm target",
"U7": "applied: no roadmap, vote or commit prompt in the hook; no planted misconception",
"U8": "applied: domain caveat that the lift needs a matching symmetry, at 1:10 and again at 17:00",
"U9": "applied: guess checkpoint (a quarter, a half, or two thirds) at 7:30, 42 percent of runtime, answered at 8:20",
"U10": "n/a: no history-of-invention ladder",
"U11": "n/a: title names a method, not an application or trigger event",
"C1": "n/a: 29.7 min, above the 10-minute threshold",
"C2": "applied: the volume claim is followed by the slice justification within about 100 s (6:50-8:20 region and the setup before it)",
"C3": "n/a: no iterated construction taken to a limit",
"C4": "n/a: no awe-objection-algebra sequence",
"C5": "n/a: a single guess, not a rising ladder",
"D1": "applied: no roadmap up front; the exception is stated early as a caveat on the method, not as a roadmap",
"D2": "applied: no brute-force numerics; the exact slice route is used",
"D3": "n/a: no wall; U2 skips it",
"D4": "n/a: no symbols; formulas narrated in words",
"D5": "n/a: no callback or teaser needed",
"N1": "n/a: over-10-minute video",
"N2": "applied: delivery target 180 wpm, the band median; text cannot verify pace",
"N3": "applied: measured 1.67 per 100 words (N-median 2.05, p25-p75 1.62-2.5), inside the band",
"N4": "broken: measured 0.39 per 100 words (N-median 0.93, p25-p75 0.62-1.34), outside the band",
"N5": "broken: measured 0.1 per 100 words (N-median 1.02, p25-p75 0.71-1.58), outside the band",
"N6": "applied: measured 3.63 per 100 words (N-median 2.49, p25-p75 1.62-3.7), inside the band",
"N7": "broken: measured 0.49 per 100 words (N-median 0.21, p25-p75 0.12-0.3), outside the band",
"N8": "broken: measured 14.0 per 100 words (N-median 24, p25-p75 22-27), outside the band",
"N9": "broken: measured 1.08 per 100 words (N-median 0.33, p25-p75 0.22-0.44), outside the band",
"N10": "broken: measured 0.39 per 100 words (N-median 0.26, p25-p75 0.16-0.34), outside the band",
"B1": "applied: no sponsor read",
"B2": "applied: no teaser; not a series video",
"B3": "applied: no spoken roadmap in the first 12 percent",
"B4": "applied: no spoken recap in the last 20 percent"
}}
```
