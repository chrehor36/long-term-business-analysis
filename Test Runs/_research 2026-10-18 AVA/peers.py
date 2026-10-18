import json
from facts import annual
def sh(f):
    d=json.load(open(f))['facts']['dei'].get('EntityCommonStockSharesOutstanding',{}).get('units',{}).get('shares',[])
    o={}
    for x in d:
        if x.get('form')=='10-K': o[int(x['end'][:4])]=x['val']
    return o
for name,f,nitag in [('AVA','cache/facts_AVA.json','NetIncomeLoss'),('IDA','cache/facts_IDA.json','NetIncomeLossAttributableToParent' ),('POR','cache/facts_POR.json','NetIncomeLoss'),('NWE','cache/facts_NWE.json','NetIncomeLoss'),('NWEG','cache/facts_NWEG.json','NetIncomeLoss')]:
    ni=annual(f,nitag) or annual(f,'NetIncomeLoss')
    eq=annual(f,'StockholdersEquity')
    ocf=annual(f,'NetCashProvidedByUsedInOperatingActivities')
    cx=annual(f,'PaymentsToAcquirePropertyPlantAndEquipment') or annual(f,'PaymentsToAcquireProductiveAssets')
    da=annual(f,'DepreciationDepletionAndAmortization') or annual(f,'DepreciationAndAmortization')
    s=sh(f)
    print('==',name)
    for y in range(2015,2026):
        r = ''
        if y in ni and y in eq and (y-1) in eq:
            r = f"ROE {100*ni[y]/((eq[y]+eq[y-1])/2):.1f}%"
        print(y, f"NI {ni.get(y,0)/1e6:.0f} EQ {eq.get(y,0)/1e6:.0f} {r} OCF {ocf.get(y,0)/1e6:.0f} CAPEX {cx.get(y,0)/1e6:.0f} DA {da.get(y,0)/1e6:.0f} SH {s.get(y,0)/1e6:.1f}")
