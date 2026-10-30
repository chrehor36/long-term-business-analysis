"""Annual series from Boeing's XBRL company facts (transcription only; FY values as filed in 10-Ks).
Usage: python -I series.py   (reads cache/companyfacts.json, writes series_out.json)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'cache', 'companyfacts.json')))
g = d['facts']['us-gaap']


def annual(tag):
    out = {}
    if tag not in g:
        return out
    for unit, rows in g[tag]['units'].items():
        for r in rows:
            if r.get('form') == '10-K' and r.get('fp') == 'FY' and 'frame' in r and len(r['frame']) == 6:
                out[int(r['frame'][2:])] = r['val'] / 1e6
    return out


tags = {
    'OCF': 'NetCashProvidedByUsedInOperatingActivities',
    'SBC': 'ShareBasedCompensation',
    'k401_shares': 'StockIssuedDuringPeriodValueEmployeeBenefitPlan',
    'capex': 'PaymentsToAcquirePropertyPlantAndEquipment',
    'DA': 'DepreciationDepletionAndAmortization',
    'revenue': 'Revenues',
    'net_income': 'NetIncomeLoss',
    'buybacks': 'PaymentsForRepurchaseOfCommonStock',
    'dividends': 'PaymentsOfDividendsCommonStock',
}
S = {k: annual(v) for k, v in tags.items()}
print('FY   ' + ' '.join(f'{k:>12}' for k in tags))
for y in range(2014, 2026):
    print(y, ' '.join(f"{S[k].get(y, float('nan')):12.0f}" for k in tags))
json.dump({k: {str(y): v for y, v in S[k].items()} for k in S},
          open(os.path.join(HERE, 'series_out.json'), 'w'), indent=1)
