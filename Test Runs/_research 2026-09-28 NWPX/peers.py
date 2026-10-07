import json, sys, time
sys.path.insert(0, '../../tools')
import sources as S
from fetch import get
from datetime import date
for t in ['WMS','FRTA','CRH','OTTR','MWA','ATKR','WLK','USLM','SMID','MLI']:
    try: print('CIK', t, S.cik_for(t))
    except Exception as e: print('CIK', t, 'EXC', e)
peers={'WMS':'0001604028','FRTA':'0001678463','SMID':'0000091440','OTTR':'0001466593'}
def ann(f, tag):
    if tag not in f: return {}
    out={}
    for u,rows in f[tag]['units'].items():
        for r in rows:
            if r.get('form') not in ('10-K','10-K/A') or r.get('fp')!='FY': continue
            if 'start' in r:
                d=(date.fromisoformat(r['end'])-date.fromisoformat(r['start'])).days
                if d<340 or d>380: continue
            out.setdefault(r['end'],{})[r['filed']]=r['val']
    return {e:v[max(v)] for e,v in out.items()}
res={}
for t,c in peers.items():
    try:
        b=get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json'); open(f'cache/facts_{t}.json','wb').write(b)
    except SystemExit as e:
        print('FAIL',t,e); continue
    F=json.loads(b); f=F['facts'].get('us-gaap',{})
    print('=====', t, F.get('entityName'))
    rev={}
    for tag in ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet']:
        for k,v in ann(f,tag).items(): rev.setdefault(k,v)
    gp=ann(f,'GrossProfit'); oi=ann(f,'OperatingIncomeLoss')
    for k in sorted(rev):
        g=gp.get(k); o=oi.get(k)
        print(k, 'rev', round(rev[k]/1e6,1), 'gp', None if g is None else round(g/1e6,1), 'gm%', None if g is None else round(100*g/rev[k],1), 'oi', None if o is None else round(o/1e6,1), 'om%', None if o is None else round(100*o/rev[k],1))
    time.sleep(1)
