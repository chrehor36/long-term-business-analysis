import json, sys
d = json.load(open(sys.argv[1]))['facts']['ifrs-full']
flow = ["Revenue","ProfitLossFromOperatingActivities","ProfitLossBeforeTax","IncomeTaxExpenseContinuingOperations","ProfitLoss","ProfitLossAttributableToOwnersOfParent","ProfitLossFromDiscontinuedOperations",
"CashFlowsFromUsedInOperatingActivities","CashFlowsFromUsedInOperatingActivitiesDiscontinuedOperations","AdjustmentsForDepreciationAndAmortisationExpense","PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities","PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities",
"CashFlowsUsedInObtainingControlOfSubsidiariesOrOtherBusinessesClassifiedAsInvestingActivities","CashFlowsFromUsedInInvestingActivities","InterestPaidClassifiedAsOperatingActivities","IncomeTaxesPaidRefundClassifiedAsOperatingActivities","DividendsPaid","DividendsPaidClassifiedAsFinancingActivities","PurchaseOfTreasuryShares","PaymentsOfLeaseLiabilitiesClassifiedAsFinancingActivities","ProceedsFromBorrowingsClassifiedAsFinancingActivities","RepaymentsOfBorrowingsClassifiedAsFinancingActivities","InterestExpenseOnBorrowings"]
stock = ["Assets","Equity","EquityAttributableToOwnersOfParent","Borrowings","LongtermBorrowings","CurrentBorrowingsAndCurrentPortionOfNoncurrentBorrowings","CashAndCashEquivalents","ContractAssets","LegalProceedingsProvision","OnerousContractsProvision"]
def series(k, isflow):
    out = {}
    if k not in d: return out
    for u, vals in d[k]['units'].items():
        if u != 'BRL': continue
        for x in vals:
            if not x.get('form','').startswith('20-F'): continue
            if isflow:
                if 'start' not in x: continue
                s, e = x['start'], x['end']
                if not (s[5:] == '01-01' and e[5:] == '12-31' and s[:4] == e[:4]): continue
            else:
                if x['end'][5:] != '12-31': continue
            key = x['end'][:4]
            # keep latest filed
            if key not in out or x['filed'] > out[key][1]:
                out[key] = (x['val'], x['filed'], x['accn'])
    return out
years = [str(y) for y in range(2013, 2026)]
for group, isflow in ((flow, True), (stock, False)):
    print("concept".ljust(48) + "".join(y.rjust(9) for y in years))
    for k in group:
        s = series(k, isflow)
        print(k[:47].ljust(48) + "".join((f"{s[y][0]/1e6:9.0f}" if y in s else "        .") for y in years))
