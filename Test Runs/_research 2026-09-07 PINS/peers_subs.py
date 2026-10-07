import json, os, re, sys, time, urllib.request
sys.stdout.reconfigure(encoding="utf-8")
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
OUT=os.path.dirname(os.path.abspath(__file__))
def get(url,tries=5):
    last=None
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=180).read()
        except Exception as e:
            last=e; time.sleep(2.0*(i+1))
    raise last
PEERS={"META":1326801,"GOOGL":1652044,"SNAP":1564408,"RDDT":1713445,"PINS":1506293,"TTD":1671933}
for tk,cik in PEERS.items():
    p=os.path.join(OUT,f"subs_{tk}.json")
    if not os.path.exists(p):
        open(p,"wb").write(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json")); time.sleep(0.35)
    d=json.load(open(p))
    r=d["filings"]["recent"]
    print(f"=== {tk} CIK {cik} :: {d.get('name')} ===")
    n=0
    for i,f in enumerate(r["form"]):
        if f=="10-K":
            print(f"  10-K acc={r['accessionNumber'][i]} filed={r['filingDate'][i]} period={r['reportDate'][i]} doc={r['primaryDocument'][i]}")
            n+=1
            if n>=7: break
    # older files
    for ff in d["filings"].get("files",[]):
        print("   older-index:",ff["name"],ff["filingFrom"],ff["filingTo"])
