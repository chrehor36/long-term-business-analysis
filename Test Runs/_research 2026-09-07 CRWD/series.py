import json, os, sys, collections
R=os.path.dirname(os.path.abspath(__file__))
f=json.load(open(os.path.join(R,'companyfacts.json')))
g=f['facts']['us-gaap']
def ann(tag):
    """FY annual values keyed by period end; returns {end: [(val,accn,fy,form,filed)]}"""
    if tag not in g: return {}
    out=collections.defaultdict(list)
    for unit,rows in g[tag]['units'].items():
        for r in rows:
            if r.get('form') not in ('10-K','10-K/A'): continue
            if r.get('fp')!='FY': continue
            if 'start' in r:
                # duration: must be ~365 days
                from datetime import date
                s=date(*map(int,r['start'].split('-'))); e=date(*map(int,r['end'].split('-')))
                if not (330 <= (e-s).days <= 400): continue
            out[r['end']].append((r['val'],r['accn'],r.get('fy'),r['form'],r.get('filed')))
    return dict(out)
def show(tag,label=None):
    d=ann(tag)
    if not d:
        print(f'  {tag}: NO DATA'); return
    print(f'  == {label or tag}')
    for end in sorted(d):
        vals=sorted(set(v[0] for v in d[end]))
        first=min(d[end],key=lambda x:x[4] or '')
        flag='  <<RESTATED %s>>'%vals if len(vals)>1 else ''
        print(f'    {end}  {first[0]/1e6:>12,.1f}M  orig-accn {first[1]} filed {first[4]}{flag}')
if __name__=='__main__':
    for t in sys.argv[1:]:
        show(t)
