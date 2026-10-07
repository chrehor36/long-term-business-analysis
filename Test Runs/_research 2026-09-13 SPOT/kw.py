# usage: python kw.py FILE REGEX [before] [after] [max]
import io
sys_stdout_fix = True
import sys, re, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
f, pat = sys.argv[1], sys.argv[2]
b = int(sys.argv[3]) if len(sys.argv) > 3 else 300
a = int(sys.argv[4]) if len(sys.argv) > 4 else 600
mx = int(sys.argv[5]) if len(sys.argv) > 5 else 10
t = open(f, encoding='utf-8').read()
n = 0
for m in re.finditer(pat, t):
    n += 1
    if n > mx: break
    s = max(0, m.start() - b); e = min(len(t), m.end() + a)
    print(f'=== @{m.start()} ===')
    print(t[s:e].replace('\n', ' / '))
print('matches shown', min(n, mx))
