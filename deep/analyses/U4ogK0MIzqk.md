# Coding Adventure: Chess (Sebastian Lague)

## Arc
Draw board (0:01), piece numbers and array (0:36), FEN (1:44), drag/drop (2:34), sliding-piece moves (3:10), pseudo-legal then legal by brute force (6:23), random and self-play opponents, why computers crunch (7:18), speedups and perft testing against known numbers (8:51), Stockfish as bug oracle (10:05), evaluation (11:58), negamax search with a small tree (12:55), alpha-beta and move ordering (14:29), quiescence (16:17), endgame bonuses (17:38), transposition and zobrist hashing (20:07), piece-square tables and opening book (22:56), iterative deepening (26:11), named weaknesses (28:15).

## Strongest moves
1. Dumb version first, stated aloud (6:23, 12:55): legality by playing every move and checking for king capture, plain search before pruning. The viewer then watches the fix beat the baseline.
2. Measure each fix (15:45-16:16): same position takes 1 s and 3.5M evaluations, then 0.25 s and 0.5M with pruning, then 25 ms and about 5000 with move ordering. The explanation of why comes after the numbers.
3. Fail on a specific position then patch (17:38 king and two rooks, 20:07 pawn endgame, 22:56 opening shuffling). The next concept is whichever flaw is visible.
4. Oracle debugging (10:27): Stockfish's per-move breakdown localises bugs in castling, pins and en passant. Rare in explainers.
5. Stated horror (26:45-27:39): says iterative deepening seemed wasteful, then reveals the payoff via move ordering, and admits the explanation may not have landed.

## Unusual
Heavy on code and test positions, light on analogy (garden shears at 14:29 is the main one). Notation is held back until FEN at 1:44 and taught by walking a tiny string. The video stays honest about shortcuts ("spare you the tedium", "live in fear" of hash collisions at 21:21).

## Principle verdicts
Confirmed: 1, 2, 5, 6, 7, 9, 10, 11, 12. Partly: 3, 4, 8 (speech rate not tested; idea rate slows via 1-2 minute tree walkthrough at 13:30 and skipped tedium), 13. No direct contradiction.

## Velocity implications
- Keep a per-concept bank of failing cases; the orchestrator picks the next concept from the failure on screen.
- Always show a before/after metric for an optimisation before explaining mechanism.
- Voice: say "I find this counterintuitive" before reversals; check comprehension ("not sure that made sense").
- Ghost hands: let the learner play the weak engine and lose before introducing the fix.
- Delay notation until the object exists; teach it by decoding one short example.
