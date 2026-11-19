# Blind script: How I deceived myself

**Channel:** PrimerBlobs
**Title:** How I deceived myself
**Target duration:** 511 s (8:31)
**Recall risk:** vague. I recognize the title as a Primer upload but do not know its content. The subject below (a confession about fooling himself with simulation results, via peeking and cherry-picking) is a guess built from the report's presenter-was-wrong, planted-error and honesty moves, not a memory. If the real video is about something else (for example a coding bug), expect the subject to miss while the structure may still hold.

## 1. Predicted beat sheet

| Time | Lvl | Moves | Narrator says / does | On screen |
|---|---|---|---|---|
| 0:00 | H | hook-paradox, story, honest-caveat | Confession: I believed a result about my own blobs, was sure of it, and it was false. How a careful person fools himself with a simulation. | Two blob colors, a bold claim label "Red is better" |
| 0:35 | H | toy-world, rule-list | The setup: red and blue blobs compete for food; both identical in rules. Rules: same speed, same food, same chance. | Arena, 10 red and 10 blue, rule panel |
| 1:10 | N | commit-to-answer, inline-quiz | Predict: if they are identical, who wins one run? (Someone always wins.) Pause. | Two outcome buttons: red wins / blue wins / tie |
| 1:45 | N | simulation-as-argument, presenter-was-wrong | Run 5 times; red wins 4 of 5. Presenter felt a rush of "there is an effect", began to theorize why. | Five small runs, tally 4-1, a thought bubble listing reasons |
| 2:50 | N | dignify-dismiss, honest-caveat | The reasons sounded good. Any pattern gets a story. Note: the blobs were identical by construction. | Strike-through on the theory bubbles |
| 3:30 | N | brute-force-first, visible-repetition | Run 100 batches of 5 runs; in how many batches does red win at least 4? About 19%. Pure luck regularly produces a "finding". | Grid of 100 batch tallies, highlighted cells |
| 4:40 | N | misconception-first, failure-shown | The second trick: stopping when ahead. Track a running tally; stop when red leads by 2. Almost always possible. | Race line chart wandering, stop marker |
| 5:40 | I | notation-after-concept | Name it: a coin-flip walk; "chance of seeing this by luck" as a number (p-value) offered as a patch for the visible failure, hand-wavy. | Small table: "luck produces this X% of the time" |
| 6:20 | N | planted-error / design-it-yourself | Design the test: decide the number of runs before starting; write it down. Viewer asked what rule they would set. | Checklist builder, viewer picks N |
| 7:00 | N | build-and-verify, honest-caveat | Rerun with the rule: 200 runs, red wins 51%. Disclosed: even this has a choice (200 was arbitrary). | Fixed-N run, 51/49 bar |
| 7:40 | B | recap, scope-the-claim | Summary: stories come free, noise looks like signal, decide before you look. Broader: this applies to every sim in my previous videos too. | Recap card; callback to opening claim |
| 8:10 | N | callback-to-hook, teaser-next, admin | Callback: the red-is-better claim in the opening; Patreon and teaser. | End card |

## 2. Full narration script

I want to tell you about the time I fooled myself. Not by lying to anyone. By running a simulation, looking at the result, and honestly believing something that was not true. And the part I find uncomfortable is how reasonable it felt.

Here is the setup, and I will make it as simple as I can. There are red blobs and there are blue blobs. They live in the same arena, they compete for the same food, and every blob follows exactly the same rules. Same speed. Same chance of finding food. Same chance of reproducing. The only difference is the color, and the color does nothing at all. Red and blue are, by construction, identical.

So here is my question for you. If I run this competition and let one color take over, who wins? Think about that for a second. If you said that it is a coin flip, you are right, and hold on to that thought, because I am going to ignore it myself in about thirty seconds. Pause if you want, and commit to an answer before I run anything.

All right, the first run. The blobs eat, reproduce, and in the end blue is wiped out. Red wins. Run two: red wins again. Run three: blue wins. Run four: red. Run five: red. So red wins four out of five.

And here is what happened in my head. I felt a small rush. Red wins so often. Maybe red blobs are slightly better, somehow. Maybe because they start on the left and the food spawns closer. Maybe the order in which I place them matters. I came up with three reasons in about a minute, and every one sounded good. And that is the first problem I want to point out: it is never hard to find a story. The story is not evidence. The blobs are identical, I wrote the rules, and I still talked myself into an effect.

Let me be honest about how that feels from the inside. It did not feel like deceiving myself. It felt like noticing something. That is why it is dangerous.

There is one more thing I did that I am less proud of. After those five runs, I kept the setup that gave me red wins, and tweaked a rule to see whether the effect got bigger. It did, for a while. That is a third way to fool yourself: you try variations until one agrees with you, and you only remember the one that did. If I tried ten tweaks on identical blobs, one of them would show an effect by luck alone, and I would report that one. So how often does pure luck do this? Let me test it directly. Instead of five runs, let me do five runs a hundred times. Each little square here is one batch of five runs, and I will color it when red wins at least four of the five. Watching them fill in: about one batch in five is colored. About nineteen percent. That means if I had run my five runs and found four reds, I should not have been surprised. Almost one time in five, identical blobs produce a result that looks like a discovery. And I should say what I did not do. I did not fake anything. Every run was real, the code was correct, and each number on the screen was honest. The deception was all in what I chose to look at and when I chose to stop looking.

