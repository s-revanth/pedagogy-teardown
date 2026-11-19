# How Do Computers Remember? (Sebastian Lague)

## Arc
Recap and question (0:01), a real light that stays on (0:35), an SR latch built from AND/OR/NOT with a feedback wire (1:07), a second NOR-only latch (2:48), DATA+STORE data latch (4:37), the power-on oscillation (5:46), a physical NAND breadboard (7:13), a 4-bit register (9:25), the runaway ALU loop (10:03), the clock (11:47), two-latch flip flop (13:11), failed AND-on-clock gating (14:19), multiplexer register (15:26), replay of the runaway setup now fixed (16:40), RAM teaser (18:35).

## Strongest moves
1. Hook as paradox in hardware (0:35): touch a wire, light stays on after removal. The question is felt before any gate is named.
2. Failure motivates the tool (11:13-11:47). The ALU result races round and overwrites 3+1, 4+1, 5+1. The clock is introduced only after the viewer sees that no human timing can fix it. Same pattern at 14:51 (AND on the clock glitches) leading to the mux at 15:26.
3. Name after behaviour (2:29, 5:46, 14:02). "SR latch", "data latch", "edge triggered flip flop" are attached after the circuit has already been run.
4. Honest-caveat plus physical grounding (4:19, 5:46, 7:13). He says the NOR latch takes a while to wrap your head around, admits he was confused by the oscillation, then rebuilds with real NAND chips to be convinced.
5. Callback (16:40-18:12): the broken runaway setup is rebuilt and now stores 8 once. Closure comes from the same experiment.

## Unusual
No analogy carries the weight. The explanation is almost purely trace-the-signal narration, repeated for set, reset, store, and each tweak. The presenter positions himself as a co-learner ("I think I roughly understand it now"). Speech rate does not slow at hard bits; instead he adds retests (13:28-14:02).

## Principle verdicts
Confirmed: 1, 2, 5, 6, 7, 9, 10, 11, 12. Partly: 3 (habit of toggle-and-observe is real but not taught), 4 (only loose metaphors like "locking" at 3:44), 8 (idea rate, not speech rate, slows), 13. No contradictions.

## Velocity implications
- Scene builder should treat a "broken first draft" scene as a first-class object: build it, run it, show it fail, then patch.
- Orchestrator: block new vocabulary until a behaviour has been shown that needs it.
- Ghost hands: reuse one canonical input choreography (set, release, reset, release) across variants so the learner compares outputs.
- Voice: allow honest "this is confusing, give it a moment" at genuinely hard steps.
- Evals: for each introduced component, check a preceding demonstrated failure exists and that the term appears after the demo.
- Learner model: the real-hardware verification beat is an optional trust-builder for skeptical learners.
