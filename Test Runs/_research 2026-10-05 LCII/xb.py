import json,sys
d=json.load(open('facts.json'))['facts']['us-gaap']
tags=sys.argv[1:]
for t in tags:
    if t not in d: print(t,'MISSING'); continue
    u=list(d[t]['units'].values())[0]
    out={}
    for x in u:
        if x.get('form')=='10-K' and x.get('fp')=='FY' and 'start' in x:
            from datetime import date
            s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
            if (e-s).days>350:
                out.setdefault(x['end'][:4],x['val'])  # first filed
        elif x.get('form')=='10-K' and 'start' not in x:
            out.setdefault('bs'+x['end'][:4],x['val'])
    print(t, {k:round(v/1e6,1) for k,v in sorted(out.items())})
