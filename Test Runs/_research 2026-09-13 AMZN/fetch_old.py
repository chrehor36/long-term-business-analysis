import sys, os, json, time, urllib.request
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
sys.path.insert(0, os.path.join(os.getcwd(), "Test Runs/_research 2026-09-13 AMZN"))
import sources as S
from fetch import grab
r = json.load(open("Test Runs/_research 2026-09-13 AMZN/submissions.json"))
for fobj in r["filings"].get("files", []):
    txt = S._get("https://data.sec.gov/submissions/" + fobj["name"], S.SEC_UA, fobj["name"], max_age_h=24)
    rr = json.loads(txt)
    for i, f in enumerate(rr["form"]):
        if f == "10-K" and rr["filingDate"][i] >= "2016-01-01":
            print(f, rr["filingDate"][i], rr["accessionNumber"][i], rr["primaryDocument"][i])
            if rr["filingDate"][i][:4] in ("2018", "2019", "2020"):
                grab("1018724", rr["accessionNumber"][i], rr["primaryDocument"][i], "10K_filed" + rr["filingDate"][i][:4])
                time.sleep(0.5)
