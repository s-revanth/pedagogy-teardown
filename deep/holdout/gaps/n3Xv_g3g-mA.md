# Gap analysis: Kurzgesagt, Loneliness (n3Xv_g3g-mA), 786 s

Inputs compared: `scripts/n3Xv_g3g-mA.md` (blind prediction) against `compact/n3Xv_g3g-mA.txt` (real, manual captions). Hypothesis under test: `deep/reports/kurzgesagt.md`.

**Out-of-distribution flag.** The 12 training videos are all physical, biological or cosmological systems. This is a psychology and self-help piece, so every miss below has to be read as either "the report is wrong" or "the report was never fitted to this topic type". I label that explicitly with `topic-conditional`. Speech ends at 10:46 (the last caption is a giggle); the final ~2:20 of the 786 s is uncaptioned, probably outro or credits, which I could not verify. The generator padded to the full 13:07 and so over-allocated by about 2 minutes.

One real quote (under 15 words): at 0:53, "If you feel lonely, you are lonely."

## 1. Real beat sheet

| Time | Level | Tags | Paraphrase |
|---|---|---|---|
| 0:00 | H | hook-assertion, second-person | Everyone gets lonely now and then (lunch table, new city, empty weekend), but for millions it has turned chronic. |
| 0:17 | N | benchmark, stats | Survey figures: 60% of UK 18-34s and 46% of all Americans feel lonely often. Paradox stated at 0:34: most connected era, yet unprecedented isolation. |
| 0:34 | N | misconception-first, define-by-contrast | Lonely is not alone: bliss alone, misery in company; purely subjective (the 0:53 quote). |
| 0:53 | N | misconception-first | Stereotype that lonely people lack social skills; population studies show skills barely matter for adults; money, fame, looks do not protect either. |
| 1:23 | B | analogy | Loneliness is a bodily function like hunger; hunger directs attention to physical needs, loneliness to social needs. The only analogy in the video. |
| 1:43 | N | story, agency | Evolution: cooperation rewarded; you were born into a group of 50-150; alone meant death. |
| 2:35 | N | agency, antithesis-aphorism | Worst ancient threat was exclusion; social pain evolved as an early-warning system; those who felt rejection more sharply stayed in the tribe. |
| 3:13 | N | story (macro-history) | Why now: Renaissance individualism, Protestant responsibility, factories, urban mobility; one dated stat, close friends fell from 3 to 2 (1985-2011). |
| 4:28 | H | second-person, story | Most people slide into chronic loneliness by accident: work, kids, streaming; friends are the cheapest thing to drop. |
| 5:04 | N | benchmark, stakes | Bodies unchanged for 50,000 years; chronic loneliness stress ages you faster, worsens cancer, Alzheimer's and immunity; twice as deadly as obesity, like a pack of cigarettes a day. |
| 5:37 | N | agency, mechanism | Social and physical pain share brain pathways; chronic loneliness puts the brain in self-preservation mode and it sees danger everywhere. |
| 6:10 | N | mechanism, aphorism | Lonely brains pay more attention to others but read them worse; face recognition drifts so neutral faces look hostile; you turn colder than you are. |
| 7:02 | I | rule-list (loop), visible-repetition | The vicious cycle in five linked steps from isolation to tension, negative attention, negative thoughts, avoidance, more isolation. |
| 7:36 | N | story | Concrete signs (sitting far away, ignoring calls, declining invitations until they stop); the self-story becomes true; can end in depression. |
| 8:09 | N | advice step 1 | Accept that loneliness is normal and universal; you cannot will a feeling away but you can remove its cause. |
| 8:27 | N | inline-quiz-lite, second-person | Self-audit of attention: a run of questions about whether you over-read a colleague's tone. |
| 9:02 | N | inline-quiz-lite | Self-audit of thoughts: do you assume the worst and pre-decide how the room will go? |
| 9:36 | N | inline-quiz-lite | Self-audit of behaviour: do you avoid people, decline invitations, push others away first? |
| 9:52 | N | honest-caveat (safety) | On-screen legal disclaimer: introspection may not be enough; seek professional help, a sign of courage not weakness. |
| 10:10 | N | generalize, zoom-out | Individual problem or public-health crisis, it deserves more attention; no gadget meets the need for connection; we should build our human world around it. |

