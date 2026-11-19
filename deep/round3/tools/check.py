"""In-loop checker for v3 generators. Reads ONLY the script and its training-derived card (cards/<id>.json).
usage: python3 deep/round3/tools/check.py deep/round3/scripts/v3/<id>.md
Prints PASS/FAIL per target, then one JSON line {"verified_trace": {...}} to paste into the script."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from features import feats, chunks_from_text
R3 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main(path):
    vid = os.path.basename(path)[:-3]; card = json.load(open(os.path.join(R3, 'cards', f'{vid}.json')))
    t = open(path).read()
    m = re.search(r'<<<NARRATION\s*\n(.*?)\n\s*NARRATION>>>', t, re.S)
    if not m: print('FAIL: no narration block between <<<NARRATION and NARRATION>>>'); return
    f = feats(chunks_from_text(m.group(1)), True)
    slots = None
    for b in re.findall(r'```json\s*(\{.*?\})\s*```', t, re.S):
        try: d = json.loads(b)
        except json.JSONDecodeError: continue
        if 'hook_type' in d: slots = d
    out = {}; npass = nmeas = 0
    print(f"words: {f['n_words']} (target ~{card['target_words']})")
    for k, b in card['targets'].items():
        if k == 'wpm':
            v = float(slots['wpm']) if slots and slots.get('wpm') else None
        else: v = f.get(k)
        if v is None: continue
        ok = b['p25'] <= v <= b['p75']; nmeas += 1; npass += ok
        out[k] = f"{'PASS' if ok else 'FAIL'} {v:.2f} (target {b['p25']}-{b['p75']}, median {b['median']})"
        print(f"  {k:13} {out[k]}" + ('' if ok else ('  -> raise' if v < b['p25'] else '  -> lower')))
    detect = {'sponsor': f['sponsor_frac'] is not None, 'teaser': f['teaser_end'], 'roadmap': f['roadmap_start'], 'recap': f['recap_end']}
    for s, d in card['switches'].items():
        want = d['default'] == 'ON'; ok = bool(detect[s]) == want
        out['switch_' + s] = f"{'PASS' if ok else 'FAIL'} detected={bool(detect[s])} default={d['default']}"
        print(f"  {s:13} {out['switch_' + s]}")
    if slots:
        for k in ('hook_type', 'ending_type'):
            dflt = card[k.replace('_type', '_default')]
            ok = str(slots.get(k)) in dflt
            out[k] = f"{'MATCHES' if ok else 'DIFFERS FROM'} default ({slots.get(k)} vs {dflt})"
            print(f"  {k:13} {out[k]}")
    else: print('  WARN: no slots json found')
    out['summary'] = f'{npass}/{nmeas} numeric targets pass'
    print(out['summary']); print(json.dumps({'verified_trace': out}))

if __name__ == '__main__':
    main(sys.argv[1])
