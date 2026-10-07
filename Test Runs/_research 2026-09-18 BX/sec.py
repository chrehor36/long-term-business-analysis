import sys, re
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
fn, start, end = sys.argv[1], sys.argv[2], sys.argv[3]
occ = int(sys.argv[4]) if len(sys.argv) > 4 else 2
t = open(fn, encoding="utf-8").read()
t = re.sub(r"\s*\|\s*", " | ", t); t = re.sub(r"[ \t]+", " ", t); t = re.sub(r"\n\s*\n+", "\n", t)
ms = [m.start() for m in re.finditer(start, t)]
s = ms[occ-1] if len(ms) >= occ else ms[-1]
e = re.search(end, t[s+10:])
e = s + 10 + e.start() if e else s + 50000
out = t[s:e]
open(sys.argv[5] if len(sys.argv) > 5 else "_sec.txt", "w", encoding="utf-8").write(out)
print(len(out), "chars; starts", s)
