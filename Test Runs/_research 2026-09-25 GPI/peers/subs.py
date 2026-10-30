import json,sys,subprocess
from fetch import get
peers={'AN':350698,'PAG':1019849,'LAD':1023128,'ABG':1144980,'SAH':1043509}
for t,c in peers.items():
    j=json.loads(get('https://data.sec.gov/submissions/CIK%010d.json'%c))
    open(f'{t}_subs.json','w').write(json.dumps(j))
    r=j['filings']['recent']
    print(t,c,j['name'])
    for i,f in enumerate(r['form']):
        if f in('10-K','10-K/A') and r['reportDate'][i][:4] in('2023','2024','2025'):
            print('  ',f,r['reportDate'][i],r['filingDate'][i],r['accessionNumber'][i],r['primaryDocument'][i])
