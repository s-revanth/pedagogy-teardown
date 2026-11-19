# Round 3 results: does the teardown help a model write a channel's script?

All scoring is deterministic code (`tools/evaluate.py`, `tools/analyze.py`, `tools/real_vs_real.py`). No LLM judge was used. The numbers are in `eval/results.json`, `eval/analysis.json`, `eval/per_feature.json` and `eval/real_vs_real.json`.

## Setup
- **Split.** We downloaded the channel corpus with yt-dlp. The frozen test set is 81 videos across 9 channels: up to 10 per channel, minus caption-quality failures. Primer has 8, Reducible 5 and Lague 8. Training statistics are fitted on the rest of the corpus, with test ids excluded.
- **Three conditions.** The same generator (Haiku 5.5, high effort) wrote all 243 scripts. Each condition gave it different inputs:
  - **base:** title plus taxonomy.
  - **v1:** base plus the round-1 channel report.
  - **v2:** v1 plus the rule-ID rulebook (`deep/policy/<ch>.md`) and training exemplars.
- **What is measured.** The same feature code runs on the generated narration and on the real transcript:
  - pronoun rates, number rate, hedge and example cues, question rate, sentence length;
  - sponsor, teaser, roadmap and recap switches;
  - slot predictions.
- **Error unit.** Error is |script − real| / channel IQR, averaged over features.
- **Baselines.**
  - **Constant:** output the channel's training median for every feature.
  - **Real-vs-real (the fair bar):** how far a random real training video from the same channel sits from the test video. It uses up to 30 per channel, seed 0.
- **Statistics.** All comparisons are paired on the same videos. We report the sign test and a bootstrap 95% CI (5,000 draws).

## Headline numbers

| | base | v1 | v2 |
|---|---|---|---|
| Text fidelity error (lower is better) | 1.11 | 1.15 | **0.97** |
| Features inside the channel's train p25–p75 | 37% | 37% | **65%** |
| Sponsor/teaser/roadmap/recap switch agreement | 66% | 62% | **77%** |
| Hook type vs blind labels (n=34) | 24% | 21% | 21% |
| Ending type vs blind labels | 6% | 21% | 24% |
| Answer-given-upfront vs labels | 47% | 65% | 65% |

Baselines: the constant median scores 0.81. Real-vs-real scores 1.15. The majority label scores 44% for hook (premise-claim), 24% for ending (impact-coda) and 76% for answer-upfront (false).

Paired tests (81 videos):
- **v2 vs base.** Fidelity improves by −0.14 (CI −0.22 to −0.05; 60 better, 21 worse; p<0.001). In-band rises by +28 points. Switch agreement rises by +10 points (p=0.001).
- **v1 vs base.** No significant difference on any metric. The fidelity change is +0.05 (CI −0.01 to +0.10).
- **v2 vs real-vs-real.** v2 is better by −0.18 (67 of 81 videos; p<0.001). Base and v1 sit at the real-vs-real level.
- **Every condition vs constant median.** All are worse. v2 is +0.16 worse (21 of 81 better).
- **Without recall.** The same pattern holds on the videos the generator marked recall "none":
  - v2 vs base: −0.16, p=0.003.
  - v1 vs base: +0.10 (worse).

## What this means
1. **The rulebook (v2) works and the prose report (v1) does not.** The round-1 reports add no measurable signal over a model's own prior about the channel, and on the videos it had not seen they make text fidelity slightly worse. The rule IDs, numeric bands, default switches and exemplars move scripts significantly closer to the real video.
2. **v2 scripts resemble the target more than another real episode does.** That is the right bar for a single sample. They still lose to the constant median, because one sample has its own variance. Beating the median would require predicting how a particular video differs from the channel average, and no condition does that. The rules describe the channel but contain nothing that is specific to one video.
3. **Structural slot predictions are below the majority baseline in every condition.** This is the biggest gap.
   - **Hooks.** Models over-predict "question" hooks: 13–20 of 34, against 5 real. The real hooks are mostly premise-claims (15/34). v2 swaps that error for over-predicting "answer-stated" (10 of 34).
   - **Endings.** Base and v1 predict a "hook-callback" ending 19–20 times. That never occurs in the labelled real videos (0/34), which end on impact-codas, phrase-mirrors, credits after the result, and teasers. v2 over-corrects to "phrase-mirror" (21 predicted, 7 real).
   - The reports teach the question/callback pattern, and it is wrong.

## Per channel (fidelity error; real-vs-real is the fair bar)

| channel | n | real-vs-real | base | v1 | v2 |
|---|---|---|---|---|---|
| 3blue1brown | 10 | 1.01 | 1.24 | 1.30 | 1.33 ✗ |
| CGPGrey | 10 | 1.06 | 0.88 | 0.89 | 0.79 |
| OverSimplified | 10 | 1.94 | 1.65 | 1.78 | 1.55 |
| PrimerBlobs | 8 | 1.50 | 1.69 | 1.92 | 1.51 |
| Reducible | 5 | 1.03 | 1.13 | 1.40 | 0.67 |
| SebastianLague | 8 | 1.05 | 1.37 | 1.28 | 1.07 |
| Vsauce | 10 | 0.76 | 0.69 | 0.58 | 0.54 |
| kurzgesagt | 10 | 0.95 | 0.71 | 0.79 | 0.58 |
| veritasium | 10 | 1.04 | 0.78 | 0.71 | 0.66 |

