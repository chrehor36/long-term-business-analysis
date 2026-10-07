import sys, os, json
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources

cik, name = sources.cik_for("BA")
print("CIK", cik, name)
f = sources.sec_facts(cik)

TAGS = {
 "OCF": ["NetCashProvidedByUsedInOperatingActivities",
         "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
 "CAPEX": ["PaymentsToAcquirePropertyPlantAndEquipment",
           "PaymentsToAcquireProductiveAssets"],
 "DA": ["DepreciationDepletionAndAmortization","DepreciationAmortizationAndAccretionNet",
        "DepreciationAndAmortization"],
 "SBC": ["ShareBasedCompensation","AllocatedShareBasedCompensationExpense"],
 "NI":  ["NetIncomeLoss","ProfitLoss"],
 "REV": ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax"],
}
series = {}
for k, tags in TAGS.items():
    d, used, unit = sources.annual(f, tags, vintage="newest")
    series[k] = d
    print(f"\n{k}  tags={used} unit={unit}")
    for e in sorted(d):
        print(f"   {e}  {d[e]:>12,.1f}")
json.dump(series, open("Test Runs/_research 2026-09-12 BA/series.json","w"), indent=1)
