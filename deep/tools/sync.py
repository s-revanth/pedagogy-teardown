"""Mark analysis status in tracker.csv from files present in analyses/."""
import csv, os, json, collections
rows=list(csv.DictReader(open('tracker.csv')))
for r in rows:
    j=f"analyses/{r['id']}.json"
    if os.path.exists(j) and os.path.exists(f"analyses/{r['id']}.md"):
        try: json.load(open(j)); r['analysis']='done'
        except Exception: r['analysis']='bad-json'
w=csv.DictWriter(open('tracker.csv.tmp','w'),fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows); os.replace('tracker.csv.tmp','tracker.csv')
print('transcript',dict(collections.Counter(r['transcript'] for r in rows)),'analysis',dict(collections.Counter(r['analysis'] for r in rows)))
