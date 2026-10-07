"""Why the triage could not price GFS: namespaces, units, annual periods, newest 20-F ingested. Transcription only."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "companyfacts.json")))
print("namespaces", {k: len(v) for k, v in d["facts"].items()})
ifrs = d["facts"]["ifrs-full"]
for tag in ["CashFlowsFromUsedInOperatingActivities", "PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities",
            "Revenue", "GrossProfit", "DepreciationAndAmortisationExpense", "AdjustmentsForSharebasedPayments",
            "ProfitLoss", "Equity", "EquityAttributableToOwnersOfParent"]:
    if tag not in ifrs:
        print(tag, "ABSENT"); continue
    for unit, facts in ifrs[tag]["units"].items():
        ann = sorted({(f["end"], f.get("fy"), f.get("form"), f.get("accn")) for f in facts
                      if f.get("form") in ("20-F", "F-1", "20-F/A") and ("start" not in f or (int(f["end"][:4]) - int(f["start"][:4]) in (0, 1) and f["end"][5:] == "12-31" and f["start"][5:] == "01-01"))})
        ends = sorted({a[0] for a in ann})
        print(tag, unit, len(facts), "annual ends:", ends)
        accns = sorted({a[3] for a in ann})
        print("   accessions:", accns)
us = d["facts"].get("us-gaap")
print("us-gaap present:", bool(us))
