import json, urllib.request, urllib.parse, time, collections, sys
sys.path.insert(0,"C:/Users/chreh/OneDrive/Documents/BRK/tools")
UA={"User-Agent":"BRK framework run chrehor36@gmail.com","Accept-Encoding":"identity"}
def get(u):
    for i in range(4):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=120).read()
        except Exception as e: print("retry",i,e); time.sleep(3)
peers={"OPLN":"0001395942","CPRT":"0000900075","RBA":"0001046102","CVNA":"0001690820","KMX":"0001170010","CRMT":"0000799850"}
for t,c in peers.items():
    open(f"{t}_companyfacts.json","wb").write(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json")); time.sleep(0.3)
    sub=json.loads(get(f"https://data.sec.gov/submissions/CIK{c}.json")); time.sleep(0.3)
    r=sub["filings"]["recent"]
    ks=[x for x in zip(r["form"],r["filingDate"],r["reportDate"],r["accessionNumber"],r["primaryDocument"]) if x[0] in ("10-K",)][:2]
    print(t, ks)
    json.dump(ks, open(f"{t}_10k_list.json","w"))
from sources import fts_count
UA2={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept":"application/json"}
for phrase in ["ACV Auctions"]:
    for frm in (0,100):
        p={"q":'"%s"'%phrase,"forms":"10-K","dateRange":"custom","startdt":"2024-01-01","enddt":"2026-09-12","from":frm}
        d=json.loads(urllib.request.urlopen(urllib.request.Request("https://efts.sec.gov/LATEST/search-index?"+urllib.parse.urlencode(p),headers=UA2),timeout=60).read())
        print(phrase,"total",d["hits"]["total"]["value"])
        cc=collections.Counter(tuple(h["_source"].get("display_names",[])) for h in d["hits"]["hits"])
        for k,v in cc.items(): print("  ",v,k)
for t,c in peers.items():
    try: print("fts ACV in",t, fts_count("ACV", cik=c, forms="10-K"))
    except Exception as e: print("fts err",t,e)
