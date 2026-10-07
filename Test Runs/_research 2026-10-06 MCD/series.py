"""Annual series from SEC companyfacts (10-K, FY, full-year duration), latest-filed value per fiscal year.
Transcription only: each figure is checked against the filed statement where the run cites it.
Usage: python series.py <companyfacts.json>"""
import json, sys
d = json.load(open(sys.argv[1]))
g = d['facts']['us-gaap']
TAGS = {
    'OCF': ['NetCashProvidedByUsedInOperatingActivities'],
    'SBC': ['ShareBasedCompensation'],
    'CAPEX': ['PaymentsToAcquirePropertyPlantAndEquipment'],
    'DA': ['DepreciationDepletionAndAmortization', 'DepreciationAndAmortization'],
    'NI': ['NetIncomeLoss'],
    'REV': ['Revenues'],
    'OPINC': ['OperatingIncomeLoss'],
    'BUYBK': ['PaymentsForRepurchaseOfCommonStock'],
    'DIV': ['PaymentsOfDividendsCommonStock', 'PaymentsOfDividends'],
    'ACQREST': ['PaymentsToAcquireOtherProductiveAssets'],
    'INT': ['InterestExpense', 'InterestExpenseNonoperating'],
}
def annual(tag):
    out = {}
    if tag not in g:
        return out
    for unit, rows in g[tag]['units'].items():
        for r in rows:
            if r.get('form') != '10-K' or r.get('fp') != 'FY':
                continue
            if 'start' in r:
                from datetime import date
                s = date.fromisoformat(r['start']); e = date.fromisoformat(r['end'])
                if not (350 <= (e - s).days <= 380):
                    continue
            y = int(r['end'][:4])
            if y not in out or r['filed'] > out[y][1]:
                out[y] = (r['val'], r['filed'])
    return out
series = {}
for k, tags in TAGS.items():
    m = {}
    for t in tags:
        for y, v in annual(t).items():
            m.setdefault(y, v)
    series[k] = m
years = list(range(2014, 2026))
print('year ' + ' '.join(f'{k:>8}' for k in TAGS))
for y in years:
    print(f'{y} ' + ' '.join(f"{(series[k][y][0] / 1e6 if y in series[k] else float('nan')):8.0f}" for k in TAGS))
print()
print('owner cash, all capex = OCF - SBC - CAPEX ; depreciation variant = OCF - SBC - DA ; restaurant-purchase variant also less ACQREST')
for y in years:
    try:
        o, s, c, da = (series[k][y][0] / 1e6 for k in ('OCF', 'SBC', 'CAPEX', 'DA'))
        a = series['ACQREST'][y][0] / 1e6 if y in series['ACQREST'] else 0.0
        print(y, round(o - s - c), round(o - s - da), round(o - s - c - a))
    except KeyError as e:
        print(y, 'missing', e)
