import sys, os, json
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
OUT = "Test Runs/_research 2026-09-13 CNR"
tick = sys.argv[1]
cik = sys.argv[2] if len(sys.argv) > 2 else None
if cik is None:
    cik, name = sources.cik_for(tick)
    print(cik, name)
cik = str(cik).zfill(10)
txt = sources._get(f"https://data.sec.gov/submissions/CIK{cik}.json", sources.SEC_UA, f"sub_{cik}.json", max_age_h=6)
open(os.path.join(OUT, f"submissions_{tick}.json"), "w", encoding="utf-8").write(txt)
d = json.loads(txt)
print(d.get("name"), d.get("formerNames"))
r = d["filings"]["recent"]
keep = set(sys.argv[3].split(",")) if len(sys.argv) > 3 else {"10-K","10-Q","DEF 14A","DEFM14A","8-K","8-K/A","10-K/A","S-4","S-4/A","425","DEFA14A"}
for i in range(len(r["form"])):
    if r["form"][i] in keep:
        print(f'{r["form"][i]:<10} filed {r["filingDate"][i]}  period {r["reportDate"][i]:<12} acc {r["accessionNumber"][i]}  {r["primaryDocument"][i]}  items={r["items"][i]}')
