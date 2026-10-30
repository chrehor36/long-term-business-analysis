import json, sys
sys.stdout.reconfigure(encoding='utf-8')
f = json.load(open(sys.argv[1]))
g = f['facts']['us-gaap']
tags = sys.argv[2].split(',')
for t in tags:
    if t not in g: print(t, 'MISSING'); continue
    u = list(g[t]['units'].values())[0]
    byfy = {}
    for x in u:
        if x.get('form') == '10-K' and x.get('fp') == 'FY':
            s, e = x.get('start'), x['end']
            if s and (int(e[:4]) - int(s[:4]) == 1 or s[5:] == '01-01') and e[5:] == '12-31' and s[:4] == e[:4]:
                byfy.setdefault(e[:4], x['val'])  # first-filed
            elif not s and e[5:] == '12-31':
                byfy.setdefault(e[:4], x['val'])
    print(t, ' '.join(f"{y}:{byfy[y]/1e6:,.0f}" for y in sorted(byfy) if y >= '2014'))
