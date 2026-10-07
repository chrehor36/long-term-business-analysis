"""Annual series (FY, 10-K, full-year duration) from SEC companyfacts, last-filed value per fiscal year.
Transcription only; the run cross-checks against the filed statements.
Usage: python series.py cache/companyfacts_X.json [tag ...]"""
import json, sys
from datetime import date

d = json.load(open(sys.argv[1]))
g = d["facts"]["us-gaap"]
tags = sys.argv[2:]


def annual(tag):
    out = {}
    for unit, rows in g.get(tag, {}).get("units", {}).items():
        for r in rows:
            if r.get("form") not in ("10-K", "10-K/A"):
                continue
            if "start" in r:
                s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                if not (350 <= (e - s).days <= 380):
                    continue
            y = int(r["end"][:4])
            # keep the earliest filing for each year-end (first-filed vintage)
            if y not in out or r["filed"] < out[y][1]:
                out[y] = (r["val"], r["filed"], r["accn"])
    return out


if __name__ == "__main__":
    data = {t: annual(t) for t in tags}
    years = sorted({y for t in data for y in data[t]})
    print("FY    " + "".join(f"{t[:22]:>24}" for t in tags))
    for y in years:
        print(f"{y}  " + "".join(f"{(data[t][y][0]/1e6 if y in data[t] else float('nan')):>24.1f}" for t in tags))
