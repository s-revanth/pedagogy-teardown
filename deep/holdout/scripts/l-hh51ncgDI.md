# Predicted script: Algorithms Explained, minimax and alpha-beta pruning

- Channel: SebastianLague
- Title: Algorithms Explained – minimax and alpha-beta pruning
- Target duration: 661 s (11:01)
- Recall risk: vague. I know this is a short entry in a series, and I suspect it relates to his chess work, but I do not recall its structure, example game, numbers or wording. Built from the channel report plus general subject knowledge of minimax and alpha-beta. Details such as the specific game chosen are guesses.

## 1. Predicted beat sheet

| Time | H/B/N/I | Move tags | Narrator says / does | On screen |
|---|---|---|---|---|
| 0:00 | H | roadmap, toy-world | In this episode: how a computer picks a move in a two-player game, using minimax, and then how to make it much faster with alpha-beta pruning. Starts with a tiny game: tic-tac-toe. | A tic-tac-toe board, X to move |
| 0:30 | H | minimal-definition-then-refine | A game position is a state; a move leads to a new state. Two players alternate; one wants a high score and the other a low one. Smallest framing only. | Board with a few arrows to the resulting boards |
| 1:00 | H | brute-force-first, build-and-verify | Dumbest bot: choose a random legal move, or the first that looks good. Plays it against a simple trap position. | Bot plays a losing move; a human-made trap |
| 1:35 | H | failure-shown | It does not think about the reply. Needs to look ahead: after my move, what could the opponent do, and what then? | Tree of boards beginning to fan out one level |
| 2:10 | N | toy-world, act-it-out | Draws the game tree by hand. Nodes are positions, edges are moves. Switches to a made-up small tree with numbers at the leaves (scores) so we can see the idea without the board. | Abstract tree: root, two or three levels, numbers on leaves |
| 3:00 | N | special-case-first, act-it-out | Walk one branch: leaves are scores from the maximiser's view. The opponent will choose the smallest value, so a parent of minimiser nodes takes the minimum. Then the maximiser takes the largest of those. | Values bubbling up one node at a time, colour-coded for max and min |
| 3:55 | N | build-and-verify, visible-repetition | Same tree, a second subtree, same procedure; arrives at the root value and the best move. Check against the earlier trap position: bot now avoids it. | Root highlighted; bot replays the trap and survives |
| 4:35 | I | notation-after-concept | Only now shows pseudocode: recursion, depth, maximising flag, loop over moves. Each line matched to something already seen. | Short pseudocode listing, lines highlighted as the tree animates |
| 5:20 | N | failure-shown, honest-caveat | Cost: the tree explodes with every extra move; full tic-tac-toe search visits many thousands of positions, and chess is out of the question. Notes depth limit and an evaluation function as the practical fix, and that picking the evaluation is hard (skipped). | Counter of positions visited climbing; "depth limit" cut line |
| 6:10 | N | design-it-yourself, minimal-definition-then-refine | Is it necessary to visit every leaf? Back to the small tree, he pauses at a node and asks if the remaining branch can matter. | Tree frozen mid-search, question mark on an unvisited subtree |
| 6:50 | N | act-it-out, special-case-first | Worked example: maximiser already has a guarantee of 5. In the next subtree the minimiser finds a 3 straight away, so it can force at most 3 there. Maximiser would never pick it, so its other children can be skipped. | The branch greys out; 5 and 3 labelled beside the nodes |
| 7:40 | I | notation-after-concept | Names the two bounds, alpha (best the maximiser can guarantee so far) and beta (best the minimiser can guarantee), and shows they pass down the tree. | alpha and beta labels appear on nodes and update; code gains two parameters |
| 8:30 | N | visible-repetition, build-and-verify | Rerun the full tree with pruning. Count leaves visited versus plain minimax; same root value. | Side-by-side: all leaves versus subset; counters |
| 9:15 | N | failure-shown, design-it-yourself | Pruning depends on order: if the best move is searched last, almost nothing is pruned. Reorder so likely-good moves come first and watch pruning grow. | Same tree with children reordered; counter drops |
| 9:55 | N | simulation-as-argument, honest-caveat | Bot with minimax versus bot with alpha-beta, same position, same depth; timings. Admits good ordering is its own problem. | Timing table: depth, positions, seconds |
| 10:30 | H | callback-to-hook, teaser-next | Ties back to the opening trap. Mentions it is how the chess engine searches and a hint of what could come next. Short sign-off. | Return to the board; fade out |

## 2. Full narration script

In this video, I would like to look at how a computer can choose a good move in a two player game. We will look at an algorithm called minimax, and then at a clever trick called alpha-beta pruning, which makes it much faster. I will start with a very simple game, tic-tac-toe.

