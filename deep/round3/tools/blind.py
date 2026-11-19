"""Anonymise one channel's scripts for the critics.

Copies scripts/{base,v1,v2}/<id>.md to scores/<channel>_blind/<id>__<label>.md under random labels P/Q/R
(drawn independently per video), and strips lines that would reveal the condition. The label key is written
OUTSIDE the project (argv[2]) so critics cannot read it.

usage: python3 blind.py <channel> <key_dir>
"""
import json, os, random, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONDS = ['base', 'v1', 'v2']
REVEAL = re.compile(r'(condition|policy|report|\bv1\b|\bv2\b|\bbase\b|pedagogy-teardown|reports/|policy/|exemplar|self-check)', re.I)

def scrub(text):
    out, skipping = [], False
    for line in text.splitlines():
        # Drop the whole self-check section, which cites the condition's sources.
        if re.match(r'#+\s*.*self[- ]check', line, re.I):
            skipping = True; continue
        if skipping and re.match(r'#+\s', line) and not re.search(r'self[- ]check', line, re.I):
            skipping = False
        if skipping:
            continue
        if REVEAL.search(line) and not line.lstrip().startswith(('"', '{', '}', '[', ']')):
            continue  # header/meta lines that name the source; JSON slot lines are kept
        out.append(line)
    return '\n'.join(out)

def main(channel, key_dir):
    ids = [l.split('\t')[1] for l in open(os.path.join(ROOT, 'tests.tsv')) if l.split('\t')[0] == channel]
    dest = os.path.join(ROOT, 'scores', f'{channel}_blind'); os.makedirs(dest, exist_ok=True)
    key = {}
    for vid in ids:
        labels = ['P', 'Q', 'R']; random.shuffle(labels)
        key[vid] = {}
        for cond, lab in zip(CONDS, labels):
            src = os.path.join(ROOT, 'scripts', cond, f'{vid}.md')
            if not os.path.exists(src):
                sys.exit(f'missing {src}')
            open(os.path.join(dest, f'{vid}__{lab}.md'), 'w').write(scrub(open(src).read()))
            key[vid][lab] = cond
    os.makedirs(key_dir, exist_ok=True)
    json.dump(key, open(os.path.join(key_dir, f'{channel}.key.json'), 'w'), indent=1)
    print(channel, 'blinded', len(ids) * 3, 'scripts')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
