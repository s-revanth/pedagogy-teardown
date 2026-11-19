# Header
- channel: 3blue1brown
- id: sULa9Lc4pck
- title: Triangle of Power
- duration: 462 s
- condition: v3
- recall: none (the title is ambiguous to me; the script takes the AC power-triangle reading, which is a standard right-triangle relation among real, reactive and apparent power)
- exemplars read: deep/corpus/compact/kjBOesZCoqc.txt, deep/corpus/compact/fNk_zzaMoSs.txt

## Content skeleton
- Claim up front: the power a wall outlet carries fits inside a right triangle.
- Toy world: 120 volts and 10 amps, apparent power 1200 volt-amperes, a phase lag of 60 degrees.
- Definitions: real power is apparent power times the cosine of the phase angle; reactive power uses the sine.
- Worked numbers: 600 watts real, about 1039 reactive, and the Pythagorean check.
- Consequence: the wires carry the apparent power, so a reactive load draws current without doing work.
- Power factor as the cosine, and the triangle collapsing or standing upright at the extremes.
- Power factor correction and the rotating triangle as the angle changes.
- Teaser: the complex-number view comes next.

## Beat sheet (about 1310 spoken words across 462 s)
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Premise: outlet power is not voltage times current, and the gap is a right triangle |
| 0:25 | toy-world | 120 volts and 10 amps on a line; apparent power 1200 |
| 0:55 | definition | Phase lag; apparent power as the product; in-step versus lagging |
| 1:30 | derivation | Cosine of 60 degrees is one half; real power 600 watts |
| 2:10 | derivation | Sine of 60 degrees; reactive power about 1039 |
| 2:40 | derivation | The three numbers together: 600, 1039, 1200 |
| 3:20 | payoff | Triangle: real leg, reactive leg, apparent hypotenuse; the Pythagorean check |
| 4:00 | misconception-defuse | Wires run hot although the device does less work than the current suggests |
| 4:35 | analogy | Power factor as the triangle seen from one angle |
| 5:00 | generalize | Ten degrees versus eighty degrees: the same apparent power hides different work |
| 5:40 | caveat | Rounded values; approximations in the sine and the sum |
| 6:10 | generalize | Power factor correction pulls the tall triangle flat |
| 6:50 | viewer-turn | Sketch the triangle and check the sides |
| 7:20 | teaser | The complex-number view of the same triangle comes next |

<<<NARRATION
Here is a claim that surprises most people who first meet alternating current: the power a wall outlet delivers is not simply voltage times current, and the gap between the two fits neatly inside a right triangle. Here we will build that triangle from scratch, and by the end you will see why electricians and engineers care about it so much.

Start with the familiar picture. Suppose a device is plugged into a standard outlet, and the voltage swings back and forth like a sine wave, so the current swings back and forth too. If those two waves line up perfectly, the device gets the full benefit of their product, which we call apparent power. So what does a shifted current actually cost us? That is the question that opens up the whole subject.

Take a concrete case. Imagine a line carrying 120 volts and 10 amps, measured in the usual root-mean-square sense, which gives an apparent power of 1200 volt-amperes. If the current and voltage are perfectly in step, all 1200 of those volt-amperes become useful work. But if the current lags behind by 60 degrees, the useful part drops, and the rest sloshes back and forth through the cycle without ever doing work on average.

Why does it drop by exactly that amount? Because the real power depends on the cosine of the phase angle. The cosine of 60 degrees is one half, so 1200 times one half gives 600 watts of real power. You can check this on any calculator in a few seconds, and I would encourage you to do so before going further, because the rest of the video depends on it.

The remaining portion is the reactive power, and it is tied to the sine of the same angle. For a lag of 60 degrees, the sine is about 0.866, so the reactive power is 1200 times 0.866, which comes out to roughly 1039 volt-amperes reactive. Notice what we now have. A real power of 600, a reactive power of about 1039, and an apparent power of 1200, and none of those three numbers is arbitrary.

Here is the triangle. Draw the real power as a horizontal leg, the reactive power as a vertical leg, and the apparent power as the hypotenuse. Then the Pythagorean theorem applies directly, so apparent squared equals real squared plus reactive squared. Check it with our numbers: 600 squared is 360,000, 1039 squared is about 1,079,000, and their sum is about 1,440,000, which is exactly 1200 squared.

Let's pause on why this is more than a neat coincidence. The triangle is a geometric statement about two perpendicular kinds of power. The horizontal part does real work, like heating a room or spinning a motor. The vertical part moves energy back and forth between the source and the load, and on average it delivers nothing. Yet both contribute to the current that the wires have to carry, and that is the crucial point.

This is exactly why the wires get hot even when the device seems to be doing less work than the current suggests. A utility has to supply the full apparent power, because the current flowing in the lines depends on the whole triangle and not only on its horizontal leg. A load with a large reactive part can draw a lot of current while delivering modest real power. Engineers capture this mismatch with a single number called the power factor, which is the ratio of real power to apparent power.

