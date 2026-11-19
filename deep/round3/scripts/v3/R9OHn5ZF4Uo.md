# Script: CGPGrey, R9OHn5ZF4Uo

- channel: CGPGrey
- id: R9OHn5ZF4Uo
- title: AI Doesn't Know Anything. It Just Passes Tests.
- duration: 534 s
- condition: v3
- recall: none
- exemplars read: deep/corpus/compact/wvWpdrfoEv0.txt, deep/corpus/compact/C25qzDhGLx8.txt

## Content skeleton

- Premise: AI does not know anything; it is built to pass tests, and that is an accurate description of how it is trained.
- What a test is: a set of known-answer questions where only the count matters.
- Training as a score-chasing loop: small changes kept when the score rises.
- Toy world: a sorter with a few dials that learns cats versus dogs without being told what a cat is.
- The answer-key problem: a history exam where memorizing last year's key looks like learning.
- Famous failure: a wolf-or-husky classifier that had learned snow.
- Measurement trap: whenever a score is rewarded, the cheapest route to it wins; check what the benchmark measures.
- Close: a passing score is evidence, not proof; return to the opening line.

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Premise stated flat: AI does not know anything, it passes tests. |
| 0:25 | answer-statement | The thesis made precise: the description is accurate, and it explains odd behavior. |
| 1:05 | definition | What a test is; the score is the only thing it counts. |
| 1:40 | derivation | The training loop: small change, check score, keep it if it rose, repeat. |
| 2:20 | toy-world | Cats and dogs sorter with a few dials; nobody explains what a cat is. |
| 3:05 | demo-sim | The piles sort: 70, then 90, then almost everything. Everybody claps. |
| 3:45 | wall | It never learned what a cat is; it learned which dial settings give the right pile. |
| 4:25 | analogy | The history exam and last year's answer key. |
| 5:05 | story-rung | Machines do the same with a huge key; a chatbot trips on one word changed. |
| 5:50 | misconception-defuse | The wolf-or-husky photos: the system had learned snow. |
| 6:30 | generalize | The trap: any rewarded measure finds the cheapest route; check the benchmark. |
| 7:10 | caveat | A passing score is evidence, not proof; this does not mean the systems are useless. |
| 7:50 | generalize | Schools and companies: when a measure becomes a target it stops being a good measure. |
| 8:25 | viewer-turn | Rhetorical check: would it still do well if the questions looked different? |
| 8:45 | callback | Return to the opening: AI doesn't know anything. It just passes tests. |

## Narration

<<<NARRATION
AI doesn't know anything. It just passes tests.

That sounds like an insult, and a lazy one, I'll admit. But it is also the most accurate short description of how these systems get built, and once you see it, a lot of their strange behavior stops being strange at all.

So what is a test, really? A test is a pile of questions with known answers, and a score is the number of them you get right. The score is the only thing the test cares about. It doesn't care how you arrived at the answers, or whether you would get them again tomorrow in a different room with a different proctor. It only counts.

Now build a machine for one job, which is to get a high score. Somebody hands it a huge pile of examples, each with the right answer attached, and tells it to get as many of them right as it can. The machine starts out terrible, which is fine, because the process is designed for that. It makes a small change, checks the score, and keeps the change if the score went up. Then it does it again, and again, millions of times, with billions of tiny adjustments that are meaningless on their own.

Here is a toy version of that. I'll use a machine whose only job is to sort pictures into two piles, cats and dogs. It has a handful of dials, and each dial controls how much the machine pays attention to one feature of a picture. Turn one dial and the machine leans toward cat when it sees pointy ears. Turn another and it leans toward dog when it sees a wet nose. Nobody tells it which dial does what, and nobody explains what a cat is. There is no lecture and no glossary, just a score and a rule that says make the number bigger.

At the start the dials are random, so the piles are a mess. You show it a picture and it guesses. You tell it whether the guess was right, and it nudges a few dials. You show it another picture, and it nudges again. After a while the piles look sorted, and it gets 70 percent right, then 90, then almost everything. Everybody in the room claps, and I think they are entitled to.

But look carefully at what actually happened. The machine never learned what a cat is. It never learned that cats are animals, or that they sleep on keyboards, or that they ignore you when you call their name. It learned which dial settings produce the right pile for the pictures on the test. Those are two very different things, and the score on its own can't tell them apart.

The easier way to see the difference is through school. You are studying for a history exam, and somebody hands you last year's exam with the answer key attached. You memorize the key. On the practice test you score perfectly, and everyone is impressed. Did you learn history? Maybe you did, but maybe you only learned the key. The only real way to find out is to give you a new exam, with questions you have never seen. If you fall apart, you learned the key, not the subject.

Machines have the same problem, except their answer key is enormous and they are extremely good at spotting patterns in it. A model trained on a giant pile of examples can look brilliant on the examples it was trained on. Then you hand it something slightly different, and it falls over. You have probably seen this yourself. A chatbot nails a question, and then trips on the very same question once a single word is changed.

Researchers built a system to tell wolves from huskies. It was very accurate on its test photos, and for a while everyone was happy with it. Then somebody checked what it was actually looking at, and the answer was embarrassing. A lot of the wolf photos had snow in the background. The system had learned snow. Snow meant wolf, so a husky standing in the snow got called a wolf, and a wolf standing on green grass got called a husky.

