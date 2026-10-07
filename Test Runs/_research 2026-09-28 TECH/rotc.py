# return on unleveraged net tangible operating capital [E2-43], from companyfacts (newest-vintage FY values), $M
import json
from datetime import date
f=json.load(open('cache/facts_tech.json'))['facts']['us-gaap']
def ser(t, dur=True):
    out={}
    if t not in f: return out
    for u in f[t]['units'].values():
        for x in u:
            if x.get('form') not in ('10-K','10-K/A') or x.get('fp')!='FY': continue
            if dur:
                if 'start' not in x: continue
                d=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days
                if not 350<=d<=380: continue
            elif 'start' in x: continue
            y=int(x['end'][:4])
            if y not in out or x['filed']>out[y][1]: out[y]=(x['val']/1e6,x['filed'])
    return {k:v[0] for k,v in out.items()}
rev={**ser('SalesRevenueNet'),**ser('RevenueFromContractWithCustomerExcludingAssessedTax')}
oi=ser('OperatingIncomeLoss'); am=ser('AmortizationOfIntangibleAssets')
ca=ser('AssetsCurrent',False); cash=ser('CashAndCashEquivalentsAtCarryingValue',False)
afs=ser('AvailableForSaleSecuritiesCurrent',False); afs2=ser('AvailableForSaleSecuritiesDebtSecuritiesCurrent',False); sti=ser('ShortTermInvestments',False)
cl=ser('LiabilitiesCurrent',False); ltdc=ser('LongTermDebtCurrent',False); ppe=ser('PropertyPlantAndEquipmentNet',False)
gw=ser('Goodwill',False); ia=ser('IntangibleAssetsNetExcludingGoodwill',False); eq=ser('StockholdersEquity',False)
print('FY  rev   OI  OI%  amort  OIpre  opcap  OIpre/opcap  goodwill+intang  equity')
for y in range(2010,2027):
    if y not in ca: continue
    fin=cash.get(y,0)+max(afs.get(y,0),afs2.get(y,0),sti.get(y,0))
    opcap=ca[y]-fin-(cl[y]-ltdc.get(y,0))+ppe[y]
    o=oi.get(y); 
    if y==2013: o=None
    a=am.get(y,0); pre=(o+a) if o is not None else None
    print(y, f"{rev.get(y,0):7.1f}", f"{o if o is not None else float('nan'):6.1f}", f"{(o/rev[y]*100) if o else float('nan'):5.1f}", f"{a:5.1f}", f"{pre if pre else float('nan'):6.1f}", f"{opcap:6.1f}", f"{(pre/opcap*100) if pre else float('nan'):6.1f}%", f"{gw.get(y,0)+ia.get(y,0):7.1f}", f"{eq.get(y,0):7.1f}")
# owners' pre-tax return on all capital: operating income before acquired amortization over (tangible operating capital + goodwill + intangibles + equity-method investment)
emi={2022:25.0,2023:255.857,2024:242.337,2025:235.983,2026:230.827}
print('\nFY  OIpre / all operating capital incl. goodwill, intangibles, Wilson Wolf stake')
for y in range(2010,2027):
    if y not in ca or y==2013: continue
    fin=cash.get(y,0)+max(afs.get(y,0),afs2.get(y,0),sti.get(y,0))
    opcap=ca[y]-fin-(cl[y]-ltdc.get(y,0))+ppe[y]
    allc=opcap+gw.get(y,0)+ia.get(y,0)+emi.get(y,0)
    pre=oi[y]+am.get(y,0)
    print(y, f'{pre:6.1f} / {allc:7.1f} = {100*pre/allc:5.1f}%')
