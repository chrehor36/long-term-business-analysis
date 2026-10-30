import sys, json, datetime
sys.path.insert(0,'tools')
import sources as s
print('SOV', s.sovereign('USD'))
r = s._chart('PAYO', '1y')
m = r['meta']
print({k: m.get(k) for k in ('regularMarketPrice','regularMarketTime','chartPreviousClose','currency','exchangeName','fullExchangeName')})
print(datetime.datetime.utcfromtimestamp(m['regularMarketTime']))
ts = r['timestamp']; c = r['indicators']['quote'][0]['close']
for t, x in list(zip(ts, c)):
    d = datetime.datetime.utcfromtimestamp(t).strftime('%Y-%m-%d')
    if d >= '2026-06-05' and d <= '2026-06-20' or d >= '2026-09-15': print(d, x)
json.dump(r, open('Test Runs/_research 2026-09-29 PAYO/px_1y.json','w'))
