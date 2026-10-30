# peer annual revenue and operating income from SEC companyfacts (10-K, FY, full-year frames), transcription only
import json, urllib.request, gzip, os, sys
UA = {'User-Agent': 'Chris Hrehor chrehor36@gmail.com', 'Accept-Encoding': 'gzip'}
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache', 'peers')
peers = {'FAST': 815556, 'MSM': 1003078, 'GWW': 277135}
def get(cik):
    p = os.path.join(D, '%d.json' % cik)
    if not os.path.exists(p):
        b = urllib.request.urlopen(urllib.request.Request('https://data.sec.gov/api/xbrl/companyfacts/CIK%010d.json' % cik, headers=UA), timeout=60).read()
        if b[:2] == b'\x1f\x8b': b = gzip.decompress(b)
        open(p, 'wb').write(b)
    return json.load(open(p))
def series(facts, tags):
    out = {}
    for tag in tags:
        u = facts['facts'].get('us-gaap', {}).get(tag, {}).get('units', {}).get('USD', [])
        for x in u:
            if x.get('form') != '10-K' or 'frame' not in x: continue
            fr = x['frame']
            if len(fr) == 6 and fr.startswith('CY'):
                y = int(fr[2:]); out.setdefault(y, (x['val'], x['accn'], tag))
    return out
for t, cik in peers.items():
    f = get(cik)
    rev = series(f, ['Revenues', 'RevenueFromContractWithCustomerExcludingAssessedTax', 'SalesRevenueNet', 'SalesRevenueGoodsNet'])
    oi = series(f, ['OperatingIncomeLoss'])
    print(t, f['entityName'])
    for y in range(2015, 2026):
        if y in rev and y in oi:
            print('  %d  rev %10.1f  opinc %9.1f  margin %5.1f%%  %s' % (y, rev[y][0]/1e6, oi[y][0]/1e6, 100*oi[y][0]/rev[y][0], oi[y][1]))
