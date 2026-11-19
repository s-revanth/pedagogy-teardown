# SebastianLague | v1V3T5BPd7E | Kinematic Equations (E01: introduction)

- channel: SebastianLague
- id: v1V3T5BPd7E
- title: Kinematic Equations (E01: introduction)
- duration: 377 s (6:17)
- condition: v2
- recall: none (I do not recognise this episode; written from the rulebook and standard constant-acceleration physics)
- class (step 0): under-10 min (6:17); format = impersonal lecture series (E01 label); answer stated by 0:40 (any three of five quantities give the other two); solved (standard kinematics); topic = physics, constant-acceleration motion
- exemplars read: deep/holdout/compact/l-hh51ncgDI.txt (Algorithms Explained: minimax, 11:01) read in full for lecture pacing and the pause cue; deep/compact/-L-WgKMFuhE.txt (A* Pathfinding E01, 11:38) read in full for the E01 series opening

## Content skeleton
- Thesis up front: five quantities, constant acceleration, any three give the other two.
- One worked referent: a ball thrown straight up at 20 metres per second, slowed by gravity at about 9.8.
- First equation stated in words, then in symbols v, u, a, t, after the ball.
- Check at one, two and three seconds; the second equation for displacement, checked at one second.
- Pause-or-guess at about 62 percent: which equation gives the peak height with no time given; answer is the time-free equation, about 20.4 metres.
- Myth defused: a heavier ball does not fall faster, since mass is absent from the equations; air drag is the stated limit.
- Two more worked cases (braking car, dropped ball) and one habit: list the five quantities first.
- One-sentence takeaway, then a teaser for the derivation in the next episode.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Kinematics introduced as motion without causes; the five quantities named; the answer is any three give the other two. |
| 0:20 | answer-statement | Thesis stated with the exception: constant acceleration only. Stated by 0:40. |
| 0:45 | toy-world | A ball thrown straight up from a hand at 20 metres per second; gravity slows it by about 9.8 each second. |
| 1:20 | definition | First equation stated in words, then symbols v, u, a, t introduced after the ball is on screen. |
| 1:50 | demo-sim | Checks at one, two and three seconds: about 10.2, 0.4 and minus 9.4 metres per second on the screen. |
| 2:40 | demo-sim | Shown, no narration: the height and velocity plots run for about 50 seconds on screen. |
| 3:30 | definition | Second equation for displacement, checked at one second: about 15 metres above the hand. |
| 3:55 | viewer-turn | Pause-or-guess: the peak height is wanted but no time is given; which equation is needed? Answer follows in about 20 seconds. |
| 4:20 | payoff | Third equation with no time term; final speed zero, start 20, acceleration minus 9.8: about 20.4 metres. |
| 4:50 | misconception-defuse | Common myth that a heavier ball falls faster; mass is absent from the equations, so the path is the same. |
| 5:20 | caveat | Air drag is ignored; a real throw falls short of 20.4 metres; this is the domain limit of the model. |
| 5:45 | generalize | Braking car from 25 metres per second at 5 metres per second squared: 62.5 metres, time missing again. |
| 5:58 | generalize | Dropped ball from rest: about 29 metres per second after three seconds and about 44 metres fallen. |
| 6:08 | advice | Habit: write the five quantities first, mark the three known, then pick the equation. |
| 6:12 | coda | One-sentence takeaway: any three of the five quantities give the other two. |
| 6:14 | teaser | Next episode derives the equations from the definition of acceleration. |

## Narration
<<<NARRATION
Kinematics is the study of motion without asking what causes it. In this episode we'll look at a small set of equations that connect five quantities for an object moving with constant acceleration: its displacement, its starting speed, its final speed, its acceleration, and the time it takes. The core idea is that any three of those five quantities are enough to find the other two, and that's what we'll test throughout.

Let's make this concrete with one object, a ball thrown straight up. Imagine it leaves a hand at 20 metres per second. Gravity makes it slow down by about 9.8 metres per second every second, which is what we call the acceleration, and it reaches the top with zero speed before it falls back down. That's the whole problem in one picture, and I find it useful to follow it with numbers.

