"""sgrep.py FILE REGEX [WIDTH] [MAX] : print a window of WIDTH chars around each regex hit
in the whitespace-collapsed, pipe-stripped text. Shows char offset of the hit."""
import sys, re
f, rx = sys.argv[1], sys.argv[2]
w = int(sys.argv[3]) if len(sys.argv) > 3 else 600
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 20
t = open(f, encoding="utf-8", errors="replace").read()
t = re.sub(r"\s*\|\s*", " ", t)
t = re.sub(r"\s+", " ", t)
k = 0
last = -10**9
for m in re.finditer(rx, t, re.I):
    if m.start() - last < w // 2:
        continue
    last = m.start()
    a = max(0, m.start() - w // 4)
    print(f"[{m.start()}] ...{t[a:a+w]}...")
    print()
    k += 1
    if k >= mx:
        break
print(f"({k} windows shown; total hits {len(re.findall(rx, t, re.I))}; text length {len(t)})")
