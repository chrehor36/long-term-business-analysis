import json,sys
def series(d,tag,fy_only=True,instant=False):
    g=d['facts']['us-gaap'].get(tag)
    if not g: return {}
    out={}
    for x in g['units'].get('USD',[]):
        if not x['form'].startswith('10-K'): continue
        if instant:
            if 'start' in x: continue
        else:
            if 'start' not in x: continue
            # full-year duration
            from datetime import date
            s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
            if not (350<=(e-s).days<=380): continue
        out.setdefault(x['end'],(x['val'],x['accn']))  # first-filed vintage
    return out
for t in sys.argv[1:]:
    d=json.load(open(f'cache/facts_{t}.json' if t!='SR' else 'cache/facts.json'))
    ni=series(d,'NetIncomeLoss'); 
    eq=series(d,'StockholdersEquity',instant=True)
    print(t, d['entityName'])
    ends=sorted(e for e in ni if e>='2015-06')
    tot_ni=0;tot_eq=0;n=0
    for e in ends:
        # prior year-end equity
        pe=[k for k in eq if k<e and (int(e[:4])-int(k[:4]))==1 and k[5:7]==e[5:7]]
        if e in eq and pe:
            a=(eq[e][0]+eq[pe[0]][0])/2
            print(f'  {e} NI {ni[e][0]/1e6:8.1f} avgEq {a/1e6:8.1f} ROE {ni[e][0]/a*100:5.1f}%  {ni[e][1]}')
            if e>='2016': tot_ni+=ni[e][0]; tot_eq+=a; n+=1
    if n: print(f'  span {n} yrs: sum NI / sum avg equity = {tot_ni/tot_eq*100:.1f}%')
