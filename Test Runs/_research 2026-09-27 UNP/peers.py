import json,os,time
from fetch import get
C={'UNP':100885,'CSX':277948,'NSC':702165,'CP':16875,'CNI':16868,'BNSF':934612}
for t,c in C.items():
    fn=f'peers/{t}_facts.json'
    if os.path.exists(fn): continue
    try:
        b=get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json'); open(fn,'wb').write(b); print(t,len(b))
    except SystemExit as e: print(t,'FAIL',e)
    time.sleep(0.3)
for t in C:
    fn=f'peers/{t}_facts.json'
    if not os.path.exists(fn): continue
    d=json.load(open(fn))
    print(t, d.get('entityName'), list(d['facts'].keys()), len(d['facts'].get('us-gaap',{})), len(d['facts'].get('ifrs-full',{})))
