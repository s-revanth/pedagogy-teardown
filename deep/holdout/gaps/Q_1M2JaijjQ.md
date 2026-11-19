# Gap analysis: Reducible, "What Is Big O Notation?" (Q_1M2JaijjQ, 17:44)

Note: the script's explicit predictions are in its section 4 (the brief says section 5). Scored from section 4. Script length shortfall is ignored.

## 1. Real beat sheet (compact)

| m:ss | Lvl | Tags | Paraphrase |
|---|---|---|---|
| 0:00 | H | hook-question, humor | Imagine asking students what Big O is; vague answers, then a dense jargon definition the narrator mocks. |
| 0:29 | B | roadmap, story | Step back and tell the history; four-part outline: story, visual reading of the definition, practical steps, worked example. |
| 0:59 | H | story, running-character, act-it-out | Problem: find non-negative triples summing to n. Alice and Bob appear; Bob's triple loop, traced at n=3. |
| 1:43 | H | brute-force-first (contrast), act-it-out | Alice's two loops with c = n-(a+b), traced at n=3. |
| 2:20 | N | second-person-role, failure-shown | "You are the judge": time both on one machine (58 s vs 15 s at n=10,000), table, log-axis plot; called a valid method. |
| 3:31 | N | inline-quiz, failure-shown | Pause: why is timing not ideal? Tedious, machine-dependent; goal becomes machine-independent measure. |
| 4:29 | N | special-case-first, visible-repetition | Count worst-case if-checks: Bob 21^3, 41^3; Alice 21^2; table of data points. |
| 5:45 | N | honest-caveat (scheme audit) | What we like (machine independence) and dislike (scaling unclear, prep effort). |
| 6:45 | N | generalize | Replace specific n with general n: (n+1)^3 and (n+1)^2. |
| 7:30 | N | approximation-gets-less-wrong, honest-caveat | Only large-n worst case matters; drop lower-order terms, trading precision for simplicity. |
| 8:14 | I | notation-after-concept, recap | Name it Big O: Alice O(n^2), Bob O(n^3). Meta-moral: we removed each annoyance one by one. |
| 9:01 | I | humor, notation | Textbook f(n) <= c g(n) definition shown; narrator reacts to its density; read as "does not grow faster". |
| 9:46 | I | build-and-verify, simulation-as-argument | f = 3n^2+5n+4 is O(n^2); plot c·g against f; c=1, 3 fail, c=4 works; cannot be O(n); "large enough n" is the key. |
| 11:30 | I | multiple-decompositions | Limit-based equivalent for viewers who know limits. |
| 11:58 | I | rule-list | Six runtime classes, best to worst. |
| 12:27 | N | rule-list (ritual) | Three steps: understand the algorithm, choose a worst-case base unit, map growth to a class. |
| 13:24 | N | special-case-first, visible-repetition, build-and-verify | Worked example: recursive f with two self-calls; count calls for n=1..5 (1, 3, 7, 15, 31), each count built from the previous via call tree. |
| 15:51 | N | notation-after-concept | Doubling pattern means exponential; 2^k - 1 gives O(2^n). |
| 16:20 | N | generalize-to-other-domains | Moral: drawing diagrams helps in any problem. |
| 16:34 | H | recap | Recap in roadmap order (history, definition, steps, example). |
| 17:18 | - | admin | Like, subscribe, Patreon. |

## 2. Prediction scorecard (script section 4)

