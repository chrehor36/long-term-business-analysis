import json, sys
exec(open('fetch.py').read().split('if __name__')[0].replace('os.path.abspath(__file__)', 'os.path.abspath("fetch.py")'))
cik = int(sys.argv[1]); tags = sys.argv[2].split(',')
fy_end_month = int(sys.argv[3]) if len(sys.argv) > 3 else 12
f = json.loads(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"))
g = f['facts'].get('us-gaap', {})
for t in tags:
    if t not in g: print(t, 'MISSING'); continue
    u = g[t]['units']; key = list(u)[0]
    best = {}
    for x in u[key]:
        if x.get('form') not in ('10-K','10-K/A'): continue
        if 'start' in x:
            from datetime import date
            s = date.fromisoformat(x['start']); e = date.fromisoformat(x['end'])
            if not (340 <= (e-s).days <= 380): continue
        e = x['end']
        # earliest filed vintage per end date
        if e not in best or x['filed'] < best[e]['filed']: best[e] = x
    print(t, ' '.join(f"{e[:7]}:{best[e]['val']/1e6:.1f}" for e in sorted(best) if e >= '2014'))