Here is a board, and it is X's turn. Any arrangement of the board is what I will call a position. A move takes us from one position to another. And the two players take turns. One of them, let's say X, wants the game to end well for X. The other one wants the opposite, and we can capture that with a single score. Higher scores are better for X, and lower scores are better for O.

Now, what is the simplest way for a bot to choose a move? Well, it could pick a random one. Or it could pick the first move that seems reasonable. Let me set up a position where there is a trap, and see how this goes. The bot makes a move that looks fine, and then the opponent replies, and, well, we lose.

The problem is that the bot has not thought about the reply at all. To avoid traps like this it has to look ahead. If I play this move, what could my opponent do, and what could I do after that? And so on. This is going to branch out very quickly, so let me draw it out.

Each position is a node, and each move is a line down to a new node. This is called a game tree. The real tree for tic-tac-toe is a little big for the screen, so let me switch to a made-up one, where I have put some scores at the bottom, the leaves. These are the outcomes, from X's point of view.

Let me walk through how we would decide on a move. Here are three leaves under this node, and it is the opponent's turn, so they will pick the worst one for us, the smallest number. So this node gets the value of its smallest child. One level up, it is our turn, and we pick the best, the largest number among the values below. And that is all minimax is. At each level, the maximiser takes the biggest and the minimiser takes the smallest, and the values bubble up to the top.

Let me do it again with the other side of the tree. Same idea. Smallest of these, smallest of these, then the larger of the two. And the number that arrives at the top tells us what we can guarantee against a perfect opponent, and which move gets us there. If I put that back into the bot and replay the trap position, it now sees the reply coming and avoids it.

Here is the pseudocode, now that we have seen all the pieces. We have a function that takes a position and a depth. If we have reached the depth limit, or the game is over, we return the score of the position. Otherwise, we loop through all of the moves. If it is the maximiser's turn, we keep the largest value, and if it is the minimiser's, we keep the smallest. Each recursive call flips whose turn it is. That is really everything.

The big problem is the cost. Every extra move multiplies the number of positions, so even in tic-tac-toe this visits a few hundred thousand positions, and chess is far, far beyond that. In practice, we only search to a certain depth, and then guess the score of the position using an evaluation function. I am not going to get into how to write a good one here, since that is a whole topic of its own.

But what I want to ask is: do we really need to look at everything? Let me go back to the small tree and stop partway through. Here, we have already found that the first branch is worth five to us. So we know that we can get at least five. Now we move on to the second branch, which is the opponent's choice, and the very first thing we see is a three. So the opponent can force this branch to be worth at most three to us. We would never choose it over the five. So it does not matter what the rest of the children are. They could be anything, nine, a hundred, and it would not change the answer, because the opponent would simply pick the three. We can skip them.

That is what alpha-beta pruning does. We keep track of two numbers. Alpha is the best value that the maximiser can already guarantee, and beta is the best the minimiser can already guarantee. These get passed down as we go deeper into the tree. And whenever alpha becomes greater than or equal to beta, we know the rest of this branch cannot matter, and we stop.

Let me run the whole tree with this. I will count how many leaves are visited. With plain minimax it is every one of them, and with alpha-beta, it is only some. And the answer at the top is exactly the same. That is important: it is not an approximation, it just skips work that could not change the result.

Now, there is a catch. How much we prune depends on the order we look at the moves. If we happen to look at the best move last, we hardly prune anything. If we look at the best move first, we prune a lot. So here I have reordered the same tree, and you can see the number of visited leaves drop. In a real game, we do not know the best move ahead of time, but we can make a decent guess, for example by trying captures first in chess.

Let me show that with the numbers. Here is the same tree with the children of each node in a different order. In the first ordering, the best branch for the maximiser comes first, and as soon as we get to the second branch, we find a bad value for us and cut it off. In the second ordering the good branch comes last, so by the time we get to it, we have already searched everything else, and the bounds were too loose to cut anything. Same tree, same answer, very different amounts of work. I find that a little surprising, to be honest, that just shuffling the order of the moves can matter so much.

It also helps to think about what the pruning is doing as the tree gets deeper. A cut near the top of the tree throws away an entire subtree, which might be thousands of positions, while a cut near the bottom saves only a few. So the bounds passing down from the top matter a lot, and getting the best moves examined early is where the real savings come from. I have been using small trees so that you can follow along, but the same thing happens with real games, just on a much bigger scale.

Finally, I have put the two bots against one another from the same position at the same depth. The one with alpha-beta searches far fewer positions and gets the same answer in a fraction of the time, which means that for the same amount of time it can search deeper. I will say that move ordering is a topic of its own, and I am only scratching the surface.

