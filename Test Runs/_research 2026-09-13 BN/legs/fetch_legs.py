import urllib.request, json, gzip, os, sys, re, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from f2 import totext
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"gzip"}
D=os.path.dirname(os.path.abspath(__file__))
def get(u):
    r=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=240); b=r.read()
    if r.headers.get("Content-Encoding")=="gzip": b=gzip.decompress(b)
    return b
tick=json.loads(get("https://www.sec.gov/files/company_tickers.json"))
want={"BIP","BEP","BBU","BBUC","BEPC","BIPC"}
ciks={}
for v in tick.values():
    if v["ticker"] in want: ciks[v["ticker"]]=v["cik_str"]; print(v["ticker"],v["cik_str"],v["title"])
for t in ["BIP","BEP","BBUC","BBU"]:
    if t not in ciks: continue
    c=str(ciks[t]).zfill(10)
    s=json.loads(get(f"https://data.sec.gov/submissions/CIK{c}.json"))
    r=s["filings"]["recent"]
    for i in range(len(r["form"])):
        if r["form"][i] in ("20-F","40-F","10-K") and r["filingDate"][i]>="2024-01-01":
            print(" ",t,r["form"][i],r["filingDate"][i],r["accessionNumber"][i],r["primaryDocument"][i],r["reportDate"][i])
    time.sleep(0.3)

jobs=[("1406234","0001406234-26-000002","bip-20251231.htm","BIP_20F_FY2025.txt"),
      ("1533232","0001533232-26-000011","bep-20251231.htm","BEP_20F_FY2025.txt"),
      ("1654795","0001628280-26-022148","bbu-20251231.htm","BBUC_20F_FY2025.txt")]
for cik,acc,fn,out in jobs:
    p=os.path.join(D,out)
    if os.path.exists(p): print("have",out); continue
    b=get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{fn}")
    open(p,"w",encoding="utf-8").write(totext(b)); print(out,len(b)); time.sleep(0.5)
