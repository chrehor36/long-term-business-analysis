import json, urllib.request, sys
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources as s
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=90).read()
d=json.load(open("submissions.json"))
r=d["filings"]["recent"]
for i in range(len(r["form"])):
    if r["form"][i] in ("40-F","40-F/A"):
        print(r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i])
print(d["filings"].get("files"))
m=s.ticker_map()
for t in ["BPYPP","BPYPO","BPYPN","BPYPM","BBUC","BEPC","BIPC","BNT","BAM","BNH","BNJ"]:
    print(t, m.get(t))
