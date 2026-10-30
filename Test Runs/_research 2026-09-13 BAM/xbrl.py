import sys, json
sys.path.insert(0, "tools")
import sources as s
f = s.sec_facts("0001937926")
json.dump(f, open("Test Runs/_research 2026-09-13 BAM/companyfacts.json","w"))
g = f["facts"].get("us-gaap", {})
for tag in ["NetCashProvidedByUsedInOperatingActivities","ShareBasedCompensation","DepreciationDepletionAndAmortization","DepreciationAndAmortization","PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireOtherProductiveAssets","PaymentsOfDividendsCommonStock","PaymentsOfDividends","AllocatedShareBasedCompensationExpense"]:
    if tag in g:
        for u, rows in g[tag]["units"].items():
            for r in rows:
                if r.get("fp") == "FY" or r.get("form") in ("10-K","20-F","40-F"):
                    print(tag, r.get("start"), r["end"], r["val"], r["form"], r["accn"])
    else:
        print(tag, "ABSENT")
print(s.annual(f, ["NetCashProvidedByUsedInOperatingActivities"]))