Here is the second way I fooled myself, and it is sneakier. I was watching the running tally. Red ahead, blue ahead, red ahead. At some point red was ahead by two wins, and I thought, that is plenty, I have seen enough. Here is the issue. If I decide when to stop by looking at the tally, I am choosing the moment when luck is on my side. Look at this chart. It tracks the lead as the runs go on. It wanders. It crosses zero. It goes up. It goes down. And in almost every case, at some moment, red is ahead by two. Stop there, and you have a result. Keep going, and it vanishes. Let me run the chart a few more times so you can see it is not a fluke of one run. Each line wanders on its own, and a good fraction of them cross the line where red is ahead by two. If I am allowed to pick my own stopping point, I can almost always find a moment that supports me.

I want to name this honestly, with a small amount of notation. People ask how likely a result is to happen by luck alone. Here it was about nineteen percent for four out of five. That chance is often called a p-value. I am not going to define it carefully, because for the point I am making all you need is the picture: how often does luck alone give me something at least this striking? The trouble is that this number only means anything if you decided how many runs to do before you looked.

So how do I stop doing this to myself? Let me ask you to design the rule. What would you set? Pause and think about it. Think about what each choice protects you from: the number of runs, the thing you are measuring, and the moment you stop. The rule that works is almost boring: decide the number of runs first, before seeing a single result, and do not change it. I pick two hundred.

Now I run all two hundred, with identical blobs, and the final tally: red wins about fifty-one percent. Which is exactly what identical blobs should do. No effect. The rule did not make the blobs different. It stopped me from picking the moment that makes it look like they were.

And I should be honest again. Two hundred is itself a choice. I picked it because it felt like enough, and there is nothing magic about it. If the real difference were tiny, two hundred runs might not show it. The rule protects me from one kind of mistake, and does not make me right in general.

Here is where I want to land. Stories are free: whatever the data shows, you can explain it. Noise looks like signal: identical blobs give discoveries one time in five. And the best defense I have found is to decide before you look. Every simulation I have shown you on this channel could have fallen for this trap. I tried to run enough, and to say when I chose numbers. But you should know the trap is there, and that I have fallen into it.

There is a version of this that is even harder to catch: when the result is something you wanted to be true. I wanted a clean story for a video. A clean story is exactly when you check less carefully. If the result had been boring, I would have rerun it without thinking twice. Remember the claim at the start, that red is better? It was never true. It was a story I told about a lucky streak, and a sample that stopped at the right moment.

Thanks to everyone who supports the channel on Patreon. Next time, we go back to the blobs and see what happens when we let them evolve. See you then.

## 3. Rule trace

| Beat | Report claim / arc step used |
|---|---|
| 0:00 hook | Arc 1 non-biology variants open on a story; honesty as connective tissue (bottom line); presenter-was-wrong 4/12 |
| 0:35 setup | toy-world 12/12; rule-list 7/12; Arc 2 baseline (identical blobs) |
| 1:10 predict | Arc 4; commit-to-answer 9/12; theory 2 (obvious-guess-is-wrong pause) |
| 1:45 runs | simulation-as-argument 11/12; presenter-was-wrong (Natural Selection 6:34) |
| 2:50 stories | New theory 4: dignify then dismiss the intuition |
| 3:30 batches | visible-repetition 8/12; Aggression 7:55 N-run batches (Green Beard 30-run frame) |
| 4:40 stop rule | theory 3: the failure names the next ingredient; planted-error (Cheater 18:54 trap) |
| 5:40 notation | Arc 6, notation-after-concept 11/12; patch-for-failure (R0 in Epidemic) |
| 6:20 design | design-it-yourself 8/12; Cheater 1:38 |
| 7:00 verify | build-and-verify 8/12; honest-caveat with "choice" labeling (Cheater: label every number a choice) |
| 7:40 recap, 8:10 end | recap 7/12; callback-to-hook 8/12; teaser-next 6/12; scope-the-claim ending |

Report claims I could not turn into a concrete choice:
- Which subject "deceived myself" is about: nothing in the report predicts it. The sim-bias topic is a guess.
- How much the presenter appears personally. The report says honesty but does not say whether Primer uses first-person narrative stories (all 12 videos are model-centered).
- Principle 12 (connect to outside): "weaker elsewhere", so I included no outside source; a real video might cite a paper.
- Principle 8 pacing: no rate data.
- Whether to use any ending other than recap plus teaser; the 6/12 teaser stat does not say when teasers appear.
- "Dense stretches near the end": no number to size how dense, so I did not model density.

## 4. Explicit predictions

- **First question time:** about 1:10 (a viewer prediction pause). A rhetorical question may come in the opening 0:30.
- **First notation/formula:** about 5:40 (p-value or a percent-by-luck table), roughly 66% into the runtime; possibly none, if the real video stays with plain percentages.
- **Misconception:** yes: "a pattern that shows up in a few runs means a real effect" (including "I saw it with my own eyes"). The presenter holds it first, as the confession.
- **Brute-force-first:** yes: repeat the whole experiment many times (batches of five runs, repeated 100 times) before any named concept.
- **Examples:** 3 to 4 that grow: 5 runs, then 100 batches of 5, then a stop-when-ahead chart, then 200 pre-decided runs.
- **Hook type:** confession or paradox ("a careful person misled by his own sim"); a story, not a quiz.
- **Ending type:** scope-the-claim recap plus a callback to the opening claim, then a short teaser and admin; ends on a limit ("this rule does not make you right").
- **Five most confident moves:** honest-caveat, presenter-was-wrong, simulation-as-argument, failure-shown, toy-world (blobs).
