"""Choose the target predictor by leave-one-out on TRAINING videos only (no test data), then apply it once to test.
Candidates: median, date_k, dur_k, title_k (word overlap of titles), date+title. k in {10, 20}."""
import json, math, os, re, statistics as st, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evaluate import TEXT, PUNCT, iqr, TS, REAL, R3
from features import meta
TR = json.load(open(os.path.join(R3, 'train_feats.json'))); M = meta()
STOPT = set('the a an of and to in is how what why you your are on for with i my it this e01 e02 e03 part episode'.split())
def toks(t): return {w for w in re.findall(r'[a-z]+', t.lower()) if w not in STOPT and len(w) > 2}
def days(d):
    try: return (int(d[:4]) - 2000) * 365 + int(d[4:6]) * 30 + int(d[6:8])
    except Exception: return 0
def MED(ch, f): return TS[ch]['all'][f]['median'] if TS[ch]['all'].get(f) else None
def predict(target, pool, how, k):
    if how == 'median': return {f: MED(target['channel'], f) for f in TEXT}
    sd = st.pstdev([days(t['date']) for t in pool]) or 1; tt = toks(target['title'])
    def score(t):
        dd = abs(days(t['date']) - days(target['date'])) / sd
        jac = len(tt & toks(t['title'])) / max(1, len(tt | toks(t['title'])))
        du = abs(math.log(t['duration']) - math.log(target['duration']))
        return {'date': dd, 'dur': du, 'title': -jac + 0.001 * dd, 'date_title': dd - 2 * jac}[how]
    near = sorted(pool, key=score)[:k]
    return {f: (st.median([t[f] for t in near if t.get(f) is not None]) if any(t.get(f) is not None for t in near) else MED(target['channel'], f)) for f in TEXT}
def err(target, P):
    ch = target['channel']; manual = target['captions'] == 'manual'
    e = [abs(P[f] - target[f]) / iqr(ch, f) for f in TEXT if target.get(f) is not None and P.get(f) is not None and iqr(ch, f) and (f not in PUNCT or manual)]
    return st.mean(e) if e else None
CANDS = [('median', 0)] + [(h, k) for h in ('date', 'dur', 'title', 'date_title') for k in (10, 20)]
if __name__ == '__main__':
    cv = {}
    for how, k in CANDS:
        es = []
        for v, t in TR.items():
            pool = [x for u, x in TR.items() if x['channel'] == t['channel'] and u != v]
            e = err(t, predict(t, pool, how, k))
            if e is not None: es.append(e)
        cv[f'{how}{k or ""}'] = round(st.mean(es), 4)
    best = min(cv, key=cv.get); print('train LOO error:', cv, '\nchosen on train:', best)
    how = re.match(r'[a-z_]+', best)[0]; k = int(best[len(how):] or 0)
    test = {}
    for v, r in REAL.items():
        t = dict(r, date=M[v]['date']); pool = [x for x in TR.values() if x['channel'] == r['channel']]
        test[v] = (err(t, predict(t, pool, how, k)), err(t, predict(t, pool, 'median', 0)))
    d = [a - b for a, b in test.values()]
    print('TEST (applied once):', best, round(st.mean(a for a, _ in test.values()), 3), 'vs median', round(st.mean(b for _, b in test.values()), 3), 'better', sum(x < 0 for x in d), 'worse', sum(x > 0 for x in d))
    json.dump({'cv': cv, 'chosen': best, 'test_err': round(st.mean(a for a, _ in test.values()), 3)}, open(os.path.join(R3, 'eval', 'cv_targets.json'), 'w'), indent=1)
