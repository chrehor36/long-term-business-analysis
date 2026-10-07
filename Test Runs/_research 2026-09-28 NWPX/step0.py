import sys, json, datetime, urllib.request
sys.path.insert(0, '../../tools')
import sources as S
url = S.USD_TREASURY.format(yr=2026); print(url)
txt = urllib.request.urlopen(urllib.request.Request(url, headers=S.WEB_UA), timeout=45).read().decode()
rows=[r for r in txt.strip().split('\n') if r.strip()]
hdr=rows[0].split(','); i=[j for j,h in enumerate(hdr) if '30 Yr' in h][0]
for r in rows[1:6]: c=r.split(','); print('TREASURY', c[0], c[i])
print('SOV tool', S.sovereign('USD'))
p = S.price('NWPX'); print('PRICE', p)
r = S._chart('NWPX')
m = r['meta']; print({k: m.get(k) for k in ('regularMarketTime','exchangeName','fullExchangeName','currency','regularMarketPrice','chartPreviousClose','regularMarketVolume')})
print('regularMarketTime UTC', datetime.datetime.utcfromtimestamp(m.get('regularMarketTime')).isoformat())
ts = r['timestamp']; cl = r['indicators']['quote'][0]['close']; vo=r['indicators']['quote'][0]['volume']
for t, c, v in list(zip(ts, cl, vo))[-15:]: print(datetime.datetime.utcfromtimestamp(t).date(), c, v)
print('first', datetime.datetime.utcfromtimestamp(ts[0]).date(), cl[0])
json.dump(r, open('cache/chart_raw.json','w'))
cik = S.cik_for('NWPX'); print('CIK', cik)
print('SPLITS', r.get('events', {}).get('splits'))
for arg in (cik, 'NWPX', int(cik[0]) if isinstance(cik, tuple) else cik, str(cik[0]).zfill(10) if isinstance(cik, tuple) else cik):
    try: print('DEAL_NOTE', repr(arg), '->', repr(S.deal_note(arg))[:800])
    except Exception as e: print('DEAL_NOTE', repr(arg), 'EXC', type(e).__name__, e)
try: print('DEAL_FILINGS', S.deal_filings(int(cik[0]) if isinstance(cik, tuple) else cik))
except Exception as e: print('DEAL_FILINGS EXC', type(e).__name__, e)
try: print('NAME_CHANGE', S.name_change_note(int(cik[0]) if isinstance(cik, tuple) else cik))
except Exception as e: print('NAME_CHANGE EXC', type(e).__name__, e)
