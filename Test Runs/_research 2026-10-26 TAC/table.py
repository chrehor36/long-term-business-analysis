# ten-year table from XBRL company facts (transcription only; cross-checked against filed statements in the run)
import json, sys
d = json.load(open(sys.argv[1]))['facts']['ifrs-full']
tags = ['Revenue','ProfitLossFromOperatingActivities','ProfitLossBeforeTax','IncomeTaxExpenseContinuingOperations','ProfitLoss',
 'ProfitLossAttributableToNoncontrollingInterests','ProfitLossAttributableToOrdinaryEquityHoldersOfParentEntity',
 'DepreciationAndAmortisationExpense','AdjustmentsForImpairmentLossReversalOfImpairmentLossRecognisedInProfitOrLoss',
 'CashFlowsFromUsedInOperatingActivities','PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities',
 'PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities','CashFlowsUsedInObtainingControlOfSubsidiariesOrOtherBusinessesClassifiedAsInvestingActivities',
 'InterestPaidClassifiedAsOperatingActivities','IncomeTaxesPaidRefund','DividendsPaid','DividendsPaidToNoncontrollingInterestsClassifiedAsFinancingActivities',
 'PaymentsOfLeaseLiabilitiesClassifiedAsFinancingActivities','PaymentsToAcquireOrRedeemEntitysShares','IncreaseDecreaseThroughSharebasedPaymentTransactions',
 'Assets','PropertyPlantAndEquipment','Goodwill','IntangibleAssetsOtherThanGoodwill','CashAndCashEquivalents','Borrowings','LongtermBorrowings',
 'CurrentBorrowingsAndCurrentPortionOfNoncurrentBorrowings','OtherProvisions','Equity','NoncontrollingInterests','IssuedCapitalPreferenceShares',
 'IssuedCapitalOrdinaryShares','WeightedAverageShares','TradeAndOtherCurrentReceivables','Inventories','RetainedEarnings']
years = range(2014, 2026)
print('tag'.ljust(44) + ''.join(str(y).rjust(8) for y in years))
for t in tags:
    if t not in d: print(t, 'n/a'); continue
    arr = list(d[t]['units'].values())[0]
    row = {}
    for x in sorted(arr, key=lambda x: x['filed']):
        if x.get('form') not in ('40-F', '40-F/A'): continue
        e = x['end']
        if not e.endswith('12-31'): continue
        if 'start' in x and not x['start'].endswith('01-01'): continue
        if 'start' in x and x['start'][:4] != e[:4]: continue
        row[int(e[:4])] = x['val']
    def fm(v):
        return ('%.0f' % (v/1e6)) if abs(v) > 1e4 else ('%.1f' % v)
    print(t[:44].ljust(44) + ''.join((fm(row[y]) if y in row else '-').rjust(8) for y in years))
