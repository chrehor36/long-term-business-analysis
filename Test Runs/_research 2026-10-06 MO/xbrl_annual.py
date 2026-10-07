"""Print annual (FY, 10-K) values of chosen us-gaap tags from the cached company facts, first-filed vintage.
Transcription only. Usage: python xbrl_annual.py cache/companyfacts.json TAG [TAG ...]"""
import json, sys

facts = json.load(open(sys.argv[1]))["facts"]["us-gaap"]
for tag in sys.argv[2:]:
    if tag not in facts:
        print(tag, "not found")
        continue
    units = facts[tag]["units"]
    unit = "USD" if "USD" in units else list(units)[0]
    rows = {}
    for f in units[unit]:
        if f.get("form") != "10-K" or f.get("fp") != "FY":
            continue
        if "start" in f:
            # annual duration only
            from datetime import date
            s = date.fromisoformat(f["start"]); e = date.fromisoformat(f["end"])
            if not (350 <= (e - s).days <= 380):
                continue
        end = f["end"]
        if end not in rows or f["filed"] < rows[end][1]:
            rows[end] = (f["val"], f["filed"], f["accn"])
    print(tag, unit)
    for end in sorted(rows)[-11:]:
        v, filed, accn = rows[end]
        print(f"   {end}  {v/1e6 if unit=='USD' else v:>12,.0f}  filed {filed}  {accn}")
