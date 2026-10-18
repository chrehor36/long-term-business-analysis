import json, sys
f=json.load(open("cache/facts.json"))["facts"]["ifrs-full"]
def annual(tag, instant=False):
    out={}
    if tag not in f or "BRL" not in f[tag]["units"]: return out
    for x in f[tag]["units"]["BRL"]:
        if not x.get("form","").startswith("20-F"): continue
        e=x["end"]
        if instant:
            if "start" in x: continue
        else:
            if "start" not in x: continue
            # full year
            if not (x["start"][5:]=="01-01" and e[5:]=="12-31" and x["start"][:4]==e[:4]): continue
        key=e[:4]
        # prefer latest filed
        if key not in out or x["filed"]>out[key][1]:
            out[key]=(x["val"],x["filed"],x["accn"])
    return out
flows=["Revenue","CostOfSales","GrossProfit","ProfitLossFromOperatingActivities","ProfitLossBeforeTax","ProfitLoss","ProfitLossAttributableToOwnersOfParent","ProfitLossAttributableToNoncontrollingInterests","CurrentTaxExpenseIncome","DeferredTaxExpenseIncome","AdjustmentsForDepreciationAndAmortisationExpense","CashFlowsFromUsedInOperatingActivities","InterestPaidClassifiedAsOperatingActivities","IncomeTaxesRefundClassifiedAsOperatingActivities","PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities","PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities","CashFlowsFromUsedInInvestingActivities","DividendsPaidClassifiedAsFinancingActivities","PurchaseOfTreasuryShares","FinanceCosts","InterestExpenseOnBorrowings","ShareOfProfitLossOfAssociatesAndJointVenturesAccountedForUsingEquityMethod","AdjustmentsForUnrealisedForeignExchangeLossesGains","AdjustmentsForFinanceCosts","OtherCashPaymentsToAcquireEquityOrDebtInstrumentsOfOtherEntitiesClassifiedAsInvestingActivities","PurchaseOfInterestsInInvestmentsAccountedForUsingEquityMethod","ProceedsFromBorrowingsClassifiedAsFinancingActivities","RepaymentsOfBorrowingsClassifiedAsFinancingActivities"]
inst=["Assets","CashAndCashEquivalents","CurrentInvestments","Inventories","TradeReceivables","ShorttermBorrowings","LongtermBorrowings","LeaseLiabilities","Equity","EquityAttributableToOwnersOfParent","NoncontrollingInterests","IntangibleAssetsAndGoodwill","PropertyPlantAndEquipment","RetainedEarnings","InvestmentAccountedForUsingEquityMethod","InvestmentsInSubsidiariesJointVenturesAndAssociates","NoncurrentInventories","TradeAndOtherCurrentPayablesToTradeSuppliers","TradeAndOtherPayablesToTradeSuppliers","CurrentLiabilities","NoncurrentLiabilities","DeferredTaxAssets","OtherCurrentPayables"]
years=[str(y) for y in range(2015,2026)]
print("tag".ljust(60)," ".join(y.rjust(9) for y in years))
for t in flows:
    a=annual(t)
    print(t[:60].ljust(60)," ".join((f"{a[y][0]/1e6:9.0f}" if y in a else "        -") for y in years))
print()
for t in inst:
    a=annual(t,True)
    print(t[:60].ljust(60)," ".join((f"{a[y][0]/1e6:9.0f}" if y in a else "        -") for y in years))
