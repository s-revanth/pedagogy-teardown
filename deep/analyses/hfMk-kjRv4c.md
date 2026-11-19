# I Tried Coding a Neural Network to Identify Doodles (Sebastian Lague, 55 min)

## Arc
Personal hook and roadmap (0:15-2:28), invented fruit and decision boundary (2:28-5:25), repairs by failure: bias, hidden layers, activation, cost (5:25-14:54), gradient descent (14:54-21:39), speedups and calculus (21:57-38:09), tests on digits, fashion, doodles, colour images (39:20-53:58).

## Strongest moves
1. **Component as repair (5:25, 9:46, 12:48).** A hand-tuned boundary can only rotate, so bias is added. A third layer does nothing, so activation is added. Counting correct answers gives no signal, so cost is defined.
2. **Brute force before calculus (14:54, 20:24).** Nudge each weight and measure cost. It works but is slow, so calculus is motivated.
3. **Nudge then derive (15:31-26:15).** Slope by a tiny h first, then the exact derivative, with a caveat about not dividing by zero.
4. **Reuse in chain rule (32:18).** Weight 1 reuses the pieces from weight 2; "same thing in a different layer" lowers effort.
5. **Stress test (43:50, 46:51, 51:18).** Own drawings break the 97% model. Honest brittleness replaces a victory lap.

## Unusual
- Slider hand-training makes the learner feel the problem before automation.
- Ends on failure (53% on colour images) with a teaser, not a win.
- Humour ("maths jail", 25:40) lets him slow down without lecturing.

## Principle verdicts
Confirmed: 1, 2, 4, 5, 6, 7, 9, 10, 11. Partly: 3, 8, 12, 13. Principle 8: speech steady; idea rate slows during derivative expansions, then accelerates through datasets.

## Velocity implications
- Gate each concept on a visible failure.
- Provide slider-driven scenes for hand-tuning before any automation.
- Show the numerical nudge before the derivative.
- Attach a stress-test scene to finished models.
- Backprop section (33-38) is fast; a tutor should insert checks there.
