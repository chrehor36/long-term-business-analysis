import sys, json, datetime
sys.path.insert(0, '../../tools')
import sources as S
print('SOV', S.sovereign('USD'))
p = S.price('ESI'); print('PRICE', p)
r = S._chart('ESI')
m = r['meta']; print({k: m.get(k) for k in ('regularMarketTime','exchangeName','fullExchangeName','currency','regularMarketPrice','chartPreviousClose')})
print('regularMarketTime UTC', datetime.datetime.utcfromtimestamp(m.get('regularMarketTime')).isoformat())
ts = r['timestamp'][-12:]; cl = r['indicators']['quote'][0]['close'][-12:]
for t, c in zip(ts, cl): print(datetime.datetime.utcfromtimestamp(t).isoformat(), c)
print('CIK', S.cik_for('ESI'))
print('SPLITS', r.get('events', {}).get('splits'))
for arg in (S.cik_for('ESI'), 'ESI', 1590714, '0001590714'):
    try: print('DEAL_NOTE', repr(arg), '->', repr(S.deal_note(arg))[:600])
    except Exception as e: print('DEAL_NOTE', repr(arg), 'EXC', type(e).__name__, e)
try:
    print('DEAL_FILINGS', S.deal_filings(1590714))
except Exception as e: print('DEAL_FILINGS EXC', e)
