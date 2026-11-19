# Predicted script: Reducible, "PageRank: A Trillion Dollar Algorithm"

- Channel: Reducible
- Video id: JGQe4kiPnrU
- Target duration: 1526 s (25:26)
- Recall risk: **vague**. I know in general that Reducible has a PageRank video and that the topic involves the web as a graph, a random surfer, linear algebra and iteration. I do not recall its order, examples, or wording. I ignored any such memory and built from the report, round-1 findings and general subject knowledge.

## 1. Predicted beat sheet

| Time | H/B/N/I | Move tags | Narrator says / does | On screen |
|---|---|---|---|---|
| 0:00 | H | hook-paradox, hook-question | A search engine existed that matched words, and results were junk. Then one idea made a company worth a trillion dollars. What was the idea? | Search results for a query, spam page first; later the company logo-free "rank" number |
| 0:50 | H | minimal-definition-then-refine | The problem: billions of pages, one query, which page goes first? Define "importance" loosely | Query box, a pile of page icons |
| 1:35 | N | roadmap | Plan: model the web, find a naive ranking, watch it break, repair it, then compute it fast. Two slots left empty: "what does importance mean?" and "can we compute it at web scale?" | Four-step plan with two slots greyed |
| 2:20 | H | toy-world, minimal-definition-then-refine | The web as circles (pages) and arrows (links): only a graph. Four pages A, B, C, D | Small directed graph, labelled |
| 3:20 | N | brute-force-first | Naive ranking: count incoming links, one link is one vote | Counters over nodes |
| 4:15 | N | failure-shown, honest-caveat | Failure: a spammer makes 1,000 junk pages that link to their target; and a link from a famous page should count more than one from nobody | Spam farm vs. a single big node |
| 5:30 | N | design-it-yourself | Key idea: a vote is worth as much as the importance of the voter; but that is circular | Arrows with weights unresolved |
| 6:30 | N | special-case-first | Split each page's importance equally among its outgoing links; set up equations for 3 pages by hand | Three-node graph with fractions on arrows |
| 8:20 | N | build-and-verify | Solve the 3-page system; check totals add up to 1 | Equations resolving, sum bar |
| 9:30 | B | analogy, analogy-breakpoint | Random surfer: a person clicks links at random forever; the fraction of time on a page is its rank. Breakpoint: no real person is this random | A dot walking a graph |
| 11:00 | N | simulation-as-argument | Simulate 100, 10,000, 1,000,000 steps; visit fractions converge to the hand-solved numbers | Bar chart stabilising |
| 12:10 | I | notation-after-concept | Write the web as a matrix M: column j is where page j sends its importance; vector r; r = M r | Matrix beside graph, columns highlighted |
| 14:00 | N | multiple-decompositions | Same rank three ways: equations, surfer, matrix; r is a fixed point / eigenvector with eigenvalue 1 | Three panels linked |
| 15:00 | N | learner-discovers, visible-repetition | Power iteration: start uniform, multiply by M again and again; the numbers settle. Repeat with a different starting vector | Bars updating each round, two starts |
| 16:50 | N | failure-shown, roadmap | Does it always work? Dead end (a page with no links) leaks importance to zero | Graph with sink; bars drain |
| 18:00 | N | failure-shown, special-case-first | Spider trap: a cycle that swallows all importance; also two disconnected parts | Closed loop absorbing bars |
| 19:00 | N | design-it-yourself, commit-to-answer | Pause: how would you patch a surfer stuck in a trap? | Stuck dot |
| 19:30 | I | notation-after-concept | Teleport with prob 1-d; damping d = 0.85; G = dM + (1-d)/n J | Formula with the two parts coloured |
| 21:10 | N | honest-caveat | 0.85 is a design choice; real search uses many other signals; PageRank was one ingredient | Caveat card |
| 21:50 | N | cost-in-learner-units, roadmap | Web with billions of pages: dense matrix is n^2 entries, impossible; M is sparse; each iteration costs the number of links; ~50 iterations enough | Memory meter, then sparse list |
| 23:10 | I | build-and-verify | Short code: python adjacency list, power iteration loop, check ranks sum to 1 | Code and printed ranks |
| 24:10 | N | generalize-to-other-domains | Other uses: ranking sports teams, scientific citations, proteins | Montage of graphs |
| 24:50 | N | recap, callback-to-hook | Recap: votes weighted by voters, fixed point, surfer, teleport; callback to the opening query and the trillion dollars | Opening page, now correct order |

