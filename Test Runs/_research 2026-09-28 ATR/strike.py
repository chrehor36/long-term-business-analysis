import urllib.request, json, datetime, sys
UA={'User-Agent':'Mozilla/5.0'}
u='https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv'
b=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read()
open('cache/treasury_2026.csv','wb').write(b)
rows=b.decode().strip().split('\n'); h=rows[0].split(','); i=[k for k,x in enumerate(h) if '30 Yr' in x][0]
for r in rows[1:4]: c=r.split(','); print('TREASURY', c[0], '30Y', c[i])
t='ATR'
u='https://query1.finance.yahoo.com/v8/finance/chart/%s?range=2y&interval=1d'%t
b=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read()
open('cache/price_raw_%s.json'%t,'wb').write(b)
r=json.loads(b)['chart']['result'][0]; m=r['meta']
print(t,'meta', m.get('regularMarketPrice'), datetime.datetime.utcfromtimestamp(m['regularMarketTime']), m.get('currency'), m.get('exchangeName'))
q=r['indicators']['quote'][0]
rows=[(datetime.datetime.utcfromtimestamp(ts).date().isoformat(),c) for ts,c in zip(r['timestamp'],q['close'])]
for d,c in rows[-6:]: print(' ',d, c)
for d,c in rows:
    if d in ('2025-03-31','2025-06-30','2025-12-31','2026-03-31','2026-06-30','2026-08-28','2026-09-01','2026-09-02'): print(' ',d, round(c,2))
cs=[c for d,c in rows if d>='2025-09-26' and c]; print('52w hi/lo', round(max(cs),2), round(min(cs),2))
print('splits', r.get('events',{}).get('splits'))
