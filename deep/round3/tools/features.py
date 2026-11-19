"""Deterministic text features, computed the SAME way on real transcripts and on generated narration.

Input is a list of (position_fraction, text) chunks. For transcripts, position = timestamp / duration.
For scripts, the narration is cut into ~40-word chunks and position = cumulative words / total words.
Features that need punctuation are None for auto-captioned videos (auto captions have no ? or .).

usage:
  python3 features.py fit     -> round3/train_stats.json  (bands per channel, all and by duration band)
  python3 features.py test    -> round3/test_features.json (features of the real test videos)
"""
import glob, json, os, re, statistics as st, sys
from collections import Counter

DEEP = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R3 = os.path.join(DEEP, 'round3')
STOP = set("""a an the and or but if then so of to in on at by for with from as is are was were be been being it its this that these those
there here i you he she we they me him her us them my your his our their what which who whom whose when where why how not no yes do does did
done have has had just very really also can could would should will shall may might must than too more most some any all each every one two
about into over under out up down off again once only own same such both few other through during before after above below between because
while until like get got going gonna go know think see look make made thing things way well right now let lets okay oh say said want need""".split())
NUMW = set('zero one two three four five six seven eight nine ten eleven twelve twenty thirty forty fifty hundred thousand million billion trillion half quarter percent'.split())
PAT = {
    'hedge': r"\b(probably|maybe|might|perhaps|roughly|approximately|about \d|we don'?t (really )?know|nobody knows|it'?s possible|likely|unclear|estimate[sd]?)\b",
    'example': r"\b(for example|for instance|imagine|let'?s say|suppose|say you|picture this|think of)\b",
    'sponsor': r"\b(sponsor(ed|s)?|brought to you by|thanks to .{0,40} for (supporting|sponsoring)|patreon|brilliant\.org|squarespace|skillshare|audible|nordvpn|link in the description|first \d+ (people|viewers))\b",
    'teaser': r"\b(next video|next time|next episode|in part (two|2)|stay tuned|see you (next|in)|coming up next|upcoming video)\b",
    'roadmap': r"\b(in this video|today (we|i)'?(re| will| am|'ll)?|we'?re going to (look|explore|talk|see|cover)|first,? we'?ll|let'?s start|here'?s the plan|by the end of this)\b",
    'recap': r"\b(to recap|in summary|to sum (it )?up|so to review|let'?s recap|in short|the takeaway)\b",
}

def words(t): return re.findall(r"[a-z0-9']+", t.lower())

def chunks_from_transcript(path, duration):
    lines = open(path).read().split('\n')[1:]
    out = []
    for l in lines:
        m = re.match(r'\[(\d+):(\d{2})\]\s*(.*)', l)
        if m: out.append(((int(m[1]) * 60 + int(m[2])) / max(duration, 1), re.sub(r'\[[^\]]*\]', ' ', m[3])))
    return out

FUNC = set('the and to of a is that it in you this we for on with be are was so as but what not'.split())

def quality(chunks, duration):
    """Reject non-English or partial captions: English function-word share >= 0.18 and timestamps covering >= 70% of runtime
    with no gap longer than 25% of runtime (troll/partial subtitle files fail this)."""
    W = words(' '.join(t for _, t in chunks))
    if len(W) < 200: return False, 'too few words'
    eng = sum(w in FUNC for w in W) / len(W)
    if eng < 0.18: return False, f'non-English ({eng:.2f})'
    ps = [p for p, _ in chunks]
    if max(ps) < 0.7: return False, f'coverage {max(ps):.2f}'
    if any(b - a > 0.25 for a, b in zip(ps, ps[1:])): return False, 'gap > 25%'
    return True, 'ok'

def chunks_from_text(text, size=40):
    w = text.split(); n = max(1, len(w))
    return [(i / n, ' '.join(w[i:i + size])) for i in range(0, len(w), size)]

