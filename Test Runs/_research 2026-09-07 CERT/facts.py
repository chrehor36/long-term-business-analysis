import json, sys
from collections import defaultdict
def load(t): return json.load(open(f'companyfacts_{t}.json'))
def annual(facts, tags, fy_end_month=12):
    """Return {calendar_year: (val, tag, accn, form)} for FY-length duration facts."""
    out={}
    for tag in tags:
        node=facts['facts'].get('us-gaap',{}).get(tag)
        if not node: continue
        for unit,pts in node['units'].items():
            for p in pts:
                if 'start' not in p: continue
                from datetime import date
                s=date.fromisoformat(p['start']); e=date.fromisoformat(p['end'])
                days=(e-s).days
                if not (350<=days<=380): continue
                if p.get('fp')!='FY' or p.get('form') not in ('10-K','10-K/A'): continue
                y=e.year if e.month>=6 else e.year-1
                key=y
                if key not in out or p['end']>out[key][4]:
                    out[key]=(p['val'],tag,p.get('accn'),p.get('form'),p['end'])
    return out
def instant(facts, tags):
    out={}
    for tag in tags:
        node=facts['facts'].get('us-gaap',{}).get(tag)
        if not node: continue
        for unit,pts in node['units'].items():
            for p in pts:
                if 'start' in p: continue
                if p.get('form') not in ('10-K','10-K/A'): continue
                e=p['end']
                if e not in out: out[e]=(p['val'],tag,p.get('accn'))
    return out
def alltags(facts, sub='us-gaap'):
    return sorted(facts['facts'].get(sub,{}).keys())
