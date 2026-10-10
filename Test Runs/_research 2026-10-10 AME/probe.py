"""Probe one filer's tag: print every 10-K fact row (start, end, val, form, accn, frame). python probe.py CIK TAG [year]"""
import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
f = json.load(open(os.path.join(HERE, "cache", f"facts_{sys.argv[1].zfill(10)}.json")))
tag = sys.argv[2]
yr = sys.argv[3] if len(sys.argv) > 3 else ""
out = []
if tag == "LIST":
    for k, v in f["facts"]["us-gaap"].items():
        if any(w in k.lower() for w in sys.argv[3].split(",")):
            n = sum(len(x) for x in v["units"].values())
            out.append(f"{k} {n}")
else:
    g = f["facts"]["us-gaap"][tag]
    for u, rows in g["units"].items():
        for r in rows:
            if r.get("form", "").startswith("10-K") and yr in r["end"]:
                out.append(f"{r.get('start','')} {r['end']} {r['val']:>16,} {r['form']} {r['accn']} {r.get('frame','')}")
open(os.path.join(HERE, "cache", "probe_out.txt"), "w", encoding="utf-8").write("\n".join(out))
