import json,sys
def annual(f,tags,unit='USD',inst=False):
    g=f['facts'].get('us-gaap',{})
    out={}
    for t in tags:
        if t not in g: continue
        for u,arr in g[t]['units'].items():
            if u!=unit: continue
            for x in arr:
                if x.get('form') not in ('10-K','10-K/A'): continue
                if inst:
                    if not x['end'].endswith('12-31'): continue
                    y=int(x['end'][:4])
                else:
                    if x.get('fp')!='FY' and 'start' not in x: continue
                    s,e=x.get('start'),x['end']
                    if not s: continue
                    d=(int(e[:4])-int(s[:4]))*12+int(e[5:7])-int(s[5:7])
                    if d<11 or d>12: continue
                    y=int(e[:4])
                # prefer latest filed
                if y not in out or x['filed']>out[y][1]: out[y]=(x['val'],x['filed'],t)
    return {y:v[0] for y,v in out.items()}
T={'rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet'],
   'gp':['GrossProfit'],
   'oi':['OperatingIncomeLoss'],
   'pti':['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],
   'ni':['NetIncomeLoss','ProfitLoss'],
   'eq':['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'],
   'gw':['Goodwill'],
   'fr':['IndefiniteLivedFranchiseRights','IndefiniteLivedIntangibleAssetsExcludingGoodwill','IntangibleAssetsNetExcludingGoodwill'],
}
res={}
for tk in ['ABG','AN','LAD','GPI','PAG','SAH']:
    f=json.load(open(tk+'_facts.json'))
    d={}
    for k,tags in T.items():
        d[k]=annual(f,tags,inst=k in('eq','gw','fr'))
    res[tk]=d
json.dump({tk:{k:{str(y):v for y,v in dd.items()} for k,dd in d.items()} for tk,d in res.items()},open('peers_extract.json','w'))
yrs=range(2009,2026)
for tk,d in res.items():
    print('==',tk)
    print('year   rev($B)  GM%   OM%   PTM%   ROE%  tangEq($M)')
    for y in yrs:
        r=d['rev'].get(y); gp=d['gp'].get(y); oi=d['oi'].get(y); pt=d['pti'].get(y); ni=d['ni'].get(y)
        e=d['eq'].get(y); e0=d['eq'].get(y-1); gw=d['gw'].get(y,0) or 0; fr=d['fr'].get(y,0) or 0
        f=lambda a,b: f"{a/b*100:5.1f}" if a is not None and b else "   - "
        roe=f"{ni/((e+e0)/2)*100:5.1f}" if ni is not None and e and e0 else "   - "
        te=f"{(e-gw-fr)/1e6:8.0f}" if e else "     -"
        print(y, f"{r/1e9:6.2f}" if r else "   -  ", f(gp,r), f(oi,r), f(pt,r), roe, te)
