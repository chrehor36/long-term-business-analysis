# Arithmetic only: field returns from XBRL company facts (10-K values; latest-filed value per fiscal year end).
import json, datetime as dt
def series(d, tags, flow):
    out={}
    for tag in tags:
        for ns in ('us-gaap','abg'):
            v=d['facts'].get(ns,{}).get(tag)
            if not v: continue
            for u in v['units'].get('USD',[]):
                if u.get('form') not in ('10-K','10-K/A'): continue
                e=dt.date.fromisoformat(u['end'])
                if flow:
                    if 'start' not in u: continue
                    s=dt.date.fromisoformat(u['start'])
                    if not (350<= (e-s).days <=380): continue
                if e.month!=12: continue
                y=e.year
                key=(y)
                if key not in out or u['filed']>out[key][1]:
                    if key in out and out[key][2]!=tag: continue  # first tag wins
                    out[key]=(u['val']/1e6,u['filed'],tag)
    return {k:v[0] for k,v in out.items()}
T={
 'ABG':dict(intx=['InterestExpenseOther']),
 'AN':dict(intx=['InterestExpenseDebt']),
 'GPI':dict(intx=['InterestExpenseOther']),
 'LAD':dict(intx=['InterestExpenseDebt']),
}
rows={}
for t in T:
    d=json.load(open(f'cache/facts_{t}.json'))
    pt=series(d,['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],True)
    ix=series(d,T[t]['intx'],True)
    rev=series(d,['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax'],True)
    eq=series(d,['StockholdersEquity'],False)
    gw=series(d,['Goodwill'],False)
    fr=series(d,['IndefiniteLivedFranchiseRights'],False)
    ltd=series(d,['LongTermDebtAndCapitalLeaseObligations'],False)
    ltc=series(d,['LongTermDebtAndCapitalLeaseObligationsCurrent'],False)
    ca=series(d,['CashAndCashEquivalentsAtCarryingValue','CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents'],False)
    print(f"\n{t}: year  revenue  pretax  nonfloorint  EBIT  equity  goodwill  franchise  debt  cash  tangcap  EBIT/tangcap  EBIT/totalcap  EBITmargin")
    for y in range(2011,2026):
        try:
            ebit=pt[y]+ix.get(y,0)
            debt=ltd.get(y,0)+ltc.get(y,0)
            tot=eq[y]+debt-ca.get(y,0)
            tang=tot-gw.get(y,0)-fr.get(y,0)
            print(f"{y} {rev.get(y,0):9.0f} {pt[y]:7.0f} {ix.get(y,0):6.0f} {ebit:7.0f} {eq[y]:7.0f} {gw.get(y,0):7.0f} {fr.get(y,0):7.0f} {debt:7.0f} {ca.get(y,0):6.0f} {tang:7.0f} {ebit/tang*100 if tang>0 else float('nan'):6.1f}% {ebit/tot*100:6.1f}% {ebit/rev.get(y,1)*100:5.2f}%")
            rows.setdefault(t,{})[y]=(ebit,tang,tot,rev.get(y,0))
        except KeyError as k:
            print(y,'missing',k)
json.dump(rows,open('field_returns.json','w'))
