import json, sys
sys.path.insert(0,'scripts'); import facts
from facts import annual
files = {'UTL':'cache/facts.json','ES':'cache/peers/facts_0000072741.json','CPK':'cache/peers/facts_0000019745.json','NWN':'cache/peers/facts_0001733998.json'}
yrs=[str(y) for y in range(2016,2026)]
for name,p in files.items():
    d=json.load(open(p)); facts.g=d['facts']['us-gaap']
    def s(t):
        a=annual(t); return {k[:4]:v[0] for k,v in a.items()}
    ni=s('NetIncomeLoss') or {}
    nic=s('NetIncomeLossAvailableToCommonStockholdersBasic')
    eq=s('StockholdersEquity'); oi=s('OperatingIncomeLoss'); at=s('Assets')
    accs=set(v[2] for v in annual('NetIncomeLoss').values())
    print(name, 'NI accessions sample:', sorted(accs)[-1] if accs else None)
    roe=[];oia=[]
    for y in yrs:
        py=str(int(y)-1)
        n = nic.get(y, ni.get(y))
        if n is not None and y in eq and py in eq: roe.append((y, n/((eq[y]+eq[py])/2)))
        if y in oi and y in at and py in at: oia.append((y, oi[y]/((at[y]+at[py])/2)))
    print(' ROE  ', ' '.join(f"{y}:{r*100:4.1f}" for y,r in roe), ' avg', f"{sum(r for _,r in roe)/len(roe)*100:.1f}" if roe else '')
    print(' OI/A ', ' '.join(f"{y}:{r*100:4.1f}" for y,r in oia), ' avg', f"{sum(r for _,r in oia)/len(oia)*100:.1f}" if oia else '')
