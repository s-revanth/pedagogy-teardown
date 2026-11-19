# Reducible: 5AllG-i_yto (v2)

- channel: Reducible
- id: 5AllG-i_yto
- title: What if you had to invent a dynamic array?
- duration: 861 s (14:21)
- condition: v2
- recall: none (I do not recall this video; written from the rulebook, the channel report and general knowledge of dynamic arrays)
- rulebook step 0: duration 14:21, so the over-10-min band; format design-it-yourself (invent-then-name comparison); title is a question and does not state the answer; solved problem; topic type data structures; no series label found.
- class chosen: invent-then-name comparison with two named builders; cost measured in copies; the fix found by failure; code last.
- exemplars read: `deep/compact/PMMc4VsIacU.txt` (DFS, read to about 16:00; invent-your-own-walk, then name; closest by format). `deep/compact/h7apO7q16V0.txt` (FFT; failure as stepping stone, notation after referent; closest by method).

## Content skeleton

- A fixed-size array fills up and a new item arrives; the video asks how to invent growth from fixed blocks.
- Two named builders, Ana (grow by one slot) and Ben (grow by a chunk of 100), each tested by total copying.
- Both hit the same quadratic wall; a guess-first pause on doubling.
- Doubling keeps total copying under twice the number of inserts; the average is named afterwards.
- Other places the trick appears (string buffers, hash tables, language lists) and one caveat about the single slow insert.
- Savings-account analogy for the amortized bill, then the code as a receipt, then a phrase-mirror ending.

## Beat sheet

| m:ss | beat | what is said or shown |
|---|---|---|
| 0:00 | hook | Question: a fixed array is full and a fifth item arrives. What do you do? The viewer is asked to try it first. |
| 0:25 | toy-world | Four blocks on screen, all full. The only rule: a block cannot grow. |
| 0:55 | definition | Minimal definition: a block, a count of used cells, a capacity. Refined once the cost of a new block appears. |
| 1:20 | brute-force | Ana grows by one cell whenever full: allocate one bigger, copy everything, insert. Run in full for five inserts. |
| 2:45 | demo-sim | Copy counter reads 0, 1, 2, 3, 4 for five inserts. The number of inserts gets its name, n, here, keyed to the five-insert run. |
| 3:45 | demo-sim | Ben grows by chunks of 100. Ten resizes over 1000 inserts, roughly 5000 copies, against about half a million for Ana. |
| 5:20 | wall | Both strategies share one shape: total copying climbs with the square of the list size. The failing property is named. |
| 5:50 | viewer-turn | Pause: guess the total copying for 1000 inserts if the block doubles. Choices: about a thousand, ten thousand, or half a million. Answer at about 6:10. |
| 6:15 | demo-sim | Doubling run: capacities 1, 2, 4, 8 and so on. Copies happen only at those sizes; the counter stays flat between them. |
| 6:40 | derivation | Decode the copy sum clause by clause: each term is one resize; the terms double; the total is under twice the largest term; so under twice the inserts. |
| 8:00 | payoff | Average copies per insert stays constant: amortized cost. Dry aside on the word. |
| 8:40 | generalize | Growable string buffers, hash-table resizing, language list types. |
| 9:30 | caveat | The average hides the one slow insert. Real-time buffers spread the copying across inserts. |
| 10:20 | demo-sim | Tiny to big: 4 slots, 16 slots, 1000 inserts. Copies per insert stay under two. |
| 12:20 | analogy | Savings account: each insert deposits coins; the big copy is paid from coins saved by earlier inserts. |
| 13:30 | derivation | Code last, as a receipt: block, capacity, count; double on full; copy; store. |
| 14:00 | sponsor | Sponsor read, placed at about 97.5% of runtime. |
| 14:08 | coda | Phrase mirror of the opening question ("if you had to invent..."). Runs to 14:21. |

## Narration

<<<NARRATION
Suppose the only data structure you have is a fixed-size array, and you allocate it with room for four items. That is that. Now it gets filled up, and a fifth item arrives. What do you do? We are going to answer that question together. By the end, we will have invented a dynamic array, a list that can grow, using nothing but fixed-size blocks. We will do it the way a real builder would do it: try the obvious thing, watch it break, and let the break tell us what to try next.

A pair of builders will help us. Ana and Ben start with the same problem and the same blocks, and each picks a strategy. Let's start with Ana, because her idea is the obvious one. When her block is full, she allocates a new block with a single extra slot, copies every item across, adds the new item, and throws the old block away. We can check that it works. Nothing gets lost.

