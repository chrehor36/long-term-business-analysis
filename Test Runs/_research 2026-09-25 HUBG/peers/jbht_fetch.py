"""Fetch JBHT 10-K filings (FY2019, FY2022, FY2024) primary documents as text, for the JBI segment line.
Transcription only."""
import json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from fetch import get, strip
cik = "728535"
sub = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik.zfill(10)}.json"))
r = sub["filings"]["recent"]
want = {"2020", "2023", "2025"}
for form, acc, doc, fd, rd in zip(r["form"], r["accessionNumber"], r["primaryDocument"], r["filingDate"], r["reportDate"]):
    if form == "10-K" and fd[:4] in want:
        a = acc.replace("-", "")
        url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{doc}"
        out = os.path.join(HERE, f"JBHT_10K_FY{rd[:4]}.txt")
        open(out, "w", encoding="utf-8").write(strip(get(url)))
        print(form, acc, fd, rd, doc, out, os.path.getsize(out))
        time.sleep(0.5)
