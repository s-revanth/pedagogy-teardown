# 3blue1brown: Bayes theorem, the geometry of changing beliefs

- channel: 3blue1brown
- id: HZGCoVF3YvM
- title: Bayes theorem, the geometry of changing beliefs
- duration: 911 s (15:11), band over10min
- condition: v2
- recall: none
- rulebook step 0: duration 15 min (>=10); format is a standalone concept explainer (no series label, not first-person); title and first 40 s give no answer; the theorem is solved; topic is probability.
- class chosen: concept explainer: question hook, toy population, area geometry, formula after the picture, two-test update, phrase-mirror close
- exemplars read: deep/compact/OkmNXy7er84.txt (Putnam probability, 11 min: reframing, the reveal, the close); deep/holdout/compact/d-o3eB9sfls.txt (Basel, 17 min: worked-number hook, geometric build)

## Content skeleton
- A positive result from a 99 percent accurate test, and why the belief after it is nowhere near 99 percent
- A population of 1,000 as the toy world: 10 sick, 990 healthy
- Two sources of positives (true positives and false alarms); their ratio is the posterior, about one in six
- Geometry: a bar of length one split into sick and healthy strips, each cut by the test; the update is restrict then rescale
- The formula appears only after the picture, as shorthand for two areas
- A second independent positive: the posterior becomes the new prior and climbs to about 80 percent
- Caveat: independence and the prior; correlated errors weaken the second test

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Question: a 99 percent accurate test comes back positive; how worried? |
| 0:40 | toy-world | Population of 1,000 on a grid: 10 sick, 990 healthy |
| 1:30 | demo-sim | Test applied to all: about 10 true positives, about 50 false alarms |
| 2:20 | definition | The positives come from two groups; count the mix |
| 3:10 | demo-sim | Bar of length one: thin sick sliver, long healthy part |
| 4:00 | toy-world | Test cuts each strip; lit strips form the positive region |
| 4:50 | demo-sim | Sick share of the lit area equals the count ratio |
| 5:40 | definition | Bayes in one sentence: discard the inconsistent, rescale |
| 6:20 | viewer-turn | Guess ladder: under 5 percent, around 50 percent, above 90 percent |
| 7:10 | payoff | Reveal: one in six, about 17 percent |
| 7:40 | derivation | Formula as shorthand for the two areas: prior times likelihood over total |
| 8:40 | derivation | Why the bottom is the total lit area |
| 9:30 | demo-sim | Second independent positive filters the sixty again |
| 10:30 | payoff | About 80 percent after two positives |
| 11:00 | payoff | Belief moved from one in six to four in five with one test repeated |
| 11:50 | generalize | Any priors, any noise: same restrict-and-rescale move |
| 12:40 | caveat | Independence and prior assumptions; shared error weakens the second test |
| 13:30 | generalize | Continuous version: belief as a bar reweighted by evidence |
| 14:10 | coda | Phrase mirror on changing beliefs |
| 14:50 | coda | Closing line on shape and evidence |
| 15:11 | end | Stop |

<<<NARRATION
Here's a question that sounds like it should have an easy answer. A test for a disease is 99 percent accurate. You take it, and it comes back positive. How worried should you be?

Most people's first instinct is to say you almost certainly have the disease. After all, the test is right 99 percent of the time. But let's slow down and count, because this is one of those problems where intuition and arithmetic pull in different directions.

Imagine a thousand people taking this test. Suppose the disease is rare, affecting one person in a hundred. So among our thousand people, ten are sick and 990 are healthy.

Now run the test on everyone. Essentially all ten sick people test positive. Of the 990 healthy people, the test is wrong five percent of the time, so about 50 of them get a false alarm. That's a second group of positives, and it's much bigger than the first.

So the positive results come from two groups: about ten sick people, and about fifty healthy people who were misled. Sixty positives in total, and only ten of them are actually sick.

