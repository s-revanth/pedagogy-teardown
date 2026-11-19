"""Score round-3 scripts with the 0-100 rubric, using both critics' JSON plus measured transcript stats.

Rubric (per script, per critic, then averaged over critics):
  arc 20      0.5 * (Kendall tau of shared beat types, rescaled 0-1) + 0.5 * Jaccard of beat-type sets
  timing 15   1 - 2 * mean abs error over 5 anchors (question, concrete object, new idea, notation, payoff), floor 0;
              both null -> 0 error, one null -> 0.5 error
  moves 25    0.4 * precision(top5 in real present) + 0.4 * overlap(top5 vs real top5) + 0.2 * absent3 accuracy
  slots 20    mean of critic verdicts over the fixed slots (hit 1, near 0.5, miss 0)
  params 10   5 if wpm within 10% of measured wpm; 5 if median beat within 25% of the critic's real median beat
  voice 10    (critic voice - 1) / 4
Quality (1-5, standalone teaching quality) is reported separately and is not part of the 100.

usage: python3 score.py <key_dir>   -> writes scores/results.json and prints tables
"""
import glob, json, os, re, statistics as st, sys
from itertools import combinations

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANCHORS = ['first_question_frac', 'first_concrete_object_frac', 'first_new_idea_frac', 'first_notation_frac', 'payoff_frac']

def slots_of(path):
    blocks = re.findall(r'```json\s*(\{.*?\})\s*```', open(path).read(), re.S)
    for b in reversed(blocks):
        try: return json.loads(b)
        except json.JSONDecodeError: continue
    return None

def measured_wpm(vid, dur):
    txt = open(os.path.join(ROOT, 'compact', f'{vid}.txt')).read().split('\n', 1)[1]
    txt = re.sub(r'\[\d+:\d{2}\]', ' ', txt); txt = re.sub(r'\[[^\]]*\]', ' ', txt)
    return len(txt.split()) / (dur / 60)

def tau(a, b):
    def first(seq):
        o = []
        for x in seq:
            if x not in o: o.append(x)
        return o
    a, b = first(a or []), first(b or [])
    shared = [x for x in a if x in b]
    if len(shared) < 2: return 0.0
    ra = {x: i for i, x in enumerate(x for x in a if x in shared)}; rb = {x: i for i, x in enumerate(x for x in b if x in shared)}
    c = d = 0
    for x, y in combinations(shared, 2):
        s = (ra[x] - ra[y]) * (rb[x] - rb[y])
        c += s > 0; d += s < 0
    return (c - d) / (c + d) if c + d else 0.0

def num(x):
    try: return float(x)
    except (TypeError, ValueError): return None

def score(pred, real, verdicts, voice, real_wpm):
    s = {}
    pb, rb = pred.get('beat_sequence') or [], real.get('beat_sequence') or []
    jac = len(set(pb) & set(rb)) / max(1, len(set(pb) | set(rb)))
    s['arc'] = 20 * (0.5 * (tau(pb, rb) + 1) / 2 + 0.5 * jac)
    errs = []
    for k in ANCHORS:
        p, r = num(pred.get(k)), num(real.get(k))
        errs.append(0 if p is None and r is None else 0.5 if p is None or r is None else abs(p - r))
    s['timing'] = 15 * max(0.0, 1 - 2 * st.mean(errs))
    present = set(real.get('present_moves') or []) | set(real.get('top5_moves') or [])
    top5 = pred.get('top5_moves') or []
    prec = len([m for m in top5 if m in present]) / 5
    over = len(set(top5) & set(real.get('top5_moves') or [])) / 5
    absent = len([m for m in (pred.get('absent3_moves') or []) if m not in present]) / 3
    s['moves'] = 25 * (0.4 * prec + 0.4 * over + 0.2 * absent)
    v = [{'hit': 1, 'near': .5}.get(x, 0) for x in (verdicts or {}).values()]
    s['slots'] = 20 * (st.mean(v) if v else 0)
    pw, rmb, pmb = num(pred.get('wpm')), num(real.get('median_beat_s')), num(pred.get('median_beat_s'))
    s['params'] = (5 if pw and abs(pw - real_wpm) / real_wpm <= .10 else 0) + (5 if pmb and rmb and abs(pmb - rmb) / rmb <= .25 else 0)
    s['voice'] = 10 * ((voice or 1) - 1) / 4
    s['total'] = sum(s.values())
    return s

