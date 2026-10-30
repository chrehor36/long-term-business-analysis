import json,sys
f=json.load(open('facts.json'))['facts']['us-gaap']
def ann(tag, unit='USD'):
    if tag not in f: return {}
    out={}
    for u,arr in f[tag]['units'].items():
        if u!=unit: continue
        for x in arr:
            if x.get('form') in ('10-K','10-K/A') and x.get('fp')=='FY':
                # duration facts: require ~1 year
                if 'start' in x:
                    from datetime import date
                    s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
                    if not (350<(e-s).days<380): continue
                yr=x['end'][:4]
                # keep first-filed value per period end (original vintage)
                if yr not in out or x['filed']<out[yr][1]:
                    out[yr]=(x['val'],x['filed'])
    return {k:v[0] for k,v in sorted(out.items())}
tags=sys.argv[1:]
for t in tags:
    unit='shares' if 'Shares' in t or 'Stock' in t and 'Shares' in t else 'USD'
    d=ann(t, 'shares' if t.endswith('Shares') or 'NumberOfShares' in t or 'SharesOutstanding' in t or 'WeightedAverage' in t else 'USD')
    print(t, {k:round(v/1e6,1) for k,v in d.items()})
