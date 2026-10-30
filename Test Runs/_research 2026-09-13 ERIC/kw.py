# usage: python kw.py FILE REGEX [width]
import re, sys
t = re.sub(r'\s+', ' ', open(sys.argv[1], encoding='utf-8').read())
w = int(sys.argv[3]) if len(sys.argv) > 3 else 250
seen = set()
for m in re.finditer(sys.argv[2], t, re.I):
    s = t[max(0, m.start()-w): m.end()+w]
    k = s[w-40:w+40]
    if k in seen: continue
    seen.add(k); print('...', s, '...\n')
