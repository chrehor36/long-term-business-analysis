import sys, json
sys.path.insert(0, 'tools')
import sources as S
print('SOV', S.sovereign('USD'))
p = S.price('TXRH'); print('PRICE', p)
r = S._chart('TXRH')
m = r['meta']; print({k: m.get(k) for k in ('regularMarketTime','exchangeName','fullExchangeName','currency','regularMarketPrice','chartPreviousClose')})
ts = r['timestamp'][-8:]; cl = r['indicators']['quote'][0]['close'][-8:]
import datetime
for t, c in zip(ts, cl): print(datetime.datetime.utcfromtimestamp(t).isoformat(), c)
print('CIK', S.cik_for('TXRH'))
print('SPLITS', r.get('events', {}).get('splits'))
