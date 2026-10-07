import json
d = json.load(open("companyfacts.json"))
print(list(d["facts"].keys()))
for ns in d["facts"]:
    for tag in ["CashFlowsFromUsedInOperatingActivities","Revenue","PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities","GrossProfit"]:
        if tag in d["facts"][ns]:
            u = d["facts"][ns][tag]["units"]
            for cur, rows in u.items():
                fy = sorted({(r["end"], r["accn"]) for r in rows if r.get("form","").startswith("20-F") and r["start"][5:] == "01-01" and r["end"][5:]=="12-31"} if rows and "start" in rows[0] else set())
                print(ns, tag, cur, sorted({e for e,a in fy})[-12:], sorted({a for e,a in fy})[-3:])
