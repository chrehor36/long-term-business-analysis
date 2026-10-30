import sys, os, json, urllib.request
from datetime import date
sys.path.insert(0, 'C:/Users/chreh/OneDrive/Documents/BRK/tools')
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
PEERS = {
    'ACNB': '0000715579',
    'ORRF': '0000826154',
    'MPB':  '0000879635',
    'FRAF': '0000723646',
    'CZNC': '0000810958',
    'NWFL': '0001013272',
    'SHBI': '0001035092',
    'FULT': '0000700564',
    'PFIS': '0001056943',
    'FKYS': '0000737875',
    'CZFS': '0000739421',
}

def facts(t, cik):
    p = f'peer_{t}_companyfacts.json'
    if not os.path.exists(p):
        d = urllib.request.urlopen(urllib.request.Request(
            f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json', headers=UA)).read()
        open(p, 'wb').write(d)
    return json.load(open(p))

def ann(g, tag, dur=True):
    if tag not in g:
        return {}
    out = {}
    for unit, vals in g[tag]['units'].items():
        for v in vals:
            if v.get('form') not in ('10-K',):
                continue
            if 'start' in v:
                s = date.fromisoformat(v['start']); e = date.fromisoformat(v['end'])
                if not (340 <= (e - s).days <= 380):
                    continue
            elif dur:
                pass
            out.setdefault(v['end'][:4], []).append(v['val'])
    return {k: max(set(vv), key=vv.count) for k, vv in sorted(out.items())}

def first(g, tags):
    for t in tags:
        r = ann(g, t)
        if r:
            return t, r
    return None, {}

YEARS = ['2021', '2022', '2023', '2024', '2025']
rows = {}
for t, cik in PEERS.items():
    d = facts(t, cik)
    g = d['facts']['us-gaap']
    ni = ann(g, 'NetIncomeLoss')
    eq = ann(g, 'StockholdersEquity')
    dep = ann(g, 'Deposits')
    assets = ann(g, 'Assets')
    _, ie_dep = first(g, ['InterestExpenseDeposits', 'InterestExpenseDepositAccounts',
                          'InterestExpenseDomesticDepositLiabilities'])
    _, nii = first(g, ['InterestIncomeExpenseNet', 'InterestIncomeExpenseAfterProvisionForLoanLoss'])
    ii = ann(g, 'InterestAndDividendIncomeOperating')
    iexp = ann(g, 'InterestExpense')
    nonii = ann(g, 'NoninterestIncome')
    nonie = ann(g, 'NoninterestExpense')
    out = {}
    for y in YEARS:
        py = str(int(y) - 1)
        r = {}
        if y in ni and y in eq and py in eq:
            r['roe'] = 100 * ni[y] / ((eq[y] + eq[py]) / 2)
        if y in ni and y in assets and py in assets:
            r['roa'] = 100 * ni[y] / ((assets[y] + assets[py]) / 2)
        if y in ie_dep and y in dep and py in dep:
            r['cod'] = 100 * ie_dep[y] / ((dep[y] + dep[py]) / 2)
        n = nii.get(y)
        if n is None and y in ii and y in iexp:
            n = ii[y] - iexp[y]
        if n and y in nonii and y in nonie:
            r['eff'] = 100 * nonie[y] / (n + nonii[y])
        if n and y in assets and py in assets:
            r['nii_avg_assets'] = 100 * n / ((assets[y] + assets[py]) / 2)
        out[y] = r
    rows[t] = out

hdr = ['metric'] + YEARS
for m, lbl in [('roe', 'ROE %'), ('roa', 'ROA %'), ('cod', 'cost of total deposits %'),
               ('eff', 'efficiency (noninterest exp / revenue) %'), ('nii_avg_assets', 'NII / avg assets %')]:
    print('\n===', lbl)
    print('ticker  ' + '  '.join(f'{y:>7}' for y in YEARS))
    for t in PEERS:
        vals = []
        for y in YEARS:
            v = rows[t][y].get(m)
            vals.append(f'{v:7.2f}' if v is not None else '      -')
        print(f'{t:6}  ' + '  '.join(vals))
json.dump(rows, open('peer_rows.json', 'w'), indent=1)