def feats(chunks, punct=True, duration=None):
    text = ' '.join(t for _, t in chunks); W = words(text); n = max(1, len(W)); c = Counter(W)
    rate = lambda k: 100 * k / n
    f = {'n_words': len(W)}
    f['you_rate'] = rate(c['you'] + c['your'] + c["you're"] + c["you'll"] + c["you've"])
    f['i_rate'] = rate(c['i'] + c['me'] + c['my'] + c["i'm"] + c["i've"] + c["i'll"])
    f['we_rate'] = rate(c['we'] + c['us'] + c['our'] + c["we're"] + c["let's"] + c["we'll"])
    f['num_rate'] = rate(sum(1 for w in W if w.isdigit() or w in NUMW))
    f['ttr1000'] = len(set(W[:1000])) / max(1, min(1000, len(W)))
    for k in ('hedge', 'example'): f[k + '_rate'] = rate(len(re.findall(PAT[k], text.lower())))
    def first(pat, lo=0.0, hi=1.0):
        for p, t in chunks:
            if lo <= p <= hi and re.search(pat, t.lower()): return round(p, 3)
        return None
    f['sponsor_frac'] = first(PAT['sponsor'])
    f['teaser_end'] = first(PAT['teaser'], 0.88) is not None
    f['roadmap_start'] = first(PAT['roadmap'], 0, 0.12) is not None
    f['recap_end'] = first(PAT['recap'], 0.80) is not None
    def seg(lo, hi): return [w for p, t in chunks if lo <= p < hi for w in words(t) if w not in STOP and len(w) > 3]
    a, b = set(seg(0, 0.08)), set(seg(0.92, 1.01))
    f['mirror_jaccard'] = len(a & b) / max(1, len(a | b))
    quint = [Counter(seg(i / 5, (i + 1) / 5)) for i in range(5)]
    cand = set(quint[0]) & set(quint[4]) & set(quint[2])
    best = max(cand, key=lambda w: min(q[w] for q in quint), default=None)
    f['anchor_word'] = best; f['anchor_min_quintile'] = min(q[best] for q in quint) if best else 0
    if punct:
        f['q_rate'] = rate(text.count('?'))
        f['first_q_frac'] = first(r'\?')
        sents = [s for s in re.split(r'[.!?]+', text) if s.strip()]
        f['sent_len'] = st.mean(len(words(s)) for s in sents) if sents else None
    else:
        f['q_rate'] = f['first_q_frac'] = f['sent_len'] = None
    if duration: f['wpm'] = len(W) / (duration / 60)
    return f

NUMERIC = ['wpm', 'you_rate', 'i_rate', 'we_rate', 'num_rate', 'ttr1000', 'hedge_rate', 'example_rate', 'mirror_jaccard',
           'anchor_min_quintile', 'q_rate', 'first_q_frac', 'sent_len', 'sponsor_frac']
BOOLS = ['teaser_end', 'roadmap_start', 'recap_end']

def meta():
    m = {}
    for l in open(os.path.join(DEEP, 'corpus', 'meta.tsv')):
        ch, vid, dur, date, src, title = l.rstrip('\n').split('\t', 5)
        m[vid] = dict(channel=ch, duration=int(float(dur)) if dur not in ('NA', '') else 0, captions=src, date=date, title=title)
    return m

def band(xs):
    xs = sorted(x for x in xs if x is not None)
    if len(xs) < 3: return None
    q = lambda p: xs[min(len(xs) - 1, int(p * (len(xs) - 1) + 0.5))]
    return {'n': len(xs), 'p10': q(.1), 'p25': q(.25), 'median': q(.5), 'p75': q(.75), 'p90': q(.9)}

def fit():
    split = json.load(open(os.path.join(R3, 'split.json'))); M = meta(); stats = {}; dropped = {}
    test = {v for ids in split['test'].values() for v in ids}
    for ch in split['train']:
        rows = []
        for v, m in M.items():
            if m['channel'] != ch or v in test or m['duration'] < 120: continue
            p = os.path.join(DEEP, 'corpus', 'compact', f'{v}.txt')
            if not os.path.exists(p): continue
            ck = chunks_from_transcript(p, m['duration'])
            if not quality(ck, m['duration'])[0]: dropped[ch] = dropped.get(ch, 0) + 1; continue
            f = feats(ck, m['captions'] == 'manual', m['duration'])
            f['short'] = m['duration'] < 600; rows.append(f)
        def summarise(rs):
            s = {k: band([r.get(k) for r in rs]) for k in NUMERIC}
            s.update({k: round(sum(bool(r[k]) for r in rs) / max(1, len(rs)), 3) for k in BOOLS})
            s['sponsor_present'] = round(sum(r['sponsor_frac'] is not None for r in rs) / max(1, len(rs)), 3)
            s['n_videos'] = len(rs); return s
        stats[ch] = {'all': summarise(rows), 'under10min': summarise([r for r in rows if r['short']]), 'over10min': summarise([r for r in rows if not r['short']])}
        print(ch, len(rows), 'train videos, dropped by quality filter:', dropped.get(ch, 0))
    json.dump(stats, open(os.path.join(R3, 'train_stats.json'), 'w'), indent=1)

def test():
    out = {}
    for l in open(os.path.join(R3, 'tests.tsv')):
        ch, vid, title, dur, cap = l.rstrip('\n').split('\t')
        ck = chunks_from_transcript(os.path.join(R3, 'compact', f'{vid}.txt'), int(dur))
        ok, why = quality(ck, int(dur))
        if not ok: print('EXCLUDED test video', ch, vid, why); continue
        out[vid] = dict(channel=ch, title=title, duration=int(dur), captions=cap, **feats(ck, cap == 'manual', int(dur)))
    json.dump(out, open(os.path.join(R3, 'test_features.json'), 'w'), indent=1); print(len(out), 'test videos')

if __name__ == '__main__':
    {'fit': fit, 'test': test}[sys.argv[1]]()
