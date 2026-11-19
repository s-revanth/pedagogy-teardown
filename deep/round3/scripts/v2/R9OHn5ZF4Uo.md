# CGPGrey | R9OHn5ZF4Uo | AI Doesn't Know Anything. It Just Passes Tests.

- channel: CGPGrey
- id: R9OHn5ZF4Uo
- title: AI Doesn't Know Anything. It Just Passes Tests.
- duration: 534 s (8:54)
- condition: v2
- recall: none (title and channel style only; no content recalled)
- rulebook step 0: duration band under 10 min; standalone explainer (no series label, not first person); answer stated in title (thesis); open question (what "knowing" means); topic type AI/ML claim
- class chosen: thesis essay, answer stated, one anchor (last year's answer key)
- exemplars read: deep/compact/qMkYlIA7mgw.txt (4.7 min, claim-first, closest format); deep/compact/oAHbLRjF0vo.txt (8.4 min, closest length)

## Content skeleton
- The thesis: a trained system is rewarded for matching expected outputs, so a high score is weak evidence of understanding.
- Anchor analogy: a student who memorized last year's answer key scores perfectly and freezes on a reworded question.
- Concession first: the trained settings do capture real structure, so "knows" holds in a narrow sense.
- The use-sense of knowing: answering unseen questions, adapting to rewording, noticing when stuck.
- Benchmarks as the answer key: fixed questions leak into training; rewording and changed numbers break the match.
- Three tests of strong evidence: unseen questions, many rewordings, and a reasoning check that the reasoning drives the answer.
- Human experts also pattern-match; the difference is noticing the edge. Close on the phrase.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Thesis stated plainly, with the admission that it sounds rude |
| 0:14 | answer-statement | The claim made precise: passing a test is not knowing the subject |
| 0:40 | analogy | The student with last year's answer key, on screen as a stapled exam |
| 1:05 | definition | Training as turning billions of settings until outputs match examples |
| 1:35 | definition | What training rewards: matching, not building a model |
| 2:05 | caveat | Concession: the settings pick up real structure; narrow "knows" holds |
| 2:40 | definition | The use-sense of knowing, contrasted with the lookup |
| 3:10 | story-rung | The student a week later: same subject, mountain question |
| 3:45 | generalize | Benchmarks as the answer key; leaked questions in training data |
| 4:20 | story-rung | Scores drop on rewording, changed numbers, shuffled choices |
| 3:35 | viewer-turn | Pause and guess: does a system pass a test nobody has seen? |
| 5:20 | analogy | Answer: it passes some, and failures cluster off the familiar pattern |
| 5:50 | story-rung | Train problem with changed speed and distance |
| 6:20 | caveat | Professional exam pass, with the asterisk of public practice material |
| 6:50 | caveat | Explanations are text too; test whether changing a step moves the answer |
| 7:20 | caveat | Autocomplete counter-argument, and why it does not settle the question |
| 7:45 | payoff | Three tests of strong evidence: unseen, reworded, reasoning check |
| 8:15 | generalize | Human experts and pattern recognition; the difference is noticing the edge |
| 8:35 | payoff | Practical risk: quiet failure on the cases nobody keyed |
| 8:50 | coda | The three plain questions, and the closing phrase mirrored |

## Narration
<<<NARRATION
AI doesn't know anything. It just passes tests. That's the claim, and I know how it sounds, so let me say exactly what I mean, and exactly what I don't.

Start with a student. Somewhere, a student gets hold of last year's exam, with the answer key stapled to the back. They study the key. They learn which answer goes with which question. Then they sit the test and score perfectly.

Did they learn the subject? Well, they learned the key. The score tells you they can match questions to answers. It doesn't tell you they understand why those answers are right.

Keep that student in mind, because the whole argument hangs on them.

A trained AI system works a bit like this. Nobody hands it a textbook and says, memorize this. Instead, it gets shown an enormous number of examples, and each time its internal settings get nudged, so its output moves closer to the expected output. There are billions of these settings. Training is the process of turning them until the answers line up.

So what is that process rewarding? Matching. Producing the expected output for a given input, over and over, across everything it sees. Nothing in the process says, build a model of the subject and check your reasoning against it. The pressure points toward matching, and these systems get very good at matching.

Now, I want to be fair, because this is where people get annoyed. Those settings probably don't end up random. They pick up real structure. A system that had learned nothing would fail badly, and these systems do not fail badly on everything. Something is being stored. So if by know you mean it has stored regularities that let it give useful answers, then yes, in that narrow sense it knows something.

But that isn't what people usually mean. When we say a person knows a subject, we mean they can use it. They can answer a question they've never seen. They notice when a question has changed in some small way, and they adjust. They can tell when they're stuck.

That's the test that matters, and it's exactly where the student falls apart.

Take the same student, a week after the exam. The teacher asks the old question, what's the boiling point of water at sea level. Easy. Then the teacher asks what happens to that boiling point if you carry the pot up a mountain. Same subject. Different wording. Different reasoning. The student probably freezes or answers confidently with the number from the key, because they only ever learned the lookup.

Here's the uncomfortable part. This isn't a thought experiment about one student. It's the core problem with how we measure these systems.

Benchmarks are how AI gets measured. A benchmark is a fixed set of questions with known answers. The system answers them, gets a score, and the score ends up in a headline. A high score sounds like understanding. But a fixed set has a built-in problem. Once the questions and answers are published, they spread across the internet, and some of that text ends up in the material used for training. So the system may have seen the answer key before it sat the exam.

When that happens, the score is partly measuring recall. And the evidence says so. Researchers have repeatedly found that scores drop when the same questions are reworded, when the numbers in a math problem are changed, or when the answer choices are shuffled. A system that looked brilliant on the original wording stumbles on a version a careful child would handle without fuss.

That's a useful clue, and maybe the most useful one. If it understood the subject, rewording shouldn't matter much. If it's matching patterns, rewording is exactly what breaks the match.

Pause here and make a guess. Give a system a test that nobody has ever seen, written after its training ended. Does it pass? Make your call, because the next part answers it.

Okay. Here's the usual result. It passes some of them and fails others, and the failures aren't random. They cluster where the question departs from the familiar pattern. That's what you'd predict if matching is the main engine, and understanding is, at most, a partial helper.

Let's make it concrete with a word problem about a train. Keep the story identical, change the speed and the distance, and ask again. A person just redoes the arithmetic. A pattern-matcher may hand back the number it associated with the original story, because the surface looks familiar. Sometimes the system notices and adapts. Sometimes it doesn't. The key word is sometimes. Getting it right sometimes is not the same as knowing it reliably.

Now somebody always says, but it passed a professional exam. Fair. That's a real result, if the exam was genuinely new to it. The question is whether it was. A professional exam has been around for years. Its questions have been discussed, practiced, copied into study guides, and summarized online. That's a lot of key floating around. So a pass on an old exam is a result, but it's a result with a very large asterisk.

The fair version is a new exam, written after training ended, graded blind, under the same time limit a human got. Those conditions are hard to arrange. Companies don't always arrange them, and when the conditions aren't stated, the score is hard to interpret.

Then there's the explanation. A common pitch is that the system shows its reasoning. Explanations are also text, and they come out of the same matching process. A written explanation can be a polished story about an answer that came from somewhere else. The check is simple. Change a step in the explanation and see whether the answer changes. If it doesn't, the explanation was an add-on.

Now, there's a version of this argument that goes too far. Some people say these systems are just autocomplete, full stop, and that ends the discussion. I don't think that's fair either. Autocomplete describes how the output gets produced, one piece at a time. It doesn't tell you what the settings have built along the way. Whether that counts as understanding is a real question about what understanding is, and philosophers have been arguing about it for a long time. A headline doesn't settle it.

So I'm not claiming the system is empty. I'm claiming something narrower. A good score on a fixed test is weak evidence of understanding, because training pushed hard toward matching that exact kind of answer.

What would strong evidence look like? Three things. First, questions written after training finished, so there was no chance to memorize them. Second, the same question asked in many rewordings, with the correct answer holding across all of them. Third, a look at the reasoning, and a check that the reasoning actually drives the answer. If you change one step and the final answer doesn't move, the reasoning was decoration.

Each of those is harder to do than running a benchmark. That's why they're rarer, and why the benchmark keeps winning the headlines.

It's also the same problem with students. We don't trust a student because they can recite the textbook. We trust them when they solve the problem the textbook didn't contain. A teacher who only ever gives last year's exam is measuring the answer key, not the student.

I want to be careful, because humans are pattern-matchers too. Chess masters recognize positions they've seen before. Doctors recognize a presentation from years of cases. Pattern recognition is a big part of expertise, not the opposite of it. The difference is what happens at the edge. A good expert notices when a case doesn't fit the pattern, slows down, and says so. The question for these systems is whether the recognition breaks down quietly when the situation changes, and whether anything notices.

So the honest version is this. These systems may be doing something real, and that something may be very useful, and it may still fail in exactly the places where the answer key runs out. Both can be true at once. The people selling the systems would like you to hear only the first half.

Let's go back to the phrase. It doesn't know anything, it just passes tests. I'm not saying tests are meaningless. Tests are how we find out anything about anyone. I'm saying that passing a test tells you less than the sentence makes it sound, and the cases that matter are the ones the answer key didn't cover.

Here's the practical part. If you deploy a system that only passes tests, it works well on the questions it has seen, and it fails quietly on the ones it hasn't. Nobody writes a key for those, so nobody sees the failure until it matters. That's the risk the score hides.

So the next time a headline says a system beat people on some exam, ask a few plain questions. Was that exam ever public? Could its answers have ended up in the training material? And if you reword the questions, does the score hold?

If it holds, that's interesting, and worth a closer look. If it collapses, you've found the answer key.

The student who memorized last year's exam did well on last year's exam. Whether they can handle this year's, with new questions, is the thing the score never told us. With these systems, that's the question to keep asking. It just passes tests. Whether that's the same as knowing is something a test score can't answer by itself.
NARRATION>>>

## Slots

```json
{
 "format_class": "thesis essay, answer stated in title, one anchor (last year's answer key)",
 "answer_given_upfront": true,
 "hook_type": "answer-stated",
 "first_question_frac": 0.08,
 "first_concrete_object_frac": 0.08,
 "first_new_idea_frac": 0.12,
 "first_notation_frac": null,
 "payoff_frac": 0.93,
 "misconception": "none",
 "brute_force_first": false,
 "examples_count": 4,
 "example_growth": "answer key -> reworded question -> leaked benchmark -> changed numbers",
 "roadmap": "none",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.4,
 "caveat_type": "epistemic",
 "recurring_anchor": "last year's answer key (student, then benchmark), reused 5 times",
 "sponsor_frac": null,
 "ending_type": "phrase-mirror",
 "teaser": false,
 "wpm": 185,
 "median_beat_s": 25,
 "beat_sequence": ["hook","answer-statement","analogy","definition","caveat","story-rung","generalize","viewer-turn","analogy","caveat","payoff","coda"],
 "top5_moves": ["analogy","honest-caveat","visible-repetition","generalize-to-other-domains","minimal-definition-then-refine"],
 "absent3_moves": ["act-it-out","callback-to-hook","roadmap"]
}
```

## Rule trace (v2)

```json
{"rule_trace": {
 "U1": "applied: duration under 10 min; format gate on (no roadmap, recap, callback or notation; beats 20-30 s)",
 "U2": "applied: thesis stated in title and at 0:14; no brute-force numerics, no wall, no staged misconception",
 "U3": "applied: final 10% uses a phrase mirror; hook callback n/a because the hook question is closed; no teaser",
 "U4": "applied: the answer key is reused 5 times, each pass adding a layer (student, mountain, benchmark, train, rewording)",
 "U5": "n/a: no symbols or formulas; the only numbers are sample figures in prose",
 "U6": "applied: 185 wpm, inside the under-10 band",
 "U7": "applied: no roadmap, no vote or commit in the hook; the only viewer turn sits at 50%; no planted misconception",
 "U8": "applied: epistemic caveat per open question (what knowing means) and inline concessions for the thesis",
 "U9": "applied: one pause-or-guess at 3:35 (about 0.40, inside 40-65%), answered within 30 s",
 "U10": "n/a: one thesis with concessions inline, no escalating ladder of named rungs",
 "U11": "n/a: title names no application, trigger event or end state",
 "C1": "applied: thesis carried by the title; claim stated in 14 s; through-line analogy (answer key) by 0:40",
 "C2": "n/a: no surely-X-is-safe ladder in this claim",
 "C3": "n/a: no familiar intuition that is right in this case to reverse",
 "C4": "applied: two parses of know (narrow regularities vs usable understanding), worst case is the answer key",
 "C5": "applied: beats 20-30 s at 185 wpm, short spoken lists in place of bracketed asides",
 "D1": "applied: hook is a plain thesis, not a situation, paradox or second-person setup",
 "D2": "n/a: thesis stated in title; no expected belief staged for a flip",
 "D3": "n/a: no invented model of 2-5 rules",
 "D4": "n/a: no toy world; the student is an analogy, not a staged setup",
 "D5": "n/a: no fake ending; claims are asserted with inline caveats",
 "D6": "n/a: hook question closed and no teaser, so no callback",
 "N1": "applied: measured 179 (band 177-207, median 192)",
 "N2": "n/a: under-10 band used",
 "N3": "applied: measured 0.88 (band 0.65-2.43, median 1.27)",
 "N4": "applied: measured 0.69 (band 0.0-1.52, median 0.27)",
 "N5": "applied: measured 0.56 (band 0.13-0.57, median 0.34)",
 "N6": "broken: measured 0.13 outside band 1.04-2.37 (median 1.45)",
 "N7": "applied: measured 0.44 (band 0.23-0.73, median 0.41)",
 "N8": "broken: mean 10.8 words per sentence, below band 13-20 (median 17)",
 "N9": "applied: measured 0.19 (band 0.13-0.43, median 0.24)",
 "N10": "applied: measured 0.0 (band 0.0-0.1, median 0.0)",
 "B1": "applied: no sponsor read (default off)",
 "B2": "applied: no teaser (default off)",
 "B3": "applied: no spoken roadmap (default off)",
 "B4": "applied: no recap pass in the last 20%; one restatement line only (default off)"
}}
```
