import json
names={'0001031296':'FirstEnergy','0000004904':'AEP','0000072741':'Eversource','0000922224':'PPL'}
tags={'NI':['NetIncomeLossAvailableToCommonStockholdersBasic','NetIncomeLoss'],
 'EQ':['StockholdersEquity'],
 'OCF':['NetCashProvidedByUsedInOperatingActivities'],
 'CAPEX':['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'],
 'DEP':['DepreciationDepletionAndAmortization','Depreciation','DepreciationAndAmortization'],
 'REV':['Revenues','RevenueFromContractWithCustomerIncludingAssessedTax']}
for c,n in names.items():
    d=json.load(open(f'cache/facts_{c}.json'))['facts']['us-gaap']
    row={}
    for k,tl in tags.items():
        for t in tl:
            if t not in d: continue
            got={}
            for u,vals in d[t]['units'].items():
                for v in vals:
                    if v.get('form')!='10-K' or 'frame' not in v: continue
                    f=v['frame']
                    if k=='EQ' and f.endswith('Q4I'): got[f[2:6]]=(v['val'],v['accn'])
                    elif k!='EQ' and len(f)==6: got[f[2:]]=(v['val'],v['accn'])
            if all(y in got for y in ['2021','2022','2023','2024','2025']) or (k=='EQ' and all(y in got for y in ['2020','2021','2022','2023','2024','2025'])):
                row[k]=(t,got); break
    print('==',n)
    for k,(t,got) in row.items():
        print(k,t,[ (y,round(got[y][0]/1e6)) for y in sorted(got) if y>='2020'], got.get('2025',(0,''))[1])
