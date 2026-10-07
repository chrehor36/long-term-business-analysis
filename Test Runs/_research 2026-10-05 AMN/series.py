import json
f=json.load(open("facts.json"))["facts"]
g=f["us-gaap"]
def annual(tag, unit="USD"):
    if tag not in g: return {}
    out={}
    for x in g[tag]["units"].get(unit,[]):
        if x.get("form") in ("10-K","10-K/A") and x.get("fp")=="FY":
            s,e=x.get("start"),x["end"]
            if s and (int(e[:4])-int(s[:4]))*12+int(e[5:7])-int(s[5:7])<11: continue
            y=int(e[:4])
            # keep earliest filing (first-filed vintage) per year
            if y not in out or x["filed"]<out[y][1]: out[y]=(x["val"],x["filed"])
    return {k:v[0] for k,v in out.items()}
tags={"Rev":["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueServicesNet"],
"GP":["GrossProfit"],"OpInc":["OperatingIncomeLoss"],"NI":["NetIncomeLoss"],
"OCF":["NetCashProvidedByUsedInOperatingActivities"],"Capex":["PaymentsToAcquirePropertyPlantAndEquipment"],
"DA":["DepreciationDepletionAndAmortization","DepreciationAndAmortization","DepreciationAmortizationAndAccretionNet"],
"SBC":["ShareBasedCompensation"],"Int":["InterestExpense","InterestExpenseNonoperating","InterestIncomeExpenseNonoperatingNet"],
"GWimp":["GoodwillImpairmentLoss"],"Acq":["PaymentsToAcquireBusinessesNetOfCashAcquired"],
"Buyback":["PaymentsForRepurchaseOfCommonStock"],"Tax":["IncomeTaxExpenseBenefit"],"Pretax":["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest","IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"]}
res={}
for k,ts in tags.items():
    d={}
    for t in ts:
        for y,v in annual(t).items(): d.setdefault(y,v)
    res[k]=d
sh=annual("WeightedAverageNumberOfDilutedSharesOutstanding","shares")
res["DilSh"]=sh
yrs=sorted(set().union(*[set(d) for d in res.values()]))
print("year "+" ".join(f"{k:>8}" for k in res))
for y in yrs:
    if y<2008: continue
    print(y, " ".join(f"{(res[k].get(y)/1e6 if res[k].get(y) is not None else float('nan')):8.1f}" for k in res))
