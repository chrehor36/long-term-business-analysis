from comp import *
from datetime import date
def inst(f,tags):
    out={}
    for tag in tags:
        d=f['facts']['us-gaap'].get(tag)
        if not d: continue
        for u in d['units'].values():
            for x in u:
                if x.get('form') in ('10-K',) and 'start' not in x:
                    out.setdefault(x['end'][:7],x['val'])
    return out
for t in C:
    f=facts(t)
    oi=annual(f,['OperatingIncomeLoss'])
    if t=='CLX':
        pt=annual(f,['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'])
        ie=annual(f,['InterestExpense','InterestExpenseNonoperating'])
        oi={k:(pt[k][0]+ie.get(k,(0,))[0],) for k in pt}
    rev=annual(f,['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet'])
    A=inst(f,['Assets']); G=inst(f,['Goodwill']); I=inst(f,['IntangibleAssetsNetExcludingGoodwill'])
    if not I:
        a=inst(f,['IndefiniteLivedIntangibleAssetsExcludingGoodwill','IndefiniteLivedTrademarks']); b=inst(f,['FiniteLivedIntangibleAssetsNet'])
        I={k:a.get(k,0)+b.get(k,0) for k in set(a)|set(b)}
    print('=====',t)
    for k in sorted(oi):
        if k<'2015-06': continue
        if k in A and k in G and k in rev:
            ta=A[k]-G[k]-I.get(k,0)
            o=oi[k][0]
            print(k,f"EBIT {o/1e6:8.0f}  om {o/rev[k][0]*100:5.1f}%  tangible assets {ta/1e6:8.0f}  EBIT/TA {o/ta*100:5.1f}%  GW+Int/Assets {(G[k]+I.get(k,0))/A[k]*100:4.0f}%")
