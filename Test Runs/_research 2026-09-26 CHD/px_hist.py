import urllib.request,json,datetime
u='https://query1.finance.yahoo.com/v8/finance/chart/CHD?range=15y&interval=1mo'
b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read()
open('price_hist_raw.json','wb').write(b)
r=json.loads(b)['chart']['result'][0]
q=r['indicators']['quote'][0]
ev=r.get('events',{}).get('splits',{})
print('splits',ev)
for t,c in zip(r['timestamp'],q['close']):
    d=datetime.datetime.utcfromtimestamp(t).date()
    if d.month==12 or (d.month==1 and d.day==1): print(d,c)
