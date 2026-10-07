"""Replace the text between two markers in the run file with a fragment file.
usage: python splice.py START_MARKER END_MARKER fragment.md
The start marker is replaced (fragment must include its own heading); END marker is kept."""
import sys
p = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - BN Brookfield Corporation.md"
start, end, frag = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(p, encoding="utf-8").read()
a = t.index(start)
b = t.index(end, a + len(start)) if end != "EOF" else len(t)
new = open(frag, encoding="utf-8").read()
if not new.endswith("\n"):
    new += "\n"
t = t[:a] + new + t[b:]
open(p, "w", encoding="utf-8").write(t)
print("spliced", len(new), "chars; file now", len(t))
