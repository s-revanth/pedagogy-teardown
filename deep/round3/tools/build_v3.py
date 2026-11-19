"""Round 4 (v3) inputs. Uses TRAINING data only; each choice below was selected by leave-one-out on training.

  deep/policy_v3/<ch>.md     short channel rulebook: structure base rates (from eval/train_labels.json),
                             switch defaults, channel style notes (C rules from v2; untraced), workflow.
  round3/cards/<id>.json     per-test-video target card built from the 20 training videos nearest by
                             upload date + title words (chosen by tools/cv_targets.py), plus the 2 nearest
                             transcripts as exemplars, structure defaults and a target length.
Test transcripts, test labels and test features are never read here (only title/duration/date metadata from tests.tsv/meta.tsv).
"""
import json, os, re, statistics as st, sys
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cv_targets import predict, TR, toks, days
from features import meta, DEEP, R3
from evaluate import TEXT
M = meta()
LAB = {k: v for k, v in json.load(open(os.path.join(R3, 'eval', 'train_labels.json'))).items() if not k.startswith('_')}
SER = re.compile(r'part|\bE\d|episode|chapter|\(ep', re.I)
SW = {'sponsor': lambda t: t['sponsor_frac'] is not None, 'teaser': lambda t: bool(t['teaser_end']),
      'roadmap': lambda t: bool(t['roadmap_start']), 'recap': lambda t: bool(t['recap_end'])}
LABEL = {'wpm': 'words per minute', 'you_rate': '"you/your" per 100 words', 'i_rate': '"I/me/my" per 100 words', 'we_rate': '"we/us/let\'s" per 100 words',
         'num_rate': 'numbers per 100 words', 'q_rate': 'question marks per 100 words', 'sent_len': 'mean words per sentence',
         'hedge_rate': 'hedges (probably/maybe/roughly...) per 100 words', 'example_rate': 'example cues (for example/imagine/let\'s say...) per 100 words'}

def neighbours(target, k=20):
    pool = [dict(t, id=v) for v, t in TR.items() if t['channel'] == target['channel']]
    sd = st.pstdev([days(t['date']) for t in pool]) or 1; tt = toks(target['title'])
    sc = lambda t: abs(days(t['date']) - days(target['date'])) / sd - 2 * len(tt & toks(t['title'])) / max(1, len(tt | toks(t['title'])))
    return sorted(pool, key=sc)[:k]

def q(xs, p):
    xs = sorted(x for x in xs if x is not None)
    return xs[min(len(xs) - 1, int(p * (len(xs) - 1) + 0.5))] if xs else None

# ---- switch policy chosen by leave-one-out on training: channel rate vs neighbour rate
def switch_cv():
    acc = {s: {'channel': [], 'neighbour': []} for s in SW}
    for v, t in TR.items():
        t = dict(t, id=v); pool = [x for u, x in TR.items() if x['channel'] == t['channel'] and u != v]
        nb = [x for x in neighbours(t) if x['id'] != v]
        for s, f in SW.items():
            cr = sum(f(x) for x in pool) / len(pool); nr = sum(f(x) for x in nb) / len(nb)
            acc[s]['channel'].append((cr >= .5) == f(t)); acc[s]['neighbour'].append((nr >= .5) == f(t))
    return {s: {m: round(sum(a) / len(a), 3) for m, a in d.items()} for s, d in acc.items()}

def hook_default(ch, title):
    c = Counter(v['hook_type'] for v in LAB.values() if v['channel'] == ch)
    if '?' in title and c['question'] >= 2: return 'question or ' + c.most_common(1)[0][0]
    return c.most_common(1)[0][0]

def ending_default(ch, title):
    if SER.search(title): return 'teaser-next'
    return Counter(v['ending_type'] for v in LAB.values() if v['channel'] == ch).most_common(1)[0][0]

