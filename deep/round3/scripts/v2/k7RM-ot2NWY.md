# 3blue1brown: Linear combinations, span, and basis vectors | Chapter 2, Essence of linear algebra

- channel: 3blue1brown
- id: k7RM-ot2NWY
- title: Linear combinations, span, and basis vectors | Chapter 2, Essence of linear algebra
- duration: 599 s (9:59), band under10min
- condition: v2
- recall: none
- rulebook step 0: duration under 10 min; series label (Chapter 2); topic is math, a definitional build; title and first 40 s give no answer.
- class chosen: chapter arc for a short series video: question hook, two-arrow toy world, definitions with demos, one checkpoint, a three-arrow redundancy case, basis, teaser; no roadmap, recap, callback or notation
- exemplars read: deep/compact/fNk_zzaMoSs.txt (Vectors, Chapter 1, 9 min: the closest format and length; read in full)

## Content skeleton
- Two arrows and the only moves allowed: scale and add; the question of what can be reached
- A linear combination as a recipe of two instructions in proportion
- Sweeping the two numbers traces a region; for non-parallel arrows it fills the plane
- Span as the set of all linear combinations; parallel arrows collapse the span to a line
- Checkpoint: can two arrows reach all of three-dimensional space?
- Three arrows in the plane: one is redundant, the span is unchanged
- Basis as a minimal spanning set; its size is a fact about the space, not the chosen arrows
- Teaser for the next chapter on moving the grid

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Question: two arrows, scale and add only; what can you reach? |
| 0:22 | toy-world | One arrow right, one arrow up, the two building blocks |
| 0:50 | definition | Linear combination: scale each arrow, add tip to tail |
| 1:25 | demo-sim | Sweep the two amounts; a dot traces a region |
| 2:10 | demo-sim | Region fills the plane; span named |
| 2:55 | definition | Span: the set of all linear combinations |
| 3:40 | demo-sim | Parallel second arrow; the reach collapses to a line |
| 4:20 | definition | Span of one nonzero arrow is a line through the origin |
| 5:00 | viewer-turn | Checkpoint: can two arrows in space reach every point? |
| 5:20 | payoff | Answer: no, only a flat plane through the origin |
| 5:55 | generalize | Three independent arrows in space needed |
| 6:35 | demo-sim | Three arrows in the plane; one can be deleted |
| 7:20 | definition | Basis: a minimal spanning set |
| 8:00 | demo-sim | Remove one arrow; the plane remains |
| 8:40 | definition | Basis is not unique; its size is |
| 8:55 | teaser | Next chapter: what happens when the grid moves |
| 9:30 | coda | Closing line |
| 9:59 | end | Stop |

<<<NARRATION
Here's a question to start. Suppose you have two arrows, and the only things you're allowed to do are stretch them, shrink them, flip them, and add them together. What can you reach?

Let's make this concrete. Take one arrow pointing one step to the right, and another arrow pointing one step up. These two arrows are our building blocks. Every other arrow we make will be built out of them.

The move that does all the work is this. Scale each arrow by some number, and then add the results tip to tail. The result is called a linear combination. If I stretch the rightward arrow by three and the upward arrow by two, I end up at a point three steps right and two steps up. If I flip the upward arrow to point down, and use a half for the rightward arrow, I end up somewhere else entirely.

Think of each arrow as an instruction. The numbers you scale by are how much of each instruction you follow. A linear combination is a recipe that mixes the two instructions in some proportion.

Now let's see what happens if we let those proportions vary. Imagine a little dot that moves as you change the two scaling numbers. When the rightward amount is one and the upward amount is zero, the dot sits on the right arrow. When both amounts are zero, you're sitting at the origin. As you slide the numbers around, the dot traces out a whole region of the plane.

And here's the striking part. With these two arrows, you can reach every single point in the flat plane. Every point is some combination of the two, provided you're willing to use the right amount of each, including negative amounts and fractions.

Let's give this a name. The span of a set of arrows is the set of all linear combinations you can make from them. So the span of our two arrows is the whole plane. That is the key word. Span is not a single arrow or a single point. It is a collection, the full set of everything the arrows can reach.

Try one example by hand. Stretch the rightward arrow by two, and use the upward arrow flipped to point down, with a scale of one. Tip to tail, you land two steps to the right and one step down. That point is in the span, and so is every other point you can reach this way. Before going on, convince yourself that the plane has no points you cannot reach.

Now watch what happens when the arrows line up. Suppose the second arrow points in the same direction as the first, only twice as long. The span of these two is no longer the whole plane. Every combination you can build lies on one line through the origin. You can stretch, shrink, or flip, but you're stuck on that line. The second arrow added nothing new.

That gives us a useful test. Two arrows that point in different directions can reach everything. Two arrows that point the same way can only reach a line.

Let's push this into three dimensions. Suppose you have two arrows in space that point in different directions. You can combine them in every possible way, and what you get is a flat sheet, a plane passing through the origin. It is enormous, but it is not all of space. Any point hovering above or below that sheet is out of reach.

Before I explain why, take a guess. If you have two arrows in three-dimensional space, can you ever reach every point in space? Yes or no? Hold your answer. The answer is no, and the reason is the sheet we just saw. Two arrows only give you a flat plane, and no combination can lift you off that plane.

