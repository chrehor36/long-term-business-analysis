"""Replace a pending section of the run file with section.md. Usage: splice.py "<heading line prefix>" """
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
run = os.path.join(here, "..", "2026-10-11 Run - SPGI S&P Global.md")
t = open(run, encoding="utf-8").read()
new = open(os.path.join(here, "section.md"), encoding="utf-8").read().rstrip() + "\n"
prefix = sys.argv[1]
i = t.index(prefix)
j = t.index("*(pending)*\n", i)
assert t[i:j].count("\n") == 1, "heading not directly followed by pending"
t = t[:i] + new + t[j + len("*(pending)*\n"):]
open(run, "w", encoding="utf-8").write(t)
os.remove(os.path.join(here, "section.md"))
print("spliced", prefix)