And going back to the position from the start, our bot no longer falls for the trap. Alpha-beta pruning is one of the ideas behind how chess engines can look so many moves ahead, and I would like to build on this in future. Thanks for watching.

## 3. Rule trace

| Beat | Report claim / arc step / move |
|---|---|
| 0:00 roadmap and tiny game | Arc step 1: roadmap and tiny toy world in the first minute (chess board and FEN, A* empty grid). Roadmap 9/12. |
| 0:30 minimal framing | Minimal-definition-then-refine 8/12 (computers 0:55). |
| 1:00 dumb bot | Arc step 2 and principle 6: dumb version first; brute-force-first 7/12 (chess "play every move"). |
| 1:35 fails to anticipate | Arc step 3 fails visibly; failure-shown 11/12; theory 1 (the need for lookahead is shown before it is named). |
| 2:10 abstract tree | Principle 11, stepping stones invented freely (fluids 8:42 meaningless function): a made-up tree with numeric leaves instead of real game boards. |
| 3:00 min then max | Special-case-first 7/12 (A* empty grid) and act-it-out 9/12; he runs the algorithm by hand as the sim. |
| 3:55 second subtree and trap replay | Theory 3 fixed test choreography; arc step 5 verify immediately with the same test; build-and-verify 11/12. |
| 4:35 pseudocode | Arc step 4 and A* pattern ("pseudocode only after every line was seen"); notation-after-concept 9/12; theory 2. |
| 5:20 cost explosion | Failure-shown; honest-caveat 10/12 for skipping the evaluation function (report section 6: "skips and omits"). Numbers shown (chess perft/timing pattern). |
| 6:10 can we skip | Design-it-yourself 10/12; theory 1 (pruning named only after the waste has been seen). Echoes chess "pruning" arc. |
| 6:50 worked prune | Act-it-out; special-case-first with concrete numbers (5 and 3). |
| 7:40 alpha and beta | Theory 2: label for something already seen; principle 2 every symbol costs effort, introduced one at a time (G/H/F in A*). |
| 8:30 rerun with pruning | Visible-repetition 11/12; before/after count (chess 15:45 timed run); verification that the root value matches. |
| 9:15 move ordering | Arc step 6, next failure triggers next concept; failure-shown; chess video's ordering/search improvements. |
| 9:55 bots head to head | Simulation-as-argument 10/12; before/after number. Honest-caveat on ordering. |
| 10:30 close | Arc step 7: honest close, callback to the opening trap, teaser (callback-to-hook 8/12, teaser-next 7/12). No lesson recap. |

Report claims I could NOT turn into concrete choices:
- The report gives no data on the "Algorithms Explained" format specifically (only A* E01, which is the closest; its three reruns with scaffolding removed was my only template). Whether this short episode uses a real game or a pure tree is therefore a guess.
- Humor (9/12): no specific style or frequency to place; I included none, which may be wrong.
- Principle 8 pacing, principle 3 habit, and principle 13: too vague to generate beat lengths or wording.
- Analogies (7/12): only "garden shears" for pruning is quoted as an example, and since that is a real line from the chess video, I deliberately did not reuse it.
- No guidance on how a short episode compresses the six-to-ten-cycle failure/fix loop; I picked three cycles (no lookahead, cost, ordering) by guess.

## 4. Explicit predictions

- First question to the viewer: none. The first real question is self-directed ("do we need to look at everything?") at about 6:10.
- First notation/formula time: pseudocode at about 4:35 (about 42% of runtime), after one full min/max worked pass. alpha and beta named at about 7:40. No algebraic formula.
- Misconception: no. If any, it would be his own wrong first bot, not a planted viewer belief. A weak "partial" is possible around the idea that pruning might change the answer; I predict he states it does not.
- Brute-force-first: yes. Random or one-move bot at about 1:00, then full unpruned minimax at about 5:20 before pruning.
- Examples: about 3 to 4. A tic-tac-toe trap board, a small abstract tree (number leaves), the same tree with pruning, the same tree reordered; possibly a final head-to-head with a bigger game. Growth is tiny to bigger on the same tree, with only the rule changing.
- Hook type: project/roadmap statement ("how to pick a move, then make it fast"). No question or paradox.
- Ending type: short honest close with a callback to the opening trap or chess and a loose teaser. No lesson recap.
- Five moves I am most confident will appear:
  1. toy-world (a tiny game and a tiny abstract tree up front)
  2. act-it-out (hand-walking the tree, values bubbling up, branches greying out)
  3. notation-after-concept (pseudocode and alpha/beta only after the process was shown)
  4. visible-repetition with build-and-verify (the same tree rerun with pruning, leaf counts compared, same root answer)
  5. failure-shown (naive bot falls for a trap; tree explosion; bad move ordering kills pruning)
