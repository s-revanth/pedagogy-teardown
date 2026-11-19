# Reducible: The Fast Fourier Transform (FFT): Most Ingenious Algorithm Ever? (h7apO7q16V0)

## Structure arc
It opens with a frame: algorithms are either useful or beautiful, and the FFT is both (0:00-1:24). Then it reframes. The usual entry point needs DFT and frequency-domain background, so the video teaches through polynomial multiplication instead (1:24). The core is a plan with one missing part. Brute-force multiplication is O(d^2) (2:21). Switching to the value representation makes multiplication O(d) (6:03). That needs fast evaluation and fast interpolation, which the video calls the "magic box" (7:35). Evaluation takes about 15 minutes: naive attempt, +/- pairs, recursion, breakdown, complex roots, code. Interpolation comes last as a short twist (22:36-26:48). It closes with a recap of four ideas and then a call to action.

## Strongest moves
1. **Failure as stepping stone (12:29).** The presenter builds the +/- pairing recursion, claims O(n log n), then asks the viewer to find the flaw: squared values are all positive. The fix (complex numbers) is now needed rather than arbitrary.
2. **Constraint reverse-engineering (13:46-15:10).** For n=4 he writes down what the recursion requires and solves it: x1=1, x2^2=-1, so x2=i. Only after that does he say "fourth roots of unity," then omega notation at 16:35. The concept is derived, then named, then given a symbol.
3. **Special case ladder (8:44-10:51).** x^2 (even) shows the pairing, x^3 (odd) shows the sign flip, and then a general degree-5 polynomial gets split into even and odd parts. Visible repetition sets up the general split.
4. **Plan with a placeholder (6:55-7:49, revisited 22:22).** A three-step pipeline with one unknown box gives the whole video its roadmap, and the video comes back to it after each piece is solved.
5. **One-line diff punchline (26:19).** FFT and inverse FFT code appear side by side and only the omega line differs. "Inverse is the same" becomes something you can see.

## What's unusual
It moves the topic into a different home domain. The FFT is presented as an algebra-class problem, not a signal-processing tool, so frequency language never comes up. Both brute-force steps are labeled as "our old foe" returning (8:16), which makes the running cost argument feel like a running character. The proofs are deliberately skipped and handed off: invertibility at 5:22 and the inverse DFT at 24:10. Those caveats are honest, but there are real gaps at exactly the points where an expert would want rigor.

## Principle verdicts (brief)
Confirmed: 1, 2, 6, 7, 9, 10, 11, 13. Partly: 3, 5, 8, 12. Not observed: 4. There is no analogy, because the familiar domain does that job. On pace (8), the text density looks flat. The slowdown comes from the hand-worked n=4 case and an explicit "take your time" at 20:32, which fits the round-1 finding that the idea rate changes, not the speech rate.

## Velocity implications
- Represent a lesson as a pipeline with empty slots. The orchestrator fills one slot per segment and re-shows the pipeline after each.
- Make breakdowns their own scenes. Run the recursion visibly, let it fail at level two, and pause for the learner to diagnose.
- Gate notation in the learner model: introduce omega only after the learner has produced 1, -1, i, -i.
- Ghost hands should support code diffs side by side for "only this changed" reveals.
- Evals: flag any tool or symbol used without a stated reason it was chosen.
