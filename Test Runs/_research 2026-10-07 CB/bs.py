import json
f=json.load(open('cache/facts.json'))
g=f['facts']['us-gaap']
def inst(tag):
    out={}
    if tag not in g: return out
    for u,vals in g[tag]['units'].items():
        for v in vals:
            if v.get('form') in ('10-K',) and v['end'][5:]=='12-31' and 'start' not in v:
                y=int(v['end'][:4])
                # latest filed value for that date
                if y not in out or v['filed']>out[y][1]: out[y]=(v['val'],v['filed'])
    return {k:v[0] for k,v in out.items()}
def dur(tag):
    out={}
    if tag not in g: return out
    for u,vals in g[tag]['units'].items():
        for v in vals:
            if v.get('form')=='10-K' and 'start' in v and v['end'][5:]=='12-31' and v['start'][5:]=='01-01':
                y=int(v['end'][:4])
                if y not in out or v['filed']>out[y][1]: out[y]=(v['val'],v['filed'])
    return {k:v[0] for k,v in out.items()}
tags_i=['Assets','Investments','CashAndCashEquivalentsAtCarryingValue','LiabilityForClaimsAndClaimsAdjustmentExpense','UnearnedPremiums','ReinsuranceRecoverablesOnUnpaidLossesGross','ReinsuranceRecoverables','PrepaidReinsurancePremiums','PremiumsReceivableAtCarryingValue','DeferredPolicyAcquisitionCosts','LiabilityForFuturePolicyBenefits','PolicyholderFunds','ShortTermBorrowings','LongTermDebt','Liabilities','StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest','Goodwill','IntangibleAssetsNetExcludingGoodwill','AccumulatedOtherComprehensiveIncomeLossNetOfTax','RetainedEarningsAccumulatedDeficit','TreasuryStockValue','DeferredTaxLiabilities']
tags_d=['PremiumsEarnedNet','NetInvestmentIncome','NetIncomeLoss','IncomeTaxExpenseBenefit','PaymentsForRepurchaseOfCommonStock','PaymentsOfDividendsCommonStock','PaymentsToAcquireBusinessesNetOfCashAcquired','TreasuryStockValueAcquiredCostMethod']
yrs=range(2014,2026)
print('tag'.ljust(60),' '.join(str(y).rjust(8) for y in yrs))
for t in tags_i:
    d=inst(t); print(t[:60].ljust(60),' '.join((f"{d[y]/1e6:8.0f}" if y in d else '       -') for y in yrs))
for t in tags_d:
    d=dur(t); print(t[:60].ljust(60),' '.join((f"{d[y]/1e6:8.0f}" if y in d else '       -') for y in yrs))
