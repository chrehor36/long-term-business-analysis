"""List CALX filings from the EDGAR submissions endpoint. Transcription only."""
import json, urllib.request, os, sys
CIK = 1406666
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
HERE = os.path.dirname(os.path.abspath(__file__))
def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read().decode("utf-8","replace")
d = json.loads(get(f"https://data.sec.gov/submissions/CIK{CIK:010d}.json"))
open(os.path.join(HERE,"submissions.json"),"w",encoding="utf-8").write(json.dumps(d))
print("SIC", d.get("sic"), d.get("sicDescription"), "| FYE", d.get("fiscalYearEnd"), "| name", d.get("name"))
rec = d["filings"]["recent"]
rows = list(zip(rec["form"], rec["filingDate"], rec["accessionNumber"], rec["primaryDocument"], rec["reportDate"], rec.get("items", [""]*len(rec["form"]))))
# older pages
for f in d["filings"].get("files", []):
    dd = json.loads(get("https://data.sec.gov/submissions/" + f["name"]))
    rows += list(zip(dd["form"], dd["filingDate"], dd["accessionNumber"], dd["primaryDocument"], dd["reportDate"], dd.get("items", [""]*len(dd["form"]))))
want = ("10-K","10-Q","8-K","DEF 14A","10-K/A")
with open(os.path.join(HERE,"filing_index.txt"),"w",encoding="utf-8") as f:
    for r in rows:
        if r[0] in want:
            line = " | ".join(str(x) for x in r)
            f.write(line+"\n")
for r in rows:
    if r[0] in ("10-K","DEF 14A","10-K/A") or (r[0]=="10-Q" and r[1]>="2025-01-01") or (r[0]=="8-K" and r[1]>="2025-01-01"):
        print(" | ".join(str(x) for x in r))
