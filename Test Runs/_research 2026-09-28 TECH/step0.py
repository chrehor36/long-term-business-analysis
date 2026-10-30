import sys, json, datetime
sys.path.insert(0, '../../tools')
import sources as S
print('SOV', S.sovereign('USD'))
p = S.price('TECH'); print('PRICE', p)
r = S._chart('TECH')
m = r['meta']; print({k: m.get(k) for k in ('regularMarketTime','exchangeName','fullExchangeName','currency','regularMarketPrice','chartPreviousClose')})
print('regularMarketTime UTC', datetime.datetime.utcfromtimestamp(m.get('regularMarketTime')).isoformat())
ts = r['timestamp'][-12:]; cl = r['indicators']['quote'][0]['close'][-12:]
for t, c in zip(ts, cl): print(datetime.datetime.utcfromtimestamp(t).isoformat(), c)
cik = S.cik_for('TECH'); print('CIK', cik)
print('SPLITS', r.get('events', {}).get('splits'))
for arg in (cik, 'TECH', int(cik[0]) if isinstance(cik, tuple) else cik, str(cik[0]).zfill(10) if isinstance(cik, tuple) else cik):
    try: print('DEAL_NOTE', repr(arg), '->', repr(S.deal_note(arg))[:800])
    except Exception as e: print('DEAL_NOTE', repr(arg), 'EXC', type(e).__name__, e)
try:
    print('DEAL_FILINGS', S.deal_filings(int(cik[0]) if isinstance(cik, tuple) else cik))
except Exception as e: print('DEAL_FILINGS EXC', type(e).__name__, e)
