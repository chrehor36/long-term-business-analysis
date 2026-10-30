import json
def series(f,tag,inst):
    g=f['facts']['us-gaap']
    out={}
    if tag not in g: return out
    for u,vals in g[tag]['units'].items():
        for v in vals:
            if v.get('form')!='10-K' or v['end'][5:]!='12-31': continue
            if inst and 'start' in v: continue
            if not inst and ('start' not in v or v['start'][5:]!='01-01'): continue
            y=int(v['end'][:4])
            if y not in out or v['filed']>out[y][1]: out[y]=(v['val'],v['filed'])
    return {k:v[0] for k,v in out.items()}
for t,path in [('CB','cache/facts.json'),('TRV','cache/peers/TRV_facts.json'),('AIG','cache/peers/AIG_facts.json'),('WRB','cache/peers/WRB_facts.json'),('MKL','cache/peers/MKL_facts.json')]:
    f=json.load(open(path))
    ni=series(f,'NetIncomeLossAvailableToCommonStockholdersBasic',False) or {}
    ni2=series(f,'NetIncomeLoss',False)
    eq=series(f,'StockholdersEquity',True)
    gw=series(f,'Goodwill',True); ia=series(f,'IntangibleAssetsNetExcludingGoodwill',True)
    row=[];rt=[]
    for y in range(2015,2026):
        n=ni2.get(y)
        if n is None or y not in eq or y-1 not in eq: row.append('   -  '); rt.append('   -  '); continue
        a=(eq[y]+eq[y-1])/2; row.append(f"{n/a*100:6.1f}")
        tg=lambda yy: eq[yy]-gw.get(yy,0)-ia.get(yy,0)
        try: rt.append(f"{n/((tg(y)+tg(y-1))/2)*100:6.1f}")
        except: rt.append('   -  ')
    print(t,'ROE ',' '.join(row))
    print(t,'ROTE',' '.join(rt))
