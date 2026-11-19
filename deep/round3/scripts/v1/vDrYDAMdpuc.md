# Header
- channel: SebastianLague
- id: vDrYDAMdpuc
- title: Introduction to Game Development (E12: script communication)
- duration: 289 s (4:49)
- condition: v1
- recall: vague

## Content skeleton
- Goal: a switch opens a door, and the two objects have separate scripts.
- Toy world: a switch and a door in the scene, each with its own script.
- Brute force: the switch script finds the door by its name string at runtime.
- Wall: rename the door and the lookup returns nothing; a null reference error appears.
- Minimal definition: a reference is a variable that points at another object.
- Dragging the door into a slot in the inspector; press Play; the door opens.
- Misconception: scripts cannot see each other automatically; the reference must be given.
- Generalise to an enemy, a sound or a pickup.
- Caveat: events are a better pattern later; teaser for the next episode.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | A switch should open a door; how do two scripts talk to each other? |
| 0:20 | roadmap | Name lookup first, then a reference, then the same idea elsewhere |
| 0:40 | toy-world | Switch and door in the scene, each with a script |
| 1:00 | brute-force | Switch script finds the door by name in code; door opens |
| 1:40 | wall | Rename the door; null reference error; the lookup returns nothing |
| 2:10 | definition | A reference is a variable pointing at the door object |
| 2:40 | demo-sim | Drag the door into the inspector slot; press Play; the door opens |
| 3:20 | misconception-defuse | Scripts cannot see each other automatically; the reference must be given |
| 3:50 | generalize | Same reference for an enemy, a sound, a pickup |
| 4:15 | caveat | Simplified; events are a better pattern later |
| 4:35 | teaser | Next episode: events |
| 4:45 | coda | Sign-off |

<<<NARRATION
A switch should open a door. That sounds simple, and in a game it is one of the first things you want to build. But the switch and the door are two different objects, each with its own script. So how do two scripts talk to each other? That is what this episode is about.

Here is the plan. We start with the way that looks easiest, which is finding the door by name. Then we see why that breaks, and replace it with a reference. Last, we use the same idea for an enemy and a sound.

The toy world is a switch and a door, sitting in the scene. Each one has a script attached. The switch script should notice when it is pressed, and the door script should open. Right now, neither script knows the other exists. That is the whole problem.

The dumb version is the first thing I tried, and it works. In the switch script, I ask the engine to find an object with the name door, and I get back the door. Then I tell the door to open. Press Play, press the switch, and the door opens. So far, nothing looks wrong.

Then I rename the door and press Play again. Pressing the switch does nothing this time. The console shows a null reference error, which means the switch asked for an object called door, and the engine could not find one. The code still says door, and the scene now says something else. That is the wall. The connection depends on a string that I have to keep in sync by hand.

So the name lookup is fragile. It works until somebody renames something, and then it fails far away from where the rename happened. That is a bad property for a game, where things get renamed all the time.

Here is the idea that replaces it, defined as small as I can make it. A reference is a variable that points at another object. That is all. It is not a copy of the door, and it is not a name. It is a direct link, stored in a field on the switch script, which points at the door itself.

To make it work, I add a public field to the switch script, and I set its type to the door's script. Now the inspector shows an empty slot for the door. I drag the door from the hierarchy into that slot. That fills the reference. I rename the door again, just to be sure, and it still works. The link is to the object, not to its name, so the rename does not matter.

Now press Play, press the switch, and the door opens. It is the same test as before, but the connection is now a reference, and I have checked that the rename no longer breaks it. Two tests, two results, and the only change between them is how the switch finds the door.

Here is a mistake I used to make. I thought that scripts could see each other automatically, that the switch would just know about the door because they were in the same scene. They cannot. Each script only has access to what you give it. Until you provide a reference, the switch has no idea that the door exists. The reference is not optional, and it is not magic. It is the link you have to make yourself.

The same pattern works for other things. An enemy can hold a reference to the player, so it knows where to move. A sound effect can hold a reference to the audio source on the coin. A pickup can hold a reference to the score display. In each case, the object that needs the other one holds a field that points at it, and you fill that field in the inspector. Once you see the shape, you can use it for anything.

Here is the honest bit. This is the simplest version, and it has limits. The switch knows about the door specifically, so if you want a second door to open with the same switch, you have to add another reference. There are better patterns for that, which send a message rather than calling a specific object, and I will cover one of them next time.
So let's recap. A name lookup works until something gets renamed, and then it breaks. A reference is a variable that points directly at the object, and it survives renaming. Scripts do not see each other on their own, so you have to give them the link.

Next time we look at events, which let one script announce that something happened without needing to know who is listening. That removes the need for a reference in many cases, and it makes the second door much easier to add.

Thanks for watching.
NARRATION>>>

## Slots

```json
{
 "format_class": "build-break-fix devlog, name lookup to reference",
 "answer_given_upfront": true,
 "hook_type": "scenario-you",
 "first_question_frac": 0.02,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.21,
 "first_notation_frac": 0.21,
 "payoff_frac": 0.55,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "name lookup -> dragged reference -> enemy and sound",
 "roadmap": "one-line",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.02,
 "caveat_type": "approximation",
 "recurring_anchor": "the door object, referenced by name in one version and by link in the next",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 30,
 "beat_sequence": ["hook","roadmap","toy-world","brute-force","wall","definition","demo-sim","misconception-defuse","generalize","caveat","teaser","coda"],
 "top5_moves": ["toy-world","brute-force-first","failure-shown","build-and-verify","honest-caveat"],
 "absent3_moves": ["hook-paradox","expert-dialogue","inline-quiz"]
}
```
