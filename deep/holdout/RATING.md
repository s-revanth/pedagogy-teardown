# Held-out test, phase 3: final rating

*Rater pass over 18 gap files, 9 critic summaries, 9 channel reports, 9 storyboards and the real transcripts. Spot-checks against `compact/*.txt` are noted where a critic's claim drives a conclusion.*

## 1. Bottom line

**Headline score: 4/10.** The teardown generalises as a **vocabulary of moves and values**, not as a **generative arc**. On held-out videos the reports reliably predict what a channel *cares about*. Honest caveats appear in about 15 of 18 videos. Notation follows its referent, special cases come before the general form, and the same cause or object is replayed. The reports do not predict *what happens where*. Every report states one signature arc fitted to its 12 training videos, and in 16 of 18 holdouts the real video used a different arc, because its format, topic type or answer status differed from the training mix. The mean critic hit rate on explicit predictions is about 55% with near-misses at half credit, and about 40% on strict hits. Discounting recall leakage (LPZh9BOjkQs, 7Pq-S557XQU, the Basel lamp) and "free" hits that subject knowledge or hedging gives away (no notation in a history video, Hilbert-Gödel-Turing order) puts the share of hits the hypothesis itself earned near 45%. The critics' mean "could it regenerate this video" score is 2.4/5. I rate slightly lower for the same discounts. The fix is mostly *conditioning*, not new moves: a format gate, an answer-status gate, conditional endings, and per-channel pace parameters.

## 2. Leaderboard

Scores are 1-5 per dimension. Each cell shows **my score**, with the mean of the two critic scores in parentheses. Rating is 1-10. `visual_data.json` stores my integers. Its `hit_rate` is the critic's hits plus half the near-misses, over the number of scored predictions, before any recall discount.

| Channel | Arc | Recall | Precision | Pacing | Voice | Regen | Rating | One-line verdict |
|---|---|---|---|---|---|---|---|---|
| kurzgesagt | 3 (3.5) | 3 (3) | 2 (2.5) | 3 (3) | 2 (2.5) | 3 (2.5) | **5** | Good inside its topic type (Peto), poor outside it (Loneliness). |
| Reducible | 2 (2.5) | 4 (4) | 3 (3) | 2 (2.5) | 3 (3) | 3 (2.5) | **5** | Best move vocabulary: 11 of 12 confident moves appeared. Arc only fits algorithm-derivation videos. |
| OverSimplified | 3 (3.5) | 3 (3) | 2 (2.5) | 3 (3.5) | 2 (2) | 2 (2.5) | **4** | Skeleton holds. Event order is mostly subject knowledge, and hook, roadmap, pivot and humour texture miss. |
| veritasium | 3 (3) | 4 (4) | 2 (2.5) | 2 (2.5) | 3 (3) | 2 (2.5) | **4** | The move set is right, but vote, roadmap, myth-defusal, ending and sponsor all miss. |
| 3blue1brown | 2 (2.5) | 3 (3) | 2 (2.5) | 2 (2) | 3 (3) | 2 (2.5) | **4** | Its values hold. Its long-form furniture was applied to a short overview and to a result-given proof. |
| PrimerBlobs | 2 (2.5) | 3 (2.5) | 2 (2.5) | 3 (3) | 2 (2.5) | 2 (2.5) | **4** | Honesty DNA holds. The sim-centric arc fails on a derivation video and an apology video. |
| SebastianLague | 2 (2.5) | 3 (3) | 2 (2) | 2 (2.5) | 2 (2) | 2 (2.5) | **4** | Build-and-verify transfers. The break-fix arc does not transfer to a devlog or to the lecture series. |
| CGPGrey | 2 (2) | 3 (3) | 2 (2) | 2 (2.5) | 3 (3) | 2 (2) | **3** | Dispositions hold. Every staged stage failed (you-hook, rule list, toy world, fake ending, fence). |
| Vsauce | 2 (2.5) | 2 (2.5) | 3 (3) | 2 (2) | 2 (3) | 2 (2) | **3** | Answer-first plus a late human pivot was unmodelled. Pace stated ~25 wpm too fast. |

