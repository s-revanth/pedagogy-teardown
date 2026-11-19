"""Fetch held-out transcripts listed in heldout.tsv via the local youtube-downloader service, then write compact/<id>.txt."""
import json, os, time, urllib.request, sys
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for line in open('heldout.tsv'):
    ch, vid, title, dur = line.rstrip('\n').split('\t')
    out = f'transcripts/{vid}.json'
    if not os.path.exists(out):
        for attempt in range(3):
            try:
                d = json.load(urllib.request.urlopen(f'http://127.0.0.1:8765/api/transcript?url={vid}&timestamps=true', timeout=180))
                if not d.get('segments'): raise ValueError(d.get('error') or 'no segments')
                json.dump(d, open(out, 'w')); break
            except Exception as e:
                print('ERR', vid, e, flush=True); time.sleep(10 * (attempt + 1))
        else: continue
        time.sleep(4)
    d = json.load(open(out)); lines = []; buf = []; t0 = None
    for s in d['segments']:
        t0 = s['start'] if t0 is None else t0; buf.append(s['text'].replace('\n', ' '))
        if s['end'] - t0 >= 15: lines.append(f"[{int(t0//60)}:{int(t0%60):02d}] {' '.join(buf)}"); buf = []; t0 = None
    if buf: lines.append(f"[{int(t0//60)}:{int(t0%60):02d}] {' '.join(buf)}")
    open(f'compact/{vid}.txt', 'w').write(f"# {d.get('title')} | {d.get('uploader')} | {d.get('duration')}s | captions: {d.get('source')}\n" + '\n'.join(lines))
    print(ch, vid, 'ok', len(lines), 'lines', flush=True)
