import json,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
def series(fn,tags):
    d=json.load(open(fn))['facts']['us-gaap']; s={}
    for t in tags:
        if t not in d: continue
        for u,v in d[t]['units'].items():
            for f in sorted(v,key=lambda f:f['filed'],reverse=True):  # earliest-filed vintage wins: iterate latest first, overwrite
                if f['form']!='10-K' or 'start' not in f: continue
                sd,ed=f['start'],f['end']
                import datetime as D; days=(D.date.fromisoformat(ed)-D.date.fromisoformat(sd)).days
                if not(330<days<380): continue
                y=int(ed[:4]) if ed[5:7]>='06' else int(ed[:4])-1
                s.setdefault(t,{})[y]=f['val']/1e6
    return s
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet']
out={}
for t in ['GD','LMT','NOC','LHX']:
    s=series(f'{t}_facts.json',REV+['OperatingIncomeLoss'])
    rev={}
    for tg in REV:
        for y,v in s.get(tg,{}).items(): rev.setdefault(y,v)
    oi=s.get('OperatingIncomeLoss',{})
    out[t]={y:(rev[y],oi[y]) for y in rev if y in oi and 2011<=y<=2025}
def agg(d,ys):
    ys=[y for y in ys if y in d]
    if not ys: return None,0
    return 100*sum(d[y][1] for y in ys)/sum(d[y][0] for y in ys),len(ys)
hii={2011:(6575,100),2012:(6708,358),2013:(6820,512),2014:(6957,655),2015:(7020,769),2016:(7068,876),2017:(7441,881),2018:(8176,951),2019:(8899,736),2020:(9361,799),2021:(9524,513),2022:(10676,565),2023:(11454,781),2024:(11535,535),2025:(12484,657)}
out['HII']=hii
for t,d in out.items():
    print(t, {y:round(100*d[y][1]/d[y][0],1) for y in sorted(d)})
    print('   2012-19',agg(d,range(2012,2020)),' 2020-25',agg(d,range(2020,2026)),' 2012-25',agg(d,range(2012,2026)),' 2023-25',agg(d,range(2023,2026)))
json.dump({k:{str(y):v for y,v in d.items()} for k,d in out.items()},open('pm.json','w'))
