import json,sys
d=json.load(open('companyfacts.json'))['facts']['us-gaap']
for t in sys.argv[1:]:
    if t not in d: print(t,'MISSING'); continue
    u=d[t]['units'].get('USD') or list(d[t]['units'].values())[0]
    fy={}
    for x in u:
        if x.get('fp')=='FY' and x['form'].startswith('10-K') and x['start'][5:]=='01-01' and x['end'][5:]=='12-31':
            fy.setdefault(x['end'][:4],x['val'])
    print(t, {k:round(v/1e6,1) for k,v in sorted(fy.items())})
