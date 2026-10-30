import json, sys
d = json.load(open(sys.argv[1]))
g = d['facts']['us-gaap']
tags = sys.argv[2].split(',')
for t in tags:
    if t not in g: print(t, 'MISSING'); continue
    u = g[t]['units']
    for unit, rows in u.items():
        seen = {}
        for r in rows:
            if r.get('fp') == 'FY' and r['form'] in ('10-K',) and 'frame' in r or (r.get('fp')=='FY' and r['form']=='10-K'):
                if 'start' in r:
                    s, e = r['start'], r['end']
                    # annual durations only
                    if int(e[:4]) - int(s[:4]) == 1 or (e[5:7]=='12' and s[5:7]=='01' and e[:4]==s[:4]):
                        if e[5:7]=='12' and s[5:7]=='01':
                            seen[e[:4]] = (r['val'], r['accn'])
                else:
                    if r['end'][5:7]=='12':
                        seen[r['end'][:4]] = (r['val'], r['accn'])
        print(t, unit, {k: seen[k][0] for k in sorted(seen) if k >= '2015'})