**Where I disagree with the critics, and why**
- **3Blue1Brown, down.** The LLM overview's 67% hit rate leans on recalled details: the torn script, the compute figure, the bank example. The generator's light idea for Basel is flagged recall. Most of the overview's beat order is forced by its subject.
- **Veritasium, down on arc.** The critic gave HeQX2HjkcNo arc 4, but the Hilbert, Russell, Gödel, Turing spine is standard history any generator knows. Every structural choice the report itself drove missed: vote, roadmap, mid sponsor, myth-defusal ending.
- **OverSimplified, down.** Its arc and pacing scores (4 on the Pig War) mostly reward chronology. Its "no notation" and "no brute force" hits are free for history.
- **Vsauce voice, down to 2.** The report fixes pace at ~170 wpm. Measured pace is 134-148, the largest parameter error in the set (section 6).
- **CGPGrey, down to 3/10.** Several matches in 7Pq-S557XQU were flagged recall (R) by the critic. With those removed, nothing the report specifically added survives, except "one cause, renamed" and humour.
- **Kurzgesagt and Reducible, kept.** These are the two cases where the report, not subject knowledge, produced the correct calls: the late-named paradox at 2:14 (about 31%), stakes before advice, failure-shown with each repair, and roadmap slots closed in order.

## 3. Cross-channel failure modes of the hypotheses

1. **Averages stated as defaults.** Every report's move table gives frequencies ("callback-to-hook 10/12", "commit-to-answer 9/12", "roadmap 11/12") with no trigger. Generators read a count as an instruction, so the most frequent training moves became the most frequent false positives. Commit-to-answer or a vote was predicted for at least 5 channels and occurred as an up-front commit in none of the 18. The only real viewer turns were mid-video quizzes. Teaser-next appeared at the end of 1 of 18 (LPZh9BOjkQs 7:08).
2. **No format or topic conditioning.** This is the dominant failure, named in all 9 summaries. The off-format holdouts include a short overview (LPZh9BOjkQs), a lecture-series episode (l-hh51ncgDI), an on-camera apology (t9N9S4loyu8), a named-formula derivation (6YzrVUVO9M0), a psychology piece (n3Xv_g3g-mA), a theory-first algorithm (JGQe4kiPnrU), a devlog (X-iSQQgOd1A) and a history-of-technology relay (88bMVbx1dzM). Each report described one arc.
3. **Answer status ignored.** The reports assume the answer is withheld: brute force, then a wall, then the reveal. In at least 7 holdouts the title or first 40 s gives the answer, and the video spends its time on *why*. Examples: Basel 0:19, Speed of Dark 0:18, Zipf 0:39, binomial formula at 0:00, Succession 0:00, Horses 0:03, HeQX 0:00. In all 7, brute-force numerics, the staged misconception, or both were absent.
4. **Position rules fitted as runtime fractions.** Several reports placed the first notation at a runtime fraction ("64-80%", "6:18 or later"). The *order* held: the referent comes before the symbol. The *position* ranged from 0% (binomial) through 7% (88bM 1:26), 23% (PageRank matrix 5:52) and 37% (Basel lemma 6:17) to about 60% (HeQX 12:13).
5. **Vague moves.** "Uses analogy", "story", "generalise", "visible repetition" and "outside sources" carry no count, size or placement. The real variants differed sharply: 4 stand-ins (Peto) against 1 (Loneliness); a barrage of 8-14 one-clause instances (Zipf 3:08) against 2-4 settings; layered reruns of one tree (minimax) against new settings.
6. **Overfitting to signature videos.** CGPGrey's rule list, toy world, fake ending and speculation fence came from a handful of rule-system videos (rulers, flags, jury). Primer's break-the-model ending came from its emergent-sim videos. Lague's failure-gated vocabulary came from his designed-lesson Coding Adventures. Veritasium's vote and question backlog came from a few myth videos. None of these recurred.
7. **No voice model.** Voice scored 2-3 for every channel. The reports state register in a sentence but give no rate, beat length, joke type or density, address person, or aphorism rate. Generators therefore wrote warm, reflective, teacherly prose, with 50-70 s beats and 19-50% fewer words than the real videos. The real voices are terser and faster: CGPGrey runs about 21 s beats, and the LLM overview runs about 20-25 s beats.
8. **Endings modelled as one fixed shape.** Recap, callback and teaser were the default ending in 7 of 9 reports. Real endings were: a closing-phrase mirror (Kurzgesagt, both), an impact coda (Veritasium, both), a human-condition pivot with a quote (Vsauce, both), credits straight after the result (Basel), an applied game or quantified stake (CGPGrey), recap only (Reducible), and an in-character what-if (OverSimplified).

## 4. New universal rules for `pedagogy-teardown.md`

Each rule is backed by gaps in 3 or more channels.

