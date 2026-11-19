# 3blue1brown: How (and why) to raise e to the power of a matrix | DE6

- channel: 3blue1brown
- id: O85OWBJ2ayo
- title: How (and why) to raise e to the power of a matrix | DE6
- duration: 1627 s (27:07), band over10min
- condition: v2
- recall: none
- rulebook step 0: duration 27 min (>=10); series label (DE6, a differential-equations series); topic is math, a definition-then-payoff build; the title names an object (e to a matrix), not its result, and no formula appears in the first 40 s.
- class chosen: series part concept: question hook, scalar case, vector field toy world, power-series definition, term-by-term payoff, guess checkpoint on the rotation, diagonal and shear examples, convergence caveat, teaser
- exemplars read: deep/compact/r6sGWTCMz2k.txt (Fourier series, DE4, 25 min; read through about 9 KB, the opening and the first worked derivation, not the full file); deep/holdout/compact/d-o3eB9sfls.txt (Basel, 17 min; read in full for the geometric build and closing)

## Content skeleton
- Hook: e to the x is the function whose rate of change equals its value; what would e to a matrix mean?
- Scalar case: the rate of change equals a times x, solved by an exponential
- Matrix as a field of arrows: each point of the plane moves along its own arrow
- Naive element-wise exponential is the wrong instinct; a definition is needed
- Definition: the exponential power series with the matrix in place of x
- Payoff: term-by-term differentiation gives the matrix exponential solving the linear system
- Examples: rotation (a rotation back out, an exact constant-distance circle), diagonal (axis stretches), shear (the series stops after two terms)
- Caveats: convergence taken as given here; truncation is an approximation and computation is a craft
- Teaser: next, repeated eigenvalues and matrices that do not diagonalize

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Question: what would it mean to raise e to the power of a matrix? |
| 0:50 | toy-world | Scalar equation: rate of change equals a times x |
| 1:40 | toy-world | Matrix as a field of arrows over the plane |
| 2:30 | demo-sim | Flow of the plane under the matrix; points carried along arrows |
| 3:20 | definition | Scalar exponential series: one, x, x squared over two factorial, and so on |
| 4:20 | definition | Same series with the matrix in place of x; identity plays one |
| 5:20 | definition | Naive element-wise exponential rejected; a definition must do the job |
| 6:40 | caveat | Convergence taken as given for matrices; proof deferred |
| 7:50 | derivation | Differentiate term by term; the derivative equals A times the exponential |
| 9:40 | derivation | Solution of the linear system: position at time t is the exponential applied to the start |
| 11:20 | payoff | The definition has the property the system needs; the solution fell out |
| 12:20 | viewer-turn | Guess: a rotation matrix moves a point in a circle, a spiral, or a collapse? |
| 13:30 | payoff | Rotation exponential is a rotation by an angle proportional to time |
| 15:00 | demo-sim | Diagonal matrix: stretch along each axis, each by its own exponential |
| 16:30 | demo-sim | Shear: the square is zero, so the series stops after two terms |
| 18:20 | caveat | Truncation gives approximations; numerical methods are a separate craft |
| 20:10 | generalize | One definition covers all linear systems of this kind |
| 21:40 | generalize | Rotations, stretches and shears under one rule |
| 23:00 | teaser | Next: repeated eigenvalues and matrices that do not diagonalize |
| 25:00 | coda | Closing image of the series revealing structure |
| 27:07 | end | Stop |

<<<NARRATION
You probably know that e to the x is special. It is the function whose rate of change equals its own value, and it is the engine behind continuous growth. So here is a question that sounds almost like nonsense. What would it mean to raise e to the power of a matrix?

Start with something we already understand. Take a single number a, and consider the equation that says the rate of change of a quantity x equals a times x. Its solution is an exponential, growing or decaying at a rate set by a. That feature, growth proportional to the current amount, is why exponentials show up in populations and in bank accounts.

