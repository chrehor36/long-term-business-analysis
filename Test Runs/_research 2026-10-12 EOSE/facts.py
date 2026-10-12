import json, sys
sys.path.insert(0, '.')
from fetch import get
cik = int(sys.argv[1]); tags = sys.argv[2].split(',')
d = json.loads(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json', f'companyfacts_{cik}.json'))
g = d['facts'].get('us-gaap', {})
for t in tags:
    if t not in g: print(t, 'MISSING'); continue
    for unit, rows in g[t]['units'].items():
        seen = {}
        for r in rows:
            if r.get('form') not in ('10-K','10-K/A','20-F','10-Q'): continue
            dur = r.get('fp')
            key = (r.get('start',''), r['end'])
            if key in seen: continue
            seen[key] = r
        for (s,e), r in sorted(seen.items(), key=lambda x: x[0][1]):
            if s and sys.argv[3:] and sys.argv[3]=='FY':
                from datetime import date
                ds = date.fromisoformat(s); de = date.fromisoformat(e)
                if (de-ds).days < 350: continue
            print(f'{t:55s} {s:10s} {e:10s} {r["val"]/1e6:12.3f} {r["form"]:6s} {r["accn"]}')
