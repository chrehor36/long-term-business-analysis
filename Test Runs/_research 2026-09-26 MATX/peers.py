import sys,json,time
sys.path.insert(0,'.')
from fetch import get
from datetime import date
P={'KEX':'0000056047','ZIM':'0001654126','HRZL':'0001302707','OSG':'0000075208'}
def ann(facts,tags,ns='us-gaap'):
    out={}
    for tag in tags:
        if tag not in facts.get(ns,{}): continue
        for u,v in facts[ns][tag]['units'].items():
            for x in v:
                if x.get('fp')=='FY' and x.get('form','') in('10-K','20-F','10-K/A','20-F/A') and 'start' in x:
                    dd=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days
                    if 350<dd<380:
                        y=int(x['end'][:4])
                        if y not in out or x['filed']>out[y][2]: out[y]=(x['val'],u,x['filed'],tag)
    return out
for k,c in P.items():
    try:
        d=json.loads(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json'))
    except SystemExit as e:
        print(k,'FAIL');continue
    open(f'peers/{k}_facts.json','w').write(json.dumps(d))
    f=d['facts']; ns='ifrs-full' if 'ifrs-full' in f else 'us-gaap'
    rev=ann(f,['Revenues','Revenue','SalesRevenueNet','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueServicesNet'],ns)
    oi=ann(f,['OperatingIncomeLoss','ProfitLossFromOperatingActivities'],ns)
    print(k,d['entityName'],ns)
    for y in sorted(set(rev)|set(oi)):
        r=rev.get(y); o=oi.get(y)
        m=f'{o[0]/r[0]*100:6.1f}%' if r and o else ''
        print(' ',y,'rev',r[0]/1e6 if r else None,'oi',o[0]/1e6 if o else None,m, (o[3] if o else ''))
    time.sleep(0.5)
