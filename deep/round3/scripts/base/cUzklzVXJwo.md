# veritasium: How Imaginary Numbers Were Invented

- channel: veritasium
- id: cUzklzVXJwo
- title: How Imaginary Numbers Were Invented
- duration: 1409 s (23:29)
- condition: base
- recall: vague (topic-level only: Cardano, Bombelli, Descartes' label, the complex plane; no memory of this video's script)

## Content skeleton

- Opens on a puzzle: split 10 into two parts whose product is 40. Trial numbers all fall short.
- Setting up the quadratic and hitting the square root of a negative number.
- Cardano's 1545 *Ars Magna* and his cubic-solving method that sometimes needs negative square roots; he dismisses them but keeps computing.
- Bombelli's 1572 rules for the new quantities, and the cubic x^3 = 15x + 4 where the imaginary parts cancel to give 4.
- Descartes' 1637 label "imaginary", and why it stuck as a misleading name.
- Euler's letter i and the Wessel / Argand / Gauss picture of numbers on a plane, with multiplication by i as a quarter turn.
- Why they matter: alternating current, quantum mechanics; closing callback to the 10-into-two-parts puzzle.

## Beat sheet

| time | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Can you split 10 into two parts whose product is 40? Trial numbers fall short on screen |
| 1:00 | roadmap | Previews the path: the puzzle, Cardano, Bombelli, the plane, the uses |
| 1:30 | definition | Writes the puzzle as x(10 - x) = 40, then the quadratic, then sqrt(-15); the real-number wall |
| 3:00 | story-rung | 1545: Cardano's *Ars Magna* and his cubic method; he calls the quantities subtle and useless |
| 5:30 | derivation | Splitting 10 gives 5 plus or minus the square root of minus 15 |
| 7:30 | wall | The cubic x^3 = 15x + 4 has real root 4, but Cardano's formula needs sqrt(-121) |
| 10:00 | story-rung | 1572: Bombelli writes rules for "plus of minus" and "minus of minus" |
| 12:30 | derivation | Checks that (2 + i) cubed equals 2 + 11i, so the two cube roots sum to 4 |
| 14:30 | story-rung | Descartes labels them imaginary in 1637; Euler adopts the letter i |
| 16:30 | demo-sim | Plane picture: multiplying by i turns a point a quarter turn each time |
| 19:00 | generalize | Alternating current as rotation; quantum wave functions; Euler's identity |
| 21:00 | misconception-defuse | "Imaginary means fake" is a naming accident; they are as consistent as negatives |
| 22:40 | coda | Back to the 10-into-two-parts puzzle: five plus or minus i root fifteen |

<<<NARRATION
Try this. Can you split the number ten into two parts so that when you multiply them, you get forty? Take a moment. Five and five gives twenty-five. Six and four gives twenty-four. Seven and three gives twenty-one. The product keeps falling as the parts spread apart, and you never quite reach forty. It looks impossible. That small puzzle pushed mathematicians to invent a whole new kind of number.

Here's the plan. We'll start with the algebra that produces the puzzle, see how it grew into a much bigger problem about cubic equations, watch a mathematician named Bombelli make these strange quantities behave, and end with the way we now picture them, which makes them feel a lot less like a trick.

Let's write the puzzle as an equation. If one part is x, the other is ten minus x, and their product should be forty. So x times ten minus x equals forty. Rearranged, that's x squared minus ten x plus forty equals zero. The quadratic formula gives x equals five, plus or minus the square root of minus fifteen. There it is. You need the square root of a negative number.

In the ordinary real numbers, you can't take a square root of a negative. Any number you square comes out positive, or zero. So for centuries, people treated this as a dead end. The answer doesn't exist. Stop there, and that's the end of the story.

The story picks up in 1545, when Gerolamo Cardano published the *Ars Magna*, a huge book about solving equations. Cardano found a way to solve cubic equations, the ones with x cubed in them. His method had a strange feature. Sometimes it asked him to take square roots of negative numbers, even when the final answer was an ordinary real number. Cardano noticed this. He called these quantities subtle and useless, and he mostly wrote them off. But he kept computing with them anyway, because they seemed to work.

