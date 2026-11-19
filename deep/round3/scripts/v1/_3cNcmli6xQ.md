# Header
- channel: SebastianLague
- id: _3cNcmli6xQ
- title: Experimenting with Buses and Three-State Logic
- duration: 1122 s (18:42)
- condition: v1
- recall: vague

## Content skeleton
- A bus is many wires carrying one shared signal, and many devices want to use it.
- Two outputs driving one wire at once is a conflict, and the value is undefined.
- Three-state logic adds a high-impedance state, meaning the output lets go of the wire.
- A tri-state buffer built from simple gates, checked with a full truth table.
- Make-before-break glitch when one driver hands the wire to another; fixed by a gap.
- Scaling from one switch to a 4-bit and an 8-bit shared bus.
- Honest approximation: a gate-level model, not real transistor timing.
- Callback to the opening two switches; teaser for the next build.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Two switches drive one wire on screen; what happens when they disagree? |
| 0:30 | roadmap | Build a shared bus, then make it safe to share |
| 1:00 | toy-world | One lamp, one switch, one wire in the sim |
| 2:30 | brute-force | Wire two switches directly to the same line; flip them |
| 4:00 | wall | Wire shows an undefined grey state when both drive it |
| 5:30 | definition | High impedance as "let go of the wire": minimal definition |
| 7:00 | demo-sim | Tri-state buffer from gates; enable input; truth table appears |
| 9:30 | derivation | Read the table: enable decides whether the data reaches the wire |
| 10:30 | misconception-defuse | Assumed the bus needs a clock; the enable bit alone is enough |
| 11:30 | demo-sim | 4-bit bus, four sources, same sweep for each source |
| 13:30 | generalize | Same idea used for a shared CPU bus between memory and devices |
| 14:30 | wall | 8-bit bus glitches when one source hands over to another |
| 15:30 | demo-sim | Gap between disable and enable removes the conflict; sweep again |
| 16:00 | payoff | Eight sources share one bus cleanly across the full sweep |
| 16:30 | caveat | Gate-level model; real chips have timing I am not modelling |
| 17:30 | recap | Three ideas: shared wire, let go, one gap |
| 18:00 | callback | Back to the two switches, now they take turns |
| 18:20 | teaser | Next build: memory on the bus |
| 18:34 | coda | Sign-off |

<<<NARRATION
So here is a question. What happens when two switches are wired to the same wire, and one of them says on while the other says off?

We are going to find out, and then we are going to build a bus that can be shared safely. Plan first. We will break a shared wire on purpose, then add a third state that lets a device let go, and then scale the idea up to eight wires.

Start with the toy world. There is one lamp, one switch, and one wire between them. Flip the switch and the lamp turns on. That is the whole of it, and it is simple enough that every later failure will come from the new part, not from the setup.

Now the dumb version. I take a second switch and wire it to the same line as the first one. Both switches are now outputs driving one wire. Let's flip them. If both are off, the lamp is off. If one is on, the lamp is on. That looks fine, which is exactly why the next part is worth looking at.

Here is the case where they disagree. One switch says on, the other says off, and both are connected to the wire at the same time. In the real world that is a short between a high and a low, and the wire has no clean answer. In the sim it shows up as a grey state. Grey means undefined, so the wire is neither zero nor one. That is the wall. The design does not work when two devices talk at once.

So the question becomes, how do you let a device be connected to the wire without the device always pushing on it? That is where the third state comes in.

Let's define it as small as possible. Each output can be a zero, a one, or high impedance. High impedance means: I am not touching the wire. It is not zero, it is not one, it is nothing at all. In effect the output lets go. That is the entire definition. Do not worry about how a real circuit does it yet. The only job is to have three options.

Now I want a device that can do this. I build a tri-state buffer out of simple gates. It has a data input, and an enable input. When enable is on, the output copies the data. When enable is off, the output lets go of the wire. The circuit is a few gates, and I am not going to walk through every one. I am going to test it.

