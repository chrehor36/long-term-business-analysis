import json
def load(p): return json.load(open(p))['facts'].get('ifrs-full', {})
def series(d, keys, isflow, pick='earliest'):
    out = {}
    for k in keys:
        if k not in d: continue
        for u, vals in d[k]['units'].items():
            if u != 'BRL': continue
            for x in vals:
                if not x.get('form','').startswith('20-F'): continue
                if isflow:
                    if 'start' not in x: continue
                    s, e = x['start'], x['end']
                    if not (s[5:] == '01-01' and e[5:] == '12-31' and s[:4] == e[:4]): continue
                elif x['end'][5:] != '12-31': continue
                y = x['end'][:4]
                better = (y not in out) or ((x['filed'] < out[y][1]) if pick == 'earliest' else (x['filed'] > out[y][1]))
                if better: out[y] = (x['val'], x['filed'], x['accn'])
        if out: return out
    return out
years = [str(y) for y in range(2016, 2026)]
res = {}
for name, p in (('AXIA', 'cache/facts.json'), ('CEMIG', 'cache/peers/cig.json'), ('COPEL', 'cache/peers/elp.json')):
    d = load(p)
    rev = series(d, ['Revenue', 'RevenueFromContractsWithCustomers'], True)
    op = series(d, ['ProfitLossFromOperatingActivities', 'ProfitLossBeforeTax'], True)
    ni = series(d, ['ProfitLossAttributableToOwnersOfParent', 'ProfitLoss'], True)
    eq = series(d, ['EquityAttributableToOwnersOfParent', 'Equity'], False)
    print(name, 'accessions used:', sorted(set(v[2] for v in ni.values())))
    print(' year     rev     op/pbt  margin%    ni   ROE% (ni / avg equity)')
    for y in years:
        if y in rev and y in ni:
            py = str(int(y) - 1)
            roe = ni[y][0] / ((eq[y][0] + eq[py][0]) / 2) * 100 if (y in eq and py in eq) else float('nan')
            o = op.get(y, (float('nan'),))[0]
            print(f" {y} {rev[y][0]/1e6:8.0f} {o/1e6:8.0f} {o/rev[y][0]*100:7.1f} {ni[y][0]/1e6:7.0f} {roe:6.1f}")
