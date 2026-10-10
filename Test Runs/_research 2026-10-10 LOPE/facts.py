import json,sys
from datetime import date
d=json.load(open('cache/facts.json'))['facts']['us-gaap']
want=sys.argv[1:]
for w in want:
    if w not in d: print(w,'NONE'); continue
    u=d[w]['units']; k=list(u)[0]
    rows={}
    for x in u[k]:
        if x.get('fp')=='FY' and x['form'] in('10-K','10-K/A'):
            if 'start' in x:
                s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
                if (e-s).days<350: continue
            rows.setdefault(x['end'][:4],x['val'])
    print(w, {y:round(v/1e6,1) if abs(v)>1e4 else v for y,v in sorted(rows.items()) if y>='2014'})
