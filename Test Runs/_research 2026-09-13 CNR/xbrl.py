import sys, os, json
from datetime import date
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
OUT = "Test Runs/_research 2026-09-13 CNR"
tick, cik = sys.argv[1], sys.argv[2]
p = os.path.join(OUT, f"companyfacts_{tick}.json")
if os.path.exists(p): f = json.load(open(p))
else:
    f = sources.sec_facts(cik); json.dump(f, open(p, "w"))
g = f["facts"]["us-gaap"]
tags = sys.argv[3].split(",") if len(sys.argv) > 3 else ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","NetIncomeLoss","ProfitLoss",
 "NetCashProvidedByUsedInOperatingActivities","ShareBasedCompensation","AllocatedShareBasedCompensationExpense","DepreciationDepletionAndAmortization","DepreciationAndAmortization",
 "PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets","PaymentsToAcquireMiningAssets",
 "AssetRetirementObligation","AssetRetirementObligationsNoncurrent","DefinedBenefitPlanFundedStatusOfPlan",
 "PaymentsForRepurchaseOfCommonStock","PaymentsOfDividendsCommonStock","PaymentsOfDividends","LongTermDebt","CashAndCashEquivalentsAtCarryingValue","StockholdersEquity",
 "IncomeTaxesPaidNet","IncomeTaxesPaid","IncomeTaxExpenseBenefit"]
for t in tags:
    if t not in g: print("--", t, "absent"); continue
    for unit, rows in g[t]["units"].items():
        ann = {}
        for r in rows:
            if r.get("form") in ("10-K","10-K/A") and r.get("fp")=="FY":
                if "start" in r:
                    s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                    if not (340 <= (e-s).days <= 380): continue
                if r["end"] not in ann or r["filed"] > ann[r["end"]][2]:
                    ann[r["end"]] = (r["val"], r["accn"], r["filed"])
        print(t, unit, {k[:4]: round(v[0]/1e6,1) for k,v in sorted(ann.items()) if k >= "2017"})