| # | Prediction | Predicted | Actual | Verdict |
|---|---|---|---|---|
| 1 | First question to viewer | 0:00-0:15 hook question | 0:00 question about what students say Big O is | hit |
| 2 | First real inline quiz | ~7:20 | 3:31 (why is timing not ideal?); 2:20 judge prompt | miss (time), existence ok |
| 3 | First notation: O(n) | ~5:05 | 8:14, as O(n^2) / O(n^3); O(n) never used as an example | near |
| 4 | Formal definition | ~15:25 | 9:01 | miss |
| 5 | Misconception | yes, partial ("lower Big O always faster" or "seconds"), crossover example | none planted; timing is shown as valid-but-flawed, no crossover | miss |
| 6 | Brute-force-first | yes: linear search, stopwatch | yes: Bob's triple loop, then wall-clock timing (linear search absent) | hit |
| 7 | Examples | 3 main (linear, pairs, binary) on n=4,8,16 ladders, rising growth rate | 3 (Bob/Alice, 3n^2+5n+4, recursive f), cubic -> quadratic -> exponential; ladders n=20,40 and n=1..5 | near (count and growth hit, identity miss) |
| 8 | Hook type | paradox: two programs, same task, different scaling | meta-pain hook (students' definitions); two programs arrive at 0:59 as Alice/Bob | near |
| 9 | Ending | recap + callback + teaser | recap only (mirrors roadmap), then outro; no callback, no teaser | near |
| 10 | Move: special-case-first | present | n=3, n=20/40, f(1..5) | hit |
| 11 | Move: notation-after-concept | present | Big O named after counting and dropping terms | hit |
| 12 | Move: roadmap | present | 0:44, four slots (different content) | hit |
| 13 | Move: honest-caveat | present | 5:45 audit, 7:45 precision-for-simplicity | hit |
| 14 | Move: recap with callback-to-hook | present | recap yes, callback no | near |
| 15 | Sixth: failure-shown | present | 3:31 timing, 6:00 tally table | hit |

Hit rate: 7 hit, 5 near, 3 miss of 15 = 47% strict, 63% with near at half credit.

## 3. Structural alignment

Predicted arc: paradox hook, define n, roadmap, linear search by hand, stopwatch fails, count steps, ladder, O(n), pairs (n^2), 3n+5, misconception crossover, guess game, binary search (log n), cost table, definition, caveat, recap + callback, teaser.

Real arc: meta hook, roadmap, Alice/Bob story with code, timing, quiz, count ops, audit, generalize, drop terms, name, decode textbook definition, six classes, three-step procedure, worked exponential example, moral, recap.

- Predicted and present: roadmap (0:44 vs 1:00), brute-force/stopwatch failure (2:34 vs 2:20), step counting (4:29 vs 3:10), special-case ladder, drop-constants (7:30 vs 8:35), notation-after-concept, formal definition with plot, honest caveat, recap (16:34 vs 16:55).
- Predicted but absent (false positives): minimal definition of "algorithm"/n, linear search home problem, pair-count quiz at n=100, crossover misconception, guess-a-number analogy, binary search/log n (about 3 min of predicted runtime), time-unit cost table, closing caveat card, callback, teaser.
- Present but unpredicted (false negatives): story frame with two named characters (0:59-2:20, again 8:29); code as the first object; "you are the judge" second-person framing; meta-moral that each flaw was removed in turn (8:44); decoding the textbook definition with a c slider (9:01-11:44, about 15% of runtime); limit alternative; six-class list; numbered three-step procedure (12:27); long worked exponential example (13:24-16:20, 16%); "draw diagrams" moral; humor aimed at jargon.

Timing drift: hook 0:00 vs 0:00 (0). First new idea (timing fails) 2:20 vs 2:34 (+0:14). Counting ops 3:10 vs 4:29 (+1:19). Payoff (name) 5:05 vs 8:14 (+3:09). Formal definition 15:25 vs 9:01 (-6:24). Recap 16:55 vs 16:34 (-0:21). Ending 17:30 vs 17:18 (-0:12).

## 4. Gap taxonomy

- Story and running characters (0:59-8:44): missing-rule. Report lists running-character as 1/12 and story 3/12 and gives no trigger. Here the whole discovery arc rides on Alice and Bob.
- Comparing two algorithms on one problem rather than one recipe on a list: missing-rule. The report has no guidance on choosing a problem with a slow and a smart solver so the notation compares them (O(n^2) vs O(n^3)).
- Textbook-definition decode (9:01-11:44): topic-conditional. Report has "formula as receipt" but no beat for a definition that learners will meet in class; the generator put the definition at 87% runtime. Real: 51%.
- Notation timing: underspecified. Report says notation arrives last. Real name at 46%, definition at 51%. The generator split the name (29%) and definition (87%) with no support in the report.
- Procedure plus worked example as the second half (11:58-16:34): underspecified. The report's "ritual" variant covers recursion/DP; it does not say a concept video can end with a 3-step recipe and one worked ladder.
- Misconception beat: generator-error plus underspecified. The report's move table never lists misconception-first; the generator imported it from round-1. The real video plants no belief.
- Teaser and callback: generator-error for the teaser (report says 3/12 and weak). Callback is `wrong-rule` if read as default (9/12): there is no answerable hook to call back to.
- Binary search, log n, cost table: generator-error (topic content, not a rule).
- Humor: voice/craft. Dry self-aware reactions to jargon at 0:15 and 9:31; report says "light, dry" with no placement rule.
- Code on screen at 1:14: underspecified. Report says code shows in about half of videos with no trigger; here code is the problem statement, not a receipt.

## 5. Overfit check

- "Names, notation and code arrive last": code arrives first here (1:14), the name at 46%.
- callback-to-hook 9/12: 0/1 here.
- hook-paradox / spectacle hooks: the hook is a classroom anecdote, not a paradox.
- Principle 1 "failure is the stepping stone" holds and is even stated aloud at 8:44.
- Roadmap 12/12 holds; the "empty slot" detail is not visible here.
- Analogy: none, consistent with the report's weak-analogy finding.

## 6. Proposed rule changes

1. Story frame for comparison topics (channel-specific, possibly universal). Trigger: topic is about judging or comparing solutions. Action: within 0:30-1:15 introduce one problem and two named solvers (slow brute force, smarter), show each as code plus an n=3 trace (about 45 s each), and reuse the pair through every measurement stage until the notation is applied to both at once. Evidence: 0:59-2:20, 8:29.
2. Scheme audit ladder (channel-specific). Trigger: defining a measurement or tool. Action: present 3 to 4 schemes in sequence; after each, say one like and one dislike aloud, ask the viewer to find the flaw at least once (about 30 s pause), and close with a one-line meta-moral "each fix removed one annoyance". Evidence: 3:31, 5:45, 8:44.
3. Definition-decode beat (likely universal). Trigger: a canonical formal definition exists that learners will meet in class. Action: place the name at 40-55% runtime and the formal definition within 60 s after it; react to its density in one dry line; translate clause by clause using one concrete function and a slider (three values: fail, fail, succeed); add an optional alternative form for experts. Evidence: 8:14, 9:01-11:44.
4. Second-half procedure block (channel-specific). Trigger: the concept is a skill applied to arbitrary inputs. Action: after notation, list the classes (about 30 s), give a 3-step recipe, then one worked example built as a ladder of 5 sizes where each count reuses the previous (about 3 min), ending on a general moral. Evidence: 11:58-16:34.
5. No default misconception or teaser (channel-specific). Trigger: generating a Reducible script. Action: do not plant a belief-misconception; use failure of the previous tool instead. Teaser only if the report's sibling video exists (3/12). Callback only when the hook promised a payoff. End with a recap that follows the roadmap order. Evidence: 16:34 recap mirrors 0:44 outline; no callback.
6. Hook by anecdote or setup (channel-specific). Trigger: definition-heavy topic. Action: open with a 30 s social or problem setup (students' answers, a scenario), then a "step back" promise by 0:30. Evidence: 0:00-0:44.

## 7. Scores (1-5)

- Arc fidelity: 3. Measurement failure to counting to dropping terms to name is right; the second half and story frame are not.
- Move-inventory recall: 4. About 11 of 16 real move types predicted; story, running-character, humor, act-it-out trace, decode-definition missed.
- Move precision: 3. Misconception, analogy, teaser, callback, cost table, crossover were absent; about 9 of 21 beats present in some form.
- Pacing/timing: 3. Hook, roadmap, first failure and recap land within about 0:20; name is 3 min late, definition 6 min early, binary search block has no counterpart.
- Voice: 3. Neutral textbook; real voice is dry and self-aware about jargon, with a judge persona.
- Overall regenerate-ability: 3. The first half is regenerable; the second half is not from the report.
