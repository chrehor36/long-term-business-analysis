import json,sys
from datetime import date
def series(g,tags):
    out={}
    for t in tags:
        if t not in g: continue
        for u,vals in g[t]['units'].items():
            for v in vals:
                if v.get('form') not in ('10-K','10-K/A') or 'start' not in v: continue
                s=date.fromisoformat(v['start']); e=date.fromisoformat(v['end'])
                if not (350<(e-s).days<380): continue
                k=v['end'][:7]
                if k not in out or v['filed']<out[k][1]: out[k]=(v['val'],v['filed'],v['accn'])
    return out
def inst(g,tags):
    out={}
    for t in tags:
        if t not in g: continue
        for u,vals in g[t]['units'].items():
            for v in vals:
                if v.get('form') not in ('10-K','10-K/A') or 'start' in v: continue
                k=v['end'][:7]
                if k not in out or v['filed']<out[k][1]: out[k]=(v['val'],v['filed'])
    return out
for t in sys.argv[1:]:
    g=json.load(open(f'peers/{t}_facts.json'))['facts']['us-gaap']
    S=series(g,['Revenues','SalesRevenueNet','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueGoodsNet'])
    GP=series(g,['GrossProfit'])
    OI=series(g,['OperatingIncomeLoss'])
    OCF=series(g,['NetCashProvidedByUsedInOperatingActivities'])
    CX=series(g,['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'])
    SBC=series(g,['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'])
    EQ=inst(g,['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'])
    GW=inst(g,['Goodwill'])
    print('==',t,' end  sales  GM%  OM%  OCF-SBC-capex  equity  goodwill  accn')
    for k in sorted(S):
        if k<'2010': continue
        s=S[k][0]/1e6
        gp=GP.get(k,(None,))[0]; oi=OI.get(k,(None,))[0]
        o=OCF.get(k,(None,))[0]; c=CX.get(k,(0,))[0]; sb=SBC.get(k,(0,))[0]
        oc=(o-c-sb)/1e6 if o is not None else float('nan')
        print(f"{t} {k} {s:9.0f} {100*gp/1e6/s if gp else float('nan'):5.1f} {100*oi/1e6/s if oi else float('nan'):5.2f} {oc:8.0f} {EQ.get(k,(0,))[0]/1e6:7.0f} {GW.get(k,(0,))[0]/1e6:7.0f} {S[k][2]}")
