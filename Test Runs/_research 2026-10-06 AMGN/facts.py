"""Annual (10-K, FY) values of selected us-gaap tags from SEC companyfacts for Amgen (CIK 318154).
Transcription only; each value is the one reported for that fiscal year in the 10-K covering it (form 10-K, fp FY,
frame-less latest filing for that period end). Output: USD millions."""
import json, sys, urllib.request
UA = 'Long-Term Business Analysis research chrehor36@gmail.com'
cache = __file__.rsplit('/', 1)[0] + '/cache/companyfacts.json'
try:
    d = json.load(open(cache))
except FileNotFoundError:
    req = urllib.request.Request('https://data.sec.gov/api/xbrl/companyfacts/CIK0000318154.json', headers={'User-Agent': UA})
    d = json.load(urllib.request.urlopen(req))
    json.dump(d, open(cache, 'w'))
g = d['facts']['us-gaap']
tags = ['NetCashProvidedByUsedInOperatingActivities', 'ShareBasedCompensation', 'PaymentsToAcquirePropertyPlantAndEquipment',
        'DepreciationDepletionAndAmortization', 'PaymentsToAcquireBusinessesNetOfCashAcquired', 'Revenues',
        'ResearchAndDevelopmentExpense', 'NetIncomeLoss', 'PaymentsForRepurchaseOfCommonStock', 'PaymentsOfDividends',
        'IncomeTaxesPaidNet', 'InterestPaidNet']
for t in tags:
    if t not in g:
        print(t, 'not tagged'); continue
    out = {}
    for u, vals in g[t]['units'].items():
        for v in vals:
            if v.get('form') == '10-K' and v.get('fp') == 'FY' and v['end'][5:] == '12-31' and v['start'][5:] == '01-01':
                y = v['end'][:4]
                if y == v['fy'] or y not in out:  # value as reported in that year's own 10-K, else latest
                    out[y] = (v['val'] / 1e6, v['accn'])
    print(t)
    for y in sorted(out)[-7:]:
        print('  ', y, round(out[y][0]), out[y][1])
