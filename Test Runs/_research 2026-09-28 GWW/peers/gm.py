import json,datetime
def ser(t,tags):
    f=json.load(open(f'{t}_facts.json'))['facts']['us-gaap']
    best={}
    for tag in tags:
        if tag not in f: continue
        for v in f[tag]['units'].get('USD',[]):
            if v.get('form')!='10-K' or 'start' not in v: continue
            d=(datetime.date.fromisoformat(v['end'])-datetime.date.fromisoformat(v['start'])).days
            if not 350<d<380: continue
            y=int(v['end'][:4]) if v['end'][5:7]>'06' else int(v['end'][:4])
            if y not in best or v['filed']<best[y][1]: best[y]=(v['val'],v['filed'],tag)
    return {y:b[0] for y,b in best.items()}
out=open('gm_out.txt','w')
for t in ['GWW','FAST','MSM','AIT']:
    rev={}
    for tag in ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet']:
        for y,v in ser(t,[tag]).items(): rev[y]=max(rev.get(y,0),v)
    gp=ser(t,['GrossProfit'])
    oi=ser(t,['OperatingIncomeLoss'])
    out.write(f'== {t}\n')
    for y in range(2009,2027):
        if y in rev and y in gp and y in oi:
            out.write(f'{y} rev {rev[y]/1e6:8.0f} GM {gp[y]/rev[y]*100:5.1f}% opex {(gp[y]-oi[y])/rev[y]*100:5.1f}% OM {oi[y]/rev[y]*100:5.1f}%\n')
out.close()
