import json,sys
d=json.load(open(sys.argv[1]))
g=d['facts']['us-gaap']
for t in sys.argv[2].split(','):
    if t not in g: print(t,'-'); continue
    out={}
    for u,arr in g[t]['units'].items():
        for x in arr:
            f=x.get('form','')
            if not (f.startswith('40-F') or f.startswith('10-K')): continue
            if 'start' in x:
                from datetime import date
                s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
                if not (350<(e-s).days<380): continue
            k=x['end']
            if k not in out or x['accn']>out[k][1]: out[k]=(x['val'],x['accn'])
    print(t,{k:round(v[0]/1e6,1) for k,v in sorted(out.items()) if k>=sys.argv[3]})
