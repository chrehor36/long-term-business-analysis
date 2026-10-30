import sys, json
sys.path.insert(0, '../../tools')
import sources as S
print('SOV', S.sovereign('USD'))
p = S.price('CLB'); print('PRICE', p)
r = S._chart('CLB')
m = r['meta']; print({k: m.get(k) for k in ('regularMarketTime','exchangeName','fullExchangeName','currency','regularMarketPrice','chartPreviousClose')})
ts = r['timestamp'][-12:]; cl = r['indicators']['quote'][0]['close'][-12:]
import datetime
for t, c in zip(ts, cl): print(datetime.datetime.utcfromtimestamp(t).isoformat(), c)
print('CIK', S.cik_for('CLB'))
print('SPLITS', r.get('events', {}).get('splits'))
