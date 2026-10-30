"""List a filer's 10-K filings from its EDGAR submissions JSON (saved under cache/).
Usage: python find_filings.py CIK10 FORM [since]"""
import json, sys, time, urllib.request, pathlib
cik, form = sys.argv[1], sys.argv[2]
since = sys.argv[3] if len(sys.argv) > 3 else "2015-01-01"
UA = "Long-Term Business Analysis research chrehor36@gmail.com"
p = pathlib.Path(__file__).parent / "cache" / f"subs_{cik}.json"
if not p.exists():
    for a in range(8):
        try:
            raw = urllib.request.urlopen(urllib.request.Request(
                f"https://data.sec.gov/submissions/CIK{cik}.json", headers={"User-Agent": UA}), timeout=60).read()
            break
        except Exception as e:
            print("retry", e, file=sys.stderr); time.sleep(15 * (a + 1))
    p.write_bytes(raw)
d = json.load(open(p))
print(d["name"])
r = d["filings"]["recent"]
for i in range(len(r["form"])):
    if r["form"][i] == form and r["filingDate"][i] >= since:
        print(r["form"][i], r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i], r["reportDate"][i])
