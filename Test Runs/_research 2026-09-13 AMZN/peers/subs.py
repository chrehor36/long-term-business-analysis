import sys, os, json, urllib.request, time
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "tools"))
import sources
HERE = os.path.dirname(os.path.abspath(__file__))
CIKS = {"GOOGL": 1652044, "META": 1326801, "EBAY": 1065088, "MELI": 1099590,
        "PDD": 1737806, "SHOP": 1594805, "ORCL": 1341439, "MSFT": 789019, "WMT": 104169}
FORMS = {"10-K", "10-Q", "20-F", "6-K", "40-F", "10-K/A", "20-F/A"}
for t, c in CIKS.items():
    url = f"https://data.sec.gov/submissions/CIK{c:010d}.json"
    req = urllib.request.Request(url, headers=sources.SEC_UA)
    raw = urllib.request.urlopen(req, timeout=60).read()
    open(os.path.join(HERE, f"submissions_{t}.json"), "wb").write(raw)
    j = json.loads(raw)
    r = j["filings"]["recent"]
    print("==", t, j["name"])
    n = 0
    for i in range(len(r["form"])):
        if r["form"][i] in FORMS and r["filingDate"][i] >= "2026-01-01":
            print(" ", r["form"][i], r["reportDate"][i], r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i], r["primaryDocDescription"][i])
            n += 1
    time.sleep(0.3)
