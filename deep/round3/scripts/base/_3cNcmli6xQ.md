# SebastianLague / _3cNcmli6xQ

- Channel: SebastianLague
- ID: _3cNcmli6xQ
- Title: Experimenting with Buses and Three-State Logic
- Duration: 1122 s (18:42)
- Condition: base
- recall: none

## Content skeleton

- Question: how do many devices share one wire without the wire being a mess?
- Starts from a two-switch, one-wire toy circuit with an LED at the end.
- Ordinary logic gives 0 and 1 only; a driverless wire is undefined; introduces a third, high-impedance state.
- A tri-state buffer gated by an enable line lets one device drive the wire and the rest let go.
- Failure case: two drivers on at once, opposite values, a short; shown with the simulator.
- Bus of several registers, one talking at a time, with a control scheme to pick which one.
- Brute-force multiplexer first, then the invariant "at most one driver active" as the design rule.
- Clocked version exposes race conditions; fix by phasing the read and write; ends with real-bus history and the next experiment.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Wires lighting up across a board; question of how many devices can share one wire. |
| 0:50 | toy-world | Two switches, one wire, one LED in the simulator; flipping switches changes the light. |
| 2:10 | definition | Name the states 0 and 1; a wire with no driver is in a third state, high-impedance. |
| 3:20 | analogy | A shared room with one microphone, where people take turns or stay silent. |
| 4:10 | demo-sim | Build a tri-state buffer with an enable input; toggle it and watch the wire follow or float. |
| 5:40 | wall | Two buffers enabled at once with opposite values; the simulator flags a short. |
| 7:10 | misconception-defuse | A floating wire does not keep its last value in the sim; it reads as nothing. |
| 8:00 | demo-sim | Four registers on one bus; enable lines chosen by a small control block. |
| 9:40 | brute-force | Wire it all through a large multiplexer first; count the gates and the wiring. |
| 10:50 | derivation | Rule: at most one enable high at a time. Everything follows from that invariant. |
| 12:10 | wall | Clocked version: two registers read and write on the same edge and the values race. |
| 13:40 | generalize | The same bus idea in old machines and memory chips; what the rule buys in practice. |
| 15:20 | recap | Three states, one driver at a time, and why the clock phase matters. |
| 16:50 | coda | Callback to the lit wire from the opening, then a teaser for the next experiment. |

## Narration

<<<NARRATION
Let's start with the picture from the beginning. A board full of wires, and every so often one of them lights up because something on the far side has decided to drive it. The question I want to answer in this video is simple to say and quite annoying to do. How do you get many different devices to share one wire, without them stepping on each other?

I'm going to do this as an experiment, which means I'm not going to pretend I know the answer before I try it. Some of what follows worked the first time, and a lot of it did not. I'll show you both, because the failures are the most useful part.

We start small. Here is a toy circuit. Two switches, one wire, and an LED at the end. The LED is on when the wire is high. If I flip one switch, the wire goes high. If I flip the other switch, it goes low. That is all we have, and it already contains a problem. If both switches are open, what is the wire doing? In the simulator it sits there with nothing pushing it either way.

In ordinary digital logic we are used to two values. Zero and one. High and low. But a wire with no driver connected is neither of those in any reliable sense. It is just floating. So if we want to share a wire, we need a third option, a state where a device says, in effect, I am not driving this wire at all. Let somebody else decide. That state has a name, high-impedance, and I'm going to call it the Z state from here on because it is shorter to write on the diagrams.

It helps me to think of it as a room with one microphone. Several people want to talk, but only one can hold the microphone at a time. The others have to stay quiet and let the one holding it speak. Nobody is shouting over anybody else. The silence is part of the protocol. A device that is not using the wire should be silent, not shouting a zero.

So how do we build that? The component is called a tri-state buffer. It has a data input, a data output, and an enable input. When enable is high, the output follows the input, so the device drives the wire to whatever value it wants. When enable is low, the output goes to Z. The device lets go of the wire completely. I've built one in the simulator here, and I'm going to toggle the enable line a few times, so you can see the wire follow the data when enabled and then just float when it is not.

Now watch what happens when I get greedy. Two buffers, both enabled at the same time, with opposite values on their inputs. One is trying to pull the wire high and the other is trying to pull it low. In the real world that is a short circuit, and things get hot. In the simulator, the wire is flagged as conflicting, and the LED goes into a state that I can only describe as unhappy. This is the single most important failure in the whole video, so I'm going to keep coming back to it.

I also want to correct something I believed for a while. When a wire is left floating, I assumed it would just keep whatever value it had last. That is not how it works, and it is not how the simulator behaves either. A floating wire is not holding a memory. It is just not connected to anything that has an opinion. So if you need a value to persist, something has to actually store it, and that is a different job.

