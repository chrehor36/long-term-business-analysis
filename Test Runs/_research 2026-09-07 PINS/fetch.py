import json, os, sys, time, urllib.request
sys.stdout.reconfigure(encoding="utf-8")
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
OUT=os.path.dirname(os.path.abspath(__file__))
def get(url,tries=4):
    last=None
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=120).read()
        except Exception as e:
            last=e; time.sleep(1.5*(i+1))
    raise last
CIK=1506293
# submissions
sub=json.loads(get(f"https://data.sec.gov/submissions/CIK{CIK:010d}.json"))
open(os.path.join(OUT,"submissions.json"),"wb").write(json.dumps(sub).encode())
r=sub["filings"]["recent"]
rows=[]
for i in range(len(r["form"])):
    if r["form"][i] in ("10-K","10-Q","DEF 14A","8-K","10-K/A"):
        rows.append((r["form"][i],r["filingDate"][i],r["reportDate"][i],r["accessionNumber"][i],r["primaryDocument"][i]))
print("name:",sub.get("name"))
for x in rows[:60]: print(x)
print("---10-K only---")
for x in rows:
    if x[0].startswith("10-K"): print(x)
