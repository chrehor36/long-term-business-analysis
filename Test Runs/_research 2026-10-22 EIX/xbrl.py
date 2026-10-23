"""Print annual 10-K XBRL values (latest-filed vintage, FY duration) for EIX tags. Transcription only."""
import json, sys
import os
FN = os.environ.get('FACTS', 'facts.json') if False else (sys.argv.pop(1) if sys.argv[1].endswith('.json') else 'facts.json')
d = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache', FN)))
g = d['facts']['us-gaap']
def ann(tag, inst=False):
    if tag not in g: return {}
    out = {}
    for unit, vals in g[tag]['units'].items():
        for v in vals:
            if v.get('form') not in ('10-K',): continue
            if inst:
                if 'start' in v: continue
                y = v['end'][:4]
                if v['end'][5:] != '12-31': continue
            else:
                if 'start' not in v: continue
                from datetime import date
                s = date.fromisoformat(v['start']); e = date.fromisoformat(v['end'])
                if not (350 <= (e - s).days <= 380): continue
                y = v['end'][:4]
            # keep latest filed
            if y not in out or v['filed'] > out[y][1]:
                out[y] = (v['val'], v['filed'], v['accn'])
    return out
tags = sys.argv[1:]
years = [str(y) for y in range(2015, 2026)]
for t in tags:
    inst = t.startswith('I:')
    tt = t[2:] if inst else t
    a = ann(tt, inst)
    print(f"{tt[:60]:60s}", ' '.join(f"{y[2:]}:{a[y][0]/1e6:9.0f}" if y in a else f"{y[2:]}:      ---" for y in years))
