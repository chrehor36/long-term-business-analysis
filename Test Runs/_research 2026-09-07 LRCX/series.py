import json,sys,collections
d=json.load(open('companyfacts_LRCX.json'))
us=d['facts']['us-gaap']
def ann(tag, unit='USD'):
    """annual (FY) values keyed by fiscal year end date, latest accession wins"""
    if tag not in us: return {}
    out={}
    for it in us[tag]['units'].get(unit,[]):
        if it.get('form') not in ('10-K','10-K/A'): continue
        if it.get('fp')!='FY': continue
        start=it.get('start'); end=it['end']
        if start:
            # duration ~ 1 year
            import datetime
            s=datetime.date.fromisoformat(start); e=datetime.date.fromisoformat(end)
            if not (330 <= (e-s).days <= 400): continue
        key=end
        prev=out.get(key)
        if prev is None or it['accn']>prev[1]:
            out[key]=(it['val'],it['accn'],it.get('fy'),it.get('start'))
    return out
def show(tag,unit='USD'):
    a=ann(tag,unit)
    print('###',tag)
    for k in sorted(a): print('  ',k,f"{a[k][0]:,}",a[k][1])
for t in sys.argv[1:]:
    show(t)
