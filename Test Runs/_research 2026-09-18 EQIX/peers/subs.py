import json, time, os
from fetch_core import get, HERE
import sources
C = {"DLR":1297996,"AMT":1053507,"IRM":1020569,"CYXT":1794905,"CONE":1553023,"QTS":1561164,"SWCH":1710583,"COR":1490892}
for t,c in C.items():
    try:
        d = json.loads(get(f"https://data.sec.gov/submissions/CIK{c:010d}.json"))
    except Exception as e:
        print(t, "ERR", e); continue
    json.dump(d, open(os.path.join(HERE, f"{t}_submissions.json"),"w"))
    r = d["filings"]["recent"]
    print("==", t, c, d["name"])
    for i,f in enumerate(r["form"]):
        if f in ("10-K","10-Q") or (t=="CYXT" and f=="8-K"):
            print(" ", f, r["filingDate"][i], r["reportDate"][i], r["accessionNumber"][i], r["primaryDocument"][i])
    time.sleep(0.3)
