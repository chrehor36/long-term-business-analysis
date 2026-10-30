import sys; sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import sys, re
# usage: python f.py FILE PATTERN [after] [before] [max]
fn, pat = sys.argv[1], sys.argv[2]
a = int(sys.argv[3]) if len(sys.argv) > 3 else 300
b = int(sys.argv[4]) if len(sys.argv) > 4 else 0
mx = int(sys.argv[5]) if len(sys.argv) > 5 else 5
t = open(fn, encoding="utf-8").read()
t = re.sub(r"\s*\|\s*", " | ", t); t = re.sub(r"\s+", " ", t)
n = 0
for m in re.finditer(pat, t, flags=re.I):
    print(f"[{m.start()}] ..." + t[max(0, m.start()-b): m.end()+a] + "...\n")
    n += 1
    if n >= mx: break
print("matches shown", n)
