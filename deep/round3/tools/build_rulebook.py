"""Build deep/policy/<channel>.md: the v2 rulebook, with a stable ID on every rule.

Sources (training data only):
  U*  universal rules  <- holdout/visual_data.json universal_new_rules (round-2 test findings)
  C*  channel rules    <- holdout/visual_data.json channels[].new_findings
  D*  corrections      <- storyboard claims that were contradicted (do not assume) or only partly held (conditional)
  N*  numeric bands    <- round3/train_stats.json, fitted on the channel's training corpus (test videos excluded)
  B*  default switches <- training base rates of sponsor / teaser / roadmap / recap
The generator must output a rule_trace saying, for every ID, applied | n/a | broken (with a reason).
"""
import json, os

DEEP = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VD = json.load(open(os.path.join(DEEP, 'holdout', 'visual_data.json')))
TS = json.load(open(os.path.join(DEEP, 'round3', 'train_stats.json')))
EX = {}
import csv
for r in csv.DictReader(open(os.path.join(DEEP, 'tracker.csv'))): EX.setdefault(r['channel'], []).append((r['id'], r['title'], r['duration'], 'deep/compact'))
for l in open(os.path.join(DEEP, 'holdout', 'heldout.tsv')):
    ch, vid, title, dur = l.rstrip('\n').split('\t'); EX.setdefault(ch, []).append((vid, title, dur, 'deep/holdout/compact'))

LABEL = {'wpm': 'words per minute', 'you_rate': '"you/your" per 100 words', 'i_rate': '"I/me/my" per 100 words', 'we_rate': '"we/us/let\'s" per 100 words',
         'num_rate': 'numbers per 100 words', 'q_rate': 'question marks per 100 words', 'sent_len': 'mean words per sentence',
         'hedge_rate': 'hedges (probably/maybe/roughly...) per 100 words', 'example_rate': 'example cues (for example/imagine/let\'s say...) per 100 words'}
BOOL = {'sponsor_present': 'a sponsor read', 'teaser_end': 'a teaser for a next video in the last 12%', 'roadmap_start': 'a spoken roadmap in the first 12%', 'recap_end': 'a spoken recap in the last 20%'}

def fmt(x): return f'{x:.2f}' if isinstance(x, float) and x < 10 else f'{x:.0f}'

def build(ch):
    c = next(x for x in VD['channels'] if x['channel'] == ch); s = TS[ch]
    L = [f'# {ch}: v2 rulebook (round 3)', '',
         'This rulebook OVERRIDES `deep/reports/' + ch + '.md` wherever they conflict. Read the report for the channel\'s moves and voice, then apply these rules.',
         'Every rule has an ID. Your script must end with a `rule_trace` saying, for EVERY ID: `applied`, `n/a` (with the reason it does not apply to this video) or `broken` (with the reason).', '',
         '## Step 0: classify before planning',
         'Write down: duration band (<10 min / ≥10 min), format (from the title and series label), whether the title or opening states the answer, solved vs open question, and topic type. Rules marked IF depend on these.', '',
         '## U: universal rules (from the round-2 held-out failures, seen in 3 or more channels)']
    for i, r in enumerate(VD['universal_new_rules'], 1):
        L.append(f"- **U{i}** [{r['confidence']}] IF {r['trigger']} → {r['rule']}")
    L += ['', '## C: channel rules found on round-2 held-out videos']
    for i, f in enumerate(c['new_findings'], 1):
        L.append(f"- **C{i}** ({f['type']}) {f['finding']}  _evidence: {f['evidence']}_")
    L += ['', '## D: corrections to the v1 report and storyboard']
    i = 0
    for cl in c['storyboard_claims']:
        if cl['status'] == 'contradicted':
            i += 1; L.append(f"- **D{i}** DO NOT default to: {cl['claim']}. It failed on held-out videos: {cl['evidence']}")
        elif cl['status'] == 'partly':
            i += 1; L.append(f"- **D{i}** CONDITIONAL, use only when the video clearly calls for it: {cl['claim']}. Mixed evidence: {cl['evidence']}")
    L += ['', f"## N: numeric targets fitted on {s['all']['n_videos']} training transcripts from this channel",
          'Aim for the median, and stay inside the p25-p75 range. Use the duration-band row that matches the video.', '',
          '| ID | measure | band | p25 | median | p75 | n |', '|---|---|---|---|---|---|---|']
    k = 0
    for key, lab in LABEL.items():
        for bandname in ('under10min', 'over10min') if key == 'wpm' else ('all',):
            b = s[bandname].get(key)
            if not b: continue
            k += 1; L.append(f"| N{k} | {lab} | {bandname} | {fmt(b['p25'])} | {fmt(b['median'])} | {fmt(b['p75'])} | {b['n']} |")
    L += ['', '## B: default switches (training base rates)']
    for j, (key, lab) in enumerate(BOOL.items(), 1):
        r = s['all'][key]
        d = 'default ON' if r >= 0.6 else 'default OFF' if r <= 0.25 else 'CONDITIONAL: include only if the video type clearly calls for it'
        L.append(f"- **B{j}** {lab}: seen in {r*100:.0f}% of training videos → {d}.")
    sp = s['all'].get('sponsor_frac')
    if sp: L.append(f"  - If there is a sponsor read, place it at about {sp['median']*100:.0f}% of runtime (p25-p75 {sp['p25']*100:.0f}-{sp['p75']*100:.0f}%).")
    L += ['', '## E: exemplars (training transcripts you may read to copy rhythm and structure, not content)',
          'Pick the 1-2 closest to the test video by format and duration, read them, and name them in your header.']
    for vid, title, dur, where in EX.get(ch, []):
        L.append(f"- `{where}/{vid}.txt` ({int(float(dur))//60} min): {title}")
    os.makedirs(os.path.join(DEEP, 'policy'), exist_ok=True)
    open(os.path.join(DEEP, 'policy', f'{ch}.md'), 'w').write('\n'.join(L) + '\n')
    return len(L)

for ch in TS: print(ch, build(ch), 'lines')
