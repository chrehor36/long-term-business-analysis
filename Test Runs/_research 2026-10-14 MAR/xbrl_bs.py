# instant (balance-sheet) values at fiscal year end from 10-K/20-F
import json, sys
def inst(cik, tags):
    d = json.load(open(f"cache/cf_{cik}.json")); out = {}
    for nsk, facts in d["facts"].items():
        for t in tags:
            if t not in facts: continue
            for unit, vals in facts[t]["units"].items():
                for v in vals:
                    if v.get("form") not in ("10-K","20-F") or "start" in v: continue
                    if v["end"][5:] not in ("12-31",): continue
                    k=(t,v["end"][:4])
                    if k not in out or v["filed"]>out[k][1]: out[k]=(v["val"],v["filed"])
    return out
cik=sys.argv[1]; tags=sys.argv[2].split(",")
o=inst(cik,tags); years=sorted({k[1] for k in o if k[1]>='2016'})
for t in tags: print(t[:40].ljust(40)," ".join(f"{y}:{o[(t,y)][0]/1e6:,.0f}" if (t,y) in o else f"{y}:-" for y in years))
