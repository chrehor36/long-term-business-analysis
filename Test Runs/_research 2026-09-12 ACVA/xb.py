import json
cf=json.load(open("companyfacts.json"))
g=cf["facts"]["us-gaap"]
def ann(tag, unit="USD"):
    if tag not in g: return None
    out={}
    for u,arr in g[tag]["units"].items():
        for x in arr:
            if x.get("fp")=="FY" and x.get("form") in ("10-K","10-K/A") and x.get("frame") is None or (x.get("form")=="10-K" and "start" in x):
                if "start" in x:
                    s,e=x["start"],x["end"]
                    from datetime import date
                    d=(date.fromisoformat(e)-date.fromisoformat(s)).days
                    if d>350 and d<380:
                        out.setdefault(e,[]).append((x["filed"],x["val"],x["accn"]))
    return {k:sorted(v)[-1] for k,v in sorted(out.items())}
tags=["NetCashProvidedByUsedInOperatingActivities","ShareBasedCompensation","AllocatedShareBasedCompensationExpense","PaymentsToAcquirePropertyPlantAndEquipment","PaymentsForSoftware","PaymentsToDevelopSoftware","DepreciationDepletionAndAmortization","DepreciationAmortizationAndAccretionNet","IncreaseDecreaseInAccountsPayable","IncreaseDecreaseInAccountsReceivable","Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","PaymentsToAcquireBusinessesNetOfCashAcquired","NetIncomeLoss","ProvisionForDoubtfulAccounts","PaymentsForProceedsFromLoansAndLeases","IncreaseDecreaseInFinanceReceivables","PaymentsForRepurchaseOfCommonStock","AmortizationOfIntangibleAssets"]
for t in tags:
    a=ann(t)
    if a: print(t, {k[:4]:(v[1]/1e3, v[0]) for k,v in a.items()})
    else: print(t,"--")
print([k for k in g if "Software" in k or "Finance" in k or "Capitaliz" in k][:40])
