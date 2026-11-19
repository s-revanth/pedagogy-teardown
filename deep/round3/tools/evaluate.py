"""Deterministic round-3 evaluation. No LLM judging.

For every script (condition x test video) it extracts the narration (between <<<NARRATION / NARRATION>>>),
the SLOTS json and (v2) the rule_trace json, then measures the narration with the SAME feature code used on
the real transcripts (tools/features.py).

Metrics
  fidelity_err   mean over text features of |script - real| / channel IQR (train p75-p25). Lower is better.
                 Punctuation features count only when the real video has manual captions.
  const_err      the same error for a "constant" predictor that outputs the channel's training median.
                 A condition only adds information if it beats this.
  in_band        share of text features where the script sits inside the channel's train p25-p75 band.
  wpm_err        |slot wpm - real wpm| / real wpm.
  switch_acc     agreement with the real video on sponsor / teaser / roadmap / recap (detected in the text).
Rule map (v2)  for each rule ID: how often the generator said applied / n-a / broken, and for rules that can be
               measured (N*, B*), whether the script really complied and whether the REAL test video obeys it.
usage: python3 evaluate.py  -> round3/eval/results.json + printed tables
"""
import json, os, re, statistics as st, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from features import feats, chunks_from_text

R3 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TS = json.load(open(os.path.join(R3, 'train_stats.json')))
REAL = json.load(open(os.path.join(R3, 'test_features.json')))
TEXT = ['you_rate', 'i_rate', 'we_rate', 'num_rate', 'hedge_rate', 'example_rate', 'q_rate', 'sent_len']
PUNCT = {'q_rate', 'sent_len'}
SW = {'sponsor': lambda f: f['sponsor_frac'] is not None, 'teaser': lambda f: bool(f['teaser_end']),
      'roadmap': lambda f: bool(f['roadmap_start']), 'recap': lambda f: bool(f['recap_end'])}
NKEY = {'words per minute': 'wpm', '"you/your" per 100 words': 'you_rate', '"I/me/my" per 100 words': 'i_rate',
        '"we/us/let\'s" per 100 words': 'we_rate', 'numbers per 100 words': 'num_rate', 'question marks per 100 words': 'q_rate',
        'mean words per sentence': 'sent_len', 'hedges (probably/maybe/roughly...) per 100 words': 'hedge_rate',
        'example cues (for example/imagine/let\'s say...) per 100 words': 'example_rate'}
BKEY = {'B1': 'sponsor', 'B2': 'teaser', 'B3': 'roadmap', 'B4': 'recap'}

def parse(path):
    t = open(path).read()
    m = re.search(r'<<<NARRATION\s*\n(.*?)\n\s*NARRATION>>>', t, re.S)
    narr = m.group(1) if m else None
    slots = trace = None
    for b in re.findall(r'```json\s*(\{.*?\})\s*```', t, re.S):
        try: d = json.loads(b)
        except json.JSONDecodeError: continue
        if 'rule_trace' in d: trace = d['rule_trace']
        elif 'hook_type' in d or 'beat_sequence' in d: slots = d
        elif 'verified_trace' in d: pass
    rec = re.search(r'recall:\s*\**\s*(none|vague|strong)', t, re.I)
    return narr, slots, trace, (rec.group(1).lower() if rec else 'unknown')

def rulebook_bands(ch):
    """Map N-rule IDs to (feature, band, p25, p75) by reading the rulebook table."""
    out = {}
    for l in open(os.path.join(R3, '..', 'policy', f'{ch}.md')):
        m = re.match(r'\| (N\d+) \| (.+?) \| (\w+) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|', l)
        if m: out[m[1]] = (NKEY.get(m[2]), m[3], float(m[4]), float(m[6]))
    return out

def defaults(ch):
    out = {}
    for l in open(os.path.join(R3, '..', 'policy', f'{ch}.md')):
        m = re.match(r'- \*\*(B\d)\*\* .*→ (default ON|default OFF|CONDITIONAL)', l)
        if m: out[m[1]] = m[2]
    return out

def iqr(ch, k):
    b = TS[ch]['all'].get(k)
    return max(b['p75'] - b['p25'], 0.05) if b else None

