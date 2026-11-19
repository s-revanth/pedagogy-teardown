channel: SebastianLague
id: egukLtEhyP0
title: My First 10 Years of Game Development
duration: 684s (11:24)
condition: v3
recall: none
exemplars read: deep/corpus/compact/--GB9qyZJqg.txt, deep/corpus/compact/TURzbXTNaA0.txt

## Content skeleton
- Open on a personal story: an old hard drive full of game attempts, and a tiny bouncing square I once thought was exciting.
- Tell the first project: a clumsy shooter, a big single function, and a score that sometimes went negative.
- Show the turning point: rebuilding the same game from scratch and seeing how much better the second version is.
- Defuse the talent myth: repetition and finishing mattered more than natural ability.
- Describe the middle years: an abandoned project, a game jam, sharing work, and the tool trap.
- Give the honest numbers: how many projects started, and how few reached a playable state.
- Close on what changed and what I would tell my earlier self, then tease the next video.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | story-rung | Old hard drive, a folder of unfinished games, a bouncing square |
| 0:45 | story-rung | The first project: a clumsy shooter, a score that went negative |
| 1:40 | caveat | The code was a mess: one giant function and copied snippets |
| 2:30 | story-rung | Rebuilding the same game from scratch, and why version two taught more |
| 3:20 | misconception-defuse | Talent is not the main separator; finishing is |
| 4:10 | story-rung | The racing game abandoned after almost a year |
| 5:00 | derivation | Learning curve: input, rendering, then the maths of movement |
| 5:50 | demo-sim | Testing a jump in a single-platform scene, one variable at a time |
| 6:40 | tangent | Tool tinkering as a form of avoidance |
| 7:20 | story-rung | First game jam: a weekend, a theme, a deadline |
| 8:10 | story-rung | First public release and the reaction of players |
| 8:50 | generalize | Teaching and explaining work reveals the holes in your knowledge |
| 9:20 | payoff | The numbers: about 40 started, about 6 playable |
| 9:50 | coda | Patience with uncertainty as the real change over ten years |
| 10:40 | teaser | Next video: returning to one early project |

## Narration
<<<NARRATION
Last week I found a folder on an old hard drive, and it contained almost every game I had tried to make in my first few years. Most of them never got past a few hours of work. I opened one, and a tiny square was bouncing off the edges of the window. At the time I thought it was incredibly exciting. Looking at it now, we can laugh a bit, and then feel a little nostalgic. So this video is a look back at the first 10 years of making games, the mistakes I made, and the few things that actually helped. You might recognise some of those mistakes from your own early work.

I didn't start with a plan. I started because a book on programming had a chapter about drawing shapes on the screen, and I wanted to see something move. My first real project was a clumsy little shooter, where the player slid along the bottom of the screen and fired at 4 rows of blocks. I spent 3 weeks on it. The collisions were wrong, the frame rate was bad, and the score sometimes went negative. We all have a project like that, and I was proud of it anyway, because it was mine and it did something.

Looking back, I can see that the code was a mess. I had one giant function that handled input, movement, drawing and the score, and every change broke something else. I didn't understand classes in any real sense, and I certainly didn't think about separating concerns. I copied snippets from forums and changed them until they worked. We learn that way at first, and it's a fine way to start, but it's a terrible way to build anything large. I think that phase taught me more about reading code than about writing it.

The turning point came when we finished a small tutorial series and tried to rebuild the shooter from scratch. I found that doing it a second time was very different. The fragile parts were easy to spot, so I wrote them more carefully. I still remember the moment the game ran cleanly, and it was far easier to change than the first version. The second version teaches more than the first, because the traps are already known. That lesson has come back to me many times since.

