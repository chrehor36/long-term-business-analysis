import json,urllib.request,sys,datetime
H={'User-Agent':'Mozilla/5.0'}
for t in sys.argv[1:]:
    ok=False
    for host in ("query1","query2"):
        try:
            u=f"https://{host}.finance.yahoo.com/v8/finance/chart/{t}?range=5d&interval=1d"
            r=urllib.request.Request(u,headers=H)
            d=json.loads(urllib.request.urlopen(r,timeout=30).read())
            res=d['chart']['result'][0]
            meta=res['meta']
            ts=res['timestamp']; cl=res['indicators']['quote'][0]['close']
            print(t,'regularMarketPrice',meta.get('regularMarketPrice'),'time',datetime.datetime.utcfromtimestamp(meta.get('regularMarketTime')).isoformat() if meta.get('regularMarketTime') else None,'currency',meta.get('currency'))
            for a,b in zip(ts,cl):
                print('   ',datetime.datetime.utcfromtimestamp(a).date().isoformat(),b)
            ok=True; break
        except Exception as e:
            err=e
    if not ok: print(t,'FAILED',err)
