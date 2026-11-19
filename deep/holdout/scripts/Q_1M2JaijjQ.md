# Predicted script: Reducible, "What Is Big O Notation?"

- Channel: Reducible
- Video id: Q_1M2JaijjQ
- Target duration: 1065 s (17:45)
- Recall risk: **vague**. I know this channel makes an algorithms-analysis video under this title and I have a loose sense of the topic list (counting steps, growth rates, binary search). I have no memory of its order, examples or wording. Everything below is built from the Reducible report, the round-1 findings and general subject knowledge.

## 1. Predicted beat sheet

| Time | H/B/N/I | Move tags | Narrator says / does | On screen |
|---|---|---|---|---|
| 0:00 | H | hook-question, hook-paradox | Two programs solve the same task. On 10 inputs both finish instantly; on 10 million one finishes and one outlasts your patience. Why? | Two progress bars, one stalls; input-size slider |
| 0:35 | H | minimal-definition-then-refine | Define an algorithm and input size n in the smallest terms: "a recipe" and "how much stuff it chews on" | Circle row of n items, label n |
| 1:00 | N | roadmap | Plan: (1) a way to measure cost that survives changing laptops, (2) count it on three examples, (3) throw away what does not matter, (4) the name and the definition | Four-slot plan with the last slot greyed |
| 1:30 | H | act-it-out, brute-force-first | Home problem: is the number 42 in this list? Walk it by hand, left to right | Row of boxes, a cursor stepping | 
| 2:20 | N | failure-shown | Time it with a stopwatch: laptop A 2 s, laptop B 0.4 s, a phone 9 s. Stopwatch measures the machine, not the idea | Three devices with timers, mismatching |
| 3:10 | N | minimal-definition-then-refine, toy-world | New rule: count basic steps (compare, add, jump). One step = one unit | Step counter beside cursor |
| 3:50 | N | special-case-first, visible-repetition | Linear search worst case at n=4, 8, 16: 4, 8, 16 steps; pattern is "as many as items" | Three stacked rows, counter ticks identically |
| 5:05 | I | notation-after-concept | Only now the label: this is O(n) | "O(n)" tag slides onto the three rows |
| 5:40 | N | design-it-yourself, special-case-first | Duplicate check: compare every pair. n=3 has 3 pairs, n=4 has 6, n=5 has 10; guess n=6 | Pair grid filling, a count column |
| 7:20 | N | inline-quiz, commit-to-answer | Pause: for n=100, roughly how many comparisons? Commit before the grid answers | Empty square grid, countdown |
| 7:50 | I | notation-after-concept | Roughly n squared over two; O(n^2) | Triangle area inside the square |
| 8:35 | N | simulation-as-argument | Cost 3n+5 vs n; plot both for n=10, 1000, 100000; the ratio settles at 3, the +5 vanishes | Overlaid curves, ratio readout |
| 9:40 | N | honest-caveat, misconception-first | Misconception: O(n) always beats O(n^2). Show small n where the quadratic with tiny constant wins; Big O speaks about growth, not small inputs | Crossover plot, shaded region |
| 10:50 | H | analogy | Guess-a-number game, "higher/lower" | Number line, two players |
| 11:15 | N | act-it-out, special-case-first | Binary search by hand on a sorted list of 16: halve each time; 4 steps. 32 gives 5 | Sorted row, window shrinking, step counter |
| 12:50 | N | visible-repetition, simulation-as-argument | 1,000 items: 10 steps. 1,000,000: 20. A billion: 30 | Counter table scaling |
| 13:40 | I | notation-after-concept | Name: O(log n), "how many times can you halve n" | Halving tree |
| 14:15 | N | failure-shown, cost-in-learner-units | At a billion steps per second, compare n, n log n, n^2, 2^n for n=50 and 100: seconds, days, ages of the universe | Table, units flip from ms to years |
| 15:25 | I | notation-after-concept, rule-list | Formal receipt: f(n) is O(g(n)) if some constant times g beats f from some n onward; two rules: drop constants, keep the dominant term | Definition on screen with the 3n+5 plot as example |
| 16:20 | N | honest-caveat | Worst vs typical case; Big O hides constants and memory; it is a tool for comparing growth | Caveat card |
| 16:55 | N | recap, callback-to-hook | Recap of count, drop, name; answer to the opening two programs: one was O(n), one O(n^2) | Opening bars, now labelled |
| 17:30 | N | teaser-next | Next: analyzing recursive algorithms | Recursion tree thumbnail |

## 2. Full narration script

[0:00] Here is a strange fact about code. You can write a program, test it on ten inputs, and it finishes before you blink. Then you give it ten million inputs, and it just sits there. Meanwhile, a friend's program solving the exact same task handles ten million without trouble. Same problem, same computer. So what is actually different between the two programs?