| # | Rule | Trigger | Action | Parameter | Evidence (channel, id, m:ss) | Confidence |
|---|---|---|---|---|---|---|
| U1 | **Format gate before arc** | Duration under 10 min; series label ("explained briefly", "Algorithms Explained"); first-person title; topic type (psychology, history-of-tech, open question, devlog) | Pick an arc template per format and switch off the moves that format does not license | At least 3 templates per channel, each with an on/off move list. Under 10 min: no roadmap, recap, callback or notation; beats 20-25 s | 3B1B LPZh9BOjkQs whole; Lague l-hh51ncgDI 0:15-10:46; Primer t9N9S4loyu8 0:20; Kurz n3Xv_g3g-mA 0:00-1:23; Reducible JGQe4kiPnrU 19:28 | high |
| U2 | **Answer-given gate** | Title or first 40 s states the answer, thesis or formula | Skip brute-force numerics, the wall and the staged misconception. State the answer, then an exception or the "why" | Answer by 0:40; exception within 20 s; first concrete object by 1:30 | 3B1B d-o3eB9sfls 0:19, 1:24; Vsauce JTvcpdfGUtQ 0:18-0:34, fCn8zs912OE 0:39; CGP boezS4C_MFc 0:00; Primer 6YzrVUVO9M0 0:00; Veritasium HeQX2HjkcNo 0:00 | high |
| U3 | **Conditional ending; no default callback plus teaser** | Final 10% of runtime | Choose by type: closing-phrase mirror, impact or legacy coda, human-condition pivot, applied game, or credits after a standalone result. Use a hook callback only if the hook question is still open; use a teaser only in a series | Coda 1-3 min; proofs end within 30 s of the result | Kurz 1AElONvi9WQ 6:46; Veritasium HeQX2HjkcNo 30:09-32:07; Vsauce fCn8zs912OE 18:20; 3B1B d-o3eB9sfls 16:35; CGP boezS4C_MFc 9:50; Reducible Q_1M2JaijjQ 16:49 | high |
| U4 | **Recurring anchor with an upgrade each pass** | A cause, toy object, model or gag line has been installed | Reuse the same object or line 3-5 times; each pass adds one layer or changes the last beat; end each case on the same tag | 3-5 reuses; layered reruns can be adjacent, gags 3-35 min apart | CGP boezS4C_MFc 0:47, 5:10, 8:26; OverS QLq6GEiHqR8 1:52, 2:57; Veritasium HeQX2HjkcNo 0:51, 10:43, 29:42; Lague l-hh51ncgDI 1:10, 3:56, 5:06, 8:44; Kurz 1AElONvi9WQ 1:54, 6:11 | high |
| U5 | **Notation keyed to its referent and formula kind** | Any symbol or formula | Show the symbol within about 60 s after one verbal computation or picture of its referent. Governing relations and cost formulas may come early; symbol systems come late; a named formula may be shown at 0:00 as the destination | No runtime-fraction rule | Veritasium 88bMVbx1dzM 1:26 vs HeQX2HjkcNo 12:13; Lague X-iSQQgOd1A 1:06, 1:43; 3B1B d-o3eB9sfls 6:17; Reducible JGQe4kiPnrU 5:52; Primer 6YzrVUVO9M0 0:00, 4:33 | high |
| U6 | **Per-channel pace and beat parameters** | Writing narration | Use the measured channel wpm and beat length, never a universal 170 | Pooled channel range 140-191 wpm (section 6); 15-30 s beats for fast channels | CGP 7Pq-S557XQU (42 beats, about 187 wpm); Vsauce fCn8zs912OE (134 wpm); OverS 26EivpCPHnQ (207 wpm); 3B1B LPZh9BOjkQs (about 20 beats in 478 s) | high (measured) |
| U7 | **Drop default up-front furniture** | Generator is about to add a roadmap, vote or commit prompt, or a planted misconception | Use a front roadmap only with 3 or more parallel open questions or a definition-heavy topic, and close them in order. Otherwise use one-clause inline signposts. Use a misconception only if a folk belief exists, as a definition-by-contrast in the first minute | At most 1 inline signpost per stage change | Veritasium 88bMVbx1dzM 0:34; 3B1B LPZh9BOjkQs 3:36; Kurz n3Xv_g3g-mA 0:34; OverS 26EivpCPHnQ (none); Reducible JGQe4kiPnrU 3:35 (licensed case) | high |
| U8 | **Typed caveats** | A claim whose type is open, proved, approximate, advice or evidence-based | Open question: an epistemic caveat after each candidate, and no commit. Proof: one domain-of-validity caveat inside the lemma. Approximation: say the winner is approximate. Advice: one safety referral. Evidence thesis: inline concessions | 1-3 per video | Kurz 1AElONvi9WQ 3:50, 4:10, 6:29; Vsauce fCn8zs912OE 3:42, 15:22; 3B1B d-o3eB9sfls 8:11; Reducible JGQe4kiPnrU 18:58; Kurz n3Xv_g3g-mA 9:52; CGP 7Pq-S557XQU 4:24 | med-high |
| U9 | **One real viewer turn mid-video** | A binary decision, an absurd magnitude, or a dependent next step at 40-65% of runtime | Explicit pause or guess prompt, answered shortly after; call it a checkpoint when it is a prerequisite | 1-3 per video; answer within 10-30 s | 3B1B LPZh9BOjkQs 3:19; Lague l-hh51ncgDI 7:06; Primer 6YzrVUVO9M0 5:40, 11:19; Reducible JGQe4kiPnrU 7:46, 10:04; OverS QLq6GEiHqR8 9:32 | med |
| U10 | **Ladder of named rungs** | History of invention, a thesis with exemptions, or an escalating antagonist | Build 4-6 rungs; each is a named instance (person and year, or tier) plus one number, and ends in a wall or a break | Rungs 1.5-3 min (3 petty anecdotes for a villain) | Veritasium 88bMVbx1dzM 2:17-17:04; CGP 7Pq-S557XQU 7:00, 9:03, 11:06; OverS 26EivpCPHnQ 6:43-7:16 | med |
| U11 | **Defer the title object** | Title names an application, a trigger event or an end state | Open upstream; first mention at about 25-30% of runtime, or later for applications | 25-80% of runtime | OverS QLq6GEiHqR8 12:00, 26EivpCPHnQ 14:17; Reducible JGQe4kiPnrU 19:28; CGP 7Pq-S557XQU 4:08 | med |

