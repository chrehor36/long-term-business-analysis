import json, urllib.request, sys
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources as s
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=90).read()
open("BWS_submissions.json","wb").write(get("https://data.sec.gov/submissions/CIK0001837429.json"))
d=json.load(open("BWS_submissions.json"))
print(d["name"], d.get("formerNames"))
r=d["filings"]["recent"]
for i in range(len(r["form"])):
    if r["filingDate"][i]>="2026-01-01" and r["form"][i] in ("20-F","6-K","40-F","6-K/A"):
        print(r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i])
print("split BN after 2026-08-13:", s.split_factor_after("BN","2026-08-13"))
print("BNT", s.price("BNT"))