## 2. Full narration script

[0:00] Imagine it is the late nineties, and you type a search into one of the popular search engines. It does what it was built to do: it finds pages that contain your words. The problem is that a page can contain your words a hundred times without having anything useful to say. People figured that out quickly, and the top of the results filled with junk.

Then a pair of graduate students had an idea that did not require reading a single page. It looked only at how pages link to each other. That idea became one of the most valuable pieces of software ever written, and today a company built around it is worth a trillion dollars. So what was the idea? And, if we had been in the room, could we have found it ourselves?

[0:50] Let us state the problem as cleanly as we can. There are billions of web pages. Someone types a query, and we have, say, thousands of pages that match. We need to decide which goes first. What we want is some number for every page, a measure of how important it is, independent of the query, so that when we have a pile of matches we can sort them. For now let me leave "important" fuzzy. We are going to sharpen it as we go.

[1:35] Here is the plan. First, we need a model of the web, something small enough to draw. Second, we will try the obvious ranking and see where it breaks. Third, we will repair it, and in doing so we will find the real idea. And fourth, we need to make it fast enough for billions of pages. I will leave two slots open as we go. One: what does "importance" actually mean? Two: can we compute it at the scale of the web? We will tick them off.

[2:20] Start with the model. A web page is a thing. A link is an arrow from one page to another. That is all we need. Circles for pages, arrows for links. Mathematicians call this a graph, but nothing in the next few minutes needs more than circles and arrows.

Here is a tiny web: four pages, which I will call A, B, C and D. A links to B and to C. B links to C. C links to A. And D links to C. Four circles, five arrows.

[3:20] Now the obvious ranking. A link is like a vote: someone chose to point at you, so you must be worth something. So count the incoming arrows. A has one. B has one. C has three. D has none. C wins. That actually seems plausible. C is the page everyone points at.

[4:15] But let us stress it. Suppose I want my own page to rank first, and I am not very scrupulous. I create a thousand new pages, each costing me nothing, and every one of them links to mine. Now I have a thousand votes, and I beat every honest page on the web. Counting links can be gamed by anyone.

And there is a second problem, even without cheating. Imagine one link coming from a major newspaper, and another from a page nobody has ever visited. In this ranking they count the same. Does that feel right to you? A recommendation from someone respected should carry more weight than a recommendation from someone nobody knows.

[5:30] That is a clue, and it is worth pausing on. If a vote is worth more when it comes from an important page, then the importance of a page depends on the importance of the pages that link to it. But those pages' importance depends on the pages that link to them. We have defined importance in terms of itself. That sounds like a circular definition, and it would be, except that it is also a system of equations. And we know what to do with systems of equations: solve them.

[6:30] Let us work it out by hand on a smaller example. Three pages: A links to B and C, B links to C, and C links to A. Rule: a page splits its importance equally among the pages it links to. A links to two pages, so it sends half of its importance to B and half to C. B links to one page, so it sends everything to C. C links to one page, A, so it sends everything to A.

Now write what each page receives. A receives everything C has. So A's importance equals C's. B receives half of A's. C receives half of A's plus all of B's.

Let us call the importances a, b and c. Then a equals c. b equals a over two. And c equals a over two plus b. Since there is nothing to anchor the scale, we also say they add up to one. Substitute b into the third equation: c equals a over two plus a over two, which is a. Good, that matches the first equation. So all we know is that c equals a, and b is half of that. With a plus b plus c equal to one, we get two a plus a over two equals one, so a is two fifths. Therefore a is 0.4, c is 0.4, and b is 0.2.

[8:20] Let us verify. Does A really get everything C has? A is 0.4, C is 0.4. Yes. Does C receive half of A plus all of B? Half of 0.4 is 0.2, plus 0.2, which is 0.4. Yes. Everything adds to one. So on this tiny web, the two pages that are linked by the most important pages share the top spot, and B trails.

