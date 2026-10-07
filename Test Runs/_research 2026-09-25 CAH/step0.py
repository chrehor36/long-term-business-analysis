import urllib.request, json, time
from fetch import get
b=get('https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv')
open('treasury_2026.csv','wb').write(b)
print(b.decode()[:400])
r=urllib.request.Request('https://query1.finance.yahoo.com/v8/finance/chart/CAH?range=2y&interval=1d',headers={'User-Agent':'Mozilla/5.0'})
p=urllib.request.urlopen(r,timeout=60).read()
open('price_raw.json','wb').write(p)
j=json.loads(p)['chart']['result'][0]
m=j['meta']; print({k:m.get(k) for k in ['regularMarketPrice','regularMarketTime','previousClose','chartPreviousClose','fiftyTwoWeekHigh','fiftyTwoWeekLow']})
import datetime
ts=j['timestamp']; c=j['indicators']['quote'][0]['close']
for t,x in list(zip(ts,c))[-6:]: print(datetime.datetime.utcfromtimestamp(t), x)
cc=[x for x in c if x]; print('2y range',min(cc),max(cc)); print('events',j.get('events'))
