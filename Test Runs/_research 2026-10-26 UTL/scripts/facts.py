import json, sys
g = None
def annual(tag, unit='USD'):
    if tag not in g: return {}
    out = {}
    for x in g[tag]['units'].get(unit, []):
        if x.get('form') in ('10-K','10-K/A') and x.get('fp') == 'FY':
            fr = x.get('frame','')
            if 'start' in x:
                # duration: require ~1 year
                from datetime import date
                s = date.fromisoformat(x['start']); e = date.fromisoformat(x['end'])
                if not (350 <= (e-s).days <= 380): continue
            yr = x['end'][:4]
            # keep latest-filed value per end date
            k = x['end']
            if k not in out or x['filed'] > out[k][1]:
                out[k] = (x['val'], x['filed'], x['accn'])
    return out
if __name__ == '__main__':
    g = json.load(open(sys.argv[1]))['facts']['us-gaap']
    pat = sys.argv[2].lower() if len(sys.argv) > 2 else ''
    for t in sorted(g):
        if pat in t.lower():
            a = annual(t)
            yrs = sorted(k for k in a)
            print(t, yrs[0] if yrs else '', yrs[-1] if yrs else '', len(yrs))