Now, solving equations by hand for a web with billions of pages is not going to work. We need a way that scales. Let us look at the same answer from a very different angle.

[9:30] Picture someone sitting at a random page and clicking a link at random. Then another random link from where they land, and so on, forever. This is often called the random surfer. The claim is: the fraction of time that surfer spends on each page is its importance. A page is important if a surfer, wandering with no purpose, is likely to end up there. And that makes intuitive sense: pages with many good routes into them are visited more.

Now I should be honest. No real person browses this way. People type addresses, use bookmarks, and give up. The surfer is not a model of behavior. It is just a convenient way to turn the equations into a process we can simulate.

Before we move on, notice how reasonable the rule is that a page splits its importance equally. We could have invented other rules, such as favoring the first link on a page, or letting a page send all of its importance to a single favorite. But equal splitting has a property that matters: nothing is created and nothing is destroyed. Whatever importance a page has, exactly that much leaves it, and every unit that leaves lands somewhere. That conservation is what will let the numbers add to one forever, and it is why a page with a thousand outgoing links passes only a thousandth of its importance down each. A link from a page that links to everything is worth very little, which is exactly the opposite of how the junk-page trick worked.

[11:00] So let us simulate it on our three pages. Start at A, and move one hundred times. Count visits. A bit rough: maybe forty-some percent on A, thirty on C, the rest on B. Now ten thousand steps. The bars are closer to forty, forty, and twenty. A million steps: indistinguishable from what we solved on paper. The surfer and the equations agree.

That is a satisfying moment, because two completely different methods give one answer. It tells us the number we were after exists and is stable.

[12:10] Now let us put the whole thing in a more compact form, since the equations are going to get long. Lay out the importances as a column of numbers, a vector, which I will call r. And build a table, a matrix, which I will call M. Column j describes where page j sends its importance. For page A, which sends half to B and half to C, the column has a half in the B row and a half in the C row, and a zero in its own row. Do the same for B and C. Now, the statement "each page receives what the pages pointing at it send" is exactly the product of M with r. And our rule, that importance is consistent with itself, reads: M times r equals r.

[14:00] Let us look at that for a moment, because the same answer is now living in three forms. In the equations, it is what we solved. In the surfer, it is what the long walk converges to. In the matrix, it is a vector that M does not change, except to give it back unchanged. In linear algebra, that is an eigenvector of M with eigenvalue one. Do not worry if that word is new; all it says is that r is a fixed point of the update.

[15:00] And a fixed point suggests a way to find it. Start with any guess, say that every page has the same importance. Apply M: let each page send out its importance along its links. We get new numbers. Apply M again. And again. Watch what happens. On our three pages, the bars wobble, and a few rounds later they stop moving at 0.4, 0.2, 0.4. Now let me start somewhere very different: all the importance on page B. Run the same steps. A few rounds of wobbling, and it ends in the same place. This is called power iteration, and the point is that it is just multiplication, done again and again. No equation solving.

Let me slow down and do the first rounds in full, because it is worth seeing the numbers. Start with a third each: A, B and C all at 0.33. Round one. A receives everything C has, so A becomes 0.33. B receives half of A, so B becomes about 0.17. C receives half of A plus all of B, so C becomes 0.17 plus 0.33, which is 0.5. Total: one. Round two. A takes C's 0.5. B takes half of A's 0.33, about 0.17. C takes half of A, 0.17, plus B's 0.17, which is 0.33. So now A is 0.5, B is 0.17, C is 0.33. Round three: A takes 0.33, B takes 0.25, C takes 0.25 plus 0.17, which is 0.42. The numbers are swinging back and forth, each swing smaller than the last, tightening around 0.4, 0.2, 0.4. You can feel it homing in. By round ten or so, the third decimal has stopped moving.

And notice what we did not need. We never asked what the right answer was. We just kept applying the rule, and the answer showed up. That is the practical power of a fixed point.

[16:50] So have we solved it? Our second slot, computing it at scale, is still open, but first, we have to ask whether this always works. Let us poke at the model. Take our web and add a page E that receives links but has no outgoing links, a dead end. When the surfer lands there, there is nowhere to go. In the matrix, the column for E is all zeros, and every round, E swallows importance and sends none of it back. Run the iteration, and watch the bars drain. Everything slides toward zero. Importance is leaking out of the web.

