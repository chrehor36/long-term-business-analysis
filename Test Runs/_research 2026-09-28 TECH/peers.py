# operating margin as filed, companyfacts, newest vintage per fiscal year end; $M
import sys, json, os, time
from fetch import get
from datetime import date
sys.stdout.reconfigure(encoding='utf-8')
P = [('TECH','0000842023'),('TMO','0000097745'),('DHR','0000313616'),('BIO','0000012208'),('RVTY','0000031791'),('WAT','0001000697'),
     ('QGEN','0001015820'),('RGEN','0000730272'),('TXG','0001770787'),('QTRX','0001503274'),('AKYA','0001711933'),('ABCAM','0001492074')]
for t,cik in P:
    p=f'cache/peers/{t}_facts.json'
    if not os.path.exists(p):
        open(p,'wb').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json')); time.sleep(0.3)
    F=json.load(open(p))['facts']
    def ann(tags, ns):
        rows={}
        f=F.get(ns,{})
        for tg in tags:
            if tg not in f: continue
            for u,arr in f[tg]['units'].items():
                for x in arr:
                    if x.get('form') not in ('10-K','10-K/A','20-F','20-F/A') or 'start' not in x: continue
                    d=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days
                    if not 340<=d<=380: continue
                    k=x['end']
                    if k not in rows or x['filed']>rows[k][1]: rows[k]=(x['val'],x['filed'],u)
            if rows: pass
        return rows
    ns='ifrs-full' if t=='ABCAM' else 'us-gaap'
    if ns=='ifrs-full':
        rev=ann(['Revenue'],ns); oi=ann(['ProfitLossFromOperatingActivities'],ns); gp=ann(['GrossProfit'],ns)
    else:
        rev={}
        for tg in ['SalesRevenueNet','Revenues','RevenueFromContractWithCustomerExcludingAssessedTax']:
            r=ann([tg],ns); rev.update(r)
        oi=ann(['OperatingIncomeLoss'],ns); gp=ann(['GrossProfit'],ns)
    print('=====',t,cik)
    for e in sorted(set(rev)&set(oi)):
        if e[:4]>='2015':
            g=gp.get(e)
            print(f'  {e} rev {rev[e][0]/1e6:9.1f} {rev[e][2]} oi {oi[e][0]/1e6:8.1f} om {100*oi[e][0]/rev[e][0]:5.1f}%'+(f' gm {100*g[0]/rev[e][0]:5.1f}%' if g else ''))
