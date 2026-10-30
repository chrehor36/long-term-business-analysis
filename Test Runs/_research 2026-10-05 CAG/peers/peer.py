import json,sys
from datetime import date
def annual(d,tags):
    out={}
    for tag in tags:
        if tag not in d: continue
        for u,vals in d[tag]['units'].items():
            for v in vals:
                if v.get('form')!='10-K' : continue
                s=v.get('start');e=v['end']
                if s and not (340<(date.fromisoformat(e)-date.fromisoformat(s)).days<380): continue
                if e not in out or v['filed']<out[e][1]:
                    out[e]=(v['val'],v['filed'])
    return {k:v[0] for k,v in out.items()}
T={'rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet'],
 'cogs':['CostOfGoodsAndServicesSold','CostOfRevenue','CostOfGoodsSold','CostOfGoodsAndServiceExcludingDepreciationDepletionAndAmortization'],
 'oi':['OperatingIncomeLoss'],
 'ocf':['NetCashProvidedByUsedInOperatingActivities'],
 'capex':['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'],
 'sbc':['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'],
 'gwimp':['GoodwillImpairmentLoss'],
 'imp':['ImpairmentOfIntangibleAssetsIndefinitelivedExcludingGoodwill','ImpairmentOfIntangibleAssetsExcludingGoodwill']}
for f in sys.argv[1:]:
    d=json.load(open(f))['facts']['us-gaap']
    S={k:annual(d,v) for k,v in T.items()}
    print('=====',f)
    print('FYend      rev    GM%   OI%   (OCF-SBC-capex)%rev  gwimp imp')
    for e in sorted(S['rev']):
        if e<'2015-06': continue
        r=S['rev'][e]
        if r<1e9: continue
        c=S['cogs'].get(e); oi=S['oi'].get(e); ocf=S['ocf'].get(e); cx=S['capex'].get(e); sb=S['sbc'].get(e,0)
        gm=f"{(r-c)/r*100:5.1f}" if c else '  -  '
        om=f"{oi/r*100:5.1f}" if oi is not None else '  -  '
        fc=f"{(ocf-sb-cx)/r*100:5.1f}" if ocf and cx else '  -  '
        print(e, f"{r/1e6:8.0f}", gm, om, fc, f"{S['gwimp'].get(e,0)/1e6:6.0f}", f"{S['imp'].get(e,0)/1e6:6.0f}")
