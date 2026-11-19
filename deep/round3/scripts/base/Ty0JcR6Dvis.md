# Header
- channel: Reducible
- id: Ty0JcR6Dvis
- title: FFT Example: Unraveling the Recursion
- duration: 458 s (7:38)
- condition: base
- recall: none

# Content skeleton
- Hook: the discrete Fourier transform of a short list is a sum of products with complex roots of unity, which is slow to do naively.
- Worked example: four numbers, 1, 2, 3, 4, computed by the direct formula.
- Split: separate even-indexed and odd-indexed entries, each a half-size transform.
- Base case: a transform of two numbers is just a sum and a difference.
- Combine: each output is the even result plus or minus a twiddle factor times the odd result.
- Recursion tree and leaf order (bit-reversed indices); total cost N log N against N squared; ends with the general recursion.

# Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Four numbers, one two three four; find how much of each frequency is inside |
| 0:35 | toy-world | List drawn as four boxes with values |
| 1:05 | definition | DFT formula: multiply by a rotating complex wave and add, once per output |
| 1:50 | brute-force | Direct computation: sixteen multiplications for four numbers |
| 2:40 | wall | Doubling the length quadruples the work; the naive cost is N squared |
| 3:10 | derivation | Split the list into evens (1, 3) and odds (2, 4) |
| 3:50 | derivation | Two-number transform: sum and difference; evens give 4, -2; odds give 6, -2 |
| 4:40 | definition | Twiddle factor: minus i for length four, the step that rotates the odd half |
| 5:10 | demo-sim | Combine: X0 = 4 + 6 = 10, X2 = 4 - 6 = -2; X1 and X3 from the rotated odd result |
| 5:50 | derivation | Recursion tree: leaves end up in the order 1, 3, 2, 4 |
| 6:30 | generalize | Each level does about N work; ten levels for 1,024 points, roughly ten thousand operations, not a million |
| 7:00 | recap | Recursion reuses the half-size work; the trick is reuse, not magic |
| 7:30 | coda | End with the four outputs and the general pattern |
| 7:38 | coda | End |

# Narration
<<<NARRATION
Here is a list of four numbers: one, two, three, four. We want to transform it, which means finding how much of each frequency is hiding inside. The formula says to take each number, multiply it by a rotating complex wave, and add everything up. Do that once for every output, and you have a complete answer. For four numbers, that is sixteen multiplications. Let's see whether we can do better by splitting the problem in half.

First, the direct way, so we have something to compare against. The transform has one output for each frequency. For output zero, the waves do not rotate at all, so you just add the numbers, and you get ten. For the other outputs, each number gets multiplied by a complex root of unity, a point on the unit circle at a particular angle. For four points, those angles are multiples of a quarter turn. So the multipliers are one, minus i, minus one, and i. Work through the sums carefully and you get ten, minus two plus two i, minus two, and minus two minus two i.

That works, and it took sixteen multiplications. The trouble is that the cost grows with the square of the length. Double the list and the work quadruples. For a list of a thousand points, that is about a million multiplications. For the signals we really care about, that is far too slow. So the question is whether the work can be reused.

Here is the idea. Split the list into two halves. Take the entries at even positions, which are one and three. Then take the entries at odd positions, which are two and four. Each half is a smaller list, and each half needs its own transform. The even half and the odd half together give you the information you need to rebuild the full transform. This is the step that makes the whole method work.

Now look at the smallest case, a transform of two numbers. It is almost trivial. If the two numbers are a and b, the two outputs are just their sum and their difference. So the even half, one and three, gives a sum of four and a difference of minus two. The odd half, two and four, gives a sum of six and a difference of minus two. Those are the two smaller transforms, and each one took just one addition and one subtraction.

Now we have to combine them back into the full answer. This is where the twiddle factor comes in. For a list of length four, the twiddle factor is minus i. It is the rotation that shifts the odd half into the right place relative to the even half. Every output is one of two combinations. You take the even result and add the rotated odd result, or you take the even result and subtract the rotated odd result.

