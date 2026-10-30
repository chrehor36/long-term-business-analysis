import json, sys
def annual(f, tag, unit="USD"):
    try: arr = f["facts"]["us-gaap"][tag]["units"][unit]
    except KeyError: return {}
    out = {}
    for x in arr:
        if x.get("form") not in ("10-K","10-K/A"): continue
        if "start" in x:
            from datetime import date
            s = date.fromisoformat(x["start"]); e = date.fromisoformat(x["end"])
            if not (340 <= (e-s).days <= 380): continue
        y = x["end"][:4] if x["end"][5:7] not in ("01","02","03","04") else str(int(x["end"][:4]))
        key = x["end"]
        # keep latest filed value per period end
        if key not in out or x["filed"] > out[key][1]:
            out[key] = (x["val"], x["filed"], x.get("accn"))
    return out
for cik in sys.argv[1:]:
    f = json.load(open(f"facts_{cik}.json"))
    print("=====", f["entityName"], cik)
    tags = ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","OperatingLeasesIncomeStatementLeaseRevenue","OperatingIncomeLoss","InterestExpense","InterestExpenseNonoperating","NetIncomeLoss","Assets","StockholdersEquity","LongTermDebt","LongTermDebtNoncurrent","DebtInstrumentCarryingAmount","NetCashProvidedByUsedInOperatingActivities","PaymentsToAcquireProductiveAssets","PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireEquipmentOnLease","ProceedsFromSaleOfProductiveAssets","ProceedsFromSaleOfPropertyPlantAndEquipment","ShareBasedCompensation","DepreciationDepletionAndAmortization","Depreciation","CashAndCashEquivalentsAtCarryingValue","IncomeTaxesPaidNet","InterestPaidNet"]
    for t in tags:
        a = annual(f, t)
        if not a: continue
        ks = sorted(a)[-19:]
        print(t, " ".join(f"{k[:7]}:{a[k][0]/1e6:.0f}" for k in ks))