[18:00] There is a second kind of failure. Suppose a group of pages links only among themselves, a closed loop, and pages elsewhere link into it. Once the surfer gets in, they can never leave. After enough steps, all the importance sits in that loop, and every other page gets zero. A page can do this on purpose, which is just another way to cheat. And if the web splits into pieces that cannot reach each other, the answer is not even unique.

[19:00] Pause here. If you were the surfer, stuck in a dead end or going around a trap, what would you do? Think about what a real person would do.

[19:30] They would give up and type a fresh address somewhere else. So let us build that in. At every step, with some probability, say fifteen percent, the surfer ignores the links and jumps to a page chosen uniformly at random from all pages. The other eighty-five percent of the time, they follow a link as before. That jump is called teleportation, and the eighty-five percent is called the damping factor, which we call d.

In the matrix language, the new update is d times M plus one minus d, over n, times a matrix of all ones, where n is the number of pages. The first part says to follow links most of the time. The second part says to spread a little importance evenly everywhere. For dead ends, you simply treat the column as uniform, so the surfer jumps anywhere. Now run the failures again. The dead end no longer drains the web. The loop no longer holds everything, because there is always a fifteen percent chance of leaving. And one can prove that, with teleportation, there is a single answer and power iteration always finds it, a result I will leave as a link rather than derive here.

[21:10] Let me add an honest caveat. The 0.85 is not a law of nature. It is a choice that works well in practice, and the original idea used it, but other values change the rankings and the speed. And PageRank is not what decides what you see in a modern search engine. It is one signal among a great many. It was the one that changed everything, but today it is one ingredient.

Let me also say why teleportation is not an arbitrary hack. It makes every page reachable from every other page in one step, with some small chance. That removes the two failure modes we saw at once: the surfer can always leave a trap, and the web can never fall into disconnected pieces. It also does something subtle for spam. A junk farm that links only to itself no longer hoards importance, because every step has a fifteen percent chance of leaving the farm for the rest of the web, and the farm gets back only the small share that teleportation hands every page.

[21:50] That leaves our last slot: speed. The real web has billions of pages. A table with a row and a column for every page has n squared entries, which is billions times billions. That will not fit in any memory. But think about M: a typical page links to a few dozen others, not billions. So almost every entry is zero. We never store the zeros. We store each page's list of outgoing links and nothing else. Each round of power iteration then costs about as many steps as there are links in total, not n squared. And the surprise is that we do not need many rounds. Fifty to a hundred is enough for the numbers to settle to a useful precision, since the damping factor makes the error shrink by a constant factor every round. That is what turns a theoretical idea into something you can run over the whole web.

[23:10] Let me show how short this is in code. We keep, for each page, a list of pages it links to. We start with a vector of ones divided by n. Then we loop: make a new vector of zeros, and for every page, give each page it links to a share equal to its rank divided by its number of links, times d. Then add one minus d over n to every entry. Repeat until the change is tiny. Let me run it on our small web and print the ranks. They add to one, and C is on top, as we computed. A quick check that the ranks sum to one is our sanity test that no importance leaked.

[24:10] Though we built this for the web, nothing in the idea is about web pages. Anything where things endorse other things can be ranked this way: scientific papers citing each other, sports teams that beat each other, even proteins that interact.

[24:50] Let us recap. We started with a ranking by counting links and saw it get cheated and misjudge the quality of votes. We fixed that by saying a vote is worth the importance of the voter, which looked circular but turned out to be a system of equations. We solved it three ways: by solving equations, by a random surfer, and by a matrix fixed point. Then we found the method that scales, power iteration. We patched dead ends and traps with teleportation. And we made it fast by never storing the zeros.

So, back to the search at the start. The page that dozens of respected pages point to now rises to the top, and the page with a thousand junk links does not. That, in a few lines of mathematics, is the idea that built a trillion-dollar company.

## 3. Rule trace

