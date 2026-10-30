import json,sys
d=json.load(open('cache/facts.json'))['facts']['us-gaap']
def annual(tag):
    if tag not in d: return {}
    out={}
    for u,vals in d[tag]['units'].items():
        for v in vals:
            if v.get('fp')=='FY' and v.get('form')=='10-K' and 'frame' in v and len(v['frame'])==6:
                out[v['frame']]=(v['val'],v['accn'])
            elif v.get('fp')=='FY' and v.get('form')=='10-K' and 'frame' in v and v['frame'].endswith('Q4I'):
                out[v['frame']]=(v['val'],v['accn'])
    return out
for t in sys.argv[1:]:
    a=annual(t)
    print(t, {k:a[k][0] for k in sorted(a) if k>='CY2014'})
