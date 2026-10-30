import urllib.request, json, datetime
UA={'User-Agent':'Mozilla/5.0'}
u='https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv'
b=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read()
open('cache/treasury_2026.csv','wb').write(b)
rows=b.decode().strip().split('\n'); h=rows[0].split(','); i=[k for k,x in enumerate(h) if '30 Yr' in x][0]
for r in rows[1:4]: c=r.split(','); print('TREASURY', c[0], '30Y', c[i])
for t in ('HWKN',):
    u='https://query1.finance.yahoo.com/v8/finance/chart/%s?range=2y&interval=1d'%t
    b=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read()
    open('cache/price_raw_%s.json'%t,'wb').write(b)
    r=json.loads(b)['chart']['result'][0]; m=r['meta']
    print(t,'meta', m.get('regularMarketPrice'), datetime.datetime.utcfromtimestamp(m['regularMarketTime']), m.get('currency'), m.get('exchangeName'))
    q=r['indicators']['quote'][0]
    rows=list(zip(r['timestamp'],q['close']))
    for ts,c in rows[-6:]: print(' ',datetime.datetime.utcfromtimestamp(ts).date(), c)
    cs=[c for ts,c in rows if datetime.datetime.utcfromtimestamp(ts).date()>=datetime.date(2025,9,25) and c]
    print(' 52w hi/lo', max(cs), min(cs))
    for ts,c in rows:
        d=datetime.datetime.utcfromtimestamp(ts).date().isoformat()
        if d in ('2025-06-30','2025-12-31','2026-06-30','2026-08-28','2026-09-01','2026-09-02'): print(' ',d,c)
