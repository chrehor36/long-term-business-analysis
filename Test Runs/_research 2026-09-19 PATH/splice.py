import sys
p = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-19 Run - PATH UiPath.md"
start, end, src = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(p, encoding="utf-8").read()
s = open(src, encoding="utf-8").read()
a = t.index(start); b = t.index(end, a + len(start))
t = t[:a] + s.rstrip("\n") + "\n\n" + t[b:]
open(p, "w", encoding="utf-8").write(t)
print("ok", len(t))
