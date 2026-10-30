"""Print annual (10-K, FY) values of chosen us-gaap tags from a cached companyfacts file.
Usage: python -I facts.py <cik10> TAG [TAG ...]"""
import sys, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
cik = sys.argv[1]
j = json.load(open(os.path.join(HERE, "cache", f"facts_{cik}.json"), encoding="utf-8"))
g = j["facts"].get("us-gaap", {})
for tag in sys.argv[2:]:
    if tag not in g:
        print(tag, "MISSING"); continue
    units = g[tag]["units"]
    for u, rows in units.items():
        out = {}
        for r in rows:
            if r.get("form") not in ("10-K", "10-K/A"):
                continue
            # duration facts: keep ~1-year spans; instants: keep FY-end
            if "start" in r:
                from datetime import date
                s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                if not (350 <= (e - s).days <= 380):
                    continue
            key = r["end"]
            # keep latest filed vintage per period end
            if key not in out or r["filed"] > out[key][1]:
                out[key] = (r["val"], r["filed"], r["accn"])
        print(f"{tag} [{u}]")
        for k in sorted(out)[-11:]:
            v, f, a = out[k]
            print(f"   {k}  {v/1e6 if abs(v) > 1e4 else v:>12,.1f}  filed {f} {a}")
