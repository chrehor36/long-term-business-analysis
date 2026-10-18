import json,sys
from datetime import date
cik=int(sys.argv[1]); d=json.load(open(f'cache/cf_{cik}.json'))
for t in sys.argv[2:]:
  for ns in d['facts']:
    u=d['facts'][ns].get(t)
    if not u: continue
    out={}
    for unit,vals in u['units'].items():
      for v in vals:
        if not v.get('form','').startswith('10-K'): continue
        if 'start' in v and not (330<(date.fromisoformat(v['end'])-date.fromisoformat(v['start'])).days<400): continue
        if v['end'][5:]!='12-31': continue
        out.setdefault(v['end'][:4],(v['val'],v['accn']))
    print(t, ' '.join(f"{y}:{out[y][0]/1e6:.1f}" for y in sorted(out)))
