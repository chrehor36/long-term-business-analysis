"""Flatten a pipe-split statement block: join each row's cells onto one line."""
import sys, re
f, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
lines = open(f, encoding='utf-8').read().split('\n')[a-1:b]
out, cur = [], ''
for L in lines:
    t = L.strip()
    if not t or t == '|': continue
    if re.match(r'^[A-Za-z]', t) and not cur.endswith('('):
        if cur: out.append(cur)
        cur = t
    else:
        cur += ' ' + t
out.append(cur)
for o in out:
    o = re.sub(r'\s*\|\s*', ' ', o); o = re.sub(r'\s+', ' ', o)
    print(o[:260].replace("Ffe6","W").encode("ascii","replace").decode())
