import json,sys
sys.path.insert(0,'scripts')
from fetch import get
peers={'AIR':'0000001750','HEI':'0000046619','ASLE':'0001754170','VSEC':'0000102752'}
tags=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','OperatingIncomeLoss','Assets','Goodwill','IntangibleAssetsNetExcludingGoodwill','StockholdersEquity','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','LongTermDebtNoncurrent','InventoryNet','PaymentsToAcquireBusinessesNetOfCashAcquired']
for t,c in peers.items():
    d=json.loads(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json'))
    open(f'cache/facts_{t}.json','w').write(json.dumps(d))
    g=d['facts'].get('us-gaap',{})
    print('=====',t,d['entityName'])
    for tag in tags:
        if tag not in g: continue
        u=g[tag]['units'].get('USD',[])
        rows={}
        for x in u:
            if x.get('form')!='10-K': continue
            if 'start' in x:
                # annual durations only
                from datetime import date
                s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
                if not (330<(e-s).days<400): continue
            rows.setdefault(x['end'],(x['val'],x['accn']))  # first filed
        ks=sorted(rows)[-11:]
        print(f"{tag[:40]:40s}", ' '.join(f"{k[:7]}:{rows[k][0]/1e6:.0f}" for k in ks))
