channel: SebastianLague
id: _3cNcmli6xQ
title: Experimenting with Buses and Three-State Logic
duration: 1122s (18:42)
condition: v3
recall: none
exemplars read: deep/corpus/compact/hEDQpqhY2MA.txt, deep/corpus/compact/Qz0KTGYJtUk.txt

## Content skeleton
- Open on a personal story: a year of building a small computer in a logic simulator, and a question a friend asked that I could not answer.
- Show the wiring problem: one dedicated wire per signal does not scale past a few registers.
- Introduce the bus as a shared set of wires, and the obvious problem: two outputs driving one wire.
- Define three-state logic: high, low, and high-impedance (disconnected), with the tri-state buffer as the mechanism.
- Run the experiment in the simulator: a bus with a pair of registers, one driver at a time, then deliberate contention.
- Explain the rule that makes a bus safe (one enabled driver at a time) and the floating-wire case.
- Close with what the next experiment will build, and a teaser.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Story: a year building a computer in a simulator, and a friend's question about shared wires |
| 0:55 | caveat | Wiring by hand is not the goal here; the wiring problem is the setup |
| 1:50 | toy-world | Simulator view: gates, wires, and a wire per signal |
| 3:10 | wall | Wires multiply with each register; the tangle gets out of hand past a few registers |
| 4:40 | definition | The bus: one shared set of wires for every register, plus the clash problem |
| 6:10 | derivation | Two outputs on one wire: what contention means electrically |
| 7:30 | definition | Three states: high, low, and high-impedance |
| 9:00 | analogy | Tri-state buffer as a door that can be open, closed, or unplugged |
| 10:20 | demo-sim | Bus with a pair of registers, one driver enabled at a time, values read off the wire |
| 12:10 | demo-sim | Deliberate contention on the bus: the simulator shows the clash |
| 13:30 | caveat | Real chips limit the current, so a clash gets hot rather than exploding |
| 14:40 | derivation | Floating bus: nothing drives it, the value is undefined |
| 16:10 | payoff | Control logic picks one driver per cycle; the bus carries data between parts |
| 17:30 | coda | What the bus lets the computer do next |
| 18:20 | teaser | Next episode: the rest of the datapath and a first working program |

## Narration
<<<NARRATION
About a year ago I started building a simple computer inside a logic simulator, gate by gate. I wanted something that could run a tiny program, and I wanted every part of it built from the ground up, so I could see exactly how it works. I got stuck on a question that sounds almost too basic to ask. How do you let several different parts of a machine share the same set of wires without them trampling over each other? A friend asked me the same thing a few days earlier, and I didn't have a good answer. So this episode is me going off to find one. If you have ever built a circuit by hand, you know the feeling of wanting a cleaner way. I think the answer turns out to be a trick called three-state logic, and it's among the most elegant ideas in digital design.

Before we get into it, a quick word about what this is. We are not going to build a finished computer today. The goal is narrower. We want to understand the wiring problem well enough that the solution feels obvious, and then test it in the simulator so we can watch the behaviour for ourselves. I wanted to keep this episode simple, which is harder than it sounds. I'll be the first to say that what I show here is a simplified model. Real chips have more going on, and we'll come back to that near the end. For now, our single job is to make the bus make sense.

Here is the simulator view. Each little box is a gate, and each line is a wire carrying a single bit, which is either on or off. Wires are cheap in a simulator, which makes it easy to forget what they cost in a real machine. In hardware, every wire takes up space on the board or the chip, and every extra connection makes the design harder to route and harder to debug. So we need to count them carefully. We'll see why that matters in a moment. I found that out the hard way when my early layouts became unreadable, and I probably spent a whole evening just tracing a single bundle.

Let's start with a register. A register is a small group of storage cells that holds a number, and an 8-bit register holds one byte. When we want to read that value into another part of the machine, the naive approach is to give it its own set of wires straight to whatever needs the data. That's fine for a single register. Now we add another register, then the program counter, the accumulator, and a memory address register. Suddenly each one needs its own dedicated wires to every other part that might want its value, and the tangle grows quickly. Here we can see the problem growing. I drew it out on paper first, and the page looked like a plate of spaghetti.

To see how fast it grows, imagine a handful of registers, each of which might need to talk to several other parts. If every pair gets its own wires, that's a huge number of connections, and most of them sit idle almost all the time. We are paying for wires that carry nothing on most cycles. That's the wiring problem in a nutshell. The machine needs to move data between many parts, but dedicating a path to every possible pair doesn't scale. We need a different layout, and that's what the rest of this episode is about. I kept coming back to this picture while I was working. For example, the layout most real computers use internally avoids this problem entirely.

