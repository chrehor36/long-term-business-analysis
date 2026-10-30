import json,sys,urllib.request
from fetch import get
cik=sys.argv[1]; out=sys.argv[2]
d=json.loads(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik.zfill(10)}.json"))
json.dump(d,open(out,'w'))