In our example, the power factor is 600 divided by 1200, which is 0.5. That is simply the cosine of 60 degrees, so the triangle and the power factor are the same idea seen from two angles. A power factor of one means the triangle has collapsed into a flat line with no vertical leg at all. A power factor near zero means the triangle is nearly all vertical, with lots of current and very little useful work.

I think this is where the title earns its keep. The triangle is one of those pictures that makes a formula feel inevitable. Once you can see the three sides, you do not need to memorize how they relate, because the shape forces the relationship on you. That is the same spirit as the Pythagorean theorem itself, applied to a problem that has nothing to do with triangles drawn on paper.

Let's look at what happens when the angle changes. If the current lags by a small angle, say 10 degrees, the triangle is nearly flat, the real power is almost the full apparent power, and the reactive power is small. If the lag grows to 80 degrees, the triangle stands almost upright, the real power shrinks toward nothing, and the wires still carry a heavy load. The same apparent power can hide wildly different amounts of useful work, depending on one angle.

Every number in this video has been rounded, so it is worth being honest about that. The sine of 60 degrees is really 0.8660 and a bit more, and the squares I quoted are approximate too. The final check still holds to within a few parts in ten thousand, which is good enough for engineering and good enough for understanding. The exact identity is what matters, and the rounding only affects the last digits.

Now a question that engineers actually face. What do you do about a triangle that is too tall? One common answer is to add a component that pushes back against the reactive part, so the vertical leg shrinks and the power factor climbs toward one. This is called power factor correction, and it lets the same wires deliver more useful energy without overheating. Many large buildings have such equipment quietly running in their basements.

To see the whole picture, imagine rotating the triangle as the angle changes. If the apparent power is fixed, the hypotenuse keeps the same length, while the two legs trade length back and forth. The corner where they meet stays a right angle no matter what the angle is, and that is the geometric heart of the whole subject. Everything else follows from that single fact about perpendicular sides.

Two more facts make the triangle even more useful. First, the reactive part is what puts the current and voltage out of step, so the triangle is really a picture of the phase relationship itself. Second, the same geometry works with complex numbers, where the real part and the imaginary part play the roles of the two legs. Engineers often write the apparent power as a single complex quantity, which packs the whole triangle into one object.

For now, sketch the triangle with 1200 as the hypotenuse and 60 degrees as the angle, and convince yourself that the legs come out as 600 and about 1039. Then try 80 degrees and watch how the picture changes. Doing this by hand is the fastest way to make the relationships feel solid rather than merely memorized.

In the next video, we will use complex numbers to turn this triangle into a single calculation, and we will see why the algebra behaves so cleanly.
NARRATION>>>

```json
{
 "format_class": "triangle build-up with worked numbers, engineering consequence, teaser",
 "answer_given_upfront": true,
 "hook_type": "premise-claim",
 "first_question_frac": 0.13,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.12,
 "first_notation_frac": 0.42,
 "payoff_frac": 0.44,
 "misconception": "mid-video-correction",
 "brute_force_first": false,
 "examples_count": 4,
 "example_growth": "one angle -> ten degrees -> eighty degrees -> correction",
 "roadmap": "none",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.95,
 "caveat_type": "approximation",
 "recurring_anchor": "the right triangle with real and reactive legs",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 33,
 "beat_sequence": ["hook","toy-world","definition","derivation","payoff","misconception-defuse","analogy","generalize","caveat","viewer-turn","teaser"],
 "top5_moves": ["toy-world","commit-to-answer","visible-repetition","analogy","teaser-next"],
 "absent3_moves": ["brute-force-first","failure-shown","learner-discovers"]
}
```

```json
{"verified_trace": {"wpm": "PASS 170.00 (target 165.74-177.86, median 170.26)", "you_rate": "FAIL 0.58 (target 1.65-2.39, median 2.24)", "i_rate": "FAIL 0.25 (target 0.94-1.47, median 1.36)", "we_rate": "PASS 0.83 (target 0.44-1.04, median 0.85)", "num_rate": "FAIL 5.47 (target 2.15-5.03, median 3.74)", "hedge_rate": "FAIL 0.33 (target 0.12-0.26, median 0.17)", "example_rate": "PASS 0.25 (target 0.16-0.33, median 0.27)", "q_rate": "PASS 0.25 (target 0.14-0.28, median 0.18)", "sent_len": "FAIL 17.48 (target 20.19-24.25, median 21.93)", "switch_sponsor": "PASS detected=False default=OFF", "switch_teaser": "PASS detected=True default=ON", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (premise-claim vs premise-claim)", "ending_type": "MATCHES default (teaser-next vs teaser-next)", "summary": "4/9 numeric targets pass"}}
```
