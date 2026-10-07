import sys, os, json
sys.path.insert(0, 'tools')
import sources

D = 'Test Runs/_research 2026-09-19 OTTR/peers'

PEERS = {
    'WLK': '0001262823', 'ATKR': '0001666138', 'WMS': '0001604028',
    'NWPX': '0001001385', 'OLN': '0000074303',
    'ALE': '0000066756', 'MGEE': '0001161728', 'NWE': '0001993004',
    'BKH': '0001130464', 'AVA': '0000104918', 'XEL': '0000072903',
    'IDA': '0001057877',
}

TAGS = ['Revenues', 'RevenueFromContractWithCustomerExcludingAssessedTax',
        'OperatingIncomeLoss', 'NetIncomeLoss', 'StockholdersEquity', 'Assets',
        'NetCashProvidedByUsedInOperatingActivities',
        'PaymentsToAcquirePropertyPlantAndEquipment',
        'PaymentsToAcquireProductiveAssets', 'DepreciationDepletionAndAmortization']


def annual(us, tag, fy_end=None):
    if tag not in us:
        return {}
    out = {}
    for unit, items in us[tag]['units'].items():
        for it in items:
            if it.get('form') not in ('10-K', '10-K/A'):
                continue
            if 'start' in it:
                s, e = it['start'], it['end']
                # ~full year
                from datetime import date
                sy, sm, sd = map(int, s.split('-'))
                ey, em, ed = map(int, e.split('-'))
                days = (date(ey, em, ed) - date(sy, sm, sd)).days
                if not (330 < days < 400):
                    continue
                y = it.get('fy') or ey
                y = ey if em >= 6 else ey - 1
            else:
                continue
            prev = out.get(y)
            if prev is None or it['filed'] > prev[1]:
                out[y] = (it['val'], it['filed'])
    return {k: v[0] for k, v in sorted(out.items())}


res = {}
for t, cik in PEERS.items():
    p = os.path.join(D, t + '_cf.json')
    if not os.path.exists(p):
        raw = sources._get('https://data.sec.gov/api/xbrl/companyfacts/CIK%s.json' % cik.zfill(10),
                           headers=sources.SEC_UA)
        open(p, 'wb').write(raw if isinstance(raw, bytes) else raw.encode())
    cf = json.load(open(p))
    us = cf['facts'].get('us-gaap', {})
    d = {}
    for tag in TAGS:
        a = annual(us, tag)
        if a:
            d[tag] = {k: v for k, v in a.items() if k >= 2019}
    res[t] = d
    rev = d.get('Revenues') or d.get('RevenueFromContractWithCustomerExcludingAssessedTax') or {}
    op = d.get('OperatingIncomeLoss', {})
    print(t, cf['entityName'])
    for y in sorted(set(rev) | set(op)):
        r, o = rev.get(y), op.get(y)
        m = ('%.1f%%' % (100.0 * o / r)) if (r and o is not None) else '-'
        print('   %d rev=%s op=%s margin=%s' % (y, ('%.0f' % (r / 1e6)) if r else '-',
                                                ('%.0f' % (o / 1e6)) if o is not None else '-', m))

json.dump(res, open(D + '/peer_series.json', 'w'), indent=1)
