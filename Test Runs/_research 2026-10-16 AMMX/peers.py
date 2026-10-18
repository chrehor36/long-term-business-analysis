import json,sys
def annual(f,tags):
    for t in tags:
        u=f['facts'].get('us-gaap',{}).get(t)
        if not u: continue
        out={}
        for x in u['units'].get('USD',[]):
            if x.get('form') in ('10-K','10-K/A') and x.get('fp')=='FY' and 'start' in x:
                from datetime import date
                s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
                if 350<(e-s).days<380: out[e.year if e.month>6 else e.year-1]=(x['val'],x['accn'])
        if out: return t,out
    return None,{}
def inst(f,tags):
    for t in tags:
        u=f['facts'].get('us-gaap',{}).get(t)
        if not u: continue
        out={}
        for x in u['units'].get('USD',[]):
            if x.get('form') in ('10-K','10-K/A') and 'start' not in x:
                from datetime import date
                e=date.fromisoformat(x['end']); out[e.year if e.month>6 else e.year-1]=(x['val'],x['accn'])
        if out: return t,out
    return None,{}
for tk in sys.argv[1:]:
    f=json.load(open(tk+'.json'))
    rt,rev=annual(f,['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet'])
    ot,op=annual(f,['OperatingIncomeLoss'])
    pt,pti=annual(f,['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'])
    nt,ni=annual(f,['NetIncomeLoss'])
    et,eq=inst(f,['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'])
    print(tk,rt,ot,pt,nt,et)
    for y in range(2015,2026):
        r=rev.get(y,(None,''))[0]; o=op.get(y,(None,''))[0]; p=pti.get(y,(None,''))[0]; n=ni.get(y,(None,''))[0]; e=eq.get(y,(None,''))[0]
        fm=lambda v: f'{v/1e6:,.1f}' if v is not None else '-'
        om=f'{o/r*100:.1f}%' if r and o is not None else '-'
        pm=f'{p/r*100:.1f}%' if r and p is not None else '-'
        roe=f'{n/e*100:.1f}%' if e and n is not None else '-'
        print(y,fm(r),fm(o),om,fm(p),pm,fm(n),fm(e),roe, rev.get(y,(0,''))[1])
