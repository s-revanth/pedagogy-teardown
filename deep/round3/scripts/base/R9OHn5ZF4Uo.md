# Channel: CGPGrey
- id: R9OHn5ZF4Uo
- title: AI Doesn't Know Anything. It Just Passes Tests.
- duration: 534 s (8:54)
- condition: base
- recall: none

## Content skeleton
- Opens on the everyday experience of a chatbot answering fluently, then asks what "knowing" would mean for a person.
- Defines a test as a small, checkable stand-in for the thing we actually care about.
- Student-who-memorized-last-year's-exam analogy, then a ten-question quiz with reworded items to show the score collapsing.
- Explains how a language model is trained (predict the next piece of text, then tuned on human ratings) and how benchmarks score it.
- Generalises Goodhart's law: once a score is the target, it stops measuring the thing.
- Three failure channels: contamination (test items leaking into training), selection (versions tuned to the benchmark), and learnable test shape.
- Defuses the "it is just a lookup table" myth without overclaiming capability; proposes better checks (new items, rephrasing, checking reasoning, failure shapes).
- Closes by returning to the title and to the memorizer image.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | A chatbot answers a hard question fluently; the tempting claim that it "knows" things. |
| 0:35 | answer-statement | Short version: passing tests is not the same as knowing; the title's claim stated plainly. |
| 1:00 | roadmap | Three parts: what knowing means, how tests go wrong, what to check instead. |
| 1:20 | definition | How you judge knowledge in a person: give a case they have not seen. A test is a stand-in. |
| 2:10 | analogy | A student memorizes last year's exam and scores perfectly, but only on that exam. |
| 2:50 | toy-world | Ten-question quiz; reword the items; the score falls from ten to two. Shown on screen as a card. |
| 3:30 | demo-sim | Simple diagram of training: text in, next-piece prediction, human ratings, then a benchmark table. |
| 4:15 | generalize | Goodhart's law: when a measure becomes a target it stops being a good measure. |
| 5:00 | generalize | Three channels: contamination, selection across many versions, and a learnable test shape. |
| 6:20 | misconception-defuse | Not a lookup table; it compresses patterns and can write new sentences. Capability is real, the leap from score to knowledge is the mistake. |
| 7:00 | caveat | None of this makes the systems useless; passing hard exams still helps real work. |
| 7:40 | payoff | Better checks: unseen problems, rewording on purpose, checking the reasoning, studying the failures. |
| 8:20 | callback | Back to the memorizer and the answer key. |
| 8:45 | coda | The title restated as a summary, with the caveat attached. |
| 8:54 | coda | End. |

## Narration
<<<NARRATION
Ask a chatbot a hard question and it answers. Fluently, politely, and often with a confident tone that makes you forget there is a machine on the other end. So it is tempting to say it knows things. The honest version is less comfortable. These systems are very good at passing tests, and passing a test is not the same thing as knowing the subject.

The short version is this: a high score tells you the system did well on that test. Whether that means it knows anything in general is a separate question, and it is the one that gets skipped.

Here is how this video is going to go. First, what it would mean to know something. Second, how the tests we use to measure AI go wrong. Third, what to check instead.

Start with a person. What would it take for you to say somebody knows a subject? You cannot look inside their head. So you do the only thing you can. You give them a case they have not seen before and you watch what they do. If a student solves a new problem using the idea behind the old ones, you believe they understand the idea. If they can only reproduce the answer key, you do not.

That is the whole problem in miniature. A test is a stand-in. It is a small, checkable sample of a bigger thing we actually care about, which is being able to use the knowledge when the situation changes. For a stand-in to be useful, it has to track the real thing. When it stops tracking it, it is still a number, it is just a number that means something else.

Imagine a student who never studies the subject. Instead they get hold of last year's exam and memorize every answer. Next term they sit the same exam and score perfectly. The teacher is impressed. The score says they know the material. But it only says they know last year's exam. Change one number in this year's question and they fall apart, because there was never an idea underneath. There was only a very good memory attached to a list of answers.

Now make it smaller still. Take a quiz with ten questions. Our memorizer gets ten out of ten. Then we give the same ten questions again, with the wording shuffled and the numbers changed. The score drops to two. It did not drop because the student had bad luck on the day. It dropped because the original score was measuring the wrong thing from the very beginning.

Now bring this to AI. A large language model is trained on an enormous amount of text with one basic job: predict what comes next. That sounds like a tiny task. But doing it well across billions of sentences forces the system to pick up grammar, facts, and a great deal of structure about how the world gets described. After that, it is tuned further, often by people rating its answers, so it learns to give replies that people find useful.

