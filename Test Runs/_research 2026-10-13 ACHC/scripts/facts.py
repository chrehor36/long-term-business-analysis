import json,sys
d=json.load(open(sys.argv[1]))
g=d['facts']['us-gaap']
tags=sys.argv[2].split(',')
for t in tags:
    if t not in g: print('MISSING',t); continue
    u=list(g[t]['units'].keys())[0]
    vals={}
    for x in g[t]['units'][u]:
        if x.get('fp')=='FY' and x.get('form','').startswith('10-K'):
            if 'start' in x:
                # annual duration ~ 1yr
                from datetime import date
                s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
                if (e-s).days<350: continue
            key=x['end']
            # keep latest filed
            if key not in vals or x['filed']>vals[key][1]: vals[key]=(x['val'],x['filed'])
    print(t, ' '.join('%s:%.1f'%(k[:4],v[0]/1e6) for k,v in sorted(vals.items()) if k>='2015'))
