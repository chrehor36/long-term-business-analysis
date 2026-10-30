import json, sys
d = json.load(open(sys.argv[1]))['facts']['us-gaap']
tags = sys.argv[2].split(',')
for t in tags:
    if t not in d: print(t, 'MISSING'); continue
    u = d[t]['units']; k = list(u)[0]
    rows = {}
    for f in u[k]:
        if f.get('fp') == 'FY' and f['form'].startswith('10-K') and f.get('frame','').startswith('CY') and len(f.get('frame',''))==6:
            rows[f['end']] = f['val']
        elif f.get('fp')=='FY' and f['form'].startswith('10-K') and 'start' in f:
            # annual duration
            from datetime import date
            s = date.fromisoformat(f['start']); e = date.fromisoformat(f['end'])
            if 360 <= (e-s).days <= 370 and f['end'] not in rows: rows[f['end']] = f['val']
    print(t, ' '.join(f"{e[:7]}:{v/1e6:.1f}" for e, v in sorted(rows.items()) if e >= '2014'))