Then, in 1572, an engineer named Rafael Bombelli took the idea seriously. He wrote out rules for how these new quantities add and multiply. Plus times plus, minus times minus, and a new piece: a quantity whose square is minus one. He called the two kinds "plus of minus" and "minus of minus". Bombelli wasn't interested in philosophy. He wanted to solve a specific cubic: x cubed equals fifteen x plus four. You can guess the answer is four. Check it: four cubed is sixty-four, and fifteen times four plus four is also sixty-four. So four works. The trouble is that Cardano's formula for this equation seems to produce a mess. It asks for the cube root of two plus the square root of minus one hundred and twenty-one, plus the cube root of two minus that same quantity. That looks hopeless.

Bombelli noticed something. Suppose the cube root of two plus eleven i is two plus i, where i stands for the square root of minus one. Let's check. Two plus i, squared, is three plus four i. Multiply that by two plus i again. Three times two is six. Four i times i is minus four, so the real part is two. The imaginary terms are three i plus eight i, which gives eleven i. So two plus i, cubed, is two plus eleven i. Bingo. The other piece must be two minus i, and adding the two cube roots gives four. The imaginary parts cancel exactly, and you're left with the real answer. The strange numbers weren't noise. They were a route.

This is an important point, and it shows up often in the history of maths. Sometimes an idea is useful before anyone understands what it is. The square root of minus one was a tool that kept producing correct answers, and mathematicians were forced to take it seriously because of that.

But the name was a problem. In 1637, René Descartes wrote about these numbers and called them imaginary. He meant it more or less as a dismissal. The label stuck, and for two centuries the phrase imaginary number carried the suggestion that these numbers were fake, a pretend tool for getting real answers. It is a terrible name, and it has made the idea harder to understand ever since.

By the late 1700s, Leonhard Euler was writing the square root of minus one as the letter i and using it freely, and his notation became standard. The deeper change came when people asked what these numbers actually are. In the late 1700s and early 1800s, Caspar Wessel, Jean-Robert Argand and then Carl Friedrich Gauss saw that you could place these numbers on a plane. The real numbers run along a horizontal line. The i direction runs straight up. A complex number is a point on this plane, a location with two coordinates.

Now look at what multiplying by i does. Pick the point three comma zero, which is the real number three. Multiply it by i, and you get three i, the point zero comma three. You've moved the point ninety degrees counterclockwise. Multiply by i again, and you're at minus three. Another quarter turn takes you to minus three i. Four multiplications by i bring you back where you started. In this picture, multiplying by i is a rotation. That is what makes these numbers feel less like tricks and more like a natural part of how space and motion work.

That's why they show up everywhere. The alternating current in your home's wiring is a wave that rises and falls, and engineers describe its phase with complex numbers, so messy trigonometry becomes simple rotation. Quantum mechanics uses complex numbers at its foundation, in the wave functions that describe particles. Even the famous identity linking e, i, pi, one and zero comes from the same rotation idea.

So go back to the question at the start. Can you split ten into two parts whose product is forty? Yes, if you accept five plus or minus the square root of minus fifteen. Those parts are not on the number line you learned in school, but they are real in the sense that they follow consistent rules, solve real problems and describe real physical behaviour. The name imaginary is a leftover from a time when nobody knew where to put them. Now we know. They live on a plane, and they turn things around.

Check the answer one more time. Five plus i times the square root of fifteen, and five minus that, multiply to forty. You never saw those numbers on the number line, but you could have predicted them from the start. The question was never whether they exist. It was whether we were willing to look where they live.
NARRATION>>>

## Slots

```json
{
 "format_class": "proof-history tour with arithmetic checkpoints",
 "answer_given_upfront": true,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.01,
 "first_new_idea_frac": 0.07,
 "first_notation_frac": 0.08,
 "payoff_frac": 0.55,
 "misconception": "planted-myth-defused",
 "brute_force_first": false,
 "examples_count": 3,
 "example_growth": "split of 10 -> cubic -> rotations and circuits",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.03,
 "caveat_type": "historical-uncertainty",
 "recurring_anchor": "the split of 10 into two parts, recalled in the coda",
 "sponsor_frac": null,
 "ending_type": "hook-callback",
 "teaser": false,
 "wpm": 170,
 "median_beat_s": 120,
 "beat_sequence": ["hook","roadmap","definition","story-rung","derivation","wall","story-rung","derivation","story-rung","demo-sim","generalize","misconception-defuse","coda"],
 "top5_moves": ["hook-question","build-and-verify","story","simulation-as-argument","generalize-to-other-domains"],
 "absent3_moves": ["act-it-out","running-character","rule-list"]
}
```
