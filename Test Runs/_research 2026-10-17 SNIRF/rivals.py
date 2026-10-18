import json,sys
names={'0000076334':'Parker-Hannifin','0001551182':'Eaton','0000067347':'Modine'}
tags_rev=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet']
tags_op=['OperatingIncomeLoss']
tags_pt=['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments']
tags_eq=['StockholdersEquity']
tags_ta=['Assets']
def annual(facts,tags,instant=False):
    out={}
    for t in tags:
        d=facts.get(t)
        if not d: continue
        for u in d['units'].get('USD',[]):
            if u.get('form') not in ('10-K','10-K/A'): continue
            if not instant:
                if u.get('fp')!='FY' : continue
                s,e=u.get('start'),u['end']
                if not s: continue
                from datetime import date
                ds=date.fromisoformat(s); de=date.fromisoformat(e)
                if (de-ds).days<350: continue
            fy=u['end'][:4]
            out.setdefault(fy,(u['val'],u['accn'],t))
    return out
for c,n in names.items():
    f=json.load(open(f'cf_{c}.json'))['facts']['us-gaap']
    rev=annual(f,tags_rev); op=annual(f,tags_op); pt=annual(f,tags_pt); eq=annual(f,tags_eq,True)
    print('==',n)
    for y in sorted(set(rev)|set(op)):
        if y<'2015': continue
        r=rev.get(y,(None,))[0]; o=op.get(y,(None,))[0]; p=pt.get(y,(None,))[0]
        acc=(op.get(y) or pt.get(y) or rev.get(y))[1]
        m=f"{o/r*100:.1f}%" if r and o else '-'
        mp=f"{p/r*100:.1f}%" if r and p else '-'
        print(y, r and round(r/1e6), o and round(o/1e6), m, 'pretax',mp, acc)
