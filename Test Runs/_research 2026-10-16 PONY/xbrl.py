import json, sys
d = json.load(open(sys.argv[1]))
g = d['facts'].get('us-gaap') or d['facts'].get('ifrs-full', {})
want = sys.argv[2:] if len(sys.argv) > 2 else None
for tag, v in sorted(g.items()):
    if want and tag not in want: continue
    for unit, rows in v['units'].items():
        fy = {}
        for r in rows:
            if r.get('form') in ('20-F','F-1','F-1/A','424B4','6-K') :
                key = (r.get('start','')[:10], r['end'])
                fy[key] = (r['val'], r['accn'], r.get('form'))
        if not fy: continue
        print(tag, unit)
        for k in sorted(fy):
            print('   ', k, fy[k])
