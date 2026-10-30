import urllib.request, json, datetime
UA={'User-Agent':'Mozilla/5.0'}
u='https://query1.finance.yahoo.com/v8/finance/chart/KVUE?period1=1735689600&period2=1790000000&interval=1d'
b=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read()
open('price_hist_raw.json','wb').write(b)
r=json.loads(b)['chart']['result'][0]; q=r['indicators']['quote'][0]
d={str(datetime.datetime.utcfromtimestamp(t).date()):c for t,c in zip(r['timestamp'],q['close'])}
for k in ['2025-06-27','2025-10-31','2025-11-03','2025-12-26','2026-01-29','2026-06-26','2026-09-11','2026-09-18','2026-09-25']:
    print(k,d.get(k))
