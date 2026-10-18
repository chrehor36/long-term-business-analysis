import json, sys
sys.stdout.reconfigure(encoding='utf-8')
def series(path, tags):
    g = json.load(open(path))['facts']['us-gaap']; out = {}
    for t in tags:
        if t not in g: continue
        for x in list(g[t]['units'].values())[0]:
            if x.get('form') == '10-K' and x.get('fp') == 'FY' and x['end'][5:] == '12-31' and x.get('start', '')[:4] == x['end'][:4] and x.get('start','')[5:] == '01-01':
                out.setdefault(x['end'][:4], x['val'] / 1e6)
    return out
C = {
 'UHS': ('cache/facts.json', ['RevenueFromContractWithCustomerExcludingAssessedTax']),
 'HCA': ('cache/hca.json', ['Revenues', 'RevenueFromContractWithCustomerIncludingAssessedTax']),
 'CYH': ('cache/cyh.json', ['Revenues', 'HealthCareOrganizationRevenue']),
 'ACHC': ('cache/achc.json', ['RevenueFromContractWithCustomerExcludingAssessedTax', 'HealthCareOrganizationRevenue']),
}
yrs = [str(y) for y in range(2016, 2026)]
for k, (p, rt) in C.items():
    rev = series(p, rt)
    pt = series(p, ['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest'])
    ip = series(p, ['InterestPaidNet'])
    ocf = series(p, ['NetCashProvidedByUsedInOperatingActivities'])
    sbc = series(p, ['ShareBasedCompensation'])
    cx = series(p, ['PaymentsToAcquirePropertyPlantAndEquipment'])
    rows = []
    for y in yrs:
        if y in rev and y in pt and y in ocf and y in cx:
            r = rev[y]; e = (pt[y] + ip.get(y, 0)) / r * 100; o = (ocf[y] - sbc.get(y, 0) - cx[y]) / r * 100
            rows.append((y, r, e, o, cx[y] / r * 100))
    print(k, ' '.join(f"{y}:{e:.1f}/{o:.1f}" for y, r, e, o, c in rows))
    for lo in ('2016', '2021'):
        sel = [x for x in rows if x[0] >= lo]
        print(f"   avg {lo}-2025: pre-interest pretax margin {sum(x[2] for x in sel)/len(sel):.1f}%  owner-cash margin {sum(x[3] for x in sel)/len(sel):.1f}%  capex/rev {sum(x[4] for x in sel)/len(sel):.1f}%  n={len(sel)}  missing={[y for y in yrs if y>=lo and y not in [x[0] for x in sel]]}")