def kappa(pairs):
    cats = ['hit', 'near', 'miss']; n = len(pairs)
    if not n: return None
    po = sum(a == b for a, b in pairs) / n
    pe = sum((sum(a == c for a, _ in pairs) / n) * (sum(b == c for _, b in pairs) / n) for c in cats)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0

def main(key_dir):
    tests = [l.rstrip('\n').split('\t') for l in open(os.path.join(ROOT, 'tests.tsv'))]
    rows, pairs = [], []
    for ch, vid, title, dur in tests:
        kf = os.path.join(key_dir, f'{ch}.key.json')
        crit = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(ROOT, 'scores', f'{ch}_[AB].json')))]
        if not os.path.exists(kf) or len(crit) < 2: continue
        key = json.load(open(kf))[vid]; rw = measured_wpm(vid, int(dur))
        for lab, cond in key.items():
            pred = slots_of(os.path.join(ROOT, 'scripts', cond, f'{vid}.md')) or {}
            per = []
            for c in crit:
                v = c['videos'].get(vid, {}); sc = v.get('scripts', {}).get(lab, {})
                per.append((score(pred, v.get('real', {}), sc.get('slot_verdicts'), sc.get('voice'), rw), sc.get('quality'), v.get('recall_level')))
            va, vb = (crit[0]['videos'].get(vid, {}).get('scripts', {}).get(lab, {}).get('slot_verdicts') or {}), (crit[1]['videos'].get(vid, {}).get('scripts', {}).get(lab, {}).get('slot_verdicts') or {})
            pairs += [(va[k], vb[k]) for k in va if k in vb]
            comp = {k: st.mean(p[0][k] for p in per) for k in per[0][0]}
            q = [p[1] for p in per if p[1]]
            recall = 'strong' if any(p[2] == 'strong' for p in per) else ('weak' if any(p[2] == 'weak' for p in per) else 'none')
            rows.append(dict(channel=ch, id=vid, title=title, cond=cond, recall=recall, quality=st.mean(q) if q else None, real_wpm=round(rw), slots_ok=bool(pred), **{k: round(v, 2) for k, v in comp.items()}))
    out = {'rows': rows, 'kappa_slot_verdicts': kappa(pairs), 'n_pairs': len(pairs)}
    def agg(sel):
        r = {}
        for cond in ['base', 'v1', 'v2']:
            xs = [x for x in rows if x['cond'] == cond and sel(x)]
            if xs: r[cond] = {k: round(st.mean(x[k] for x in xs), 1) for k in ['total', 'arc', 'timing', 'moves', 'slots', 'params', 'voice']} | {'quality': round(st.mean(x['quality'] for x in xs if x['quality']), 2), 'n': len(xs)}
        if 'base' in r:
            b = r['base']['total']
            for c in ['v1', 'v2']:
                if c in r: r[c]['report_value'] = round((r[c]['total'] - b) / (100 - b), 3)
        return r
    out['overall'] = agg(lambda x: True)
    out['overall_no_strong_recall'] = agg(lambda x: x['recall'] != 'strong')
    out['by_channel'] = {ch: agg(lambda x, ch=ch: x['channel'] == ch) for ch in sorted({x['channel'] for x in rows})}
    json.dump(out, open(os.path.join(ROOT, 'scores', 'results.json'), 'w'), indent=1)
    print('kappa', out['kappa_slot_verdicts'], 'pairs', len(pairs))
    for name in ['overall', 'overall_no_strong_recall']:
        print(name); [print(' ', c, v) for c, v in out[name].items()]
    for ch, r in out['by_channel'].items():
        print(ch, {c: (v['total'], v.get('report_value')) for c, v in r.items()})

if __name__ == '__main__':
    main(sys.argv[1])
