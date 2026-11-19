# PrimerBlobs: Simulating the Evolution of Teamwork

- channel: PrimerBlobs
- id: TZfh8hpJIxo
- title: Simulating the Evolution of Teamwork
- duration: 1102 s (18:22)
- condition: v1
- recall: none

## Content skeleton
- Opens on the puzzle: a selfish blob should out-eat a generous one, so why does helping exist?
- A grid world of blobs and food, one rule (eat, split when full), and a helper versus keeper trait.
- Baseline with only keepers, then helpers mixed in: helpers lose, and the sim shows why.
- Spatial clustering (children land next to parents) is the first change that makes helping pay.
- A cost sweep with thirty runs per setting, where the boundary is a benefit-to-cost line that is named only after it is seen.
- A memory-based reciprocity rule, with a self-corrected bug and a caveat that perfect memory is generous.
- Recap of the two routes to helping (relatives nearby, or remembered partners), then a teaser for changing partners.

## Beat sheet

| Time | Beat type | What is said or shown |
|---|---|---|
| 0:00 | hook | Question: why would a blob give away food it could keep? |
| 0:20 | roadmap | Build the world, add helping, see what it takes for helping to spread. |
| 0:50 | toy-world | Grid of blobs and food pellets; one rule: eat, and split when full. |
| 1:40 | definition | Each blob carries one trait, keeper or helper; helping costs the helper food. |
| 2:30 | brute-force | Baseline: everyone is a keeper. Population grows, food runs out where it is crowded. |
| 3:20 | demo-sim | Add a few helpers at random. Run once. Helpers shrink and vanish. |
| 4:20 | viewer-turn | Pause: three outcomes listed (helpers die out, balance, takeover). Viewer picks one. |
| 5:05 | demo-sim | Thirty runs from the same start. Keepers win in each. |
| 6:05 | misconception-defuse | The intuition "helping is good for the group, so the group wins" is set up and broken. |
| 7:10 | wall | In a mixed crowd, the helper pays the cost while neighbors keep the food. |
| 8:00 | demo-sim | Rule change: children land next to their parent. Run it. |
| 9:10 | demo-sim | Helper clusters grow; food given by a helper tends to reach another helper. |
| 10:20 | payoff | Inside clusters helpers beat the keepers near them; clusters take large regions. |
| 11:15 | caveat | Grid size, neighbor count and food amounts are the presenter's picks, not claims about animals. |
| 12:10 | demo-sim | Cost sweep: thirty runs per setting. Helpers win below a cost threshold. |
| 13:20 | derivation | Relatedness times benefit must exceed cost: the line the sweep already showed, now written as a formula. |
| 14:30 | generalize | Shared work in crews and teams follows the same bookkeeping. |
| 15:20 | viewer-turn | Pause: if blobs remember who helped them, does reciprocity beat keepers? |
| 15:50 | demo-sim | Memory rule: help those who helped last round. Reciprocators win in small groups. |
| 16:40 | caveat | Memory is perfect and free in the model; real memory is short and costly. |
| 17:10 | recap | Helping spreads near relatives or with remembered partners; otherwise keepers win. |
| 17:45 | teaser | Next: blobs that change partners and forget the last round. |
| 18:10 | coda | Closing image: one cluster of helpers on the grid, still growing at the edge. |

<<<NARRATION
Why would a blob give away food it could keep? The obvious answer is that it shouldn't. The blob that keeps everything should do better, and over time the generous blobs should die out. Yet real animals help each other all the time, sometimes at a real cost to themselves. So the question for this video is whether helping can evolve, and if it can, under what conditions. We'll answer it the way we've answered everything else: build a small world, run it, and watch what happens.

Here is the world. It's a grid. Some squares hold food. Each blob sits on a square, and it can eat any food it touches. When a blob has eaten enough, it splits in two, and the new blob lands on an empty square nearby. If a blob runs out of food, it dies. That's the whole world.

Each blob carries one trait, and the trait passes to its children. There are two kinds. Keepers eat everything they touch. Helpers do the same, but when a neighbor is hungry, a helper gives it a share of its food. That share costs the helper. It ends up with less than it would have had.

Before I add anything, I want a baseline. This is the dumbest version. Everyone is a keeper. Run it. The population grows, and in the crowded parts of the grid the food runs out. Nothing surprising yet, but this is the reference point for everything that follows.

Now add helpers. I'll start with a few, scattered at random among the keepers, and run it once. Watch the helpers. They give food away, and their neighbors grow. But the keepers keep everything, and they are the ones who get to split. Over several generations the helpers become fewer, and then they are gone.