Now let the situation be richer. Instead of one number changing, imagine a point in the plane that moves, and whose velocity depends on where it is. The rule that says how velocity depends on position can be a matrix. Each matrix defines a field of arrows, one arrow at every point, telling you which way a point there should move and how fast.

This is a picture you can see. Give the matrix its values, and every point of the plane gets carried along its own arrow. The question is simple to state. If you start at a particular point, where are you after time t? If the matrix were just a number, the answer would be e to that number times t. So the natural guess is that the answer for a matrix should involve e raised to a matrix times t. But what could that possibly mean?

You cannot just take e to the power of each entry of the matrix and call it done. That is the wrong instinct, and it gives you a matrix that does not solve the equation. So we need a definition, and it has to be a good one. We start from the infinite series for the ordinary exponential. e to the x is one, plus x, plus x squared over two factorial, plus x cubed over three factorial, and so on forever.

Every term in that series is a power of x times a number. Powers of a matrix make perfect sense, because you can multiply a matrix by itself. So we define e to the matrix A as the same series with A in place of x. The identity matrix plays the role of one. You add A, then A squared over two factorial, then A cubed over three factorial, and keep going.

Does this infinite sum settle down for every matrix? For ordinary numbers the exponential series converges for every x, and for matrices the same thing holds. I am going to take that as given here rather than prove it. The proof matters less than the payoff, which is what this definition does to the differential equation.

Here's the payoff. Consider e to the A t, and ask how its rate of change behaves as t changes. Differentiate the series term by term. Each derivative shifts the powers down by one, and the result is that the derivative of e to the A t equals A times e to the A t. It satisfies the same equation as the scalar case, with the matrix standing where the number a stood.

So the matrix exponential solves the system. If x is a point whose velocity is A times x, then its position at time t is e to the A t applied to the starting point. We did not guess this. We defined the exponential so that it has exactly the property the system needs, and the solution fell out.

Before the examples, make a guess, because the central move is easier to see once you commit. Suppose the matrix is a rotation, one that turns every vector by the same angle. Starting from a point, what happens over time? Does it circle the origin at a constant distance, spiral outward, or slide in toward the center? Pick one.

The rotation case is the nice one. Its exponential turns out to be a rotation too, by an angle proportional to time. The point circles the origin at constant distance. It does not spiral out and it does not collapse, because a rotation preserves length. You can check this with the series, and the pattern of terms rebuilds the cosine and sine you expected, which is a reassuring sign that the definition is doing the right thing.

Now the diagonal case, which is the easy one. If A has numbers only on its diagonal, its powers are simple. Each diagonal entry is raised to the power on its own, and the exponential becomes a stretch along each axis, scaled by its own exponential. That is a good sanity check. The rotation was the example where something new happened, and the diagonal is where the new thing is easy to see.

The shear is the last example, and it shows where the series earns its keep. Take a matrix that slides one axis sideways. Its square is zero, so the series stops after two terms. The exponential is a shear whose amount grows with time, and you can read that straight off the series without any clever algebra. Here the series is not only a numerical tool. It gives the answer.

Now a caveat, because I don't want you to think computing these by hand is always easy. In practice you truncate the series. Keep too few terms and your answer is only an approximation. Keep many and it becomes accurate, but expensive for large matrices. Real numerical methods are cleverer than adding terms, and that is a whole craft of its own. The definition is solid. The computation is a separate job.

The solutions of linear systems of differential equations are all given by this matrix exponential, and that single definition covers rotations, stretches, and shears under one rule. Nothing about the rule depends on the particular matrix. That is why it is worth the detour through an infinite series.

In the next video I want to look at what happens when the matrix is not nice enough to diagonalize, and what the exponential does with repeated eigenvalues. That is where the picture gets stranger, and where the series starts to reveal structure you did not see coming.
NARRATION>>>