3Blue1Brown is the one channel where v2 hurts: in-band falls from 25% to 15%. Its rulebook's numeric bands mix short lessons with long proofs, and the generated narration sits outside them.

## Rule gap map (v2, 81 traces)
- **Self-reported compliance is unreliable.** There are 74 numeric-rule claims of "applied" that measurement shows failed. The teaser default (B2) fails 15 times and the roadmap default (B3) 14 times.
- **The numeric bands describe the channel, not the video.** Only 48% of real test values fall inside the p25–p75 band. That is about chance by construction, so a band says nothing about which side a given video is on.
- **The worst numeric rules:**
  - Sentence length: the script complies 46% of the time. Every condition writes sentences that are too short (bias −0.5 to −0.7 IQR).
  - Number rate: the script complies 46%. v2 overshoots, with dates and figures.
  - Hedges: 57%.
  - "I/me": 56%. Base and v1 under-use first person, by −0.66 IQR.
- **Pronoun bias.** "We" and "you" are under-used without the rulebook, at −0.69 and −0.30 IQR for base. v2 halves that bias.
- **The universal rules (U1–U11) and the channel and correction rules (C, D) cannot be measured.** They are "applied" or "n/a" on the generator's word alone, and none was ever marked broken except U6, beat length (6%). They need operational tests before they count as evidence.
- **Length versus pace conflict.** The 1,800-word cap makes N2 (wpm over 10 minutes) impossible for long videos. Lague, Veritasium and Kurzgesagt marked it broken by construction.

## What to change next (round 4)
1. **Fix the structural priors.** Add explicit hook and ending base rates per channel to the rulebook, the same way B-switches are defined. Ban the "question" hook and "hook-callback" ending as defaults.
2. **Predict the video, not the channel.** Condition the numeric targets on the format class: lesson, proof, devlog, mini-war, explainer. 3B1B and Lague show the class split matters.
3. **Make every U, C and D rule measurable,** or drop it from the trace.
4. **Verify the trace with code.** Run `features.py` inside the generation loop so "applied" can't be claimed falsely.
5. **Drop the prose report from the inputs** (v1 adds nothing) or rewrite it as rules.
6. **Lift the 1,800-word cap for long videos,** or score pace from slots only.

## Caveats
- Base read all of `deep/BRIEF.md`, including the round-1 lens, so it is slightly informed.
- The rulebooks were built before the caption-quality refit. The bands differ slightly from `train_stats.json`.
- v2 mixes rules with exemplars, so their effects can't be separated without an ablation.
- Small channel samples: Primer 8, Reducible 5, Lague 8.
- Recall is self-reported. 42 of 81 base scripts are "vague", but the no-recall subset shows the same result.
- Slot labels are single-annotator hand labels (Claude, blind, n=34), and the majority baseline is computed on the labels themselves, which favours the baseline.
- Text features are stylometric. They do not judge whether the explanation is good, only whether it sounds like the channel.

---

# Round 4 (v3): video-conditioned targets, structure priors, verified checker

Same frozen 81 test videos, same generator (Haiku 5.5, high), same deterministic scorer. One new condition, **v3**, compared paired against base, v1 and v2. Code: `tools/cv_targets.py`, `tools/build_v3.py`, `tools/check.py`, `GEN_BRIEF_v3.md`. Data: `cards/`, `../policy_v3/`, `eval/train_labels.json`.

## What changed, and how each choice was made (training data only)
1. **Per-video numeric targets.** We tested five ways to set targets with leave-one-out on the 1,540 cached training videos. The best was the 20 training videos nearest by upload date plus title words (LOO error 0.692, against 0.735 for the channel median). Duration-matched targets did not help. We applied the winner once to test: 0.778 against 0.81 for the median, better on 50 of 81 videos.
2. **Switch defaults.**
   - Sponsor and teaser come from the nearest neighbours. LOO accuracy for sponsor rose from 0.76 to 0.85.
   - Roadmap and recap come from the channel rate.
3. **Structure priors.**
   - I hand-labelled 106 training videos for hook and ending, mapped from the round-1 analyses with the same definitions as the test labels.
   - Hook default: the channel majority. A question hook is allowed only when the title is itself a question (questions open 8 of 18 such training titles).
   - Ending default: teaser-next for series titles, otherwise the channel majority.
   - Hook-callback and phrase-mirror were merged into one category, phrase-mirror.
4. **Verification instead of self-report.** `check.py` measures the draft with the scoring code against the card. The generator revised until at least 7 targets passed, then pasted the checker's output as its trace.
5. **What was dropped:** the prose report, the U and D rules, and the old trace. The C rules were kept as untraced style notes.
6. **Length** is now duration × target wpm, capped at 2,200 words.

