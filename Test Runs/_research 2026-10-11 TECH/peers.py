import json, sys
sys.path.insert(0, '.')
from facts import load, annual
def ser(f, tags):
    out = {}
    for t in tags:
        for k, v in annual(f, t).items():
            out.setdefault(k[:4] if k[5:7] in ('12','06') else k[:7], (v[0], v[1], t))
    return out
def inst(f, tags):
    # balance sheet, instant values from 10-K, first filed
    out = {}
    for t in tags:
        try: rows = f['us-gaap'][t]['units']['USD']
        except KeyError: continue
        for r in sorted(rows, key=lambda r: r['filed']):
            if r.get('form') != '10-K' or 'start' in r: continue
            out.setdefault(r['end'][:4], r['val'])
    return out
for tk in sys.argv[1:]:
    f = load(f'cache/facts_{tk}.json')
    rev = ser(f, ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet'])
    oi = ser(f, ['OperatingIncomeLoss'])
    am = ser(f, ['AmortizationOfIntangibleAssets'])
    ta = inst(f, ['Assets']); gw = inst(f, ['Goodwill']); ia = inst(f, ['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'])
    cash = inst(f, ['CashAndCashEquivalentsAtCarryingValue'])
    print(tk)
    print(' year   rev    OI   OI%  OI+amort%  (OI+amort)/tangible-assets-ex-cash')
    for y in sorted(rev):
        if y < '2015' or y not in oi: continue
        r = rev[y][0]/1e6; o = oi[y][0]/1e6; a = am.get(y, (0,))[0]/1e6
        tang = None
        if y in ta and y in gw:
            tang = (ta[y] - gw.get(y,0) - ia.get(y,0) - cash.get(y,0))/1e6
        rt = f'{(o+a)/tang*100:6.1f}%' if tang else '   n/a'
        print(f' {y} {r:8.0f} {o:7.0f} {o/r*100:5.1f}% {(o+a)/r*100:6.1f}%  {rt}')