We'll write the first equation in words before we use it. The final speed equals the starting speed plus the acceleration times the time. That's the one relationship we need for speed, and in symbols we write v equals u plus a t, where u is the starting speed, a is the acceleration, and t is the time. Each symbol names something we just saw happening to the ball.

Let's check it at a few moments, and after one second the ball has slowed by 9.8 metres per second, so it's moving at roughly 10.2 metres per second upwards. After two seconds it's down to about 0.4, and I think that's a nice moment to pause and look at it. After three seconds it has passed the top and is moving down at about 9.4 metres per second. The equation gives the same answers every time, which is the whole point of an equation, and I'd say it's the reason we trust it.

Now the position, and the second equation tells us how far the ball travels, and it says the displacement equals the starting speed times the time, plus one half of the acceleration times the time squared. That looks more complicated, but it uses the same ingredients as before. Checking it at one second gives about 15 metres above the hand, and I was pleased that this agrees with the speeds we just worked out.

Pause here if you want to guess. We want the highest point the ball reaches, but we aren't given the time it takes to get there, so the first equation is no help. Take a moment to decide which equation we should use before reading on.

The answer is a third equation that leaves out time. The final speed squared equals the starting speed squared plus two times the acceleration times the displacement. At the top the final speed is zero, the starting speed is 20, and the acceleration is minus 9.8. So the height is twenty squared divided by two times 9.8, which comes to roughly 20.4 metres. I'd call that the answer, and the rest of the problem is just bookkeeping.

Now a common myth, and many people think a heavier ball falls faster, and the equations say something different. Mass doesn't appear anywhere in them, so a heavy ball and a light ball with the same starting conditions follow the same path. That only holds when air resistance is negligible, and that brings us to the main limitation of this model.

Our model ignores air drag, and a real ball slows down because of the air, and the faster it moves, the more it slows, so a real throw falls short of the 20.4 metre height we calculated. That's a domain limit of the model, and it matters most for light objects or high speeds. We'll handle drag in a later episode, where these equations stop being this simple.

Let's apply the same equations to a different object, and a car brakes from 25 metres per second to rest, with a constant deceleration of 5 metres per second squared. We don't know the time it takes, and the third equation gives the braking distance: zero equals 25 squared plus two times minus 5 times the distance, so the distance is 62.5 metres. Here is another case where time is missing, and I like this one because one equation is enough.

Now a dropped ball. Released from rest, it starts with zero speed and accelerates downward at about 9.8 metres per second squared. After three seconds its speed is about 29 metres per second, and it has fallen about 44 metres, which I find a surprisingly large number for a ball dropped from rest. Notice that the starting speed is zero here, so the equations simplify. That's a useful habit, and I use it all the time: set the known values first, then pick the equation that leaves out the unknown quantity.

Before we finish, here's one habit to keep. Write down the five quantities first, mark which three you know, and only then choose an equation. Many students skip this step and reach for whichever equation they remember, rather than the one that fits the numbers they have. That mistake is common, and it's cheap to avoid if we write the list down every time.

The main takeaway, which I would put on the first slide, fits in a sentence. With constant acceleration, any three of the five quantities give us the other two. The equations are the same for a ball, a car, or a falling stone, and only the signs and the known values change between problems. That's the whole structure of this episode, and everything later builds on it.

Next episode we'll derive these equations from the definition of acceleration, so we know where each one comes from rather than taking them on trust. Thanks for watching, and I'll see you in the next episode.
NARRATION>>>

## Slots
```json
{
 "format_class": "impersonal lecture series (E01): thesis up front, one worked ball, pause-or-guess, defused myth, domain caveat, teaser",
 "answer_given_upfront": true,
 "hook_type": "answer-stated",
 "first_question_frac": 0.62,
 "first_concrete_object_frac": 0.12,
 "first_new_idea_frac": 0.05,
 "first_notation_frac": 0.24,
 "payoff_frac": 0.69,
 "misconception": "planted-myth-defused",
 "brute_force_first": false,
 "examples_count": 3,
 "example_growth": "thrown ball -> braking car -> dropped ball",
 "roadmap": "none",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.62,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the thrown ball at 20 metres per second, reused in 4+ passes",
 "sponsor_frac": null,
 "ending_type": "phrase-mirror",
 "teaser": true,
 "beat_sequence": [
  "hook",
  "answer-statement",
  "toy-world",
  "definition",
  "demo-sim",
  "definition",
  "viewer-turn",
  "payoff",
  "misconception-defuse",
  "caveat",
  "generalize",
  "advice",
  "coda",
  "teaser"
 ],
 "top5_moves": [
  "minimal-definition-then-refine",
  "special-case-first",
  "misconception-first",
  "visible-repetition",
  "honest-caveat"
 ],
 "absent3_moves": [
  "hook-paradox",
  "commit-to-answer",
  "expert-dialogue"
 ],
 "wpm": 156,
 "median_beat_s": 25
}
```

