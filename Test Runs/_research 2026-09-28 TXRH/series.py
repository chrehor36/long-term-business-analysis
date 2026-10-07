import json, datetime, sys
# Annual series from SEC companyfacts, keyed by fiscal-year END date (duration 350-380 days), latest filing wins.
d = json.load(open('cache/facts.json'))
g = d['facts']['us-gaap']
def D(s): return datetime.date.fromisoformat(s)
def ann(tag, unit='USD'):
    out = {}
    if tag not in g: return out
    for x in g[tag]['units'].get(unit, []):
        if 'start' not in x: continue
        dur = (D(x['end']) - D(x['start'])).days
        if 350 <= dur <= 380 and x.get('form', '').startswith('10-K'):
            k = x['end']
            if k not in out or x['filed'] > out[k][1]:
                out[k] = (x['val'], x['filed'])
    return {k: v[0] for k, v in sorted(out.items())}
def inst(tag, unit='USD'):
    out = {}
    if tag not in g: return out
    for x in g[tag]['units'].get(unit, []):
        if 'start' in x: continue
        if x.get('form', '').startswith('10-K'):
            k = x['end']
            if k not in out or x['filed'] > out[k][1]:
                out[k] = (x['val'], x['filed'])
    return {k: v[0] for k, v in sorted(out.items())}
TAGS = ['NetCashProvidedByUsedInOperatingActivities', 'ShareBasedCompensation', 'DepreciationDepletionAndAmortization',
        'AmortizationOfIntangibleAssets', 'PaymentsToAcquirePropertyPlantAndEquipment', 'PaymentsToAcquireBusinessesNetOfCashAcquired',
        'OperatingIncomeLoss', 'RevenueFromContractWithCustomerExcludingAssessedTax', 'Revenues', 'SalesRevenueNet',
        'NetIncomeLoss', 'ProfitLoss', 'PaymentsOfDividendsCommonStock', 'PaymentsForRepurchaseOfCommonStock', 'IncomeTaxesPaidNet',
        'ProceedsFromStockOptionsExercised', 'PaymentsRelatedToTaxWithholdingForShareBasedCompensation']
if __name__ == '__main__':
    for t in TAGS:
        a = ann(t)
        print(t)
        print('   ', {k[:10]: round(v / 1e6, 1) for k, v in a.items()})
    for t in ['StockholdersEquity', 'StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest', 'Assets', 'CashAndCashEquivalentsAtCarryingValue', 'LiabilitiesCurrent', 'Goodwill', 'LongTermDebt', 'LongTermDebtNoncurrent', 'OperatingLeaseRightOfUseAsset', 'OperatingLeaseLiabilityCurrent', 'ContractWithCustomerLiabilityCurrent']:
        a = inst(t)
        print(t, {k: round(v / 1e6, 1) for k, v in a.items() if k >= '2008'})
    a = inst('CommonStockSharesOutstanding', 'shares'); print('shares', {k: round(v / 1e6, 2) for k, v in a.items()})
