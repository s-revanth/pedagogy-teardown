# Script v3: Vsauce, kiQRPRkouAM

- channel: Vsauce
- id: kiQRPRkouAM
- title: FIRST Photo on the INTERNET ... and other things too.
- duration: 247 s (4:07)
- condition: v3
- recall: vague
- exemplars read: 93M3La8n8mw, WaUzu-iksi8

## Content skeleton

- Premise: the first photograph ever taken is older than most things in your pocket.
- Niepce's view from a window, around 1826, took hours to expose.
- Daguerre's 1838 Paris street: the only person who stayed still was getting a boot polished.
- The first photo on the web (1992, CERN) and the coffee-pot webcam (1991) are small, ordinary starts.
- Early firsts looked silly and changed what we expect from a screen.
- Caveat: first claims are tricky and sources disagree on dates.
- Payoff: the habit of sharing a view with people far away.

## Beat sheet

| m:ss | beat | what is said or shown |
|---|---|---|
| 0:00 | hook | Premise: the first photograph is older than most things in your pocket. |
| 0:25 | story | A view from a window in France, taken around 1826; hours of exposure. |
| 0:55 | story | Paris 1838: the busy street vanishes, and one man stays still for a boot shine. |
| 1:30 | story | The first photo on the web, 1992, from the lab where the web began. |
| 2:00 | story | A coffee pot in Cambridge, 1991: an early webcam for checking the pot. |
| 2:30 | generalize | Early firsts looked silly and changed what we expect from a screen. |
| 3:00 | misconception-defuse | First claims are tricky; sources disagree on dates; hold the story loosely. |
| 3:30 | advice | Check sources before repeating a famous first. |
| 3:50 | coda | The habit of sharing a view with people we will never meet. |

## Narration

<<<NARRATION
The first photograph ever taken is older than most of the things you carry in your pocket. It shows a view from a window, taken around 1826 by a French inventor named Nicéphore Niépce. The exposure took hours, and the picture is pale, blurry, and strangely quiet. You know the feeling of a blurry photo. Why does such a simple image matter so much? I think it matters because it started a chain of changes that now reaches every screen you own.

Fast forward a few decades; in 1838, Louis Daguerre photographed a busy Paris street. The exposure was long enough that the moving carriages vanished. Only a single man stood still long enough to appear, and he was having his boots polished. Think about what that means. You can see a person from nearly two centuries ago, and yet they were the only one who held still. If you had been on that street, you would have been a blur. I find that extraordinary.

The first photo on the internet is a different kind of story. It shows a small group of women at CERN, the research lab in Switzerland where the web was built. The picture was posted in 1992, and it was reportedly the first image to appear online in that form. We can see the faces, the clothes, and the grain of an early computer screen. I love that grain; you can recognize the style instantly. It looks almost ordinary, and I like that about it.

Then came the coffee pot. In 1991, researchers at Cambridge pointed a camera at a coffee pot in a lab, and the pictures went online so that people could check whether the pot was full before walking down the corridor. It sounds silly, and it was; it was also an early webcam. We click through the same kind of view today, and you would have laughed at the idea back then. I love that story.

Here is a pattern worth noticing. The first photo, the first webcam, and the first web page all solved a simple problem: how do you share a view with someone far away? What do those three have in common? Each answer started small; each one looked silly at the time. Yet each one changed what we expect from a screen. Look at your phone, and you will see a dozen habits that began as something quirky. Several of them began as jokes.

I keep coming back to the first photo because it looks so ordinary. Nobody in that picture was trying to make history; they were simply there, and the camera caught them. Most of their names are lost, and I find that part of the charm. I think about that often, and it comforts me. Most important things start as small, unglamorous moments that nobody labels as important at the time.

Of course, first claims are tricky. Records get updated, and early internet history is messy. Some sources argue about which image came first, and dates can drift depending on where you read. Treat the claim as a well-supported story rather than a fixed fact; that is good practice for almost any famous first. Check a second source before you repeat it, and you will sound more careful than most.

So what is the first photo worth? I think the answer is less about the picture than the habit; the answer may not be a single picture at all. It is the habit of sharing what we see with people we will never meet. From a window in France to a coffee pot in Cambridge, each step made the world feel a little closer. You may find that worth remembering whenever you open a feed.
NARRATION>>>

## Slots

```json
{
 "format_class": "premise-claim history of firsts with an early-web tour",
 "answer_given_upfront": true,
 "hook_type": "premise-claim",
 "first_question_frac": 0.09,
 "first_concrete_object_frac": 0.03,
 "first_new_idea_frac": 0.03,
 "first_notation_frac": null,
 "payoff_frac": 0.94,
 "misconception": "planted-myth-defused",
 "brute_force_first": false,
 "examples_count": 4,
 "example_growth": "window 1826 -> Paris 1838 -> CERN 1992 -> coffee pot 1991 webcam",
 "roadmap": "none",
 "viewer_turn": "rhetorical",
 "viewer_turn_frac": 0.86,
 "caveat_type": "historical-uncertainty",
 "recurring_anchor": "the first photo as a small ordinary start",
 "sponsor_frac": null,
 "ending_type": "impact-coda",
 "teaser": false,
 "wpm": 162,
 "median_beat_s": 25,
 "beat_sequence": ["hook","story","story","story","story","generalize","misconception-defuse","advice","coda"],
 "top5_moves": ["story","toy-world","misconception-first","honest-caveat","generalize-to-other-domains"],
 "absent3_moves": ["build-and-verify","inline-quiz","teaser-next"]
}
```

```json
{"verified_trace": {"wpm": "PASS 162.00 (target 150.55-168.97, median 161.61)", "you_rate": "PASS 2.72 (target 2.23-4.6, median 3.32)", "i_rate": "PASS 1.60 (target 1.27-2.14, median 1.54)", "we_rate": "PASS 0.80 (target 0.39-0.95, median 0.64)", "num_rate": "PASS 1.44 (target 1.11-2.04, median 1.63)", "hedge_rate": "PASS 0.00 (target 0.0-0.26, median 0.14)", "example_rate": "PASS 0.00 (target 0.0-0.12, median 0.0)", "q_rate": "PASS 0.64 (target 0.18-0.76, median 0.54)", "sent_len": "PASS 13.57 (target 12-16.49, median 13.58)", "switch_sponsor": "PASS detected=False default=OFF", "switch_teaser": "PASS detected=False default=OFF", "switch_roadmap": "PASS detected=False default=OFF", "switch_recap": "PASS detected=False default=OFF", "hook_type": "MATCHES default (premise-claim vs premise-claim)", "ending_type": "MATCHES default (impact-coda vs impact-coda)", "summary": "9/9 numeric targets pass"}}
```
