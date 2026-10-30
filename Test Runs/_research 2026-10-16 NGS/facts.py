import json, sys
def annual(d, tag, unit="USD"):
    f = d['facts']['us-gaap'].get(tag)
    if not f: return {}
    out = {}
    for u, rows in f['units'].items():
        if u != unit: continue
        for r in rows:
            if r.get('form') not in ('10-K','10-K/A'): continue
            if 'frame' in r and not r['frame'].startswith('CY'): pass
            fy_end = r['end']
            if 'start' in r:
                # duration: keep ~1 year
                from datetime import date
                s = date.fromisoformat(r['start']); e = date.fromisoformat(r['end'])
                if not (350 <= (e-s).days <= 380): continue
            y = fy_end[:4]
            # keep the first-filed value (earliest filed)
            if y not in out or r['filed'] < out[y][1]:
                out[y] = (r['val'], r['filed'], r['accn'])
    return out
if __name__ == "__main__":
    d = json.load(open(sys.argv[1]))
    for tag in sys.argv[2:]:
        a = annual(d, tag)
        print(tag, {k: round(v[0]/1e6,1) for k, v in sorted(a.items())})
