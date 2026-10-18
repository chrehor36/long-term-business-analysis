import json, sys
d = json.load(open(sys.argv[1]))['facts']['us-gaap']
def inst(tag):
    out = {}
    if tag not in d: return out
    for u, rows in d[tag]['units'].items():
        for r in rows:
            if r.get('form') == '10-K' and r['end'].endswith('12-31'):
                y = int(r['end'][:4])
                # first-filed vintage: keep earliest filed
                if y not in out or r['filed'] < out[y][1]:
                    out[y] = (r['val'], r['filed'])
    return {y: v[0] for y, v in out.items()}
for t in sys.argv[2:]:
    a = inst(t)
    print(t[:45].ljust(45), ' '.join(f"{y}:{a[y]/1e6:,.0f}" for y in sorted(a) if y >= 2011))
