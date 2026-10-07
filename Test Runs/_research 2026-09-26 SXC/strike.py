import urllib.request, json, datetime
UA={'User-Agent':'Mozilla/5.0'}
u='https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv'
b=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read()
open('treasury_2026.csv','wb').write(b)
rows=b.decode().strip().split('\n'); h=rows[0].split(','); i=[k for k,x in enumerate(h) if '30 Yr' in x][0]
for r in rows[1:4]: c=r.split(','); print('TREASURY', c[0], '30Y', c[i])
u='https://query1.finance.yahoo.com/v8/finance/chart/SXC?range=1mo&interval=1d'
b=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read()
open('price_raw.json','wb').write(b)
r=json.loads(b)['chart']['result'][0]; m=r['meta']
print('meta', m.get('regularMarketPrice'), datetime.datetime.utcfromtimestamp(m['regularMarketTime']), m.get('currency'), m.get('exchangeName'))
q=r['indicators']['quote'][0]
for t,c in list(zip(r['timestamp'],q['close']))[-5:]: print(datetime.datetime.utcfromtimestamp(t).date(), c)
