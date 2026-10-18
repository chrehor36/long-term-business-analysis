import sys
p = "Test Runs/2026-10-13 Run - TEX Terex.md"
start, end, src = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(p, encoding="utf-8").read()
a = s.index(start); b = s.index(end, a + 1)
new = open(src, encoding="utf-8").read()
s = s[:a] + new + s[b:]
open(p, "w", encoding="utf-8").write(s)
print("inserted", len(new))
