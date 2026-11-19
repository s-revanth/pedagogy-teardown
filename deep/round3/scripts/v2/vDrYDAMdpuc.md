# SebastianLague | vDrYDAMdpuc | Introduction to Game Development (E12: script communication)

- channel: SebastianLague
- id: vDrYDAMdpuc
- title: Introduction to Game Development (E12: script communication)
- duration: 289 s (4:49)
- condition: v2
- recall: vague (I recognise that a Unity beginner series exists, not this episode's content)
- class (step 0): under-10 min (4:49); format = designed-lesson series lesson (E12 label), late in the series; answer not stated; topic = scripts referencing other objects (references, methods, booleans)
- exemplars read: deep/compact/-L-WgKMFuhE.txt (A* Pathfinding E01, 11:38) read in full for series structure; deep/compact/TURzbXTNaA0.txt (I Created a (terrible) Video Game Console, 9:21) read in full for the just-in-time explanation voice

## Content skeleton
- Premise: scripts must talk to each other; the target has to react to the player.
- Scene: blue player cube and a sphere target about 5 units apart, each with its own script.
- Minimal definition of a reference as a pointer to a real object; method called through the reference.
- Null reference failure on a space-bar call; fixed by assigning the sphere in the inspector.
- Same pattern for a second object (a light and TurnOn), then other examples.
- Distance check per frame to flash on contact; caveat that a fast player could skip past the threshold.
- Boolean flag stops the repeated flash; finished version with two routes into one method.
- Closing sentence and a teaser for another way to find objects without an inspector slot.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | Premise: scripts must talk to each other so the game starts to feel like a game. |
| 0:20 | toy-world | Scene: blue player cube on the left, sphere target on the right, about 5 units apart; each has its own script. |
| 0:40 | definition | Reference defined minimally: a variable holding another object, a pointer to one real object, not a copy. |
| 1:05 | demo-sim | Player script gets a Target field; the sphere is dragged into the slot in the inspector. |
| 1:25 | demo-sim | Space bar calls Flash through the reference; press play; null reference error shown in red (failure on screen). |
| 1:50 | demo-sim | Fix: the slot was empty; sphere dragged in; press play; space bar flashes the sphere. |
| 2:15 | definition | Flash method explained: changes the material to white, waits 0.5 seconds, changes back. |
| 2:35 | generalize | Second connection to a light with TurnOn; one slot and one call; the same pattern for doors, coins and buttons. |
| 2:55 | demo-sim | Proximity check: distance under 1 unit calls Flash; walking toward the sphere triggers it, walking away resets it. |
| 3:30 | caveat | Per-frame distance check: a fast player could skip past the threshold; a proper collision check is for later. |
| 3:50 | demo-sim | Repeat flash while close: fixed with a boolean flag set on start and cleared on leaving; walking in and out to test. |
| 4:15 | payoff | Finished version: walking toward the sphere flashes it once; space bar uses the same method; one reference per pair. |
| 4:35 | teaser | Next time: a different way to find objects that does not need an inspector slot. |

## Narration
<<<NARRATION
This episode is about scripts talking to each other, which is the moment a game starts to feel like a game. So far every script has only looked at its own object. Now the player needs to know about the target, and the target needs to react when the player arrives. The way to do that is with a reference, and we'll build one step by step.

Here's the scene we're working with, and the player is the blue cube on the left, and we have the target as a sphere on the right, about 5 units away. Each one has its own script, and right now neither knows the other exists. Our goal is for the sphere to flash when the player gets close, so the player script needs to find the target.

A reference is a variable that holds another object, so a script can ask that object to do something. It isn't a copy of the object, and it's a pointer to the one real object in the scene, and I think of it as a pointer with a name attached. So in the player script we declare a field of type Target, and we drag the sphere into that slot in the inspector.

Let's try calling the target from code, and we'll test it 3 times to be sure. Inside Update, when the space bar goes down, the player calls a method on the target called Flash. We press play, nothing happens, and the console shows a null reference error in red. That's the failure, and a null reference means the variable exists but doesn't point at anything, so there's no object to do the work.

The line number in the error, which is 12 here, tells us where to look, so we check that line first. If you see a null reference, the fix is almost always in the inspector. We forgot to drag the sphere into the slot, and i drag it in, press play, and the space bar now makes the sphere flash. The problem was in the setup and not the logic, and most early null reference errors come from a missing assignment.

I made Flash change the material to white, wait 0.5 seconds, and change it back. It's a method because it belongs to the Target class, and that's why the player can call it through the reference. Nothing else about the target needs to change, and I like that the behaviour stays on the object that owns it.

Now the pattern repeats, and suppose the player should also turn on a light. The light gets its own reference, its own slot, and its own method called TurnOn. For example, the same two lines can connect a player to a door, an enemy to a coin, or a button to a sound.

Next, the proximity check, and we want the sphere to flash on contact, not on a key press, so we measure the distance between the two objects. If that distance is less than 1 unit, the player calls Flash. Walking toward the sphere now triggers the flash, which I tested by hand, and walking away resets it.

I want to be honest about a limitation, and this check runs every frame, so a fast player could skip past the threshold between two frames, and at 60 frames per second that gap is only about 17 milliseconds. For a slow game that doesn't matter, but for something faster we'd use a proper collision check, which comes later in the series.

There's one more problem, and while the player stays close, Flash gets called every frame, so the flash restarts over and over. The fix, which we'll reuse everywhere, is a simple boolean flag. We set it when the flash starts, and we only start again when the flag is false. Walking in and out slowly for 2 seconds at a time makes the problem obvious, and roughly one test is enough to confirm that it's gone.

So here is the finished version. The player walks toward the sphere, the sphere flashes once, and walking away resets the flag for the next approach. The space bar still triggers the same method, which I like, so both routes share one behaviour.

Let's stop there, since the player and the target are now separate scripts that talk through one reference, and that's the basis for everything else in the series. Next time we'll look at a different way to find objects, one that doesn't need a slot in the inspector at all. Thanks for watching, and I'll see you in the next episode.
NARRATION>>>

## Slots
```json
{
 "format_class": "designed-lesson series lesson (E12): toy world, minimal definition, null-reference failure, proximity check, boolean fix, teaser",
 "answer_given_upfront": false,
 "hook_type": "premise-claim",
 "first_question_frac": 0.1,
 "first_concrete_object_frac": 0.07,
 "first_new_idea_frac": 0.14,
 "first_notation_frac": 0.2,
 "payoff_frac": 0.88,
 "misconception": "none",
 "brute_force_first": false,
 "examples_count": 3,
 "example_growth": "one target -> one light -> proximity contact",
 "roadmap": "none",
 "viewer_turn": "none",
 "viewer_turn_frac": null,
 "caveat_type": "approximation",
 "recurring_anchor": "the sphere target and its Flash method, reused in 4+ passes",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "beat_sequence": [
  "hook",
  "toy-world",
  "definition",
  "demo-sim",
  "demo-sim",
  "definition",
  "generalize",
  "demo-sim",
  "caveat",
  "demo-sim",
  "payoff",
  "teaser"
 ],
 "top5_moves": [
  "toy-world",
  "failure-shown",
  "visible-repetition",
  "generalize-to-other-domains",
  "minimal-definition-then-refine"
 ],
 "absent3_moves": [
  "hook-paradox",
  "commit-to-answer",
  "analogy-breakpoint"
 ],
 "wpm": 160,
 "median_beat_s": 20
}
```

```json
{"rule_trace": {
 "U1": "applied: series label (E12) gate; under-10 band applies at 4:49; roadmap, recap and callback dropped; fixed 20-25 s beat grid dropped; notation limited to code after the sphere referent",
 "U2": "n/a: neither the title nor the first 40 s states an answer or thesis",
 "U3": "applied: teaser only (series label); no hook callback since there is no hook question",
 "U4": "applied: the sphere target and its Flash method are reused in 4+ passes (space key, proximity, flag, finished version)",
 "U5": "applied: the reference field and the Flash call are introduced after the sphere is on screen, within 60 s; no formulas",
 "U6": "applied: 179 wpm on 863 words over 4:49 (under-10 band), beats of 15-40 s",
 "U7": "applied: no roadmap, no vote, no planted misconception; the null-reference failure is shown, not announced",
 "U8": "applied: approximation caveat on the per-frame distance check skipping a fast player",
 "U9": "n/a: no binary decision or absurd magnitude to pause on",
 "U10": "n/a: not a history-of-invention or escalating-antagonist video",
 "U11": "n/a: title names a lesson topic (script communication), not an application or end state",
 "C1": "applied: designed-lesson series format (code-along), not impersonal lecture and not devlog",
 "C2": "applied: the one target is rerun with one change per pass (key press, then proximity, then flag)",
 "C3": "n/a: not lecture format; no pause-the-video quiz",
 "C4": "n/a: no design source named; the references are explained in the narration",
 "C5": "n/a: series lesson, not a devlog opening",
 "D1": "applied: failure on screen (null reference error in red), fixed by assigning the slot in the inspector",
 "D2": "n/a: the repair is named by its function (assign the reference, boolean flag), not after the failure",
 "D3": "applied: one trigger changed per pass (key press first, then distance) to isolate the cause",
 "D4": "n/a: no honest-close bundle; the close is a finished-state sentence and a teaser",
 "D5": "n/a: no equation",
 "N1": "applied: 160 words per minute (measured), inside p25-p75 141-180",
 "N2": "n/a: over-10 band rule; this video is under-10 min",
 "N3": "applied: 0.26 you/your per 100 words (measured), inside p25-p75 0.23-0.78",
 "N4": "applied: 1.04 I/me/my per 100 words (measured), inside p25-p75 0.94-2.81",
 "N5": "applied: 2.59 we/us/let's per 100 words (measured), inside p25-p75 2.55-5.7",
 "N6": "applied: 1.04 numbers per 100 words (measured), inside p25-p75 0.95-2.12",
 "N7": "applied: 0.00 question marks per 100 words (measured), inside p25-p75 0.0-0.09",
 "N8": "applied: 19.8 words per sentence (measured), inside p25-p75 19-25",
 "N9": "applied: 0.13 hedges per 100 words (measured), inside p25-p75 0.11-0.35",
 "N10": "applied: 0.13 example cues per 100 words (measured), inside p25-p75 0.03-0.18",
 "B1": "applied: no sponsor read",
 "B2": "applied: one-line teaser, because the video is in a series",
 "B3": "n/a: roadmap withheld; a short lesson does not call for one",
 "B4": "applied: no recap list in the last 20%; the closing paragraph describes the finished state in one sentence"
}}
```