To see how good it is, we give it tests. Multiple-choice exams from medicine and law. Maths problems. Coding tasks. Reading comprehension. Each one is a stand-in, exactly like our exam. The model gets a score, the score goes into a table, and the table goes into an announcement.

Here is where it goes wrong. There is a saying, usually credited to the economist Charles Goodhart, that when a measure becomes a target, it ceases to be a good measure. Once a number is the thing everybody is trying to push up, people optimise for the number. The number keeps rising, but the thing it was supposed to represent may not be rising with it.

For AI, there are at least three ways this happens.

The first is contamination. The test questions are public. They have been posted on websites, copied into forums, and quoted in articles. A model trained on a huge slice of the internet may have seen the questions, or near copies of them, during training. Seeing the answer key before the exam is the memorizer's trick, and it can happen by accident. Nobody has to cheat on purpose for it to matter.

The second is selection. Researchers build many versions of a system. The ones that score highest on a benchmark get published, and the others quietly disappear. Over a few years, everybody looking at the benchmark has tuned toward it, even if no single person meant to. The test ends up shaped by the people who take it.

The third is that tests have a shape, and the shape can be learned. Many multiple-choice questions can be answered by spotting patterns in the options, such as which answer is the longest, or which one looks like the others, without reading the question closely. A system that has learned how tests look can do well on them without knowing the subject underneath.

Now you might think this means the thing is just a glorified search engine, a lookup in an enormous database. That is not quite right, and it is worth being careful here. A language model does not store the internet as a list of facts that it pulls out on request. It squeezes patterns into numbers, and it can produce sentences it has never seen before. That is a real capability, and it is not nothing. The mistake is treating a high score as proof of the very thing the score was meant to measure. The capability and the score are two different things, and the gap between them is where the problem lives.

So what would a better test look like? It is the same test we used on the student. Give the system problems that were written after its training finished, so it cannot have seen them. Change the wording on purpose. Ask the same question three different ways and see whether the answers agree. Ask it to explain its reasoning, then check the reasoning, not only the final answer. And study the cases where it fails, because a system that really knows something tends to fail in a different shape from one that is only matching patterns.

Researchers have been doing exactly this, and it is why benchmarks keep getting replaced. A test becomes famous, scores climb, people start to suspect the questions have leaked, and a new test gets written. The cycle is useful. Each new test reveals something the last one hid. But it also tells you what a score actually is. It is a snapshot of performance on one kind of question, at one moment, using a sample that may be fresher-looking than it really is.

I want to be fair here. None of this means these systems are useless. A tool that passes a hard exam can still help a doctor draft a note, or help a programmer find a bug, and it can be checked on the job. Passing tests is a real achievement. The mistake is the leap from passing tests to knowing things in general. You can be very good at the exam and still not have learned the subject. With machines, we have more reasons than usual to check which of those two things we are looking at.

So the next time you see a headline with a score in it, ask a few plain questions. What was the test? Was it public? Were the questions new? What happens if you change one number? Those questions separate a student who learned the material from a student who memorized the answer key.

That is the short version of the title. The system does not know anything in the way a person knows something. It passes tests. Sometimes that is exactly what we asked for. The rest of the time, we need to be careful that we are not fooling ourselves about what the score means.
NARRATION>>>

## Slots
```json
{
 "format_class": "premise-claim explainer: stand-in test analogy, Goodhart generalisation, three failure channels",
 "answer_given_upfront": true,
 "hook_type": "premise-claim",
 "first_question_frac": 0.15,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.15,
 "first_notation_frac": null,
 "payoff_frac": 0.86,
 "misconception": "planted-myth-defused",
 "brute_force_first": false,
 "examples_count": 3,
 "example_growth": "one memorizing student -> ten-question quiz -> public benchmarks",
 "roadmap": "one-line",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.2,
 "caveat_type": "domain-limit",
 "recurring_anchor": "the memorized answer key (returns at 0:00, 2:10, 2:50, 8:20)",
 "sponsor_frac": null,
 "ending_type": "hook-callback",
 "teaser": false,
 "wpm": 170,
 "median_beat_s": 40,
 "beat_sequence": ["hook","answer-statement","roadmap","definition","analogy","toy-world","demo-sim","generalize","misconception-defuse","caveat","payoff","callback","coda"],
 "top5_moves": ["analogy","toy-world","generalize-to-other-domains","honest-caveat","callback-to-hook"],
 "absent3_moves": ["act-it-out","notation-compaction","inline-quiz"]
}
```
