# Reducible: Ty0JcR6Dvis (v2)

- channel: Reducible
- id: Ty0JcR6Dvis
- title: FFT Example: Unraveling the Recursion
- duration: 458 s (7:38)
- condition: v2
- recall: none (I do not recall this video; written from the rulebook, the channel report and general knowledge of the FFT recursion)
- rulebook step 0: duration 7:38, so the under-10-min band (U1 applies); series label "FFT Example" (a worked-example companion to the main FFT video); title is a process, not an answer; solved problem; topic type algorithms (not a U1 topic type); no first-person title.
- class chosen: short worked-example companion. One tiny input traced through a recursion, counted level by level, one caveat, then a teaser. No roadmap, recap, callback or notation (U1).
- exemplars read: `deep/compact/xlVX7dXLS64.txt` (BFS, 10 min; closest by duration and by a short, single-algorithm walk-through with no roadmap) and `deep/compact/h7apO7q16V0.txt` (FFT, 28 min; the same algorithm, used for the recursion and the combine step).

## Content skeleton

- Restates that the last video built the FFT; this one traces one tiny input through the recursion, move by move.
- Eight values read as polynomial coefficients; the job is the same at every level.
- Split into even and odd positions, recurse to single values, then the combine rule (sum and twisted difference).
- Count the combine steps level by level (4, 4, 4, so 12), with a guess pause before the count.
- Compare with the naive method (64 multiplications) and the sixteen-value scale-up.
- A merge-sort aside, one honest caveat about powers of two and padding, a teaser for the inverse, a sponsor read and a teaser-style ending.

## Beat sheet

| m:ss | beat | what is said or shown |
|---|---|---|
| 0:00 | hook | Question: what does the recursion actually do? We trace one small input. |
| 0:20 | toy-world | A full line of eight values, read as polynomial coefficients; the job is the same at every level. |
| 0:45 | definition | Minimal definition: a polynomial is just a list here. Dry aside on the word. |
| 1:10 | demo-sim | Split into even positions and odd positions: two lists, nothing computed yet. |
| 1:45 | demo-sim | Split each half again; the call tree is drawn; the same shape at every box. |
| 2:30 | demo-sim | Base case: a list of one value returns itself; all arithmetic waits for the way up. |
| 3:10 | derivation | Decode the combine rule clause by clause in words: keep the even value, twist the odd value, output the sum and the difference. |
| 3:50 | viewer-turn | Pause: guess the number of combine steps for eight values. Answer at 4:10. |
| 4:10 | derivation | Count level by level from the top: four, four, four; twelve in total. |
| 4:40 | brute-force | Naive method for comparison: every evaluation multiplies every value; 64 multiplications. Shown as a count. |
| 5:10 | payoff | Sixty-four down to twelve; sixteen values give 256 against about 32. Each combine is done once and reused. |
| 5:40 | generalize | Merge sort has the same split-and-combine shape; the same counting argument applies. |
| 6:20 | caveat | Power-of-two assumption; padding with filler values for messy inputs. |
| 6:50 | teaser | Next part: reverse the process and recover the original values. |
| 7:25 | sponsor | Sponsor read at 97.5% of runtime. |
| 7:35 | coda | Phrase mirror of the title: the recursion unravels once the combines are counted. Runs to 7:38. |

## Narration

<<<NARRATION
Last time we built the fast Fourier transform from the top down. Today we are going to take a small input and watch the recursion unfold, move by move. Nothing new appears here. I want to be clear on that from the start. The same pair of moves happens at every level, and only the size of the list changes. Let's go slowly, because the slow pace is the point.

Start with a short row of values, a full line of them. Think of them as the coefficients of a polynomial, written in order from the constant term upward. Yes, the word polynomial sounds intimidating. Here it is just a list, nothing more. The job is to evaluate that polynomial at a set of special points. We don't need those points yet. What we need to know is that the job looks the same at every level, and that is what makes the recursion work.

Here is what we will do: we split, we recurse, and we combine. The first move is a split. We take the values sitting in even positions and gather them into a single list. Then we take the values in odd positions and gather them into another list. Each new list has half as many entries as the original. Nothing has been computed yet. We have only sorted the input, and sorting is cheap. If you want a mental picture, imagine dealing a deck of cards into a pair of piles, alternating as you go.

