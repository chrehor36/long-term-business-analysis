import json,datetime
def load(cik):
    F=json.load(open(f'facts/facts_{str(cik).zfill(10)}.json'));return F['facts']['us-gaap']
def annual(g,tags,inst=False):
    out={}
    for t in tags:
        if t not in g: continue
        for u,vals in g[t]['units'].items():
            if u!='USD':continue
            for v in vals:
                if v.get('form') not in ('10-K','10-K/A','10-KT'):continue
                if inst: k=v['end']
                else:
                    if 'start' not in v: continue
                    d=(datetime.date.fromisoformat(v['end'])-datetime.date.fromisoformat(v['start'])).days
                    if not 350<=d<=380: continue
                    k=v['end']
                if k not in out or v['filed']<out[k][1]: out[k]=(v['val'],v['filed'],t)
    return {k:v[0] for k,v in out.items()}
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','RevenueFromContractWithCustomerIncludingAssessedTax','SalesRevenueNet','SalesRevenueServicesNet']
cos={'Hornbeck old (1131227)':(1131227,'2009','2019'),'Helix (866829) 2013-25':(866829,'2013','2025'),'Tidewater FY2010-FY2025':(98222,'2010','2025'),'Oceaneering 2010-25':(73756,'2010','2025'),'TechnipFMC 2017-25':(1681459,'2017','2025'),'SEACOR Marine 2015-25':(1690334,'2015','2025')}
for name,(cik,a,b) in cos.items():
    g=load(cik)
    rev={}
    for t in REV:
        for k,v in annual(g,[t]).items():
            rev.setdefault(k,v)
    op=annual(g,['OperatingIncomeLoss']); assets=annual(g,['Assets'],True); ocf=annual(g,['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations']); cap=annual(g,['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'])
    ni=annual(g,['NetIncomeLoss'])
    ys=[k for k in op if a<=k[:4]<=b and k[5:7] in ('12','03') and k in rev]
    ys=sorted(set(ys))
    R=sum(rev[y] for y in ys);O=sum(op[y] for y in ys);N=sum(ni.get(y,0) for y in ys)
    A=[assets[y] for y in ys if y in assets]
    print(f"{name:28s} yrs={len(ys)} {ys[0][:7]}..{ys[-1][:7]}  rev={R/1e6:8.0f} opinc={O/1e6:7.0f} margin={O/R*100:5.1f}%  avgassets={sum(A)/len(A)/1e6:6.0f} opinc/assets/yr={O/len(ys)/(sum(A)/len(A))*100:5.1f}%  NI sum={N/1e6:7.0f}  yrs op loss={sum(1 for y in ys if op[y]<0)}")