## Test labels grew from 34 to 79
I labelled 47 more test videos blind, from the transcript's head and tail, before any v3 script existed. Five endings are unobservable because the tail is a sponsor read. The round-3 slot results were rescored on 79 labels with callbacks merged, and the conclusions did not change.

## Results (paired, 81 videos)

| | base | v1 | v2 | **v3** | baselines |
|---|---|---|---|---|---|
| Fidelity error ↓ | 1.11 | 1.15 | 0.97 | **0.78** | real episode 1.15 · channel median 0.81 · neighbour targets 0.78 |
| In channel band | 37% | 37% | 65% | **83%** | |
| Switch agreement | 66% | 62% | 77% | **83%** | |
| Hook type (n=79) | 20% | 14% | 23% | **53%** | training-majority per channel 52% |
| Ending type (n=74, callbacks merged) | 18% | 31% | 16% | **36%** | training-majority per channel 32% |
| Answer given up front | 43% | 76% | 65% | **34%** ✗ | majority 89% |

Paired tests:
- **v3 vs v2:** fidelity −0.19 (CI −0.25 to −0.12; 67 better, 14 worse; p<0.001). The no-recall subset agrees: −0.17, 33 to 7.
- **v3 vs a real episode:** better on 78 of 81 videos.
- **v3 vs the channel median:** −0.03 (CI −0.06 to +0.01; 42 better, 39 worse; p=0.82), a tie. For the first time a generated script is not worse than the constant.
- **Per feature:** v3 has the lowest error on all 8 text features. The bias against the training median is near zero for every feature except sentence length (−0.2).

## What it means
1. **Most of the climb came from better targets plus verification.** v3 is roughly level with its own targets: 0.78 against 0.778 for the neighbour-median constant. The generator now hits whatever numbers it is given. Further gains on this metric need targets that know about the specific video, for example topic-driven number density, not better instruction-following.
2. **Structure priors work, but they cap out at the base rate.** Hook accuracy went from 23% to 53%, which is exactly the training-majority level, so the generator learned the prior and nothing beyond it. Endings are slightly above the prior (36% vs 32%). To beat the prior, a model would need to predict when a channel deviates from its default.
3. **New regression: answer given up front.** v3 generators equated a premise-claim hook with stating the answer: 49 of 62 premise-claim scripts set it to true, while 89% of real videos don't give the answer early. The rulebook has to say explicitly that a premise is not the answer.
4. **3Blue1Brown is fixed.** Its fidelity went from 1.33 to 0.80. The neighbour targets separate its lessons from its long proofs, which the date-and-title match does implicitly.

## New gaps found in round 4
- **Tie-break bug.** SebastianLague's training hooks were a three-way tie, and the card picked story-anecdote. Real Lague test hooks are 86% premise-claim, and v3 scored 14% there. Ties should break toward the overall corpus majority.
- **Card conflict.** In some cards the ending default comes from hand labels (teaser-next) while the teaser switch comes from phrase detection (OFF). Agents resolved this by writing teasers that dodge the detector. The two sources should be reconciled.
- **The sentence-length feature is partly a caption artifact.** SebastianLague, Veritasium and Primer have a tail of barely punctuated "manual" captions (p90 of 75, 34 and 36 words per sentence), which inflates their targets. 3Blue1Brown's 24-word median is genuine. Fix: trim captions with very long sentences before fitting.
- **Goodhart effects.** Agents added semicolons to stretch sentences, wrote teasers that avoid the detected phrases, and two read `features.py`. The improvement on the real test transcript is genuine, but in-band (83%) is partly gamed and should not be read as quality.
- **Corpus contamination.** At least one CGPGrey "exemplar" (C25qzDhGLx8) contains another narrator. Channel corpora need speaker filtering.
- **Protocol slips (disclosed by the agents).** Some ran the read-only checker over other channels' files. Two read `features.py` or `check.py`. No test data was exposed by any of this.

## Next (round 5)
1. **Fix the obvious bugs:** the tie-break, the answer-upfront definition, and the switch/ending reconciliation.
2. **Predict deviations from the prior.** Train a small classifier from title and topic to hook and ending on the 106 training labels, and check whether it beats the majority by LOO before using it.
3. **Topic-aware targets.** Number rate and example rate depend on the topic, so add title-topic features to the neighbour search.
4. **Clean the targets.** Trim captions with unpunctuated sentences and filter non-channel speakers out of the corpus.
5. **Score what the stylometry misses.** Add a measurable content check, such as a beat-sequence edit distance against hand-labelled beats for a sample, so the metric isn't just style.

## Caveats (round 4)
- v3 bundles six changes, so there is no ablation of which change helped.
- The hook and ending labels for training and the second test batch come from one annotator (me). Training labels were mapped from round-1 analyses, not from transcripts.
- The v3 narrations are longer (2,200-word cap against 1,800). Rate features are length-normalised, but this is still a difference between conditions.
- The 2,200-word cap still binds on videos over about 13 minutes.
