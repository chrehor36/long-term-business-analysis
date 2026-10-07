import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fetch_core import get, strip
HERE = os.path.dirname(os.path.abspath(__file__))
for tk, cik in [("UBER",1543151),("CART",1579091),("LYFT",1759509)]:
    s = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    r = s["filings"]["recent"]
    got = {"10-K":0, "10-Q":0}
    for i,f in enumerate(r["form"]):
        if f in got and got[f] < (2 if f=="10-K" else 1) and tk!="LYFT":
            acc=r["accessionNumber"][i]; doc=r["primaryDocument"][i]; rd=r["reportDate"][i]
            name=f"{tk}_{f.replace('-','')}_{rd}"
            p=os.path.join(HERE,name+".txt")
            if not os.path.exists(p):
                raw=get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}")
                open(p,"w",encoding="utf-8").write(strip(raw))
            print(tk, f, rd, acc, r["filingDate"][i]); got[f]+=1; time.sleep(0.4)
