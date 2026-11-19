# Header

- channel: Vsauce
- id: kiQRPRkouAM
- title: FIRST Photo on the INTERNET ... and other things too.
- duration: 247 s (4:07)
- condition: v1
- recall: vague

## Content skeleton

- Opens on a question about the first photo ever shared online
- Explains that a photo is a grid of numbers that can travel over a network
- Puts the 1991 Cambridge coffee-pot camera forward as the leading candidate
- Breaks the idea that early web photos were deliberate publishing events
- Admits the earliest image sharing is poorly documented, so "first" is hard to pin
- Generalises the grid-plus-link trick to every modern image
- Runs a short tangent on other "firsts" and closes on a callback to the coffee pot

## Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Asks what the first photo ever put online was; shows a blurred grey frame. |
| 0:22 | roadmap | Three steps: what a photo is to a computer, the first candidate, why it mattered. |
| 0:40 | toy-world | Zooms into a photo until it becomes a grid of coloured squares, each a few numbers. |
| 1:05 | story-rung | 1991 Cambridge lab: a camera on the coffee pot so people could check before walking over. |
| 1:50 | misconception-defuse | Early photos were lab tools, not deliberate publishing; "first" is hard to pin down. |
| 2:20 | generalize | A modern image is numbers, a file name and a link: the same as the coffee pot. |
| 2:40 | viewer-turn | Asks the viewer to guess what the first image looked like. |
| 3:15 | payoff | Describes the grainy coffee-pot image and why it mattered. |
| 3:40 | tangent | Other firsts (GIF, emoji) as small hacks shared before anyone knew they were historic. |
| 3:55 | callback | Returns to the opening question and the answer. |
| 4:15 | teaser | Points to the next first and who was there to notice. |

## Narration

<<<NARRATION
What was the first photo ever put on the internet? Pause for a second and guess. Really, guess. Most people imagine something ancient, grainy and historic, and the real answer is weirder and more ordinary than that.

Here's the plan. We're going to look at what a photo even is to a computer, then find the first image people shared online, and then see why it mattered more than anyone expected at the time.

Start with the photo itself. Your phone camera doesn't capture a picture the way you'd think. It records a grid of tiny light readings, one for each pixel, and each reading is just a few numbers: red, green and blue, each one a value from zero to 255. Sending a photo across a network means sending those numbers, in order, in an agreed format, and hoping the other end knows how to rebuild the grid.

Which brings us to 1991. At the University of Cambridge, the computer lab had a problem with coffee. The coffee pot was on a floor the researchers didn't want to walk to. Somebody pointed a camera at the pot, connected it to a computer, and wrote a little program that grabbed a picture every so often. Anyone on the local network could load the picture and see whether the pot was empty or full before making the trip.

That's a webcam, and it is a sensible candidate for the first photo ever shared online, or at least the first live image anyone remembers being shared. The pictures were small and grainy, a few dozen shades of grey, and they were refreshed slowly. It was a tool for not wasting a walk.

Here's the misconception worth breaking. People picture early internet photos as big, deliberate publishing events, a magazine cover for the web. In practice, the first images were hacks by researchers and students who wanted to share data, diagrams and sometimes each other. A photo was just a file you could fetch, and the people who built the web were mostly trying to make their lab notes reachable.

So was the coffee pot the first? Honestly, it's hard to say. Early image sharing happened on bulletin boards and in newsgroups, where people posted encoded files that had to be decoded by hand, and many of those files are lost. A lot of the early history was never written down, because it didn't seem important at the time. That's a useful lesson on its own. The past is full of firsts that nobody recorded.

Now try the idea on something else. Every image you see online works the same way: a list of numbers, a file name, and a link that tells your browser where to look. The coffee pot needed the same three ingredients as a modern photo of your lunch. The only things that changed are the resolution and the number of people who can fetch the file.

And then the strange part. Once a picture is a link, anyone can fetch it, copy it and keep it forever. The first photo on the internet was a way to check on coffee. The millionth was a way to check on a friend. Each one was built on the same small step: a grid of numbers that another machine could turn back into a picture.

The same is true of the other things in this episode. The first GIF, the first meme and the first emoji each sound like a moment, but each one was a small, useful hack that somebody shared before anyone knew it was historic. So if you find an old photo that looks boring, look again. It may be the most important coffee pot in history.

So, back to the question. Did you guess right? If you guessed something fancy, you were in good company. The answer is a grainy view of a pot, shared so people didn't have to walk for nothing. That's the first photo on the internet, and it's a good place to start thinking about everything else the web carries.

Next time, we'll look at another first, and see who was there to notice it.

Thanks for watching.
NARRATION>>>

## Slots

```json
{
 "format_class": "found-object history tour, question then unpacking",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.01,
 "first_concrete_object_frac": 0.00,
 "first_new_idea_frac": 0.16,
 "first_notation_frac": null,
 "payoff_frac": 0.79,
 "misconception": "planted-myth-defused",
 "brute_force_first": false,
 "examples_count": 3,
 "example_growth": "one coffee pot to many firsts",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.65,
 "caveat_type": "historical-uncertainty",
 "recurring_anchor": "the coffee pot",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 22,
 "beat_sequence": ["hook", "roadmap", "toy-world", "story-rung", "misconception-defuse", "generalize", "viewer-turn", "payoff", "tangent", "callback", "teaser"],
 "top5_moves": ["hook-question", "toy-world", "misconception-first", "generalize-to-other-domains", "story"],
 "absent3_moves": ["notation-after-concept", "build-and-verify", "inline-quiz"]
}
```
