"""Join hand-annotated beats (work/beats/*.json) with timestamped transcripts.

Outputs beats.csv, work/stats.json and wpm_by_novelty.png.
Words in a beat = caption segments whose midpoint falls inside [start, end).
'admin' beats (sponsors, outros) are excluded from WPM and share metrics.
"""
import csv, glob, json, os, re, statistics as st
from collections import Counter, defaultdict

LEVELS = {"H": "Home", "B": "Bridge", "N": "New idea", "I": "New interface"}
KEY_PATTERNS = {"aleph null": r"\b(alf|aleph)\s*(null|n|nol|nought)\b|\balol\b|\balfl\b"}

def secs(t):
    if t in (None, "none"): return None
    m, s = t.split(":"); return int(m) * 60 + float(s)

def fmt(t): return "none" if t is None else f"{int(t // 60)}:{int(t % 60):02d}"

rows, stats = [], {}
for bf in sorted(glob.glob("work/beats/*.json")):
    slug = os.path.basename(bf)[:-5]
    b = json.load(open(bf)); segs = json.load(open(f"transcripts/{slug}.json"))["segments"]
    b["end"] = min(b["end"], max(g["end"] for g in segs) + 1)
    starts = [secs(x[0]) for x in b["beats"]]; ends = starts[1:] + [b["end"]]
    per_level = defaultdict(lambda: [0, 0.0]); speech = defaultdict(float); beat_durs = defaultdict(list); tag_counts = Counter(); content_t = 0.0; concrete_t = 0.0
    for (ts, lvl, tags, para), s, e in zip(b["beats"], starts, ends):
        words = sum(len(g["text"].split()) for g in segs if s <= (g["start"] + g["end"]) / 2 < e)
        dur = e - s; wpm = words / dur * 60 if dur > 0 else 0
        tl = tags.split("|")
        rows.append({"video": f'{b["channel"]}: {b["title"]}', "start": fmt(s), "end": fmt(e), "words": words,
                     "wpm": round(wpm), "novelty_level": LEVELS[lvl], "move_tags": " ".join(tl), "paraphrase": para})
        if "admin" in tl: continue
        per_level[lvl][0] += words; per_level[lvl][1] += dur; content_t += dur; beat_durs[lvl].append(dur)
        iv = sorted((max(g["start"], s), min(g["end"], e)) for g in segs if g["end"] > s and g["start"] < e)
        cur = None
        for a, z in iv:
            if cur and a <= cur[1]: cur[1] = max(cur[1], z)
            else:
                if cur: speech[lvl] += cur[1] - cur[0]
                cur = [a, z]
        if cur: speech[lvl] += cur[1] - cur[0]
        if lvl in "HB": concrete_t += dur
        tag_counts.update(t for t in tl)
    m = b["meta"]
    kt = m["key_term"].lower(); pat = KEY_PATTERNS.get(kt, r"\b" + re.escape(kt) + r"s?\b")
    hits = [g for g in segs if re.search(pat, g["text"].lower())]
    intro = hits[0]["start"] if hits else secs(m["key_term_intro"])
    reps = sum(len(re.findall(pat, g["text"].lower())) for g in segs if intro <= g["start"] < intro + 120)
    nf = secs(m["notation_first"])
    stats[slug] = {
        "channel": b["channel"], "title": b["title"], "id": b["id"], "subject": b["subject"],
        "quality": b.get("transcript_quality", "manual captions"), "runtime": b["end"], "beats": len(b["beats"]),
        "wpm_by_level": {LEVELS[k]: round(v[0] / v[1] * 60) for k, v in per_level.items() if v[1] > 0},
        "share_by_level": {LEVELS[k]: round(v[1] / content_t * 100) for k, v in per_level.items()},
        "silence_pct_by_level": {LEVELS[k]: round((1 - speech[k] / v[1]) * 100) for k, v in per_level.items() if v[1] > 0},
        "median_beat_s_by_level": {LEVELS[k]: round(st.median(v)) for k, v in beat_durs.items()},
        "concrete_share": round(concrete_t / content_t * 100),
        "first_question": m["first_question"], "notation_first": m["notation_first"],
        "notation_setup_pct": None if nf is None else round(nf / b["end"] * 100),
        "key_term": m["key_term"], "key_term_intro": fmt(intro), "key_term_reps_2min": reps,
        "tags": dict(tag_counts), **{k: m[k] for k in ("misconception", "brute_force", "examples", "examples_grow", "ending", "quote", "notation_note")},
    }

with open("beats.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
json.dump(stats, open("work/stats.json", "w"), indent=1)

# Cross-video move catalog
uses = Counter(); total = Counter()
for s in stats.values():
    for t, c in s["tags"].items(): uses[t] += 1; total[t] += c
json.dump({t: {"videos": uses[t], "beats": total[t]} for t, _ in uses.most_common()}, open("work/moves.json", "w"), indent=1)

# Chart: small multiples, one panel per video, cross-video median as reference
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
order = ["Home", "Bridge", "New idea", "New interface"]
med = [st.median([s["wpm_by_level"][l] for s in stats.values() if l in s["wpm_by_level"]]) for l in order]
fig, axes = plt.subplots(3, 4, figsize=(14, 9.5), sharex=True, sharey=True)
ink, ink2, grid, blue, ref = "#0b0b0b", "#52514e", "#e6e5e0", "#2a78d6", "#a3a29c"
for ax, (slug, s) in zip(axes.flat, stats.items()):
    xs = [i for i, l in enumerate(order) if l in s["wpm_by_level"]]; ys = [s["wpm_by_level"][order[i]] for i in xs]
    ax.plot(range(4), med, color=ref, lw=1.5, ls=(0, (3, 2)), zorder=1)
    ax.plot(xs, ys, color=blue, lw=2, marker="o", ms=6, mec="white", mew=1.5, zorder=3)
    for x, y in zip(xs, ys): ax.annotate(str(y), (x, y), textcoords="offset points", xytext=(0, 7), ha="center", fontsize=8, color=ink2)
    ax.set_title(f"{s['channel']}\n" + (lambda t: t[:34] + ("…" if len(t) > 34 else ""))(s["title"].split(" (")[0]), fontsize=9, color=ink, loc="left")
    ax.grid(axis="y", color=grid, lw=0.8); ax.set_axisbelow(True)
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"): ax.spines[sp].set_color(grid)
    ax.tick_params(colors=ink2, labelsize=8)
    ax.set_xticks(range(4), ["Home", "Bridge", "New\nidea", "New\ninterface"])
ax0 = axes.flat[0]; ax0.set_ylim(80, 260)
for ax in axes[:, 0]: ax.set_ylabel("Words per minute", fontsize=9, color=ink2)
fig.suptitle("Words per minute by novelty level, per video", x=0.01, ha="left", fontsize=14, color=ink, fontweight="bold")
fig.text(0.01, 0.945, "Blue: the video. Dashed gray: median across all 12 videos. Sponsor and outro beats excluded.", fontsize=9.5, color=ink2)
fig.tight_layout(rect=(0, 0, 1, 0.93)); fig.savefig("wpm_by_novelty.png", dpi=160, facecolor="#fcfcfb")
print("median wpm by level:", dict(zip(order, med)))
