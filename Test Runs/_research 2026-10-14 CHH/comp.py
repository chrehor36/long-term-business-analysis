import json
from xb import load, annual
def inst(d,tags):
    for t in tags:
        a=annual(d,t)
        if a: return {k[:4]:v[0]/1e6 for k,v in a.items()}
    return {}
rows={}
for t in ['CHH','WH','HLT','MAR']:
    d=load(t)
    oi=inst(d,['OperatingIncomeLoss'])
    ta=inst(d,['Assets'])
    gw=inst(d,['Goodwill'])
    ia=inst(d,['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'])
    ia2=inst(d,['IndefiniteLivedIntangibleAssetsExcludingGoodwill','IndefiniteLivedTrademarks'])
    ca=inst(d,['CashAndCashEquivalentsAtCarryingValue'])
    rev=inst(d,['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax'])
    print(t)
    for y in [str(x) for x in range(2016,2026)]:
        try:
            intang=ia.get(y,0)
            if t in ('HLT','MAR','WH'): intang=ia.get(y,0)
            base=ta[y]-gw.get(y,0)-intang-ca.get(y,0)
            print(y, 'OI',round(oi.get(y,float('nan'))), 'TA',round(ta[y]),'GW',round(gw.get(y,0)),'IA',round(intang),'IA-indef',round(ia2.get(y,0)),'cash',round(ca.get(y,0)),'tangible-op-assets',round(base),'OI/base %.1f%%'%(100*oi[y]/base) if y in oi else '')
        except KeyError as e: print(y,'missing',e)
