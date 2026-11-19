"""Round-3 analysis on top of eval/results.json. Deterministic, no LLM judging.

1. Paired comparisons on the SAME test videos: v1 - base, v2 - base, v2 - v1, and each condition vs the
   constant-median predictor. Mean difference, wins/losses, sign-test p, bootstrap 95% CI (seed 0, 5000 draws).
2. Slot accuracy against the blind hand labels (eval/real_labels.json) for hook_type, ending_type and
   answer_given_upfront, with the majority-label baseline (label-set majority: optimistic for the baseline).
3. Measurable slots against the real transcript: wpm, first_question_frac (manual captions only), sponsor, teaser.
4. Rule gap map: rules ranked by how often they are broken, claimed-but-failed and how valid they are on real videos.
usage: python3 analyze.py -> eval/analysis.json + printed tables
"""
import json, math, os, random, statistics as st, sys
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evaluate import parse

R3 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = json.load(open(os.path.join(R3, 'eval', 'results.json')))
REAL = json.load(open(os.path.join(R3, 'test_features.json')))
RVR = json.load(open(os.path.join(R3, 'eval', 'real_vs_real.json')))
LAB = {k: v for k, v in json.load(open(os.path.join(R3, 'eval', 'real_labels.json'))).items() if not k.startswith('_')}
CONDS = ('base', 'v1', 'v2', 'v3')
TRL = {k: v for k, v in json.load(open(os.path.join(R3, 'eval', 'train_labels.json'))).items() if not k.startswith('_')}
CB = lambda x: 'phrase-mirror' if str(x).strip().lower() in ('hook-callback', 'phrase-mirror') else str(x).strip().lower()

def sign_p(w, l):
    n = w + l
    if n == 0: return 1.0
    k = min(w, l)
    return min(1.0, 2 * sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n)

def boot(d, seed=0, B=5000):
    rnd = random.Random(seed); n = len(d)
    ms = sorted(st.mean(rnd.choice(d) for _ in range(n)) for _ in range(B))
    return round(ms[int(.025 * B)], 3), round(ms[int(.975 * B)], 3)

def paired(rows, key, a, b, lower_better=True, sel=lambda r: True):
    by = {}
    for r in rows:
        if sel(r) and r.get(key) is not None: by.setdefault(r['id'], {})[r['cond']] = r[key]
    d = []
    for vid, x in by.items():
        xa = RVR[vid]['rvr_mean'] if a == 'rvr' else x.get(a) if a != 'const' else next((r['const_err'] for r in rows if r['id'] == vid), None)
        if xa is None or b not in x: continue
        d.append(x[b] - xa)
    if not d: return None
    better = sum((v < 0) if lower_better else (v > 0) for v in d); worse = sum((v > 0) if lower_better else (v < 0) for v in d)
    return {'n': len(d), 'mean_diff': round(st.mean(d), 3), 'ci95': boot(d), 'better': better, 'worse': worse, 'sign_p': round(sign_p(better, worse), 4)}

