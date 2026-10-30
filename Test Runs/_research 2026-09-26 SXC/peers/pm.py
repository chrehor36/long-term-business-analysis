import json,sys,os,time
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fetch import get
P={'SXC':1514705,'CLF':764065,'X':1163302,'HCC':1691303,'AMR':1704715,'DTE':936340,'KOP':1315257}
REVT=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','RevenueFromContractWithCustomerIncludingAssessedTax']
out=[]
for tk,cik in P.items():
    fn=f'peers/cf_{tk}.json'
    if not os.path.exists(fn):
        open(fn,'wb').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json')); time.sleep(0.3)
    d=json.load(open(fn)); name=d['entityName']; g=d['facts'].get('us-gaap',{})
    def ser(tags):
        s={}
        for t in tags:
            if t not in g: continue
            for u,v in g[t]['units'].items():
                if u!='USD': continue
                for f in v:
                    if f['form'] in('10-K','10-K/A') and 'start' in f and f['end'][5:]=='12-31' and f['start'][5:]=='01-01' and f['start'][:4]==f['end'][:4]:
                        s.setdefault(int(f['end'][:4]),f['val']/1e6)
        return s
    R=ser(REVT); O=ser(['OperatingIncomeLoss'])
    def agg(a,b):
        ys=[y for y in range(a,b+1) if y in R and y in O]
        if not ys: return 'n/a',0
        return f'{100*sum(O[y] for y in ys)/sum(R[y] for y in ys):.1f}%',len(ys)
    line=[tk,name]
    for a,b in [(2012,2019),(2020,2025),(2012,2025),(2021,2023),(2024,2025)]:
        v,n=agg(a,b); line.append(f'{a}-{b}: {v} ({n}y)')
    yrs=sorted(set(R)&set(O)); line.append(f'years {yrs[0] if yrs else None}-{yrs[-1] if yrs else None}')
    out.append(' | '.join(line)); print(out[-1])
open('peers/pm_out.txt','w').write('\n'.join(out))