Okay, so the rule is becoming clear. Several devices can share one wire, but only if at most one of them is driving it at any moment. Everybody else has to be in the Z state. Let's build a real bus to test this. Four registers, each holding a small value, all connected to the same wire. Each register has its own enable line, and a little control block decides which one is allowed to drive the bus this time.

I'll run it step by step. Enable register one, and its value appears on the bus. Disable it, enable register three, and the bus changes to match three. Nothing else changes, and nothing else needs to. It is a very satisfying thing to see, because the wire is now shared by four devices and none of them knows about the others. They only know whether they are enabled.

Before we settle on that design, let's try the obvious alternative, which is brute force. Instead of tri-state buffers, route every register into one big multiplexer, a selector that picks one of the inputs and passes it to the output. This works. It also gives you a very different machine. The multiplexer grows with every register you add, you need a lot of wiring, and you have to think about the select lines explicitly. It is correct, but it is clumsy, and it is not really what a shared bus is for.

So the tri-state version wins, and the reason is worth stating as a rule. At most one enable is high at any time. Every other device is in the Z state. If you hold that invariant, the wire is always either driven by exactly one source, or briefly driven by none. From that one rule, almost everything else falls out. You never need a central selector. You need a control scheme that never violates the invariant.

The control scheme deserves some attention, because it is where things get tricky. If the control logic changes the enable lines in the middle of a cycle, you can get a moment where two enables overlap, even if only for a fraction of a tick. The simulator shows this clearly. I can slow the clock down and watch a brief overlap appear between one register switching off and another switching on. The wire spikes, and the value read by the next stage is wrong.

Now let's add a clock, which is what real machines do. Every register reads and writes on the edge of the clock. The problem is that if two registers are both trying to read from the bus on the same edge, and one of them is also writing to it, the timing becomes a race. Which value wins depends on which gate settles first. Sometimes it is right and sometimes it is wrong, and that kind of bug is very hard to find in a real board.

The fix is to phase the clock. Split each cycle into two halves. In the first half, the register that is driving the bus is allowed to put its value on the wire. In the second half, the registers that are reading latch whatever is there. Once the phases are separated, the race disappears. I tried several other arrangements first, and all of them had a case where the reads happened too early or too late. The phased version is the one that survived every test I threw at it.

This is also where I want to step back and say why any of this matters outside the simulator. Older computers used shared buses like this for their memory and their peripherals. The idea that a single wire carries data between many parts, with a strict rule about who gets to drive it, is still how a lot of memory chips are wired internally. So the Z state is not a toy trick. It is the thing that makes a single wire into a conversation between many parts.

I should also say what this simulator is leaving out. Real tri-state buses have capacitance, real delays, and real analogue behaviour when two drivers briefly overlap. The simulator treats everything as clean zeros, ones and Zs, so it can tell you about the logic, but not about the electrical reality. If you ever build one of these on a breadboard, you will meet the analogue world quickly, and the invariant will matter even more.

Let me run the whole bus once more from the top, with all four registers, the clock phased, and the control block choosing who speaks. Watch the wire. Each value appears, holds for one phase, and gets read by the next register that needs it. No overlaps, no spikes, and no mystery values. It is a small thing, but it is a fairly complete story about shared hardware.

Now I want to come back to the opening question, and the lit wires on the board. Those lights are exactly this. Some device is driving the wire, the others are quiet, and the value on the line is the one the current owner decided to put there. The whole design is a set of rules for taking turns.

So to recap. We have three states on a wire, zero, one and high-impedance. A tri-state buffer lets a device step out of the way. The invariant is that at most one driver is active at a time. A clock lets us separate who writes from who reads. And the phased clock is what removes the race. Each of those pieces is simple on its own, and together they make one wire serve many devices.

For the next experiment, I want to put these buses to work inside something that runs a small program. The registers will hold data, the bus will carry it, and the control logic will decide the order of operations. That is going to take a lot more wiring, and I expect to break it several times before it works, so I'm looking forward to it. Thanks for watching, and I will see you in the next one.
NARRATION>>>

## Slots

```json
{
 "format_class": "experiment log, build-as-you-go",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.01,
 "first_new_idea_frac": 0.04,
 "first_notation_frac": 0.12,
 "payoff_frac": 0.58,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 4,
 "example_growth": "two switches -> three devices -> four registers",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.3,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the shared wire with an LED at the end, reused in 3+ sections",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 85,
 "beat_sequence": ["hook", "toy-world", "definition", "analogy", "demo-sim", "wall", "misconception-defuse", "demo-sim", "brute-force", "derivation", "wall", "generalize", "recap", "coda"],
 "top5_moves": ["build-and-verify", "failure-shown", "simulation-as-argument", "brute-force-first", "visible-repetition"],
 "absent3_moves": ["inline-quiz", "humor", "expert-dialogue"]
}
```
