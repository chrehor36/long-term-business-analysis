"""Annual series from XBRL company facts (transcription only; the filed statements govern).
Usage: python series.py cache/<facts>.json [TAG ...]
For each tag prints FY-end value from the latest-filed 10-K covering that full fiscal year (duration ~ 1 year)."""
import sys, json
from datetime import date

def d(s):
    return date.fromisoformat(s)

facts = json.load(open(sys.argv[1]))
tags = sys.argv[2:] or [
    "Revenues", "NetCashProvidedByUsedInOperatingActivities", "ShareBasedCompensation",
    "PaymentsToAcquirePropertyPlantAndEquipment", "DepreciationDepletionAndAmortization",
    "NetIncomeLoss", "PaymentsForRepurchaseOfCommonStock", "PaymentsOfDividends",
    "WeightedAverageNumberOfDilutedSharesOutstanding", "OperatingIncomeLoss",
]
ug = facts["facts"].get("us-gaap", {})
for tag in tags:
    if tag not in ug:
        print(tag, "NOT FOUND"); continue
    units = ug[tag]["units"]
    u = list(units)[0]
    best = {}
    for f in units[u]:
        if f.get("form") not in ("10-K", "10-K/A"):
            continue
        if "start" in f:
            days = (d(f["end"]) - d(f["start"])).days
            if not (350 <= days <= 380):
                continue
        end = f["end"]
        if end not in best or f["filed"] > best[end]["filed"]:
            best[end] = f
    print("==", tag, u)
    for end in sorted(best)[-16:]:
        f = best[end]
        print(f"  {end}  {f['val']:>18,}  {f['accn']}  filed {f['filed']}")