Now let's do a different example. Take three arrows in the flat plane. Two of them point in different directions, and the third points somewhere in between. The span is still the whole plane. Which means the third arrow is redundant. You could delete it and lose nothing, because anything it reaches, the other two can already reach.

That raises the natural question. Which arrows are essential? Is there a smallest set that still spans everything?

This is where the word basis comes in. A basis for a space is a set of vectors that spans the whole space and has no redundant members. Remove any one of them and the span shrinks. For the plane, a basis is any pair of arrows pointing in different directions. The right and up pair is just the most convenient one to look at.

The basis is not unique. Many different pairs of arrows will do the job. What is unique is the count. Any basis of the plane has exactly two arrows. That count is a fact about the space itself, not about the particular arrows you picked.

Here is a quick check you can run in your head. Take two arrows that point in the same direction, and notice that every scaling you try lands on one line. Now take two arrows at a sharp angle, and notice that the span already fills the plane. The angle between the arrows is most of the story.

Three arrows spanning the plane is a set with redundancy, and you can always throw one out and keep the span. That is a preview of an idea I'll get to next time, which is about when one arrow in a set is secretly built from the others.

That is also why the count matters. If you hand me three arrows in the plane, I can always find two of them that already span it, unless all three line up. That is a surprisingly useful thing to know without computing anything.

And that next video is where I want to go with this. Every linear combination we built today can be picked up and moved as a whole. What happens to the grid when the arrows themselves are transported to new places is where the real action of linear algebra starts.
NARRATION>>>

```json
{
 "format_class": "chapter arc for a short series video: question hook, two-arrow toy world, definitions with demos, one checkpoint, redundancy case, basis, teaser",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.04,
 "first_new_idea_frac": 0.08,
 "first_notation_frac": null,
 "payoff_frac": 0.53,
 "misconception": "none",
 "brute_force_first": false,
 "examples_count": 3,
 "example_growth": "two arrows -> parallel pair -> three arrows",
 "roadmap": "none",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.5,
 "caveat_type": "none",
 "recurring_anchor": "the right and up basis arrows, redrawn in each example",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 173,
 "median_beat_s": 25,
 "beat_sequence": ["hook","toy-world","definition","demo-sim","definition","demo-sim","viewer-turn","payoff","generalize","demo-sim","definition","teaser","coda"],
 "top5_moves": ["hook-question","special-case-first","visible-repetition","toy-world","generalize-to-other-domains"],
 "absent3_moves": ["roadmap","recap","callback-to-hook"]
}
```

```json
{"rule_trace": {
"U1": "applied: under 10 min with a series label; chapter arc, no roadmap, recap, callback or notation",
"U2": "n/a: title is a topic and first 40 s state no answer",
"U3": "applied: closes on the teaser, which a series video allows; no callback",
"U4": "applied: the right and up basis arrows return in each example (three or more uses)",
"U5": "n/a: no symbols or formulas; arrows are named in words and C1 drops notation",
"U6": "applied: 173 wpm under-10 target, beats of about 25 s",
"U7": "applied: no roadmap, vote or commit prompt; no planted misconception",
"U8": "n/a: the claims are definitional and exact; no approximation or open question",
"U9": "applied: binary checkpoint (can two arrows span space?) at 50 percent of runtime",
"U10": "n/a: no history-of-invention ladder",
"U11": "n/a: title names a topic, not an application or trigger",
"C1": "applied: under 10 min; roadmap, recap, callback and notation all dropped",
"C2": "n/a: no lemma block; the span facts are shown, not proved",
"C3": "n/a: no iterated construction",
"C4": "n/a: no proof payoff with an objection stage",
"C5": "n/a: the checkpoint is binary, not a magnitude ladder",
"D1": "applied: no roadmap",
"D2": "applied: no brute-force numerics",
"D3": "n/a: no wall or need posed as a design problem",
"D4": "n/a: no symbols; notation is absent by C1",
"D5": "applied: the teaser is used as the series chapter allows; no callback to the hook",
"N1": "applied: 173 wpm under-10 median as the delivery target; text cannot verify pace",
"N2": "n/a: under 10 min",
"N3": "broken: measured 3.2 per 100 words (N-median 2.05, p25-p75 1.62-2.5), outside the band",
"N4": "applied: measured 0.87 per 100 words (N-median 0.93, p25-p75 0.62-1.34), inside the band",
"N5": "applied: measured 0.97 per 100 words (N-median 1.02, p25-p75 0.71-1.58), inside the band",
"N6": "broken: measured 4.47 per 100 words (N-median 2.49, p25-p75 1.62-3.7), outside the band",
"N7": "broken: measured 0.49 per 100 words (N-median 0.21, p25-p75 0.12-0.3), outside the band",
"N8": "broken: measured 12.1 per 100 words (N-median 24, p25-p75 22-27), outside the band",
"N9": "applied: measured 0.39 per 100 words (N-median 0.33, p25-p75 0.22-0.44), inside the band",
"N10": "broken: measured 0.49 per 100 words (N-median 0.26, p25-p75 0.16-0.34), outside the band",
"B1": "applied: no sponsor read",
"B2": "applied: teaser used only because the video is a series chapter (U3 licence)",
"B3": "applied: no spoken roadmap",
"B4": "applied: no spoken recap"
}}
```
