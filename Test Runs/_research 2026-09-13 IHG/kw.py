# usage: python kw.py FILE "regex" [width] [maxhits]
import re, sys
fn, pat = sys.argv[1], sys.argv[2]
w = int(sys.argv[3]) if len(sys.argv) > 3 else 600
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 10
t = re.sub(r'\s+', ' ', open(fn, encoding='utf-8', errors='replace').read())
n = 0
for m in re.finditer(pat, t, flags=re.I):
    a = max(0, m.start() - w // 3); b = min(len(t), m.end() + w)
    print(f'--- @{m.start()}: ' + t[a:b]); n += 1
    if n >= mx: break
print('hits shown', n)
