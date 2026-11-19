# Solving Wordle using information theory (3Blue1Brown)

Note: the stored transcript is Arabic; this analysis is from reading it. Timestamps are reliable, wording approximate.

**Arc.** Game hook and demo (0:00-2:27), honest naive attempts (2:48-3:39), game setup and data choices (3:39-5:00), concrete pattern probabilities (5:16-7:14), bits and log (8:13-10:28), expected information and entropy (10:48-13:54), the bot in action with margin annotations (13:54-17:25), simulation and failure (17:25), word-frequency prior (18:22-25:07), score metric fitted to data (25:07-28:00), limits and lookahead tease (28:15).

**Strongest moves**
1. *Quantity before name (8:13-9:03).* One bit is halving, two is a quarter, then the formula 2^bits = 1/p. The learner can predict the formula from the table.
2. *Why logs, in plain terms (9:37-10:28).* Information adds where probabilities multiply, shown with an example. This justifies a tool rather than just using it.
3. *Entropy joke as de-mystifier (11:44-12:41).* The von Neumann anecdote followed by "just think of it as expected information."
4. *Quiz with a twist (20:28-21:57).* Entropy of 4 equal words is 2 bits; add 12 very unlikely words and it is only 2.11. It shows why probabilities, not counts, matter, before the prior is applied everywhere.
5. *Data-validated metric (25:07-27:39).* Rather than assert that more information means fewer guesses, he plots past games and fits it. Bot average improves to about 3.6.

**Unusual.** Fully build-and-verify structure: every concept goes straight into a working bot, and the bot's failures drive the next concept. Presenter intentionally ignores the leaked answer list (4:26) and sometimes overrides the bot (16:12). It ends with limits and no "perfect" claim.

**Principle verdicts.** 1 confirmed. 2 confirmed. 3 confirmed (colored patterns and bar chart reused). 4 confirmed. 5 confirmed (plays the game). 6 confirmed. 7 confirmed (puzzles). 8 partly, no speech data; slowdown via example counts. 9 confirmed. 10 confirmed. 11 confirmed. 12 confirmed. 13 confirmed.

**Velocity implications.** Keep one persistent chart interface across the lesson. Derive formulas from tabulated cases. Ask for predictions before each reveal. Make "test against data" a recurring beat. State exclusions and why.
