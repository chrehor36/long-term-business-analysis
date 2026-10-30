import sys, datetime
sys.path.insert(0, r'../../tools')
import sources as S
r = S._chart('WING')
ts = r['timestamp']; cl = r['indicators']['quote'][0]['close']
for t, c in zip(ts, cl):
    d = datetime.datetime.utcfromtimestamp(t).date().isoformat()
    if d in ('2025-06-26','2025-06-27','2025-06-30','2024-12-27','2025-12-26','2026-02-18','2026-07-29','2026-07-30') or d >= '2026-09-15':
        print(d, round(c, 2) if c else c)
cs = [c for c in cl if c]; print('max', max(cs), 'min last 2y', min(cs[-500:]))
print('splits', r.get('events', {}).get('splits'))