## 5. Channel-specific additions (ranked)

- **3Blue1Brown:**
  1. Result-given proof tour: claim each lemma, then justify it within 60-100 s, plus one optional second proof and a link (d-o3eB9sfls 5:45-8:28).
  2. Iterate a construction exactly three times, label the last "one more step", then jump to the limit (9:18-13:16).
  3. Two-stage payoff: an awe beat, then a voiced objection, then the algebra (14:24-16:35).
- **CGPGrey:**
  1. One cause plus one recurring device by 60 s, with a rule list only for rule-system topics (7Pq-S557XQU 0:20; boezS4C_MFc 0:47).
  2. Ladder of exemptions with title cards (7Pq-S557XQU 7:00-12:33).
  3. Ambiguity shown as two parses, then a worst case (boezS4C_MFc 4:21, 8:26).
- **OverSimplified:**
  1. Open with an in-period anachronistic skit within 20 s of the sponsor tag (QLq6GEiHqR8 0:16).
  2. Verbatim gag of 8-15 words used 3 times, with the last beat changed (1:52, 2:57).
  3. Full-complexity map montage when actors exceed about 6 (26EivpCPHnQ 9:33-12:11).
- **PrimerBlobs:**
  1. Three-template switch: sim exploration, named-formula derivation, on-camera reflection.
  2. Pain-driven second act deriving the closed form (6YzrVUVO9M0 8:54-13:11).
  3. Numbered lessons with the strongest last (t9N9S4loyu8 1:57, 6:57).
- **Reducible:**
  1. Arc selector: derivation, property-hunt (JGQe4kiPnrU 7:46, 10:04), or definition-decode plus procedure (Q_1M2JaijjQ 9:01-16:34).
  2. Story frame with two named solvers for comparison topics (Q_1M2JaijjQ 0:59).
  3. Hold the named application until the theory is built (JGQe4kiPnrU 19:28).
- **SebastianLague:**
  1. Format gate: lecture series against devlog (l-hh51ncgDI against X-iSQQgOd1A).
  2. Layered reruns of one example, with the answer stated unchanged after each pass (l-hh51ncgDI 1:10-8:44).
  3. Cite the design source at the moment of choice, and replace failure-gating with a next-feature chain (X-iSQQgOd1A 6:19, 7:28).
- **Vsauce:**
  1. Answer first, then an exception within 20 s (JTvcpdfGUtQ 0:18).
  2. Late pivot of the title idea to the human condition, ending on one quote (8:53; fCn8zs912OE 18:20).
  3. A sanctioned 2-3 min detour joined by one pivot sentence (JTvcpdfGUtQ 3:26-6:22).
