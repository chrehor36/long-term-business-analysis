import json, time
from fetch import get
for t,c in {'WMS':'0001604028','FRTA':'0001678463','SMID':'0000924719','NWPX':'0001001385','OTTR':'0001466593'}.items():
    d=json.loads(get(f'https://data.sec.gov/submissions/CIK{c}.json'))
    print(t, c, d['name'], '|', d.get('sicDescription'), '|', d.get('fiscalYearEnd'), '|', d.get('stateOfIncorporation'))
    time.sleep(0.5)
