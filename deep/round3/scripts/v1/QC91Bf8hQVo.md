# PrimerBlobs: Coin Flip Cheaters: A game from Primer

- channel: PrimerBlobs
- id: QC91Bf8hQVo
- title: Coin Flip Cheaters: A game from Primer
- duration: 348 s (5:48)
- condition: v1
- recall: none

## Content skeleton
- Opens on a game: two players log one hundred coin flips each, and one of them is faking the record.
- Sets up the trap: a fair-looking total (fifty heads each) cannot separate the players, because a careful cheater matches the average.
- Viewer picks a test in a pause; the number of runs (streaks and switches) is the test that exposes the cheater.
- Derives an expected run count for fair flips and sets two-sided cutoffs at a five percent false-accusation rate.
- Checks the cutoff with ten thousand simulated fair players, then names the cost of the choice and the fair-coin assumption.
- Ends with an invitation for the viewer to design a different test and check its false-accusation rate.

## Beat sheet

| Time | Beat type | What is said or shown |
|---|---|---|
| 0:00 | hook | Question: two players flip a coin a hundred times and one cheats; can you tell which from the logs? |
| 0:25 | roadmap | One line: set a test, run it on the logs, then check the test itself. |
| 0:50 | definition | A fair coin: each flip is heads or tails at equal chance, with no memory of earlier flips. |
| 1:30 | toy-world | Two logs of one hundred flips each, written in the same format, so the file does not reveal who is who. |
| 2:05 | brute-force | First test: count heads. Both players have fifty; the total cannot separate them. |
| 2:45 | misconception-defuse | Matching the average is the trap; a careful cheater matches the total on purpose. |
| 3:15 | viewer-turn | Pause: which test would you use, longest streak, switches, or first half against second? |
| 3:45 | demo-sim | Count runs: one player switches far too often for a fair coin; the cheater shows up. |
| 4:30 | derivation | Expected runs in a hundred fair flips is about fifty; a cutoff on each side sets the false-accusation rate. |
| 5:00 | demo-sim | Ten thousand simulated fair players: about five percent are accused under these cutoffs, as set. |
| 5:20 | caveat | Five percent is a choice; the test assumes the honest coin is really fair. |
| 5:40 | advice | Try another test on the two logs and check its false-accusation rate before trusting it. |

<<<NARRATION
Two players sit down to a game of coin flips. Each flips a coin one hundred times and writes down heads or tails for every flip. One of them is cheating. The cheater doesn't flip the coin at all. They write down a sequence that looks random. The question is whether you can tell which player is cheating from the two records alone.

Here's the plan. I'll set up a test, run it on the two logs, and then check the test itself, because a test you haven't checked can fool you as easily as a cheater can.

Let's start with what a fair coin does. Each flip has the same chance of heads or tails, and no flip depends on the one before it. That second part matters. A fair coin has no memory. Its results come in streaks by chance, and those streaks are part of what randomness looks like.

Here are the two logs. Each is one hundred flips long. Both players wrote the same kind of record, so the file doesn't tell you who is who. There's no name on either log and no timestamp, only a list of heads and tails in order. You have to pick a test.

The first test most people reach for is the simplest one: count the heads. Fair coins give about fifty heads in a hundred flips. So let's count. Player A has fifty heads. Player B has fifty heads too. That tells you nothing. A cheater who knows the rule will match the total, and this test cannot separate them.

This is the trap, and it's the reason I built the game. Matching the average is the first thing a careful cheater does. If you rely on the average, you lose. The test has to look at something the cheater didn't think to fake.

Think of it as a problem the cheater is solving. The goal is to make the record look like the coin. The total is the easy part, and the cheater has already solved it. The harder part is the order of the flips. A person writing a sequence by hand almost never reproduces the right amount of streakiness, and that is where the test should look.

So pause here. Which test would you use instead? You could look at the longest run of heads. You could count how often the coin switches from heads to tails. You could compare the first half of the log with the second. Pick the one you'd trust most, and think about why. Pause the video.

Welcome back. The test I want to try is the number of runs. A run is an unbroken stretch of the same outcome. A fair coin produces a predictable number of runs in a hundred flips. A cheater who tries to look random usually overcorrects and switches too often, because they keep alternating to seem unpredictable. Or they fall into long streaks without meaning to, and produce too few switches. Either way, the count of runs gives them away, even when the total heads looks perfect.

Let's run it on both logs. Player A has around fifty runs. Player B has around seventy. Player B alternates far too often for a fair coin. That's the cheater. The total heads didn't show it. The runs did.

Now, how sure can you be? Here's where I'll derive a number. For a fair coin, the expected number of runs in a hundred flips is about fifty. The count also varies from one fair sequence to the next, and it follows a predictable spread. So you set a cutoff on each side, because a streaky cheater falls below the lower one. Anything beyond either cutoff is an accusation. The cutoffs decide how often you wrongly accuse an honest player. I picked five percent, which means a fair player gets accused about one time in twenty.

Let's check that claim rather than trust the algebra. I'll simulate ten thousand fair players, each flipping a hundred times, and count how many get accused under these cutoffs. About five percent of them do. That's the false accusation rate, and it's what I set in advance. The test does what I claimed.

Here's the honest part. Five percent is a choice, not a law. If you want to be safer about accusing honest players, set the cutoffs wider. Then you'll catch fewer cheaters, especially the ones who cheat only a little. There's no setting that catches every cheater while never accusing an honest one. The tradeoff is built into the test.

It also matters what the test assumes. It assumes the honest player really is a fair coin. If the coin itself is biased, the honest player's run count shifts, and the cutoffs are wrong. So the test is only as good as the assumption that honest flips are fair. A cheater who also biases the coin can slip past it.

So here's the outcome. The total count fails, because the cheater matched it. The run count succeeds, because the cheater couldn't fake the streak structure of a fair coin. And the five percent cutoff gives you a specific, checkable promise about how often an honest player is wrongly accused.

The game is built so that both logs look equally fair on the first test. That is exactly what makes the second test necessary, and it's the lesson I'd most like you to take away.

Now it's your turn. Take the two logs. Choose a different test, perhaps the longest streak, or the first half against the second. Check it against ten thousand simulated fair players, and see how often it falsely accuses an honest player. Then decide whether your test can catch a cheater who knows about your test.
NARRATION>>>

```json
{
 "format_class": "trap set, viewer picks the test, sim checks the test",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.0,
 "first_concrete_object_frac": 0.0,
 "first_new_idea_frac": 0.14,
 "first_notation_frac": null,
 "payoff_frac": 0.86,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "heads total, run count, ten thousand fair players",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.56,
 "caveat_type": "approximation",
 "recurring_anchor": "the same two one-hundred-flip logs, reused for every test",
 "sponsor_frac": null,
 "ending_type": "applied-game",
 "teaser": false,
 "wpm": 170,
 "median_beat_s": 30,
 "beat_sequence": ["hook","roadmap","definition","toy-world","brute-force","misconception-defuse","viewer-turn","demo-sim","derivation","demo-sim","caveat","advice"],
 "top5_moves": ["design-it-yourself","hook-question","brute-force-first","simulation-as-argument","honest-caveat"],
 "absent3_moves": ["humor","story","running-character"]
}
```
