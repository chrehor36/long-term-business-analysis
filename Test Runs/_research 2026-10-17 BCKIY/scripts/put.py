# Replace a section of the run file with the text of a fragment file.
# Usage: python put.py "<start marker>" "<end marker>" fragment.md
# The section from the start marker (inclusive) to the end marker (exclusive) is replaced.
import sys
RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-17 Run - BCKIY Babcock International Group.md"
start, end, frag = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(RUN, encoding="utf-8").read()
f = open(frag, encoding="utf-8").read()
s = t.index(start) if start != "^" else 0
e = t.index(end, s + 1)
t = t[:s] + f + t[e:]
open(RUN, "w", encoding="utf-8").write(t)
print("ok", s, e)