Speech rate: 1,577 words over ~10:46, about 146 wpm, slowest in statistic- and history-heavy stretches (3:13-5:21, ~126-143 wpm).

## 2. Prediction scorecard (script section 4)

| # | Prediction | Predicted | Actual | Verdict |
|---|---|---|---|---|
| P1 | First question | 0:30-0:50, direct "how can this be" | No question in the hook. First questions are the self-audit at 8:27 | miss |
| P2 | First notation | none | None; numbers only | hit |
| P3 | Misconception | yes, alone vs lonely (1:25-2:10), second one weakness or modern-only | Alone vs lonely at 0:34; social-skills stereotype at 0:53 (type matches "personal failing") | hit (50 s early, second one 7 min early) |
| P4 | Brute-force-first | no | None | hit |
| P5a | Examples | ~3: running person, evolution scene, numbers | No running person; instead lunch/new city/weekend (0:00), tribe (2:00), history (3:34), survey figures, concrete cycle behaviours (7:36) | near |
| P5b | Growth | individual > population > city design | Individual (0:00) > population stats (0:17) > ancestors > society history > body > individual advice > society (10:10) | near |
| P5c | Analogy | hunger sustained, junk food second | Hunger once (1:23) and never reused; no junk food | miss |
| P6 | Hook type | hook-paradox as a question | Relatable assertion list, then stats, then paradox statement at 0:34 | near |
| P7 | Ending | callback to person/window, warm line, credits, no teaser | Safety caveat > society reframe > closing thought that echoes the "most connected" hook; no person, no credits captioned, no teaser | near |
| M1 | hook-paradox/question | confident | Paradox present but at 0:34, as a statement | near |
| M2 | analogy | confident | 1:23 | hit |
| M3 | story | confident | 1:43 evolution; 3:13 history; 4:28 and 7:36 | hit |
| M4 | honest-caveat | confident | Only a safety caveat (9:52); no epistemic hedge on health claims (5:21 states them flatly) | near |
| M5 | callback-to-hook | confident | Thematic echo of 0:34 at 10:28; no return to a scene or question | near |
| bonus | misconception-first (close sixth) | | 0:34, 0:53 | hit |

Hit rate: 5 hit, 7 near, 2 miss of 14. Strict 36%; weighted 61%.

Beat-level checks beyond section 4:
- Hit: evolution as survival (1:43-3:13); social pain shares pain circuitry (5:37); hypervigilance and misread faces (6:10-6:44); a vicious cycle (7:02); health stakes benchmarked to obesity and smoking (5:21-5:37); stakes placed before advice (advice at 8:09); professional-help line (9:52); mismatch of ancestral brain and modern world (5:04); society-level close (10:10).
- Miss (false positives): named running character; roadmap (0:40); gap-gauge definition (real definition is "purely subjective"); short-term-works template then escalation (4:15); correlational caveat (7:15); world-map data; fast-food analogy and social-media section; three behavioural action rules (reach out, give, join); voiced "that's exhausting" objection; virtuous-spiral reversal; city design; ball-tossing study; credits.

## 3. Structural alignment

Predicted arc: city + Mia hook > roadmap + gap definition > alone vs lonely > evolution/hunger > mechanism > template escalation > spiral trap > health stakes > correlation caveat > weakness misconception > fast-food analogy > action rules > caveat + society > window callback.
Real arc: relatable assertion + stats > paradox > two stereotype-breakers > hunger anchor > evolution and social pain > history of why-now > health stakes > brain mechanism > loop > normalisation > three-part self-audit > referral caveat > society zoom-out.

- Predicted and present: misconception (alone vs lonely), evolution, hunger analogy, social-pain mechanism, health benchmarks, spiral, stakes before advice, professional help, society-level close, no notation, no brute force.
- Predicted but absent: Mia, roadmap, gap definition, template escalation, correlational caveat, fast-food analogy, behavioural action rules, objection beat, virtuous spiral, callback scene, credits.
- Present but unpredicted: stats-as-hook (0:17); misconception 2 within 20 s of misconception 1; macro-history chain (3:13-4:28); accidental-slide story (4:28); face-recognition mechanism; five-step loop; the self-audit mirroring the loop (attention, thoughts, behaviour); normalisation first (8:09); on-screen disclaimer; you-as-ancestor second person (2:00); aphorisms (2:17, 6:10, 0:53).

