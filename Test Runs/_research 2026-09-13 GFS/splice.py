"""Replace one template section of the run file (from its '## Qn' heading to the next '## ' heading of the listed ones) with a file."""
import sys, re
run, start, end, src = sys.argv[1:5]
t = open(run, encoding="utf-8").read()
s = t.index(start)
e = t.index(end, s + len(start)) if end != "EOF" else len(t)
new = open(src, encoding="utf-8").read()
t = t[:s] + new + t[e:]
open(run, "w", encoding="utf-8").write(t)
print("spliced", len(new))
