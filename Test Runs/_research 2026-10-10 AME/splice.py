"""Replace the run file's text from the line starting with START up to (not including) the line starting with END
by the contents of FILE.  python splice.py "## Q1" "## Q3" cache/q1q2.md"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.join(HERE, "..", "2026-10-10 Run - AME AMETEK.md")
start, end, src = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(RUN, encoding="utf-8").read()
i = t.index("\n" + start) + 1
j = t.index("\n" + end, i) + 1
new = open(os.path.join(HERE, src), encoding="utf-8").read().rstrip("\n") + "\n\n"
open(RUN, "w", encoding="utf-8").write(t[:i] + new + t[j:])
print("spliced", len(new))
