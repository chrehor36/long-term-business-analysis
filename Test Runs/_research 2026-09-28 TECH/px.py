import sys, datetime
sys.path.insert(0, '../../tools')
import sources as S
r = S._chart('TECH')
ts = r['timestamp']; q = r['indicators']['quote'][0]; cl = q['close']; vol = q.get('volume')
pairs=[(datetime.datetime.utcfromtimestamp(t).date().isoformat(), c, v) for t,c,v in zip(ts,cl,vol) if c]
print('range', r['meta'].get('range'), r['meta'].get('dataGranularity'))
print('n', len(pairs), 'first', pairs[0], 'last', pairs[-1])
print('max', max(pairs, key=lambda p:p[1]), 'min', min(pairs, key=lambda p:p[1]))
print('events', r.get('events'))
for d,c,v in pairs:
    if d[:7] in ('2026-06','2026-07','2026-08','2026-09') or d[5:] in ('12-31','12-30','12-29','06-30','06-28','06-29'): print(d, round(c,2), v)
