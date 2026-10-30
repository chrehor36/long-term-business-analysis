import json,sys
f=json.load(open(sys.argv[1]))
g=f['facts']['us-gaap']
def annual(tag):
    if tag not in g: return {}
    out={}
    for u,vals in g[tag]['units'].items():
        for v in vals:
            if v.get('form')=='10-K' and v.get('fp')=='FY':
                fy=v['end'][:4]
                if 'start' in v:
                    from datetime import date
                    s=date.fromisoformat(v['start']);e=date.fromisoformat(v['end'])
                    if (e-s).days<350: continue
                # keep first filed for each end date
                k=v['end']
                if k not in out or v['filed']<out[k][1]: out[k]=(v['val'],v['filed'],v['accn'])
    return out
for tag in sys.argv[2:]:
    d=annual(tag)
    print(tag)
    for k in sorted(d)[-13:]: print('  ',k,round(d[k][0]/1e6,1),d[k][2])
