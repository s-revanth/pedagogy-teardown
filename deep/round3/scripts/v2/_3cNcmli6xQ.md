# SebastianLague | _3cNcmli6xQ | Experimenting with Buses and Three-State Logic

- channel: SebastianLague
- id: _3cNcmli6xQ
- title: Experimenting with Buses and Three-State Logic
- duration: 1122 s (18:42)
- condition: v2
- recall: none (not recognised; written from the rulebook and general knowledge of logic circuits)
- class (step 0): over-10 min; format = devlog experiment (first-person, no series label); answer not stated up front; open question (how to share one wire between many drivers); topic = computer hardware and logic
- exemplars read: deep/compact/QZwneRb-zqA.txt (Exploring How Computers Work, 18 min) read in full; deep/compact/PGk0rnyTa1U.txt read in full for devlog voice

## Content skeleton
- Cold open on the classic problem: many parts sharing one wire, with 256 enable settings and only 9 safe.
- Naive wiring: two always-on outputs on one wire; a conflict flag fires (failure on screen).
- Mid-video correction: 'off means zero' was wrong; the third state (let go, high impedance) makes sharing possible.
- Honest caveat on transistor-level understanding; the tri-state chip datasheet is cited at the choice.
- Build a tri-state buffer from switches; the same sweep table is run on every variant.
- Silent screen run, then a pause-or-guess about two drivers enabled at once; answer: conflict.
- Eight drivers behind a three-bit decoder; registers read the bus back; a deliberate break and fix.
- Timing caveat, scaling of select lines, and a counter loop as the closing test; no recap, no teaser.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Classic problem on screen: eight drivers, one wire, 256 enable settings, 9 safe. Premise stated, no answer yet. |
| 0:50 | toy-world | One wire, high or low (1 and 0). One output driving it works; the trouble starts with a second output. |
| 1:35 | demo-sim | Naive wiring: two always-on outputs joined to one wire. Conflict flag lights; the wire has no valid value. |
| 2:30 | misconception-defuse | Narrator's own belief that off means zero is wrong; a third state, let go (Z), is introduced. |
| 3:20 | caveat | Only a rough understanding of the transistor level; the tri-state chip datasheet is cited to check the behaviour. |
| 3:55 | demo-sim | Buffer built from switches: data in, enable line, output connects or disconnects. Three states from one circuit. |
| 4:45 | demo-sim | Sweep table run on the buffer: enable off gives Z, enable on gives the data. Same table reused for every variant. |
| 5:35 | demo-sim | Shown, no narration: the switch circuit runs under three random input patterns for about four minutes. |
| 9:35 | viewer-turn | Pause-or-guess: two buffers enabled onto one wire, one drives 1 and one drives 0. What does the wire read? |
| 9:55 | payoff | Answer: conflict, not zero and not one. Rule stated: at most one enable line on at a time. |
| 10:20 | demo-sim | Eight drivers, each with an enable; a three-bit address feeds a decoder so exactly one line is on. |
| 11:10 | demo-sim | Sweep of all eight addresses; the wire follows the selected driver; the conflict flag never fires. |
| 11:55 | demo-sim | Two registers added: one loads from the bus, one drives onto it; a load line and an output line. |
| 12:40 | demo-sim | Deliberate break: the decoder select floats, two registers drive, the stored value turns to garbage; fix; rerun. |
| 13:30 | caveat | Timing not modelled: real controllers add dead time between switching one driver off and the next on. |
| 14:15 | generalize | Scaling: 8 drivers need 3 select lines, 16 need 4, 256 need 8; each driver still needs its own buffer. |
| 15:00 | demo-sim | Switch-per-driver alternative compared; the decoder keeps the one-driver rule inside the wiring. |
| 15:40 | demo-sim | Counter loop run for several hundred steps on the bus; log shows no conflicts (mostly shown, little narration). |
| 16:50 | coda | One lesson stated: a shared wire needs three-state drivers and enable lines that guarantee one driver at a time. |
| 17:50 | coda | Not a complete computer; the bus stays in the machine for the next experiment. |
| 18:25 | coda | Closing thanks; the video ends on the running counter. |

