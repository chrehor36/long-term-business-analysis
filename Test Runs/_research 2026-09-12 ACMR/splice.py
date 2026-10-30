import io, sys
p = "Test Runs/2026-09-12 Run - ACMR ACM Research.md"
src = sys.argv[1]; start_marker = sys.argv[2]; end_marker = sys.argv[3]
s = io.open(p, encoding="utf-8").read()
new = io.open(src, encoding="utf-8").read()
a = s.index(start_marker); b = s.index(end_marker)
s = s[:a] + new + "\n" + s[b:]
io.open(p, "w", encoding="utf-8").write(s)
print("spliced", src, "->", len(s), "bytes")
