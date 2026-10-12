"""Rival margins from SEC companyfacts (10-K annual values), for the competitors the AMBQ 10-K names."""
import sys
sys.path.insert(0, 'tools')
import sources as s
TAGS = {
 'rev': ['RevenueFromContractWithCustomerExcludingAssessedTax', 'Revenues', 'SalesRevenueNet'],
 'gp': ['GrossProfit'],
 'oi': ['OperatingIncomeLoss'],
}
def series(facts, tags):
    out = {}
    for t in tags:
        u = facts['facts'].get('us-gaap', {}).get(t, {}).get('units', {}).get('USD', [])
        for x in u:
            if x.get('form') == '10-K' and x.get('fp') == 'FY' and 'frame' in x and len(x['frame']) == 6:
                out.setdefault(int(x['frame'][2:]), x['val'])
    return out
for tk in sys.argv[1:]:
    cik = s.cik_for(tk)[0]
    f = s.sec_facts(cik)
    r, g, o = (series(f, TAGS[k]) for k in ('rev', 'gp', 'oi'))
    print(tk, cik)
    for y in sorted(r):
        if y < 2016: continue
        gm = f"{g[y]/r[y]*100:.1f}%" if y in g else 'n/a'
        om = f"{o[y]/r[y]*100:.1f}%" if y in o else 'n/a'
        print(f"  CY{y} revenue {r[y]/1e6:,.0f}M gross {gm} operating {om}")
