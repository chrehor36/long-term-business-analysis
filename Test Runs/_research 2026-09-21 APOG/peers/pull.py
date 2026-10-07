import sys, os, json
sys.path.insert(0,'..')
import fetch
M=json.load(open('ciks.json'))
for t,c in M.items():
    p=f'{t}_companyfacts.json'
    if os.path.exists(p): print('have',t); continue
    try:
        d=fetch.get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json')
        open(p,'wb').write(d); print('wrote',t,len(d))
    except Exception as e: print('FAIL',t,e)
