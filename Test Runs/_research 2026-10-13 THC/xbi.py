# instant (balance sheet) values at fiscal year ends, first-filed in a 10-K; usage: python -I xbi.py TICKER tags...
import json, sys
t=sys.argv[1]; d=json.load(open(f'cache/cf_{t}.json')); g=d['facts'].get('us-gaap',{})
for tag in sys.argv[2:]:
    if tag not in g: print(tag,'MISSING'); continue
    u=g[tag]['units']; k=list(u)[0]; out={}
    for f in u[k]:
        if f.get('form','').startswith('10-K') and 'start' not in f and f['end'][5:]=='12-31':
            y=f['end'][:4]
            if y not in out or f['filed']<out[y][1]: out[y]=(f['val'],f['filed'])
    print(tag,' '.join(f"{y}:{round(v[0]/1e6)}" for y,v in sorted(out.items()) if y>='2015'))
