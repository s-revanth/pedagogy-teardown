# Channel report + storyboard brief

Inputs: every `analyses/<id>.json` and `.md` for ONE channel (ids from `tracker.csv`, column channel), plus `BRIEF.md` (the lens) and `../pedagogy-teardown.md` (round-1 findings). Read all of them for your channel. Paraphrase; quotes only as already recorded in the analyses.

## Output 1: `reports/<channel>.md` (1500-3000 words)
1. Bottom line: how this channel teaches, in 3 sentences.
2. Signature arc: the recurring structure across videos (with which videos follow it, timestamps).
3. Move frequency table: move | videos using it (n/12) | best example (video, m:ss).
4. Principle scorecard 1-13: verdict + evidence across videos (count confirmed/partly/contradicted).
5. New principles / theories: 3-6 NEW generalisable claims about pedagogy this channel reveals, each with evidence from >=2 videos and a falsifiable form ("if X then learners Y").
6. What this channel does badly or never does.
7. Velocity translation: concrete changes (scene builder, voice/beat script, orchestrator rules, playbooks, learner model, ghost hands, evals).
8. Per-video one-liners table (title, id, theory).

## Output 2: `storyboards/<channel>.html`
A single self-contained HTML page (inline CSS/JS only, no external requests except Google Fonts optional) that tells "How <Channel> teaches" as a STORYBOARD:
- A horizontal sequence of 6-10 storyboard panels = the channel's generalised lesson arc (e.g. Hook -> Misconception -> Toy world -> ... -> Callback). Each panel: big step name, a small hand-built SVG/CSS sketch of what's on screen, what the narrator is doing, the move tags, and 2 real examples (video + m:ss).
- Below: a move-frequency bar list (CSS bars), the principle scorecard as a compact grid (colour = verdict, with text label too), and the new theories as cards.
- Title `<title>` 2-4 words. Colours as CSS vars on :root with a dark-mode variant under @media (prefers-color-scheme: dark). Body has explicit background. Works at 360px wide (panels scroll horizontally with snap; no page-level horizontal scroll). Distinct visual personality per channel is welcome, but readable.
Write only these two files.