Now apply the same move to each half. Take the first list and split it into evens and odds again. Then do the same to the second list. Each of those pieces is now a very short list. Let's pause on the call tree, the picture of what the function is doing. The top box calls a pair of boxes below it, and each of those calls a pair more. Every box has the same shape, and I want you to notice that shape from far away, because it tells you how much work is waiting underneath.

Keep going until there is nothing left to split. Every single box follows the same rule. A list with a single value is the base case. There is nothing to divide, so the function just hands back that lone value. That is the bottom of the tree, and at the bottom the work is trivial. We have not done any real arithmetic yet, and that is deliberate. For example, a single value needs no work at all. All the arithmetic happens on the way back up.

Now comes the combine step, where all the real work happens. Picture a pair of results sitting side by side, a value from the even list and another from the odd list. Each combine, perhaps the most important piece, takes the even value and the odd value. It twists the odd value by a fixed amount that depends only on its position. Then it produces a pair of outputs. The first output is their sum, and the second is their difference. Let's run a single combine on screen. The sum lands in a spot, the difference lands in the other, and both travel back up to the box above.

I think this is the key part, so let's decode that rule clause by clause. The even value is the thing we keep as it is. The odd value is the thing we twist. The sum and the difference are the pair of outputs that travel back up the tree. Nothing else happens inside a combine, and that is exactly why it is so easy to count. Let me say that again: count the combines. If we can count the combines, we can count the work.

Now, a question for you. Suppose the list were twice as long. How many more combines would we need? Consider the whole tree we just drew. How many combine steps do you think happen when we start with a list of eight values? Pause and count the levels. Consider how many merges happen at each level, and how the number of boxes changes as you go up. Make your guess now. You will probably guess a little low.

Here is the count, level by level, starting from the top. The top box merges both halves of four values each, and that is four combine steps, one for each pair of positions. Below it, there are boxes side by side, and each one merges its two halves of two values. Each of them needs a pair of combines, so that is four more. At the bottom, there are more boxes, and each needs one combine to merge its single values. That is four more again. Four, four, four. Twelve combine steps in total. We can check each level against the picture.

Now compare with the naive method. The naive way evaluates the polynomial at each of the eight points separately, and each evaluation multiplies every one of the values. That is eight times eight, or sixty-four multiplications. The recursion needs only twelve combines, plus some bookkeeping for the splits. So even at this tiny size, the gap is already large, and it is worth asking how that gap grows.

That is the payoff. My favourite part is watching the numbers fall apart. Sixty-four down to twelve for eight values. For sixteen values, the naive count is two hundred fifty-six, and the recursive count is thirty-two. Notice what happened there. The naive count quadruples when the list doubles, while the recursive count only doubles and adds a little. The savings come from doing each combine once and reusing its result on the way back up. Each level does the same kind of work, and we only do it once per piece.

The same halving move appears outside this algorithm. Merge sort splits a list in half, sorts each half, and merges them back together. Anything that splits a problem into smaller copies of itself and does a linear amount of combining has this shape. When we see that shape, we can reach for the same counting argument, and we can often predict the cost before writing any code.

One honest note. This count assumes the list length is a power of two, so every split comes out even all the way down. Real inputs rarely fit that shape. They need padding with filler values, or a more careful version of the split. The walk we just watched is the clean case, and the clean case is what the idea rests on. I'd keep that in mind before you apply the count to messy data.

In the next part, we will reverse the process and recover the original values from the transformed ones. The same recursion appears again, with a change at the end. That change is the interesting part, so do not skip ahead.

This video is brought to you by a sponsor. The link is in the description, and thanks to them for supporting the channel.

So the recursion is not magic. It is a split, then another split, then a combine per box. Count the combines, and the whole thing unravels.
NARRATION>>>

## Slots

```json
{
 "format_class": "short worked-example companion: one tiny input traced through a recursion, counted level by level, one caveat, then a teaser",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.0,
 "first_concrete_object_frac": 0.04,
 "first_new_idea_frac": 0.15,
 "first_notation_frac": null,
 "payoff_frac": 0.68,
 "misconception": "none",
 "brute_force_first": false,
 "examples_count": 3,
 "example_growth": "8 values -> 2 levels -> 16-value estimate",
 "roadmap": "none",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.5,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the eight-value list and its call tree, redrawn at each level (5+ times)",
 "sponsor_frac": 0.975,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 165,
 "median_beat_s": 22,
 "beat_sequence": ["hook","toy-world","definition","demo-sim","derivation","viewer-turn","brute-force","payoff","generalize","caveat","teaser","sponsor","coda"],
 "top5_moves": ["visible-repetition","inline-quiz","minimal-definition-then-refine","special-case-first","generalize-to-other-domains"],
 "absent3_moves": ["roadmap","recap","callback-to-hook"]
}
```

