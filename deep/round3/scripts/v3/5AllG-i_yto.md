# Header
- channel: Reducible
- id: 5AllG-i_yto
- title: What if you had to invent a dynamic array?
- duration: 861 s (14:21)
- condition: v3
- recall: none
- exemplars read: VAt2mR7gY0k, FtwF6cmzamo

## Content skeleton
- Premise: a dynamic array is a list that grows by itself, and it can be invented from scratch.
- Fixed array as a row of boxes; index jumps are fast because the block is contiguous.
- The wall: the block cannot stretch because the neighbouring memory is taken.
- Brute-force growth by one slot per resize; count the copies, roughly n squared over two.
- Viewer turn: pause and guess how to grow it, then double instead of adding one.
- Tiny run (one box to sixteen) shows copying spikes that get rarer; geometric sum gives fewer than two n copies.
- Savings-jar argument (three coins per insert) explains amortized constant cost; caveats on memory, worst-case inserts, stale references.
- Impact coda on policy versus structure, sponsor read, teaser for the next layout.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | premise-claim: a list that grows by itself is everywhere, and we invent one |
| 0:40 | roadmap | here is the plan: wall, obvious fix, better policy, its costs |
| 1:00 | toy-world | a row of boxes in memory; jumping to a position is instant |
| 2:20 | wall | a row of four is full and the memory next door belongs to someone else |
| 3:10 | viewer-turn | pause and think about how you would grow it |
| 3:40 | brute-force | add one slot per resize, copy everything each time |
| 5:30 | derivation | the copy count adds to roughly n squared over two; short list versus a million |
| 7:40 | demo-sim | single box, then two, four, eight, sixteen; which inserts copy and how many |
| 9:30 | derivation | doubling sums to fewer than two n copies; the three-coin savings jar |
| 11:20 | caveat | amortized is an average; wasted memory, one slow insert, stale references, reserve |
| 12:30 | generalize | growth factor is a policy knob; same shape of argument in other structures |
| 13:05 | coda | why languages hide this, and what it means for hot loops |
| 14:03 | sponsor | generic developer-tool read with a link in the description |
| 14:12 | teaser | next video: a layout that avoids copying but gives up fast indexing |

<<<NARRATION
A dynamic array is a list that grows by itself. You keep adding things to it, and it never tells you it is full. Python lists work this way, and so do vectors in C plus plus and ArrayLists in Java. Almost every program you have ever run has one somewhere. Yet the mechanism is usually hidden, so let's pretend nobody has built one yet, and that we are the people who have to invent it.

Here is the plan. First we look at the thing we already have, then we hit a wall, then we try the obvious fix and measure what it costs. After that we look for a better policy, and finally we talk about what that policy costs us. In this video we will keep the structure simple and watch the numbers closely.

We start from something simpler. A plain array is a fixed block of memory, a row of boxes sitting side by side, and each box holds one value. The great thing about this layout is that we can jump straight to any box. If we want the box at position seven, we already know where it lives, because every box is the same size and they sit next to each other. That is why reading by index is so fast. The catch is that the row has a fixed length. Once it is full, it stays full.

Let's make that concrete. Say we have a row of four boxes and we want to add a fifth value. The obvious move is to make the row longer. But we cannot simply stretch it. The memory right after our last box might already belong to something else, some other variable or some other object, and we are not allowed to touch it.

This is the wall we keep running into, and it is worth staring at for a moment. Our data needs to sit in one contiguous block, because that contiguity is what makes access fast. But the space around that block is not ours to claim. So the only way forward is to find a bigger block somewhere else, copy everything over, and throw the old one away.

Pause here and think about how you would grow it. Take a moment, because the answer is not hard, and it is more interesting than it looks. Then let's try the most straightforward version. Every time we need to add an element and the row is full, we allocate a new block that is exactly one slot bigger. We copy all the old values across, we put the new value at the end, and we free the old block. That works. Every operation gives the right answer. The question is how expensive it is.

Let's count. Suppose we insert n items this way. The first insert copies nothing, the second copies one value, the third copies two, and so on. By the last insert we are copying almost n values. Add up all those copies and the total comes to roughly n times n minus one, divided by two. So about n squared over two copies in total, just to insert n things.

