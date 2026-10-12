import json, sys
def load(p): return json.load(open(p))['facts']
def annual(f, tag, ns='us-gaap', unit='USD', fy_end_month=None):
    """first-filed 10-K value per fiscal period end, full-year duration only"""
    try: rows = f[ns][tag]['units'][unit]
    except KeyError: return {}
    out = {}
    for r in sorted(rows, key=lambda r: r['filed']):
        if r.get('form') not in ('10-K','10-K/A','20-F'): continue
        if 'start' in r:
            from datetime import date
            s = date.fromisoformat(r['start']); e = date.fromisoformat(r['end'])
            if not (350 <= (e - s).days <= 380): continue
        out.setdefault(r['end'], (r['val'], r['accn']))
    return out
if __name__ == '__main__':
    f = load(sys.argv[1])
    for tag in sys.argv[2:]:
        a = annual(f, tag)
        print(tag, {k: round(v[0]/1e6,1) for k, v in sorted(a.items()) if k >= '2014'})
