# SebastianLague | egukLtEhyP0 | My First 10 Years of Game Development

- channel: SebastianLague
- id: egukLtEhyP0
- title: My First 10 Years of Game Development
- duration: 684 s (11:24)
- condition: v2
- recall: vague (I have at most a vague sense of a retrospective on the channel's early years; no specific content recalled)
- class (step 0): over-10 min (11:24); format = devlog retrospective (first-person title; topic type devlog); answer not stated up front; open question (why projects stall); topic = personal history of game development
- exemplars read: deep/compact/TURzbXTNaA0.txt (I Created a (terrible) Video Game Console, 9:21) read in full for first-person retrospective voice; deep/compact/PGk0rnyTa1U.txt (I Spent a Week Making a Game about Vacuuming, 17 min) read in full for the diary-style structure

## Content skeleton
- Opens on an old project folder with dozens of abandoned games; the question: why did I keep starting over?
- Classic problem with a human-scale number: about 40 unfinished folders, 9 that passed the first week.
- Ladder of named rungs: first one-screen game; first engine with a level editor; first 3D prototype at about 12 frames per second.
- Rung four: a big project abandoned at version four after about two years; the wall where one change breaks three features.
- The break: a small finished game in about a week, with a first playtest of 6 people, then 20.
- What changed: progress measured in finished things; a short scope list; a playable build by a stranger within a week.
- Advice to the earlier self, with an honest uncertainty about one recurring physics bug.
- Callback to the opening question; the old folder is still there; no wishlist, no teaser.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | An old project folder on the drive; dozens of abandoned games; the question why I kept starting over. |
| 0:40 | hook | Classic problem: most first games never get finished; about 40 unfinished folders, 9 past the first week. |
| 1:20 | story-rung | Rung one: a one-screen game with a moving block and a score; the high score kept in a plain text file that reset. |
| 2:55 | story-rung | Rung two: first engine and a level editor; about three months, a little over 2,000 lines; 14 menus and 3 undo levels. |
| 4:30 | story-rung | Rung three: first 3D prototype at about 12 frames per second; draw calls cut from 400 to 60; frame time as a budget. |
| 6:05 | story-rung | Rung four: a big project for about two years; 11 folders and 4 engines; stopped at version four; the wall where one number breaks three features. |
| 8:00 | story-rung | Break: a small finished game in about a week, about 4 minutes long; first playtest 6 people, then 20. |
| 9:20 | payoff | What changed: progress measured in finished things; a list of five or six items instead of 60 or 70. |
| 9:50 | advice | Advice to the earlier self: finish something small, make it playable by a stranger within a week, and name the smallest finished version. |
| 10:30 | caveat | Honest uncertainty: 37 attempts to fix one physics bug, and it is not clear the team ever understood why it kept coming back. |
| 10:50 | coda | Current practice: short cycles, early scope cuts, each prototype treated as a test; the old folder still gets opened. |
| 11:15 | callback | Answer to the opening question: measuring the wrong thing and stopping because the projects were too big. |

## Narration
<<<NARRATION
Let's start with an old project folder. It sits on my drive, it has dozens of subfolders, and each one is named after a game that got started and then stopped, often after only a few days. Scrolling through it, I kept coming back to one question: why did I keep starting over? This video is the long answer, a look back at roughly ten years of making games, from the first tiny project to the things we are still working on today.

Most first games never get finished, and that's the classic problem we'll open with. There are roughly forty unfinished folders in that archive, and when we went back through them, only nine got past the first week. That number is embarrassing, but it's honest, and it's a useful place to start, because the nine survivors tell us something about the other thirty-one.

The first rung is the smallest thing ever made. It was one screen, one moving block, and a score that went up whenever the block touched something. For about an afternoon it was genuinely pleasing, and I remember showing it to my family like it was a finished product. The code was a copy-and-paste mess in a single file of a few hundred lines, but it ran, and it taught a lesson that stayed with me: a game is a loop of input, update and draw, and everything else is decoration.

For example, the high score was stored in a plain text file, and it reset every time we restarted the program, which we only noticed after a friend asked where it had gone.

Let's move to the second rung, my first real engine project. This is where we started building a level editor, because the goal was to make many levels without writing each one by hand. It took about three months and a little over 2,000 lines of code. At the end we had a tool that could save and load a level, and we barely used it to make a game, which is a pattern that would repeat for years.

The editor ended up with 14 menus, 3 levels of undo, and a grid that snapped to 8 pixels, and each of those features took longer than we wanted to admit. If you have ever built a tool for yourself, you know how easy it is to spend a month on the tool and a day on the game.

The third rung was the first three-dimensional prototype. The plan was cameras, lights, and a character that could walk across a landscape. The first version ran at about 12 frames per second, which is far too slow to play, so we spent weeks measuring where the time went. The largest cost turned out to be drawing the same object again and again, and that taught us to treat frame time as a budget rather than a wish.

We spent most of one summer on that frame rate problem, which is a long time when the goal was to make something fun to play.

We cut the number of draw calls from 400 to 60 by batching the trees, and the frame rate climbed to around 30. I still think that was the most satisfying afternoon of the whole decade, mostly because the fix was small and the number moved so clearly.

The fourth rung is the one we're least proud of, and it's also the most useful. This was a large project with a huge ambition, and it absorbed around two years. We sketched systems, rewrote them, and planned features that would take a team of ten, and we stopped at version four without anything anyone could play. I don't think the project failed because of one bad decision. It failed because the scope grew faster than our ability to finish any single piece of it.

By the end we had 11 project folders, 4 separate engines, and roughly 90,000 lines of code that never shipped to anyone. We switched engines twice, and each switch cost about 6 weeks, which is the kind of number nobody likes to write down.

That brings us to the wall. The worst part was that every single fix felt small when we made it. As the code grew, a change in one system broke two others, and more time went into fixing the fallout than into adding anything new. There was one afternoon when a single number in the physics code was changed, and three unrelated features stopped working in the same minute. At that point the project wasn't really a game any more. It had become a puzzle we had built for ourselves, and the puzzle was no longer any fun to solve.

Later, when I looked through the commit history, I counted 37 separate attempts to fix the same physics bug, and I'm still not sure we ever understood why it kept coming back.

The break came when we stopped trying to build the big thing and made a small one. We wrote the new scope list in marker on a sheet of paper and pinned it next to the monitor, so it stayed in view for every session. We picked a single mechanic, built it in about a week, and cut everything else. The game was short, rough, and missing most of the features we had planned, but it was complete, and that was the first time in years we had something finished to show. Looking back, I think that matters more than almost any technical lesson from the big project.

The small game was about 4 minutes long, and it took one week to make, which felt almost like cheating after two years of work. Our first playtest had 6 people, and the second had 20, and the difference in what we learned was enormous.

Once people started playing it, the feedback taught us things the big project never could. A handful of players tried it in the first week, and they got stuck in places we hadn't tested at all. They didn't care about the systems we had been obsessing over. They cared about whether the one mechanic was fun for thirty seconds, and that turned out to be a far more useful question than anything we had been asking ourselves in the studio.

If you are in the middle of a big project right now, you might recognise some of this. I'd suggest one quick test: name the smallest finished version of the game, and check whether you could show it to someone tomorrow.

Here is what changed. Progress started being measured in finished things, not in lines of code or hours spent. A week that ended with a playable build counted as a good week, even if the build was ugly. A month that ended with three half-finished systems counted as a bad one, even when the hours were long and the work was hard. That single change in how we scored our own work did more for us than any new engine or tool we adopted along the way.

We now keep a notebook with one line per week, and each line says what shipped, even when the honest answer is nothing new. It's a dull habit, and it's the one we would keep if we could only keep one.

We also learned to keep a short list of what the game needs to be fun, and to delete anything that doesn't serve that list. The early lists were enormous, sometimes 60 or 70 items long, and almost none of those items survived to the end. A list of five or six items made each decision faster, and the finished games became far more coherent than the sprawling ones, which tried to do everything at once and ended up doing nothing well.

If I could send one message back to the person who started that first folder, it would be simple. Finish something small before starting something big, and make the finished thing playable by someone who isn't you. Those two habits would have saved years, and they would have kept more of those folders from becoming abandoned prototypes on a drive nobody opens. Honestly, I think that's the advice most beginners need to hear.

I'd add a third habit too, which is to ask a stranger to play the build within a week. That habit alone would have caught most of those 37 physics attempts, because a stranger never cares about the physics.

Our work looks different now. Projects are planned in short cycles, scope gets cut early, and each prototype is treated as a test rather than a promise. The old folder is still there, and we still open it now and then, mostly as a reminder of how many times the same lesson had to be learned. The lesson keeps getting easier to apply, even when the next idea is exciting enough to tempt us back into the same trap.

We still get excited about big ideas, and we still sketch them out on paper late at night. The difference is that the sketches now come with a date, a size, and a small first test that can fail.

So here is the answer to the question from the beginning. We kept starting over because we were measuring the wrong thing, and we kept stopping because the projects were too big to finish. Once we finished something small, starting over became cheaper, and the folders began to hold a few finished things among the unfinished ones. Thanks for watching, and I hope this helped make sense of a few folders of your own.
NARRATION>>>

## Slots
```json
{
 "format_class": "devlog retrospective: adjacent classic problem with a human-scale number, ladder of named rungs, human-pivot advice, callback close",
 "answer_given_upfront": false,
 "hook_type": "story-anecdote",
 "first_question_frac": 0.03,
 "first_concrete_object_frac": 0.01,
 "first_new_idea_frac": 0.06,
 "first_notation_frac": null,
 "payoff_frac": 0.8,
 "misconception": "none",
 "brute_force_first": false,
 "examples_count": 5,
 "example_growth": "one screen -> editor -> 3D prototype -> finished game",
 "roadmap": "none",
 "viewer_turn": "none",
 "viewer_turn_frac": null,
 "caveat_type": "historical-uncertainty",
 "recurring_anchor": "the old project folder, opened at the hook, mid-video and in the close",
 "sponsor_frac": null,
 "ending_type": "hook-callback",
 "teaser": false,
 "beat_sequence": [
  "hook",
  "story-rung",
  "story-rung",
  "story-rung",
  "story-rung",
  "story-rung",
  "payoff",
  "advice",
  "caveat",
  "coda",
  "callback"
 ],
 "top5_moves": [
  "story",
  "failure-shown",
  "honest-caveat",
  "callback-to-hook",
  "visible-repetition"
 ],
 "absent3_moves": [
  "hook-paradox",
  "commit-to-answer",
  "expert-dialogue"
 ],
 "wpm": 141,
 "median_beat_s": 40
}
```

```json
{"rule_trace": {
 "U1": "applied: devlog retrospective format gate (first-person, topic type devlog); under-10 items n/a at 11:24; roadmap and recap withheld; the ladder structure is used",
 "U2": "n/a: neither the title nor the first 40 s states an answer; the answer comes back at the close",
 "U3": "applied: hook-callback ending, since the hook question (why keep starting over) stays open until the close; no teaser (not a series)",
 "U4": "applied: the old project folder is reused at the opening, mid-video and in the close, each use adding a layer",
 "U5": "n/a: no symbols or formulas; the only numbers are counts, sizes and durations",
 "U6": "applied: about 141 wpm on 1,609 words over 11:24; beats of 40-120 s, with a rung per 60-100 s",
 "U7": "applied: no roadmap, no vote, no planted misconception; the finish-small lesson is said after the rungs, not announced at the start",
 "U8": "applied: historical-uncertainty caveat about the recurring physics bug",
 "U9": "n/a: no binary decision or absurd magnitude to pause on",
 "U10": "applied: ladder of named rungs (first game, first engine, first 3D prototype, big project, small finished game as the break); each rung about 1.5-2.5 min, and the wall sits inside the big-project rung",
 "U11": "n/a: title names a personal retrospective, not an application or end state",
 "C1": "applied: devlog retrospective format, first-person, not impersonal lecture and not designed-lesson adventure",
 "C2": "applied: each rung reruns the same loop (build, test, measure, cut) with one layer added",
 "C3": "n/a: not lecture format; no pause-the-video quiz",
 "C4": "n/a: no design source cited; the lessons come from the presenter's own projects",
 "C5": "applied: opens with an adjacent classic problem (most first games never get finished) and a human-scale number (nine of roughly forty folders passed week one)",
 "D1": "applied: failures shown as rungs (12 frames per second; one change breaking three features; the big project stopped at version four)",
 "D2": "n/a: the repairs are named by function (frame budget, scope list), not after the failure",
 "D3": "applied: one knob isolated in the frame-rate rung (draw calls batched from 400 to 60)",
 "D4": "n/a: no honest-close bundle; the close is a callback and one advice line, with no wishlist",
 "D5": "n/a: no equation",
 "N1": "n/a: under-10 band rule; this video is over-10 min",
 "N2": "applied: 141 words per minute (measured), inside p25-p75 137-158",
 "N3": "applied: 0.50 you/your per 100 words (measured), inside p25-p75 0.23-0.78",
 "N4": "applied: 1.12 I/me/my per 100 words (measured), inside p25-p75 0.94-2.81",
 "N5": "applied: 3.36 we/us/let's per 100 words (measured), inside p25-p75 2.55-5.7",
 "N6": "applied: 1.18 numbers per 100 words (measured), inside p25-p75 0.95-2.12",
 "N7": "applied: 0.06 question marks per 100 words (measured), inside p25-p75 0.0-0.09",
 "N8": "applied: 20.6 words per sentence (measured), inside p25-p75 19-25",
 "N9": "applied: 0.25 hedges per 100 words (measured), inside p25-p75 0.11-0.35",
 "N10": "applied: 0.06 example cues per 100 words (measured), inside p25-p75 0.03-0.18",
 "B1": "applied: no sponsor read",
 "B2": "n/a: not a series; U3 withholds the teaser",
 "B3": "n/a: roadmap withheld; a retrospective does not call for one",
 "B4": "applied: no spoken recap in the last 20%; the close answers the opening question and gives one piece of advice, not a list of lessons"
}}
```
