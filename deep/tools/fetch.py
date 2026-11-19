"""Resumable, rate-limited transcript fetch. Updates tracker.csv 'transcript' column: done | failed:<reason>."""
import csv, json, os, shutil, time, urllib.request, glob
T='tracker.csv'; old={json.load(open(f))['video_id']:f for f in glob.glob('../transcripts/*.json')}
def load(): return list(csv.DictReader(open(T)))
def save(rows):
    w=csv.DictWriter(open(T+'.tmp','w'),fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows); os.replace(T+'.tmp',T)
delay=8
while True:
    rows=load(); todo=[r for r in rows if r['transcript']!='done' and not r['transcript'].startswith('failed:permanent')]
    if not todo: break
    r=todo[0]; out=f"transcripts/{r['id']}.json"
    try:
        if r['id'] in old: shutil.copy(old[r['id']],out)
        else:
            d=json.load(urllib.request.urlopen(f"http://127.0.0.1:8765/api/transcript?url={r['id']}&timestamps=true",timeout=180))
            if not d.get('segments'): raise ValueError(d.get('error') or 'no segments')
            json.dump(d,open(out,'w'))
        r['transcript']='done'; delay=max(8,delay*0.8)
    except Exception as e:
        n=int(r['transcript'].split(':')[1]) if r['transcript'].startswith('failed:') and r['transcript'].split(':')[1].isdigit() else 0
        r['transcript']=f'failed:{n+1}' if n<3 else 'failed:permanent'; delay=min(900,delay*2); print('ERR',r['id'],e,flush=True)
    save([r if x['id']==r['id'] else x for x in load()]); print(r['id'],r['transcript'],f'next in {delay:.0f}s',flush=True)
    time.sleep(delay)
