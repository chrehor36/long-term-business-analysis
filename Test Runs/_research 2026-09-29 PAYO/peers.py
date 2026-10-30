import sys, json
sys.path.insert(0,'tools')
import sources as s
out = open('Test Runs/_research 2026-09-29 PAYO/peers_out.txt','w',encoding='utf-8')
def P(*a):
    print(*a); print(*a, file=out)
def ann(f, tags, ns_list=('us-gaap','ifrs-full')):
    res = {}
    for ns in ns_list:
        for tag in tags:
            v = f['facts'].get(ns, {}).get(tag)
            if not v: continue
            for unit, arr in v['units'].items():
                if not unit.startswith('USD'): continue
                for x in arr:
                    if x.get('form') not in ('10-K','20-F','10-K/A','20-F/A'): continue
                    st = x.get('start')
                    if not st: continue
                    mo = int(x['end'][:4])*12+int(x['end'][5:7]) - int(st[:4])*12-int(st[5:7])
                    if mo not in (11,12): continue
                    y = x['end'][:4]
                    res.setdefault(y, {}).setdefault(tag, x['val'])
    return res
for t in ['PYPL','FLYW','DLO','RELY','BILL','WU','IMXI','XYZ','AFRM','TOST','ADYEY','WISE']:
    cik, name = s.cik_for(t)
    if not cik:
        P(t, 'NOT IN SEC TICKER MAP'); continue
    try:
        f = s.sec_facts(cik)
    except Exception as e:
        P(t, cik, name, 'facts failed', e); continue
    sub = json.loads(s._get(f'https://data.sec.gov/submissions/CIK{cik}.json', s.SEC_UA, None))
    rev = ann(f, ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','Revenue'])
    op = ann(f, ['OperatingIncomeLoss','ProfitLossFromOperatingActivities'])
    P(f'{t} {cik} {name} SIC {sub.get("sic")} {sub.get("sicDescription")}')
    for y in sorted(set(rev)|set(op)):
        if y < '2018': continue
        r = rev.get(y, {}); o = op.get(y, {})
        rv = max(r.values()) if r else None
        ov = list(o.values())[0] if o else None
        m = f'{100*ov/rv:.1f}%' if rv and ov is not None else '-'
        P(f'   {y} rev {rv/1e6 if rv else None:.1f} op {ov/1e6 if ov is not None else float("nan"):.1f} margin {m} tags {list(r)} {list(o)}' if rv else f'   {y} rev None op {ov}')
