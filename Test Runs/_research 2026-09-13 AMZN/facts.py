import sys, os, json
sys.path.insert(0, "tools")
import sources as S
f = S.sec_facts("0001018724")
json.dump(f, open("Test Runs/_research 2026-09-13 AMZN/companyfacts.json", "w"))
kw = ["Lease", "PropertyAndEquipment", "PropertyPlant", "Financing", "ShareBased", "Depreciation", "OperatingActivities", "Incentive", "BuildToSuit"]
for ns in f["facts"]:
    for tag, v in f["facts"][ns].items():
        if any(k.lower() in tag.lower() for k in kw):
            u = v["units"].get("USD", [])
            fy = sorted({(x["end"], x["val"]) for x in u if x.get("form") == "10-K" and x.get("fp") == "FY" and x.get("start","")[:4] == x["end"][:4] and x["end"][5:] == "12-31"})
            if fy:
                print(ns, tag, [(e[:4], round(val/1e6)) for e, val in fy][-10:])
