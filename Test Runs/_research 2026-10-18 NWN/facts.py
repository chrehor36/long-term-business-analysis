import json,sys
f=json.load(open(sys.argv[1]))['facts']
tags=sys.argv[2].split(',')
for t in tags:
    for ns in ('us-gaap','dei'):
        if t in f.get(ns,{}):
            u=f[ns][t]['units']; k=list(u)[0]
            rows={}
            for r in u[k]:
                if r.get('fp')=='FY' and r['form'].startswith('10-K') and ('frame' in r) and (('start' not in r) or (r['end'][:4]==r['start'][:4] and r['start'][5:]=='01-01')):
                    rows[r['end']]=r['val']
            print(t, ' '.join(f"{e[:4]}:{v/1e6:.1f}" for e,v in sorted(rows.items()) if e>='2014'))
