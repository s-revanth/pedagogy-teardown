# Header
- channel: Reducible
- id: 5AllG-i_yto
- title: What if you had to invent a dynamic array?
- duration: 861 s (14:21)
- condition: base
- recall: none

# Content skeleton
- Motivation: a fixed-size array cannot grow, yet programs need append.
- Naive fix: allocate a new array of size n+1 and copy everything on every insert, which is correct but quadratic in total work.
- Why it is slow: copies sum to 1+2+...+n, so the cost grows with n squared.
- Fix in two parts: keep spare capacity, and grow that capacity by a multiplier (doubling) instead of a fixed chunk.
- Amortized analysis: the copies from doubling sum to less than 2n, so each insert is amortized constant time; the claim is about any sequence, not average-case.
- Trade-off in the growth factor: 2 versus about 1.5 (memory waste against copying and allocator reuse). Ends by tying back to the shelf picture.

# Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Question: a shelf of fixed slots gets a sixth book. How do you build a list that grows? |
| 0:50 | toy-world | Bookshelf with five full slots, drawn as a row of boxes |
| 1:40 | definition | A plain array: size chosen at creation and then fixed |
| 2:20 | brute-force | Allocate n+1 slots, copy every item, place the new one. Correct, so it goes first |
| 3:40 | demo-sim | Copy counter ticks up one, two, three; running total shown beside it |
| 5:00 | wall | Total copies 1+...+n; 100 items gives 5,050; the curve is a parabola |
| 6:00 | analogy | Moving house every time you buy one book |
| 6:40 | derivation | Reserve spare room: adding a free write until the array is full |
| 7:40 | derivation | Fixed ten-slot chunks still quadratic; the chunk has to scale with size |
| 8:40 | derivation | Doubling: copies 1, 2, 4, 8, 16; each resize copies about the sum of all earlier ones |
| 9:50 | demo-sim | Table of inserts 1 to 16 with copy counts marking full moments; total 15 copies |
| 10:50 | misconception-defuse | Amortized is not average-case: every sequence of n inserts costs at most about 2n copies |
| 11:40 | analogy | Three coins per insert: one pays the write, two are saved on the new item to pay the next copy |
| 12:40 | generalize | Growth factor 1.5 versus 2: less waste and allocator reuse against more copying |
| 13:20 | viewer-turn | Pause: pick the growth factor for speed or for memory? |
| 13:50 | recap | Dynamic array = fixed array + spare room + a multiplier |
| 14:10 | coda | Next append is usually one write; the rare big move is spread across every insert |
| 14:21 | coda | End |

# Narration
<<<NARRATION
Imagine a bookshelf with exactly five slots, and every slot is already full. Someone hands you a sixth book. There is nowhere to put it. A plain array works like that shelf. You choose its size when you create it, and that size is fixed for the life of the array. But programs want a list that grows whenever you add something to it. So the question is simple to say and less simple to answer. How would you build a list that grows?

Let's start with the most obvious idea, even though it will turn out to be slow. Say you have an array holding n items, and it is completely full. To add one more item, you create a brand new array with room for n plus one. You copy every old item across, one by one. Then you place the new item at the end, and throw the old shelf away. That works. It is correct, and correctness is the first thing we need.

Now count the work. Adding the first item costs one copy. Adding the second costs two copies, because the first item has to be moved again. Adding the third costs three copies, and so on. If you build a list of a hundred items this way, the total number of copies is one plus two plus three, all the way up to a hundred. That sum is 5,050. Build a list of a thousand items and you are past half a million copies. The total grows with the square of the number of items. That is the wall this naive method hits, and it is worth staring at for a moment, because the rest of the video is about getting around it.

Here is a way to feel it. Imagine you move house every time you buy one new book. You pack every box, drive to a slightly bigger house, unpack everything, and then finally shelve the book. Nobody does that. You would rent a house with a spare room, and you would wait until the spare room was actually full before moving again.

So let's reserve spare room. Say our array has eight slots but we are only using five. Now adding an item is almost free. We write it into the next empty slot and we are done. Copying only happens when the array is actually full. The new question is how much spare room to add each time we run out.

Try adding a fixed chunk of ten slots every time. This helps a little, but it does not solve the problem. When the array is big, each resize still copies everything, and the resizes keep coming. If you work through the numbers, the total copying is still quadratic, just with a smaller constant in front of it. A fixed chunk is the wrong shape. The chunk has to grow along with the array.

So try doubling. When the array reaches capacity c, make a new one with capacity two times c, and copy over. Now look at the sequence of copies. The first resize copies one item. The next copies two. Then four, then eight, then sixteen. Notice that each resize copies about as many items as all the earlier resizes put together. One, then two, then four: the sum of everything before is always smaller than the copy you are about to make.

