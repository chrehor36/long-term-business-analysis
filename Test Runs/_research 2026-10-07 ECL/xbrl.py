# print annual (10-K, FY, 12-month) values of us-gaap tags from companyfacts; transcription only
import json, sys
d = json.load(open(sys.argv[1]))['facts']
def annual(tag, ns='us-gaap'):
    if tag not in d.get(ns, {}): return {}
    out = {}
    for unit, rows in d[ns][tag]['units'].items():
        for r in rows:
            if r.get('form') not in ('10-K', '10-K/A'): continue
            if 'start' in r:
                from datetime import date
                s = date.fromisoformat(r['start']); e = date.fromisoformat(r['end'])
                if not (350 <= (e - s).days <= 380): continue
            y = r['end'][:4]
            # keep the latest filed value per year (restated) and the first filed
            out.setdefault(y, []).append((r['filed'], r['val'], r['accn']))
    return {y: sorted(v) for y, v in out.items()}
tags = sys.argv[2].split(',')
years = [str(y) for y in range(int(sys.argv[3]), int(sys.argv[4]) + 1)]
for t in tags:
    a = annual(t)
    row = []
    for y in years:
        if y in a:
            first = a[y][0][1]; last = a[y][-1][1]
            row.append(f"{first/1e6:,.0f}" + ("" if first == last else f"/{last/1e6:,.0f}"))
        else: row.append("-")
    print(f"{t[:55]:55s} " + " ".join(f"{v:>13s}" for v in row))
print("years:", " ".join(years), " (first-filed/last-filed where they differ)")
