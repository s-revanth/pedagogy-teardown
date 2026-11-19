# 3blue1brown: Solving problems by adding a dimension

- channel: 3blue1brown
- id: piJkuavhV50
- title: Solving problems by adding a dimension
- duration: 1782 s (29:42)
- condition: v1
- recall: none

## Content skeleton

- Hook: a flat packing puzzle that resists every attempt to find a clean answer.
- Roadmap: try the flat puzzle, name the move, lift to three dimensions, project back, check, and flag where lifting fails.
- Hand arrangements in the plane: each attempt is a special case with no reason to be optimal.
- The lift: the flat problem becomes a configuration with more symmetry, giving a countable structure and a bound.
- A classical example: volume of a sphere by slicing against a cylinder minus a double cone, with cross-sections that match at every height.
- Higher dimensions are a tool, not a curiosity; the hypersphere case keeps the algebra going past what can be drawn.
- Caveats: higher-dimensional pictures mislead (volume concentrates near the surface), and a lift can add freedom that a projection destroys.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | A flat packing puzzle with circles in a square. Try to find the clean answer. Every attempt looks almost right. |
| 0:50 | roadmap | Plan: the flat puzzle, the named move, a lift into three dimensions, a classical example, a higher-dimensional case, and a caveat. |
| 1:30 | toy-world | Circles placed in the square: a grid wastes corners, a staggered layout does better, sliding one circle trades one gap for another. |
| 3:10 | brute-force | Pause and try it yourself. By hand, the arrangements work but nothing tells you whether a better one exists. |
| 4:40 | wall | Flat problems have too few symmetries to organize the shapes. Nothing certifies an arrangement as optimal. |
| 5:40 | definition | The move named: when a planar problem is stuck, add a dimension and look for more symmetry. Then solve and project back. |
| 7:00 | derivation | Lift each circle to a sphere. The sphere is the most symmetric object in three dimensions, so the contacts can be counted. |
| 9:30 | demo-sim | Rotate the lifted picture and watch its projection onto the square. Find the angle where the flat pattern is clearest. |
| 11:30 | story-rung | Older geometers had only flat tools and wanted a volume. Slicing a sphere, a cylinder and a double cone at the same heights. |
| 14:00 | derivation | At every height the cylinder slice minus the cone slice equals the sphere slice. Equal slices give equal volumes. |
| 17:00 | demo-sim | Move a horizontal plane up through the shapes and watch the areas match at each height. The principle holds in any dimension. |
| 19:00 | misconception-defuse | Higher dimensions are weird and useless. The lift shows they are a tool that gives the problem room to show its structure. |
| 20:00 | generalize | Four dimensions: the same symmetry and slicing logic works for a hypersphere. The picture stops, the algebra keeps going. |
| 22:30 | caveat | Higher-dimensional pictures mislead. A ball's volume concentrates near its surface. Check the answer with algebra or a small case. |
| 23:30 | derivation | Back to the flat puzzle. The lifted count gives the answer, and the projection puts it back in the square, where it can be checked. |
| 26:00 | wall | Adding a dimension can add freedom too. Lifted solutions may not project to good flat ones. The lift needs the symmetry preserved. |
| 27:30 | recap | Lift, count or solve in the higher space, project back, check in the original setting. |
| 28:30 | callback | Back to the opening puzzle. The hopeless-looking packing now has one clear line of reasoning. Ends at 29:42. |

## Narration

<<<NARRATION
Here's a puzzle that looks like it has no clean solution. Take a square and put some circles inside, all the same size, touching the edges and each other as needed. Now ask: what's the largest number of circles you can fit? Or flip it: what's the smallest square you can pack a fixed set of circles into? Try it on paper. You'll find arrangements that work, and you'll find that none of them feels like the right one. Each attempt has a slightly different shape, and no obvious pattern takes over.

This is a common experience with flat problems. They're hard because two dimensions give you few symmetries to hold onto. Each arrangement is a special case with no clear structure. The main idea of this video is that there's a move that often rescues you: add a dimension. Put the problem in three dimensions, where the symmetry is richer, solve it there, and then project the answer back down. Sometimes the extra room makes the hard problem easy.

Here's the plan. We'll try the flat puzzle by hand and see where it stalls. Then we'll name the move, lift the problem into three dimensions, and use the symmetry of a sphere to get a clean count. We'll look at a classical example where a dimension was added to compute a volume, and see that the same logic works. We'll push one step further into higher dimensions, where the pictures become unreliable but the algebra stays honest. And at the end, we'll come back to the flat puzzle with the answer in hand. There's a caveat near the end: lifting a problem can also make it harder, and not every problem benefits.

Start with the flat puzzle. Place a few equal circles in a square, and try to fit as many as possible with no overlap. Try a grid first. A grid is neat, but it wastes space in the corners. Try a staggered pattern, where each row sits in the gaps of the row above. That's better. Now slide one circle to make room for another. Each move changes the packing, and each change helps in one place and hurts in another. You can get a good answer by trial and error, but you can't easily tell whether a better one exists.

Pause and try it yourself. Pick a number of circles and find the arrangement that fits the most in a square. You'll probably land on something that looks right, and you'll have no way to say whether it's the best.

That's the wall. Flat problems give you no reason to believe your arrangement is optimal, because there are too many shapes and too few symmetries to organize them.

