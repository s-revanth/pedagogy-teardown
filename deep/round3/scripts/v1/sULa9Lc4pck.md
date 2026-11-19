# 3blue1brown: Triangle of Power

- channel: 3blue1brown
- id: sULa9Lc4pck
- title: Triangle of Power
- duration: 462 s (7:42)
- condition: v1
- recall: none

## Content skeleton

- Hook: two to some power is eight; what is the power, and which operation finds it.
- Roadmap: three corners (base, exponent, result), three questions, a triangle as a memory aid with a caveat.
- A triangle diagram with the three quantities at the corners and an operation on each side.
- Brute-force guess-and-check works for small whole numbers and fails for a root-of-two exponent.
- Named operations: roots find the base, logarithms find the exponent; the inverse curves shown by flipping the axes.
- Defusing the belief that logarithms are a division button or only for big numbers.
- Generalization to any base (base ten for orders of magnitude, base e for growth); caveat on negative bases and the complex plane.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Two raised to some power gives eight. What is that power, and what operation finds it? |
| 0:30 | roadmap | Plan: three corners, three questions, guessing by hand, naming the operations. Caveat: the triangle is a memory aid. |
| 0:55 | toy-world | Triangle diagram: base at one corner, exponent at another, result at the third. Each side is one operation. |
| 1:50 | brute-force | Pause to find the missing exponent. Then guess and check: two squared is four, two cubed is eight. Works for small whole numbers. |
| 2:50 | wall | Try two to the power of root two. No whole number to guess. Guessing gives estimates, not a rule. |
| 3:40 | definition | Logarithm named for the missing exponent; root named for the missing base. Symbols written after the picture. |
| 4:40 | demo-sim | Slider on the exponent traces the exponential curve. Flip the axes and the logarithm curve appears as its inverse. |
| 5:30 | misconception-defuse | Belief that logs are a division button or only for big numbers. Logs answer a how-many-times question. |
| 6:10 | generalize | Any base: base ten for orders of magnitude, base e for continuous growth. The same triangle, only the base changes. |
| 6:45 | caveat | Positive base, not equal to one. Negative bases need the complex plane. The triangle is a memory aid, not a theorem. |
| 7:10 | callback | Back to eight and the power three: the triangle answered it. Now two to root two has a named answer. Ends at 7:42. |

## Narration

<<<NARRATION
Two to some power gives eight. What is that power? You probably found it in a moment: two times two times two, so three. That was easy because the answer is a whole number and the numbers are small. Now let's go bigger. What power of two gives you a thousand? And what if the power itself is not a whole number, but something between two and three?

Those questions have something in common. Each one asks you to undo part of a single expression. In every case you have three things: a base, an exponent, and a result. Two to the third is eight. The base is two, the exponent is three, and the result is eight. If you know any two of those, you can ask for the third. That's the subject of this video: the three questions you can ask, and the three operations that answer them.

Here's the plan. We'll set up a triangle that holds the three quantities at its corners. We'll try guessing the missing piece by hand, which works for small cases and fails for others. Then we'll name the operation for each question, and point out where the triangle needs a caveat. The triangle is a memory aid, not a theorem, and I'll say exactly why at the end.

Put the three quantities at the corners. The base sits at one corner. The exponent sits at a second corner. The result sits at the third. Each side of the triangle is one operation linking two corners. If you know the base and the exponent, you can compute the result along one side. If you know the base and the result, you have to undo the power along another side. And if you know the exponent and the result, you're asking a third question entirely. The triangle is a picture of which corner is missing.

Let's try the brute-force method. Two squared is four, two cubed is eight. So the exponent that takes base two to eight is three. Easy, because we only had to try a few numbers. For base two and result sixteen, we try four. For base ten and result one thousand, we try three. Each time the guess is a whole number, and we find it quickly.

But now try two raised to the power of root two. There's no whole number to guess here. You can estimate it by sandwiching: the exponent is between one and two, so the answer is between two and four. Refine the sandwich and you get closer, but guessing doesn't give you a rule. Brute force can find answers, but it can't tell you how to get them for any base and any result.

That's the wall. The guessing method runs out, and we need an operation that reads the missing corner directly.

Let's name the operations. When the base and result are known and you want the exponent, that's the logarithm. The logarithm of eight in base two is three. It answers the question: how many times do I multiply the base by itself to get the result? The notation writes the base as a subscript, applied to the result. The logarithm is the exponent. It's the corner you were missing.

When the exponent and the result are known and you want the base, that's a root. Two is the cube root of eight, because two cubed is eight. So each of the three corners has a matching operation. Power fills the result. Root finds the base. Logarithm finds the exponent. And here's a detail worth holding onto: logarithms and roots are not the same thing. They answer different questions, and mixing them up is one of the most common mistakes in this topic.

Let's make it concrete with the slider. Move the exponent and watch the result trace a curve, the exponential curve. Now flip the picture. Plot the exponent against the result, and the same curve appears reflected across the diagonal. The logarithm is exactly the inverse of the exponential, so the two curves on the triangle's sides are the same curve with the axes swapped.

Here's the misunderstanding worth defusing. Many people learn logarithms as a button that performs division, or as something that only happens to very big numbers. It's better to see them as the answer to a question about how many times you multiply. That question has a clear meaning even when the answer isn't a whole number. Two to the power of root two is an exponent you can now name, and its logarithm in base two is root two.

Now generalize. The triangle doesn't care which base you pick. Base ten gives you orders of magnitude, which is why logarithmic scales show up for earthquakes and sound. Base e, which is about two point seven, gives you continuous growth. In each case the same triangle is the picture, and only the base changes. That's why the picture is worth remembering. You learn the triangle once, and it works for any base.

Now the caveat. The triangle works cleanly when the base is positive and not equal to one. Those restrictions matter. If you try a negative base with a fractional exponent, the result leaves the real numbers, and the picture needs a bigger space, the complex plane, to make sense. And the triangle is a memory aid for the three questions. For this video, positive bases are the domain where the picture is honest.

So, back to the start. Two to some power is eight. The base is two, the result is eight, and the exponent is three. The triangle has three corners, three sides, and three operations. Each pair of corners answers the question for the third. Now you can ask the same question about two to the power of root two, and know exactly what kind of answer you're looking for.
NARRATION>>>

## Slots

```json
{
 "format_class": "three-corner diagram, guess then named operations, caveat",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.0,
 "first_concrete_object_frac": 0.0,
 "first_new_idea_frac": 0.12,
 "first_notation_frac": 0.48,
 "payoff_frac": 0.8,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "two cubed -> root two exponent -> any base",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.24,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the triangle with base, exponent and result at its corners",
 "sponsor_frac": null,
 "ending_type": "hook-callback",
 "teaser": false,
 "wpm": 170,
 "median_beat_s": 40,
 "beat_sequence": ["hook","roadmap","toy-world","brute-force","wall","definition","demo-sim","misconception-defuse","generalize","caveat","callback"],
 "top5_moves": ["toy-world","brute-force-first","minimal-definition-then-refine","notation-after-concept","honest-caveat"],
 "absent3_moves": ["humor","running-character","act-it-out"]
}
```
