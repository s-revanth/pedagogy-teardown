# Header

- channel: Reducible
- id: Ty0JcR6Dvis
- title: FFT Example: Unraveling the Recursion
- duration: 458 s (7:38)
- condition: v1
- recall: none

## Content skeleton

- Opens on the question of getting the transform of four numbers with fewer than sixteen multiplications.
- Input 1, 2, 3, 4; omega is a fourth root of unity (minus i in this convention); powers cycle around the circle.
- Direct method gives 10, minus two plus two i, minus two, minus two minus two i.
- Even/odd split: two size-two transforms, (4, minus 2) and (6, minus 2), using omega squared equals the half-size omega.
- Glue step: outputs k and k plus two combine the halves with one twiddle multiplication; all four answers reproduced.
- Recursion bottoms out at size one; work recurrence gives N log N; example numbers for 1024.
- Caveats: sign convention, exact arithmetic here versus rounding in real signals, power-of-two sizes.
- Ends with a pause to compute one output by hand and a recap of split, solve, glue.

## Beat sheet

| m:ss | beat | what is said or shown |
|---|---|---|
| 0:00 | hook | Question: four numbers and a direct recipe of sixteen multiplications; is there less work for the same answer? |
| 0:20 | roadmap | Split into two smaller problems of the same kind, solve them, glue the answers back. |
| 0:35 | definition | Input one, two, three, four; omega for size four is minus i; its powers cycle through the circle. |
| 1:30 | brute-force | Each output is a weighted sum of the inputs with powers of omega; four outputs, sixteen multiplications. |
| 2:30 | demo-sim | Fill in all four direct outputs: ten, minus two plus two i, minus two, minus two minus two i. |
| 3:20 | derivation | Split by position: even list one and three; odd list two and four; omega squared equals the half-size omega. |
| 4:10 | derivation | Size-two transform of a and b is a plus b and a minus b: even gives four and minus two; odd gives six and minus two. |
| 5:00 | derivation | Glue step: output k is even plus omega to the k times odd; output k plus two subtracts that term. |
| 5:30 | demo-sim | Trace outputs zero through three through the glue step; each matches the direct answer. |
| 6:20 | generalize | Work recurrence: two half-size problems plus one pass gives n log n; 1024 is about a million direct versus about ten thousand. |
| 6:50 | caveat | Sign convention may flip to plus i; real signals bring rounding error and need power-of-two sizes or padding. |
| 7:10 | viewer-turn | Pause: compute output one from the even answers four and minus two and the odd answers six and minus two. |
| 7:25 | recap | Split by position, solve each half, glue with one multiplication per output, repeat until size one. |
| 7:32 | callback | Back to the four numbers: sixteen questions asked in smaller groups that share the work. Runs to 7:38. |

<<<NARRATION
Here's a question. Suppose you have four numbers and you want their discrete Fourier transform. The direct recipe takes sixteen multiplications. Is there a way to do less work and still get the same answer? Let's find out. We'll use real numbers, so you can check every step.

The plan is short. We split the problem into two smaller problems of the same kind, solve those, and then glue the answers back together.

Our input is the list one, two, three, four. The transform gives four outputs, one per frequency. Each output is a weighted sum of the inputs, where the weights are powers of a special number called omega. For four points, omega is a fourth root of unity. It's a point on the unit circle, and in this convention it equals minus i. Its powers go around the circle: one, minus i, minus one, i. That's all the notation we need for now.

Let's do the direct method first, so we know what the answers should be. Output zero adds up the inputs, and that gives ten. Output one weights the inputs by one, minus i, minus one, and i. That gives minus two plus two i. Output two alternates signs, which gives minus two. Output three is the conjugate of output one, so it's minus two minus two i. So the four answers are ten, minus two plus two i, minus two, and minus two minus two i.

Count the work. Four outputs, each a sum of four products. That's sixteen multiplications. The number of multiplications grows with the square of the input size. For four numbers that's fine. For a thousand numbers it's a real problem, and that's the reason we're looking for a shortcut.

