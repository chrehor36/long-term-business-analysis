import json, sys
def series(path, tags):
    d = json.load(open(path))
    print(d['entityName'])
    g = d['facts']['us-gaap']
    res = {}
    for t in tags:
        if t not in g: continue
        for u in g[t]['units'].get('USD', []):
            if u.get('fp') == 'FY' and u.get('form') in ('10-K','10-K/A'):
                # keep annual duration facts only (approx 1 year)
                s, e = u.get('start'), u['end']
                if s is None: continue
                from datetime import date
                ds = date.fromisoformat(s); de = date.fromisoformat(e)
                if 350 <= (de-ds).days <= 380:
                    res.setdefault((t, e), (u['val'], u['accn']))
    return res
for path, tags in [(sys.argv[1], ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','OperatingIncomeLoss','NetIncomeLoss']),
                   (sys.argv[2], ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','OperatingIncomeLoss','NetIncomeLoss'])]:
    r = series(path, tags)
    byend = {}
    for (t,e),(v,a) in r.items():
        byend.setdefault(e, {})[t] = (v, a)
    for e in sorted(byend):
        if e < '2014-01-01': continue
        row = byend[e]
        rev = next((row[t][0] for t in ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet'] if t in row), None)
        oi = row.get('OperatingIncomeLoss', (None,None))[0]
        ni = row.get('NetIncomeLoss', (None,None))[0]
        acc = [row[t][1] for t in row][0]
        m = f"{oi/rev:.1%}" if (rev and oi is not None) else "-"
        print(e, rev, oi, ni, m, acc)