Let's check that with actual numbers. For output zero, there is no rotation, because the twiddle factor to the power zero is one. So output zero is four plus six, which is ten. That matches the direct computation. Output two uses the same two pieces but subtracts instead. Four minus six is minus two. Again, that matches. For output one, the rotation matters. The twiddle factor to the power one is minus i. Multiply minus two by minus i and you get two i. Add that to minus two and you get minus two plus two i. Subtract it and you get minus two minus two i. Both match the direct answers from before.

Notice what happened. We did not compute new multiplications for the whole list. We reused the two small transforms twice, once with a plus and once with a minus. The even and odd halves were each computed once, and the combination step is cheap. Four outputs came out of two small transforms and a handful of extra operations.

Now let's unravel the recursion, because that is what the name means. Each time we split a list, we produce two smaller lists. Each of those splits again, if it still has more than one entry. Draw this as a tree. At the top is the full list of four. Below it are two lists of two. Below those are four lists of one. Each single entry is already its own transform, because the transform of one number is just that number. So the work happens on the way back up the tree, as the pieces combine.

There is a curious order to the leaves of that tree. If you read the single entries from left to right, you do not see the original order one, two, three, four. You see one, three, two, four. The reason is that each split pulls out the even positions first, and that pulls out the evens recursively. The leaves come out in an order where the binary form of each index is reversed. Zero is zero, one becomes two, two stays one, and three stays three. Those four numbers are the bit-reversed order. You do not need to memorise this. You only need to know that it is the natural pattern of repeated even and odd splitting, and that many implementations arrange the data this way from the start to avoid copying.

Now think about the cost. Each level of the tree does about N units of combining work, because every entry gets touched once when pieces are combined. The number of levels is the number of times you can halve the list, which is the logarithm of N. So the total work is about N times log N. For four points, that is about eight units, compared with sixteen multiplications directly. That gap sounds small, but it grows quickly. For a list of one thousand and twenty-four points, the direct method needs about a million multiplications, while the recursive method needs roughly ten thousand. That difference is the reason the method is so widely used.

Let's step back. The trick is not magic, and it is not some special property of the numbers. It is a recursion. Split the problem into two smaller versions of itself, solve each one, and combine the answers with a cheap step. The combining step is where the complex rotations happen, and the twiddle factors are just the fixed rotations needed to line the halves up.

So the next time you see a fast transform, look for this pattern. Find the even and odd halves. Find the base case. Find the combining rule. Once you can do the four-point example by hand, the larger versions are the same steps, repeated. That is what unraveling the recursion means in practice.
NARRATION>>>

# Slots
```json
{
 "format_class": "worked numeric example, answer stated then unpacked",
 "answer_given_upfront": true,
 "hook_type": "answer-stated",
 "first_question_frac": 0.02,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.08,
 "first_notation_frac": 0.15,
 "payoff_frac": 0.90,
 "misconception": "none",
 "brute_force_first": true,
 "examples_count": 2,
 "example_growth": "four numbers -> split into two-number halves -> bigger lists",
 "roadmap": "one-line",
 "viewer_turn": "none",
 "viewer_turn_frac": null,
 "caveat_type": "none",
 "recurring_anchor": "the list one two three four, reused at every level",
 "sponsor_frac": null,
 "ending_type": "phrase-mirror",
 "teaser": false,
 "wpm": 170,
 "median_beat_s": 35,
 "beat_sequence": ["hook", "toy-world", "definition", "brute-force", "wall", "derivation", "definition", "demo-sim", "derivation", "generalize", "recap", "coda"],
 "top5_moves": ["brute-force-first", "build-and-verify", "visible-repetition", "special-case-first", "minimal-definition-then-refine"],
 "absent3_moves": ["humor", "story", "expert-dialogue"]
}
```
