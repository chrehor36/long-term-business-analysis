import sys
p = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - UMC United Microelectronics.md"
start, end, src = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(p, encoding="utf-8").read()
i = t.index(start); j = t.index(end, i + len(start))
new = open(src, encoding="utf-8").read()
if not new.endswith("\n\n"):
    new = new.rstrip("\n") + "\n\n"
t = t[:i] + new + t[j:]
open(p, "w", encoding="utf-8").write(t)
print("spliced", src, len(new))
