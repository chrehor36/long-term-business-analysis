import sys, os, json
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
f = sources.sec_facts("0001868941")
json.dump(f, open("Test Runs/_research 2026-09-12 FLNC/companyfacts.json","w"))
g = f["facts"]["us-gaap"]
tags = ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","CostOfGoodsAndServicesSold","GrossProfit","NetIncomeLoss","ProfitLoss",
 "NetCashProvidedByUsedInOperatingActivities","ShareBasedCompensation","DepreciationDepletionAndAmortization","DepreciationAndAmortization",
 "PaymentsToAcquirePropertyPlantAndEquipment","PaymentsForSoftware","PaymentsToDevelopSoftware",
 "IncreaseDecreaseInAccountsPayable","IncreaseDecreaseInContractWithCustomerLiability","IncreaseDecreaseInDeferredRevenue","IncreaseDecreaseInInventories",
 "IncreaseDecreaseInAccountsReceivable","IncreaseDecreaseInAccruedLiabilities","ContractWithCustomerLiabilityCurrent","InventoryNet","AccountsPayableCurrent",
 "CashAndCashEquivalentsAtCarryingValue","StockholdersEquity","MinorityInterest"]
for t in tags:
    if t not in g: print("--", t, "absent"); continue
    for unit, rows in g[t]["units"].items():
        ann = {}
        for r in rows:
            if r.get("form") in ("10-K","10-K/A") and (r.get("fp")=="FY"):
                if "start" in r:
                    from datetime import date
                    s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                    if not (340 <= (e-s).days <= 380): continue
                ann[r["end"]] = (r["val"], r["accn"], r["filed"])
        print(t, unit, {k: round(v[0]/1e6,1) for k,v in sorted(ann.items())})
