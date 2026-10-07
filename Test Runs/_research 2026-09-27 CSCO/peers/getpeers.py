import sys, json, time, os
sys.path.insert(0,'..')
from fetch import get
ciks={'CSCO':858877,'ANET':1596532,'JNPR':1043604,'HPE':1645590,'EXTR':1078271,'FFIV':1048695,'FTNT':1262039,'PANW':1327567,'UI':1511737,'CIEN':936395,'ZS':1713683,'CRWD':1535527,'DDOG':1561550,'NTGR':1122904}
for t,c in ciks.items():
    o=f'{t}_facts.json'
    if os.path.exists(o): continue
    try:
        open(o,'wb').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json')); print(t, os.path.getsize(o))
    except SystemExit as e: print('FAIL',t,e)
    time.sleep(0.2)
