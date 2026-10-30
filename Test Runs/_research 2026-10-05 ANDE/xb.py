import json, datetime
def load(t): return json.load(open(f'facts_{t}.json'))
def annual(f, tag, ns='us-gaap', instant=False, unit='USD'):
    try: arr = f['facts'][ns][tag]['units'][unit]
    except KeyError: return {}
    out = {}
    for x in arr:
        if x.get('form') not in ('10-K','10-K/A','10-KT'): continue
        e = x['end']
        if not instant:
            if 'start' not in x: continue
            d = (datetime.date.fromisoformat(e) - datetime.date.fromisoformat(x['start'])).days
            if d < 350 or d > 380: continue
        else:
            if 'start' in x: continue
        # keep latest filed
        if e not in out or x['filed'] > out[e][1]:
            out[e] = (x['val'], x['filed'], x['accn'])
    return {k: v[0] for k, v in sorted(out.items())}
def first(f, tags, **kw):
    res = {}
    for t in tags:
        a = annual(f, t, **kw)
        for k, v in a.items():
            res.setdefault(k, v)
    return dict(sorted(res.items()))
