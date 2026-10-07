import sys, os, json
sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "tools"))
import sources
T = {
 "rev": ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "SalesRevenueNet"],
 "cor": ["CostOfRevenue", "CostOfGoodsAndServicesSold"],
 "gp": ["GrossProfit"],
 "op": ["OperatingIncomeLoss"],
 "sbc": ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"],
 "ocf": ["NetCashProvidedByUsedInOperatingActivities"],
 "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"],
 "capsw": ["PaymentsToDevelopSoftware", "PaymentsForSoftware"],
}
tick = sys.argv[1:] or ["SNOW", "MDB", "TDC", "DDOG", "ESTC", "CFLT", "PLTR"]
out = {}
for t in tick:
    cik = sources.cik_for(t)[0]
    f = sources.sec_facts(cik)
    row = {"cik": cik, "name": f.get("entityName")}
    for k, tags in T.items():
        a = sources.annual(f, tags, vintage="newest")[0]
        row[k] = {d: round(x, 1) for d, x in sorted(a.items())[-5:]}
    out[t] = row
    print(t, cik, row["name"])
    for k in T:
        print("  ", k, row[k])
json.dump(out, open(os.path.join(os.path.dirname(__file__), "peers", "peers_facts.json"), "w"), indent=1)
