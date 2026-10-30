import json, sys
d = json.load(open(sys.argv[1]))
g = d['facts']['us-gaap']
tags = sys.argv[2].split(',')
for t in tags:
    if t not in g: print(t, 'MISSING'); continue
    u = g[t]['units']; unit = list(u)[0]
    vals = {}
    for f in u[unit]:
        if f.get('form') == '10-K' and f.get('fp') == 'FY':
            if 'start' in f:
                from datetime import date
                s = date.fromisoformat(f['start']); e = date.fromisoformat(f['end'])
                if (e - s).days < 350: continue
            y = f['end'][:4]
            # keep the latest-filed value per year (restated)
            if y not in vals or f['filed'] > vals[y][1]:
                vals[y] = (f['val'], f['filed'])
    print(t.ljust(60), ' '.join(f"{y}:{v[0]/1e6:,.0f}" for y, v in sorted(vals.items()) if y >= '2015'))
