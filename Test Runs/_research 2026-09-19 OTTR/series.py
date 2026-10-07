import json, collections

D = 'Test Runs/_research 2026-09-19 OTTR'
cf = json.load(open(D + '/companyfacts.json'))
us = cf['facts']['us-gaap']

TAGS = [
    'NetCashProvidedByUsedInOperatingActivities',
    'PaymentsToAcquirePropertyPlantAndEquipment',
    'PaymentsToAcquireProductiveAssets',
    'DepreciationDepletionAndAmortization',
    'DepreciationAmortizationAndAccretionNet',
    'ShareBasedCompensation',
    'NetIncomeLoss',
    'StockholdersEquity',
    'Assets',
    'Liabilities',
    'LongTermDebtNoncurrent',
    'PaymentsOfDividendsCommonStock',
    'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest',
    'IncomeTaxesPaidNet',
    'IncomeTaxesPaid',
    'Revenues',
    'CashAndCashEquivalentsAtCarryingValue',
    'ProceedsFromIssuanceOfCommonStock',
    'PaymentsForRepurchaseOfCommonStock',
]


def annual(tag):
    if tag not in us:
        return {}
    out = {}
    for unit, items in us[tag]['units'].items():
        for it in items:
            if it.get('form') not in ('10-K', '10-K/A'):
                continue
            fp = it.get('fp')
            if 'start' in it:
                s, e = it['start'], it['end']
                # full year only
                if not (e[5:] in ('12-31',) and s[5:] == '01-01'):
                    continue
                y = int(e[:4])
            else:
                if it['end'][5:] != '12-31':
                    continue
                y = int(it['end'][:4])
            # latest filing wins
            key = y
            prev = out.get(key)
            if prev is None or it['filed'] > prev[1]:
                out[key] = (it['val'], it['filed'])
    return {k: v[0] for k, v in sorted(out.items())}


res = {}
for t in TAGS:
    a = annual(t)
    if a:
        res[t] = a
        print(t)
        print('  ', ' '.join('%d=%.1f' % (y, v / 1e3) for y, v in a.items()))

json.dump(res, open(D + '/annual_series.json', 'w'), indent=1)
