"""Competitor row (CONVENTION of this run: the KBR 10-K names no rival). Pull annual revenue and
operating income from each rival's own XBRL company facts, with the accession of the 10-K that filed
each value (newest vintage, so a restated year shows as restated). Transcription only."""
import json, os, sys, urllib.request, time
from datetime import date
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
HERE = os.path.dirname(os.path.abspath(__file__))
def facts(cik):
    fn = os.path.join(HERE, "cache", f"facts_{cik}.json")
    if not os.path.exists(fn):
        req = urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{int(cik):010d}.json", headers=UA)
        open(fn, "wb").write(urllib.request.urlopen(req, timeout=60).read()); time.sleep(0.3)
    return json.load(open(fn, encoding="utf-8"))
def annual(f, tags):
    out = {}
    for t in tags:
        node = f["facts"].get("us-gaap", {}).get(t)
        if not node: continue
        for x in node["units"].get("USD", []):
            if x.get("form") != "10-K" or not x.get("start"): continue
            d = (date.fromisoformat(x["end"]) - date.fromisoformat(x["start"])).days
            if not 350 <= d <= 380: continue
            k = x["end"]
            if k not in out or x["filed"] > out[k][2]:
                if k in out and out[k][3] != t: continue
                out[k] = (x["val"] / 1e6, x["accn"], x["filed"], t)
    return out
PEERS = {"KBR": 1357615, "LDOS": 1336920, "CACI": 16058, "BAH": 1443646}
for name, cik in PEERS.items():
    f = facts(cik)
    rev = annual(f, ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax"])
    oi = annual(f, ["OperatingIncomeLoss"])
    print(f"== {name} ({f['entityName']}, CIK {cik})")
    for k in sorted(oi):
        if k < "2016-06-01": continue
        r = rev.get(k)
        rv = r[0] if r else float('nan')
        print(f"  FY end {k}  revenue {rv:10.0f}  operating income {oi[k][0]:8.0f}  margin {oi[k][0]/rv*100:5.1f}%  accn {oi[k][1]}")
