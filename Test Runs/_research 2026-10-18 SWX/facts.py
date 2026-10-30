"""Print annual 10-K values for chosen us-gaap tags from SEC companyfacts. Usage: python -I facts.py CIK10 tag1,tag2,..."""
import sys, json, urllib.request
cik, tags = sys.argv[1], sys.argv[2].split(',')
req = urllib.request.Request(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json', headers={'User-Agent': 'Chris Hrehor chrehor36@gmail.com'})
d = json.load(urllib.request.urlopen(req, timeout=120))
print(d.get('entityName'))
g = d['facts'].get('us-gaap', {})
for t in tags:
    if t not in g: print(t, 'absent'); continue
    out = {}
    for unit, arr in g[t]['units'].items():
        for x in arr:
            if x.get('form') != '10-K': continue
            fy_end = x['end']
            if 'start' in x:
                from datetime import date
                s = date.fromisoformat(x['start']); e = date.fromisoformat(x['end'])
                if (e - s).days < 350: continue
            out.setdefault(fy_end, (x['val'], x['accn']))
    print(t, ' '.join(f"{k[:4]}:{v[0]/1e6:.0f}" for k, v in sorted(out.items()) if k >= '2015'))
