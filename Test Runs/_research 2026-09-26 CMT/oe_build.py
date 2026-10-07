import json,re
from cfparse import parse
keys={'ni':r'net (income|loss|earnings)','da':r'depreciation','sbc':r'share-based|stock-based|stock based','ocf':r'^net cash.*operating','capex':r'purchase of property','ar':r'accounts receivable','inv':r'^inventor|: inventor| inventories$|^inventories','pre':r'prepaid','ap':r'accounts payable','acc':r'accrued','acq':r'^(cash flows from investing activities: )?(acquisition|purchase of assets|purchase of horizon|payment for acquisition)|^acquisition'}
data={}
for fy in range(2006,2026):
    try: rows=parse(f'tenk_FY{fy}.txt')
    except Exception as e: print('fail',fy,e); continue
    rec={}
    for l,v in rows:
        L=l.lower()
        for k,p in keys.items():
            if k in rec: continue
            if k=='ni' and not L.startswith('cash flows from operating') and not L.startswith('net income'): continue
            if k=='inv' and 'inventor' not in L: continue
            if k=='ar' and 'receivable' not in L: continue
            if k!='inv' and k!='ar' and not re.search(p,L): continue
            if k=='acq' and not v: continue
            rec[k]=v
    data[fy]=rec
    print(fy,{k:v for k,v in rec.items()})
json.dump(data,open('cf_parsed.json','w'),indent=0)
