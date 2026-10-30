import json,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
def annual(f,tags,unit='USD',inst=False):
    out={}
    for t in tags:
        for ns in ('us-gaap','ifrs-full'):
            d=f['facts'].get(ns,{}).get(t)
            if not d: continue
            for u,vals in d['units'].items():
                if u!=unit: continue
                for v in vals:
                    if v.get('form') not in ('10-K','40-F','10-K/A','20-F'): continue
                    if inst:
                        key=v['end']
                    else:
                        if 'start' not in v: continue
                        from datetime import date
                        s=date.fromisoformat(v['start']);e=date.fromisoformat(v['end'])
                        if not (350<(e-s).days<380): continue
                        key=v['end']
                    out.setdefault(key,v['val'])
        if out: return out,t
    return out,None
names={'AHCO':'peers/facts_AHCO.json','VMD':'peers/facts_0001729149.json','QIPT':'peers/facts_0001540013.json','APR':'peers/facts_0001735803.json'}
for n,p in names.items():
    f=json.load(open(p))
    rev,rt=annual(f,['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','HealthCareOrganizationRevenue','Revenue'])
    oi,ot=annual(f,['OperatingIncomeLoss','ProfitLossFromOperatingActivities'])
    gw,_=annual(f,['GoodwillImpairmentLoss'])
    assets,_=annual(f,['Assets'],inst=True)
    good,_=annual(f,['Goodwill'],inst=True)
    intang,_=annual(f,['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet','IntangibleAssetsOtherThanGoodwill'],inst=True)
    cash,_=annual(f,['CashAndCashEquivalentsAtCarryingValue','Cash','CashAndCashEquivalents'],inst=True)
    print('==',n,rt,ot)
    for y in sorted(rev):
        if y<'2015': continue
        r=rev[y]; o=oi.get(y); g=gw.get(y,0) or 0
        a=assets.get(y); gd=good.get(y,0) or 0; it=intang.get(y,0) or 0; c=cash.get(y,0) or 0
        tang=(a-gd-it-c) if a else None
        oadj=(o+g) if o is not None else None
        print(y, f"rev {r/1e6:8.1f}", f"OI {o/1e6 if o is not None else float('nan'):8.1f}", f"impair {g/1e6:6.1f}", f"OI ex-impair margin {100*oadj/r if oadj is not None else float('nan'):5.1f}%", f"tangible assets ex cash {tang/1e6 if tang else float('nan'):8.1f}", f"pre-tax ROTA {100*oadj/tang if (tang and oadj is not None) else float('nan'):5.1f}%")
