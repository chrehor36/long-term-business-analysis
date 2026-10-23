import json, sys
d = json.load(open(sys.argv[1]))
g = d['facts']['us-gaap']
def annual(tag):
    if tag not in g: return {}
    out = {}
    for unit, arr in g[tag]['units'].items():
        for x in arr:
            if x.get('fp') == 'FY' and x.get('form') in ('10-K','10-K/A') and 'start' in x:
                from datetime import date
                s = date.fromisoformat(x['start']); e = date.fromisoformat(x['end'])
                if 350 < (e - s).days < 380:
                    y = e.year
                    # keep latest filed
                    if y not in out or x['filed'] > out[y][1]:
                        out[y] = (x['val'], x['filed'])
    return {k: v[0] for k, v in out.items()}
tags = sys.argv[2:]
years = range(2014, 2026)
print('tag'.ljust(60), ' '.join(str(y).rjust(8) for y in years))
for t in tags:
    a = annual(t)
    print(t[:60].ljust(60), ' '.join((f"{a[y]/1e6:8.1f}" if y in a else '       -') for y in years))
