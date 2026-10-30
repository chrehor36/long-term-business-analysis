import sys, json
sys.path.insert(0, r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-13 ABNB')
from fetch import get
cos = {"BKNG":"0001075531","EXPE":"0001324424","TCOM":"0001269238","MAR":"0001048286"}
for t,c in cos.items():
    j = json.loads(get(f"https://data.sec.gov/submissions/CIK{c}.json", f"sub_{t}.json"))
    r = j['filings']['recent']
    rows = list(zip(r['form'], r['filingDate'], r['reportDate'], r['accessionNumber'], r['primaryDocument']))
    extra = j['filings'].get('files', [])
    for f in extra:
        jj = json.loads(get("https://data.sec.gov/submissions/"+f['name'], f"sub_{t}_{f['name']}"))
        rows += list(zip(jj['form'], jj['filingDate'], jj['reportDate'], jj['accessionNumber'], jj['primaryDocument']))
    print("==", t, j['name'])
    for x in rows:
        if x[0] in ("10-K","10-Q","20-F","10-K/A","20-F/A") and x[1] >= "2020-01-01":
            print("  ", x)
