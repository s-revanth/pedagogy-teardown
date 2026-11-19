# Exploring How Computers Work (Sebastian Lague, QZwneRb-zqA)

## Arc
Wonder hook (0:03) -> physical switches and lamp (0:38) -> AND/NOT named after seeing them (1:12) -> transistor as an electric switch (2:03) -> simulator with two blocks (2:56) -> build NAND, OR (3:14-4:43) -> binary place value (5:01) -> add by hand (6:17) -> half adder, full adder, 4-bit adder (7:16-11:45) -> negatives (12:02) -> subtraction and ALU (14:16-17:28) -> teaser for memory.

## Strongest moves
1. **Truth-table as detective tool (7:56-8:29).** For the half adder he writes the wanted table and compares each column to chips he already owns. Carry equals AND exactly. Sum equals OR except in one row, so he patches with a NAND. The learner watches an invention being made from parts, not a formula delivered.
2. **Brute force first, then mechanise (6:17).** He adds 35+7 by hand, naming sum bit and carry bit only when the worked example needs them. The circuit then has an obvious job to copy.
3. **Presenter-was-wrong plus derive by solving (12:02-13:39).** He admits he assumed the top bit was a sign flag, shows 7 + (-7) fails, then asks what to add to 7 to get zero and fills in bits right to left. The reveal that the top bit is the -8 place lands because the learner has just computed it.
4. **Package-then-reuse (4:06, 4:43, 10:39, 17:47).** Each solved circuit becomes a named chip. This is both the dependency order and the interface the learner gets used to.
5. **Exhaustive verification loops (10:20, 16:48).** Every build is followed by testing all classes of input (none, one, two, three on) and later subtraction cases including negative minus negative.

## Unusual
Very little hand-holding about "why", but a lot of build-and-verify. The opening wonder is never called back at the end. Speech is a calm stream; slowing happens in idea density (long adder wiring, negatives) not obvious rate change. The transcript cannot confirm that.

## Principle verdicts
Confirmed: 1, 2, 4, 5, 6, 7, 9, 10, 11. Partly: 3 (reuse shown, habit not named), 8 (no speech-rate evidence), 12 (only Ben Eater and Nand2Tetris), 13 (plain, expert, no explicit simple-for-12-year-old pass).

## Velocity implications
- Scene builder needs a "seal as chip" action so later scenes use bigger blocks.
- Orchestrator rule: behaviour and table first, name second.
- Auto-run exhaustive sweeps after each build step and display them.
- Learner model should store which chips the learner built and let scripts reference them ("your XOR").
- Let the tutor voice hold a wrong prior belief and have the simulation refute it, as at 12:22.
