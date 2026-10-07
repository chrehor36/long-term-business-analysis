import json, sys, collections
d=json.load(open('companyfacts.json'))
US=d['facts']['us-gaap']
DEI=d['facts']['dei']

FYE=[('FY2017','2016-02-01','2017-01-31'),('FY2018','2017-02-01','2018-01-31'),
     ('FY2019','2018-02-01','2019-01-31'),('FY2020','2019-02-01','2020-01-31'),
     ('FY2021','2020-02-01','2021-01-31'),('FY2022','2021-02-01','2022-01-31'),
     ('FY2023','2022-02-01','2023-01-31'),('FY2024','2023-02-01','2024-01-31'),
     ('FY2025','2024-02-01','2025-01-31'),('FY2026','2025-02-01','2026-01-31')]

def dur(tag, unit='USD'):
    """return dict fy -> (value, accn, form, fy_field) preferring original 10-K"""
    out={}
    if tag not in US: return None
    units=US[tag]['units']
    if unit not in units: 
        return {'__units__':list(units.keys())}
    for it in units[unit]:
        if 'start' not in it: continue
        for lbl,s,e in FYE:
            if it['start']==s and it['end']==e:
                cur=out.get(lbl)
                # prefer 10-K form, and prefer earliest accn (original filing) else any
                score=(0 if it['form']=='10-K' else 1, it['accn'])
                if cur is None or score<cur[0]:
                    out[lbl]=(score,(it['val'],it['accn'],it['form'],it.get('fy'),it.get('frame','')))
    return {k:v[1] for k,v in out.items()}

def inst(tag, unit='USD', dates=None):
    out={}
    if tag not in US: 
        if tag in DEI: units=DEI[tag]['units']
        else: return None
    else: units=US[tag]['units']
    if unit not in units: return {'__units__':list(units.keys())}
    for it in units[unit]:
        if 'start' in it: continue
        e=it['end']
        if dates and e not in dates: continue
        cur=out.get(e)
        score=(0 if it['form']=='10-K' else 1, it['accn'])
        if cur is None or score<cur[0]:
            out[e]=(score,(it['val'],it['accn'],it['form']))
    return {k:v[1] for k,v in out.items()}

def show(tag, unit='USD', kind='dur'):
    r = dur(tag,unit) if kind=='dur' else inst(tag,unit)
    print('===',tag,'===')
    if r is None: print('  TAG ABSENT'); return
    if '__units__' in r: print('  units available:',r['__units__']); return
    for k in sorted(r):
        v=r[k]
        print(f'  {k}: {v[0]:>18,.0f}  accn={v[1]} form={v[2]}')

if __name__=='__main__':
    for t in sys.argv[1:]:
        parts=t.split(':')
        tag=parts[0]; unit=parts[1] if len(parts)>1 else 'USD'; kind=parts[2] if len(parts)>2 else 'dur'
        show(tag,unit,kind)
