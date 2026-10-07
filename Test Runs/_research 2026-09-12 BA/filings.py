import sys, os, json, urllib.request
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
txt = sources._get("https://data.sec.gov/submissions/CIK0000012927.json", sources.SEC_UA, "sub_BA.json", max_age_h=6)
d = json.loads(txt)
r = d["filings"]["recent"]
keep = {"10-K","10-Q","DEF 14A","8-K","8-K/A","10-K/A"}
n=0
for i in range(len(r["form"])):
    if r["form"][i] in keep:
        print(f'{r["form"][i]:<8} filed {r["filingDate"][i]}  period {r["reportDate"][i]:<12} acc {r["accessionNumber"][i]}  {r["primaryDocument"][i]}')
        n+=1
    if n>45: break