Before we go on, make a prediction. This is where the answer is not obvious. There are three outcomes I can see. The helpers die out. The helpers and keepers settle into a balance. Or the helpers take over. Pause the video and choose one.

Welcome back. If you chose die out, you're right for this setup. One run can be a fluke, so I ran thirty copies of the same starting grid. In every one, the keepers win. The thin lines are individual runs, and the thick line is the average. The helper share falls to zero, or close to it, in all of them.

So helping, in a mixed crowd, is a losing strategy. The reason is easy to see once you watch it. A helper pays its cost, and the food it gives away goes to a neighbor who has no reason to return it. The helper is subsidizing the keepers around it.

A common argument goes like this. Helping is good for the group, so the group should do well, and the group should win. It's a reasonable thought. But a group only does better when its helpers stay together. In a well-mixed population, there is no group. There are individuals, and the individual keeper always has the edge.

So what would have to change? I'll try one thing at a time. The first change is where offspring land. In the original version, a child can land anywhere nearby. Now let's say a child always lands right next to its parent. That's a small change in the rules, and it matters a lot.

Run it. Look at the helpers now. They're clustered. A helper's neighbors are often its own children, and those are helpers too. When a helper gives food away, the food is more likely to go to another helper. The cost is still paid, but the benefit comes back to the cluster.

The clusters grow. At their edges, keepers still take advantage. But inside a cluster, helpers do better than the keepers near them. Over time the clusters take over large regions of the grid. In the thirty runs, helpers win in most of them.

Here is where I want to be careful. This result depends on choices I made. I picked the grid, how many neighbors count, how much food a helper gives, and what it costs. I'm not claiming these numbers describe any real animal. I'm claiming the shape of the result: clustering can make helping pay.

To check the shape, let's sweep the cost. I keep the benefit fixed, change the cost of helping, and run thirty copies at each setting. When the cost is low, helpers win. When the cost is high, they lose. The boundary between the two is where the benefit to the helper's relatives, weighted by how related they are, equals the cost. In the standard notation, relatedness times benefit has to exceed cost. That symbol doesn't appear until the sweep is done, because the sweep is what it summarizes. We already saw the line before we wrote it down.

This bookkeeping is not limited to blobs. Any shared work has the same shape. A crew of people who stick together and share their gains can beat a crew of individuals who keep theirs, provided the crew doesn't fill up with members who only take.

Now the next change. What if blobs remember who helped them last round? Make a prediction first. If a blob helps back the neighbors who helped it, does that reciprocity beat the keepers? Pause and decide.

Here's what I first got, and it was wrong. My first memory version reset every blob's record each round, so the reciprocators never had a history to act on. Keepers won everywhere, and I had expected the opposite. The bug was mine. When I fixed it so that memory carried across rounds, the reciprocators won in small groups. That's the result I'm showing you now.

Even then, the model is generous. Memory is perfect, and it costs nothing. Some keepers still sneak through each round. When I shorten the memory, the keepers do better, and reciprocity weakens. Real animals don't keep perfect records, and remembering takes energy. So the honest version of this result is narrower than the sim makes it look.

Let's sum up. Helping spreads when helpers sit near their relatives, so the benefit lands on other helpers. It also spreads when partners can remember who helped them and return the favor. Otherwise, a mixed crowd rewards whoever keeps everything.

Next time, we'll break one more assumption. What happens when blobs can change partners, and nobody remembers the last round? Before then, try the sweep yourself. Change the cost, run thirty copies, and see where your own line falls.
NARRATION>>>

```json
{
 "format_class": "build the world, baseline first, one rule changed per step",
 "answer_given_upfront": false,
 "hook_type": "question",
 "first_question_frac": 0.0,
 "first_concrete_object_frac": 0.0,
 "first_new_idea_frac": 0.09,
 "first_notation_frac": 0.73,
 "payoff_frac": 0.56,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 4,
 "example_growth": "keepers only, mixed helpers, clustered, remembered partners",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.24,
 "caveat_type": "approximation",
 "recurring_anchor": "the same grid and blob rules reused in every run",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 50,
 "beat_sequence": ["hook","roadmap","toy-world","brute-force","demo-sim","viewer-turn","misconception-defuse","demo-sim","payoff","caveat","derivation","generalize","recap","teaser"],
 "top5_moves": ["toy-world","brute-force-first","simulation-as-argument","visible-repetition","honest-caveat"],
 "absent3_moves": ["story","humor","expert-dialogue"]
}
```
