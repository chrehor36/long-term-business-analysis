"""Annual (10-K, FY, 12-month) values from SEC companyfacts, latest filing wins per period end. Transcription only."""
import json, sys
from datetime import date
def annual(t, tags, unit="USD"):
    d = json.load(open(f"cache/facts_{t}.json"))["facts"]
    out = {}
    for tag in tags:
        ns = "us-gaap" if tag in d.get("us-gaap", {}) else ("dei" if tag in d.get("dei", {}) else None)
        if not ns: continue
        for u, rows in d[ns][tag]["units"].items():
            if u != unit: continue
            for r in rows:
                if r.get("form") not in ("10-K", "10-K/A"): continue
                if "start" in r:
                    s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                    if not (350 <= (e - s).days <= 380): continue
                e = r["end"]
                if e not in out or r["filed"] > out[e][1]:
                    out.setdefault(e, None)
                    out[e] = (r["val"], r["filed"], tag)
    return dict(sorted(out.items()))
if __name__ == "__main__":
    t = sys.argv[1]
    for tags in sys.argv[2:]:
        res = annual(t, tags.split(","))
        print(tags)
        for e, (v, f, tag) in res.items():
            if e >= "2007": print("  ", e, round(v/1e6, 1) if abs(v) > 1e4 else v, tag)
