"""Ten-year table from SEC companyfacts, latest-filed value per FY end (40-F only). Transcription, checked against filings."""
import json, sys, os
d = json.load(open(sys.argv[1]))
g = d['facts']['us-gaap']
tags = ['Revenues','OperatingIncomeLoss','DepreciationDepletionAndAmortization','InterestExpenseNonoperating','IncomeTaxExpenseBenefit','ProfitLoss',
 'NetIncomeLossAttributableToNoncontrollingInterest','PreferredStockDividendsAndOtherAdjustments','NetIncomeLossAvailableToCommonStockholdersBasic',
 'PublicUtilitiesAllowanceForFundsUsedDuringConstructionCapitalizedCostOfEquity','DeferredIncomeTaxExpenseBenefit','IncreaseDecreaseInOperatingCapital',
 'NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireIntangibleAssets','ProceedsFromContributionInAidOfConstruction',
 'PaymentsForProceedsFromOtherInvestingActivities','ProceedsFromDivestitureOfBusinessesNetOfCashDivested','NetCashProvidedByUsedInInvestingActivities',
 'ProceedsFromIssuanceOfLongTermDebt','RepaymentsOfLongTermDebtAndCapitalSecurities','ProceedsFromLinesOfCredit','RepaymentsOfLinesOfCredit','ProceedsFromRepaymentsOfShortTermDebtMaturingInThreeMonthsOrLess',
 'ProceedsFromIssuanceOfCommonStock','PaymentsOfDividendsCommonStock','PaymentsOfDividendsPreferredStockAndPreferenceStock','PaymentsOfDividendsMinorityInterest',
 'DividendsCommonStock','InterestPaidNet','IncomeTaxesPaidNet',
 'CashAndCashEquivalentsAtCarryingValue','AccountsReceivableNetCurrent','PublicUtilitiesInventory','RegulatoryAssets','PublicUtilitiesPropertyPlantAndEquipmentNet','Goodwill','IntangibleAssetsNetExcludingGoodwill','Assets',
 'ShortTermBorrowings','LongTermDebtCurrent','LongTermDebtNoncurrent','FinanceLeaseLiability','DeferredIncomeTaxLiabilitiesNet','RegulatoryLiabilities',
 'CommonStockValue','PreferredStockValue','RetainedEarningsAccumulatedDeficit','AccumulatedOtherComprehensiveIncomeLossNetOfTax','StockholdersEquity','MinorityInterest',
 'CommonStockSharesOutstanding','WeightedAverageNumberOfSharesOutstandingBasic','CommonStockDividendsPerShareDeclared','EarningsPerShareBasic']
years = [f"{y}-12-31" for y in range(2016, 2026)]
out = {}
for t in tags:
    if t not in g: continue
    for unit, rows in g[t]['units'].items():
        best = {}
        for x in rows:
            if x.get('form') not in ('40-F','40-F/A'): continue
            if x['end'] not in years: continue
            if 'start' in x:
                # annual durations only
                from datetime import date
                s = date.fromisoformat(x['start']); e = date.fromisoformat(x['end'])
                if not 340 <= (e - s).days <= 380: continue
            k = x['end']
            if k not in best or x['filed'] > best[k][1]: best[k] = (x['val'], x['filed'])
        out[t] = {k: v[0] for k, v in best.items()}
def f(v, t):
    if v is None: return '-'
    if 'PerShare' in t: return f"{v:.2f}"
    if 'Shares' in t: return f"{v/1e6:.1f}"
    return f"{v/1e6:,.0f}"
print("tag | " + " | ".join(y[:4] for y in years))
for t in tags:
    if t not in out: print(t, "| MISSING"); continue
    print(t + " | " + " | ".join(f(out[t].get(y), t) for y in years))
json.dump(out, open(sys.argv[2], 'w'), indent=1)
