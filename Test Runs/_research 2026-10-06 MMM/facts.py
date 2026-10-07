"""Print annual (FY, 10-K) values of chosen us-gaap tags from cached companyfacts, as first filed and as last filed.
Usage: python -I facts.py cache/companyfacts.json TAG [TAG ...]
Transcription only; every figure used in the run is read back against the filed statement."""
import sys, json

d = json.load(open(sys.argv[1]))["facts"]["us-gaap"]
for tag in sys.argv[2:]:
    if tag not in d:
        print(tag, "not tagged"); continue
    units = d[tag]["units"]
    for u, rows in units.items():
        by_end = {}
        for r in rows:
            if r.get("form") != "10-K" or r.get("fp") != "FY":
                continue
            if "start" in r:
                # annual duration only
                y0, y1 = int(r["start"][:4]), int(r["end"][:4])
                if not (r["start"][5:] in ("01-01",) and r["end"][5:] == "12-31" and y0 == y1):
                    continue
            by_end.setdefault(r["end"], []).append((r["filed"], r["val"], r["accn"]))
        print(f"== {tag} [{u}]")
        for end in sorted(by_end):
            v = sorted(by_end[end])
            first, last = v[0], v[-1]
            print(f"  {end}  first {first[1]:>16,}  ({first[2]})   last {last[1]:>16,}  ({last[2]})")
