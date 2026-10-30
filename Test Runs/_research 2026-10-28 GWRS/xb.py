import json,sys
d=json.load(open(sys.argv[1]))['facts']['us-gaap']
tags=sys.argv[2:]
for t in tags:
    if t not in d: print(t,'MISSING'); continue
    u=list(d[t]['units'].values())[0]
    out={}
    for x in u:
        if x.get('fp')=='FY' and x['form'].startswith('10-K'):
            if 'start' in x:
                from datetime import date
                s=date.fromisoformat(x['start']);e=date.fromisoformat(x['end'])
                if (e-s).days<300: continue
            out.setdefault(x['end'],x['val'])  # first-filed
    print(t, {k:round(v/1e3,0) if abs(v)>1000 else v for k,v in sorted(out.items()) if k>='2014'})
