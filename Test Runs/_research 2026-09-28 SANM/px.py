import sys, datetime
sys.path.insert(0, '../../tools')
import sources as S
r = S._chart('SANM')
ts = r['timestamp']; cl = r['indicators']['quote'][0]['close']
want = ['2025-03-28','2025-10-27','2025-10-24','2025-11-13','2026-07-27','2026-09-25']
for t, c in zip(ts, cl):
    d = datetime.datetime.utcfromtimestamp(t).date().isoformat()
    if d in want: print(d, c)
print('first', datetime.datetime.utcfromtimestamp(ts[0]).date(), len(ts))
print('events', list(r.get('events', {}).keys()))