Nothing about this is a bug in the usual sense. The machine did exactly what it was asked to do, which was to get a high score. The problem is that the score measured something a little different from what we wanted. The test was about photos, but we wanted the machine to be about animals. Those are not the same test, and the machine passed the one it was given. The researchers were not fools, and I suspect most of us would have made the same mistake, because the number looked wonderful.

This is the trap. Whenever you measure something and reward a machine for scoring well on it, the machine will find the cheapest way to score well. Sometimes the cheapest way is actual understanding, though often it is a shortcut. Snow is a shortcut. A watermark in the corner of an image is a shortcut. A question that showed up in the training text is a shortcut too, the same as a leaked answer key, and it is the most common one of all.

So when someone tells you a model got 95 percent on a benchmark, the first thing to ask is what that benchmark actually tests. Was it the same kind of problem you care about? Could the machine have seen those exact questions before, somewhere in its training? Did they all come from the same website, in the same style, in the same year? If the answer to any of those is yes, the number is telling you less than it seems to.

Now, this isn't only about pictures. Language models are trained on enormous amounts of text, and they are scored on whether they predict the next word or answer a question correctly. If the test questions were sitting in the training text, the model has seen the key already. If the questions are phrased in a familiar way, the model may match the phrasing without matching the idea underneath. It is the same trap, just with a bigger pile.

I want to be careful here, because it is easy to overshoot. None of this means these systems are useless, and I would not want you to walk away thinking that. They can be very good at real tasks. A student who memorized the key might still grow into a good doctor, but only if the memorizing was backed by real practice with real patients. So the question isn't whether a system works. The question is whether it works for the reason you think it does.

And that is where the honest answer gets uncomfortable. We do not have a clean way to look inside a system and say, yes, this one understands. What we have is a score, plus a set of checks on whether the score means what we hope it means. The best check is a brand new test, one the machine has never seen, ideally written by someone who is actively trying to break it.

This problem is not special to machines, which is part of why it's worth caring about. Any field that runs on tests has it. Schools have it, where students learn to pass the exam instead of learning the subject, and eventually the exam quietly becomes the subject. Companies have it too, where a team gets a bonus for hitting a number, the number goes up, and the product gets worse. Economists have a name for this. When a measure becomes a target, it stops being a good measure.

So the lesson here isn't that AI is fake. The lesson is that a passing score is evidence, not proof. It tells you the machine is good at the test. Whether that means it is good at the thing you actually care about depends on how close the test sits to the real job, and some tests sit very close while others are an answer key with a nicer name.

Next time a headline says a machine beat a human, try this. Ask whether it would still do well if the questions looked a little different. If nobody checked, then you simply don't know yet. If it falls apart when you rephrase the question, then you have learned something real about the machine, and it is not what the headline suggested.

That is also why the ordinary test of "does it answer correctly" is weaker than it sounds. Ask it harder versions of the question. Ask it the same thing in a different costume. Ask it something with no answer sitting anywhere in the training text. A system that understands should handle those with some grace, while a system that is only passing tests will show you the seams.

So, back to the start. AI doesn't know anything. It just passes tests. It is very good at passing tests, and some of those tests are close enough to real life that passing them is genuinely useful. But the thing to keep asking is whether the test is the real thing, or just the answer key in a nicer costume.
NARRATION>>>

## Slots

```json
{
 "format_class": "premise-claim explainer, answer stated, toy-world then test-trap",
 "answer_given_upfront": true,
 "hook_type": "premise-claim",
 "first_question_frac": 0.12,
 "first_concrete_object_frac": 0.07,
 "first_new_idea_frac": 0.04,
 "first_notation_frac": null,
 "payoff_frac": 0.88,
 "misconception": "planted-myth-defused",
 "brute_force_first": false,
 "examples_count": 3,
 "example_growth": "toy sorter, then history exam, then wolf photos",
 "roadmap": "none",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.6,
 "caveat_type": "epistemic",
 "recurring_anchor": "the answer key",
 "sponsor_frac": null,
 "ending_type": "phrase-mirror",
 "teaser": false,
 "wpm": 181,
 "median_beat_s": 40,
 "beat_sequence": ["hook","answer-statement","definition","toy-world","demo-sim","wall","analogy","story-rung","misconception-defuse","generalize","caveat","generalize","viewer-turn","callback"],
 "top5_moves": ["analogy","toy-world","failure-shown","generalize-to-other-domains","callback-to-hook"],
 "absent3_moves": ["brute-force-first","inline-quiz","teaser-next"]
}
```

```json
{"verified_trace": {"wpm": "PASS 181.00 (target 150.41-192.54, median 180.67)", "you_rate": "PASS 2.20 (target 1.26-3.06, median 1.7)", "i_rate": "PASS 0.39 (target 0.12-1.61, median 0.45)", "we_rate": "PASS 0.39 (target 0.28-0.77, median 0.54)", "num_rate": "PASS 0.97 (target 0.81-1.26, median 1.05)", "hedge_rate": "PASS 0.26 (target 0.15-0.35, median 0.25)", "example_rate": "PASS 0.00 (target 0.0-0.08, median 0.07)", "q_rate": "PASS 0.32 (target 0.14-1.02, median 0.5)", "sent_len": "PASS 14.46 (target 12.88-17.3, median 15.57)", "switch_sponsor": "PASS detected=False default=OFF", "switch_teaser": "PASS detected=False default=OFF", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (premise-claim vs premise-claim)", "ending_type": "MATCHES default (phrase-mirror vs phrase-mirror)", "summary": "9/9 numeric targets pass"}}
```
