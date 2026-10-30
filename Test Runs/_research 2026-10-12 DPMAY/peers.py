# operating margin by fiscal year from SEC companyfacts (annual 10-K values): python peers.py <json> ...
import json, sys
def series(f, tags):
    g = f['facts'].get('us-gaap', {})
    out = {}
    for t in tags:
        if t not in g: continue
        for u in g[t]['units'].get('USD', []):
            if u.get('form') == '10-K' and u.get('fp') == 'FY' and u.get('frame', '').startswith('CY') and len(u['frame']) == 6:
                out.setdefault(int(u['frame'][2:]), (u['val'], u['accn']))
    return out
for p in sys.argv[1:]:
    f = json.load(open(p))
    rev = series(f, ['Revenues', 'RevenueFromContractWithCustomerExcludingAssessedTax', 'SalesRevenueNet', 'SalesRevenueGoodsNet'])
    op = series(f, ['OperatingIncomeLoss'])
    print('==', f['entityName'])
    for y in sorted(set(rev) & set(op)):
        if y >= 2014:
            print(y, 'rev %.0f' % (rev[y][0]/1e6), 'op %.0f' % (op[y][0]/1e6), 'margin %.1f%%' % (100*op[y][0]/rev[y][0]), op[y][1])
