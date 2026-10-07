import json,sys
from datetime import date
def ann(f,tag):
    g=f['facts']['us-gaap']
    if tag not in g: return {}
    out={}
    for u,arr in g[tag]['units'].items():
        if u!='USD': continue
        for x in arr:
            if x.get('form') not in ('10-K','10-K/A') or x.get('fp')!='FY': continue
            if 'start' in x:
                s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
                if not (350<(e-s).days<380): continue
            yr=x['end'][:7]
            if yr not in out or x['filed']<out[yr][1]: out[yr]=(x['val'],x['filed'],x['accn'])
    return out
for tk in sys.argv[1:]:
    f=json.load(open(f'peers/{tk}_facts.json'))
    rev={}
    for t in ('Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet','SalesRevenueServicesNet'):
        for k,v in ann(f,t).items():
            rev.setdefault(k,v)
    oi=ann(f,'OperatingIncomeLoss'); ocf=ann(f,'NetCashProvidedByUsedInOperatingActivities')
    cap=ann(f,'PaymentsToAcquirePropertyPlantAndEquipment') or ann(f,'PaymentsToAcquireProductiveAssets')
    print('==',tk)
    for k in sorted(rev):
        if k<'2010': continue
        r=rev[k][0]; o=oi.get(k,(None,))[0]
        print(k, 'rev %.0f'%(r/1e6), 'opinc %s'%('%.0f'%(o/1e6) if o else '-'), 'margin %s'%('%.1f%%'%(100*o/r) if o else '-'),
              'ocf %s'%('%.0f'%(ocf[k][0]/1e6) if k in ocf else '-'), 'capex %s'%('%.0f'%(cap[k][0]/1e6) if k in cap else '-'), rev[k][2])
