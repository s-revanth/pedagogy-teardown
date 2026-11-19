channel: SebastianLague
id: vDrYDAMdpuc
title: Introduction to Game Development (E12: script communication)
duration: 289s (4:49)
condition: v3
recall: none
exemplars read: deep/corpus/compact/nWuekr5rUcg.txt, deep/corpus/compact/m7VY1T6f8Ak.txt

## Content skeleton
- Open on the problem: a player walks up to a door, but the door script has no idea the player exists.
- Explain that each script is a component on a game object, and objects can hold several components.
- Show GetComponent with a type in angle brackets, and what it returns.
- Store the reference once, in Start, instead of searching every frame.
- Call a public method on the other script, then handle the case where the reference is missing.
- Close with the rule of thumb for script communication, and a teaser for the next episode.

## Beat sheet
| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | A player walks up to a door, but the door script knows nothing about the player |
| 0:35 | definition | Scripts are components, and one object can hold several of them |
| 1:05 | toy-world | GetComponent with a type in angle brackets, returning the matching component |
| 1:50 | derivation | Store the reference once in Start, not every frame |
| 2:25 | demo-sim | Call a public method on the door, and watch it open in the scene |
| 3:05 | failure-shown | Missing reference: a null error, then the guard that prevents it |
| 3:40 | payoff | Rule of thumb: ask for the component you need, and check it exists |
| 4:20 | teaser | In the next episode, scripts start sending events to each other |

## Narration
<<<NARRATION
A player walks up to a door, and the door has no idea the player exists. That is the problem this episode is about. Scripts rarely work alone in a real game. The player needs to tell the door to open, and the door needs a way to respond. We can solve this by letting one script reach another. Once that connection is clear, the rest of the game starts to feel much more organised.

Every script we write is a component, and a component attaches to a game object. A single object can hold several components at once, such as a mesh renderer, a collider and our own scripts. That's the key point. I like to think of components as small workers on a shared team. You can picture the door as one worker and the player as another, and they only succeed when they can find each other. The components sit side by side on the same object, so they can find each other. We need a way to ask the object for one of its components, and that's where GetComponent comes in.

We write GetComponent with the type in angle brackets, for example GetComponent of Door. Unity looks through the object's components, finds the one that matches the type, and returns it to us. If the door script is on the same object, we get a reference we can use straight away. The reference is the handle we keep, and it's the thing we call methods on. A reference is simple, but it's also the foundation of nearly every script that talks to another script. I still remember the first time this bit me, about 5 years ago, when a door silently refused to open.

Here is where many people go wrong. It's tempting to call GetComponent inside Update, because that feels like the moment we need the answer. But Update runs every frame, and searching the object each time wastes work. Instead, we store the reference once, in a field, and we fill that field in Start. We only pay the cost of the search once, and every later call reuses the stored handle. That's a much better pattern, and it's the one we will keep using. I probably got this wrong in my first few projects, and I still see it in code written by people who should know better. You can measure the cost yourself with a simple timer, and you will be surprised how quickly the searches add up.

With the reference in place, we can call a method on the door. We write a public method called Open that changes the door's rotation or moves it out of the way. The player script calls door dot Open when the player touches the trigger. In the scene view, we see the door swing open the moment the call happens. It's a clean connection, and the two scripts stay separate. Each one still owns its own job.

Now for the failure case, because it happens to everyone. If the reference is missing, the field is null, and calling a method on it throws a null reference error. The console shows the line number, and that is usually enough to find the problem. A simple guard fixes it. We check whether the field is null before we use it, and we print a warning if it is. That guard costs almost nothing, and it turns a crash into a readable message. I usually add the object name to that warning, so the console points to the exact door. It takes 2 extra seconds to write, and it saves a lot of hunting later. We could even add the check in Awake, which runs before Start, so the problem shows up even sooner.

In a typical scene, we might have 3 scripts that all touch the same door: one for the player, one for the door itself, and one for the sound. Each script asks for what it needs, and none of them reach into the others' internals. That keeps the door at 2 states, open and closed, and nothing else leaks in. I like that restraint, and you will see it in every example from here on.

So the rule of thumb is simple. We ask for the component we need, we store it, and we check that it exists before we use it. We also keep the public methods small, so the other script has a clear action to call. If we follow those steps, we rarely have trouble with scripts talking to each other. You can keep a short checklist beside the code as a reminder. We find that a checklist helps more than memory, especially when several scripts are involved. One door is manageable, but a level with 12 doors needs a system. A good connection makes the code easy to read, and it makes the game easier to change later.

In the next episode, scripts start sending messages to each other, and the door example gets much more interesting. I'm curious how that changes the way we structure a scene. It should make the whole setup feel much less tangled.
NARRATION>>>

## Slots
```json
{
 "format_class": "tutorial series episode, code-first with scene check",
 "answer_given_upfront": false,
 "hook_type": "story-anecdote",
 "first_question_frac": 0.5,
 "first_concrete_object_frac": 0.02,
 "first_new_idea_frac": 0.08,
 "first_notation_frac": 0.35,
 "payoff_frac": 0.85,
 "misconception": "mid-video-correction",
 "brute_force_first": false,
 "examples_count": 2,
 "example_growth": "one door, one call, one missing reference",
 "roadmap": "none",
 "viewer_turn": "none",
 "viewer_turn_frac": null,
 "caveat_type": "none",
 "recurring_anchor": "the door and the player script, reused in every section",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 159,
 "median_beat_s": 40,
 "beat_sequence": ["hook", "definition", "toy-world", "derivation", "demo-sim", "failure-shown", "payoff", "teaser"],
 "top5_moves": ["story", "toy-world", "failure-shown", "rule-list", "visible-repetition"],
 "absent3_moves": ["brute-force-first", "hook-question", "expert-dialogue"]
}
```

```json
{"verified_trace": {"wpm": "PASS 159.00 (target 152.0-165.69, median 159.44)", "you_rate": "PASS 0.58 (target 0.45-0.85, median 0.64)", "i_rate": "PASS 1.05 (target 0.6-1.47, median 0.96)", "we_rate": "PASS 3.84 (target 3.81-5.27, median 4.85)", "num_rate": "PASS 1.86 (target 1.32-2.36, median 2.04)", "hedge_rate": "PASS 0.35 (target 0.15-0.36, median 0.32)", "example_rate": "PASS 0.23 (target 0.08-0.37, median 0.17)", "q_rate": "PASS 0.00 (target 0.0-0.0, median 0.0)", "sent_len": "FAIL 15.07 (target 19.31-20.56, median 20.56)", "switch_sponsor": "PASS detected=False default=OFF", "switch_teaser": "PASS detected=True default=ON", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (story-anecdote vs story-anecdote)", "ending_type": "MATCHES default (teaser-next vs teaser-next)", "summary": "8/9 numeric targets pass"}}
```
