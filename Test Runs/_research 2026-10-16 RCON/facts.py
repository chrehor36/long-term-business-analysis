"""Print annual (FY, 20-F) values for chosen us-gaap tags, latest filing per fiscal year end. Arithmetic transcription only."""
import json, sys
d = json.load(open("cache/facts.json"))["facts"]["us-gaap"]
tags = sys.argv[1:]
for t in tags:
    if t not in d: print(t, "MISSING"); continue
    for unit, rows in d[t]["units"].items():
        best = {}
        for r in rows:
            if r.get("form", "").startswith("20-F") and r["end"][5:] == "06-30":
                if "start" in r and (int(r["end"][:4]) - int(r["start"][:4])) != 1: continue
                k = r["end"]
                if k not in best or r["filed"] > best[k]["filed"]: best[k] = r
        print(t, unit, " ".join(f"{k[:4]}:{v['val']:,.0f}" for k, v in sorted(best.items())))
