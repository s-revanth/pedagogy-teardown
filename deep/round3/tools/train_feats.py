"""Cache per-video features for every quality-passing TRAINING video (test ids excluded). -> train_feats.json"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from features import feats, chunks_from_transcript, quality, meta, DEEP, R3
split = json.load(open(os.path.join(R3, 'split.json'))); M = meta()
test = {v for ids in split['test'].values() for v in ids}; out = {}
for v, m in M.items():
    if m['channel'] not in split['train'] or v in test or m['duration'] < 120: continue
    p = os.path.join(DEEP, 'corpus', 'compact', f'{v}.txt')
    if not os.path.exists(p): continue
    ck = chunks_from_transcript(p, m['duration'])
    if not quality(ck, m['duration'])[0]: continue
    out[v] = dict(channel=m['channel'], title=m['title'], duration=m['duration'], captions=m['captions'], date=m['date'], **feats(ck, m['captions'] == 'manual', m['duration']))
json.dump(out, open(os.path.join(R3, 'train_feats.json'), 'w')); print(len(out), 'training videos cached')
