"""Pull annual flows for the Q7 computation from RPM XBRL (10-K, May FY). Transcription only."""
import json
from datetime import date
d = json.load(open('cache/facts.json'))['facts']['us-gaap']
def ann(t):
    out = {}
    if t not in d: return out
    for u, vals in d[t]['units'].items():
        for v in vals:
            if v.get('form') == '10-K' and 'start' in v and v['end'][5:7] == '05':
                s = date.fromisoformat(v['start']); e = date.fromisoformat(v['end'])
                if 350 < (e - s).days < 380: out.setdefault(int(v['end'][:4]), v['val'] / 1e6)
    return out
tags = ['InterestExpense','InterestPaidNet','IncomeTaxExpenseBenefit','IncomeTaxesPaidNet','EffectiveIncomeTaxRateContinuingOperations',
 'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','NetIncomeLoss',
 'Depreciation','DepreciationDepletionAndAmortization','AmortizationOfIntangibleAssets',
 'PaymentsToAcquireBusinessesNetOfCashAcquired','ProceedsFromDivestitureOfBusinesses','ProceedsFromSaleOfPropertyPlantAndEquipment',
 'ProceedsFromSaleOfProductiveAssets','ProceedsFromDivestitureOfBusinessesNetOfCashDivested',
 'PaymentsForRepurchaseOfCommonStock','PaymentsOfDividends','PaymentsOfDividendsCommonStock','FinanceLeasePrincipalPayments',
 'RevenueFromContractWithCustomerExcludingAssessedTax','InvestmentIncomeInterestAndDividend','InvestmentIncomeInterest']
for t in tags:
    a = ann(t)
    if a: print(f'{t:70s}', ' '.join(f'{y}:{a[y]:.1f}' for y in sorted(a) if y >= 2016))