Now let's ask what that costs. Imagine Ana inserts five items. The first fits. The second doesn't, so she copies a single item across. The next insert copies two items, and the one after that copies more. Every insert that hits a full block copies the entire list. With Ana's strategy, every insert hits a full block, so we keep paying for the whole list again and again.

Let's give the number of inserts a name, n. If k items are already stored, the next insert copies those k items. So to store n items, the total copying is nothing, plus a little, plus a little more, all the way up to n minus one. That sum grows like n squared over two. We can see the damage in a single figure: a long list costs half a million copies. You probably already sense that the figure is wrong before we finish adding it up.

Ben, perhaps, sees the trouble and makes a sensible change. Instead of growing by a single slot, he grows by a chunk of a hundred. Now a resize happens once per chunk, and that is a real improvement. Over a long run of inserts he resizes ten times, and the total copying comes to 5000. That is a tenth of Ana's total. We should be happy for him.

But look at the shape. Ben still copies the whole list at every chunk boundary. If we double the number of inserts, the resizes double, and each resize costs twice as much, so the total goes up by a factor of four. Ben has only shrunk the constant in front of the same square. Both builders hit the same wall, so we need a different kind of change.

Here is a question for you to pause on. Ben's trick was a bigger chunk. What if the chunk grows with the list itself? Pause and guess. If you resize by a factor of two instead, do you think the total copying for a long run of inserts is a thousand, ten thousand, or half a million? Make your guess now.

Okay, the answer is close to a thousand. Let's see why. The block goes from a single slot to twice that, then twice again, and so on. The copies happen at those sizes only. For a long run of inserts, the copies are powers of two, all the way up to the largest block. A list of doubling terms adds up to just under twice its largest term, so the total stays a little over a thousand copies. That is one copy per insert on average, and we can work with that.

Let's decode that sum clause by clause, because it is the heart of the video. Each term is the number of items copied during one resize. Each term is the size of the block at the moment it fills up. The terms double, so each one is as large as all the earlier ones added together. That makes the total less than twice the largest term. And the largest term is no bigger than the number of inserts. So total copying is less than twice n. Doubling turns the square into a straight line.

Now we can name the average. Computer scientists call it amortized cost. I know, it sounds like a bank statement. It just means the average over the whole history. Each insert costs a constant number of copies on average, even though a few individual inserts are expensive. That average is why the trick works, and it is exactly what we were inventing when we chose doubling.

This shows up in more places than arrays. Growable string buffers do it. Hash tables resize when they fill and do the same kind of copy. Many language list types do it quietly, so when we push an item onto one, we are standing on this same argument.

Now the caveat, because averages can hide things, and I'll be upfront on that point. A single insert that triggers a resize still copies the whole list. If we are building something where one slow operation matters, like a real-time audio buffer, the average is not enough. Some systems spread the copying across many inserts, so no single insert pays the entire bill. We should always ask which kind of guarantee our system needs.

Let's go tiny to big once more to see the shape. With four slots, we resize at the first few powers of two. With sixteen slots, we resize at every power of two up to sixteen. With a long run of inserts, the copy counter stops climbing as fast as the insert counter. The ratio of copies to inserts stays under two, no matter how far we go. I want you to watch the counter, not the array.

Think of it like a savings account. Each insert deposits a couple of coins, even the inserts that copy nothing. When the block fills and the big copy comes due, we pay it from coins saved by earlier inserts. Nobody goes broke, because the money was already there when the bill arrived.

Last, the code, as a receipt for everything we have watched. We keep a block, a capacity, and a count. On insert, if the count equals the capacity, we allocate a new block of twice the capacity, copy the items across, and swap the blocks. Then we store the new item and increase the count. That is a dynamic array. Let me say it plainly: the rest is detail, and in my experience most of that detail concerns memory.

So if you had to invent a dynamic array, I think you would land in the same place. Try the obvious thing. Watch it break. Then double.

This video is brought to you by a sponsor. There is a link in the description if you want to check them out, and thanks to them for supporting the channel.

Thanks for watching, and try the copy counter yourself.
NARRATION>>>

## Slots

