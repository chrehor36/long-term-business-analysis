"""Annual series from EDGAR company facts (10-K, full-year duration, first-filed vintage).
Usage: python series.py CIK10 TAG[,TAG2...] ...   (several tags joined by comma = first one found per year)
Transcription only: every figure used in the run is cross-checked against a filed statement."""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get
cik = sys.argv[1]
p = get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json", f"companyfacts_{cik}.json")
facts = json.load(open(p))["facts"]


def series(tag):
    out = {}
    for ns in ("us-gaap", "dei"):
        if tag in facts.get(ns, {}):
            for unit, rows in facts[ns][tag]["units"].items():
                for r in rows:
                    if r.get("form") != "10-K" or r.get("fp") != "FY":
                        continue
                    end = r["end"]
                    if "start" in r:
                        from datetime import date
                        s = date.fromisoformat(r["start"]); e = date.fromisoformat(end)
                        if not 350 <= (e - s).days <= 380:
                            continue
                    y = int(end[:4])
                    # first-filed vintage
                    if y not in out or r["filed"] < out[y][1]:
                        out[y] = (r["val"], r["filed"], r["accn"])
    return out


for arg in sys.argv[2:]:
    merged = {}
    for t in arg.split(","):
        for y, v in series(t).items():
            merged.setdefault(y, v)
    print(arg)
    for y in sorted(merged):
        if y >= 2008:
            v = merged[y]
            print(f"  {y}  {v[0]/1e6:>12,.1f}  filed {v[1]}  {v[2]}")