## Narration
<<<NARRATION
Here's a classic problem: a computer has lots of parts that need to pass numbers to one another, and the cheapest way to connect them is a single shared wire. That sounds simple, until two parts try to drive the same wire at the same time with opposite values. With eight drivers on one wire there are 256 ways to set their enable lines, and only 9 of those settings are safe. That is a lot of ways to short something out, so in this experiment we want to see whether a shared wire can be made to work at all.

Let's start with the wire itself, and in our simulation a wire is either high or low, which we call 1 and 0. Any output connected to it can pull the wire high or pull it low, and that works fine with one output, and we can see it on screen, steady. The trouble starts as soon as a second output is wired to the same place, because nothing in the circuit says which one should win.

So the first thing we tried was the obvious wiring, with two outputs, both always on, joined to one wire. I watched the simulation light up a conflict flag straight away, because both drivers were pulling against each other and the wire sat in no valid state at all. That's the failure we need to avoid, and it's also where I'd start, because it shows exactly what breaks and why the fix has to be structural rather than a matter of tidier wiring.

Then I had to ask what an output should do when it isn't driving the wire. My instinct was that off means zero, and I carried that around in my head for quite a while. That turns out to be wrong, and a proper output can be in a third state where it simply lets go of the wire, so it neither pulls high nor pulls low. Engineers call that high impedance, and i'll write it as Z in these notes, and that third state is the piece that makes a shared wire possible at all.

We're going to be careful here, because we only roughly understand what happens at the transistor level. The idea I'm confident in is this: a buffer with an enable line either passes its input through to the wire, or it lets go. The datasheet for a common tri-state buffer chip describes exactly that behaviour, and I used it to check the sketch before I trusted my own version of the circuit.

Let's build one from switches, and the data input feeds two switches arranged in a pattern, and the enable line decides whether the output is connected to the wire or disconnected from it. When enable is off, nothing is connected and the wire is free. When enable is on, the output follows the data input. That is three states from one small circuit, and it's all we need for everything that follows.

We'll test it the same way every time, because a repeatable test is what lets us trust a change. We'll sweep the data input through 0 and 1, then sweep the enable through off and on, and write down what the wire does for each combination. Enable off gives Z, which means nothing drives the wire. Enable on with data 0 gives 0, and enable on with data 1 gives 1. That same table goes on screen for every variant from here on, so we can compare them row by row.

Pause here if you want to guess before I show the answer. Two buffers are enabled onto the same wire, one drives 1 and the other drives 0. What does the wire read? Take a moment with it.

The answer is conflict, not zero and not one. Both outputs are connected and pulling in opposite directions, so the simulation flags the conflict and the wire has no valid value. Real chips can probably overheat in exactly this situation, which is why it's worth taking seriously even in a toy model. The rule is simple once we see it: at most one enable line should be on at any moment. If you have ever wired a shared line by accident, you know the feeling.

So the next version puts eight drivers on one bus. Each one has its own enable line, and we need a way to guarantee that only one of them is active. The easiest way is to drive the enables from a three-bit address. Three bits can name eight values, so each address turns on exactly one buffer. That piece is called a decoder, and it's a small block with eight outputs where exactly one line is high at a time. For example, the address 101 turns on driver number five and leaves the other seven off.

Here's the sweep for all eight, and we set the address to 000, put a value on driver 0, and read the wire. Then we set address 001, a different value on driver 1, and read the wire again. The wire follows whichever driver is selected, and the conflict flag never fires. Eight runs, eight matching readings, and the table is the same table I showed earlier, just wider. Nothing in the table has changed except the number of rows.

We also need to read the bus back, and right now the bus is only a path from the drivers to the wire, so a register sitting on the bus has to be able to read the value by listening on the same line. We make a register that can load from the bus, and another that can drive its stored value onto it. A load line decides whether the register captures what is on the wire, and an output line decides whether the register puts its value onto the wire. Both lines are just enables, so the same rule applies to them as well.

