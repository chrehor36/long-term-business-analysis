import json
from datetime import date
def load(f):
    return json.load(open(f))['facts']['us-gaap']
def series(d, tag, inst=False):
    if tag not in d: return {}
    out={}
    for u,arr in d[tag]['units'].items():
        for x in arr:
            if x.get('form') not in ('10-K','20-F','10-K/A','20-F/A'): continue
            if inst:
                if 'start' in x or x['end'][5:]!='12-31': continue
            else:
                if 'start' not in x: continue
                if (date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<350: continue
            y=int(x['end'][:4])
            if y not in out or x['filed']<out[y][1]: out[y]=(x['val']/1e6,x['filed'])
    return {k:v[0] for k,v in out.items()}
def merge(*ss):
    o={}
    for s in ss:
        for k,v in s.items(): o.setdefault(k,v)
    return o
cfg={
 'WLFC':('cache/peers/WLFC_companyfacts.json',['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest'],['InterestExpense'],['StockholdersEquity'],['LongTermDebt']),
 'AER':('cache/peers/AER_companyfacts.json',['IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],['InterestExpense','InterestExpenseOperating'],['StockholdersEquity'],['LongTermDebt']),
 'FTAI':('cache/peers/FTAI_companyfacts.json',['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest'],['InterestExpense','InterestExpenseNonoperating'],['StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'],['LongTermDebt']),
}
for name,(f,pt,ie,eq,dt) in cfg.items():
    d=load(f)
    P=merge(*[series(d,t) for t in pt]); I=merge(*[series(d,t) for t in ie])
    E=merge(*[series(d,t,True) for t in eq]); A=series(d,'Assets',True); D=merge(*[series(d,t,True) for t in dt])
    print(f"== {name}  year: pretax/avgEq  (pretax+int)/avgAssets  int/avgDebt  debt/equity")
    rows=[]
    for y in range(2016,2026):
        try:
            ae=(E[y]+E[y-1])/2; aa=(A[y]+A[y-1])/2; ad=(D[y]+D[y-1])/2
            r=(P[y]/ae, (P[y]+I[y])/aa, I[y]/ad, D[y]/E[y])
            rows.append(r)
            print(y, ' '.join(f"{v*100:7.1f}%" if i<3 else f"{v:6.2f}x" for i,v in enumerate(r)), f"  pretax {P[y]:.0f} int {I[y]:.0f}")
        except KeyError as e: print(y,'missing',e)
    n=len(rows)
    if n: print('mean', ' '.join(f"{sum(r[i] for r in rows)/n*100:7.1f}%" if i<3 else f"{sum(r[i] for r in rows)/n:6.2f}x" for i in range(4)), f"  n={n}")
print("\n== overhead: G&A (WLFC) / SG&A (AER) over average assets")
for name,f,tag in [('WLFC','cache/peers/WLFC_companyfacts.json','GeneralAndAdministrativeExpense'),('AER','cache/peers/AER_companyfacts.json','SellingGeneralAndAdministrativeExpense')]:
    d=load(f); G=series(d,tag); A=series(d,'Assets',True)
    vals=[]
    for y in range(2016,2026):
        if y in G and y in A and y-1 in A:
            v=G[y]/((A[y]+A[y-1])/2); vals.append(v); print(name,y,f"{v*100:.2f}%")
    print(name,'mean',f"{sum(vals)/len(vals)*100:.2f}%")
