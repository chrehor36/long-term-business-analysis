import sys
sys.path.insert(0, r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-13 IHG')
import edgar
P = {'MAR':1048286,'HLT':1585689,'H':1468174,'WH':1722684,'CHH':1046311}
tags = ['NetCashProvidedByUsedInOperatingActivities','ShareBasedCompensation','OperatingIncomeLoss','PaymentsToAcquirePropertyPlantAndEquipment','StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest']
for t,c in P.items():
    try:
        d = edgar.companyfacts(c)
    except Exception as e:
        print(t,'ERROR',e); continue
    g = d['facts'].get('us-gaap',{})
    for tag in tags:
        if tag not in g: print(t,tag,'absent'); continue
        for unit,vals in g[tag]['units'].items():
            seen={}
            for v in vals:
                if v.get('form')!='10-K': continue
                if v.get('fp')!='FY': continue
                key=(v['end'])
                if 'start' in v and int(v['end'][:4])-int(v['start'][:4])>1: continue
                if v['end'][:4] in ('2019','2020','2021','2022','2023','2024','2025') and v['end'][5:7]=='12':
                    seen.setdefault(key,set()).add((v['val'],v['accn']))
            for k in sorted(seen):
                print(t,tag,k,sorted(seen[k])[:3])
