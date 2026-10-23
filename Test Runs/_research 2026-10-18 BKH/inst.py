import json, sys
from datetime import date
g = json.load(open(sys.argv[1]))['facts']['us-gaap']
for tag in sys.argv[2:]:
    if tag not in g: print(tag, '-'); continue
    out = {}
    for u, arr in g[tag]['units'].items():
        for x in arr:
            if 'start' in x: continue
            e = date.fromisoformat(x['end'])
            if e.month == 12 and e.day == 31 and e.year >= 2019:
                if e.year not in out or x['filed'] > out[e.year][1]: out[e.year] = (x['val'], x['filed'])
    print(tag[:55].ljust(55), {k: round(v[0]/1e6,1) for k, v in sorted(out.items())})