That's a small machine now, and we have two registers, a bus, and a decoder that picks which register drives at any moment. The program we're going to run is simple: load a value into one register, add it to the other through the arithmetic unit we built earlier, and store the result back. We'll run the program once and check the answer by hand, then run it again on a slightly changed design and check that the same answers come out. Repeating the same test is how we catch a change that quietly broke something.

Let's do one more run on purpose, with the enable lines wrong. We'll leave the decoder's select floating for a moment, so two registers drive the bus at the same time. The conflict flag fires, and the stored value turns into garbage, which is exactly what we would expect. Then we fix the decoder, rerun the same program, and the flag stays off. Seeing it break and then seeing it recover is the strongest evidence I have that the logic is right, because a passing test alone can hide a wiring mistake.

Now I want to be honest about what I'm not modelling. We don't fully know how real bus controllers handle timing when two enables switch at nearly the same moment. In this simulation every change happens in a single step, so the question never comes up. On real hardware there is a short gap where two drivers could both be on, and that's why designers add a small dead time between switching one driver off and the next one on. we're not going to model that here, and we'd want a proper source before claiming anything about it, so you should check it yourself.

Next is the scaling question, which is where the experiment starts to feel like engineering. With the decoder, a bus of 8 drivers needs 3 select lines. A bus of 16 drivers needs 4, a bus of 256 needs 8, and the decoder grows slowly, which is a good trade. But every extra driver still needs its own buffer and its own decoded line, so the wiring inside the chip keeps growing with the number of drivers. That cost doesn't go away, and it's the reason real machines use fewer, wider buses rather than many narrow ones.

We considered a row of plain switches instead, one for each driver, but then somebody has to set them by hand, which just moves the problem somewhere else. The decoder keeps the one-driver rule inside the wiring, so we don't have to trust the program to behave.

Let's look at the full sweep once more, from the top. Eight drivers, one address, one wire, and the same table on every row, with the registers reading back exactly what they were given. I don't see any conflicts in any of the rows. For the last part of the experiment we're going to run a longer program, a loop that adds 1 to a counter and stores the result each time through the loop. It's a bit dull to watch, but dull is exactly what we want from a bus.

The loop runs for several hundred steps, and the counter goes up by one each time with no conflicts anywhere in the log, which is roughly what we want. Nothing surprising happens, and after the earlier breakage we are glad of that. We get the same kind of step every time, and that repetition is what makes the machine trustworthy.

So the lesson we'd keep is short, and a wire can be shared if every driver has three states, low, high, and let go, and if the enable lines guarantee that only one driver is active at a time. The decoder is what makes that guarantee cheap to build, and the conflict flag is what tells us the moment the guarantee has been broken. Everything else on the bus is careful wiring, and careful wiring is mostly a matter of repeating the same test until you stop being surprised by it.

This experiment is far from a complete computer, and there's no memory hierarchy, no clock distribution worth mentioning, and the registers are a stand-in for something much more complicated in a real design. Still, the core idea of one shared path with a rule for who may speak on it is a large part of how real machines move data around. We'll leave the bus in the machine and keep building from here, and we'll see each other in the next one.

Thanks for watching this experiment all the way through, and we'll be back to the wire soon, probably with a bigger bus.
NARRATION>>>

## Slots
```json
{
 "format_class": "devlog experiment: adjacent classic problem with blow-up number, failure on screen, mid-video correction, pause-or-guess",
 "answer_given_upfront": false,
 "hook_type": "premise-claim",
 "first_question_frac": 0.03,
 "first_concrete_object_frac": 0.05,
 "first_new_idea_frac": 0.08,
 "first_notation_frac": 0.22,
 "payoff_frac": 0.8,
 "misconception": "mid-video-correction",
 "brute_force_first": true,
 "examples_count": 4,
 "example_growth": "two drivers -> eight drivers -> two-register machine -> counter loop",
 "roadmap": "none",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.51,
 "caveat_type": "epistemic",
 "recurring_anchor": "the shared wire with enable lines, reused in 5+ passes",
 "sponsor_frac": null,
 "ending_type": "impact-coda",
 "teaser": false,
 "beat_sequence": [
  "hook",
  "toy-world",
  "brute-force",
  "misconception-defuse",
  "caveat",
  "demo-sim",
  "viewer-turn",
  "payoff",
  "demo-sim",
  "generalize",
  "coda"
 ],
 "top5_moves": [
  "failure-shown",
  "build-and-verify",
  "honest-caveat",
  "visible-repetition",
  "brute-force-first"
 ],
 "absent3_moves": [
  "hook-paradox",
  "commit-to-answer",
  "expert-dialogue"
 ],
 "wpm": 95,
 "median_beat_s": 45
}
```