def main():
    rows = RES['rows']
    out = {'paired': {}, 'slots': {}, 'measured_slots': {}, 'gap_map': []}
    # only videos where all three conditions exist, so comparisons are on identical sets
    full = {v for v in {r['id'] for r in rows} if all(any(r['id'] == v and r['cond'] == c and r.get('fidelity_err') is not None for r in rows) for c in [c for c in CONDS if any(x['cond'] == c for x in rows)])}
    for name, sel in (('all', lambda r: r['id'] in full), ('no_recall', lambda r: r['id'] in full and r['recall'] in ('none', 'unknown'))):
        p = out['paired'][name] = {}
        for key, lb in (('fidelity_err', True), ('wpm_err', True), ('switch_acc', False), ('in_band', False)):
            for a, b in (('base', 'v1'), ('base', 'v2'), ('v1', 'v2'), ('v2', 'v3'), ('base', 'v3'), ('const', 'base'), ('const', 'v1'), ('const', 'v2'), ('const', 'v3'), ('rvr', 'base'), ('rvr', 'v1'), ('rvr', 'v2'), ('rvr', 'v3')):
                if key != 'fidelity_err' and a in ('const', 'rvr'): continue
                r = paired(rows, key, a, b, lb, sel)
                if r: p[f'{key}: {b} vs {a}'] = r
    out['n_full_videos'] = len(full)
    # slots vs hand labels. Endings: hook-callback and phrase-mirror merged (one "return to the opening" family);
    # labels with ending None (content ending not observable) are skipped. Two baselines: label-set majority
    # (optimistic, uses test labels) and per-channel TRAINING majority (fair: what a no-model predictor would say).
    full = {v for v in full}
    for slot in ('hook_type', 'ending_type', 'answer_given_upfront'):
        labs = {k: v for k, v in LAB.items() if v.get(slot) is not None}
        norm = CB if slot == 'ending_type' else (lambda x: str(x).strip().lower())
        vals = [norm(v[slot]) for v in labs.values()]; maj = max(set(vals), key=vals.count)
        s = out['slots'][slot] = {'majority_label': maj, 'majority_acc': round(vals.count(maj) / len(vals), 3), 'n_labels': len(vals)}
        if slot != 'answer_given_upfront':
            hit = []
            for vid, lab in labs.items():
                ch = REAL[vid]['channel'] if vid in REAL else None
                tv = [norm(v[slot]) for v in TRL.values() if v['channel'] == ch]
                if tv: hit.append(max(set(tv), key=tv.count) == norm(lab[slot]))
            s['train_channel_majority_acc'] = round(sum(hit) / len(hit), 3)
        for c in CONDS:
            hit = []; pred = []
            for vid, lab in labs.items():
                pth = os.path.join(R3, 'scripts', c, f'{vid}.md')
                if not os.path.exists(pth): continue
                _, sl, _, _ = parse(pth)
                if sl and slot in sl: hit.append(norm(sl[slot]) == norm(lab[slot])); pred.append(norm(sl[slot]))
            s[c] = {'n': len(hit), 'acc': round(sum(hit) / len(hit), 3) if hit else None, 'top_predictions': Counter(pred).most_common(3)}
    # measurable slots vs the real transcript
    for c in CONDS:
        m = {'fq_abs_err': [], 'sponsor_ok': [], 'teaser_ok': [], 'wpm_abs_pct': []}
        for vid, r in REAL.items():
            pth = os.path.join(R3, 'scripts', c, f'{vid}.md')
            if not os.path.exists(pth): continue
            _, sl, _, _ = parse(pth)
            if not sl: continue
            if r['captions'] == 'manual' and r.get('first_q_frac') is not None and isinstance(sl.get('first_question_frac'), (int, float)):
                m['fq_abs_err'].append(abs(sl['first_question_frac'] - r['first_q_frac']))
            m['sponsor_ok'].append((sl.get('sponsor_frac') is not None) == (r['sponsor_frac'] is not None))
            m['teaser_ok'].append(bool(sl.get('teaser')) == bool(r['teaser_end']))
            try: m['wpm_abs_pct'].append(abs(float(sl['wpm']) - r['wpm']) / r['wpm'])
            except (TypeError, ValueError, KeyError): pass
        out['measured_slots'][c] = {k: (round(st.mean(map(float, v)), 3), len(v)) if v else None for k, v in m.items()}
    # gap map
    for ch, rules in RES.get('rule_map', {}).items():
        for rid, e in rules.items():
            out['gap_map'].append(dict(channel=ch, rule=rid, **e))
    json.dump(out, open(os.path.join(R3, 'eval', 'analysis.json'), 'w'), indent=1)
    print('videos with all 3 conditions:', len(full))
    for name, p in out['paired'].items():
        print('\n==', name)
        for k, v in p.items(): print(f'  {k:32} {v}')
    print('\n== slots vs hand labels'); [print(' ', k, v) for k, v in out['slots'].items()]
    print('\n== measured slots'); [print(' ', k, v) for k, v in out['measured_slots'].items()]

if __name__ == '__main__' and len(sys.argv) == 1:
    main()

def per_feature():
    """Signed and absolute error per text feature, script vs real, in channel-IQR units; const = train median."""
    from features import feats, chunks_from_text
    from evaluate import TEXT, PUNCT, iqr, TS
    out = {}
    for vid, r in REAL.items():
        ch = r['channel']; manual = r['captions'] == 'manual'
        for c in CONDS:
            p = os.path.join(R3, 'scripts', c, f'{vid}.md')
            if not os.path.exists(p): continue
            narr = parse(p)[0]
            if not narr: continue
            f = feats(chunks_from_text(narr), True)
            for k in TEXT:
                if (k in PUNCT and not manual) or r.get(k) is None or not iqr(ch, k) or f.get(k) is None: continue
                q = iqr(ch, k)
                d = out.setdefault(k, {}).setdefault(c, {'abs': [], 'signed': [], 'const': []})
                d['abs'].append(abs(f[k] - r[k]) / q); d['signed'].append((f[k] - TS[ch]['all'][k]['median']) / q)
                if c == 'base': out[k].setdefault('const', []).append(abs(TS[ch]['all'][k]['median'] - r[k]) / q)
    res = {}
    for k, d in out.items():
        res[k] = {'const_abs': round(st.mean(d['const']), 2) if d.get('const') else None}
        for c in CONDS:
            if c in d: res[k][c] = {'abs': round(st.mean(d[c]['abs']), 2), 'bias_vs_train_median': round(st.median(d[c]['signed']), 2), 'n': len(d[c]['abs'])}
    json.dump(res, open(os.path.join(R3, 'eval', 'per_feature.json'), 'w'), indent=1)
    for k, v in res.items(): print(f'{k:13}', v)

if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'features':
    per_feature()
