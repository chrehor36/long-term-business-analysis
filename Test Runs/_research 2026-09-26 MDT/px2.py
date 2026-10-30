import urllib.request, json, datetime
UA={'User-Agent':'Mozilla/5.0'}
for t,rng in (('MMED','range=6mo&interval=1d'),('MDT','period1=1735689600&period2=1790000000&interval=1d')):
    u='https://query1.finance.yahoo.com/v8/finance/chart/%s?%s'%(t,rng)
    b=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read()
    open('price_hist_%s.json'%t,'wb').write(b)
    r=json.loads(b)['chart']['result'][0]; q=r['indicators']['quote'][0]
    d={str(datetime.datetime.utcfromtimestamp(ts).date()):c for ts,c in zip(r['timestamp'],q['close'])}
    ks=sorted(d)
    print(t, r['meta'].get('exchangeName'), 'last', ks[-6:], [round(d[k],2) for k in ks[-6:]])
    for k in ['2025-10-24','2026-03-09','2026-04-24','2026-07-31','2026-08-28','2026-09-11','2026-09-14']:
        if k in d: print('  ',k,round(d[k],2))
