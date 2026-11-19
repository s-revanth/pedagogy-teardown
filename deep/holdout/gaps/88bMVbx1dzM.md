# Gap analysis: Veritasium, "Can You Keep Zooming In Infinitely?" (88bMVbx1dzM, 21:29)

Scope notes. The generator guessed the topic from the title (physical zoom, Mandelbrot, computer precision). The real video is a history of how the electron microscope came to resolve single atoms (de Broglie, Ruska, Scherzer's aberration limit, Crewe, then the Urban/Haider/Rose corrector), bookended by an on-site lab visit. Per instruction, topic mismatch is counted as `generator-error` and is NOT charged to the hypothesis; the focus is whether the pedagogical structure was predicted. Section numbering: the script's explicit predictions are in its section 4 (the brief says 5). Hit = 1, near = 0.5, miss = 0.

## 1. Real beat sheet

| m:ss | Lvl | Tags | Paraphrase |
|---|---|---|---|
| 0:00 | H | hook-paradox, spectacle-first, act-it-out | A 3 mm metal chip is zoomed 1,000x, 100,000x, 50,000,000x until single atoms show as blobs. |
| 0:18 | H | story, honest-caveat | Seen on a visit to Sydney; direct imaging of atoms was thought impossible until about 30 years ago; shielded, costly rooms. |
| 0:34 | B | hook-question, minimal-definition-then-refine | Why is it hard to see atoms? Light wavelength (380-750 nm) is thousands of times bigger than an atom and bends around it; need a much shorter wavelength. |
| 1:11 | N | story | Electrons are the best candidate; de Broglie 1924: matter has a wavelength. |
| 1:26 | I | notation-after-concept (early) | The wavelength formula stated in words: Planck's constant over momentum. |
| 1:44 | N | expert-dialogue, build-and-verify | In the lab the host quizzes an expert: 300 kV electrons, about 80% of light speed, wavelength 2-3 pm, over 100,000x better than light. |
| 2:17 | N | story, necessity-ladder | Glass cannot bend electrons; Busch proposes a magnetic lens (1926) but never builds it; student Ruska builds one. |
| 2:53 | N | simulation-as-argument, act-it-out | How the coil-and-iron lens works: Lorentz force pushes the electron sideways, then spirals it inward to a focus (3:09-3:40). |
| 3:59 | N | story, minimal-definition-then-refine | 1931 first working electron microscope (TEM); thin sample, transmitted-electron imprint, second lens magnifies it (4:34 names TEM). |
| 4:34 | N | failure-shown, story | Early TEM no better than an optical microscope; Ruska keeps adding lenses; 10,000x by mid-1930s, viruses visible. |
| 5:05 | N | failure-shown, new:wall-as-theorem | Just as it takes off, Scherzer claims an unavoidable flaw; ideal deflection angle graphed against distance from axis (5:23-6:16, new chart). |
| 6:16 | N | simulation-as-argument | Real magnet over-deflects outer rays, so focus smears; named spherical aberration, worse at high magnification. |
| 6:33 | B | generalize-to-other-domains, Home | Every spherical lens (camera, telescope, magnifier) has it. |
| 6:50 | B | Home, minimal-definition-then-refine | The familiar fix: stack a diverging lens with equal and opposite aberration. |
| 7:26 | N | failure-shown, explanation-block | A magnet cannot do that: no single poles, field lines are closed loops (Maxwell), so electrons always cross twice and converge (to 8:24). |
| 8:24 | N | failure-shown | Scherzer's 1936 theorem: no radially symmetric magnetic lens can diverge; resolution progress slows (8:41). |
| 9:00 | N | story | Meanwhile a field ion microscope (1955) gives the first accepted atom picture but only of a needle tip. |
| 9:46 | admin | humor, sponsor | Segue joke from "bombarded with electrons" to spam calls and ads; data-removal sponsor read, about 75 s. |
| 11:00 | N | story, necessity-ladder | Back: Crewe replaces the filament with a field-emission tip, 1000x brighter beam. |
| 11:34 | B | analogy | Pairs it with the scanning idea from CRT televisions; builds a scanning TEM (to 12:22). |
| 12:22 | N | story | Earlier prototype by Ardenne destroyed in WWII; Crewe's 1970 first single-atom image. |
| 12:56 | N | failure-shown | Aberration still caps resolution; Crewe gives up (quote at 13:12). |
| 13:29 | N | honest-caveat | Probe microscopes (stylus) image atoms without lenses but "feel" rather than see. |
| 14:01 | N | new:loophole-in-theorem, design-it-yourself | Scherzer's proof assumes radial symmetry; drop it and the theorem no longer applies, but breaking symmetry breaks the image. |
| 14:18 | N | story, new:underdog | Urban, Haider, Rose: known troublemakers, unfunded, idea seen as crazy. |
| 15:08 | N | simulation-as-argument | Hexapole/octopole/decapole magnets twist the image into a triangular saddle, leaving a weak divergence; a second hexapole untwists it and cancels the aberration (to 15:59). |
| 15:59 | N | expert-dialogue | Expert aside: most thought it infeasible. |
| 16:15 | N | story, new:countdown | Two months of funding left; lens only on a drawing board; test fails; 24 h wait; 2 a.m. it stabilises (to 17:04). |
| 17:04 | N | payoff | Clear atoms; resolution 0.13 nm; before and after image (17:22). |
| 17:38 | N | story | Conference: first in a back room, then crowds queue to see the images (to 18:09). |
| 18:09 | H/N | act-it-out, build-and-verify, expert-dialogue | Back in the Sydney lab: sample holder, alignment, tilting along a crystal direction, focus until the edge is sharp, atoms appear (to 19:58). |
| 19:58 | N | payoff | Host reacts to seeing atoms live. |
| 20:13 | N | generalize-to-other-domains | Parallel work on scanning version; 2020 Kavli prize; atom imaging now routine. |
| 20:36 | N | expert-dialogue, generalize-to-other-domains | Expert: aberration correction is a game changer for materials, chemistry, engineering; every university needs one. Ends here, no outro or teaser. |

Metrics: first viewer question 0:34; first formula 1:26 (verbal, one line), first new chart 5:23; misconception: partial (atoms thought unseeable, light cannot do it); brute force: none in the hand-calculation sense; ending: expert significance statement.

## 2. Prediction scorecard (script section 4 plus committed beats)

| # | Prediction | Predicted | Actual | Verdict |
|---|---|---|---|---|
| 1 | First question time | 0:30-0:50 | 0:34 ("why is it so hard to see atoms?") | hit |
| 2 | First notation | about 11:20, nothing earlier | 1:26 formula in words, 5:23 chart | miss |
| 3 | Misconception | yes: "always more detail underneath" | partial: atoms "impossible to see" and "light cannot"; no viewer-held belief stated or defused | miss (generator-error on content) |
| 4 | Brute-force-first | yes: hand iteration, "just use more digits" | none; closest structural analogue is adding more lenses (4:50) and "clever workarounds" (11:17) | miss |
| 5 | Examples and growth | 3-4 worlds plus 2-3 hand runs; growth by world | one subject; about 6 successive instruments (TEM, FIM, STEM, probe, corrected TEM); growth by historical generation | near |
| 6 | Hook type | spectacle zoom plus "would you run out?" question plus vox-pop | spectacle zoom plus "why hard to see atoms?"; no vox-pop | near |
| 7 | Ending | callback to opening image and poll, layered answer, sponsor/teaser | return to the lab, expert significance statement; no poll, no callback to the opening question, no teaser or outro | miss |
| 8 | Sponsor placement | end (21:15); hedge about 7:40 after first wall | 9:46, right after the first big wall, 75 s | near (hedge only) |
| 9 | Five confident moves | hook-paradox, analogy, failure-shown, min-def-then-refine, callback-to-hook | failure-shown strong; min-def present; hook is spectacle not paradox; analogy thin (3 weak); callback absent | near |
| 10 | Commit-to-answer / poll within about 1 min | 0:50 | none anywhere in the video | miss |
| 11 | Roadmap | 1:25 | none; question at 0:34 serves as the only frame | miss |

Hit rate: 1 hit + 4 near + 6 miss = 3.0 / 11 = 27%. Excluding rows that are topic-bound (3, 4, 5 content, 7 poll and three-worlds): rows 1, 2, 6, 8, 9, 10, 11 give 2.5 / 7 = 36%.

## 3. Structural alignment

Predicted arc: spectacle zoom hook -> poll -> roadmap -> real-world ladder of walls (light, electrons, needle) -> caveat -> a second world -> prediction -> failure -> brute force -> clever trick -> verify -> limit -> callback -> sponsor.
Real arc: spectacle zoom hook -> why-question -> wavelength wall -> electrons -> long relay of people each unlocking one piece with a win-then-wall rhythm (Ruska, Scherzer, FIM, Crewe, probes) -> sponsor at the darkest point -> loophole in the theorem -> underdog trio with a funding countdown -> payoff -> crowd vindication -> hands-on lab session -> impact coda.

- Predicted and present: spectacle hook (0:00); question about what stops the zoom (0:34); wavelength wall explained early (0:34, but predicted 3:10); expert-dialogue (1:44, 15:59, 18:09-20:57); necessity ladder (2:17-14:18, stronger and longer than predicted); failure-shown (4:34, 8:24, 12:56, 16:32); minimal-definition (TEM 4:34); honest-caveat in the "feeling not seeing" form (13:45); needle-style probe microscopy (13:29, predicted at 5:10); verify-by-demo (18:09, predicted 18:30 for a different object); mid-video sponsor (hedge).
- Predicted but absent (false positives): vox-pop and commit prompt; roadmap; Planck-length floor; Mandelbrot world and everything after it (about 11 of 21 beats, generator-error); prediction-before-data; design-it-yourself with a lecture of the clever trick; callback to the hook question; sponsor at the end; teaser; humour beat at close.
- Present but unpredicted (false negatives): relay of named people with year and one-line character tags; win-then-wall alternation across five rungs; impossibility theorem followed by a loophole in its assumption (14:01); underdog with a funding deadline and a 2 a.m. success (16:15-17:04); crowd vindication scene (17:38); lab bookend with host and expert as 20% of runtime; impact coda (20:13-20:57); a topical pun segue into the sponsor (9:46); an early one-line formula with numbers plugged in at once (1:26-1:59); CRT analogy as a borrowed familiar technology (11:34).

Timing drift: hook 0:00 predicted, 0:00 actual (0). First new idea (a wall): predicted 3:10, actual 0:34 (-2:36). First formula: predicted 11:20, actual 1:26 (-9:54). Payoff: predicted 18:30 (verify the trick), actual 17:04 (clear atoms), content differs, -1:26. Sponsor: predicted 21:15, actual 9:46 (-11:29; hedge 7:40 is +2:06 off). Ending: predicted 20:50 callback, actual 20:36-20:57 expert statement (about 0 on time, different content). Total length matched because the target was given.

## 4. Gap taxonomy

| Miss | Class | Notes |
|---|---|---|
| Entire Mandelbrot / computer-precision / three-worlds structure | generator-error | Title guess. Not charged. |
| Poll plus vox-pop plus roadmap in the first 90 s | generator-error plus overfit | The report itself says the viewer turn is "fake"; the generator inflated it to a rule. Zero instances here and in the sibling video; see section 5. |
| Formula at 1:26 vs predicted 11:20 | topic-conditional | Report says notation is absent or late (6:18 or later) but gives no condition. A one-line quantitative relation that answers "why can't we" appears at once in a physics-mechanism video, then is used with numbers within 30 s. |
| Relay of named people, each solving the last person's blocker | underspecified | Report has "story 11/12" and "need-attempt-failure loop" (MiUH) but no dated-handoff structure, no cadence (a rung every 2-3 min), no character tags. |
| Win-then-wall rungs (TEM works, then Scherzer; STEM works, then aberration) | underspecified | The necessity ladder is defined as rejected alternatives; here the rungs are partial wins that expose a deeper wall. |
| Theorem as wall, then break the theorem's assumption (14:01) | missing-rule | No rule for impossibility results. |
| Underdog climax with a deadline and a crowd | underspecified | The loop exists (MiUH 51:27, AF8d); the climax grammar (countdown, failure, overnight wait, success, vindication) is not specified. |
| Lab bookend plus mid-video expert interludes, ending on the expert | underspecified | "expert-dialogue 7/12" cites only pir_. No placement rule. |
| No callback to the opening question, ends on significance | wrong-rule (soft) | Report and its Velocity section say the callback to the hook is placed last; here the video ends on impact, with only a location callback. |
| Sponsor at 46% runtime, at a wall, with a pun segue | underspecified | Report says only "between last idea and callback in several". |
| Sparse analogy: three, all borrowed from technology or the expert | wrong-rule (soft) | "analogy 11/12" and "one plain analogy anchor" overstate; the anchor here is a physical demonstration and a diagram animation. |
| Pun segue into the sponsor; deadpan emotional restraint at the 2 a.m. moment | voice/craft | Not captured. |

## 5. Overfit check

- Commit-to-answer 9/12 and roadmap 9/12: absent in both held-out videos, so the counts are probably inflated by loose tagging of "what do you think" lines.
- "Misconception-first 9/12": here there is only a soft planted impossibility ("thought impossible", 0:18), not a held belief that is then broken.
- "Callback to the hook placed last" and "teaser or sponsor after it": not true here.
- "Notation absent or very late (6:18+)": contradicted at 1:26 for a physics relation.
- "Analogy then rigor" and "one plain analogy": weak here; the explanation runs on diagrams and named history.
- Sponsor "between last idea and callback": not true here (mid-video).
- Holds up: hook with an odd object (0:00), question within the first minute (0:34), obstacle course with people failing, failure-shown, "no real viewer turn", expert dialogue.

## 6. Proposed rule changes

1. **Win-then-wall relay ladder.** Trigger: the topic has a history of incremental invention. Action: build 4-6 rungs; each rung is one named person plus year plus one-line character tag, solves the previous blocker, and ends in a new wall; rung length 2-3 min; the final rung carries a deadline or funding countdown and a visible before/after image. Evidence: 1:11, 2:17, 4:34, 5:05, 9:00, 11:00, 12:56, 14:18, 16:15, 17:04. Channel-specific, likely universal for history-of-technology explainers.
2. **Impossibility-theorem loophole.** Trigger: a wall is stated as a proved theorem. Action: spend 30-60 s naming the theorem's hidden assumption, then make the protagonists break it on purpose; give the explanation block of why the theorem holds before it (7:26-8:41), the loophole at 14:01, and the mechanism animation after (15:08). Universal.
3. **Notation timing by formula type.** Trigger: the first obstacle is quantitative. Action: state the one governing relation within 90 s of the hook, plug numbers in within 30 s (1:26-1:59); reserve "late notation" for symbol systems, which come after 10 min. Evidence: 1:26 here, 12:13 and 15:35 in the sibling maths video. Channel-specific.
4. **Site visit as a frame.** Trigger: an instrument or lab exists. Action: open on a location shot within 20 s, interleave 2-3 short expert exchanges (about 30 s each) during the physics, finish with a hands-on session of 2-3 min and end on the expert's statement of significance. Evidence: 0:18, 1:44, 16:15, 18:09-20:57. Channel-specific.
5. **Sponsor at a wall with a topical segue.** Trigger: a sponsor read exists. Action: place at the first big wall around 45% of runtime, open with a joke tied to the preceding line (9:46), read of about 75 s, then return with "back to" plus the topic. Evidence: 9:46-11:00. Channel-specific; HeQX puts it at the end, so position needs a per-era condition.
6. **Delete roadmap and vote as defaults.** Trigger: generator tempted to add roadmap or poll. Action: only add them when the video has 3 or more parallel questions; otherwise use one first question within 60 s. Evidence: 0:34 and none else. Channel-specific.

## 7. Scores (1-5)

- Arc fidelity: 2. The skeleton (spectacle hook, early why-question, ladder of walls, mid sponsor) matches; the second half and ending do not, mostly through topic.
- Move-inventory recall: 4. Nearly every real tag (spectacle, question, failure, min-def, caveat, expert, verify, sponsor, generalise) was in the predicted set; only underdog, loophole and relay were missed.
- Move precision: 2. About half the predicted beats are tied to Mandelbrot and the poll/roadmap, none of which occur.
- Pacing/timing: 2. Walls and formula come far earlier; the sponsor is 11 minutes off.
- Voice: 3. The first-person reflective narrator and "think about it" prompts are absent in the real third-person fast-fact narration with brief host reactions.
- Could the hypothesis regenerate this video: 2 (3 if topic mismatch is excluded). The report gives the ladder idea but not the relay, the loophole, the climax grammar or the lab frame.
