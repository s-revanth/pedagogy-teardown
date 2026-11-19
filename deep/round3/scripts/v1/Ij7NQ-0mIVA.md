# Header

- channel: Reducible
- id: Ij7NQ-0mIVA
- title: The Simple and Elegant Idea behind Efficient Dynamic Arrays
- duration: 473 s (7:53)
- condition: v1
- recall: none

## Content skeleton

- Puzzle: a resize copies everything, so one append can be expensive; why is appending cheap on average?
- Setup: capacity and size; writes are cheap, the resize copy is the expensive part.
- Count for eight appends: eight writes plus copies of 1, 2 and 4 items, fifteen operations in total.
- Coin model: each append carries three coins; one pays the write, two are saved on the new item.
- Check at append nine: items five through eight each saved two coins, eight coins, exactly covering the copy of eight items.
- General rule: after a doubling to capacity c, c over two items save two coins each, covering the next copy of c.
- Honest caveat: bookkeeping, not a stopwatch; a potential function gives the same bound.
- Misconception cleared: one slow append does not make the average slow; the rare bill is spread over cheap payments.

## Beat sheet

| m:ss | beat | what is said or shown |
|---|---|---|
| 0:00 | hook | Question: a resize can copy everything, so how can appends be cheap on average? |
| 0:20 | roadmap | Give each append a price and let the items save up for the expensive moment. |
| 0:35 | definition | Array with capacity and size; writes are cheap; the full-array event allocates double and copies all. |
| 1:30 | demo-sim | Eight appends: eight writes; resizes copy one, two and four items; fifteen operations. |
| 2:45 | analogy | Coin purse: each append carries three coins; one pays the write, two are saved on the item. |
| 3:30 | derivation | Saved coins pay for the item's own future move and for one older item's move. |
| 4:20 | demo-sim | Append nine: the array is full at eight; items five through eight hold eight coins; the copy of eight is paid. |
| 4:50 | viewer-turn | Pause: sixteen items are in a full array; how many coins sit on items since the last resize, and does that cover the next copy? |
| 5:20 | generalize | Answer: items nine through sixteen, eight items, sixteen coins; general rule for any capacity c. |
| 6:00 | caveat | Bookkeeping is a model; a different growth factor changes coin amounts; a potential function gives the same bound. |
| 6:50 | misconception-defuse | Planted idea: a slow resize makes appends slow; the rare bill averages over many cheap payments. |
| 7:10 | recap | Each append pays three coins, one to write and two saved; a resize is covered by coins from items added since the last one. |
| 7:30 | callback | Back to the puzzle: the expensive copy was prepaid by the items that came before it. |
| 7:45 | coda | Closing line; the video runs to 7:53. |

<<<NARRATION
Here's a puzzle. A dynamic array sometimes has to copy everything when it's full, so a single append can be expensive. But appending is cheap on average. How can both be true? Let's find out with a bookkeeping trick that doesn't need any heavy algebra.

Our plan is one line. Give every append a price, and let the items save up for the expensive moment.

Start with the setup. The array has a capacity and a size. Appends write into the next free slot. When the size reaches the capacity, the next append allocates a block with double the capacity, copies everything across, and then writes the new item. The copying is the expensive part. The writing is cheap.

Let's count the real work for eight appends. Each append writes once, so that's eight writes. The resizes happen when we append the second, third and fifth items, because the array is full each time. Those copy one, two and four items, so seven copies. The total work for eight appends is fifteen operations. Fifteen for eight appends, which is under two each.

Now the bookkeeping. Imagine each append comes with a purse of three coins. One coin pays for writing the new item. That leaves two coins. The new item keeps those two coins for itself, saved for the future. Here's the rule. One saved coin pays for this item's own move the next time the array resizes. The other saved coin pays for moving an older item.

Let's test the rule at the moment that matters. Append nine. The array was full at eight items, so we have to copy eight items into a block of size sixteen. That's expensive. Who pays? The resize that made capacity eight happened when we appended item five. So the items added after that copy were five, six, seven and eight. Each one saved two coins. That's four items times two coins, which is eight coins. Eight coins to copy eight items. The expensive copy is paid for exactly.

