import json,sys
d=json.load(open(sys.argv[1]))
g=d['facts']['us-gaap']
tags=sys.argv[2].split(',')
def annual(tag):
    if tag not in g: return {}
    out={}
    for u,arr in g[tag]['units'].items():
        for x in arr:
            if x.get('form','').startswith('40-F') and x.get('fp')=='FY':
                fy=x['end'][:4]
                if 'start' in x:
                    s=x['start']; 
                    if int(x['end'][:4])-int(s[:4])>1 or (x['end'][5:7]!='12'): continue
                    if s[5:7]!='01': continue
                if x['end'][5:]!='12-31': continue
                out.setdefault(fy,(x['val'],x['accn'],u))
                # prefer latest filing
                if x['accn']>out[fy][1]: out[fy]=(x['val'],x['accn'],u)
    return out
for t in tags:
    a=annual(t)
    print(t, {k:round(v[0]/1e6,1) if isinstance(v[0],(int,float)) and abs(v[0])>1e4 else v[0] for k,v in sorted(a.items()) if k>='2014'})
