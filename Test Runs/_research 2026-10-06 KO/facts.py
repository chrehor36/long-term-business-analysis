"""Annual (10-K, FY, 12-month) values of chosen us-gaap tags for KO, latest-filed vintage per fiscal-year end.
Usage: python facts.py TAG [TAG ...]   (USD millions; shares tags printed raw)"""
import json, os, sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
F = json.load(open(os.path.join(HERE, "cache", "companyfacts_KO.json")))["facts"]


def annual(tag, ns="us-gaap"):
    try:
        units = F[ns][tag]["units"]
    except KeyError:
        return {}
    out = {}
    for u, rows in units.items():
        for r in rows:
            if r.get("form") not in ("10-K", "10-K/A"):
                continue
            end = r["end"]
            if "start" in r:
                d0 = date.fromisoformat(r["start"]); d1 = date.fromisoformat(end)
                if not (350 <= (d1 - d0).days <= 380):
                    continue
            key = end
            prev = out.get(key)
            if prev is None or r["filed"] > prev[1]:
                out[key] = (r["val"], r["filed"], r["accn"], u)
    return out


if __name__ == "__main__":
    for tag in sys.argv[1:]:
        ns = "us-gaap"
        if ":" in tag:
            ns, tag = tag.split(":")
        a = annual(tag, ns)
        print("==", tag)
        for k in sorted(a)[-14:]:
            v, filed, accn, u = a[k]
            vv = v / 1e6 if u == "USD" else v
            print(f"  {k}  {vv:>14,.1f}  {u}  filed {filed}  {accn}")
