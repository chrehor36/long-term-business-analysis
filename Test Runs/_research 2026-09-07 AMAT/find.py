import sys, re, os
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
OUT = os.path.dirname(os.path.abspath(__file__))
fn = sys.argv[1]; pat = sys.argv[2]
w = int(sys.argv[3]) if len(sys.argv) > 3 else 400
maxn = int(sys.argv[4]) if len(sys.argv) > 4 else 8
t = open(os.path.join(OUT, fn), encoding="utf-8").read()
t = t[t.find("\n"):] if len(t.split("\n")[0]) > 20000 else t
n = 0
for m in re.finditer(pat, t, re.I):
    a = max(0, m.start() - w // 3); b = min(len(t), m.end() + w)
    print("-----", m.start())
    print(re.sub(r"\s+", " ", t[a:b]))
    n += 1
    if n >= maxn: break
print(f"[{n} hits shown]")
