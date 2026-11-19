# 3Blue1Brown held-out summary (Basel d-o3eB9sfls, LLM overview LPZh9BOjkQs)

**Scores (arc / recall / precision / pacing / voice / overall).** Basel 2/3/2/2/3/2. LLM overview 3/3/3/2/3/3. Hit rates: Basel 6 hit, 6 near, 5 miss of 17 (35% strict, 53% weighted). LLM 8 hit, 4 near, 3 miss of 15 (53% strict, 67% weighted), but several LLM hits look recalled (the torn-script hook, the exact compute figure, the bank example), so the real figure is lower. Both generators reported vague recall; the LLM script shows more than that.

## Recurring gaps
1. **The report has no conditioning axis.** It describes one long-form arc (hook, roadmap, brute force, wall, notation late, callback, teaser). Basel (17 min, answer stated in the hook) skipped brute force and the wall and ended on credits. The LLM overview (8 min) dropped roadmap, recap, callback and notation entirely. In both, the generator applied the full furniture and was wrong.
2. **Beat density and timing are unmodelled.** Basel's first idea came 2-3.5 minutes earlier than predicted. LLM mid-video beats came about 100 s earlier, with about twice the predicted idea density at the same speech rate (164 wpm). This supports principle 8 as idea-rate pacing, but shows idea rate can swing 2x by format.
3. **Notation rule is a fitted artefact.** "First symbol at 64-80%" fails: Basel's first formula is a lemma at about 37%, and sums stay verbal.
4. **Presenter-led proof structure is missing.** Claim-then-justify for each lemma, three-time iteration then limit, voiced objection ("but wait"), post-payoff awe beat. The inventor headline is overgeneralised for these.
5. **Endings are overpredicted.** Callback plus teaser appeared in neither; Basel ended on the algebra and credits, the overview on a choice of follow-ups.

## Strongest proposed rules, ranked
1. Duration/format gate: under 10 minutes, drop roadmap, recap, callback, notation; about 20-25 s per beat (LLM, whole video).
2. Result-given proofs: skip numerics and wall; first object by about 1:30 (Basel 1:24).
3. Claim, then justify within 60-100 s, plus an optional second proof and link (Basel 1:56-3:38, 5:45-8:28).
4. Iterate a construction exactly three times with "one more step", then jump to the limit (Basel 9:18-13:16).
5. Two-stage payoff with voiced objection and an awe beat (Basel 14:24-16:35).
6. Magnitude-guess quiz near 40% of runtime (LLM 3:19).
7. Ending conditional on standalone result vs series installment/author (Basel 16:35, LLM 7:08).
8. Notation tied to a completed picture, not to a runtime fraction (Basel 6:17).

## Most wrong or vague report sections
- Section 2 arc and section 5 (stepping stone, hope, undercut): wrong as defaults for proof tours.
- Section 3 move table: gives frequencies without triggers or durations (inline-quiz, roadmap, callback, brute-force).
- Notation guidance in section 1: vague, and the interpolated threshold failed.
- Section 4 principle 8: needs idea-rate numbers per format.

## Verdict
The hypothesis generalises weakly to the voice, the physical-object-first habit, the honest caveat and the teaser. Four of five structural calls on the overview held (no notation, no brute force, scene hook, teaser end), though most of its beat order is dictated by subject. It does not generalise on arc order, timing, endings or the inventor framing for the Basel proof. Both videos are cases the training set lacked (a stated-answer proof tour and a short overview), so the failures are mostly missing conditions, not wrong core beliefs. Adding the format gate and the proof-tour rules should lift both videos, but one more held-out round on a long-form non-math 3Blue1Brown video is needed to separate real improvement from tuning to these two cases.
