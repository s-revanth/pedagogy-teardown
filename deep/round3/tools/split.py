"""Freeze the round-3 train/test split.

TRAIN-EXCLUDED (never test): the 108 deep-analysis videos (tracker.csv), the 12 round-1 videos, the 18 round-2 holdouts.
TEST per channel: the 3 videos already picked in tests.tsv, plus random others (seed 42) until there are 10, drawn from
corpus videos 240-2700 s long, preferring manual captions (punctuation makes text features reliable).
Channels with too few videos get every eligible remaining one (reported).
TRAIN = every other corpus transcript for that channel (used only to fit feature bands).

Moves test transcripts into round3/compact (a folder generators may not read) and removes them from corpus/compact.
Writes round3/split.json and rewrites round3/tests.tsv (channel, id, title, duration, captions).
"""
import csv, glob, json, os, random, shutil

DEEP = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R3 = os.path.join(DEEP, 'round3'); CC = os.path.join(DEEP, 'corpus', 'compact')
random.seed(42)

excluded = {r['id'] for r in csv.DictReader(open(os.path.join(DEEP, 'tracker.csv')))}
excluded |= {l.split('\t')[1] for l in open(os.path.join(DEEP, 'holdout', 'heldout.tsv'))}
excluded |= {json.load(open(f)).get('video_id') for f in glob.glob(os.path.join(DEEP, '..', 'transcripts', '*.json'))}

meta = {}
for l in open(os.path.join(DEEP, 'corpus', 'meta.tsv')):
    ch, vid, dur, date, src, title = l.rstrip('\n').split('\t', 5)
    meta[vid] = dict(channel=ch, id=vid, duration=int(float(dur)) if dur not in ('NA', '') else 0, date=date, captions=src, title=title)

picked = {}
for l in open(os.path.join(R3, 'tests.tsv')):
    p = l.rstrip('\n').split('\t'); picked.setdefault(p[0], []).append(p[1])

split = {'train': {}, 'test': {}, 'notes': {}}
for ch in sorted({m['channel'] for m in meta.values()}):
    have = lambda v: os.path.exists(os.path.join(CC, f'{v}.txt')) or os.path.exists(os.path.join(R3, 'compact', f'{v}.txt'))
    pool = [m for m in meta.values() if m['channel'] == ch and m['id'] not in excluded and have(m['id'])]
    test = [v for v in picked.get(ch, []) if v in meta]
    elig = [m for m in pool if m['id'] not in test and 240 <= m['duration'] <= 2700]
    manual = [m['id'] for m in elig if m['captions'] == 'manual']; auto = [m['id'] for m in elig if m['captions'] != 'manual']
    random.shuffle(manual); random.shuffle(auto)
    test += (manual + auto)[:10 - len(test)]
    split['test'][ch] = test
    split['train'][ch] = [m['id'] for m in pool if m['id'] not in test]
    split['notes'][ch] = f'test={len(test)} train_corpus={len(split["train"][ch])} (+deep/holdout training videos)'

os.makedirs(os.path.join(R3, 'compact'), exist_ok=True)
rows = []
for ch, ids in split['test'].items():
    for v in ids:
        src, dst = os.path.join(CC, f'{v}.txt'), os.path.join(R3, 'compact', f'{v}.txt')
        if os.path.exists(src):
            if not os.path.exists(dst): shutil.copy(src, dst)
            os.remove(src)  # keep test transcripts out of the corpus folder
        m = meta[v]; rows.append(f"{ch}\t{v}\t{m['title']}\t{m['duration']}\t{m['captions']}")
open(os.path.join(R3, 'tests.tsv'), 'w').write('\n'.join(rows) + '\n')
json.dump(split, open(os.path.join(R3, 'split.json'), 'w'), indent=1)
for ch, n in split['notes'].items(): print(ch, n)