Timing drift (absolute; fraction of captioned length 10:46 in brackets):
| Moment | Predicted | Actual | Drift |
|---|---|---|---|
| Hook | 0:00 | 0:00 | 0 |
| First new idea (definition/misconception) | 1:25 [11% of 13:07] | 0:34 [5%] | -51 s |
| Main mechanism / spiral | 5:10 | 5:37 to 7:02 | +27 s to +112 s |
| Advice (payoff) | 10:20 [79%] | 8:09 [76%] | -131 s absolute, -3 pts relative |
| Ending | 12:25 [95%] | 10:10 [94%] | -135 s absolute, -1 pt relative |

Once rescaled to the captioned length, the second-half timing of the prediction matches; the front is compressed (misconceptions and analogy arrive ~50 s early). The absolute drift is mostly a generator artefact (it filled 13:07 with speech; the real video has about 2:20 without captions).

## 4. Gap taxonomy

| Miss | Class | Why |
|---|---|---|
| Statistics-led hook, relatable list before paradox; no question | topic-conditional | Emotional topic begins from shared experience then a survey benchmark; the report's hooks are what-ifs, paradoxes and quantities. |
| Misconceptions first, doing the definitional work | topic-conditional | Report arc puts misconception after mechanism (step 5). For a lay concept the viewer already has theories about, the video defines by contrast within the first minute, twice. |
| One analogy only; hunger not sustained | topic-conditional | Report says analogy 12/12 and cites sustained metaphors (war, heist). Here a single bodily-function anchor (1:23), then literal science. The generator followed the report faithfully; the report didn't say when not to. |
| No running character | underspecified | Report mentions second-person-role (Egg) only; the generator invented a named avatar. Real video uses unnamed "you" and "your ancestors" (2:00-2:35). The report doesn't say when to pick which. |
| No roadmap | wrong-rule | The arc lists scope/roadmap; this video has none. Roadmap is optional, tied to scale-ladder or multi-part topics. |
| No epistemic caveats; one safety caveat | wrong-rule (for this topic) | Report claims honest-caveat 10/12 and arc step; here health stats at 5:21-5:37 are stated flatly. The caveat is a referral line (9:52). The report doesn't type caveats. |
| Advice is a self-audit mapped onto the loop's nodes | missing-rule | Report has "stakes before advice" but nothing on the shape of advice. Real advice mirrors the diagnosed cycle: attention (8:27), thoughts (9:02), behaviour (9:36). |
| Self-audit questions, viewer directed to introspect for ~85 s | wrong-rule | Report section 6 says no inline quizzes or learner response. This is a 20-question run addressed to the viewer. |
| Macro-history chain as the why-now answer | missing-rule | Story is in the report but not "resolve a modern paradox with a dated causal chain". |
| No short-term-works template, no trap | generator-error | The generator mapped principles 3 and 6 onto a topic that has no repeated template. Not counted against the report. |
| Callback is thematic not scene-based | underspecified | Same issue as the Peto video. |
| No credits in transcript | underspecified | No year/era field to know whether credits are expected. |
| Concise aphorisms | voice/craft | Short antithesis lines recur (2:17, 6:10, 0:53). |

## 5. Overfit check

- "Roadmap 6/12": absent here (0/2 with Peto only a mini-roadmap).
- "Commit-to-answer 9/12": here advice is given, but no single answer is committed to; the video ends on a reframe.
- "Analogy 12/12 and sustained metaphors": one analogy, one time.
- "Callback-to-hook 10/12" and "every video ends by cashing in its opening hook": this ending is thematic only.
- "Retire fears with benchmarks": the benchmarks here amplify stakes (obesity, cigarettes at 5:21-5:37) rather than retire anything.
- "Sponsor/credit 8/12": none captioned.
- "Flat at ~170 wpm": 146 wpm here, with the slowest stretches on dense statistics.
- "No inline quizzes or learner response": contradicted by 8:27-9:52.
- "No interfaces": holds, but the five-step loop at 7:02 is a rule-list used as an interface, which the report doesn't list for this channel.
- Holds: agency before mechanism (social pain as an evolved warning, 2:35; brain switching to self-protection at 5:53), stakes before advice, notation almost absent, dependency order (why we have it, then why it hurts, then what to do).

