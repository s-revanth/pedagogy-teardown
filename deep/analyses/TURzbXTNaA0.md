# I Created a (terrible) Video Game Console (SebastianLague, 9 min)

## Arc
Shelf of beginner electronics (0:00), Arduino as a small computer with pins (0:19), joystick and potentiometer research (0:36), wire and read a value (1:45), display (2:53), buzzer and music editor (3:29), snake and shooter code (4:36), case building and failures (6:09), power problem (8:10), self-deprecating wrap (8:26). This is a project vlog with light teaching, not a structured explainer.

## Strongest moves
1. **Familiar first, then mechanism (0:36-1:30).** Starts from what a potentiometer does in volume and light dimmers, then explains the wiper on a resistive track, then the outer-terminal voltage reading. Knowing the voltage tells the knob angle, which becomes the joystick position.
2. **Verify understanding on the real device (1:30-2:18).** He says he is checking his understanding, then does wiring, a short script and watching the number rise with the knob.
3. **Pre-empt the misconception (2:02-2:18).** The reading is 0 to 1023, not a thousand volts: 5 V mapped to a 10-bit integer. One sentence, with humour.
4. **Performance failure shown (5:14).** Turning LEDs on one at a time costs about 15 ms per frame, replaced by row-bit buffers. Brute force first, then the fix.
5. **Failure as comedy (4:00, 7:14).** The music editor is annoying, the cover is glued wrong twice. Low-stakes tone invites beginners.

## Unusual
Very little notation or theory; depth is intentionally shallow. Each part is studied just before it is used. Honesty about the result being pre-built parts in a poor box (8:51) doubles as a callback to the opening premise.

## Principle verdicts
1 confirmed. 2 partly. 3 not observed. 4 partly. 5 confirmed. 6 confirmed (LED one at a time). 7 partly. 8 not observed; idea rate is fast and shallow. 9 partly. 10 confirmed (one pot then two, one display then two). 11 confirmed. 12 partly. 13 partly.

## Velocity implications
- Scene builder: just-in-time component intros with a live readout widget.
- Voice: self-deprecating casual register as an option for nervous novices.
- Orchestrator: project-arc playbook (input, output, game, case) for motivation.
- Evals: tutor asks to see a reading right after a concept.
- Caution: this video is weak evidence for rigor transfer; use it for tone and sequencing, not for depth.
