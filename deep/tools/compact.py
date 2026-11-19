"""transcripts/<id>.json -> compact/<id>.txt with ~15 s timestamped lines."""
import json, glob, os, sys
os.makedirs('compact', exist_ok=True)
for f in glob.glob('transcripts/*.json'):
    o=f"compact/{os.path.basename(f)[:-5]}.txt"
    if os.path.exists(o): continue
    d=json.load(open(f)); out=[]; buf=[]; t0=None
    for s in d['segments']:
        t0 = s['start'] if t0 is None else t0; buf.append(s['text'].replace('\n',' '))
        if s['end']-t0>=15: out.append(f"[{int(t0//60)}:{int(t0%60):02d}] {' '.join(buf)}"); buf=[]; t0=None
    if buf: out.append(f"[{int(t0//60)}:{int(t0%60):02d}] {' '.join(buf)}")
    open(o,'w').write(f"# {d.get('title')} | {d.get('uploader')} | {d.get('duration')}s | captions: {d.get('source')}\n"+'\n'.join(out))
