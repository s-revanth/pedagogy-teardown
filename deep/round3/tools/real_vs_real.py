"""Fair yardstick: how far does a REAL training video of the same channel sit from each test video?
Same metric as fidelity_err (mean |a-b|/IQR over the text features; punctuation features only when both are manual).
A generated script that matches this level is as close to the target as another real episode is.
Seeded: up to 30 training videos per channel (seed 0). -> eval/real_vs_real.json"""
import json, os, random, statistics as st, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from features import feats, chunks_from_transcript, quality, meta, DEEP
from evaluate import TEXT, PUNCT, iqr, REAL, R3
split = json.load(open(os.path.join(R3, 'split.json'))); M = meta()
test = {v for ids in split['test'].values() for v in ids}
rnd = random.Random(0); train = {}
for ch in split['train']:
    vids = sorted(v for v, m in M.items() if m['channel'] == ch and v not in test and m['duration'] >= 120 and os.path.exists(os.path.join(DEEP, 'corpus', 'compact', f'{v}.txt')))
    rnd.shuffle(vids); got = []
    for v in vids:
        ck = chunks_from_transcript(os.path.join(DEEP, 'corpus', 'compact', f'{v}.txt'), M[v]['duration'])
        if not quality(ck, M[v]['duration'])[0]: continue
        f = feats(ck, M[v]['captions'] == 'manual', M[v]['duration']); f['manual'] = M[v]['captions'] == 'manual'; got.append(f)
        if len(got) == 30: break
    train[ch] = got
out = {}
for vid, r in REAL.items():
    ch = r['channel']; manual = r['captions'] == 'manual'; errs = []
    for f in train[ch]:
        e = [abs(f[k] - r[k]) / iqr(ch, k) for k in TEXT if r.get(k) is not None and f.get(k) is not None and iqr(ch, k) and (k not in PUNCT or (manual and f['manual']))]
        if e: errs.append(st.mean(e))
    out[vid] = {'channel': ch, 'rvr_mean': round(st.mean(errs), 3), 'rvr_median': round(st.median(errs), 3), 'rvr_best': round(min(errs), 3), 'n_train': len(errs)}
json.dump(out, open(os.path.join(R3, 'eval', 'real_vs_real.json'), 'w'), indent=1)
print('mean real-vs-real err', round(st.mean(v['rvr_mean'] for v in out.values()), 3), 'median-of-medians', round(st.mean(v['rvr_median'] for v in out.values()), 3))
for ch in sorted(train): print(f'{ch:15}', len(train[ch]), round(st.mean(v['rvr_mean'] for v in out.values() if v['channel'] == ch), 3))
