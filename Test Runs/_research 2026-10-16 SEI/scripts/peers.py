import json, sys
from datetime import date
def series(d, tag, dur=True):
    out = {}
    for ns in ('us-gaap',):
        if tag not in d['facts'].get(ns, {}): continue
        for f in d['facts'][ns][tag]['units'].get('USD', []):
            if f.get('form') not in ('10-K', '10-K/A'): continue
            if dur:
                if 'start' not in f: continue
                if (date.fromisoformat(f['end']) - date.fromisoformat(f['start'])).days < 350: continue
            out.setdefault(f['end'], f['val'])
    return out
for t in sys.argv[1:]:
    d = json.load(open(f'cache/peers/{t}_companyfacts.json'))
    oi = series(d, 'OperatingIncomeLoss')
    rev = series(d, 'Revenues') or {}
    rev2 = series(d, 'RevenueFromContractWithCustomerExcludingAssessedTax')
    A = series(d, 'Assets', False); G = series(d, 'Goodwill', False)
    I = series(d, 'IntangibleAssetsNetExcludingGoodwill', False)
    print('==', t)
    for y in sorted(oi):
        if y < '2016': continue
        a = A.get(y); g = G.get(y, 0) or 0; i = I.get(y, 0) or 0
        r = rev.get(y) or rev2.get(y)
        ta = (a - g - i) if a else None
        print(y, 'rev', r and round(r/1e6), 'OI', round(oi[y]/1e6,1), 'TA', ta and round(ta/1e6), 'OI/TA', ta and f'{oi[y]/ta*100:.1f}%', 'OI/rev', r and f'{oi[y]/r*100:.1f}%')
