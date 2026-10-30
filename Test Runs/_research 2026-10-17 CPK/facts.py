import json, sys
d = json.load(open(sys.argv[1]))
g = d['facts']['us-gaap']
tags = sys.argv[2].split(',')
for t in tags:
    if t not in g: print(t, 'MISSING'); continue
    u = list(g[t]['units'].values())[0]
    rows = {}
    for f in u:
        if f.get('form') == '10-K' and f.get('fp') == 'FY':
            dur = f.get('start')
            if dur:
                from datetime import date
                s = date.fromisoformat(f['start']); e = date.fromisoformat(f['end'])
                if (e - s).days < 350: continue
            rows.setdefault(f['end'], (f['val'], f['accn']))  # first filed
    out = ' '.join(f"{k[:4]}:{v[0]/1e6:.1f}" for k, v in sorted(rows.items()) if k >= '2014')
    print(t, out)
