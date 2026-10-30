# peer and AQN returns from SEC XBRL company facts (10-K / 40-F annual values)
# python -I peers.py  (reads cache/*.json fetched by curl)
import json
from datetime import date

def ann(d, tag, forms):
    g = d['facts']['us-gaap']
    if tag not in g: return {}
    out = {}
    for unit, vals in g[tag]['units'].items():
        if unit != 'USD': continue
        for v in vals:
            if v.get('form') not in forms: continue
            if 'start' in v:
                s = date.fromisoformat(v['start']); e = date.fromisoformat(v['end'])
                if not (350 <= (e - s).days <= 380): continue
            fy = v['end'][:4]
            # keep the latest filed per period end
            k = v['end']
            if k not in out or v['filed'] > out[k][1]:
                out[k] = (v['val'], v['filed'], v['accn'])
    # one value per fiscal year end date (use the year-end of the filer's FY)
    return out

def series(d, tags, forms):
    for t in tags:
        a = ann(d, t, forms)
        if a: return a, t
    return {}, None

peers = {
    'AQN': ('cache/facts.json', ('40-F', '40-F/A')),
    'EVRG': ('cache/f_EVRG.json', ('10-K',)),
    'AWK': ('cache/f_AWK.json', ('10-K',)),
    'ATO': ('cache/f_ATO.json', ('10-K',)),
}
for name, (f, forms) in peers.items():
    d = json.load(open(f))
    ni, tni = series(d, ['NetIncomeLossAvailableToCommonStockholdersBasic', 'NetIncomeLoss'], forms)
    eq, teq = series(d, ['StockholdersEquity'], forms)
    ocf, _ = series(d, ['NetCashProvidedByUsedInOperatingActivities'], forms)
    cap, tcap = series(d, ['PaymentsToAcquireProductiveAssets', 'PaymentsToAcquirePropertyPlantAndEquipment'], forms)
    iss, _ = series(d, ['ProceedsFromIssuanceOfCommonStock'], forms)
    oi, _ = series(d, ['OperatingIncomeLoss'], forms)
    assets, _ = series(d, ['Assets'], forms)
    print(f'== {name} (ni tag {tni}; capex tag {tcap})')
    ends = sorted(e for e in ni if e[:4] >= '2015')
    roes = []
    for e in ends:
        prev = [x for x in eq if x < e]
        if not prev or e not in eq: continue
        p = max(prev)
        avg = (eq[e][0] + eq[p][0]) / 2
        if name == 'AQN':
            avg -= 184.3e6  # preferred shares carried inside StockholdersEquity
        roe = ni[e][0] / avg
        roes.append((e, roe))
        o = ocf.get(e, (None,))[0]; c = cap.get(e, (None,))[0]
        a = assets.get(e, (None,))[0]; op = oi.get(e, (None,))[0]
        print(f"  {e} NI {ni[e][0]/1e6:9.1f}  avgEq {avg/1e6:9.1f}  ROE {roe*100:6.2f}%  OCF {o/1e6 if o else float('nan'):8.1f}  capex {c/1e6 if c else float('nan'):8.1f}  opinc/assets {(op/a*100) if (op and a) else float('nan'):5.2f}%  acc {ni[e][2]}")
    last = [r for e, r in roes if '2016' <= e[:4] <= '2025']
    if last:
        print(f"  mean ROE over {len(last)} fiscal years {min(e for e,r in roes if '2016'<=e[:4]<='2025')[:4]}-{max(e for e,r in roes if e[:4]<='2025')[:4]}: {sum(last)/len(last)*100:.2f}%")
    s_o = sum(ocf[e][0] for e in ocf if '2016' <= e[:4] <= '2025')
    s_c = sum(cap[e][0] for e in cap if '2016' <= e[:4] <= '2025')
    s_i = sum(iss[e][0] for e in iss if '2016' <= e[:4] <= '2025')
    print(f"  2016-2025 sums: OCF {s_o/1e6:.0f}  capex {s_c/1e6:.0f}  common issued (XBRL ProceedsFromIssuanceOfCommonStock) {s_i/1e6:.0f}")