For a short list that is not terrible. For a list of a million items, the total is on the order of half a trillion element copies. Each insert ends up costing, on average, about half the length of the list. That is the brute-force answer, and it is the one I would write first if someone asked me to just make it work. Then I would want to make it better, because the copying is wasted effort in a very specific way. We keep moving the same old values again and again, and each time we gain only a single extra slot. We are paying a huge price for a tiny amount of room.

So here is a different question. What if, instead of growing by one, we grow by a lot more? For example, we double the size. When the row of four boxes is full, we make a row of eight. When that fills, we make a bigger row again, and so on. The shape of the rule matters more than the exact sizes, so keep your eye on the shape.

Let's walk through a small run to see what happens. Start with a single box. Insert the first value, and it fits. Insert the second, and the box is full, so we double to two boxes and copy one value across. Insert the third, and the two boxes are full, so we double to four and copy two values. The fourth insert fits into the free box. The fifth forces a double to eight and copies four values. The next few just write into empty boxes. The ninth forces a double to sixteen and copies eight values.

Look at the pattern of copying. The expensive steps happen at inserts two, three, five and nine, and the amount they copy doubles each time. Between those steps, the cheap inserts just write into an empty box. A resize is a big event, but it happens less and less often as the array grows. That is the whole trick, and it is sitting right there in the numbers. Notice also that the gap between expensive steps keeps growing, which is exactly why the total stays small.

Now let's add up the copies for the doubling version. To reach size n, the copies are one plus two plus four plus eight, all the way up to about n over two. A sum like that, where each term doubles, comes to just under n. So for n insertions in total, we have done fewer than about two n copies. That is a shocking change. We went from roughly n squared copies down to fewer than two n.

Here is the way I like to think about it. Averaged over the whole sequence, each insert costs a small constant number of copies. That average is what people mean when they say the cost is amortized constant time. Notice the word average. It does not say that every insert is fast. Most inserts are a single write. Every so often one insert is very slow, because it has to move everything.

There is a neat way to see where the cheap average comes from, and I think it is worth the detour. Imagine every insert pays three coins instead of one. One coin pays for writing the new value into its box. The other two coins go into a savings jar. Now think about the next resize. The half of the array that arrived since the last resize has banked two spare coins each. That is exactly enough to move everything at the next resize. The savings always cover the work, and three is a constant, so the cost per insert is constant on average.

I like this argument because it does not need any heavy machinery. It only asks you to notice that the expensive moments are paid for by the cheap moments that came before them. It takes a few minutes on paper, and we get more out of it when we work it through by hand, so it is worth doing.

Now let's look at a few things that matter in practice. The first is wasted memory. With doubling, the array can be half empty right after a resize. That is a real cost, and it is the price of the speed. Some implementations tune this choice and use a smaller growth factor, somewhere below two. The idea is the same. A smaller factor means resizes happen more often and the leftover space is smaller. A larger factor means fewer copies but more waste. That is a trade-off, and no single factor is correct for every workload.

Real libraries make different choices. As far as I know, a common C plus plus standard library doubles, while Java's ArrayList grows by about half. Python's list grows by a smaller percentage each time, so it resizes more often but wastes less space. I would not rely on those exact figures for anything important, because implementations change and I may be a bit off on the details. The point is that the growth rule is a design knob, and it is worth reading your own runtime's rule before betting on it.

The second thing is worst-case behavior, and this is the caveat I care about most. Amortized constant time does not mean every single insert is constant time. One unlucky insert can take time proportional to the whole array, because it triggers a copy of everything. For example, if your array holds a few million values, that one append can stall for a noticeable moment. If a system has to meet a deadline and one slow operation would break it, we need to know that. The average can look wonderful while the worst case still hurts. Real-time code often avoids this by spreading the copying across several later inserts instead of doing it all at once.

There is a practical consequence the math hides, and we should look at it. After a resize, the values live in a new block. Any pointer or reference that still points into the old block now points at memory that has been freed. So a dynamic array can invalidate references to its own elements. If we hold onto an element's address across an append, that address can break. This is a common source of bugs, and it is one reason languages often tell us not to keep those references around.

