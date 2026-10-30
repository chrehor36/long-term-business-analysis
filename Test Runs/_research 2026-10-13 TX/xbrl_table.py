# ten-year table from SEC companyfacts (ifrs-full), value from the latest 20-F that reports each year-end
import json, sys, datetime as dt
d = json.load(open(sys.argv[1]))['facts']['ifrs-full']
C = sys.argv[2].split(',')
def get(c):
    out = {}
    if c not in d: return out
    for u, xs in d[c]['units'].items():
        for x in xs:
            if x.get('form') not in ('20-F', '20-F/A'): continue
            e = x['end']
            if not e.endswith('12-31'): continue
            if 'start' in x:
                s = dt.date.fromisoformat(x['start']); en = dt.date.fromisoformat(e)
                if (en - s).days < 360: continue
            y = int(e[:4])
            if y not in out or x['filed'] > out[y][1]:
                out[y] = (x['val'], x['filed'], x['accn'])
    return out
yrs = list(range(2015, 2026))
print('concept'.ljust(50), *[str(y).rjust(8) for y in yrs])
for c in C:
    g = get(c)
    print(c[:50].ljust(50), *[(str(round(g[y][0]/1e6)) if y in g else '-').rjust(8) for y in yrs])
