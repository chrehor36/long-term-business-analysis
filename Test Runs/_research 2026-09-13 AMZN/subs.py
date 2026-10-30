import sys, os, json
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources as S
OUT = "Test Runs/_research 2026-09-13 AMZN"
txt = S._get("https://data.sec.gov/submissions/CIK0001018724.json", S.SEC_UA, "sub_0001018724.json", max_age_h=1)
open(os.path.join(OUT, "submissions.json"), "w", encoding="utf-8").write(txt)
r = json.loads(txt)["filings"]["recent"]
for i, f in enumerate(r["form"]):
    d = r["filingDate"][i]
    if d >= "2025-10-01" and f not in ("4", "3", "144", "SC 13G", "SC 13G/A"):
        print(f, d, r["accessionNumber"][i], r["primaryDocument"][i], r.get("items", [""])[i], r.get("primaryDocDescription", [""])[i])
print(S.deal_note("1018724"))
