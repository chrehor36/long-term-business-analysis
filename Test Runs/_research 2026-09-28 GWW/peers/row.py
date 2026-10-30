"""Competitor row for AIT, the GPC run's construction (row_gpc_original.py) with one change:
revenue per year is the LARGEST of the revenue tags (AIT tags about $20M of other revenue under 'Revenues' for FY2011-2016,
which a first-tag reader takes as its sales). EBIT = pretax income + interest expense; margin = EBIT / revenue;
NTOA = assets - cash - goodwill - intangibles - operating ROU - (current liabilities - current debt - short-term borrowings - current op lease liability);
return = EBIT / year-end NTOA. First-filed 10-K value per period end."""
import json, sys, io, datetime
from collections import defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.')
import importlib.util
spec = importlib.util.spec_from_file_location('g', 'row_gpc_original.py'); g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
def revmax(f):
    best = {}
    for tag in g.T['rev']:
        s = g.fy(g.series(f, [tag], flow=True))
        for y, v in s.items():
            if v > best.get(y, 0): best[y] = v
    return best
def run(t, y0=2009, y1=2026):
    f = g.load(t)
    s = {k: g.fy(g.series(f, v, flow=k in ('rev', 'pti', 'intx', 'ni'))) for k, v in g.T.items()}
    s['rev'] = revmax(f)
    rows = {}
    for y in range(y0, y1 + 1):
        G = lambda k: s[k].get(y)
        rev, pti, ix = G('rev'), G('pti'), G('intx')
        if rev is None or pti is None: continue
        ebit = pti + abs(ix or 0)
        z = lambda k: G(k) or 0
        n = z('A') - z('C') - z('G') - z('I') - z('R') - (z('L') - z('CD') - z('SD') - z('CL'))
        rows[y] = dict(rev=rev, ebit=ebit, m=ebit / rev, ntoa=n, ret=(ebit / n if n > 0 else None))
    return rows
out = {}
for t in ['AIT', 'FAST', 'GWW', 'MSM', 'DXPE', 'DSGR', 'GIC', 'GPC']:
    r = run(t); out[t] = r
    print('==', t)
    for y, x in r.items():
        print(y, 'rev %8.0f ebit %6.0f margin %5.1f%% NTOA %7.0f ret %s' % (x['rev'] / 1e6, x['ebit'] / 1e6, x['m'] * 100, x['ntoa'] / 1e6, '  n/a' if x['ret'] is None else '%5.1f%%' % (x['ret'] * 100)))
    for a, b in ((2009, 2025), (2016, 2025), (2021, 2025)):
        ys = [y for y in range(a, b + 1) if y in r]
        if not ys: continue
        mm = sum(r[y]['m'] for y in ys) / len(ys); rr = [r[y]['ret'] for y in ys if r[y]['ret'] is not None]
        print(f'  mean {a}-{b} ({len(ys)} yrs): margin {mm*100:.1f}%  return {sum(rr)/len(rr)*100 if rr else float("nan"):.1f}%  margin range {min(r[y]["m"] for y in ys)*100:.1f}-{max(r[y]["m"] for y in ys)*100:.1f}%')
json.dump(out, open('row.json', 'w'), indent=0)
