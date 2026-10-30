# rivals' ten-year figures from XBRL companyfacts (us-gaap), transcription only
import json, sys
def series(f, tag):
    if tag not in f: return {}
    out = {}
    for u in f[tag]['units'].values():
        for x in sorted(u, key=lambda x: x['filed']):
            if x.get('form') != '10-K': continue
            e = x['end']
            if 'start' in x:
                if int(e[5:7]) != 12 or x['start'][5:10] != '01-01' or x['start'][:4] != e[:4]: continue
            elif e[5:] != '12-31': continue
            out[int(e[:4])] = x['val']
    return out
for fn in sys.argv[1:]:
    d = json.load(open(fn)); f = d['facts']['us-gaap']
    print('==', d['entityName'])
    for t in ['OperatingIncomeLoss','NetIncomeLoss','StockholdersEquity','LongTermDebtNoncurrent','LongTermDebt','Assets','Revenues','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment']:
        s = series(f, t)
        print(t[:36].ljust(37) + ' '.join(('%7.0f' % (s[y]/1e6)) if y in s else '      -' for y in range(2016, 2026)))
