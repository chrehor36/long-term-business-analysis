import json, sys
def annual(g, tag, unit='USD'):
    out = {}
    if tag not in g: return out
    for f in g[tag]['units'].get(unit, []):
        if f.get('form') != '10-K': continue
        s = f.get('start'); e = f['end']
        if s:
            if not (s[5:] == '01-01' and e[5:] == '12-31' and s[:4] == e[:4]): continue
        else:
            if e[5:] != '12-31': continue
        out.setdefault(int(e[:4]), (f['val'], f['accn']))
    return out
for tk in sys.argv[1:]:
    p = f"Test Runs/_research 2026-10-27 XEL/cache/{tk}_facts.json" if tk != 'XEL' else "Test Runs/_research 2026-10-27 XEL/cache/companyfacts.json"
    d = json.load(open(p)); g = d['facts']['us-gaap']
    ni = annual(g, 'NetIncomeLossAvailableToCommonStockholdersBasic') or annual(g, 'NetIncomeLoss')
    if tk in ('XEL',): ni = annual(g,'NetIncomeLoss')
    eq = annual(g, 'StockholdersEquity')
    ocf = annual(g, 'NetCashProvidedByUsedInOperatingActivities')
    cap = annual(g, 'PaymentsToAcquireProductiveAssets') or annual(g,'PaymentsToAcquirePropertyPlantAndEquipment')
    for alt in ('PaymentsToAcquirePropertyPlantAndEquipment','PaymentsForCapitalImprovements','PaymentsToAcquireProductiveAssets'):
        a = annual(g, alt)
        for y,v in a.items(): cap.setdefault(y, v)
    rev = annual(g, 'Revenues')
    for alt in ('RegulatedAndUnregulatedOperatingRevenue','RevenueFromContractWithCustomerIncludingAssessedTax','RevenueFromContractWithCustomerExcludingAssessedTax'):
        for y,v in annual(g, alt).items(): rev.setdefault(y, v)
    da = annual(g, 'DepreciationDepletionAndAmortization')
    for alt in ('DepreciationAmortizationAndAccretionNet','DepreciationAndAmortization','UtilitiesOperatingExpenseDepreciationAndAmortization'):
        for y,v in annual(g, alt).items(): da.setdefault(y, v)
    iss = annual(g, 'ProceedsFromIssuanceOfCommonStock')
    sh = {}
    for f in g.get('CommonStockSharesOutstanding',{}).get('units',{}).get('shares',[]):
        if f.get('form')=='10-K' and f['end'][5:]=='12-31': sh.setdefault(int(f['end'][:4]), f['val'])
    print(f"== {tk}")
    print(" yr   rev    NI   avgEq  ROE%   OCF   capex  OCF-cap  D&A  OCF-D&A  issue  shares(M)")
    for y in range(2016, 2026):
        def v(dct): return dct.get(y,(None,))[0]
        r, n, e1, e0 = v(rev), v(ni), v(eq), eq.get(y-1,(None,))[0]
        o, c, dd = v(ocf), v(cap), v(da)
        roe = n/((e1+e0)/2)*100 if n and e1 and e0 else None
        f = lambda x: f"{x/1e6:7.0f}" if x is not None else "     -"
        print(f" {y}{f(r)}{f(n)}{f((e1+e0)/2 if e1 and e0 else None)} {roe if roe is None else round(roe,1)!s:>5}{f(o)}{f(c)}{f(o-c if o and c else None)}{f(dd)}{f(o-dd if o and dd else None)}{f(v(iss))} {sh.get(y,0)/1e6:7.1f}")
    accs = sorted({v[1] for v in list(ocf.values()) if v})
    print(" accessions (first-filed OCF):", ", ".join(a for a in accs[-10:]))
