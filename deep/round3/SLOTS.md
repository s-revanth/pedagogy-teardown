# Round 3 fixed prediction slots

Every script ends with ONE fenced ```json block holding exactly these keys. Fill every slot with a single value. No hedges such as "none or maybe X". Fractions are of the total runtime (0.0-1.0). Use null only where the slot says null is allowed.

```json
{
 "format_class": "free text: the class/template you chose (e.g. 'proof tour, answer stated', 'devlog', 'mini-war')",
 "answer_given_upfront": true,
 "hook_type": "question|paradox|answer-stated|scenario-you|story-anecdote|spectacle-demo|premise-claim|gag-skit|confession",
 "first_question_frac": 0.05,
 "first_concrete_object_frac": 0.08,
 "first_new_idea_frac": 0.15,
 "first_notation_frac": null,
 "payoff_frac": 0.8,
 "misconception": "none|staged-early|planted-myth-defused|mid-video-correction",
 "brute_force_first": false,
 "examples_count": 4,
 "example_growth": "free text, <12 words (e.g. 'tiny numeric -> bigger -> real-world')",
 "roadmap": "none|one-line|full",
 "viewer_turn": "none|rhetorical|pause-or-guess",
 "viewer_turn_frac": null,
 "caveat_type": "none|epistemic|approximation|domain-limit|safety|historical-uncertainty",
 "recurring_anchor": "free text: object/cause/gag reused 3+ times, or 'none'",
 "sponsor_frac": null,
 "ending_type": "hook-callback|phrase-mirror|impact-coda|human-pivot|teaser-next|applied-game|credits-after-result|advice|open-question",
 "teaser": false,
 "wpm": 165,
 "median_beat_s": 30,
 "beat_sequence": ["hook","..."],
 "top5_moves": ["tag","tag","tag","tag","tag"],
 "absent3_moves": ["tag","tag","tag"]
}
```

- `beat_sequence` uses ONLY this vocabulary, in order of first appearance, with 8-14 entries and repeats allowed: hook, answer-statement, roadmap, toy-world, definition, brute-force, wall, analogy, derivation, demo-sim, story-rung, misconception-defuse, generalize, viewer-turn, caveat, payoff, coda, recap, callback, teaser, sponsor, advice, tangent.
- `top5_moves` and `absent3_moves` use tags from the `deep/BRIEF.md` taxonomy. `absent3_moves` are three taxonomy moves you predict will NOT appear at all.
