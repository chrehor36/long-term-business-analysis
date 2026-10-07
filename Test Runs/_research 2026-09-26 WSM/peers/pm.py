import json, datetime, sys
REV = ['Revenues', 'RevenueFromContractWithCustomerExcludingAssessedTax', 'SalesRevenueNet', 'SalesRevenueGoodsNet',
       'RevenueFromContractWithCustomerIncludingAssessedTax']
def annual(facts, tag):
    out = {}
    u = facts.get(tag, {}).get('units', {}).get('USD', [])
    for v in u:
        if v.get('form') not in ('10-K', '10-K/A', '10-KT'): continue
        if 'start' not in v: continue
        s = datetime.date.fromisoformat(v['start']); e = datetime.date.fromisoformat(v['end'])
        if not (350 < (e - s).days < 380): continue
        k = v['end']
        if k not in out or v['filed'] > out[k][1]:
            out[k] = (v['val'], v['filed'])
    return {k: x[0] for k, x in out.items()}
def fy(end):
    # label a fiscal year by the calendar year in which most of it falls
    d = datetime.date.fromisoformat(end)
    return d.year - 1 if d.month <= 3 else d.year
def series(t):
    f = json.load(open(f'cf_{t}.json' if t != 'WSM' else '../companyfacts.json'))['facts']['us-gaap']
    rev = {}
    for tag in REV:
        for k, v in annual(f, tag).items():
            rev.setdefault(k, v)
    oi = annual(f, 'OperatingIncomeLoss')
    gp = annual(f, 'GrossProfit')
    rows = {}
    for k in sorted(set(rev) & set(oi)):
        rows[fy(k)] = (rev[k], oi[k], gp.get(k))
    return rows
if __name__ == '__main__':
    windows = [(2010, 2019), (2015, 2019), (2020, 2025), (2021, 2022), (2023, 2025)]
    allrows = {}
    for t in sys.argv[1:]:
        r = series(t); allrows[t] = r
        line = [t.ljust(5)]
        for a, b in windows:
            ys = [y for y in r if a <= y <= b]
            if len(ys) < (b - a + 1) * 0.6:
                line.append(f'{a}-{b}: n/a ({len(ys)}y)'); continue
            R = sum(r[y][0] for y in ys); O = sum(r[y][1] for y in ys)
            line.append(f'{a}-{b}: {100*O/R:5.1f}% ({len(ys)}y)')
        print('  '.join(line))
        print('      by year:', ' '.join(f'{y}:{100*r[y][1]/r[y][0]:.1f}' for y in sorted(r)))
    json.dump({t: {str(y): v for y, v in r.items()} for t, r in allrows.items()}, open('pm_out.json', 'w'))
