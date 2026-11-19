# Analysis brief: pedagogy teardown of one YouTube explainer

You are analysing how a great explainer TEACHES. Not the facts — the moves. Your output feeds Velocity, an AI tutor that teaches live with voice synced to on-screen simulations, adapts to a learner model, and picks "playbooks".

## Inputs
- `compact/<id>.txt`: timestamped transcript (~15 s lines). Paraphrase only; at most ONE quote per video, under 15 words.
- Taxonomy below; add new tags freely (prefix new ones with `new:`).

## Lens: Velocity's working principles (test each where evidence exists)
1 Start from the familiar. 2 Every new symbol costs effort. 3 Interfaces become comfortable through habit. 4 Analogy first, then step toward rigor. 5 Act out the problem literally. 6 Dumb/brute-force way first, neat scratch pad. 7 Learner discovers the insight via visible repetition. 8 Pace by novelty — round 1 found speech rate stays FLAT (~170 wpm); slowdown happens via idea rate (longer beats, more examples, late notation). Look for evidence for/against. 9 Repeat across examples. 10 Tiny to bigger examples. 11 Dependency order; invent stepping stones. 12 Connect everything incl. outside sources. 13 Simple for a 12-year-old, expert depth, say why each tool is chosen.
Round-1 extra moves to watch: honest-caveat, minimal-definition-then-refine, callback-to-hook, commit-to-answer, presenter-was-wrong, build-and-verify, show-full-complexity-then-zoom, roadmap, second-person-role, running-character, rule-list-as-interface, you-could-invent-it.

## Move taxonomy
hook-paradox, hook-question, misconception-first, act-it-out, brute-force-first, visible-repetition, learner-discovers, analogy, analogy-breakpoint, minimal-definition-then-refine, design-it-yourself, special-case-first, multiple-decompositions, approximation-gets-less-wrong, notation-after-concept, notation-compaction, simulation-as-argument, toy-world, running-character, inline-quiz, honest-caveat, generalize-to-other-domains, recap, callback-to-hook, teaser-next, story, humor, roadmap, commit-to-answer, build-and-verify, failure-shown, second-person-role, rule-list, expert-dialogue.

## Output: write TWO files, nothing else
1. `analyses/<id>.json`:
```json
{"id":"","channel":"","title":"","captions":"manual|automatic",
 "beats":[["m:ss","H|B|N|I","tag|tag","one-line paraphrase"]],
 "metrics":{"first_question":"m:ss|none","notation_first":"m:ss|none","key_term":"","misconception":"none|partial|yes: ...","brute_force":"no|yes m:ss: ...","examples":"n + how they grow","ending":"..."},
 "principles":{"1":"confirmed|partly|contradicted|not-observed: evidence with m:ss", "...":"... through 13"},
 "new_moves":[{"name":"","what":"","evidence":"m:ss ..."}],
 "theory":"2-4 sentences: the single most transferable insight about how this video teaches",
 "velocity":["one-line concrete implication for the AI tutor (scene builder, voice, orchestrator, learner model, ghost hands, evals)"],
 "quote":["m:ss","<15 words"]}
```
H=Home (familiar), B=Bridge (leaving an analogy toward the new), N=New idea, I=New interface (notation/formula/code/new chart). Beats are 10-90 s teaching moves; tag sponsor/outro beats `admin`.
2. `analyses/<id>.md`: 300-600 words — structure arc, the 3-5 strongest moves with timestamps, what's unusual vs other explainers, principle verdicts in brief, Velocity implications.

Be concrete, timestamped, skeptical. Don't invent content not in the transcript. Do not edit any other file.
