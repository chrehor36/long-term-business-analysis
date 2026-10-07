import urllib.request, json, datetime
UA={'User-Agent':'Mozilla/5.0'}
u='https://query1.finance.yahoo.com/v8/finance/chart/ABT?range=2y&interval=1d'
b=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read()
open('cache/price_hist_ABT.json','wb').write(b)
r=json.loads(b)['chart']['result'][0]
q=r['indicators']['quote'][0]
rows=[(datetime.datetime.utcfromtimestamp(t).date().isoformat(),c) for t,c in zip(r['timestamp'],q['close'])]
want=('2025-06-30','2025-12-31','2026-01-21','2026-01-23','2026-03-20','2026-06-30','2026-07-15','2026-07-17','2026-08-28','2026-09-01','2026-09-02','2026-09-03')
for d,c in rows:
    if d in want: print(d, round(c,2))
cs=[c for d,c in rows if d>='2025-09-25']; print('52w hi/lo', round(max(cs),2), round(min(cs),2))
