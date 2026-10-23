"""Ten-year table from SEC companyfacts (ifrs-full), KRW millions. Arithmetic only.
For each fiscal year take the value as reported in the latest 20-F that reports that period."""
import json, sys
d = json.load(open(sys.argv[1]))['facts']['ifrs-full']
def series(tag, dur=True):
    out = {}
    if tag not in d: return out
    for u, rows in d[tag]['units'].items():
        for r in rows:
            if r.get('form') not in ('20-F', '20-F/A'): continue
            end = r['end']
            if dur:
                if 'start' not in r: continue
                from datetime import date
                s = date.fromisoformat(r['start']); e = date.fromisoformat(end)
                if not (350 <= (e - s).days <= 380): continue
            else:
                if 'start' in r: continue
            if not end.endswith('12-31'): continue
            y = int(end[:4])
            # latest filing wins
            if y not in out or r['filed'] > out[y][1]:
                out[y] = (r['val'], r['filed'], r['accn'])
    return out
tags_d = ['Revenue','ProfitLossFromOperatingActivities','ProfitLossBeforeTax','IncomeTaxExpenseContinuingOperations','ProfitLoss',
 'ProfitLossAttributableToOwnersOfParent','CashFlowsFromUsedInOperatingActivities','PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities',
 'PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities','ProceedsFromSalesOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities',
 'DepreciationAndAmortisationExpense','DepreciationExpense','AdjustmentsForDepreciationExpense','InterestExpense','InterestPaidClassifiedAsOperatingActivities',
 'IncomeTaxesPaidRefundClassifiedAsOperatingActivities','DividendsPaidClassifiedAsFinancingActivities','DividendsPaid',
 'CashFlowsUsedInObtainingControlOfSubsidiariesOrOtherBusinessesClassifiedAsInvestingActivities','InterestReceivedClassifiedAsOperatingActivities',
 'DividendsReceivedClassifiedAsOperatingActivities','ShareOfProfitLossOfAssociatesAndJointVenturesAccountedForUsingEquityMethod','RevenueFromSaleOfElectricity']
tags_i = ['Assets','CurrentAssets','CashAndCashEquivalents','PropertyPlantAndEquipment','IntangibleAssetsOtherThanGoodwill','Liabilities','CurrentLiabilities',
 'Borrowings','ShorttermBorrowings','CurrentBorrowingsAndCurrentPortionOfNoncurrentBorrowings','LongtermBorrowings','LeaseLiabilities',
 'Equity','EquityAttributableToOwnersOfParent','NoncontrollingInterests','InvestmentAccountedForUsingEquityMethod','ShorttermDepositsNotClassifiedAsCashEquivalents',
 'CurrentFinancialAssetsAtFairValueThroughProfitOrLoss','CurrentFinancialAssetsAtAmortisedCost','DeferredTaxAssets','DeferredTaxLiabilities']
years = range(2014, 2026)
def show(tags, dur):
    for t in tags:
        s = series(t, dur)
        if not s: print(f'{t[:60]:60s} (none)'); continue
        print(f'{t[:60]:60s}' + ''.join(f'{(s[y][0]/1e9 if y in s else float("nan")):>10.0f}' for y in years))
print('KRW billions'.ljust(60) + ''.join(f'{y:>10d}' for y in years))
show(tags_d, True); print(); show(tags_i, False)
