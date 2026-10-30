import json, sys, time, os, re
import requests
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip, deflate"}
def get(url, fn=None, binary=False):
    r = requests.get(url, headers=UA, timeout=60)
    r.raise_for_status()
    if fn:
        with open(fn, "wb" if binary else "w", encoding=None if binary else "utf-8") as f:
            f.write(r.content if binary else r.text)
    return r
CIKS = {"COST":909832, "WMT":104169, "BJ":1531152, "TGT":27419, "AMZN":1018724, "KR":56873, "PSMT":1041803}
os.makedirs("edgar", exist_ok=True)
for t, c in CIKS.items():
    sub = get(f"https://data.sec.gov/submissions/CIK{c:010d}.json").json()
    json.dump(sub, open(f"edgar/{t}_sub.json","w"))
    time.sleep(0.2)
    facts = get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json").json()
    json.dump(facts, open(f"edgar/{t}_facts.json","w"))
    time.sleep(0.2)
    rf = sub["filings"]["recent"]
    print(f"== {t} {sub['name']} fy-end {sub.get('fiscalYearEnd')}")
    n=0
    for i,(form,dt,acc,desc) in enumerate(zip(rf["form"], rf["filingDate"], rf["accessionNumber"], rf["primaryDocument"])):
        if form in ("10-K","10-Q","DEF 14A","8-K","10-K/A") and dt >= "2025-06-01":
            print(f"   {form:8} {dt} {acc} {desc}")
            n+=1
        if n>40: break
