import json
d=json.load(open('cache/cf_0000041719.json'))
tags=['Assets','Liabilities','StockholdersEquity','CashAndCashEquivalentsAtCarryingValue','AccountsReceivableNetCurrent','InventoryNet','Goodwill','IntangibleAssetsNetExcludingGoodwill','LongTermDebtNoncurrent','LongTermDebtCurrent','RetainedEarningsAccumulatedDeficit','PropertyPlantAndEquipmentNet']
for t in tags:
    vals=d['facts']['us-gaap'].get(t,{}).get('units',{}).get('USD',[])
    rows={}
    for v in vals:
        if v['form']!='10-K' or v['filed']>'2024-06-01': continue
        if v['end'][5:]!='12-31': continue
        if v['end'] not in rows: rows[v['end']]=(v['val']/1e6,v['accn'])
    print(t.ljust(42),' '.join(f"{k[:4]}:{rows[k][0]:.0f}" for k in sorted(rows) if k>='2013'))