Not everything gets finished, and I want to be honest about that. I worked on a racing game for almost a year. The physics kept fighting back, and I kept rewriting the car controller instead of building the track. Eventually I realised I was avoiding the part that would show whether the idea worked at all. I packed the project away and started something smaller. Abandoned projects also have a practical side. Each one leaves behind code, notes and assets, and those become a library for the next attempt. Nothing is really lost when a project stops, provided the lessons are kept. A folder of half finished work can be searched, copied and reused, and it often saves a surprising amount of time. Keeping a rough log of what went wrong is a habit that pays back for years. We can learn from abandoned projects, and that one hurt, but it taught me more than almost anything I finished that year.

There's a common story that talent is the main thing separating people who make games from people who don't. That story is appealing, and I believed it for a long time. I thought I'd either be good at it or not, and I spent a lot of time worrying about which one I was. Looking back, most of the progress came from repetition. We finished small projects, and each one was slightly better than the last. Talent helps, but finishing things matters far more, and nobody hears that early enough.

Over the next few years, the projects grew, and so did the problems. We adopted a proper engine, and along the way we had to learn physics, timing, and the structure of a scene. I remember each stage having its own frustrations. One year it was input, the next year it was rendering, and then it was the maths behind movement. Every problem turned out to be solvable once we broke it into smaller parts and tested each part on its own. I still find that approach useful.

For example, I had a jumping character that refused to land properly. I built a tiny test scene with a single platform, and I only tuned the gravity and the jump height. Once that felt right, I moved on to the camera. We would never have got there by tweaking everything at once. Small, testable pieces are a habit I still use every day, and I'd recommend it to anyone who feels stuck. If you're stuck, try the smallest version first.

Early on, I spent far too long customising my editor. I changed colours, rearranged windows and tweaked settings. It felt productive, but nothing was really being built. We eventually settled on a simple setup, and the windows stopped being rearranged every week. The tools matter, but how quickly you can test an idea matters more. If your setup slows that down, it's worth fixing. Looking back, the most useful resources were not the flashy ones. Small forum threads, short documentation pages and a few patient community members did far more than any large course. The better sources had one thing in common, which was that they explained why a line of code worked, not only what to type. Once a source explains the reason, a whole family of problems becomes easier. We can say the same about almost any field.

Around the middle of the decade, I entered my first game jam. A jam gives 48 hours, a theme, and a deadline, and that combination is brutal in the best way. I made a game about stacking boxes in the wrong order, and I barely slept. It wasn't a good game, but it was complete, and every hour of that weekend taught me something about scope. We still use jams as one of the best ways to get better, because they force quick decisions. I still believe that.

The first project I actually released was a modest puzzle game, and the launch was nerve-wracking. I expected almost nobody to play it. About 300 people did, and a handful wrote in about a level they found hard. That was the moment it became clear to me that finishing and sharing something changes how a creator thinks about their own work. It stops being an exercise and starts being something other people use. I still remember the first message, and I read it more than once. Players respond to things in ways that are hard to predict. A level that seemed obvious to the creator can stop a player completely, while a throwaway joke becomes the most quoted line in the game. Every such reaction is useful information. The job becomes sorting the reactions that point to a real problem from the ones that only reflect a single bad afternoon. Watching how people actually play is one of the cheapest forms of testing available.

Sharing the work changed things in another way. Explaining what a project does means understanding it properly, so we tend to notice the parts we glossed over. I hit a bug, describe it to someone, and the description often reveals the answer. That's one reason I like making videos about code. Teaching is a very effective way of finding the holes in your own knowledge, and when it is explained out loud, it can't be faked for long.

Some numbers from that period are worth mentioning. I counted once, and roughly 40 projects had been started in about 3 years. Only about 6 of them ever reached a playable state. That ratio is typical, although I'm not sure anyone tracks it properly. We can see that each of the 6 taught something the others couldn't. The 34 that didn't finish weren't wasted either, because they gave us the practice that made the 6 possible.

There's something I need to correct from earlier. I used to say that a game needs a big idea before work begins. That isn't really true. For example, most of my favourite ideas came out of playing with a small mechanic until it surprised someone. The big idea usually arrived after the prototype, not before it. So if you're waiting for the perfect concept, my honest advice is to start with a rough prototype today. We don't need permission to start.

