import json,sys
d=json.load(open('facts.json'))['facts']['us-gaap']
def annual(tag):
    if tag not in d: return {}
    out={}
    for u,vals in d[tag]['units'].items():
        for v in vals:
            if v.get('fp')=='FY' and v.get('form','').startswith('10-K'):
                # duration facts: use frame CYxxxx if available
                fr=v.get('frame','')
                if 'start' in v:
                    import datetime
                    s=datetime.date.fromisoformat(v['start']); e=datetime.date.fromisoformat(v['end'])
                    if (e-s).days<350: continue
                    out.setdefault(e.year,v['val'])
                else:
                    e=v['end']
                    if e[5:]=='12-31': out.setdefault(int(e[:4]),v['val'])
    return out
for t in sys.argv[1:]:
    a=annual(t); print(t, {k:round(a[k]/1e6,1) for k in sorted(a)})