```json
{
 "format_class": "series part concept: question hook, scalar case, vector-field toy world, power-series definition, term-by-term payoff, guess checkpoint, rotation diagonal shear examples, convergence caveat, teaser",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.0,
 "first_concrete_object_frac": 0.03,
 "first_new_idea_frac": 0.05,
 "first_notation_frac": 0.06,
 "payoff_frac": 0.7,
 "misconception": "none",
 "brute_force_first": false,
 "examples_count": 3,
 "example_growth": "diagonal -> rotation -> shear",
 "roadmap": "none",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.46,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the flow picture of the matrix, redrawn in each example",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 180,
 "median_beat_s": 58,
 "beat_sequence": ["hook","toy-world","demo-sim","definition","caveat","derivation","payoff","viewer-turn","payoff","demo-sim","caveat","generalize","teaser","coda"],
 "top5_moves": ["hook-question","minimal-definition-then-refine","notation-after-concept","simulation-as-argument","generalize-to-other-domains"],
 "absent3_moves": ["humor","running-character","rule-list"]
}
```

```json
{"rule_trace": {
"U1": "applied: series part (DE6) sets the format gate: definition-then-payoff arc; no roadmap, recap or callback",
"U2": "n/a: title names an object; no formula or result is stated in the first 40 s; definition begins at 3:20",
"U3": "applied: closes on teaser-next, which a series part allows; no callback, no phrase mirror",
"U4": "applied: the flow picture of the matrix returns in the rotation, diagonal and shear examples",
"U5": "applied: symbols come after the scalar picture; e to the A t is tied to the flow on screen",
"U6": "broken: beat rows average about 58 s, above the 15-30 s guidance; table condensed for a 27-minute runtime; pace held at the 180 wpm target",
"U7": "applied: no roadmap, vote or commit prompt; no planted misconception",
"U8": "applied: domain caveat on convergence taken as given, and on truncation as approximation at 18:20",
"U9": "applied: rotation guess (circle, spiral, or collapse) at 12:20, 46 percent of runtime, answered at 13:30",
"U10": "n/a: no history-of-invention ladder",
"U11": "n/a: title names an object, not an application or trigger event",
"C1": "n/a: 27 min, above the 10-minute threshold",
"C2": "applied: the claim that the exponential solves the system is followed by the term-by-term derivative within about 100 s (7:50-9:40)",
"C3": "n/a: no iterated construction taken to a limit",
"C4": "n/a: no awe-objection-algebra sequence",
"C5": "n/a: single guess, not a rising ladder",
"D1": "applied: no roadmap; the caveat comes mid-video, not up front",
"D2": "applied: the naive element-wise exponential is rejected, not shown as a default route",
"D3": "applied: the definition is posed as a design question (what must e to A satisfy?) before the series is given",
"D4": "applied: notation follows the scalar picture and the flow picture",
"D5": "applied: teaser only, as a series allows; no callback to the hook",
"N1": "n/a: over-10-minute video",
"N2": "applied: delivery target 180 wpm, the band median; text cannot verify pace",
"N3": "broken: measured 1.61 per 100 words (N-median 2.05, p25-p75 1.62-2.5), outside the band",
"N4": "broken: measured 0.28 per 100 words (N-median 0.93, p25-p75 0.62-1.34), outside the band",
"N5": "broken: measured 0.57 per 100 words (N-median 1.02, p25-p75 0.71-1.58), outside the band",
"N6": "applied: measured 1.71 per 100 words (N-median 2.49, p25-p75 1.62-3.7), inside the band",
"N7": "broken: measured 0.57 per 100 words (N-median 0.21, p25-p75 0.12-0.3), outside the band",
"N8": "broken: measured 14.1 per 100 words (N-median 24, p25-p75 22-27), outside the band",
"N9": "applied: measured 0.38 per 100 words (N-median 0.33, p25-p75 0.22-0.44), inside the band",
"N10": "broken: measured 0.38 per 100 words (N-median 0.26, p25-p75 0.16-0.34), outside the band",
"B1": "applied: no sponsor read",
"B2": "applied: teaser allowed by U3 because the video is a series part",
"B3": "applied: no spoken roadmap",
"B4": "applied: no spoken recap; the closing paragraphs are a coda and a teaser"
}}
```
