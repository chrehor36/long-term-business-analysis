import json
def series(tk,tags):
    d=json.load(open(f'{tk}_facts.json'))['facts']['us-gaap']
    out={}
    for tag in tags:
        if tag not in d: continue
        for u,arr in d[tag]['units'].items():
            for x in arr:
                if x.get('form')=='10-K' and x.get('fp')=='FY' and x.get('start'):
                    s,e=x['start'],x['end']
                    if (int(e[:4])-int(s[:4]))*12+int(e[5:7])-int(s[5:7])<11: continue
                    y=e[:4]
                    # first-filed value per fiscal end
                    if y not in out or x['filed']<out[y][1]: out[y]=(x['val']/1e6,x['filed'],x['accn'])
    return out
import os
os.chdir('.')
res={}
for tk,path in [('NSIT','../NSIT_facts.json'),('CDW','CDW_facts.json'),('SNX','SNX_facts.json'),('PLUS','PLUS_facts.json')]:
    if tk=='NSIT':
        import shutil; shutil.copy(path,'NSIT_facts.json')
    gp=series(tk,['GrossProfit']); oi=series(tk,['OperatingIncomeLoss'])
    rv={}
    for t in ['Revenues','SalesRevenueNet','RevenueFromContractWithCustomerExcludingAssessedTax']:
        for y,v in series(tk,[t]).items(): rv.setdefault(y,v)
    res[tk]=(rv,gp,oi)
print('year | '+' | '.join(f'{t} GM / EBIT% / EBIT÷GP' for t in res))
for y in range(2009,2027):
    y=str(y); row=[y]
    for t,(rv,gp,oi) in res.items():
        if y in gp and y in oi and y in rv:
            row.append(f'{gp[y][0]/rv[y][0]*100:.1f} / {oi[y][0]/rv[y][0]*100:.1f} / {oi[y][0]/gp[y][0]*100:.1f}')
        else: row.append('-')
    print(' | '.join(row))
for t,(rv,gp,oi) in res.items():
    ys=sorted(gp); print(t,'latest',ys[-1],gp[ys[-1]][2], 'first',ys[0],gp[ys[0]][2])
    # averages
    for a,b in [(2010,2016),(2017,2021),(2022,2025),(2010,2025)]:
        ks=[str(k) for k in range(a,b+1) if str(k) in gp and str(k) in oi]
        if ks: print('  ',a,b,'sum EBIT/sum GP %.1f%%'%(100*sum(oi[k][0] for k in ks)/sum(gp[k][0] for k in ks)),len(ks))
