import json, sys
sys.path.insert(0, '.')
from fetch import get
def annual(g, tag):
    out = {}; acc = {}
    if tag not in g: return out, acc
    for f in g[tag]['units'].get('USD', []):
        if f.get('form') == '10-K' and 'frame' in f:
            fr = f['frame']
            if (len(fr) == 6) or (fr.endswith('Q4I')):
                y = f['end'][:4]; out[y] = f['val']; acc[y] = f['accn']
    return out, acc
for name, cik in [('IDACORP', '0001057877'), ('Avista', '0000104918'), ('NorthWestern Energy Group', '0001993004'), ('NorthWestern Corp', '0000073088'), ('PacifiCorp', '0000075594')]:
    j = json.loads(get("https://data.sec.gov/api/xbrl/companyfacts/CIK%s.json" % cik))
    g = j['facts'].get('us-gaap', {})
    print('==', name, cik)
    yrs = [str(y) for y in range(2015, 2026)]
    for t in ['NetIncomeLoss', 'ProfitLoss', 'StockholdersEquity', 'StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest', 'NetCashProvidedByUsedInOperatingActivities', 'PaymentsToAcquirePropertyPlantAndEquipment', 'PaymentsToAcquireProductiveAssets', 'Revenues', 'RegulatedAndUnregulatedOperatingRevenue', 'ElectricUtilityRevenue']:
        a, acc = annual(g, t)
        if not a: continue
        print(t[:40].ljust(41), ' '.join(('%8.1f' % (a[y]/1e6)) if y in a else '       -' for y in yrs))
    print(' '*41, ' '.join(y.rjust(8) for y in yrs))
    lastacc = sorted(set(acc.values()))[-3:] if acc else []
    print('  accessions (latest):', lastacc)