These lessons aren't specific to games. Writing software, making music, drawing or building anything else follows the same pattern. Everyone starts clumsy, things that don't quite work get made, and a sense of what good looks like slowly develops. We all go through that. The ten years were less about finding a secret and more about showing up, repeatedly, and paying attention to what went wrong. I'd call that the whole method. Writing the notes for each video follows a similar pattern. We start with a question, we find the smallest working example, and we revise the explanation until a newcomer could follow it. That process is slower than just recording, but the results hold up much better later on. We also keep a list of the places where the explanation failed, because those are usually the parts that need the most care.

Looking at the whole decade, the thing that changed most is not skill, although that improved a lot. It's patience with uncertainty. Early on, I felt every bug as a personal failure. Now I treat most bugs as clues. Everyone carries some version of the belief that the answer should already be known, and we can let go of it. I found that letting go made the work far more enjoyable, and I'd much rather be curious than certain.

If I could say one thing to the person who made that first shooter, it would be to finish more things and worry less about whether they're good. Most of them weren't, and that was fine. The good ones only appeared because the others kept getting made. Development rarely feels like progress from the inside. Weeks can pass with a single bug in view, and the visible result looks the same. Progress shows up later, when an old project is opened and something that once took a month takes an afternoon. It's a slow form of evidence, and it's easy to miss unless someone deliberately looks for it. We kept old builds for exactly that reason. I'd tell you the same thing if you're starting out today.

In the next video, one of those early projects gets rebuilt from its core loop, using everything we've learned since. It will be interesting to see what changes when you know a little more, and how much of the original code survives. The guess is that not much will, but that's part of the fun. We'll see how it goes, and I'm looking forward to it.
NARRATION>>>

## Slots
```json
{
 "format_class": "personal retrospective, story-led devlog essay",
 "answer_given_upfront": false,
 "hook_type": "story-anecdote",
 "first_question_frac": 0.5,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.04,
 "first_notation_frac": null,
 "payoff_frac": 0.85,
 "misconception": "planted-myth-defused",
 "brute_force_first": false,
 "examples_count": 2,
 "example_growth": "one blocky shooter, then a jumping platform, then a whole decade",
 "roadmap": "none",
 "viewer_turn": "none",
 "viewer_turn_frac": null,
 "caveat_type": "none",
 "recurring_anchor": "the bouncing square from the old hard drive, reused at the close",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 174,
 "median_beat_s": 40,
 "beat_sequence": ["hook", "story-rung", "caveat", "story-rung", "misconception-defuse", "story-rung", "derivation", "demo-sim", "tangent", "story-rung", "generalize", "payoff", "coda", "teaser"],
 "top5_moves": ["story", "failure-shown", "learner-discovers", "visible-repetition", "minimal-definition-then-refine"],
 "absent3_moves": ["brute-force-first", "hook-question", "expert-dialogue"]
}
```

```json
{"verified_trace": {"wpm": "PASS 174.00 (target 158.26-180.94, median 174.34)", "you_rate": "PASS 0.54 (target 0.48-0.75, median 0.52)", "i_rate": "PASS 3.72 (target 2.11-4.05, median 3.14)", "we_rate": "PASS 1.40 (target 0.46-3.16, median 2.17)", "num_rate": "PASS 1.40 (target 0.99-1.51, median 1.35)", "hedge_rate": "PASS 0.22 (target 0.12-0.28, median 0.17)", "example_rate": "PASS 0.11 (target 0.05-0.2, median 0.12)", "q_rate": "PASS 0.00 (target 0.0-0.0, median 0.0)", "sent_len": "FAIL 14.39 (target 24.7-75, median 75)", "switch_sponsor": "PASS detected=False default=OFF", "switch_teaser": "PASS detected=True default=ON", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (story-anecdote vs story-anecdote)", "ending_type": "MATCHES default (teaser-next vs teaser-next)", "summary": "8/9 numeric targets pass"}}
```
