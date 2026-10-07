"""Transcribe annual 10-K values from XBRL companyfacts (latest-filed vintage per FY end). Transcription only."""
import json, sys
d = json.load(open("CENT_facts.json"))["facts"]["us-gaap"]
tags = sys.argv[1].split(",")
rows = {}
for t in tags:
    if t not in d: print("missing", t); continue
    for unit, vals in d[t]["units"].items():
        for v in vals:
            if v.get("form") != "10-K" or v.get("fp") != "FY": continue
            if "start" in v:
                from datetime import date
                s = date.fromisoformat(v["start"]); e = date.fromisoformat(v["end"])
                if not (350 <= (e - s).days <= 380): continue
            key = v["end"]
            prev = rows.setdefault(key, {}).get(t)
            if prev is None or v["filed"] > prev[1]:
                rows[key][t] = (v["val"], v["filed"], v["accn"])
for k in sorted(rows):
    print(k, " | ".join(f"{t.split(':')[-1][:28]}={rows[k][t][0]/1e6:,.1f}" if t in rows[k] else f"{t[:28]}=-" for t in tags))
