# pull annual (10-K, FY, 12-month) values for tags; usage: python -I xb.py TICKER tag1 tag2 ...
import json, sys
t=sys.argv[1]; d=json.load(open(f'cache/cf_{t}.json'))
g=d['facts'].get('us-gaap',{})
for tag in sys.argv[2:]:
    if tag not in g: print(tag,'MISSING'); continue
    u=g[tag]['units']; k=list(u)[0]; out={}
    for f in u[k]:
        if f.get('form','').startswith('10-K') and f.get('fp')=='FY':
            s=f.get('start'); e=f['end']
            if s and (int(e[:4])-int(s[:4]))*12+int(e[5:7])-int(s[5:7]) not in (11,12): continue
            yr=e[:4]
            if yr not in out or f['filed']<out[yr][1]: out[yr]=(f['val'],f['filed'])  # first-filed
    print(tag, ' '.join(f"{y}:{round(v[0]/1e6) if abs(v[0])>1e5 else v[0]}" for y,v in sorted(out.items()) if y>='2014'))