```json
{"rule_trace": {
 "U1": "applied: under-10 band and series label (E01); roadmap, recap and callback dropped; notation deferred until after the ball referent; fixed 20-25 s beat grid dropped",
 "U2": "applied: thesis stated by 0:40 (any three of five quantities give the other two); exception at 0:20 (constant acceleration only); worked ball by 0:45; no brute-force numerics; no wall",
 "U3": "applied: phrase-mirror ending restates the any-three thesis; teaser only (series); no hook callback since the thesis is already answered",
 "U4": "applied: the thrown ball is reused in 4+ passes (checks, height, drag caveat, contrast with the dropped ball), each adding a layer",
 "U5": "applied: symbols v, u, a and t spoken at about 1:20, within 60 s of the ball; governing equations stated before the demo, as U5 permits",
 "U6": "applied: about 156 wpm on 983 words over 6:17 (under-10 band), beats of 15-40 s with one silent 50-second plot",
 "U7": "applied: no roadmap, no vote or commit prompt; the myth appears only as a definition by contrast (mass absent from the equations)",
 "U8": "applied: domain caveat (air drag ignored) at 5:20",
 "U9": "applied: one pause-or-guess at 62 percent (3:55), answered after about 20 seconds",
 "U10": "n/a: not a history-of-invention or escalating-antagonist video",
 "U11": "n/a: title names a topic (kinematic equations), not an application or end state",
 "C1": "applied: impersonal lecture series format (E01), not devlog and not designed-lesson adventure",
 "C2": "applied: the ball is the one example, rerun with the same numbers for each equation; the picture does not change",
 "C3": "applied: pause-the-video guess at about 62 percent of runtime, in lecture format",
 "C4": "n/a: no design source cited; the equations are standard constant-acceleration kinematics",
 "C5": "n/a: lecture series opens with the thesis, not a devlog problem",
 "D1": "n/a: no failure shown on screen; the checks are consistency checks on the arithmetic",
 "D2": "n/a: no repair term named after a failure",
 "D3": "n/a: no knob turned; one parameter set per worked example",
 "D4": "n/a: no honest-close bundle; the close is an advice line and a phrase-mirror takeaway",
 "D5": "n/a: the governing equation is stated before the demo, so the equation-after-behaviour default is not used",
 "N1": "applied: 156 words per minute (measured), inside p25-p75 141-180",
 "N2": "n/a: over-10 band rule; this video is under-10 min",
 "N3": "applied: 0.31 you/your per 100 words (measured), inside p25-p75 0.23-0.78",
 "N4": "applied: 1.02 I/me/my per 100 words (measured), inside p25-p75 0.94-2.81",
 "N5": "applied: 2.75 we/us/let's per 100 words (measured), inside p25-p75 2.55-5.7",
 "N6": "applied: 2.03 numbers per 100 words (measured), inside p25-p75 0.95-2.12",
 "N7": "applied: 0.00 question marks per 100 words (measured), inside p25-p75 0.0-0.09",
 "N8": "applied: 19.7 words per sentence (measured), inside p25-p75 19-25",
 "N9": "applied: 0.20 hedges per 100 words (measured), inside p25-p75 0.11-0.35",
 "N10": "applied: 0.10 example cues per 100 words (measured), inside p25-p75 0.03-0.18",
 "B1": "applied: no sponsor read",
 "B2": "applied: teaser only (series label)",
 "B3": "n/a: roadmap withheld; the thesis is stated by 0:40 instead of a roadmap",
 "B4": "applied: no recap; the single takeaway sentence is a phrase mirror, not a list of lessons"
}}
```
