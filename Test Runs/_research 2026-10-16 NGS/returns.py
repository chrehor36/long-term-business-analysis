import json
from facts import annual
def g(d,t): return {k:v[0]/1e6 for k,v in annual(d,t).items()}
def merge(*ds):
    o={}
    for x in ds:
        for k,v in x.items(): o.setdefault(k,v)
    return o
rows={}
for n in ['NGS','AROC','USAC','KGS']:
    d=json.load(open(f'cache/peers/{n}.json'))
    A=g(d,'Assets'); GW=g(d,'Goodwill'); IA=g(d,'IntangibleAssetsNetExcludingGoodwill')
    if n=='AROC':
        pt=g(d,'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest')
        ie=merge(g(d,'InterestExpense'),g(d,'InterestExpenseNonoperating'))
        oi={y:pt[y]+ie.get(y,0) for y in pt}
        rev=g(d,'RevenueFromContractWithCustomerExcludingAssessedTax')
    else:
        oi=g(d,'OperatingIncomeLoss')
        rev=merge(g(d,'Revenues'),g(d,'RevenueFromContractWithCustomerExcludingAssessedTax'),g(d,'SalesRevenueNet'))
    if n=='USAC':
        # USAC intangibles tag
        IA=merge(IA,g(d,'FiniteLivedIntangibleAssetsNet'))
    if n=='KGS':
        IA=merge(IA,g(d,'FiniteLivedIntangibleAssetsNet'))
    print('==',n,'  year: EBIT  tangible-assets(avg of yr-end)  EBIT/TA  EBIT/rev')
    tot_e=0;tot_c=0
    for y in sorted(oi):
        if y<'2009' : continue
        if n=='AROC' and y<'2016': continue
        if y not in A: continue
        ta=A[y]-GW.get(y,0)-IA.get(y,0)
        py=str(int(y)-1)
        tap=(A[py]-GW.get(py,0)-IA.get(py,0)) if py in A and not (n=='AROC' and py<'2016') else ta
        avg=(ta+tap)/2
        r=rev.get(y)
        print(f'  {y}: {oi[y]:8.1f} {avg:9.1f}  {100*oi[y]/avg:6.1f}%  ' + (f'{100*oi[y]/r:6.1f}%' if r else ''))
        if y>='2014': tot_e+=oi[y]; tot_c+=avg
    print(f'  2014(or first)-2025 sum EBIT / sum avg tangible assets: {100*tot_e/tot_c:.1f}%')
