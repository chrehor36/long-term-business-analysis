"""First-filed annual values from SEC companyfacts (transcription only; checked against the filed statements in the run)."""
import json,sys
from datetime import date
d=json.load(open('cache/facts.json'))['facts']['us-gaap']
def annual(tags):
    out={}
    for tag in tags.split('+'):
        if tag not in d: continue
        for unit,vals in d[tag]['units'].items():
            for v in vals:
                if v.get('form')!='10-K' or v.get('fp')!='FY': continue
                e=date.fromisoformat(v['end']); fyear=e.year if e.month>6 else e.year-1
                if 'start' in v:
                    s=date.fromisoformat(v['start'])
                    if not 350<(e-s).days<380: continue
                if v.get('fy')!=fyear: continue   # the year's own 10-K
                out.setdefault(fyear,v['val'])
    return out
tags=sys.argv[1:]
rows={t:annual(t) for t in tags}
years=sorted(set(y for r in rows.values() for y in r))
print('year,'+','.join(t.split('+')[0][:22] for t in tags))
for y in years:
    print(str(y)+','+','.join(str(round(rows[t][y]/1e6,1)) if y in rows[t] else '' for t in tags))