## 6. Proposed rule changes

1. **Topic-type switch for psychology/self-help (channel-specific, topic-conditional).** Trigger: topic is an emotion or behaviour the viewer experiences. Action: hook = 3 relatable micro-situations in 12 s (0:00-0:17), then 2 survey figures (0:17-0:34), then the paradox as a statement; two stereotype-breakers each under 25 s, using them as the definition (0:34-1:23); at most 1 analogy (body-function anchor at 1:23); second person as ancestor, no named character (2:00-2:35).
2. **Advice mirrors the loop (likely universal).** Trigger: a cycle with N nodes has been diagnosed (5 nodes, 7:02-7:36). Action: give one question set per node, 4-5 questions and ~20-30 s each (attention 8:27, thoughts 9:02, behaviour 9:36), preceded by one normalising line (8:09) and followed by a referral line (9:52).
3. **Typed caveats (channel-specific).** Trigger: choose by topic. Open-science question: epistemic caveat after each candidate, three per video (Peto 3:50, 4:10, 6:29). Mental-health advice: one safety referral at 90% of captioned length framed as strength (9:52), and state headline epidemiology with a named study type but no inline hedge (5:21).
4. **Why-now history chain (likely universal for societal-trend topics).** Trigger: the hook states a modern paradox. Action: resolve it with a 3-link dated causal chain plus one trend stat, 60-75 s, before the stakes beat (3:13-4:28).
5. **Misconception-first as definition (cross-channel).** Trigger: the viewer holds a folk theory (loneliness equals solitude). Action: put the contrast in the first 60 s (0:34) and treat it as the minimal definition; when the report's arc says "definition then misconception", swap the order.
6. **Closing-phrase mirror (likely universal).** Trigger: last beat. Action: reuse a key phrase from the first 40 s with a stronger sense (0:34 vs 10:28) rather than returning to a scene; no avatar needed.

## 7. Scores (1-5)

| Dimension | Score | Justification |
|---|---|---|
| Arc fidelity | 3 | Same broad order (stakes, mechanism, loop, advice, caveat, society) but misconceptions and analogy arrive early, a history chain appears, and the ending is not a callback. |
| Move-inventory recall | 3 | Got misconception, analogy, evolution, social pain, benchmarks, loop, safety caveat, society close; missed stats hook, define-by-contrast, history chain, self-audit, loop-mirrored advice. |
| Move precision | 2 | Roughly half of the predicted moves are absent (running character, roadmap, template escalation, correlational caveat, fast-food, behavioural rules, callback scene). |
| Pacing/timing | 2 | Relative timing is right in the second half, but the front is 50 s late, the generator over-wrote by 18%, and speech rate is 146 not ~165 wpm. |
| Voice | 2 | Real voice is clinical, statistic-led and second-person; the script is warm, narrative and built on a named character. |
| Could the hypothesis regenerate this video | 2 | The report has no mechanism for emotion or behaviour topics, so the skeleton survives but content choices (hook, analogy count, advice, ending) do not. |

## 8. What the report would need to condition on topic type

1. A `topic_type` field per training video (physical system, scale ladder, bio-mechanism, open paradox, human psychology/self-help, historical story) and per-type values for: hook form, number of analogies, stand-in kind (agent or object vs ancestral you), evidence kind (benchmark vs survey statistic), advice presence and shape, caveat type, ending type.
2. At least 4-6 psychology or self-help videos from the same channel and era, so that each topic-type rule has n of at least 4 instead of 0.
3. A `question_status` flag (solved vs open) to switch commit-to-answer on or off.
4. Publish year or era, to test whether credits, sponsor reads, brand idents and speech rate depend on date.
5. A voice section with sentence-level rules (aphorism rate, address person, humour density).