## rule_trace

```json
{"rule_trace": {
 "U1": "applied: duration 7:38 is under 10 min and the title carries the series label FFT Example; roadmap, recap, callback and notation are switched off, and beats run 20 to 25 s",
 "U2": "n/a: the title is a process (unraveling), not an answer; the first 40 s pose the input and the job, and the count lands at 4:10",
 "U3": "applied: final 10% (from 6:52) holds the teaser for the next part (6:50, series allowed), the sponsor read at 7:25 (0.975) and a phrase-mirror coda at 7:35; no hook callback because the hook question closes by 4:10",
 "U4": "applied: the eight-value list and its call tree recur at 0:20, 1:10, 1:45, 2:30, 3:10, 4:40 and 5:10, each pass adding a layer",
 "U5": "n/a: U1 drops notation under 10 minutes; the script uses no symbols, and the sums and counts are spoken in words and plain numbers",
 "U6": "applied: 165 wpm target for a short video (inside the pooled 140 to 191 range, low-middle); beats of 20 to 25 s",
 "U7": "applied: no front roadmap (U1, and the video has no three parallel open questions); no vote or commit in the hook; no planted misconception; inline signposts only",
 "U8": "applied: domain caveat at 6:20 (the count assumes a power-of-two length; messy inputs need padding), typed as domain-limit",
 "U9": "applied: one viewer turn at 3:50 (0.50) on the number of combine steps, which the payoff depends on; answered at 4:10",
 "U10": "n/a: no history of invention, no thesis with exemptions, no escalating antagonist",
 "U11": "n/a: the title names an algorithm (FFT), not an application, trigger event or end state",
 "C1": "n/a: no hint-led counterexample; the video is a single trace, not a property hunt",
 "C2": "applied: the combine rule is decoded clause by clause in words at 3:10 (0.42 of runtime), with no symbols",
 "C3": "n/a: the comparison is counts, not two named solvers",
 "C4": "n/a: no named application; merge sort at 5:40 is a related algorithm, not an application",
 "C5": "applied: dry self-aware aside on the word polynomial sounding intimidating at 0:45",
 "D1": "n/a: the hook is a question with no promise of beauty or surprise; a worked-example companion does not clearly call for it",
 "D2": "n/a: the naive method appears as a count (64 multiplications) rather than run in full; short-video format",
 "D3": "applied: the walk comes before any new name; the algorithm name in the opening line is a reference to the previous video; no notation and no code",
 "D4": "n/a: U1 drops the recap and the callback under 10 minutes; the closing mirror is a phrase mirror, not a recap",
 "N1": "n/a: the N1 table has only an over-10-min row; the short-video pace is set by U6 at 165 wpm",
 "N2": "applied: you/your 11 per 1199 words = 0.92 per 100 (band 0.73 to 1.35, median 1.05)",
 "N3": "applied: I/me/my 6 = 0.50 per 100 (band 0.46 to 1.10, median 0.75)",
 "N4": "applied: we/us/let's 30 = 2.50 per 100 (band 2.46 to 4.00, median 3.76)",
 "N5": "applied: numbers 34 = 2.84 per 100 (digit tokens plus spelled-out cardinals; band 1.82 to 3.19, median 2.56)",
 "N6": "applied: hedges 2 = 0.17 per 100 (band 0.10 to 0.24, median 0.16)",
 "N7": "applied: example cues 3 = 0.25 per 100 (band 0.15 to 0.37, median 0.22)",
 "B1": "applied: sponsor read at 7:25 (0.975 of runtime, inside the 96 to 99% band)",
 "B2": "applied: teaser for the next part at 6:50 (series label present, so U3 allows it)",
 "B3": "n/a: U1 drops the roadmap under 10 minutes",
 "B4": "applied: default-off recap kept off"
}}
```