def build():
    cv = switch_cv(); print('switch LOO accuracy on train:', cv)
    choice = {s: max(d, key=d.get) for s, d in cv.items()}
    os.makedirs(os.path.join(R3, 'cards'), exist_ok=True); os.makedirs(os.path.join(DEEP, 'policy_v3'), exist_ok=True)
    tests = [l.rstrip('\n').split('\t') for l in open(os.path.join(R3, 'tests.tsv'))]
    for ch, vid, title, dur, cap in tests:
        dur = int(dur); target = {'channel': ch, 'title': title, 'duration': dur, 'date': M[vid]['date']}
        nb = neighbours(target)
        tg = {}
        for f in ['wpm'] + TEXT:
            xs = [t.get(f) for t in nb if t.get(f) is not None]
            if len(xs) >= 3: tg[f] = {'p25': round(q(xs, .25), 2), 'median': round(q(xs, .5), 2), 'p75': round(q(xs, .75), 2), 'n': len(xs)}
        pool = [t for t in TR.values() if t['channel'] == ch]
        sw = {}
        for s, f in SW.items():
            src = nb if choice[s] == 'neighbour' else pool
            r = sum(f(t) for t in src) / len(src); sw[s] = {'rate': round(r, 2), 'default': 'ON' if r >= .5 else 'OFF'}
        sp = [t['sponsor_frac'] for t in nb if t['sponsor_frac'] is not None]
        if sp: sw['sponsor']['position_median'] = round(st.median(sp), 2)
        wpm = tg.get('wpm', {}).get('median', 160)
        ex = [f"deep/corpus/compact/{t['id']}.txt" for t in nb if os.path.exists(os.path.join(DEEP, 'corpus', 'compact', f"{t['id']}.txt"))][:2]
        card = {'id': vid, 'channel': ch, 'title': title, 'duration_s': dur, 'upload_date': M[vid]['date'],
                'targets': tg, 'switches': sw,
                'hook_default': hook_default(ch, title), 'ending_default': ending_default(ch, title),
                'target_words': int(max(500, min(2200, dur / 60 * wpm))),
                'exemplars': ex, 'neighbours_used': len(nb),
                '_how': 'Built from the 20 training videos of this channel nearest by upload date + title words (selected by training LOO), never from the test video.'}
        json.dump(card, open(os.path.join(R3, 'cards', f'{vid}.json'), 'w'), indent=1)
    for ch in sorted({t[0] for t in tests}):
        x = [v for v in LAB.values() if v['channel'] == ch]
        hc = Counter(v['hook_type'] for v in x); ec = Counter(v['ending_type'] for v in x)
        old = open(os.path.join(DEEP, 'policy', f'{ch}.md')).read()
        notes = re.search(r'## C:.*?\n(.*?)\n## D:', old, re.S).group(1).strip()
        notes = re.sub(r'\*\*C(\d)\*\*', r'**S\1**', notes)
        L = [f'# {ch}: v3 rulebook (round 4)', '',
             'This replaces the v2 rulebook and the prose report. Everything here comes from training data only.', '',
             '## 1. Structure: how this channel opens and closes (hand-labelled training videos, n=' + str(len(x)) + ')',
             'Hook (the first spoken content after any sponsor/admin cold open): ' + ', '.join(f'{k} {v}' for k, v in hc.most_common()),
             'Ending (the last CONTENT beat before any sponsor/Patreon outro): ' + ', '.join(f'{k} {v}' for k, v in ec.most_common()), '',
             'Definitions (use these exact meanings in your slots):',
             '- premise-claim: the first sentence states a striking fact, claim or set-up. It is NOT a question.',
             '- question: the first spoken sentence IS a question to the viewer. Uncommon: 18 of 106 training hooks (17%).',
             '- scenario-you: "Imagine you..." / "You are..." puts the viewer in a situation.',
             '- story-anecdote: opens on a dated event or a person\'s story. gag-skit: a comic scene/dialogue. confession: the presenter talks about himself.',
             '- phrase-mirror: the close returns to the opening\'s image, phrase or question (this is the whole "callback to the hook" family; do not use hook-callback).',
             '- impact-coda: closes on a widening takeaway or consequence. teaser-next: names what the next video/part covers. credits-after-result: the result lands, then the video just stops.', '',
             '**Use the card\'s `hook_default` and `ending_default` unless the title or topic clearly demands otherwise.** Do not open with a question just because the topic is a mystery: the channels state a premise first far more often.', '',
             '## 2. Style notes for this channel (from round-2 held-out videos; guidance, not scored)', notes, '',
             '## 3. Numbers and switches come from your per-video card',
             'Your card `deep/round3/cards/<id>.json` has p25/median/p75 targets for this specific video (from its 20 nearest training videos by date and title), the sponsor/teaser/roadmap/recap defaults, a target word count and 2 exemplar transcripts. Aim for the median, stay inside p25-p75.', '',
             '## 4. Verify, do not self-report',
             'After drafting, run `python3 deep/round3/tools/check.py deep/round3/scripts/v3/<id>.md`. It measures your narration with the same code that scores it and prints PASS/FAIL per target. Revise the narration until at least 7 of the measured targets pass, then paste the checker\'s final JSON line into the file as the last ```json block. Never write a trace by hand.',
             ]
        open(os.path.join(DEEP, 'policy_v3', f'{ch}.md'), 'w').write('\n'.join(L) + '\n')
    json.dump({'switch_cv': cv, 'switch_choice': choice}, open(os.path.join(R3, 'eval', 'v3_build.json'), 'w'), indent=1)
    print('choice:', choice, '| cards:', len(tests))

if __name__ == '__main__':
    build()