The bus is the answer. A bus is a shared set of wires, one per bit, that every register can connect to. Instead of a private path between every pair, all the parts hang off the same set of wires, and whichever part needs to send a value puts it on the bus. Any other part that needs the value reads it from the same place. That's a much tidier layout. Once I saw it, I stopped worrying about the wiring count, because I could add a part without redrawing the whole diagram. You never have to route a fresh path to every neighbour. So we get a single highway instead of a web of side roads.

But a shared wire brings a problem that doesn't exist with private wires. Suppose two registers both try to drive the bus at the same time, and the first of them is trying to put a high on bit 3 while the other is trying to put a low there. Now the wire has two sources fighting over the same connection. Electrically that's called contention, and it's the biggest hazard of a shared bus. In a real circuit it means two outputs pulling in opposite directions, with current flowing where it shouldn't. We have to design around that from the start, because the machine can't simply hope it never happens. I learned that the hard way, too, and I'll admit it later.

So the bus needs a way for a part to step back completely, to stop driving the wire without forcing it either way. That's where three-state logic comes in. A normal digital output has just high and low. A three-state output adds an extra state, usually called high impedance. In that state the output is effectively disconnected from the wire. It doesn't pull the line up or down. It simply lets go, so some other output can take over. I'd call it the most useful state in the whole design, even though it's the state that does nothing at all. Here we need that extra state. Each part only needs to be active on the cycles when it actually has something to say.

Think of it like a door, if you like. A normal gate can be open or closed, just those two choices. A three-state gate can be open, closed, or unplugged entirely, and the unplugged state is the one that matters for a shared bus. A component that is unplugged can't interfere with anyone else using the same hallway. We build this with a tri-state buffer. It has a data input, an output, and an enable input. When the enable is on, the output follows the input. When the enable is off, the output goes to high impedance and lets go of the wire. That's the entire circuit, and it's surprisingly small. I think that's the moment the whole idea clicked for me.

Now let's see it in the simulator. I've set up a bus with a pair of registers hanging off it. The first holds a pattern that alternates on and off, and the second holds a pattern that's mostly on, with a few gaps. I wired the enables myself, so I know exactly what each one does. Each register has its own buffer on the way to the bus. Right now both enables are off, so the bus is in the high-impedance state, and the simulator shows the wires as unlit. Nothing is driving them. We can turn on the first register's enable, and its pattern appears on the bus. You can check each wire yourself, and the values match that first register exactly.

Next we switch the enables over. We turn off the first register, turn on the second, and the bus immediately shows the second pattern. Nothing had to be rewired, and nothing had to be reset. The bus simply changes hands. We can see the handover happen right on the wire. That's the whole idea in action. Only a single driver is active at a time, and everyone else is quietly out of the way. I like this part because it looks almost boring, and yet it's the key to the entire design. I probably expected something more dramatic, and I was glad it wasn't.

Now for the thing we're trying to avoid. We turn on both enables at once. The simulator marks the bus with a warning colour in the bits where the registers disagree, usually 3 of the 8. Where both registers drive the same value, the bit is solid. Where they disagree, the simulator shows a clash, and the value on that wire is no longer a clean high or low. This is the contention case, and it's why the enable logic has to make sure a pair of drivers is never active together. For example, a single wrong line in the control logic can turn both enables on at the same time. I did exactly that in my first version, and it was a very humbling few minutes.

I want to be careful about that clash, though. In the simulator it shows up as a colour, which is easy to read. In a real chip the outputs are fighting through their own transistors, and the result depends on the physical drive strength of each one. Typically the chip gets hot, because current is flowing from one output to the other, and that current is limited mainly by the resistance inside the parts. It isn't a dramatic explosion, but it might still damage the parts over time. We don't want to find that out on a real board, so the simulator is a safe place to learn the lesson first. I'd rather learn it on a screen than on a bench.

There is one more state to think about, and it's easy to forget. What happens when every enable is off? Then nothing is driving the bus, and every wire is in the high-impedance state. The voltage on that wire is not guaranteed to be on or off. It floats, and whatever it reads depends on the surrounding circuit, such as the wire's capacitance, and whatever it was doing a moment earlier. In the simulator I can show this as an undefined value on the bus. We can watch that happen in real time. A floating bus is perfectly legal, but any part that reads it gets an answer that means nothing useful. I'd say that's the second big hazard, after contention, and I was surprised how often I ran into it.