If you are one of those sixty, the chance you're sick is ten out of sixty. That's one in six, about 17 percent. A positive result has raised the chance from one in a hundred to one in six, which is a big jump, and it is still far from certainty.

Now let's see the geometry, because the picture does most of the work. Picture the population as a bar of length one. Split the bar into two parts. The thin left sliver is the sick people, one percent of the length. The long right part is the healthy people, ninety-nine percent of the length.

Now the test cuts each part again. Inside the sick sliver, the positive results are almost all of it. Inside the healthy part, only a thin strip, five percent of its height, lights up as a false alarm. The positive region is the union of those two lit pieces, and the sick share of that lit region is the answer.

Here is the whole idea in one sentence. When you learn some evidence, throw away every possibility that is inconsistent with the evidence, and then rescale what is left so the total is one again. The belief you hold afterward is the fraction of the surviving area that belongs to each hypothesis.

Before I write any formula, make a guess, because the formula will mean more once you have committed to a number. Here are three options. Is the chance you're sick below 5 percent? Around 50 percent? Or above 90 percent? Pick one in your head.

The answer, as we just counted, is one in six. If you guessed around 50 percent, you're in the company of a lot of people who make the same first error. The 99 percent accuracy pulls the answer toward yes, and the rarity of the disease pulls it hard back toward no.

Now the formula. Call the chance of being sick before any test the prior. Call the chance that a sick person tests positive the likelihood. The chance of a positive result overall is the total lit area, and the updated belief is the sick part of that lit area divided by the total lit area. In shorthand, the probability of sick given positive equals the probability of positive given sick, times the prior probability of sick, divided by the total probability of positive.

Notice what each piece points to. The top is the area of the sick strip that lights up. The bottom is the area of every lit strip. The formula is not a magic rule. It is a ratio of two areas in the picture, written compactly.

Let's see what happens when you keep going. Suppose the same person takes a second, independent test, and it is also positive. The belief from the first test does not start over. The one-in-six posterior becomes the new prior, and you filter the population again. Of the sixty people who tested positive the first time, about ten are sick and about fifty are healthy. The second test catches almost all the sick people and lets through five percent of the healthy ones. So it keeps about ten sick people and about two or three healthy ones.

About ten out of twelve and a half. That is roughly 80 percent. The same test, taken twice, moved the belief from one in six to four in five. Each piece of evidence gets its own cut and its own rescaling.

Nothing here depends on these particular numbers. If the prior were different, the bar would split at a different place. If the test were noisier, the lit strips would be thicker. The update is always the same move: restrict to what the evidence allows, then rescale. Picture the belief as a shape that evidence trims.

If you want to test the idea on different numbers, try a common disease instead of a rare one. Suppose one person in five is sick. Now the sick sliver is large, and the same five percent false alarm rate is a small share of the lit area. The positive result pushes the belief to about 83 percent. Same test, same geometry, very different starting bar, and the answer moves with the prior exactly as the picture says it should.

Now a caveat, because a formula gives a clean answer whether or not the picture fits the world. This calculation assumed the two tests are independent once you know the disease status, and that the one percent rate and the five percent false alarm rate apply to the person in front of you. If both tests share a cause of error, like the same contaminated sample, the second positive is worth much less than I just said. And the one-in-six number depends entirely on the prior. For a group at much higher risk, the same positive means something very different.

So should you panic after a positive result? Not yet, and not because the test is useless. A positive result moves your belief a lot, but it does not settle the question until you know how rare the thing was to begin with. Belief changes like a shape. Evidence cuts it, and the part that survives gets stretched back to fill the whole frame. That is what changing your mind looks like, when you do the geometry honestly.
NARRATION>>>