Here is the test. There are two inputs for the data and the enable. That gives four combinations, and I write out the truth table for all four. The data goes to the wire only when enable is on. When enable is off, the wire is high impedance, and I show that as a dim line in the sim. Every row is checked by the same sweep, so you can see the result on screen.

Now read the table. It is the same table every time, and the enable bit is the only thing that decides whether the data gets through. That gives the rule for the bus: at most one device has its enable on at a time. If every device lets go except one, the wire has one owner, and it is clean. The table is the whole argument.

Here is a mistake I made while I was building this. I assumed that the bus would need a clock, so that the devices take turns on each tick. I wrote a clock into the design, and it made the sim harder to read. Then I realised the enable bit alone is enough, provided only one bit is on at a time. The clock is a way to enforce that rule, but the rule is the part that matters. Take the clock out and the bus still works, as long as the enables are controlled. So I took it out, and I was right to do so.

Now let's scale up. I wire four buffers to a four-bit bus. Each buffer drives its own enable, and I choose one source at a time. The sweep is the same as before, but now it runs across all four sources. Source one on, the others off. Source two on, the others off. And so on. I check the bus value after each step. It takes the value of whichever source is on, and nothing else leaks through.

This is the same idea as the shared bus inside a computer. A processor talks to memory, to a graphics card, to a network device, all over shared wires. Only one of them can drive the bus at a time. Every other device lets go, and the bus carries exactly one conversation. The sim is small, but the rule is the same one.

Now the eight-bit version, and this is where I got caught out. When I switch from one source to the next, there is a tiny moment where the old enable is still on and the new enable is already on. For that moment, two devices are driving the bus. In the sim it shows up as a short grey flicker on some bits. It is not a logic bug in the table, which is the annoying part. The truth table is correct, and the timing is still wrong.

The fix is a gap. Disable the old source first, wait one step with nobody driving the wire, and only then enable the new one. Break before make. I did not expect a single empty step to matter this much, but it removes the flicker completely. So I add that step, and then I run the eight-source sweep again. Every source takes its turn, and no step shows a conflict. That is the payoff I wanted from the start.

Here is what I need to be honest about. This is a gate-level model. Real chips have timing, capacitance and a lot of analogue behaviour that I am not modelling. The gap I added is a clean abstraction of what a real controller would do. I do not know the exact margins a real chip needs, and I am not going to pretend I do. What I have shown is the logic, and the logic is right.

So let's recap the three ideas. The first is that a shared wire needs a rule about who is driving it. The second is that a device must be able to let go, which is the high-impedance state. The third is that the handover needs a gap, so that two drivers never overlap.

Now go back to the two switches from the start. They were fighting over one wire, and the wire had no answer. Now they take turns. One is connected while the other lets go, and the wire always has a clear value. It is the same wiring as before, with one extra bit that says who is allowed to talk.

Next time we will put memory on this bus, and see what happens when a device reads back from the wire it just wrote to. I suspect that is where the real trouble starts. Thanks for watching.
NARRATION>>>

## Slots

```json
{
 "format_class": "toy build, failure then fix",
 "answer_given_upfront": true,
 "hook_type": "question",
 "first_question_frac": 0.005,
 "first_concrete_object_frac": 0.01,
 "first_new_idea_frac": 0.03,
 "first_notation_frac": 0.37,
 "payoff_frac": 0.86,
 "misconception": "mid-video-correction",
 "brute_force_first": true,
 "examples_count": 4,
 "example_growth": "two switches -> four bits -> eight sources",
 "roadmap": "one-line",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.005,
 "caveat_type": "approximation",
 "recurring_anchor": "the grey undefined wire colour, checked after every change",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 60,
 "beat_sequence": ["hook","roadmap","toy-world","brute-force","wall","definition","demo-sim","misconception-defuse","demo-sim","generalize","payoff","caveat","callback","teaser"],
 "top5_moves": ["toy-world","brute-force-first","failure-shown","visible-repetition","generalize-to-other-domains"],
 "absent3_moves": ["hook-paradox","expert-dialogue","commit-to-answer"]
}
```
