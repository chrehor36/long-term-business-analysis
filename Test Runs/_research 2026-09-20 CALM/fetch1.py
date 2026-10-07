import sys, json, urllib.request, os
sys.path.insert(0, 'tools')
import sources
R = "Test Runs/_research 2026-09-20 CALM"
UA = {"User-Agent": "BRK research chrehor36@gmail.com"}
def get(url, path):
    if os.path.exists(path):
        return open(path, 'rb').read()
    req = urllib.request.Request(url, headers=UA)
    b = urllib.request.urlopen(req, timeout=60).read()
    open(path, 'wb').write(b)
    return b
sub = json.loads(get("https://data.sec.gov/submissions/CIK0000016160.json", R + "/submissions.json"))
print("name:", sub["name"], "| sic:", sub["sic"], sub["sicDescription"], "| fye:", sub["fiscalYearEnd"], "| state:", sub.get("stateOfIncorporation"))
print("tickers:", sub["tickers"], sub["exchanges"])
print("former:", [f["name"] for f in sub.get("formerNames", [])])
print("older files:", [f["name"] for f in sub["filings"].get("files", [])])
r = sub["filings"]["recent"]
rows = list(zip(r["form"], r["filingDate"], r["reportDate"], r["accessionNumber"], r["primaryDocument"], r["items"]))
for f in ("10-K", "10-Q", "8-K", "DEF 14A"):
    sel = [x for x in rows if x[0] == f][:8]
    print("\n==", f)
    for x in sel:
        print("  ", x[1], "report", x[2], x[3], x[4], "|", x[5][:60])