def main():
    rows, rulemap = [], {}
    for vid, r in REAL.items():
        ch = r['channel']; manual = r['captions'] == 'manual'
        feats_used = [k for k in TEXT if (manual or k not in PUNCT) and r.get(k) is not None and iqr(ch, k)]
        const = st.mean(abs(TS[ch]['all'][k]['median'] - r[k]) / iqr(ch, k) for k in feats_used) if feats_used else None
        for cond in ('base', 'v1', 'v2', 'v3'):
            p = os.path.join(R3, 'scripts', cond, f'{vid}.md')
            if not os.path.exists(p): continue
            narr, slots, trace, recall = parse(p)
            row = dict(channel=ch, id=vid, cond=cond, recall=recall, has_narr=bool(narr), has_slots=bool(slots), has_trace=bool(trace), const_err=const)
            if narr:
                f = feats(chunks_from_text(narr), True); row['n_words'] = f['n_words']
                errs = [abs(f[k] - r[k]) / iqr(ch, k) for k in feats_used if f.get(k) is not None]
                row['fidelity_err'] = st.mean(errs) if errs else None
                inb = [TS[ch]['all'][k]['p25'] <= f[k] <= TS[ch]['all'][k]['p75'] for k in TEXT if f.get(k) is not None and TS[ch]['all'].get(k)]
                row['in_band'] = sum(inb) / len(inb) if inb else None
                row['switch_acc'] = st.mean(SW[s](f) == SW[s](r) for s in SW)
                row.update({f'sw_{s}': SW[s](f) for s in SW})
            if slots and slots.get('wpm'):
                try: row['wpm_err'] = abs(float(slots['wpm']) - r['wpm']) / r['wpm']
                except (TypeError, ValueError): pass
            if cond == 'v2' and trace and narr:
                bands = rulebook_bands(ch); dfl = defaults(ch); short = r['duration'] < 600
                for rid, val in trace.items():
                    rid = rid.strip(); status = str(val).split(':')[0].strip().lower()
                    e = rulemap.setdefault(ch, {}).setdefault(rid, {'applied': 0, 'n/a': 0, 'broken': 0, 'other': 0, 'script_ok': [], 'real_ok': [], 'claimed_but_failed': 0})
                    e[status if status in e else 'other'] += 1
                    ok_s = ok_r = None
                    if rid in bands and bands[rid][0]:
                        k, bnd, lo, hi = bands[rid]
                        if k == 'wpm':
                            if (bnd == 'under10min') != short: continue
                            ok_s = slots and slots.get('wpm') and lo <= float(slots['wpm']) <= hi
                            ok_r = lo <= r['wpm'] <= hi
                        elif not (k in PUNCT and not manual):
                            ok_s = f.get(k) is not None and lo <= f[k] <= hi
                            ok_r = r.get(k) is not None and lo <= r[k] <= hi
                    elif rid in BKEY and rid in dfl and dfl[rid] != 'CONDITIONAL':
                        want = dfl[rid] == 'default ON'
                        ok_s = SW[BKEY[rid]](f) == want; ok_r = SW[BKEY[rid]](r) == want
                    if ok_s is not None:
                        e['script_ok'].append(bool(ok_s)); e['real_ok'].append(bool(ok_r))
                        if status == 'applied' and not ok_s: e['claimed_but_failed'] += 1
            rows.append(row)
    def agg(sel):
        out = {}
        for cond in ('base', 'v1', 'v2', 'v3'):
            xs = [x for x in rows if x['cond'] == cond and sel(x)]
            if not xs: continue
            m = lambda k: round(st.mean(x[k] for x in xs if x.get(k) is not None), 3) if any(x.get(k) is not None for x in xs) else None
            out[cond] = {'n': len(xs), 'fidelity_err': m('fidelity_err'), 'const_err': m('const_err'), 'in_band': m('in_band'),
                         'wpm_err': m('wpm_err'), 'switch_acc': m('switch_acc'), 'narr_ok': round(sum(x['has_narr'] for x in xs) / len(xs), 2)}
        return out
    res = {'overall': agg(lambda x: True), 'no_recall': agg(lambda x: x['recall'] in ('none', 'unknown')),
           'by_channel': {ch: agg(lambda x, ch=ch: x['channel'] == ch) for ch in sorted({x['channel'] for x in rows})},
           'rows': rows}
    rm = {}
    for ch, rules in rulemap.items():
        for rid, e in rules.items():
            n = e['applied'] + e['n/a'] + e['broken'] + e['other']
            rm.setdefault(ch, {})[rid] = {'n': n, 'applied': e['applied'], 'n/a': e['n/a'], 'broken': e['broken'],
                'script_comply': round(sum(e['script_ok']) / len(e['script_ok']), 2) if e['script_ok'] else None,
                'real_valid': round(sum(e['real_ok']) / len(e['real_ok']), 2) if e['real_ok'] else None,
                'claimed_but_failed': e['claimed_but_failed']}
    res['rule_map'] = rm
    os.makedirs(os.path.join(R3, 'eval'), exist_ok=True)
    json.dump(res, open(os.path.join(R3, 'eval', 'results.json'), 'w'), indent=1)
    for name in ('overall', 'no_recall'):
        print(name); [print(' ', c, v) for c, v in res[name].items()]
    for ch, r in res['by_channel'].items():
        print(f'{ch:15}', {c: (v['fidelity_err'], v['const_err'], v['in_band'], v['switch_acc']) for c, v in r.items()})

if __name__ == '__main__':
    main()
