import sys, json, datetime
sys.path.insert(0, '../../tools')
import sources as S
print('SOV', S.sovereign('USD'))
p = S.price('KEYS'); print('PRICE', p)
r = S._chart('KEYS')
m = r['meta']; print({k: m.get(k) for k in ('regularMarketTime','exchangeName','fullExchangeName','currency','regularMarketPrice','chartPreviousClose')})
print('regularMarketTime UTC', datetime.datetime.utcfromtimestamp(m.get('regularMarketTime')).isoformat())
ts = r['timestamp'][-12:]; cl = r['indicators']['quote'][0]['close'][-12:]
for t, c in zip(ts, cl): print(datetime.datetime.utcfromtimestamp(t).isoformat(), c)
print('CIK', S.cik_for('KEYS'))
print('SPLITS', r.get('events', {}).get('splits'))
print('DEAL_NOTE', repr(S.deal_note('0001601046')))