- **Kurzgesagt:**
  1. Topic and question-status switch: an open question gets a 2-item menu at about 36% with no commit (1AElONvi9WQ 2:34); psychology gets a stats hook and at most 1 analogy.
  2. Advice mirrors the diagnosed loop, then a referral (n3Xv_g3g-mA 7:02-9:52).
  3. Closing-phrase mirror (6:46; 10:28).
- **Veritasium:**
  1. Win-then-wall relay of named people with a countdown climax (88bMVbx1dzM 14:18-17:38).
  2. A running toy object returned to 3 or more times (HeQX2HjkcNo 0:51-29:42).
  3. An impact and legacy coda, then a reprise of the hook (30:09-32:07).

## 6. Principle audit

**Speech rate, verified.** I counted alphanumeric word tokens in each `compact/<id>.txt`, excluding timestamps and bracketed sound cues. Note that the `words` field in `transcripts/*.json` undercounts by 3-15%, because caption lines are joined without spaces. Two columns are given: wpm over the full runtime, and wpm over the speech span (to the last caption plus its estimated duration).

| Channel | Video A wpm (full / speech) | Video B wpm (full / speech) | Pooled (full / speech) | Report claim |
|---|---|---|---|---|
| 3blue1brown | Basel 177 / 180 | LLM 164 / 170 | 173 / 177 | not stated |
| CGPGrey | Horses 187 / 190 | Succession 176 / 182 | 183 / 186 | 160-180 |
| OverSimplified | Three Kingdoms 207 / 212 | Pig War 166 / 167 | 179 / 181 | not stated |
| PrimerBlobs | Binomial 198 / 199 | Deceived 179 / 181 | 191 / 193 | untestable |
| Reducible | Big O 167 / 166 | PageRank 158 / 158 | 162 / 162 | ~170 |
| SebastianLague | Ant/slime 142 / 144 | Minimax 192 / 194 | 161 / 163 | not stated |
| **Vsauce** | **Dark 148 / 150** | **Zipf 134 / 139** | **140 / 144** | **~170** |
| kurzgesagt | Peto 155 / 156 | Loneliness 121 / 146* | 133 / 150 | flat |
| veritasium | Microscopes 155 / 157 | Flaw 153 / 153 | 154 / 155 | not stated |

\*Loneliness captions end at 10:46 of 13:07, so the full-runtime figure is not meaningful there.

**The critics are right about Vsauce.** Its pace is 134-148 wpm on the full runtime (139-150 on the speech span), not the flat 170 stated in round 1 and in the Vsauce report. The holdout median across all 18 is about 165 wpm, so round 1's cross-channel median survives. As a *per-channel generator parameter*, though, "flat 170" is wrong. Pooled channel pace spans 140-191 wpm, and single videos span 134-207. Pace also varies *within* a channel by format: Lague's devlog runs at 142 and his lecture at 192, and OverSimplified runs 166-207. The second spread is format-driven, which supports U1 and U6.

| Velocity principle | Held-out verdict | Rewording |
|---|---|---|
| 1 Start from the familiar | **Weakened.** Openings are often an assertion, a fact or a formula (Zipf 0:00, binomial 0:00, Peto 0:00), with the concrete object within 90 s | "A concrete object within 90 s", not "open on Home" |
| 2 Symbols cost; notation late | **Order held, position failed** (0-60% of runtime) | See U5 |
| 3 Habit with interfaces | Untestable on video | Keep as Velocity-only |
| 4 Analogy first, then rigor | **Contradicted as an ordering.** Formal first, re-skin second (HeQX2HjkcNo 9:33, 20:40); late capstone analogy (t9N9S4loyu8 6:57); analogy budget varies 1-4 | "Analogy where it carries the hardest step; count set per topic" |
| 5 Act it out | **Held** (minimax 1:10, lighthouses 1:24, skits throughout) | none |
| 6 Dumb way first | **Conditional.** Present when the answer is withheld (Big O, ant TSP, binomial); absent when given (Basel, Zipf, Dark) | Gate on answer status (U2) |
| 7 Discovery via repetition | **Held as staged.** Real viewer turns occur mid-video (U9) | Add the viewer-turn rule |
| 8 Pace by idea rate | **Held on the knob, wrong on the constant.** Idea rate swings about 2x by format (LLM about twice the beat density) | "Hold channel wpm constant (±10%); vary beat length and examples" |
| 9 Repeat across examples | **Held strongly** (U4; Zipf barrage 3:08) | Add the forms: rerun, barrage, verbatim gag |
| 10 Tiny to bigger | **Held for maths and CS**; history and Vsauce escalate by stakes, importance or abstraction | "Escalate along one stated axis" |
| 11 Dependency order | **Held** | none |
| 12 Connect, outside sources | **Held strongly** (Lague 6:19, Vsauce named sources, 3B1B links 8:11) | Add a trigger: cite at the decision point |
| 13 Simple plus expert; why this tool | **Partly.** Expert depth carried by caveats; why-this-step clauses (LPZh9BOjkQs 4:46) | none |

