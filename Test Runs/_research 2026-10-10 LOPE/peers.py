import json,sys
from datetime import date
def series(d,tags,flow=True):
    out={}
    for t in tags:
        if t not in d: continue
        u=d[t]['units']; k='USD' if 'USD' in u else list(u)[0]
        for x in u[k]:
            if x['form'] not in('10-K','10-K/A','10-KT'): continue
            if flow:
                if 'start' not in x: continue
                if (date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<350: continue
            y=x['end'][:7]
            out.setdefault(y,x['val'])
    return out
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueServicesNet']
OPI=['OperatingIncomeLoss']
OCF=['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations']
CAPEX=['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets']
SBC=['ShareBasedCompensation','AllocatedShareBasedCompensationExpense']
EQ=['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest']
GW=['Goodwill']; INT=['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet','IndefiniteLivedIntangibleAssetsExcludingGoodwill']
TA=['Assets']
for t in sys.argv[1:]:
    d=json.load(open(f'cache/peers/{t}_facts.json' if t!='LOPE' else 'cache/facts.json'))['facts']['us-gaap']
    r=series(d,REV);o=series(d,OPI);c=series(d,OCF);k=series(d,CAPEX);s=series(d,SBC)
    e=series(d,EQ,False);g=series(d,GW,False);ta=series(d,TA,False)
    print('==',t)
    for y in sorted(set(r)|set(o)):
        if y<'2015': continue
        R=r.get(y);O=o.get(y)
        m= f"{O/R*100:5.1f}%" if R and O is not None else '  -  '
        f=lambda v: f"{v/1e6:8.1f}" if v is not None else '     -  '
        print(y,'rev',f(R),'opinc',f(O),'margin',m,'ocf',f(c.get(y)),'capex',f(k.get(y)),'sbc',f(s.get(y)),'eq',f(e.get(y)),'gw',f(g.get(y)),'assets',f(ta.get(y)))
