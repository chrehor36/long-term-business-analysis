import json, sys
from collections import defaultdict
def annual(facts, tag, unit='USD', fyend=None):
    """return {period_end: value} for 10-K annual durations (or instants), first-filed... use latest filed value"""
    try:
        arr = facts['facts']['us-gaap'][tag]['units'][unit]
    except KeyError:
        return {}
    out = {}
    for x in arr:
        if x.get('form') not in ('10-K','10-K/A'): continue
        if 'start' in x:
            from datetime import date
            s = date.fromisoformat(x['start']); e = date.fromisoformat(x['end'])
            if not (350 <= (e-s).days <= 380): continue
        k = x['end']
        # keep latest filed
        if k not in out or x['filed'] > out[k][1]:
            out[k] = (x['val'], x['filed'])
    return {k:v[0] for k,v in out.items()}
def tags(facts, sub):
    return [t for t in facts['facts']['us-gaap'] if sub.lower() in t.lower()]
if __name__ == '__main__':
    f = json.load(open(sys.argv[1]))
    if sys.argv[2] == 'find':
        for t in tags(f, sys.argv[3]): 
            a = annual(f, t)
            print(t, len(a), sorted(a)[-1] if a else '')
    else:
        for t in sys.argv[2:]:
            a = annual(f, t)
            print(t)
            for k in sorted(a): print('  ', k, round(a[k]/1e6,1))
