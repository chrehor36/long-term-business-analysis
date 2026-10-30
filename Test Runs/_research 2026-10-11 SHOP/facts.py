import json, sys
d = json.load(open('cache/facts.json'))
g = d['facts'].get('us-gaap', {})
def annual(tag):
    if tag not in g: return {}
    out = {}
    for unit, rows in g[tag]['units'].items():
        for r in rows:
            if r.get('fp') == 'FY' and r.get('form') in ('10-K','40-F','20-F','10-K/A','40-F/A'):
                if 'start' in r:
                    from datetime import date
                    s = date.fromisoformat(r['start']); e = date.fromisoformat(r['end'])
                    if (e - s).days < 350: continue
                key = r['end'][:4]
                out.setdefault(key, (r['val'], r['accn'], r['form']))  # first filed
    return out
tags = sys.argv[1:]
for t in tags:
    a = annual(t)
    print(t, {k: round(v[0]/1e6,1) for k, v in sorted(a.items())})
