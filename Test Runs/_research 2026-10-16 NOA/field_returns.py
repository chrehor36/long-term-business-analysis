# Field returns: operating income / year-end total assets, from each filer's own XBRL (10-K / 40-F facts).
import json
def ser(path,tag,acc=False):
    g=json.load(open(path))['facts']['us-gaap'][tag]; out={}
    from datetime import date
    for u,arr in g['units'].items():
        for x in arr:
            f=x.get('form','')
            if not (f.startswith('40-F') or f.startswith('10-K')): continue
            if 'start' in x:
                s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
                if not (350<(e-s).days<380): continue
            if x['end'][5:]!='12-31': continue
            k=int(x['end'][:4])
            if k not in out or x['accn']>out[k][1]: out[k]=(x['val'],x['accn'])
    return out
yrs=range(2016,2026)
rows={}
for name,p in [('NOA','cache/facts.json'),('GVA','cache/peers/GVA_facts.json'),('NC','cache/peers/NC_facts.json'),('STRL','cache/peers/STRL_facts.json')]:
    oi=ser(p,'OperatingIncomeLoss'); a=ser(p,'Assets')
    eq=ser(p,'IncomeLossFromEquityMethodInvestments') if name=='NOA' else {}
    r=[]; r2=[]
    for y in yrs:
        v=oi[y][0]/a[y][0]; r.append(v)
        if name=='NOA': r2.append((oi[y][0]+eq.get(y,(0,))[0])/a[y][0])
    print(name,' '.join(f'{y}:{v*100:5.1f}' for y,v in zip(yrs,r)),f'| mean {sum(r)/len(r)*100:.1f}%', '| last accn', oi[2025][1])
    if r2: print(name+'+equity',' '.join(f'{y}:{v*100:5.1f}' for y,v in zip(yrs,r2)),f'| mean {sum(r2)/len(r2)*100:.1f}%')
