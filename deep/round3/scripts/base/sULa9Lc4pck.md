channel: 3blue1brown
id: sULa9Lc4pck
title: Triangle of Power
duration: 462 s (7:42)
condition: base
recall: none

## Content skeleton
- Exponentiation as one equation linking three pieces: base, exponent, result.
- Three possible "missing piece" questions, each with an inverse: roots for the base, logarithms for the exponent.
- Brute-force counting (doublings) to find an exponent before any formula.
- Contrast with addition and multiplication, which have only one kind of inverse because they are commutative.
- Log as turning the exponent into a ratio of logarithms; the link stated simply.
- Domain limits: negative bases and non-real answers need care.
- Open question about whether the next operation has its own three-corner triangle.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Question on screen: a to the b equals c; what if one of the three pieces is missing? |
| 0:40 | answer-statement | Three questions, and exponentiation has two inverses, not one. |
| 1:20 | roadmap | One line: set up the triangle, then go corner by corner. |
| 1:50 | toy-world | A triangle with base, exponent, and result at the corners, drawn with small numbers. |
| 2:50 | definition | Exponentiation as repeated multiplication: two to the fifth is thirty-two. |
| 3:40 | brute-force | Find the exponent of two that gives thirty-two by doubling; then guess the base for cube equal to twenty-seven. |
| 4:30 | wall | The exponent question has no clean algebraic route; counting or a name is needed. |
| 5:10 | analogy | Subtraction undoes addition and division undoes multiplication; both are symmetric. |
| 5:50 | derivation | Logarithm names the exponent, root names the base; the ratio of logs gives the exponent. |
| 6:40 | generalize | Check negative bases and where the answers stop being clean. |
| 7:10 | recap | Three corners, three questions, two named inverses. |
| 7:25 | coda | Open question: does the next operation have its own triangle? Ends at 7:42. |

## Narration
<<<NARRATION
You already know what it means to raise a number to a power. Two to the third is two times two times two, which is eight. Three pieces, the base, the exponent, and the result, are tied together by one equation. But there is a question hiding in that equation that most people never ask, and it turns out to be the whole story. What happens when one of the three pieces is missing?

Here is the short answer. Given any two of the three, you can ask for the third. That gives three questions. Two of them have names that you may have learned, and the third is the odd one out. That odd one out is exactly why exponentiation is more interesting than addition or multiplication.

Here is the plan. Let's set up the triangle, then go corner by corner. Put the three pieces at the three corners. One corner is the base, one is the exponent, and one is the result. The equation connects them, and each corner is the answer to a question built from the other two. Let's use the same small numbers so we can check ourselves.

Start with the familiar corner. Base and exponent are given. Two to the fifth is two times two times two times two times two, which is thirty-two. Finding the result is just repeated multiplication. Nothing new happens here, and that is the point. Multiplication has been doing this since childhood. Notice also that this direction is fully determined. Given the base and the exponent, there is exactly one result. That is what makes it a function, and it is why this corner needs no special name beyond the power itself.

Now move to a different corner. Suppose you know the base is two and the result is thirty-two, but you don't know the exponent. You are asking: how many times do I need to multiply two by itself to reach thirty-two? You can answer by counting. Two, four, eight, sixteen, thirty-two. That is five doublings, so the exponent is five. This is brute force, and it works beautifully here. But notice that you had to count. There was no formula you could write down that solved the question directly.

That name for the exponent is the logarithm. The logarithm of thirty-two in base two is five, because two to the fifth is thirty-two. In symbols, log base two of thirty-two equals five. The logarithm is exactly the tool for the question "what exponent?" It did not come from nowhere. It is the name we gave to the answer you found by counting.

Now the third corner. Suppose the exponent is three and the result is twenty-seven, but the base is missing. You are asking: what number, multiplied by itself three times, gives twenty-seven? This time you may guess three, check it, see that three cubed is twenty-seven, and be done. Here the answer is a root, specifically the cube root. The root is the name for the base question.

So far, two questions have clean names. The root answers for the base. The logarithm answers for the exponent. Those are the two inverses of exponentiation, and this is where the triangle stops being symmetric. The root has a second face, too. Suppose the exponent is two and the result is nine. The base could be three, but it could also be minus three, since minus three squared is also nine. So the base question can have two answers. That is an early hint that the corners do not all behave the same way.

Let's compare with addition and multiplication. Addition has one inverse, subtraction. If you know a plus b equals c, and you want a missing piece, subtraction handles either one, because addition is commutative. Two plus three and three plus two are the same. Multiplication is similar: division undoes multiplication, and the order of the factors doesn't matter.

Exponentiation breaks that symmetry. Two to the third is eight, but three to the second is nine. Swapping the base and the exponent changes the answer. So the question "what is the base?" and the question "what is the exponent?" are genuinely different questions, each with its own inverse. That is why the triangle has three corners and not one. A simple table makes the imbalance visible. Hold the base at two and vary the exponent: one, two, four, eight, sixteen, growing quickly. Hold the exponent at two and vary the base: one, four, nine, sixteen, growing more slowly, and in a way that is easy to misread. The same kind of operation, with two very different structures. Addition and multiplication never give you that kind of imbalance between their inputs.

Here is a derivation of the link, kept simple. If a to the b equals c, take the logarithm of both sides and use the rule that an exponent comes down in front. You get b times log a equals log c. So the exponent is the ratio of two logarithms. The logarithm is not an extra idea bolted on. It is a way of turning exponents into multiplication, and that turns the hardest corner into a division.

Now let's check whether the triangle is a general pattern or a quirk of positive whole numbers. Try a negative base. Negative one, squared, is positive one. Negative one to the one half is not a real number in the ordinary sense. So the triangle has edges where the answers stop being clean. The root corner needs care when the base is negative, and the logarithm corner needs care when the base is negative or zero. Those are honest limits, and they are the reason textbooks spend so long on the rules.

Here is a question to end on, and it is open. Once you have addition, multiplication, and exponentiation, each with its inverses, what would the next operation look like? Would it also have a triangle of three corners, with its own odd one out? I don't know the full answer, and the question is the part I want you to keep.

To sum up, the triangle has three corners: base, exponent, and result. Three questions, one for each missing piece. Two of them have the names roots and logarithms. The asymmetry between base and exponent is what makes exponentiation the interesting one. Thanks for watching.
NARRATION>>>

## Slots
```json
{
 "format_class": "triangle-of-relations explainer, inverses named then derived",
 "answer_given_upfront": true,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.09,
 "first_notation_frac": 0.02,
 "payoff_frac": 0.87,
 "misconception": "none",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "small whole numbers -> bigger powers -> negative bases",
 "roadmap": "one-line",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": null,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the three-corner triangle, shown at four points",
 "sponsor_frac": null,
 "ending_type": "open-question",
 "teaser": false,
 "wpm": 165,
 "median_beat_s": 40,
 "beat_sequence": ["hook","answer-statement","roadmap","toy-world","definition","brute-force","wall","analogy","derivation","generalize","recap","coda"],
 "top5_moves": ["hook-question","brute-force-first","minimal-definition-then-refine","analogy","generalize-to-other-domains"],
 "absent3_moves": ["humor","running-character","failure-shown"]
}
```
