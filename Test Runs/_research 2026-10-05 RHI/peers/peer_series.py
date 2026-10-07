import json,sys
from datetime import date
def ser(f,tag):
    if tag not in f: return {}
    out={}
    for u,vals in f[tag]['units'].items():
        if u!='USD': continue
        for v in vals:
            if v.get('form') not in ('10-K','10-K405','10-KT'): continue
            if 'start' not in v: continue
            s=date.fromisoformat(v['start']); e=date.fromisoformat(v['end'])
            if not (350<(e-s).days<380): continue
            fy=v['end'][:4] if v['end'][5:7]>='06' else str(int(v['end'][:4])-1)
            if fy not in out or v['filed']>out[fy][1]: out[fy]=(v['val'],v['filed'],v['accn'])
    return out
for t in sys.argv[1:]:
    f=json.load(open(f'{t}_facts.json'))['facts']['us-gaap']
    rev={}
    for tag in ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueServicesNet','SalesRevenueNet']:
        for k,v in ser(f,tag).items():
            if k not in rev or v[1]>rev[k][1]: rev[k]=v
    oi=ser(f,'OperatingIncomeLoss')
    print('==',t)
    for y in sorted(set(rev)|set(oi)):
        r=rev.get(y,(None,))[0]; o=oi.get(y,(None,))[0]
        m=f'{o/r*100:.1f}%' if r and o is not None else ''
        print(y, round(r/1e6) if r else '', round(o/1e6,1) if o is not None else '', m, oi.get(y,('','',''))[2])
