"""Step 1: confirm tickers/CIKs, pull submissions, list annual and interim filings since 2021."""
import json, os
from p_common import get, jsave, HERE

TICKERS = ["PG", "CHD", "CLX", "KMB", "KVUE", "GIS", "SJM", "FRPT", "UL", "HLN"]
tk = json.loads(get("https://www.sec.gov/files/company_tickers.json"))
jsave(tk, "company_tickers.json")
m = {v["ticker"]: v for v in tk.values()}
out = {}
for t in TICKERS:
    v = m.get(t)
    print(t, v)
    if not v:
        continue
    cik = v["cik_str"]
    sub = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    jsave(sub, f"{t}_submissions.json")
    r = sub["filings"]["recent"]
    rows = []
    for i in range(len(r["form"])):
        f = r["form"][i]
        if f in ("10-K", "10-K/A", "20-F", "20-F/A", "10-Q", "10-KT") and r["filingDate"][i] >= "2021-01-01":
            rows.append(dict(form=f, filed=r["filingDate"][i], period=r["reportDate"][i],
                             acc=r["accessionNumber"][i], doc=r["primaryDocument"][i]))
    # older pages if any
    for fl in sub["filings"].get("files", []):
        print("  extra file", fl)
    out[t] = dict(cik=cik, name=sub["name"], fye=sub.get("fiscalYearEnd"), filings=rows)
    print(" ", sub["name"], "FYE", sub.get("fiscalYearEnd"))
    for x in rows:
        if x["form"] != "10-Q":
            print("   ", x)
    q = [x for x in rows if x["form"] == "10-Q"][:2]
    for x in q:
        print("    Q", x)
jsave(out, "index.json")
