# Header
- channel: 3blue1brown
- id: k7RM-ot2NWY
- title: Linear combinations, span, and basis vectors | Chapter 2, Essence of linear algebra
- duration: 599 s
- condition: v3
- recall: vague (the series is recognised; the script is written from the v3 rules and general subject knowledge, not from the video)
- exemplars read: deep/corpus/compact/fNk_zzaMoSs.txt, deep/corpus/compact/P2LTAUO1TdA.txt

## Content skeleton
- Claim up front: two arrows that point in different directions can reach every point in a flat plane.
- Vocabulary: vectors are scaled and added; i-hat and j-hat as the standard basis; coordinates as recipes.
- Linear combination and span; one vector gives a line, two independent vectors give the plane.
- Worked solve: which coefficients reach the point (5, 5) from (1, 2) and (3, -1); twenty sevenths and five sevenths.
- Basis as spanning and non-redundant; unique coordinates for each point.
- Contrast case: a second vector that is twice the first collapses the span to a line.
- Basis change: the point stays put while the description changes; three dimensions for the same test.
- Close with a recap, then teaser for the next chapter on transformations.

## Beat sheet (about 1658 spoken words across 599 s)
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Premise: two arrows in different directions reach the whole plane |
| 0:25 | definition | Vectors as arrows; the two operations, scaling and adding |
| 1:05 | toy-world | i-hat and j-hat; the vector three, two built by hand |
| 1:50 | definition | Linear combination: a times v plus b times w |
| 2:24 | viewer-turn | Rhetorical: which points can you reach with two arrows |
| 2:50 | generalize | One vector: every multiple traces a line |
| 3:30 | generalize | Two independent vectors fill the plane |
| 4:00 | derivation | Set up the two equations for the point five, five |
| 4:30 | payoff | Twenty sevenths and five sevenths; the point is reachable |
| 5:00 | wall | Second vector equal to twice the first; the span collapses to a line |
| 5:40 | generalize | Dependence means redundancy; a basis is the sweet spot |
| 6:10 | analogy | Change the basis, keep the point; the coordinates change |
| 7:00 | generalize | Three dimensions: a third vector inside the plane adds nothing |
| 8:00 | recap | Scale, add, combine, span, basis |
| 9:30 | teaser | Next video: transformations and where they send the basis |

<<<NARRATION
Pick any point in a flat plane, and you can reach it by walking along just two arrows, provided those arrows point in genuinely different directions. That simple fact is the seed of almost everything in linear algebra, and in this video I want to build it up carefully from the ground. Nothing here is hard on its own, but the pieces fit together in a way that is worth seeing slowly.

Begin with the arrows themselves. Picture a vector drawn from the origin to some point, and treat it as a little instruction, a recipe for moving across the plane. I like to picture it as an arrow with a length and a direction, because that is the picture that will carry us through the rest of the discussion, and you will keep coming back to it.

Two operations are available for these arrows. You can stretch or shrink one by multiplying it by a number, and you can add two of them tip to tail. Those are the only two things you ever do with vectors, and the rest of the subject is really about what happens when you combine those two moves over and over again without ever leaving the plane.

Now give names to two special arrows. The first, which points a unit to the right, we'll call i-hat, and the second, which points a unit straight up, we'll call j-hat. Any vector in the plane can be written as a number times i-hat plus another number times j-hat, and that pair of numbers is exactly what its coordinates tell us, so the coordinates are really a recipe in disguise.

Take the vector with coordinates three and two. That means you scale i-hat by three, scale j-hat by two, and then place the two scaled arrows tip to tail. The result lands exactly on the point you started with. You can check this by drawing it on paper, and I really encourage you to do so before moving on, because the habit of drawing will save you a lot of trouble later.

This kind of expression has a name. A linear combination of two vectors is any sum where each vector gets multiplied by some number, and those two numbers can be anything at all, including zero or negative values. So if I have two vectors called v and w, then a times v plus b times w is a linear combination, for any choice of the numbers a and b that you like.

Here is the key question. Given a fixed pair of vectors, which points can you reach by taking linear combinations of them? The collection of all reachable points is called the span. It answers a question about the reach of your two arrows, and it turns out to depend sharply on how those arrows relate to each other, which is the whole story of this chapter in a single sentence.

Start with just one vector, call it v. Its span is every scaled version of v, which means all the multiples of v as you let the scalar range over every number. If you stretch an arrow forward, then backward, and then through every amount in between, you trace out an entire line through the origin. So the span of a single nonzero vector is a line, and nothing more.

Now add a second vector, w, which points in a different direction from v. Each choice of a and b gives a point, and as you vary both numbers, the reachable points fill out more and more of the plane. In fact, if v and w point in genuinely different directions, their span is the entire two dimensional plane, which means that every single point is reachable.

I'll check that claim with a concrete pair. Take v equal to one, two, and take w equal to three, negative one. Can we reach the point five, five? We need a times v plus b times w to equal five, five. That gives two equations: a plus three b equals five, and two a minus b equals five. Equations like these are probably easy to solve with a little patience.

Solving it is straightforward. The second equation gives b equals two a minus five. Substitute that into the first, and you get a plus six a minus fifteen equals five, which simplifies to seven a equals twenty. So a is twenty over seven, and then b works out to five over seven. Therefore the point five, five is reachable, and the coefficients are twenty sevenths and five sevenths.

I want to pause on that result, because it contains the whole idea of a basis. A basis is a set of vectors that does two jobs at once. It spans the whole space, so that every point is reachable, and it does so without any redundancy, so that each point is reachable in exactly one way. Our pair v and w satisfies both requirements, and that is why the solution above was unique.