```json
{"rule_trace": {
 "U1": "applied: devlog format gate (topic type devlog); under-10 items n/a at 18:42; roadmap and callback withheld; recap off",
 "U2": "n/a: neither the title nor the first 40 s states the answer; the answer comes after the naive failure",
 "U3": "applied: impact coda (running counter and one-line lesson); no teaser (not a series); hook question not left open, so no callback",
 "U4": "applied: the shared wire with enable lines is reused in 5+ passes, each adding one layer (driver, decoder, register, loop)",
 "U5": "applied: notation (1, 0, Z) introduced only after the wire and switch circuit give each state a referent; no formulas",
 "U6": "applied: 146 wpm channel median for the over-10 band; silent screen runs between spoken segments, not a fixed 20-25 s grid",
 "U7": "applied: no roadmap, no vote, no commit prompt; the misconception is the presenter's own, corrected mid-video",
 "U8": "applied: epistemic caveats on transistor-level understanding and on real-chip timing; datasheet cited",
 "U9": "applied: one pause-or-guess at 51% (about 9:35), answered after about 20 s",
 "U10": "n/a: not a history-of-invention or escalating-antagonist video",
 "U11": "n/a: title names a topic and an experiment, not an application or an end state",
 "C1": "applied: devlog (experiment-diary) format, not impersonal lecture and not a series lesson",
 "C2": "applied: the shared wire is rerun with one layer per pass and the same sweep table each time",
 "C3": "n/a: not lecture format; the pause is one guess, not a quiz",
 "C4": "applied: the tri-state buffer chip datasheet is cited at the moment the third state is introduced",
 "C5": "applied: devlog opens with an adjacent classic problem (sharing one wire) and a human-scale blow-up number (256 enable settings, 9 safe)",
 "D1": "applied: failure on screen (two drivers conflict; the stored register value turns to garbage)",
 "D2": "n/a: no repair term is named after the failure; the decoder is named by its function",
 "D3": "applied: one knob isolated in the break-and-fix run (the decoder select)",
 "D4": "n/a: no honest-close bundle; caveats sit inline and the ending is an impact coda",
 "D5": "n/a: no equation is revealed as a label after behaviour",
 "N1": "n/a: under-10 band rule; this video is over-10 min",
 "N2": "broken: 95 words per minute (measured), outside p25-p75 137-158; the 1,800-word cap gives about 95 wpm over this 18:42 runtime; spoken segments run near the band and silent screen runs fill the rest",
 "N3": "applied: 0.34 you/your per 100 words (measured), inside p25-p75 0.23-0.78",
 "N4": "applied: 0.96 I/me/my per 100 words (measured), inside p25-p75 0.94-2.81",
 "N5": "applied: 2.59 we/us/let's per 100 words (measured), inside p25-p75 2.55-5.7",
 "N6": "applied: 1.35 numbers per 100 words (measured), inside p25-p75 0.95-2.12",
 "N7": "applied: 0.06 question marks per 100 words (measured), inside p25-p75 0.0-0.09",
 "N8": "applied: 20.7 words per sentence (measured), inside p25-p75 19-25",
 "N9": "applied: 0.23 hedges per 100 words (measured), inside p25-p75 0.11-0.35",
 "N10": "applied: 0.06 example cues per 100 words (measured), inside p25-p75 0.03-0.18",
 "B1": "applied: no sponsor read",
 "B2": "n/a: not a series; U3 withholds the teaser",
 "B3": "n/a: roadmap withheld; a devlog experiment does not call for one",
 "B4": "applied: no full recap; the closing paragraph states one lesson only"
}}
```
