import sys, json
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
raw = sources._get("https://data.sec.gov/submissions/CIK0001835591.json",
                   headers=sources.SEC_UA, cache_name="sub_vizio.json", max_age_h=240)
d = json.loads(raw)
print("name:", d["name"], "| tickers:", d.get("tickers"), "| exchanges:", d.get("exchanges"))
print("fiscalYearEnd:", d.get("fiscalYearEnd"), "| category:", d.get("category"))
print("former names:", [f["name"] for f in d.get("formerNames",[])])
r = d["filings"]["recent"]
rows = list(zip(r["filingDate"], r["form"], r["accessionNumber"], r["primaryDocument"], r["reportDate"]))
rows.sort(reverse=True)
for x in rows[:45]:
    print(" | ".join(x))
print("--- older files:", d["filings"].get("files"))