```json
{
 "format_class": "concept explainer: question hook, toy population, area geometry, formula after picture, two-test update, phrase-mirror close",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.03,
 "first_new_idea_frac": 0.05,
 "first_notation_frac": 0.5,
 "payoff_frac": 0.47,
 "misconception": "none",
 "brute_force_first": false,
 "examples_count": 3,
 "example_growth": "one test -> two tests -> any priors",
 "roadmap": "none",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.42,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the 1,000-person population, returned to in four passes",
 "sponsor_frac": null,
 "ending_type": "phrase-mirror",
 "teaser": false,
 "wpm": 180,
 "median_beat_s": 38,
 "beat_sequence": ["hook","toy-world","demo-sim","definition","viewer-turn","payoff","derivation","demo-sim","payoff","generalize","caveat","coda"],
 "top5_moves": ["hook-question","toy-world","notation-after-concept","visible-repetition","honest-caveat"],
 "absent3_moves": ["roadmap","humor","rule-list"]
}
```

```json
{"rule_trace": {
"U1": "n/a: 15 min, no series label, not first-person, not psychology or devlog",
"U2": "n/a: title and first 40 s state no answer; the posterior is revealed at 7:10",
"U3": "applied: closes on the phrase mirror 'changing beliefs'; no callback, no teaser",
"U4": "applied: the 1,000-person population returns in four passes, each adding a layer",
"U5": "applied: formula appears only after the area picture at 7:40; each term tied to a strip",
"U6": "broken: beat rows average about 38 s, above the 15-30 s guidance; table condensed for a 15-minute runtime; pace held at the 180 wpm target",
"U7": "applied: no roadmap, vote or commit prompt in the hook; misconception appears only as contrast",
"U8": "applied: domain caveat on independence and priors at 12:40",
"U9": "applied: guess ladder at 6:20 (42 percent of runtime), answered at 7:10",
"U10": "n/a: no history-of-invention ladder; standalone concept",
"U11": "n/a: title names a theorem, not an application or trigger event",
"C1": "n/a: 15 min, above the 10-minute threshold",
"C2": "applied: claim of the one-in-six posterior, then the area justification within about 90 s (7:10-8:40)",
"C3": "n/a: no iterated construction taken to a limit",
"C4": "applied: awe beat (one in six), voiced objection (should it not be 99 percent?), then algebra",
"C5": "applied: rising guess ladder of three magnitudes at about 42 percent of runtime",
"D1": "applied: no roadmap up front",
"D2": "applied: no brute-force numeric partial sums; counting uses the population grid only",
"D3": "n/a: no wall; need not posed as a design problem",
"D4": "applied: symbols appear only after the geometric picture",
"D5": "n/a: hook answered mid-video; no callback or teaser (not a series)",
"N1": "n/a: over-10-minute video",
"N2": "applied: delivery target 180 wpm, the band median; text cannot verify pace",
"N3": "applied: measured 2.02 per 100 words (N-median 2.05, p25-p75 1.62-2.5), inside the band",
"N4": "broken: measured 0.18 per 100 words (N-median 0.93, p25-p75 0.62-1.34), outside the band",
"N5": "broken: measured 0.46 per 100 words (N-median 1.02, p25-p75 0.71-1.58), outside the band",
"N6": "broken: measured 6.8 per 100 words (N-median 2.49, p25-p75 1.62-3.7), outside the band",
"N7": "broken: measured 0.46 per 100 words (N-median 0.21, p25-p75 0.12-0.3), outside the band",
"N8": "broken: measured 13.3 per 100 words (N-median 24, p25-p75 22-27), outside the band",
"N9": "broken: measured 1.47 per 100 words (N-median 0.33, p25-p75 0.22-0.44), outside the band",
"N10": "broken: measured 0.37 per 100 words (N-median 0.26, p25-p75 0.16-0.34), outside the band",
"B1": "applied: no sponsor read",
"B2": "applied: no teaser; not a series video",
"B3": "applied: no spoken roadmap in the first 12 percent",
"B4": "applied: no spoken recap in the last 20 percent"
}}
```
