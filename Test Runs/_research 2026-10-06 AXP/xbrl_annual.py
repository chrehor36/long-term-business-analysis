"""Transcribe annual (FY, 10-K) XBRL facts for a CIK. Arithmetic support only; the filed statements govern.
Usage: python xbrl_annual.py CIK TAG [TAG ...]   (fetches companyfacts from data.sec.gov with a contact User-Agent)"""
import sys, json, urllib.request
UA = "Long-Term Business Analysis research chrehor36@gmail.com"
cik = sys.argv[1].zfill(10)
req = urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json", headers={"User-Agent": UA})
facts = json.load(urllib.request.urlopen(req))["facts"]
for tag in sys.argv[2:]:
    node = facts.get("us-gaap", {}).get(tag)
    if not node:
        print(tag, "not tagged"); continue
    for unit, rows in node["units"].items():
        seen = {}
        for r in rows:
            if r.get("form") != "10-K" or r.get("fp") != "FY": continue
            # annual duration or instant at FY end; keep the first-filed value per period end
            if "start" in r:
                from datetime import date
                s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                if (e - s).days < 350: continue
            key = r["end"]
            if key not in seen or r["filed"] < seen[key]["filed"]:
                seen[key] = r
        for k in sorted(seen)[-8:]:
            r = seen[k]
            print(f"{tag:55s} {unit:6s} {k} {r['val']:>16,} {r['accn']}")
