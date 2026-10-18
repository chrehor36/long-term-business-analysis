"""Print instant (balance-sheet) values at fiscal year ends from 10-K filings, first-filed vintage."""
import json, sys
def inst(path, tag):
    d = json.load(open(path))
    f = d["facts"].get("us-gaap", {}).get(tag)
    if not f: return {}
    out = {}
    for u, rows in f["units"].items():
        if u != "USD": continue
        for r in rows:
            if r.get("form") not in ("10-K", "10-K/A") or "start" in r: continue
            if r.get("fp") != "FY": continue
            e = r["end"]
            if e not in out or r["filed"] < out[e][1]:
                out[e] = (r["val"], r["filed"], r["accn"])
    return out
if __name__ == "__main__":
    path = sys.argv[1]
    for tag in sys.argv[2:]:
        a = inst(path, tag)
        print(tag, {e: round(a[e][0]/1e6,1) for e in sorted(a) if e >= "2014"})
