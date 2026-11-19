# Header

- channel: kurzgesagt
- id: t7tA3NNKF0Q
- title: How Facebook is Stealing Billions of Views
- duration: 302 s
- condition: v3
- recall: vague (I know the general autoplay view-count controversy, not this video's content)
- exemplars read: deep/corpus/compact/IXxZRZxafEQ.txt, deep/corpus/compact/JhHMJCUmq28.txt
- test captions: manual

# Content skeleton

- A view counter is one of the most inflated numbers online, and the gap between a counter and a crowd is the story.
- Platform rules counted an autoplaying video as viewed after a few seconds, even muted and unwatched.
- A view was meant to signal choice and attention; autoplay measures exposure instead.
- The scroll scene: a muted clip starts, the counter ticks, and nobody has really watched.
- Publishers saw gaps between view totals and their own watch-time data; the argument ran for years.
- The arithmetic: a few thousand starts, a small share watching, and an inflated number that sells impressions.
- Views drive recommendations and pay, so the metric shapes what gets made.
- Caveat: platform definitions change and internal data is hard to check. Coda: the number reshapes what people make.

# Beat sheet

| m:ss | beat type | what is said or shown |
|---|---|---|
| 0:00 | hook | A view count is one of the most inflated numbers online, and a counter is not a crowd. |
| 0:25 | answer-statement | The platform rule counted autoplay as a view after 3 seconds, so the metric stopped meaning attention. |
| 0:50 | definition | A view was meant to be a choice to watch. Autoplay measures exposure, and the difference matters. |
| 1:20 | demo-sim | A crowded train: a thumb flicks past, a muted clip starts, and the counter ticks after 3 seconds. |
| 1:55 | story-rung | Publishers noticed the gap between platform views and their own watch data, and the argument ran on. |
| 2:30 | derivation | 1,000 autoplay starts, about 1 in 10 watching, and the inflated number becomes the sales pitch. |
| 3:05 | misconception-defuse | Views are not vanity numbers. They shape recommendations, pay, and who gets noticed. |
| 3:35 | caveat | Definitions change and internal data is hard to check, so treat any one snapshot carefully. |
| 4:00 | analogy | A turnstile that clicks for every passer-by counts walkers as attendance. |
| 4:20 | coda | When the counter rewards exposure, creators make clips that stop a thumb in the first second. |
| 4:41 | sponsor | A generic sponsor read for a planner app. Ends at 5:02. |

# Narration

<<<NARRATION
A view count is one of the most inflated numbers on the internet, and few people stop to ask what it actually measures. A video can show a big number at the top of its page while almost nobody has truly watched it. That gap is the story here, and it touches nearly all of us who have tried to find an audience online.

The short answer is that the platform's rule counted an autoplaying video as viewed after 3 seconds, even when the sound was off and nobody had chosen to press play. That single rule changed what the number meant, and it changed how the whole industry chased it. Let's look at how that happened, and why it matters beyond one company.

A view is supposed to mean something specific. When we press play on a video, we are choosing to watch it, and that choice is the signal advertisers want. An autoplay view is different. The video starts by itself as someone scrolls past, and a counter ticks up if it plays for long enough. It measures exposure, not attention, and that distinction matters a great deal. What does a view really measure? In this case, it measures whether a clip appeared on a screen, not whether a person cared.

Picture a crowded train. A thumb flicks upward in one smooth motion, and a muted clip starts playing in the middle of the screen. After 3 seconds, the counter moves by one. The viewer never heard a sound, never read the caption, and never looked back, but the number went up anyway. Multiply that by billions of scrolls, and the total starts to look very impressive. Our phones are full of these moments, and we scroll past them every day without a second thought.

Publishers noticed the gap almost immediately. Several news outlets and video makers reported in 2015 that their view totals on the platform were far higher than the watch time their own analytics showed. Some argued that the platform was counting attention it had not earned, and others argued that the metric was simply a different yardstick. Both sides had a point, which is why the argument dragged on, and it affected all of us who watch. More than 1 billion people used the platform, so even a small change in the counting rule moved an enormous number.

Let's do the arithmetic, because the numbers explain why the gap matters. Take a clip that gets 1,000 autoplay starts, and only about 1 in 10 of those viewers stay past the first few seconds. The counter shows 1,000 views, but the real attention could be closer to 100. The inflated number then becomes a sales pitch. Advertisers buy views, creators chase views, and the platform sells the impression as proof of reach. Each step rests on the first, so one definition can shape a whole market.

A common reaction is that views are just vanity numbers, and nobody should care about them. That is not quite right. Views help decide what the feed recommends, how much a clip is paid for, and how a new creator gets noticed at all. When the number is wrong, the whole system tilts toward whatever makes the counter move fastest, which means it would likely reward clips that are good at tricks rather than good at holding attention. So the stake is not pride. Our attention is what gets sold, and it is who gets rewarded for making things people actually want to watch.

There is an honest limit here. Platforms change their definitions often, and the exact rules applied at any given moment are not always public. Internal metrics are also hard for outsiders to check, and the rules may have changed since the controversy first surfaced. So we should treat any specific number as a snapshot, not as a permanent law of the platform.

Think of it this way. A turnstile that clicks for every person passing the gate would count walkers as attendance, even if nobody bought a ticket or sat down in a seat. A view counter that fires after 3 seconds works the same way. It is not lying about the clicks. It is simply measuring the wrong thing, and then all of us plan around the clicks.

The bigger lesson is that a number can quietly reshape what people make. When the counter rewards exposure, creators build clips to stop a thumb in the first second, rather than stories that hold attention for minutes. Our feeds gradually fill with the same kind of content, and we rarely notice the trade-off. Once you see the gap between a counter and a crowd, you start to read every big number with more care. What would a better number look like? Probably one that counts people who actually stayed.

This video is sponsored by a planner app for busy people, and we were asked to say that the first 30 days are free. It is a paid message, so decide for yourself whether it fits your week. If you do not need it, skip ahead, and your day will be just fine.
NARRATION>>>

# Slots

```json
{
 "format_class": "platform-metrics explainer with arithmetic demo and sponsor read",
 "answer_given_upfront": true,
 "hook_type": "premise-claim",
 "first_question_frac": 0.20,
 "first_concrete_object_frac": 0.04,
 "first_new_idea_frac": 0.09,
 "first_notation_frac": null,
 "payoff_frac": 0.86,
 "misconception": "planted-myth-defused",
 "brute_force_first": false,
 "examples_count": 2,
 "example_growth": "one thumb flick -> 1,000 starts -> whole market",
 "roadmap": "none",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.20,
 "caveat_type": "historical-uncertainty",
 "recurring_anchor": "the counter and the crowd, reused 3+ times",
 "sponsor_frac": 0.93,
 "ending_type": "impact-coda",
 "teaser": false,
 "wpm": 164,
 "median_beat_s": 25,
 "beat_sequence": ["hook","answer-statement","definition","demo-sim","story-rung","derivation","misconception-defuse","caveat","analogy","coda","sponsor"],
 "top5_moves": ["misconception-first","story","honest-caveat","analogy","generalize-to-other-domains"],
 "absent3_moves": ["act-it-out","brute-force-first","inline-quiz"]
}
```

```json
{"verified_trace": {"wpm": "PASS 164.00 (target 158.28-168.0, median 163.54)", "you_rate": "PASS 0.58 (target 0.32-1.2, median 0.75)", "i_rate": "PASS 0.00 (target 0.0-0.0, median 0.0)", "we_rate": "PASS 1.63 (target 1.23-2.59, median 2.02)", "num_rate": "PASS 2.33 (target 1.85-3.15, median 2.35)", "hedge_rate": "PASS 0.35 (target 0.29-0.79, median 0.5)", "example_rate": "PASS 0.12 (target 0.0-0.19, median 0.13)", "q_rate": "PASS 0.23 (target 0.11-0.98, median 0.32)", "sent_len": "PASS 15.91 (target 14.17-18.57, median 16.63)", "switch_sponsor": "PASS detected=True default=ON", "switch_teaser": "PASS detected=False default=OFF", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (premise-claim vs premise-claim)", "ending_type": "MATCHES default (impact-coda vs impact-coda)", "summary": "9/9 numeric targets pass"}}
```
