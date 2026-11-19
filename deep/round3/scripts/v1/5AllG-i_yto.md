# Header

- channel: Reducible
- id: 5AllG-i_yto
- title: What if you had to invent a dynamic array?
- duration: 861 s (14:21)
- condition: v1
- recall: none

## Content skeleton

- Opens on the question of inventing a growable list from a fixed-size block of memory.
- Home problem: contiguous slots give O(1) indexing, but a full block has no room.
- Naive fix: grow by one, copy everything each time. Copy counts go quadratic (28 copies for 8 appends).
- Growing by a fixed chunk changes only the constant, not the shape of the cost.
- Doubling the capacity makes copies rare; a 1, 2, 4, 8 trace shows fifteen copies for sixteen appends.
- Geometric-sum argument gives amortized constant cost per append; a coin-purse picture explains why.
- Honest caveat: the count models copies only; allocator, cache and realloc behaviour and growth factors differ in real libraries.
- Ends by returning to the opening question and an exercise on growth factor three.

## Beat sheet

| m:ss | beat | what is said or shown |
|---|---|---|
| 0:00 | hook | Question: fixed-size arrays and a list that must grow; how would you invent one? |
| 0:25 | roadmap | Try the obvious idea, watch it break, follow the break. |
| 0:50 | definition | Home problem: slots in a row give a one-step jump to item i, but a full block has no room. |
| 1:50 | brute-force | Grow by one: allocate size plus one, copy everything, write the new item. |
| 3:20 | demo-sim | Copy counter for eight appends: zero through seven copies, total 28. |
| 5:00 | wall | Scaling: about n squared over two; a million appends means roughly half a trillion copies. |
| 6:10 | misconception-defuse | "Grow by a hundred instead": still about n squared over 2k, so the wall only moves. |
| 7:30 | derivation | Double the capacity instead; the next copy is far away. |
| 8:40 | demo-sim | Trace capacity one to sixteen with a running copy count: 1, 2, 4, 8, fifteen total. |
| 10:00 | derivation | Copies are powers of two below n; they sum to under 2n; amortized constant per append. |
| 10:50 | analogy | Coin purse: three coins per append; saved coins pay for future moves. |
| 11:45 | caveat | The count is a model: allocator time, cache misses, growth factor 1.5, realloc. |
| 12:35 | definition | Pseudocode for append, written after the idea is in place. |
| 13:00 | generalize | Same pattern in hash-table resizing and growable string buffers. |
| 13:20 | recap | Three moves: grow by one is quadratic; fixed chunk keeps the shape; doubling is linear. |
| 13:50 | callback | Back to the question; pause and try growth by three; the expensive copy was prepaid. |
| 14:10 | coda | Closing line; the video runs to 14:21. |

<<<NARRATION
Imagine you're writing a program in a language where arrays have a fixed size. You make one with room for five things, and the sixth thing has nowhere to go. You still want a list that grows. You want to keep adding to the end and never worry about the size.

So here's the question. What if you had to invent a dynamic array yourself, starting from nothing but a plain block of memory?

Let's do it the way you'd do it without knowing the answer. We'll try the obvious idea first, watch where it breaks, and let the break tell us what to try next.

First, what do we actually have? A block of memory with slots in a row. Each slot holds one item. The slots sit next to each other, so you can jump straight to item number i in one step. That's the whole reason arrays are fast. What we lack is room. The block has a fixed number of slots, and once it's full, the next item has nowhere to go.

So here's the obvious fix. When the block is full, make a new block that's one slot bigger. Copy every old item across. Put the new item at the end. Throw the old block away.

Let's count what that costs. The first append is free, because the block is empty. The second append fills a block of size one, so it copies one item into a new block of size two. The third append has to copy two items. The fourth copies three. In general, the k-th append copies k minus one items, because the block was exactly full just before it.

Let's go up to eight appends and add up the copies. Zero, one, two, three, four, five, six, seven. That's twenty eight copies to store eight items. Already the copying dwarfs the storing. This is the first place to stop and notice. Something is structurally wrong here, not just a little slow.

Here's the pattern. For n appends, the total copying is about n squared over two. If you double n, the work goes up by four. A million appends would mean roughly half a trillion copies, and at that point the list spends nearly all its time shuffling the same data around.

Some of you are probably thinking, fine, don't grow by one. Grow by a hundred. That's a reasonable instinct, so let's test it instead of trusting it. Say you grow by a fixed chunk k every time. You copy once every k appends, and each copy moves everything you have so far. The total still comes out to roughly n squared over two k. A bigger chunk only shrinks the constant in front. It doesn't change the shape of the curve. The curve still bends upward, and the wall is still there, just further away.