Here is a short table, so you can watch it happen. Start with capacity one. The array is full at inserts two, three, five and nine, and those are the moments that cost copies. Between them, inserts are just writes. Up to sixteen inserts, the total copying is one, plus two, plus four, plus eight, which is fifteen. Sixteen inserts, fifteen copies. Double the number of inserts and the copies roughly double too. The total work is a straight line now, not a parabola.

This is the central idea of amortized analysis. Individual inserts are not all cheap. Most of them are instant, and a few are expensive, and the expensive ones are very expensive. But if you look at a long run of inserts and divide the total work by the number of inserts, you get a fixed amount per insert. For doubling, that amount is about two copies. We call the cost amortized constant time.

Let me stress what that does and does not mean. We do not mean the average case. Nothing here is random. Every possible sequence of n inserts costs at most about two n copies, no matter what order you do things in. The guarantee is about any run of operations, not about typical runs. The expensive resizes are paid for by the many cheap inserts that came before them.

It helps to see that bookkeeping directly. Imagine each insert pays three coins. One coin pays for writing the new item, which is the work the insert really does. The other two coins go into a savings jar attached to the item that was just added. When the array becomes full and must resize, every item that arrived since the last resize has been carrying two saved coins. Those coins cover copying the old items across, and the bill is always covered. Nothing is ever short.

Now, doubling is not the only option. You could grow by a factor of one and a half instead. That changes the trade-off in two ways. First, it wastes less memory at any moment, because the spare room never gets as large as half the array. Second, it can let the memory allocator reuse space. When the array grows by one and a half times, the blocks you freed from earlier, smaller arrays can add up to enough room for the next one. With a factor of two, the freed blocks always fall just short. So a smaller factor means more copying in total, but less waste and sometimes better reuse. Real libraries choose different factors, and that choice is a trade-off, not a law of nature.

What about removing items? The same logic applies in reverse. If you shrink the array the moment it is half empty, you can get a bad pattern where one insert grows it and one delete shrinks it, and you pay a copy every single time. The usual fix is to shrink only when the array is a quarter full, and to shrink to half its size. That leaves a comfortable gap, so the expensive moves stay rare in both directions.

Let's notice what we did. We began with a shelf of fixed walls. We tried the obvious thing and measured it, and we saw the quadratic wall. Then we changed one part of the plan. We reserved spare room, and we made that room grow by a multiplier instead of a fixed amount. That one change turned a parabola into a straight line.

Now here is a question for you, and it is worth pausing on. If you were picking the growth factor for your own list, would you think about speed, or would you think about memory? Pause the video and decide. There is no single right answer, and the best choice depends on what your program does most. A program that rarely grows can tolerate large spare rooms. A program that is tight on memory cannot.

The same pattern shows up well outside arrays. Strings that you build by appending characters work this way. Hash tables that double when they get too full work this way. Whenever a structure must move its contents to a bigger home, and the move is rare enough, the cost of moving spreads thinly across all the cheap operations. That is the thing to take away.

Let's step back and sum up. A dynamic array is a fixed array plus two ideas. Keep spare room, and grow that room by a multiplier. Everything else is bookkeeping. Once you see those two ideas, the list types in most programming languages stop looking like magic. They are the same plan, with careful engineering around it.

So the next time you call append, think about what is happening behind the scenes. Most of the time, it is one write into an empty slot. Occasionally, it is a big move to a bigger house, and the bookshelf has to be emptied and refilled. Those big moves are rare enough that their cost is spread across every insert that came before them. That is why the cheap average is real, and why the design works.
NARRATION>>>

# Slots
```json
{
 "format_class": "problem-to-design tour, answer deferred",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.12,
 "first_notation_frac": 0.40,
 "payoff_frac": 0.82,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 4,
 "example_growth": "one more item -> fixed chunks -> doubling -> factor 1.5",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.94,
 "caveat_type": "none",
 "recurring_anchor": "the bookshelf of fixed slots, returned to at the end",
 "sponsor_frac": null,
 "ending_type": "hook-callback",
 "teaser": false,
 "wpm": 170,
 "median_beat_s": 55,
 "beat_sequence": ["hook", "toy-world", "definition", "brute-force", "demo-sim", "wall", "analogy", "derivation", "misconception-defuse", "generalize", "viewer-turn", "recap", "coda"],
 "top5_moves": ["brute-force-first", "hook-question", "analogy", "design-it-yourself", "visible-repetition"],
 "absent3_moves": ["humor", "story", "expert-dialogue"]
}
```
