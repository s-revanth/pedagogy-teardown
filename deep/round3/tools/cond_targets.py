"""Offline check, no generation: does a VIDEO-CONDITIONED constant beat the channel median on the test set?
Predictors (each outputs one number per feature for a test video, using training data only):
  median   channel training median
  dur_k    median of the k training videos closest in log-duration
  date_k   median of the k closest in upload date (style drifts over years)
  both_k   closest by standardized (log-duration, date)
  cap      median of training videos with the same caption type (manual vs auto)
usage: python3 cond_targets.py -> printed table + eval/cond_targets.json"""
import json, math, os, statistics as st, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evaluate import TEXT, PUNCT, iqr, TS, REAL, R3
from features import meta
TR = json.load(open(os.path.join(R3, 'train_feats.json'))); M = meta()
def days(d):
    try: return (int(d[:4]) - 2000) * 365 + int(d[4:6]) * 30 + int(d[6:8])
    except Exception: return None
def pred(vid, how, k):
    r = REAL[vid]; ch = r['channel']; pool = [t for t in TR.values() if t['channel'] == ch]
    dd = days(M.get(vid, {}).get('date', '')); ld = math.log(r['duration'])
    sdur = st.pstdev([math.log(t['duration']) for t in pool]) or 1
    sdat = st.pstdev([days(t['date']) or 0 for t in pool]) or 1
    def dist(t):
        a = abs(math.log(t['duration']) - ld) / sdur
        b = abs((days(t['date']) or 0) - (dd or 0)) / sdat if dd else 0
        return {'dur_k': a, 'date_k': b, 'both_k': math.hypot(a, b)}[how]
    if how == 'cap': near = [t for t in pool if t['captions'] == r['captions']] or pool
    else: near = sorted(pool, key=dist)[:k]
    return {f: st.median([t[f] for t in near if t.get(f) is not None] or [MED(ch, f)]) for f in TEXT}
def err(vid, P):
    r = REAL[vid]; ch = r['channel']; manual = r['captions'] == 'manual'
    e = [abs(P[f] - r[f]) / iqr(ch, f) for f in TEXT if r.get(f) is not None and iqr(ch, f) and (f not in PUNCT or manual)]
    return st.mean(e)
res = {}
MED = lambda ch, f: TS[ch]['all'][f]['median'] if TS[ch]['all'].get(f) else 0
base = {v: err(v, {f: MED(r['channel'], f) for f in TEXT}) for v, r in REAL.items()}
res['median'] = round(st.mean(base.values()), 3)
for how in ('dur_k', 'date_k', 'both_k', 'cap'):
    for k in ((5, 10, 20) if how != 'cap' else (0,)):
        e = {v: err(v, pred(v, how, k)) for v in REAL}
        d = [e[v] - base[v] for v in REAL]; b = sum(x < 0 for x in d); w = sum(x > 0 for x in d)
        res[f'{how}{k or ""}'] = {'err': round(st.mean(e.values()), 3), 'vs_median': round(st.mean(d), 3), 'better': b, 'worse': w}
json.dump(res, open(os.path.join(R3, 'eval', 'cond_targets.json'), 'w'), indent=1)
for k, v in res.items(): print(f'{k:10}', v)
