import sys, json, os
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources as s, urllib.request
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read()
open("submissions.json","wb").write(get("https://data.sec.gov/submissions/CIK0001001085.json"))
d=json.load(open("submissions.json"))
print(d["name"], d.get("formerNames"), d.get("sicDescription"), d.get("stateOfIncorporation"), d.get("fiscalYearEnd"))
r=d["filings"]["recent"]
for i in range(len(r["form"])):
    if r["filingDate"][i] >= "2025-01-01" and r["form"][i] not in ("4","3","144","SC 13D/A","SC 13G/A"):
        print(r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i], r["primaryDocDescription"][i][:60])
print(s.sovereign("USD"))
for t in ["BN","BAM","BNT","BEP","BIP","BBU","BPY","BEPC","BIPC","BBUC"]:
    try: print(t, s.price(t))
    except Exception as e: print(t, "ERR", e)