It is not the language, and it is not how clever the syntax is. It is something about how the amount of work grows as the input grows. And the tool people use to talk about that growth is called Big O notation.

Now, if you have seen Big O before, you may have seen it as a bit of notation to memorize: O of n, O of n squared, O of log n. In this video I want to do it the other way around. We will start with a problem, try to measure the cost of solving it, run into trouble, and see that the notation is just a name for the fix. By the end, I think you will feel that you could have invented it yourself.

[0:35] Let us set the smallest possible vocabulary. An algorithm is just a recipe, a fixed list of instructions for solving a problem. And the input size, which we will call n, is how much stuff the recipe has to chew on. If the problem is about a list, n is the number of items in the list. If it is about a picture, n might be the number of pixels. We will refine this later, but that is enough to get started.

[1:00] Here is the plan. First, we need a way to measure the cost of an algorithm that does not change when you change laptops. Second, we will count that cost on a few small examples by hand. Third, we will notice that most of what we counted does not matter, and throw it away. And fourth, only then, we will give the leftover a name and write down the real definition. I am leaving that last slot empty on purpose. We will come back and fill it in.

[1:30] Let us begin with a problem you could solve in your sleep. I give you a list of numbers and ask: is the number 42 in here?

Do it the way you naturally would. Look at the first number. Not 42. Look at the second. Not 42. Third. Fourth. You keep going left to right until you either find 42 or run out of list. This approach is called linear search, and I want you to notice how plain it is. There is no trick. It is the obvious thing.

[2:20] Now, how expensive is this? The most natural idea is to time it. So let us run this on my laptop. Two seconds. Now run it on an older laptop: it takes nearly nine. Now on a faster machine: less than half a second. Three machines, three completely different answers, and none of them tells us anything about the recipe itself. The stopwatch is measuring the hardware, the programming language, even whatever else the computer happened to be doing, rather than the algorithm. So timing in seconds is a dead end if we want a statement about the idea.

[3:10] So here is a different plan. Let us count the basic steps instead. Comparing two numbers, adding two numbers, moving to the next position: call each of these one step, one unit of cost. This is a simplification, and I will be honest that real processors do not treat every operation as equal. But it lets us ask a question that does not depend on the machine: how many steps does the recipe take?

[3:50] Let us count for linear search, and let us take the worst case, where 42 is the very last item or not there at all. With a list of four items, we check four numbers: four steps. With eight items, we check eight: eight steps. With sixteen items, we check sixteen. Watch the counter carefully each time, because I am doing exactly the same walk each time. The list doubles, and the steps double. The number of steps grows in step with the number of items.

[5:05] That relationship deserves a short name. We say linear search takes order n steps, and write it O of n. The O stands for order, as in "on the order of." And notice what it is: a label for a pattern we have already watched happen, not a new idea.

[5:40] Let us try a second problem. I hand you a list and ask: does any number appear twice? The obvious approach is to compare every item with every other item. So how many comparisons is that?

Let us work small. With three items, the pairs are one-two, one-three, two-three: three comparisons. With four items, we add a fourth item that must be compared with each of the three before it, so we get six. With five items, the new one is compared with four others, so ten. Before I show you six items, pause and guess. Do you see how the number grows?

It went three, six, ten, so the next one adds five, giving fifteen.

[7:20] Now a harder question, and this time I want you to actually commit to an answer. With a hundred items, roughly how many comparisons? Take a moment. Do not compute exactly; just estimate. Think about the grid of every item against every item.

[7:50] Here is one way to see it. Draw a square grid, with the items along both sides. Every cell is a pair. But comparing item three with item seven is the same as comparing seven with three, and comparing an item with itself is pointless. So we only need about half the square, a triangle. The square has n times n cells, so the triangle has about n squared over two. For a hundred items, around five thousand comparisons. Compared with the hundred steps of linear search, that is a very different animal. This growth, where doubling the list roughly quadruples the work, we write as O of n squared.

[8:15] Before we go on, let me show you how this looks in code, because this is where you will meet it in practice. A single loop that walks over the list once, doing one comparison per item, is the linear search we already counted. Put a second loop inside the first, so that for every item you walk the whole list again, and you get n times n steps. You do not need to run anything to see this. Count how deeply loops are nested, and you already have a rough guess for the exponent. One loop, order n. Two nested, order n squared. Three nested, order n cubed. And two loops placed one after the other, not inside each other, simply add: n plus n is two n, which, as we are about to see, is still order n.

[8:35] Now something should bother you. When I said linear search takes n steps, I was ignoring that checking each number really takes a few steps: a comparison, a move, a check that we are not at the end. So perhaps the true count is three n plus five. Does that matter? Let us plot three n plus five next to n itself. For n equal to ten, the gap looks huge: thirty-five against ten. For a thousand, it is three thousand and five against a thousand. For a hundred thousand, the five is a rounding error, and the ratio between the two curves has settled at three. The constant five has vanished, and the three just stretches the line without changing its character.