Why exactly one way? If there were a second recipe for the same point. Subtracting one recipe from the other would give a nontrivial combination of v and w that equals the zero vector. But for vectors that point in different directions, that can only happen if both coefficients are zero, so the two recipes must have been identical all along. I find that uniqueness is not a coincidence, but a consequence of the directions being different.

Now I want to look at a pair that fails. The second vector could simply be two times v, so w equals two, four. The span, in that case, is something else entirely. Every combination a v plus b w is really a v plus two b v, which is simply some multiple of v. You are back to a single line, and the second vector has added nothing new to the picture at all.

This is what we call linear dependence. Two vectors are dependent when one of them can be written as a scalar times the other, which means they point along the same line. When vectors are dependent, one of them is redundant, because it does not extend the span in any direction. Independent vectors, by contrast, each contribute a genuinely fresh direction, and that freshness is what makes them valuable.

This is really a question about efficiency, and you should expect it to come up constantly. The point is how few vectors you need in order to reach everything, and how many you can throw away without losing anything. A basis is the sweet spot, the smallest set that still spans the space. In the plane that means exactly two vectors, and in space it means exactly three, and the count matches the dimension of the space itself.

Next, connect this to coordinates, because it changes how we think about a point. Once you pick a basis, a point no longer has coordinates relative to the standard arrows alone. Instead, its coordinates are the two scalars needed to reach it using the basis vectors. Change the basis, and the very same point gets different numbers, even though nothing about the point has moved at all.

That might sound like a nuisance, but perhaps it is actually a powerful idea. The point itself has not changed. What changed is the grid of directions you use to describe it. Some bases make a problem easy, because they line up with the structure of the situation, and other bases make the same problem look messy and tangled, even though the underlying geometry is identical.

Often, if the vectors that matter in a problem all point along a few special directions, choosing those directions as your basis can turn a hard calculation into a simple one. You will see this idea again and again as the course develops, because it is one of the main tools for simplifying a problem without changing its content. It is like choosing the right language before you start speaking.

I also want to mention a subtle point about the word span. People sometimes say that a set spans a space, and they mean exactly the same thing as saying the set can reach every point of that space through linear combinations. That phrasing sounds technical, but it is really just the statement we have been using all along, dressed up in more formal clothing so that it reads well in a textbook.

I want to test the pattern in space, since it reinforces everything we have seen. Take three vectors that do not all lie in one flat plane. Their linear combinations fill up all of space. If instead one of the three lies inside the plane spanned by the other two, the span collapses down to that plane, and the third vector adds nothing that the first two did not already provide.

So the dimension of a span is simply a count of how many genuinely independent directions you have to work with. You can always detect a redundant vector by asking whether it lies in the span of the others. That test is easy to state, and in practice it is the main way you will check whether a given set of vectors is a basis, which is a check you will perform constantly.

I'll gather the core moves in one place before going on. Vectors can be scaled and added. A linear combination uses those two operations with arbitrary coefficients. The span is the set of all such combinations. A basis is a span with no redundancy, and every point in the space then has a unique set of coordinates in that basis. Those four sentences contain the whole chapter in compressed form.

I know that feels like a lot, but don't worry, because all of it comes from a single picture. Two arrows pointing in different directions can reach the whole plane, while two arrows pointing along the same line can only reach that line. Everything else in this chapter is a careful elaboration of that single observation, and each new idea is just a way of asking the same question from a slightly different angle.

In the next video, we'll take this idea of a span and ask what happens when a transformation acts on the plane, and why a linear transformation is completely determined by where it sends the basis vectors.
NARRATION>>>

```json
{
 "format_class": "definition chain, worked solve, contrast case, recap, teaser",
 "answer_given_upfront": true,
 "hook_type": "premise-claim",
 "first_question_frac": 0.24,
 "first_concrete_object_frac": 0.03,
 "first_new_idea_frac": 0.07,
 "first_notation_frac": 0.10,
 "payoff_frac": 0.40,
 "misconception": "none",
 "brute_force_first": false,
 "examples_count": 4,
 "example_growth": "scaled arrows -> reachable plane -> dependent pair",
 "roadmap": "none",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.24,
 "caveat_type": "none",
 "recurring_anchor": "the two arrows v and w, and i-hat and j-hat",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 166,
 "median_beat_s": 34,
 "beat_sequence": ["hook","toy-world","definition","derivation","viewer-turn","payoff","generalize","wall","analogy","recap","teaser"],
 "top5_moves": ["toy-world","commit-to-answer","minimal-definition-then-refine","recap","teaser-next"],
 "absent3_moves": ["brute-force-first","failure-shown","second-person-role"]
}
```

```json
{"verified_trace": {"wpm": "PASS 166.00 (target 158.89-171.67, median 166.11)", "you_rate": "PASS 1.83 (target 1.82-2.39, median 2.17)", "i_rate": "FAIL 0.86 (target 0.92-1.44, median 1.15)", "we_rate": "PASS 0.69 (target 0.59-1.06, median 0.96)", "num_rate": "FAIL 4.36 (target 2.56-3.96, median 3.48)", "hedge_rate": "PASS 0.17 (target 0.14-0.28, median 0.23)", "example_rate": "FAIL 0.00 (target 0.24-0.42, median 0.31)", "q_rate": "PASS 0.17 (target 0.14-0.26, median 0.2)", "sent_len": "FAIL 18.55 (target 21.64-24.25, median 22.58)", "switch_sponsor": "PASS detected=False default=OFF", "switch_teaser": "PASS detected=True default=ON", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (premise-claim vs premise-claim)", "ending_type": "MATCHES default (teaser-next vs teaser-next)", "summary": "5/9 numeric targets pass"}}
```