So the fix can't be a bigger constant. We need a different growth rule, and the cost tells us what to look for. Every copy pays for all the items again. What if copies happened so rarely that each one covered a lot of appends?

Here's the move. When the block is full, allocate a new block with twice the capacity. Now the next copy won't happen for a long time, because the new block has room for as many new items as you already had.

Let's trace it from capacity one, with a running count of copies. Append one fills the single slot. Append two finds the block full, so we make a block of size two and copy one item. Append three finds the size two block full, so we make size four and copy two items. Append four fits. Append five finds it full, so size eight, copying four items. Appends six, seven and eight fit without copying. Append nine triggers a copy of eight items into a block of size sixteen.

Now add up the copies from the first sixteen appends. One, two, four and eight. That's fifteen copies for sixteen appends. Notice how they're spread out. Most appends are a single write into a free slot. The big copies happen only at the doubling points, like rare milestones.

Let's make that general. Suppose you've done n appends. Every copy size is a power of two, and each one is smaller than n. The powers of two below n add up to less than twice n. So the total copying is under 2n, no matter how big n gets.

That's the whole trick in one line. The copies get bigger, but they get rarer at the same rate. Average the cost over the whole sequence, and each append costs a small constant amount of work. Computer scientists call that the amortized cost.

The word amortized can sound like magic, so let's make the mechanism concrete. Think of each append as carrying a purse of three coins. One coin pays for writing the new item. The other two are saved, and the new item keeps them for later. When a resize comes, the items added since the last resize have been saving their coins. In the doubling scheme, those items have exactly enough saved to pay for copying the older items. Nobody pays for a copy out of thin air. Each coin was set aside by an item that was going to need it.

Let's check the bookkeeping at the doubling point, since that's the part that matters. Suppose the capacity is c and the block is full. Since the last doubling, c over two items have been added, and each saved two coins. That's c coins. The next resize copies c items, and the coins cover it exactly.

Now the honest part. This bookkeeping is a model, not a stopwatch. It counts copies. It doesn't count the time to allocate memory, the time to free the old block, or the cache misses while copying. Some real libraries grow by a factor of one and a half instead of two. That gives back memory faster, but resizes come more often, and the constant changes. The shape of the answer doesn't change. C's realloc can sometimes extend a block in place, which makes some resizes nearly free. None of this breaks the core idea. It just means the textbook count is a model, not a clock.

Let me put the structure into code shape, since it helps once you know what it's doing. On append, if size equals capacity, allocate a new block with double the capacity, copy every item over, and point at the new block. Then write the new item at position size, and increase size by one. That's the whole thing. Two numbers, a block, and one rule about when to grow.

This pattern shows up beyond arrays. Hash tables resize their bucket arrays on a similar schedule. Growable string buffers do the same. Whenever you see a structure that keeps adding and occasionally rebuilds itself, look for the doubling rule and check the total work.

Let's recap the three moves, since they're the ones that matter. Growing by one looks natural, but its total copying is quadratic. Growing by a fixed chunk changes only the constant, so it still hits the wall. Doubling makes the total copying linear in the number of appends, which makes the average cost per append constant.

Now look back at the question. You didn't need to remember a clever data structure. You needed the first attempt that fails, a count of the copies, and the observation that copies could be made rarer. Each step was something you could have reached yourself, from a plain block of memory and a counter. That's what it means to invent a dynamic array.

Before you check the next step, try this. Suppose you grow by a factor of three instead of two. Does the total copying still stay linear? What's the average cost per append now, and what do you give up in wasted memory? Work it out on paper first, then see whether your answer matches the counting argument we just made.
NARRATION>>>

## Slots

```json
{
 "format_class": "invent-then-name, failure-driven build",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.0,
 "first_concrete_object_frac": 0.06,
 "first_new_idea_frac": 0.13,
 "first_notation_frac": 0.23,
 "payoff_frac": 0.7,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 4,
 "example_growth": "eight appends, then sixteen, then a million",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.96,
 "caveat_type": "approximation",
 "recurring_anchor": "running count of copies per append",
 "sponsor_frac": null,
 "ending_type": "hook-callback",
 "teaser": false,
 "wpm": 170,
 "median_beat_s": 50,
 "beat_sequence": ["hook", "roadmap", "definition", "brute-force", "demo-sim", "wall", "misconception-defuse", "derivation", "analogy", "caveat", "generalize", "recap", "callback", "coda"],
 "top5_moves": ["brute-force-first", "visible-repetition", "special-case-first", "misconception-first", "honest-caveat"],
 "absent3_moves": ["hook-paradox", "commit-to-answer", "running-character"]
}
```