So that is our second discovery. If we care about how the cost grows, we can throw away the added constants, and we can throw away multiplication by a constant. Only the shape matters.

The same thing happens when two different growth rates are added together. Take a recipe that costs n squared plus n. For n equal to ten, that is a hundred and ten, and the n is a noticeable ten percent. For a thousand, the square is a million and the n adds a thousand, which is a tenth of a percent. For a million, the extra n is a rounding error on a trillion. Whichever term grows fastest eventually swallows the rest. So when we describe a cost, we keep only that dominant term. n squared plus n is order n squared. Three n cubed plus ten n squared plus a hundred is order n cubed. This is why Big O descriptions look so short: they are what is left after everything that stops mattering has been thrown away.

[9:40] Here is where a very common misconception creeps in. People hear that O of n is better than O of n squared and conclude that an O of n algorithm is always faster. It is not. Suppose one recipe takes a hundred n steps and another takes n squared. For n equal to ten, the quadratic costs a hundred, and the linear one costs a thousand. The quadratic wins. They tie at n equal to a hundred, and beyond that the linear one wins forever. So Big O does not say which is faster on a given input. It says who wins once the input gets big enough. For small inputs, constants can and do decide. That is a real limitation, and any time someone tells you an algorithm is better because of its Big O, ask how large the input is.

[10:50] Now I want to look at something that goes in the opposite direction, an algorithm that gets much, much better than linear. Think of the game where I pick a number between one and a hundred and you guess, and I only answer higher or lower. A bad strategy is to guess one, two, three, and so on. That is linear search again. A good player guesses fifty. Higher or lower, and half the possibilities disappear instantly.

[11:15] We can do this with a list too, as long as the list is sorted. Take sixteen numbers in order and look for a target. Check the middle. If the target is bigger, the left half is gone; if it is smaller, the right half is gone. Now check the middle of what remains. Eight items, then four, then two, then one. That is four steps for sixteen items. Let us double the list to thirty-two: one extra halving, so five steps. Double again to sixty-four: six steps. Each time the list doubles, we pay one extra step and no more.

[12:50] Let us push this. A list of a thousand items needs about ten steps. A million items: twenty steps. A billion items: thirty steps. I want you to sit with that for a second. A billion items, and we answer after thirty looks. Meanwhile, linear search would be looking a billion times.

[13:40] The question we are really asking is: how many times can you halve n before you reach one? That number is called the logarithm of n, base two, and so this algorithm, called binary search, takes order log n steps, written O of log n. Again, notice the name arrived last. We saw halving, we counted it, and only now we wrote the symbol.

[14:00] There is one more rate worth meeting, because it is where good sorting algorithms live. Suppose you want to sort a list. A natural idea is to split the list in half, sort each half, and merge the two sorted halves together. Merging costs about n steps, since you walk both halves once. And how many times can we split before the pieces have one item? Log n times, the same halving count as before. So we pay about n steps at each of log n levels, which gives n times log n. Compare that to the simple approach of repeatedly picking the smallest remaining item, which compares every item with every other and costs n squared. For a million items, n log n is about twenty million steps, and n squared is a trillion. That gap, a trillion against twenty million, is the reason sorting algorithms were worth inventing.

[14:15] To feel how different these growth rates are, let us put time on them, in units you can imagine waiting for. Suppose the computer does a billion simple steps per second. With a hundred items: log n finishes instantly, n finishes instantly, n squared takes ten microseconds. Fine. Now take a million items. Log n is still instant. Linear search takes a thousandth of a second. But n squared takes a thousand seconds, over a quarter of an hour. Go to a billion items: linear is one second, and n squared is about thirty years.

And there is a worse family. Some algorithms take two to the n steps, doubling with every extra item. With just fifty items, that is about two weeks. With a hundred items, it is longer than the age of the universe. Same computer. That is the real meaning of "does not scale."

[15:25] Now we can fill in the last slot of the plan, the formal definition. We say that a cost function f of n is O of g of n if, past some point, a constant multiple of g sits above f. In other words, I am allowed to pick a constant, and I am allowed to start caring only from some n onward. Look back at three n plus five. Take g to be n, pick the constant four, and from n equal to five onward, four n is always at least three n plus five. So three n plus five is O of n. And you can see the two rules we found by hand are baked in: constants disappear, and only the part that grows fastest survives.

[16:20] A few honest caveats before we finish. We counted the worst case, but some algorithms behave differently on typical input. We counted steps and ignored memory. And we treated every step as the same size, which real hardware does not. Big O is a tool for comparing how recipes grow, not a prediction of how many milliseconds your program takes.

