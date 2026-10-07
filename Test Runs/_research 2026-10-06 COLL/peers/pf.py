import json,sys
t=sys.argv[1]; d=json.load(open(f'peers/{t}_facts.json')); print(d['entityName'])
g=d['facts']['us-gaap']
def annual(tag):
    if tag not in g: return {}
    out={}
    for u,vals in g[tag]['units'].items():
        for v in vals:
            if v.get('fp')=='FY' and v.get('form','').startswith('10-K'):
                s,e=v.get('start'),v['end']
                if not s: continue
                if (int(e[:4])-int(s[:4]))*12+int(e[5:7])-int(s[5:7])<11: continue
                out.setdefault(e[:4],(v['val'],v['accn']))
    return out
for tag in sys.argv[2:]:
    a=annual(tag); print(tag,{k:round(v[0]/1e6,1) for k,v in sorted(a.items()) if k>='2012'})
