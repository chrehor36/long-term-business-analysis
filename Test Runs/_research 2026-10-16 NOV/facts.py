import json, sys
def annual(path, tags, start=2008):
    d = json.load(open(path))
    g = d['facts'].get('us-gaap', {})
    out = {}
    for t in tags:
        if t not in g: continue
        for unit, rows in g[t]['units'].items():
            for r in rows:
                if r.get('form') not in ('10-K','10-K/A'): continue
                fy_end = r['end']
                if 'start' in r:
                    from datetime import date
                    s = date.fromisoformat(r['start']); e = date.fromisoformat(r['end'])
                    if not (330 <= (e - s).days <= 380): continue
                y = int(fy_end[:4])
                if y < start: continue
                # keep the earliest-filed (first vintage) value for each year end
                key = (t, fy_end)
                if key not in out or r['filed'] < out[key][1]:
                    out[key] = (r['val'], r['filed'], r['accn'])
    return out
if __name__ == '__main__':
    path = sys.argv[1]; tags = sys.argv[2].split(',')
    o = annual(path, tags)
    for t in tags:
        rows = sorted((k[1], v) for k, v in o.items() if k[0] == t)
        if rows: print(t); [print('  ', e, round(v[0]/1e6,1), v[2]) for e, v in rows]