[16:55] So let us recap. To measure an algorithm, do not time it. Count steps. Then notice that constants and small terms wash out, and describe only the shape of the growth. That shape has names: linear, quadratic, logarithmic, exponential, and the notation O is just a short way to say them.

And that brings us back to the two programs at the start. One scanned the data once, an O of n recipe. The other compared everything with everything, an O of n squared recipe. On ten items you could not tell. On ten million, one needs a fraction of a second and the other needs more than a day.

[17:30] In the next video, we will use the same counting idea on recursive algorithms, where counting steps gets more interesting. See you there.

## 3. Rule trace

| Beat | Report claim / move that produced it |
|---|---|
| 0:00 hook | Sec. 3: hook-question 9/12 and hook-paradox 5/12; JPEG's paradox opening. Chosen because "same task, wildly different cost" is a paradox about cost. |
| 0:35 minimal definition | Sec. 3: minimal-definition-then-refine 12/12 (graph theory circles-and-lines first). |
| 1:00 roadmap | Roadmap 12/12 and new principle 5 (plan with named empty slots, FFT magic box). I left the definition as the empty slot, to be closed at 15:25. |
| 1:30 linear search by hand | Principle 5 act-it-out (DFS long literal walk), principle 6 brute force first. |
| 2:20 stopwatch fails | New principle 1 (failure is the stepping stone) and failure-shown 6/12; the tool "step counting" is introduced as a repair. |
| 3:10 step counter | Honest-caveat 11/12 (PNG 3:28 misleading number). |
| 3:50 n=4, 8, 16 | Principle 9 and 10 (repeat across examples, tiny to bigger); visible-repetition 10/12 (identical walk each time). |
| 5:05 O(n) | Notation-after-concept 9/12; new principle 2 (invent, derive, then name). Notation placed at ~29% of runtime; the FFT places omega at ~57% and JPEG formula at ~60%, so I put the first label early but the formal definition late. |
| 5:40 pairs | Special-case-first 9/12; FFT x^2 then x^3 ladder; design-it-yourself. |
| 7:20 quiz | Inline-quiz 8/12 (recursion 2:19) and commit-to-answer 5/12 (marching squares 12:22). |
| 8:35 3n+5 | Simulation-as-argument 5/12 (marching squares 1k, 10k, 20k samples). |
| 9:40 misconception | Honest-caveat; the report is weak on misconceptions in this channel (Sec. 6: partial at best), so this is a "partial" misconception, not a long planted trap. |
| 10:50 guessing game | Analogy 8/12 but short (principle 4 "partly"); bridge into act-it-out. |
| 11:15 to 12:50 binary search | Tiny to bigger plus repeating across examples; doubling ladder. |
| 14:15 cost felt | New principle 3 (cost in learner's units: collisions 1h40m vs 3 minutes, PNG 5^240). |
| 15:25 definition | JPEG formula as receipt (18:03); principle 2 and notation-after-concept. |
| 16:20 caveat | Honest-caveat 11/12. |
| 16:55 recap + callback | Recap 11/12, callback-to-hook 9/12. |
| 17:30 teaser | Teaser-next 3/12, weak; I included it as a one-liner only. |

Report claims I could not turn into a concrete choice (too vague to generate from):
- "Reducible slows via idea rate": no number for how long a beat lasts or how many examples; I guessed.
- Principle 3 (interfaces via habit) and principle 8: no generative rule; ignored.
- "Humor (light, dry)" 10/12: no pattern for where; I placed no explicit jokes in the script, which may be a miss.
- Which arc variant (core, ritual, guided tour) fits a definition-heavy topic: the report doesn't say. I chose the core arc.
- Whether a code stage appears: the report shows code in about half the videos but gives no trigger. I omitted code here.

## 4. Explicit predictions

- First question to the viewer: 0:00 to 0:15 (the hook question "what is different between the two programs"); first real inline quiz at about 7:20.
- First notation/formula: O(n) at about 5:05. Formal definition f(n) <= c g(n) at about 15:25.
- Misconception: yes, partial: "lower Big O always means faster", or "Big O gives time in seconds". Broken with a crossover example.
- Brute-force-first: yes. Linear search by hand, and timing with a stopwatch as the naive measuring method.
- Examples: 3 main (linear search, pair comparison, binary search), possibly a fourth (n log n sorting or exponential). Each is run through an n=4, 8, 16 style ladder; they grow in complexity of growth rate: n, n^2, log n.
- Hook type: paradox/question about two programs with the same task but very different scaling.
- Ending: recap plus callback to the hook, then a teaser to the next video (recursion or sorting analysis).
- 5 most confident moves: (1) special-case-first, (2) notation-after-concept, (3) roadmap, (4) honest-caveat, (5) recap with callback-to-hook. Close sixth: failure-shown (naive timing or exponential blow-up).
