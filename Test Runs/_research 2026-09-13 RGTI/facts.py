import sys, os, json
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
OUT = "Test Runs/_research 2026-09-13 RGTI"
p = os.path.join(OUT, "companyfacts.json")
if not os.path.exists(p):
    f = sources.sec_facts("0001838359")
    json.dump(f, open(p, "w"))
f = json.load(open(p))
g = f["facts"]["us-gaap"]
def show(tag, forms=("10-K","10-Q","8-K"), unit=None, fy_only=False):
    if tag not in g: print("NO TAG", tag); return
    for u, rows in g[tag]["units"].items():
        seen = {}
        for r in rows:
            if r.get("form") not in forms: continue
            key = (r.get("start"), r["end"])
            seen.setdefault(key, []).append((r["filed"], r["form"], r["accn"], r["val"], r.get("fp")))
        print("==", tag, u)
        for k in sorted(seen, key=lambda x: (x[1], x[0] or "")):
            v = seen[k]
            print(" ", k, [(x[0], x[1], x[3]) for x in v][:4])
for t in sys.argv[1:]:
    show(t)
