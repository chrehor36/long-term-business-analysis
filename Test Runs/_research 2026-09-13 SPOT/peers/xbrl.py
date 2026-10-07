import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from edgar import companyfacts
cik = int(sys.argv[1]); tags = sys.argv[2].split(',')
cf = companyfacts(cik)
json.dump(cf, open(f'companyfacts_{cik}.json','w'))
for ns, facts in cf['facts'].items():
    for tag in tags:
        if tag in facts:
            for unit, arr in facts[tag]['units'].items():
                for a in arr:
                    if a.get('fp')=='FY' and a.get('form') in ('20-F','10-K') and (a.get('frame') or '').startswith('CY') :
                        print(ns, tag, unit, a['end'], a['val'], a['accn'], a.get('frame'))