So here's the move. Name it before using it. When a problem in a plane is stuck, add a dimension and look for a configuration with more symmetry. Then solve the higher-dimensional version, and project back. The name is simple: adding a dimension. The trick isn't magic. It's a reframing. You use the extra room to make the structure visible.

Let's apply it. Take the circles and lift each one into a sphere. Picture each circle as the equator of a sphere in three dimensions, or think of the centers as points on a surface. Now the packing problem in the plane becomes a packing in space. A sphere is the most symmetric object in three dimensions. Every direction looks the same. That symmetry means the contacts between neighbors come in a pattern you can count.

Look at the contacts. In the lifted picture, each sphere touches its neighbors in a way that looks identical from every direction. Count the touching pairs and you get a number that's constrained by the geometry. That count tells you something about how many pieces can share the same space, and it gives a bound the flat packing has to respect. You haven't solved the flat problem yet, but you've found a limit it must obey.

Now the slider. Rotate the three-dimensional picture, and watch the lifted arrangement project onto the flat square. The projection of a symmetric configuration is a flat arrangement, and as you rotate, the flat picture changes shape. Find the angle where the projection shows the clearest pattern, and you've found the arrangement the flat problem seems to want.

Now let's see the same move in an old, classic setting: computing the volume of a sphere. Ancient geometers had only flat tools, and they wanted a three-dimensional volume. The strategy was to slice. Take a sphere, a cylinder of the same height and radius, and a double cone with its tips at the center. Slice all three with a horizontal cut at the same height. The cross-section of the sphere is a disk, and its area depends on the height. Now compare: the cylinder's cross-section minus the double cone's cross-section gives exactly the same area as the sphere's cross-section, at every height.

That's a remarkable match. Since the slices match at every height, the volumes must match. So the volume of the sphere equals the volume of the cylinder minus the volume of the double cone. The cylinder and the cones are easy to compute, and the sphere's volume falls out.

Let's run the slices. Move a horizontal plane up through the shapes. At each height, the sphere's disk and the leftover from the cylinder and cones have the same area. The match holds at every height, not just one. That's the general principle: if two solids have equal cross-sections at every level, they have equal volumes. The principle works in any dimension.

A common belief to address here. People often think higher dimensions are weird and useless, something for physics or science fiction. But the lifting move shows the opposite. Higher dimensions are a tool. They give you more room to place a problem so its structure becomes obvious. It's the same mental move as adding a layer to a map so the roads line up.

Now let's push to four dimensions. The same lifting works for a hypersphere, a sphere in four-dimensional space. You can't draw it, but you can write its equations, and the symmetry argument is the same. Every direction looks alike, so the contact counts and the slicing logic carry over. The picture stops at three dimensions, but the algebra keeps going. That's the advantage of this approach: the reasoning doesn't need the picture.

And here's the caveat, which matters. Pictures in higher dimensions mislead. Intuition built from three dimensions doesn't always transfer. A ball in high dimensions has most of its volume concentrated near the surface, which surprises almost everyone. So when we lift a problem, we should check the answer with algebra or with a small case, not just with the picture. The lift gives you the right question. The algebra gives you the right answer.

Now back to the flat puzzle. We lifted the problem into three dimensions, used the sphere's symmetry to count contacts, and got a bound. Then we projected back. The arrangement that matches the bound is the answer to the flat problem, and it can be checked directly in the square. The lifted count and the flat count agree, and that agreement is the sign the lift worked.

But not every problem gets easier. Here's the wall in the other direction. Sometimes adding a dimension adds freedom too. The configurations in three dimensions are more numerous, so the lifted problem can have many solutions that don't project to good flat ones. You have to check that the projection keeps the structure you need. The lift helps when the symmetry survives the projection, and it doesn't help when the projection destroys it.

Let's recap the move in four steps. Lift the problem into a higher dimension where symmetry is easier to see. Solve or count there. Project the answer back down. Check it in the original setting. Each step is short, and the power is in the middle one: the extra room is where the structure lives.

Now return to the opening. We started with circles in a square and no clear answer. The lift gave us a count of contacts, the projection gave us an arrangement, and the check confirmed it in the flat square. The puzzle that looked hopeless is now one clear line of reasoning, and it became clear because we borrowed a dimension we didn't need.
NARRATION>>>

## Slots

```json
{
 "format_class": "lift-to-higher-dimension puzzle, classical volume detour, caveat",
 "answer_given_upfront": false,
 "hook_type": "paradox",
 "first_question_frac": 0.0,
 "first_concrete_object_frac": 0.05,
 "first_new_idea_frac": 0.19,
 "first_notation_frac": 0.24,
 "payoff_frac": 0.79,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "flat circles -> sphere volume -> four dimensions",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.11,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the circles and the square, returned to in the closing",
 "sponsor_frac": null,
 "ending_type": "hook-callback",
 "teaser": false,
 "wpm": 170,
 "median_beat_s": 90,
 "beat_sequence": ["hook","roadmap","toy-world","brute-force","wall","definition","derivation","demo-sim","story-rung","misconception-defuse","generalize","caveat","recap","callback"],
 "top5_moves": ["special-case-first","design-it-yourself","analogy","act-it-out","multiple-decompositions"],
 "absent3_moves": ["running-character","humor","rule-list"]
}
```
