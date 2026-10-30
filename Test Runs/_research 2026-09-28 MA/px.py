import sys, datetime
sys.path.insert(0, '../../tools')
import sources as S
r = S._chart('MA')
ts = r['timestamp']; cl = r['indicators']['quote'][0]['close']
pairs=[(datetime.datetime.utcfromtimestamp(t).date().isoformat(), c) for t,c in zip(ts,cl) if c]
print('n', len(pairs), 'first', pairs[0], 'last', pairs[-1])
print('max', max(pairs, key=lambda p:p[1]), 'min', min(pairs, key=lambda p:p[1]))
for d,c in pairs:
    if d[:7] in ('2026-08','2026-09') or d in ('2025-12-31','2024-12-31','2023-12-29','2022-12-30','2021-12-31','2020-12-31'): print(d, round(c,2))