There is also an escape hatch. Suppose we know roughly how many items we will need, say ahead of a big import. We can ask for the capacity up front, and then the expensive resizes never happen at all. Many libraries expose exactly this kind of reserve call, and it is one of the cheapest performance wins we can make. Use it when you can, and do not guess blindly when you cannot.

The reverse operation has its own version of the same trick. If we remove many elements, the array can sit mostly empty and waste memory. Many implementations shrink the block when it falls below about a quarter full, and they shrink it to half. Shrinking at a quarter rather than at a half matters, because otherwise an alternating pattern of one insert and one removal could trigger a resize on every single step. The thresholds are chosen so that no single operation can flip the decision back and forth.

Let's step back and count what we actually changed. The data structure did not change much at all. We still have a contiguous block of boxes, we still jump to any index in constant time, and we still copy into a bigger block when we run out of room. The only thing we changed was the policy for when to make room. We stopped growing by one and started growing by a factor. That single change took the total cost from quadratic down to linear.

That, I think, is the most transferable lesson here. A lot of performance in programming comes from choosing a policy, not from building something exotic. If you find yourself doing something expensive over and over, ask whether you could do it less often and pay for it using the cheap steps in between. That question shows up in hash tables that rehash as they fill, in buffers that flush in batches, and in memory managers, and the same shape of argument keeps working.

It is also worth noticing why so many languages hide all this from you. The array does the resizing for you, and in most code you never have to think about it. The cost is still there, but the abstraction keeps you from paying attention to it. Knowing what sits underneath lets you use the abstraction well, and it lets you notice when an append inside a hot loop is quietly doing far more work than you think.

Before we go on, a word from our sponsor. This part of the video is brought to you by a company that builds tools for software developers. They asked me to mention their free trial, and I would encourage you to take a look if you are curious. I will leave a link in the description, and you are under no obligation to do anything with it.

In the next video, we are going to look at a structure that avoids this copying altogether. It uses a different layout, and it gives up the fast indexing we started with. That trade-off is the interesting part, so keep it in mind.
NARRATION>>>

```json
{
 "format_class": "premise-to-invention build, brute-force then policy change",
 "answer_given_upfront": false,
 "hook_type": "premise-claim",
 "first_question_frac": 0.22,
 "first_concrete_object_frac": 0.07,
 "first_new_idea_frac": 0.16,
 "first_notation_frac": 0.38,
 "payoff_frac": 0.72,
 "misconception": "staged-early",
 "brute_force_first": true,
 "examples_count": 4,
 "example_growth": "single box -> four boxes -> million-element list",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.22,
 "caveat_type": "approximation",
 "recurring_anchor": "the row of boxes and the wall beside it, returned to at each resize",
 "sponsor_frac": 0.98,
 "ending_type": "impact-coda",
 "teaser": true,
 "wpm": 172,
 "median_beat_s": 40,
 "beat_sequence": ["hook","roadmap","toy-world","wall","viewer-turn","brute-force","derivation","demo-sim","derivation","caveat","generalize","coda","sponsor","teaser"],
 "top5_moves": ["brute-force-first","toy-world","failure-shown","notation-after-concept","roadmap"],
 "absent3_moves": ["inline-quiz","humor","story"]
}
```
```json
{"verified_trace": {"wpm": "PASS 172.00 (target 163.32-184.1, median 172.25)", "you_rate": "PASS 1.08 (target 0.73-1.35, median 1.05)", "i_rate": "PASS 0.66 (target 0.46-1.1, median 0.75)", "we_rate": "PASS 3.20 (target 2.46-4.0, median 3.76)", "num_rate": "PASS 3.01 (target 1.82-3.19, median 2.56)", "hedge_rate": "PASS 0.19 (target 0.1-0.24, median 0.16)", "example_rate": "PASS 0.24 (target 0.15-0.37, median 0.22)", "switch_sponsor": "PASS detected=True default=ON", "switch_teaser": "PASS detected=True default=ON", "switch_roadmap": "PASS detected=True default=ON", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (premise-claim vs premise-claim)", "ending_type": "MATCHES default (impact-coda vs impact-coda)", "summary": "7/7 numeric targets pass"}}
```
