#!/usr/bin/env python3
"""Fetch ANF EDGAR submissions index + peer companyfacts into the bt17 cache, and list
the 10-K / 10-Q / DEF 14A accessions so the documents themselves can be pulled."""
import json, os, sys, time
import urllib.request

ROOT = r"c:\Users\chreh\OneDrive\Documents\BRK"
OUT = os.path.join(ROOT, "Test Runs", "_research 2026-09-02 ANF")
CACHE = os.path.join(ROOT, "Backtests", "bt17_cache")
UA = {"User-Agent": "Long-Term Business Analysis chrehor36@gmail.com"}


def get(url, dest=None, binary=False):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    if dest:
        with open(dest, "wb") as f:
            f.write(data)
    return data if binary else data.decode("utf-8", "replace")


# 1. peer companyfacts into the shared cache
for cik in (39911, 912615, 1397187):
    p = os.path.join(CACHE, f"facts_{cik}.json")
    if not os.path.exists(p):
        get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json", dest=p)
        print("fetched facts", cik)
        time.sleep(0.4)

# 2. ANF submissions
sub_p = os.path.join(OUT, "anf_submissions.json")
if not os.path.exists(sub_p):
    get("https://data.sec.gov/submissions/CIK0001018840.json", dest=sub_p)
sub = json.load(open(sub_p, encoding="utf-8"))
rec = sub["filings"]["recent"]
rows = list(zip(rec["accessionNumber"], rec["form"], rec["filingDate"],
                rec["reportDate"], rec["primaryDocument"]))
print(f"\nrecent filings: {len(rows)} (older files: {[f['name'] for f in sub['filings'].get('files', [])]})")
for acc, form, fdate, rdate, doc in rows:
    if form in ("10-K", "10-K/A", "10-Q", "DEF 14A", "8-K", "S-8") and form != "S-8":
        if form == "8-K" and fdate < "2026-05-01":
            continue
        print(f"{form:9s} filed {fdate}  period {rdate}  {acc}  {doc}")