Notice what happened. The copy at item nine wasn't a surprise. It was prepaid, one coin at a time, by the items that were already sitting in the array. Each one was saving up for the move that would eventually happen to it, and to one of its older neighbours.

The same check works at every size, so let's try a smaller one. The resize at append five copied four items. The resize before that, at append three, made capacity four, and the items added after it were three and four. Each of them saved two coins, so that's four coins for four copies. Every copy has a payer, and the payer is always an item that arrived after the last big move.

Now the total for eight appends. We collected three coins per append, so twenty four coins in all. We spent fifteen of them on writes and copies. The remaining nine are still saved on the items, waiting for the next resize. The bill never went unpaid, and nothing had to be borrowed from the future.

You could try charging the copy cost at the moment it happens. But then the append that resizes would look enormous, and every cheap append would look free. That hides the pattern. Spreading the bill is an accounting choice, and it's exactly the choice that makes the average visible.

Now a question for you to try before I give the answer. Suppose you've appended sixteen items, and the array is full. How many saved coins are sitting on the items added since the last resize? Does that cover the next copy of sixteen items? Pause and work it out.

Here's the answer. The last resize happened at item nine, when capacity went from eight to sixteen. So the items added since then are nine through sixteen. That's eight items, each with two saved coins, which is sixteen coins. The next resize copies sixteen items, and the sixteen coins cover it exactly.

Let's make that general. Suppose the capacity is c, and the array is full. The last doubling produced capacity c. Since then, c over two items have been added, and each saved two coins. That's c coins. The next resize copies c items, and the saved coins cover it, every time, at every size. So every append pays three coins in total, and the total work for n appends is at most three n. The average is a constant.

Now the honest part. This is accounting, not a stopwatch. The coins are a way to show the bill is covered. They don't tell you how long a memory allocation takes, or how the cache behaves while copying. A library that grows by one and a half instead of two would use different coin amounts, and the constant would change. The argument is about the shape of the total cost, not the exact number. There's another bookkeeping method, called a potential function, that gets the same answer with different arithmetic, so you can pick whichever feels natural.

Here's a misconception to clear up. Some people hear that the resize is expensive and conclude that appends are slow. But one slow operation doesn't make the average slow. The resize is rare, and its cost is spread over all the cheap appends that came before it. That spreading is the whole idea. A rare large bill, averaged over many small payments, is a small bill per payment.

If you want to convince yourself, do it on paper. Keep a running tally of coins after each append, write down each copy as it happens, and watch the saved coins cover every resize. The numbers we used here will come out the same, and you'll see the pattern for yourself, which is more convincing than any algebra.

Let's recap. Each append pays three coins, one to write and two saved. A resize copies everything, and the saved coins from items added since the last resize cover it. So the average cost per append is constant, even though a single append can be expensive.

Back to the puzzle. The expensive copy wasn't a surprise. It was paid for in advance, by the items that came before it.

Thanks for watching.
NARRATION>>>

## Slots

```json
{
 "format_class": "accounting argument, prepaid coins, puzzle-then-resolve",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.0,
 "first_concrete_object_frac": 0.07,
 "first_new_idea_frac": 0.07,
 "first_notation_frac": 0.74,
 "payoff_frac": 0.55,
 "misconception": "planted-myth-defused",
 "brute_force_first": false,
 "examples_count": 3,
 "example_growth": "eight appends, then append nine, then any capacity c",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.61,
 "caveat_type": "approximation",
 "recurring_anchor": "the coin purse of three coins per append",
 "sponsor_frac": null,
 "ending_type": "hook-callback",
 "teaser": false,
 "wpm": 170,
 "median_beat_s": 30,
 "beat_sequence": ["hook", "roadmap", "definition", "demo-sim", "analogy", "derivation", "viewer-turn", "generalize", "caveat", "misconception-defuse", "recap", "callback", "coda"],
 "top5_moves": ["analogy", "visible-repetition", "misconception-first", "inline-quiz", "generalize-to-other-domains"],
 "absent3_moves": ["hook-paradox", "running-character", "rule-list"]
}
```
