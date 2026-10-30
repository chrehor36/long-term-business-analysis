# replace a template section (from start heading to the line before the next heading) with a research md file
import sys, re
run = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-18 Run - RIVN Rivian.md"
start, nxt, src = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(run, encoding="utf-8").read()
i = s.index(start); j = s.index(nxt, i + len(start))
new = open(src, encoding="utf-8").read().rstrip() + "\n\n"
s = s[:i] + new + s[j:]
open(run, "w", encoding="utf-8").write(s)
print("replaced", j - i, "chars with", len(new))
