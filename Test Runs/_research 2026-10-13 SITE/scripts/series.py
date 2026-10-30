"""Annual series from XBRL company facts (transcription only; first-filed 10-K value for each fiscal year end)."""
import json, sys
from datetime import date
d = json.load(open(sys.argv[1]))
g = d['facts']['us-gaap']
def annual(tag, instant=False):
    out = {}
    if tag not in g: return out
    for unit, facts in g[tag]['units'].items():
        for f in facts:
            if f.get('form') not in ('10-K',): continue
            end = f['end']
            if not instant:
                if 'start' not in f: continue
                days = (date.fromisoformat(end) - date.fromisoformat(f['start'])).days
                if days < 350 or days > 380: continue
            key = end
            # first-filed vintage
            if key not in out or f['filed'] < out[key][1]:
                out[key] = (f['val'], f['filed'], f['accn'])
    return out
flow = ['RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','Revenues','GrossProfit','OperatingIncomeLoss','NetIncomeLoss','IncomeTaxExpenseBenefit','InterestExpense','InterestPaidNet','IncomeTaxesPaidNet',
        'NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','ProceedsFromSaleOfPropertyPlantAndEquipment','PaymentsToAcquireBusinessesNetOfCashAcquired','PaymentsToAcquireIntangibleAssets',
        'ShareBasedCompensation','Depreciation','AmortizationOfIntangibleAssets','DepreciationDepletionAndAmortization','DepreciationAmortizationAndAccretionNet','FinanceLeasePrincipalPayments','RepaymentsOfLongTermCapitalLeaseObligations',
        'RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability','PaymentsForRepurchaseOfCommonStock','IncreaseDecreaseInInventories','IncreaseDecreaseInAccountsReceivable','IncreaseDecreaseInAccountsPayable','FinanceLeaseRightOfUseAssetAmortization']
inst = ['Goodwill','IntangibleAssetsNetExcludingGoodwill','InventoryNet','AccountsReceivableNetCurrent','AccountsPayableCurrent','CashAndCashEquivalentsAtCarryingValue','StockholdersEquity','Assets','LongTermDebtNoncurrent','LongTermDebtCurrent','FinanceLeaseLiability','FinanceLeaseLiabilityCurrent','FinanceLeaseLiabilityNoncurrent','OperatingLeaseLiability','CapitalLeaseObligations','PropertyPlantAndEquipmentNet','PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization','TreasuryStockCommonShares','CommonStockSharesOutstanding']
for t in flow:
    s = annual(t)
    if s: print('F', t, ' '.join(f"{k}:{v[0]/1e6:.1f}" for k, v in sorted(s.items())))
for t in inst:
    s = annual(t, instant=True)
    if s: print('I', t, ' '.join(f"{k}:{v[0]/1e6:.1f}" for k, v in sorted(s.items())))