**Round-1 claims**
- **Honest caveat (11/12): held**, in about 15 of 18; absent only in minimax and HeQX. Its *type* is topic-conditional (U8).
- **Special case first and minimal definition then refine (12/12): held** in most holdouts.
- **Callback to the hook (10/12): weakened.** A clear end-of-video hook callback appears in about 3 of 18, and a soft echo or phrase mirror in about 5 more.
- **Commit to answer: not replicated.** No up-front commit or vote in any of the 18.
- **Misconception first: weakened.** It appears as definition-by-contrast or false resolution, not as a planted viewer belief. Reducible has none in either holdout.
- **Ending as recap, callback and teaser (8-10/12): contradicted** (U3).
- **Flat 170 wpm: needs rewording** (see above).
- **Concrete share by subject:** untested.

## 7. Method critique and round 3

**Weaknesses of this evaluation**
1. **n = 2 per channel**, and the draw was skewed toward off-format videos. Of the 18, 8 are formats the training set lacked. That tests generalisation, but it confounds "wrong rule" with "missing condition".
2. **Recall leakage.** Generators self-reported vague-to-strong recall on several popular videos. Critics discounted ad hoc, inconsistently: LPZh9BOjkQs was discounted and HeQX2HjkcNo was not, though its spine is common knowledge.
3. **Subject knowledge confound.** History chronology, algorithm order and standard proofs dictate much of the arc. Hits there do not credit the report.
4. **Generator skill confounds.** Wrong topic guesses (t9N9S4loyu8, 88bMVbx1dzM), under-filled scripts (19-50% short) and a tendency to apply every listed move were scored inconsistently.
5. **Critic bias and format drift.** One critic per video, with no agreement check. Predictions sat in section 4, not 5, so each critic chose its own row set. Hedged predictions ("none, or possibly X") earned hits cheaply.
6. **Timing measured in absolute minutes**, which penalises the same proportional error more in long videos.

**Round 3 design**
- **Sample:** 5 held-out videos per channel, stratified by format and era (at least 2 off-format). Each training and test video is tagged with `format`, `topic_type`, `answer_status` and `year`.
- **Two baselines:** a *no-report* generator (title plus general knowledge only), and a *wrong-channel* generator. Report value = report score − no-report score.
- **Recall control:** a pre-generation recall probe of 5 factual questions on the video. If 2 or more are correct, the video is swapped out or its content rows are excluded.
- **Fixed prediction form:** about 20 slots in a JSON schema. No hedges allowed; one value per slot.
- **Two independent critics,** with Cohen's kappa reported on hit/near/miss. Disagreements are adjudicated.
- **Script length:** the generator must hit the channel wpm (±10%) and the real word count.

**Proposed numeric rubric (0-100 per video)**

| Component | Weight | Measure |
|---|---|---|
| Arc order | 20 | Kendall tau between predicted and real sequences of 8-12 canonical beat types, rescaled to 0-1 |
| Timing | 15 | 1 − mean absolute error of 6 anchors (hook, first concrete object, first new idea, first notation, payoff, ending) as a fraction of runtime, floored at 0 |
| Move recall and precision | 25 | F1 of the predicted move set against real tags (a move counts if it appears at least once) |
| Slot predictions | 20 | Hit = 1, near = 0.5, over about 20 fixed slots (question time, notation time, misconception, brute force, examples count and axis, hook type, ending type, sponsor position, top-5 moves, 3 predicted-absent moves) |
| Parameters | 10 | wpm within ±10% (5 points); median beat length within ±25% (5 points) |
| Voice | 10 | Blind pairwise test: raters pick the real paragraph from a matched pair; score = 2 × (1 − accuracy), capped at 1 |

**Report score** = mean over videos of (report − no-report baseline) ÷ (100 − baseline). A report passes when it scores at least 0.3 on in-format videos and at least 0.15 on off-format videos.
