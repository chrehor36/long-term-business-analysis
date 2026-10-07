import sys
p = "Test Runs/2026-09-13 Run - BAM Brookfield Asset Management.md"
start_marker, end_marker, src = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(p, encoding="utf-8").read()
start = t.index(start_marker)
end = t.index(end_marker) if end_marker != "EOF" else len(t)
new = open(src, encoding="utf-8").read()
if not new.endswith("\n"):
    new += "\n"
t = t[:start] + new + ("\n" if end_marker != "EOF" else "") + t[end:]
open(p, "w", encoding="utf-8").write(t)
print("replaced", start_marker[:30], "->", end_marker[:30], len(new), "chars")