Now the split. Take the inputs at even positions, which are one and three, and the inputs at odd positions, which are two and four. Call them the even list and the odd list. Here's the observation that makes this work. Omega for size four, squared, equals omega for size two. So the even and odd lists each need a transform of half the size, using the same kind of weights, just with fewer of them.

Let's do the size two transforms. For two numbers a and b, the transform is a plus b and a minus b. Check it with the even list. One plus three is four, and one minus three is minus two. So the even transform is four and minus two. For the odd list, two plus four is six, and two minus four is minus two. So the odd transform is six and minus two.

Those are the two half-size answers. Now we glue. For each output k from zero to one, we compute the even answer plus omega to the k times the odd answer. For output k plus two, we subtract that same term instead. That's the whole combining step.

Let's check output zero. Even zero plus odd zero is four plus six, which is ten. That matches the direct answer. Output two uses the same numbers with a minus sign. Four minus six is minus two. That matches too.

Output one is even one plus omega times odd one. Omega to the first power is minus i. Odd one is minus two, so minus i times minus two is two i. Add the even answer, minus two, and you get minus two plus two i. That matches the direct answer. Output three is even one minus the same term, which gives minus two minus two i. That matches as well.

So the glue step reproduced all four answers, starting from two half-size problems. Look at what changed. The multiplications by omega happen only in the combining step, and only one of them is a real multiplication. The rest are trivial. Each half-size transform did its own small job.

Now the recursion. A size two transform is itself a split. Its two halves are single numbers, and the transform of a single number is just the number itself. So the recursion bottoms out at size one, where there is nothing to do. Each level of splitting halves the size, and each level does one glue pass over all the numbers.

Here's the cost. Call the work for size n, T of n. It's two half-size problems, plus one glue pass of about n work. That gives T of n equals two times T of n over two, plus n. The depth of the recursion is the number of times you can halve n before reaching one, which is log base two of n. Each level costs about n, so the total is n log n.

Let's make it concrete. A transform of size one thousand twenty four done directly needs about a million multiplications. Using the split, the glue passes need about ten thousand operations. The gap grows as the sizes grow.

Before we go on, here's a check to do yourself. Take the even answers, four and minus two, and the odd answers, six and minus two, that we just computed. Use the glue step to compute output one by hand. If you get minus two plus two i, your arithmetic matches. Pause here if you want to do it.

Now a few caveats. The convention I used has omega equal to minus i. Many textbooks use plus i instead, which flips the sign of the imaginary parts, and the algorithm is identical. Second, I picked numbers where every step is exact. Real signals are long, and floating point arithmetic adds small rounding errors at each glue step. The algorithm is the same, but your output is approximate. And the clean split needs the size to be a power of two. Otherwise you pad with zeros or use a more general split.

Let's recap, since it's short. Split the input by position into two halves. Solve each half as a smaller transform of the same kind. Glue the answers back with one multiplication for each output. Repeat until the pieces are a single number. The four numbers we started with show every step.

And back to the four numbers, one, two, three, four. The direct method asked sixteen questions. The recursion asked the same questions in smaller groups, and the groups shared the work. That's why it's fast.

Thanks for watching.
NARRATION>>>

## Slots

```json
{
 "format_class": "worked numeric example, split-solve-glue recursion",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.0,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.08,
 "first_notation_frac": 0.2,
 "payoff_frac": 0.72,
 "misconception": "none",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "four points, then two halves, then 1024",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.94,
 "caveat_type": "approximation",
 "recurring_anchor": "the four input numbers one, two, three, four",
 "sponsor_frac": null,
 "ending_type": "hook-callback",
 "teaser": false,
 "wpm": 170,
 "median_beat_s": 30,
 "beat_sequence": ["hook", "roadmap", "definition", "brute-force", "demo-sim", "derivation", "generalize", "caveat", "viewer-turn", "recap", "callback"],
 "top5_moves": ["special-case-first", "brute-force-first", "visible-repetition", "inline-quiz", "honest-caveat"],
 "absent3_moves": ["hook-paradox", "story", "running-character"]
}
```
