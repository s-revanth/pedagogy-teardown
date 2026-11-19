# PrimerBlobs: What's a "selfish gene"?

- channel: PrimerBlobs
- id: 2mTVtToioLg
- title: What's a "selfish gene"?
- duration: 354 s (5:54)
- condition: v1
- recall: none

## Content skeleton
- Opens on the puzzle that a gene has no mind, so "selfish" must mean something narrower.
- Defines a gene by its versions, and "selfish" as a version that gets passed on more than its fair share.
- A fair-inheritance baseline where the driver version stays near half and nothing is selected.
- A driver that transmits sixty percent of the time; a prediction pause; then the spread, limited by a fitness cost to carriers.
- Defuses the group-benefit myth and names real cases of genes that bias their own transmission.
- Flags the metaphor honestly, and teases the case where cost cancels advantage.

## Beat sheet

| Time | Beat type | What is said or shown |
|---|---|---|
| 0:00 | hook | Question: how can a gene be selfish if it has no mind? |
| 0:20 | roadmap | One line: define the word, then test it in a population. |
| 0:40 | definition | A gene is a stretch of DNA that exists in versions; selfish means a version passed on more than its fair share. |
| 1:20 | toy-world | Two hundred creatures, each carrying two copies of a gene: a normal version and a driver. |
| 1:55 | brute-force | Baseline with fair inheritance: the driver stays near half and nothing is selected. |
| 2:30 | demo-sim | The driver gets into sixty percent of offspring instead of fifty; run it. |
| 3:10 | viewer-turn | Pause: the driver starts at ten percent; does it take over, stay put, or level off? |
| 3:40 | demo-sim | Reveal: the driver climbs to most of the population; a fitness cost to carriers sets the limit. |
| 4:20 | caveat | "Selfish" is a metaphor; the gene has no goal, only versions that persist. |
| 4:50 | misconception-defuse | The myth that genes act for the species is set up and broken; the sim needs no group benefit. |
| 5:10 | generalize | Other genes that bias their own transmission, and genes that help relatives, follow the same bookkeeping. |
| 5:30 | recap | Selfish means passed on more than a fair share; the spread is limited by its cost. |
| 5:45 | teaser | Next: the case where the cost and the advantage balance. |

<<<NARRATION
What does it mean for a gene to be selfish? A gene has no mind. It doesn't want anything, and it doesn't plan. So the word has to mean something narrower, and that narrower meaning is what I want to build in this video.

Let's start with what a gene is, for our purposes. A gene is a stretch of DNA, and that stretch can exist in more than one version. Those versions are called alleles. A creature carries two copies of most genes, one from each parent. When it reproduces, each offspring receives one of those two copies. That's the key step. Whichever version gets passed on more often is the one that spreads.

So here's the working definition. A gene is selfish when its version gets into more than its fair share of the next generation. Notice what the definition leaves out. It says nothing about intention, and nothing about what is good for the body the gene sits in. It only says which copies end up in the next round.

Let's build a world to test that. I have a population of two hundred creatures. Each one carries two copies of a gene with two versions, a normal version and a driver. Each offspring gets one of its parent's two copies, chosen at random. With fair inheritance, each copy has a fifty percent chance of being passed on, so the driver's share stays where it started. That's the baseline. Run it. The frequency wobbles from one generation to the next, but it stays near half. Nothing is selected, so nothing changes.

Now let's make the driver selfish. In this version, when a creature carries one driver and one normal copy, the driver gets into sixty percent of its offspring instead of fifty. The rule is small, and it is built to look like a cheat: the driver takes more than its share, mechanically, every time. Run it.

Before you watch the rest, make a prediction. The driver starts at ten percent of the population. Will it take over? Will it stay near ten percent? Or will it level off somewhere in between? Pause the video and choose.

Welcome back. Here's the run. The driver's frequency climbs, and it doesn't stop at a middle level. Within a few dozen generations, most of the population carries it. The change in any single generation is small. A ten-point advantage in transmission, repeated over and over, compounds. That's the same shape we saw in the growth videos: a small rate applied again and again to a changing amount.

But the driver isn't free. In this version, creatures carrying two copies of the driver have fewer viable offspring. As the driver spreads, the population's average fitness falls. Run it again with a higher cost. The driver still rises, but it levels off below full takeover, at the frequency where its gain just cancels its cost. That's an equilibrium, and it comes out of the model, not out of anything I drew into the plot.

Here's the point I want to stress. Nothing in this sim gives the driver a goal. The driver doesn't know it's spreading. What the sim shows is that a version which gets passed on more often will increase in the population, whatever it does. The word selfish is shorthand for that. The gene is selfish in the sense that its copies persist, and that's all the word needs to mean.

One way to see the difference between the gene's view and the creature's view is to ask what each one counts. The creature counts its own offspring and whether they survive. The gene counts how many of its copies exist in the next generation. Both counts are real, and they can point in different directions. The driver in this sim is a case where they do.

There's a common assumption I want to address head on. People often assume that genes act for the good of the species, or for the good of the body they sit in. That assumption is what makes the word feel wrong. But the sim doesn't need either assumption. The driver spreads even though it lowers the average fitness of the population, as long as its own transmission is high enough. The good of the group doesn't enter the bookkeeping at all.

Is this a rare case? Not really. Genes that bias their own transmission have been found in several species, including in the process that produces sperm and eggs. Versions of this kind, sometimes called meiotic drive, have been studied in fruit flies and in mice. My driver is a simple version of that. Other genes spread by helping a relative carry the same version. That is a different route to advantage, but the bookkeeping is the same: which copies get into the next generation.

I should be honest about the metaphor. The phrase "selfish gene" is a metaphor, and it carries the risk that people hear intent in it. I've tried to keep the meaning narrow here. It's about which versions get copied, and nothing else. If you want to test the metaphor itself, build a version where the driver changes nothing about transmission. Its frequency then stays put, which shows that the spread comes from the bias, not from the word.

So, the short version. A gene is selfish when its version is passed on more than its fair share. In a population, that version spreads, and the spread is limited by whatever it costs its carriers. And the word tells you nothing about what the gene wants, because genes don't want anything.

Next time, we'll look at the case where the cost and the advantage balance, and the driver stalls partway through the population. Before then, change the transmission rate in the sim and see how the cost moves the point where it stops.
NARRATION>>>

```json
{
 "format_class": "one definition, one fair baseline, one changed rule",
 "answer_given_upfront": true,
 "hook_type": "question",
 "first_question_frac": 0.0,
 "first_concrete_object_frac": 0.23,
 "first_new_idea_frac": 0.11,
 "first_notation_frac": null,
 "payoff_frac": 0.62,
 "misconception": "planted-myth-defused",
 "brute_force_first": true,
 "examples_count": 3,
 "example_growth": "fair baseline, driver, costly driver, real genes",
 "roadmap": "one-line",
 "viewer_turn": "pause-or-guess",
 "viewer_turn_frac": 0.54,
 "caveat_type": "epistemic",
 "recurring_anchor": "the two-version gene and the two-hundred-creature population",
 "sponsor_frac": null,
 "ending_type": "teaser-next",
 "teaser": true,
 "wpm": 170,
 "median_beat_s": 30,
 "beat_sequence": ["hook","roadmap","definition","toy-world","brute-force","demo-sim","viewer-turn","demo-sim","caveat","misconception-defuse","generalize","recap","teaser"],
 "top5_moves": ["minimal-definition-then-refine","toy-world","brute-force-first","simulation-as-argument","honest-caveat"],
 "absent3_moves": ["humor","story","running-character"]
}
```
