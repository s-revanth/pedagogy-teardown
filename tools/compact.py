"""Merge caption segments into ~15 s lines: '[start] text' for beat annotation."""
import json, glob, os, sys
def fmt(t): return f"{int(t//60)}:{int(t%60):02d}"
for f in sorted(glob.glob('transcripts/*.json')):
    d = json.load(open(f)); out=[]; buf=[]; t0=None
    for s in d['segments']:
        if t0 is None: t0 = s['start']
        buf.append(s['text'].replace('\n',' '))
        if s['end'] - t0 >= 15:
            out.append(f"[{fmt(t0)}] {' '.join(buf)}"); buf=[]; t0=None
    if buf: out.append(f"[{fmt(t0)}] {' '.join(buf)}")
    name = os.path.basename(f)[:-5]
    open(f'work/compact/{name}.txt','w').write(f"# {d['title']} ({d['duration']}s)\n" + '\n'.join(out))
