import json,sys
d=json.load(open(sys.argv[1]))['facts']['us-gaap']
tags=sys.argv[2:]
for t in tags:
    if t not in d: print(t,'MISSING'); continue
    u=list(d[t]['units'].values())[0]
    rows={}
    for x in u:
        if x.get('fp')=='FY' and x['form'].startswith('10-K'):
            if 'start' in x:
                from datetime import date
                s=date.fromisoformat(x['start']);e=date.fromisoformat(x['end'])
                if (e-s).days<350: continue
            rows.setdefault(x['end'],x)  # first filed
    print(t, ' '.join(f"{k[:4]}:{v['val']/1e6:.1f}" for k,v in sorted(rows.items()) if k>='2014'))
