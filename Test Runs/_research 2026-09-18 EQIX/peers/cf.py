import json,os,time
from fetch_core import get,HERE
C = {"DLR":1297996,"AMT":1053507,"IRM":1020569,"CYXT":1794905,"CONE":1553023,"QTS":1577368,"SWCH":1710583,"COR":1490892}
for t,c in C.items():
    p=os.path.join(HERE,f"{t}_companyfacts.json")
    if not os.path.exists(p):
        open(p,"w").write(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json")); time.sleep(0.3)
    d=json.load(open(p))
    print(t, len(d["facts"].get("us-gaap",{})))