```json
{
 "format_class": "invent-then-name comparison: two named builders, cost measured in copies, doubling found by failure, code last",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.0,
 "first_concrete_object_frac": 0.03,
 "first_new_idea_frac": 0.06,
 "first_notation_frac": 0.19,
 "payoff_frac": 0.56,
 "misconception": "none",
 "brute_force_first": true,
 "examples_count": 4,
 "example_growth": "5 inserts -> 16 slots -> 1000 inserts -> per-insert bound",
 "roadmap": "none",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.41,
 "caveat_type": "domain-limit",
 "recurring_anchor": "fixed array with copy counter, redrawn at every resize (5+ times)",
 "sponsor_frac": 0.975,
 "ending_type": "phrase-mirror",
 "teaser": false,
 "wpm": 172,
 "median_beat_s": 30,
 "beat_sequence": ["hook","toy-world","definition","brute-force","demo-sim","wall","viewer-turn","derivation","payoff","generalize","caveat","analogy","sponsor","coda"],
 "top5_moves": ["brute-force-first","visible-repetition","design-it-yourself","special-case-first","generalize-to-other-domains"],
 "absent3_moves": ["roadmap","callback-to-hook","humor"]
}
```

## rule_trace

```json
{"rule_trace": {
 "U1": "n/a: duration 14:21 is at least 10 min; no series label; title is second person, not first person; topic type is data structures, not one of the U1 topic types",
 "U2": "n/a: title is a question and the first 40 s pose the problem without stating the answer; doubling is not stated until about 6:10",
 "U3": "applied: final 10% (from about 12:55) ends on a phrase mirror (14:08); no hook callback because the hook question is closed by 6:15; no teaser because there is no series",
 "U4": "applied: the fixed array with a copy counter recurs at 0:25, 1:20, 2:45, 6:15, 10:20 and 13:30, each pass adding a layer",
 "U5": "applied: n is introduced at 2:45 with the five-insert run as referent; the cost sum is decoded at 6:40 after the concrete counts; no symbol precedes its referent",
 "U6": "applied: 172 wpm target (over-10 median); beats of 20 to 35 s; narration capped at 1800 words and written well under the cap",
 "U7": "applied: no front roadmap because only two parallel strategies are open, not three; inline signposts at 2:45, 5:20, 6:40; no vote or commit in the hook; no planted misconception",
 "U8": "applied: domain caveat at 9:30 (the average hides one slow insert; real-time buffers need spread-out copying)",
 "U9": "applied: binary choice (grow by one or double) gets one pause at 5:50 (0.41), answered within about 20 s",
 "U10": "n/a: no history of invention and no thesis with exemptions; the two builders are a comparison frame (C3), not a ladder",
 "U11": "n/a: title names an object (dynamic array), not an application, trigger event or end state",
 "C1": "applied: hint-led challenges for Ana and Ben, then the failing property (total copying grows with the square) is named at 5:20",
 "C2": "applied: definition-decode of the copy sum, clause by clause, at 6:40 (0.46 of runtime)",
 "C3": "applied: two named builders, Ana and Ben, carry the whole comparison",
 "C4": "n/a: the video names no application; the savings-account analogy is not an application",
 "C5": "applied: dry aside at 8:00 on the word amortized (sounds like a bank statement)",
 "D1": "n/a: question hook with no promise of beauty or surprise; the video does not clearly call for it",
 "D2": "applied: the grow-by-one scheme is run in full for five inserts with a copy counter before any other scheme",
 "D3": "applied: name (dynamic array) at 0:55 after the concrete block at 0:25; notation n at 2:45; code last at 13:30",
 "D4": "n/a: hook question closed by 6:15, so no callback; recap is default-off (B4); the closing mirror is a phrase mirror, not a recap",
 "N1": "applied: 172 wpm target (over-10 median). Narration is 1169 words, about 6.8 minutes of speech at 172 wpm; the rest of the 14:21 runtime is on-screen work and pauses",
 "N2": "applied: you/your 14 per 1169 words = 1.20 per 100 (band 0.73 to 1.35, median 1.05)",
 "N3": "applied: I/me/my 6 = 0.51 per 100 (band 0.46 to 1.10, median 0.75)",
 "N4": "applied: we/us/let us 34 = 2.91 per 100 (band 2.46 to 4.00, median 3.76)",
 "N5": "applied: numbers 31 = 2.65 per 100 (digit tokens plus spelled-out cardinals; band 1.82 to 3.19, median 2.56)",
 "N6": "applied: hedges 2 = 0.17 per 100 (band 0.10 to 0.24, median 0.16)",
 "N7": "applied: example cues 2 = 0.17 per 100 (band 0.15 to 0.37, median 0.22)",
 "B1": "applied: sponsor read at 14:00 (0.975 of runtime, inside the 96 to 99% band)",
 "B2": "n/a: no series label; U3 allows a teaser only in a series",
 "B3": "n/a: U7 blocks a front roadmap because fewer than three parallel open questions are open",
 "B4": "applied: default-off recap kept off; the ending is a phrase mirror"
}}
```