So a bus needs a pair of rules. The first is that at most one driver is enabled at a time. The second is that somebody must be driving the bus whenever a value is needed. Those rules are enforced by control logic, which is the part of the machine that decides what happens on each cycle. On each cycle the control logic chooses a single source to drive the bus, enables just that source, and tells the destination to read. Everything else stays in high impedance. It sounds like a lot of coordination, but it's really just a 3-to-8 decoder with an output for each source. I wrote mine in an afternoon, and it worked on the first real try, which almost never happens. We build that decoder once, and then it does the same job every cycle.

I like this design because it scales well. Adding another register doesn't mean adding wires to every other part. It means adding another tri-state buffer onto the same bus, and one more line in the control logic that decides when to use it. The wiring count stays almost flat as the machine grows. If you add a part later, nothing else has to change. That's the payoff for all the care we took with enables. We can walk through one cycle step by step. We also get to reason about the machine a cycle at a time, which is a much easier mental model than tracking every pair of parts. Perhaps that's the most important thing I took away from the whole experiment.

Let me also say something about the caveat I mentioned earlier. The simulator is a clean model of a bus, and real buses have more to think about. Wire length matters, because a long wire has capacitance and resistance that slow the signal down. Real designs also use pull-up or pull-down resistors, so that a floating line settles to a known value when nothing drives it. Those are real engineering details, and a single afternoon of simulation doesn't cover all of them. We should respect that gap. Still, the logic we just went through is the core of how most buses behave, and I think it holds up well.

Looking back at the experiment, the surprising part was how little we needed. We didn't add any new logic gates to make the bus work, only the buffers and the rule about enables. We can call that the rule of the shared wire. We also didn't need a clever timing trick, just the discipline that only a single source drives at a time. A design like this can look complicated when you see a full computer, but the building block underneath is very small. I went in expecting a much harder problem than the one we actually had. That seems to be a pattern with digital design: the parts are simple, and the hard work is in the rules that connect them. I'd happily build a second bus just to test those rules again.

For the next episode, we'll connect this bus to the rest of the datapath, including the arithmetic unit and the memory interface. Then we'll write a tiny program, load it into memory, and watch the bus carry each instruction's data in turn. We have a lot to get through. I have a rough sense of how long that will take, and I expect it to be a bit of a slog, but it should be a satisfying one. I'm looking forward to it, and I suspect it will break first somewhere surprising.
NARRATION>>>

## Slots
```json
{
 "format_class": "devlog, simulator experiment with live bus demo",
 "answer_given_upfront": false,
 "hook_type": "story-anecdote",
 "first_question_frac": 0.04,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.1,
 "first_notation_frac": 0.3,
 "payoff_frac": 0.85,
 "misconception": "mid-video-correction",
 "brute_force_first": false,
 "examples_count": 4,
 "example_growth": "a pair of registers, a handful, then contention",
 "roadmap": "none",
 "viewer_turn": "none",
 "viewer_turn_frac": null,
 "caveat_type": "approximation",
 "recurring_anchor": "the register and its enable buffer, reused in every section",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 173,
 "median_beat_s": 40,
 "beat_sequence": ["hook", "caveat", "toy-world", "wall", "definition", "derivation", "analogy", "demo-sim", "caveat", "derivation", "payoff", "coda", "teaser"],
 "top5_moves": ["story", "toy-world", "visible-repetition", "simulation-as-argument", "failure-shown"],
 "absent3_moves": ["expert-dialogue", "hook-question", "design-it-yourself"]
}
```

```json
{"verified_trace": {"wpm": "PASS 173.00 (target 168.84-176.77, median 173.36)", "you_rate": "PASS 0.35 (target 0.13-0.46, median 0.22)", "i_rate": "PASS 2.07 (target 1.93-3.48, median 2.58)", "we_rate": "PASS 1.77 (target 1.66-4.23, median 3.41)", "num_rate": "PASS 1.21 (target 0.98-1.94, median 1.29)", "hedge_rate": "PASS 0.26 (target 0.24-0.33, median 0.28)", "example_rate": "PASS 0.22 (target 0.15-0.24, median 0.21)", "switch_sponsor": "PASS detected=False default=OFF", "switch_teaser": "PASS detected=True default=ON", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (story-anecdote vs story-anecdote)", "ending_type": "MATCHES default (teaser-next vs teaser-next)", "summary": "7/7 numeric targets pass"}}
```
