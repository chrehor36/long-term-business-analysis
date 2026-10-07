import json,sys
d=json.load(open(sys.argv[1]))['facts']['us-gaap']
def annual(tag):
    if tag not in d: return {}
    out={}
    for u,vals in d[tag]['units'].items():
        for v in vals:
            if v.get('form') in ('10-K','10-K/A') and v.get('fp')=='FY':
                s=v.get('start'); e=v['end']
                if s:
                    from datetime import date
                    ds=date.fromisoformat(s); de=date.fromisoformat(e)
                    if not (340<(de-ds).days<380): continue
                key=e
                # first filed
                if key not in out or v['filed']<out[key][1]:
                    out[key]=(v['val'],v['filed'])
    return out
tags=sys.argv[2:]
rows={}
for t in tags:
    for k,(v,f) in annual(t).items(): rows.setdefault(k,{})[t]=v
for k in sorted(rows):
    if k<'2014': continue
    print(k,' '.join(f"{t[:22]}={rows[k].get(t,'-')/1e6 if isinstance(rows[k].get(t),(int,float)) else '-':.0f}" if isinstance(rows[k].get(t),(int,float)) else f"{t[:22]}=-" for t in tags))
