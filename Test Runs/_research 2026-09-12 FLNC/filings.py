import sys, os, json
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
cik, name = sources.cik_for("FLNC")
print(cik, name)
txt = sources._get(f"https://data.sec.gov/submissions/CIK{cik}.json", sources.SEC_UA, f"sub_{cik}.json", max_age_h=6)
open("Test Runs/_research 2026-09-12 FLNC/submissions.json","w",encoding="utf-8").write(txt)
d = json.loads(txt)
r = d["filings"]["recent"]
keep = {"10-K","10-Q","DEF 14A","8-K","8-K/A","10-K/A","S-1","424B4","SC 13D","SC 13D/A","S-3","S-3ASR","424B5","SCHEDULE 13D/A","SCHEDULE 13D"}
for i in range(len(r["form"])):
    if r["form"][i] in keep:
        print(f'{r["form"][i]:<10} filed {r["filingDate"][i]}  period {r["reportDate"][i]:<12} acc {r["accessionNumber"][i]}  {r["primaryDocument"][i]}  items={r["items"][i]}')
print(sources.sovereign("USD"))