| Beat | Report claim / move that produced it |
|---|---|
| 0:00 hook | Hook-paradox 5/12 (JPEG gap) and hook-question 9/12; "you could have invented it" framing from round-1 move 13. |
| 0:50 definition | Minimal-definition-then-refine 12/12; "importance" left fuzzy on purpose, to be sharpened. |
| 1:35 roadmap with two empty slots | New principle 5 (plan with named empty slots: FFT magic box, GJK five open questions). Roadmap 12/12. |
| 2:20 circles and arrows | Graph theory 0:00 "circles and lines before vertex"; toy-world 9/12. |
| 3:20 count in-links | Brute-force-first 6/12 (FFT 2:05); principle 6. |
| 4:15 failure | New principle 1 (failure is the stepping stone; PNG gradient image defeats tools); failure-shown. |
| 5:30 circular definition | Principle 11 (dependency order, invent stepping stones); learner-discovers. |
| 6:30 to 8:20 three-page by hand | Special-case-first 9/12, tiny to bigger (principle 10), build-and-verify 11/12 (recursion 9:20 "is that coincidence"). |
| 9:30 surfer | Analogy 8/12 with analogy-breakpoint 3/12 (Hanoi dominoes that fail); also honest caveat. |
| 11:00 simulation | Simulation-as-argument 5/12 (marching squares 1k, 10k, 20k). |
| 12:10 matrix | Notation-after-concept 9/12, placed after a hand-solved case and a simulation; FFT puts omega at about 57% of runtime, so this is about 48%. |
| 14:00 three forms | Multiple-decompositions 6/12 (FFT evaluation as matrix product). |
| 15:00 power iteration twice | Visible-repetition 10/12 and principle 9 (repeat across examples); two start vectors. |
| 16:50 to 19:00 failures | Failure is the stepping stone; each patch is the repair of a failure the learner just watched. |
| 19:00 pause | Inline-quiz 8/12, commit-to-answer 5/12; regulation line analog (new principle 6). |
| 19:30 teleport | Invent, derive, then name (new principle 2): the damping factor is named after the behavior. |
| 21:10 caveat | Honest-caveat 11/12. |
| 21:50 cost | New principle 3 (cost felt in learner's units; collisions memory/time). Also "say why this tool" (principle 13: adjacency list for sparse graphs, graph theory 12:00). |
| 23:10 code | Code appears in about half the videos (FFT 20:46, Hanoi 14:07), after the concept, as a receipt. |
| 24:10 generalise | Generalize-to-other-domains 8/12 (marching squares electric potential). |
| 24:50 recap + callback | Recap 11/12, callback-to-hook 9/12. |

Report claims I could not turn into a concrete choice:
- Humor 10/12 (light, dry): no pattern for placement; I included no scripted jokes beyond the dry tone.
- Regulation line (principle 6 new): the report gives no exact wording rule; I used a single pause prompt at 19:00 only.
- Pace: "slow via longer beats, more examples" gives no numbers; I guessed beat length 30 to 90 s.
- Which of the core, ritual or tour arcs: the report does not predict; I used the core arc.
- How deep proofs go: report says "often skipped or linked"; I assumed convergence proof is linked, which is a guess.
- Whether a real-data demo (not toy) appears: no rule.

## 4. Explicit predictions

- First question to the viewer: 0:00 to 0:50 (rhetorical hook question about what the idea was); first genuine pause/commit prompt at about 19:00, with a smaller "does that feel right?" at about 4:30.
- First notation/formula: the three-equation system at about 6:30, the matrix M and r = Mr at about 12:10, and the damping formula at about 19:30.
- Misconception: yes, partial. The belief that "more incoming links means more important" (or that the surfer models human behavior), broken at about 4:15.
- Brute-force-first: yes. Count incoming links; and, by extension, solving the system directly.
- Examples: 3 main toy webs (a 4-page graph, a 3-page graph solved by hand, one with a dead end and a trap), growing by one failure each time; then the real web by sparse storage.
- Hook type: paradox/question around an idea worth a trillion dollars.
- Ending: recap plus callback to the hook; a pointer to the code and a link to the proof rather than a teaser.
- 5 most confident moves: (1) failure-shown with each repair, (2) roadmap with open slots, (3) special-case-first on a small graph, (4) notation-after-concept, (5) honest-caveat. Close sixth: simulation-as-argument for the random surfer.
