# SebastianLague | bqtqltqcQhw | Coding Adventure: Boids

- channel: SebastianLague
- id: bqtqltqcQhw
- title: Coding Adventure: Boids
- duration: 515 s (8:35)
- condition: v2
- recall: vague (I recognise the series and the subject, not the video's content; written from the rulebook and general knowledge of flocking)
- class (step 0): duration <10 min; format = designed-lesson adventure (series label "Coding Adventure"); title does not state the answer; answer stated by 0:40 (three local rules make the flock); solved; topic = simulation / CS
- exemplars read: deep/compact/r_It_X7v-1E.txt (Coding Adventure: Ecosystem, 6:40), read in full

## Content skeleton
- Cold open on a finished flock, then the claim that nothing leads it.
- A single boid defined as position, velocity and sight radius; edges wrap.
- Random headings first, so the baseline is visible before any rule is on.
- Three rules added one per pass on one fixed random seed: cohesion, separation, alignment. The three rules are credited to the 1987 flocking paper at the point of choice.
- Failures on screen: cohesion alone collapses into a clump; a bounce edge pushes the flock into the walls.
- Sliders swept one at a time to show what each radius and weight does.
- Performance: neighbour search grows with the square of the flock; a grid of cells fixes it.
- Caveat on real starlings, then a large-flock finale and a short teaser for the next adventure.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Flock of about 300 triangles on screen; narrator says nothing leads them. |
| 0:20 | answer-statement | Three simple rules, each looking only at nearby neighbours, are enough. Stated by 0:40. |
| 0:40 | toy-world | One boid: position, velocity, sight radius; edges wrap. Exception at 0:55: it sees neighbours only, not the flock. |
| 1:05 | demo-sim | A few hundred boids with random headings; jitter, looks like dust. Baseline shown first. |
| 1:30 | definition | Cohesion defined as steering to the neighbours' average; credited to the 1987 flocking paper. |
| 2:10 | demo-sim | Cohesion on alone: boids collapse into one clump. |
| 2:40 | definition | Separation defined as steering away from very close neighbours, push scaled by closeness. |
| 3:15 | demo-sim | Clump opens into a spaced group; overlap stops. |
| 3:45 | definition | Alignment defined as matching neighbours' average heading; streams form. |
| 4:20 | demo-sim | Fixed seed, one rule per pass; the same start shows what each change does. |
| 5:00 | demo-sim | Radius and weight sliders swept one knob at a time. |
| 5:40 | demo-sim | Edge failure: boids vanish, then the bounce pushes the flock into walls; switch to wrap. |
| 6:20 | demo-sim | Performance: frame rate drops near 2,000 boids; grid of cells added, same rules, faster search. |
| 6:55 | caveat | Real starlings track roughly seven neighbours; the model is simpler and is not a claim about birds. |
| 7:20 | demo-sim | Full 2,000-boid flock in a larger space; streams, folds, split groups. Separation-off contrast. |
| 8:10 | payoff | Recap of the mechanism, said once, in one line: three rules, a radius, a grid, a wrap edge. |
| 8:25 | coda | Phrase mirror of the opening: a flock with nothing leading it. |
| 8:32 | teaser | One line: the next adventure gives these boids something to chase. |

## Narration
<<<NARRATION
Here are 300 triangles flying around a box, and nothing is leading them, so we should ask how that's even possible, because there's no flock controller and no path written for any one of them. In this video we want to find out how little each boid needs to know to make something that looks like a flock, and it turns out three simple rules are enough, as long as each rule only looks at neighbours nearby, within a short distance.

Let's start with a single boid, because we need to know exactly what it is before we give it any behaviour at all. For us a boid is just three things, a position, a velocity, and a sight radius, and it moves at a fixed speed in whatever direction it's facing. When it reaches an edge it reappears on the other side, and that's all it does for now, so we'll let it run for a while and watch, which is nothing very interesting at all, and that's fine.

Next we'll add a few hundred boids with random headings, and they jitter about, bump into one another, and mostly look like dust caught in a draft. That's roughly what random motion should look like, so nothing is broken yet, and we can be confident about that, even though it's just not a flock. I think it's important to see this boring version first, so we know exactly what changes when a rule turns on, and why.

Before any code, I wrote the three rules down in plain words on paper. I did that because we both know they're easy to get subtly wrong while you tune them by eye. The first rule is cohesion, and each boid looks at the neighbours inside its sight radius, works out their average position, and steers gently toward that point. The rule comes from Craig Reynolds' 1987 paper on flocking, which is where I first read about these three rules, and it was written for believable animation rather than physical accuracy, so keep that in mind.

Let's switch cohesion on, and the boids start pulling together until within a few seconds we have one tight clump. That's a ball, not a flock, and a lot of the boids are sitting on top of each other, which we expected, although seeing it happen is still a little funny. Cohesion on its own is too strong because nothing pushes boids apart. The steering is also capped at 5 degrees per frame, so a boid can only turn so far in one step, and without that cap the boids snap around like a glitch that we would have to explain away.

So we need the second rule, separation. If a neighbour is closer than a small distance, the boid steers directly away from it, and the push gets stronger the closer that neighbour is. A boid almost on top of another gets shoved hard, while one at the edge of the range barely moves at all. Now the clump opens up, the boids keep a gap between them, and the overlapping stops, which is exactly what we wanted to see, and you can see it on screen as the first real success.

They still don't move together, though. Some drift left while their neighbours drift right, so the group looks more like a cloud than a flock, and that's where the third rule comes in. Alignment makes each boid average its neighbours' headings and turn a little toward that average, and it's the rule that makes the group flow in one direction. Once it's on, we get streams of boids that travel together, and this is the moment where it starts to look like a flock. It's also the one I was most curious about, because a small change in the alignment weight changes the whole pattern.

From here on I'm keeping the random seed fixed for every run, with the same starting positions, the same starting headings, and the same frame number. That way every change on screen comes from the one rule we just touched, and we can compare two runs side by side without guessing what differs. We're adding one rule per pass on top of the same seed, so the starting picture never changes, and if the picture changes in a way I didn't expect, I know the cause is the rule I just edited.

Now the sliders. Each rule has a radius and a weight, and we'll sweep the alignment radius first. For example, with a radius of 10 pixels the boids move in tiny groups that barely notice each other, while at 50 pixels the groups grow to around 10 boids each. At 100 pixels they merge into long streams of 100 or so, and that's one knob with one visible effect. Then we'll do the same for cohesion and separation, one at a time, before we try any combination, and if you pause here, try to guess what a very large separation weight will do, because it's a useful habit to build.

The next problem shows up at the edges. Boids that leave the box simply vanish, because nothing brings them back into view. Our first attempt was a bounce, where a boid turns around when it hits a wall, and that looked stiff and pushed the whole flock into the walls in waves. So we switched to wrapping, which is the same behaviour the single boid already had, and the problem is gone. Wrapping has a side effect, though, since a boid near the left edge now counts boids on the right edge as neighbours, which is correct for this kind of space and a good reminder that the edge rule changes what counts as nearby.

Then performance, and here we hit the second wall. At about 2,000 boids the frame rate falls off a cliff, dropping from 60 frames per second to around 9, because every boid checks every other boid to find its neighbours. The number of checks grows with the square of the flock size, so doubling the flock roughly quadruples the work. The fix is a grid, and we split the box into square cells, each the size of the sight radius, and drop every boid into its cell. A boid then only looks in its own cell and the eight around it, which is 9 cells in total, and the rules stay exactly the same while the search gets much smaller. My first grid version was slower than I hoped, because I was rebuilding it every frame, and filling the cells once per frame turned out to be fast enough.

I want to be honest about one thing here. Real birds don't look at every neighbour inside a radius, and studies of starling flocks suggest they track roughly seven of their closest neighbours, which matters for how a flock responds when something startles it. Our model is simpler than that, and it still looks convincing, which is part of why rules like these became popular in animation, but I'm not claiming that it explains birds at all.

So let's go back to a full flock, and we'll give it room. Here are 2,000 boids in a space 4 times the size, with all three rules running and the grid doing the neighbour search, and the flock stretches into long streams, folds back on itself, and splits into two groups that pass through each other's gaps. Nothing in the model plans any of that, and it's only the three rules and the neighbours. For contrast, we'll run the same seed again with separation turned off, and the flock becomes a dense, overlapping cloud that is clearly wrong, which is the best argument I have for that rule.

We'll stop this adventure here, with three rules, a sight radius, a grid for speed, and a wrap-around edge. Next time we'll give these boids something to chase, because that's where the rules really get tested. Thanks for watching, and we'll see you then.
NARRATION>>>

## Slots
```json
{
 "format_class": "designed-lesson adventure: toy world, one rule per pass on a fixed seed, build-break-fix (Coding Adventure)",
 "answer_given_upfront": true,
 "hook_type": "spectacle-demo",
 "first_question_frac": 0.04,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.05,
 "first_notation_frac": null,
 "payoff_frac": 0.94,
 "misconception": "none",
 "brute_force_first": false,
 "examples_count": 4,
 "example_growth": "one boid -> 300 random -> 2,000 full flock",
 "roadmap": "none",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": null,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the single boid and the fixed random seed, reused in 5+ passes",
 "sponsor_frac": null,
 "ending_type": "phrase-mirror",
 "teaser": true,
 "wpm": 160,
 "median_beat_s": 25,
 "beat_sequence": ["hook", "answer-statement", "toy-world", "definition", "demo-sim", "definition", "demo-sim", "definition", "demo-sim", "caveat", "demo-sim", "payoff", "coda", "teaser"],
 "top5_moves": ["toy-world", "visible-repetition", "design-it-yourself", "minimal-definition-then-refine", "failure-shown"],
 "absent3_moves": ["hook-paradox", "analogy-breakpoint", "commit-to-answer"]
}
```

```json
{"rule_trace": {
 "U1": "applied: under 10 min and series label, so roadmap, recap and callback are off; the fixed 20-25 s beat grid is dropped and beats follow the designed-lesson template",
 "U2": "applied: thesis (three local rules make the flock) stated by 0:20; exception (boids see neighbours only) at 0:55; no brute-force numerics and no wall beat",
 "U3": "applied: final 10% is a phrase mirror plus a one-line teaser (series label); no hook callback because the hook question is not left open",
 "U4": "applied: the single boid and the fixed seed are reused in 5+ passes, each pass adding one rule",
 "U5": "n/a: no symbols or formulas are spoken; the rules are described in words",
 "U6": "applied: 160 wpm for the under-10 band, beats of about 20-30 s",
 "U7": "applied: no roadmap, no vote, no commit prompt; no planted misconception",
 "U8": "applied: domain caveat on real starlings near 7:00",
 "U9": "n/a: no binary decision or absurd magnitude to pause on; the only guess cue is rhetorical",
 "U10": "n/a: not a history-of-invention or escalating-antagonist video",
 "U11": "n/a: the title names the subject (boids), not an application or an end state",
 "C1": "applied: designed-lesson adventure format, not impersonal lecture and not devlog",
 "C2": "applied: rules are layered one per pass on the same seed, the starting picture unchanged",
 "C3": "n/a: not lecture format; no pause-the-video quiz",
 "C4": "applied: Reynolds 1987 flocking paper cited at the moment the cohesion rule is chosen",
 "C5": "n/a: series adventure opens on the finished flock, not on a devlog problem",
 "D1": "applied: failures shown on screen (cohesion clump, bounce edge, frame-rate drop)",
 "D2": "n/a: rules are named by their function, not by the failure they repair",
 "D3": "applied: sliders swept one knob at a time (alignment radius, then cohesion and separation)",
 "D4": "n/a: no honest-close bundle; the ending is a phrase mirror and a one-line teaser, with the caveat placed mid-video",
 "D5": "n/a: no equation; no formula revealed as a label",
 "N1": "applied: 156 wpm measured on the narration (1,336 words over 8:35), inside p25-p75 141-180",
 "N2": "n/a: under-10 band used for this video",
 "N3": "applied: you/your 0.30 per 100 words, inside p25-p75 0.23-0.78",
 "N4": "applied: I/me/my 1.05 per 100 words, inside p25-p75 0.94-2.81",
 "N5": "applied: we/us/let's 2.62 per 100 words, inside p25-p75 2.55-5.70",
 "N6": "applied: numbers 1.05 per 100 words, inside p25-p75 0.95-2.12",
 "N7": "applied: 0 question marks, the channel median",
 "N8": "applied: mean 24.8 words per sentence, inside p25-p75 19-25",
 "N9": "applied: hedges 0.22 per 100 words, inside p25-p75 0.11-0.35",
 "N10": "applied: example cues 0.07 per 100 words, inside p25-p75 0.03-0.18",
 "B1": "applied: no sponsor read",
 "B2": "applied: one-line teaser, because the video is in a series",
 "B3": "n/a: roadmap withheld; video type does not call for one",
 "B4": "applied: no spoken recap"
}}
```
