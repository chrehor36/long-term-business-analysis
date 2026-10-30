"""Splice a fragment into the run file, replacing the text from START up to (not including) END.
Usage: python -I splice.py FRAGMENT "START MARKER" "END MARKER" """
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
run = os.path.join(here, "..", "2026-10-23 Run - FE FirstEnergy.md")
frag = open(os.path.join(here, sys.argv[1]), encoding="utf-8").read()
start, end = sys.argv[2], sys.argv[3]
s = open(run, encoding="utf-8").read()
a = s.index(start)
b = s.index(end, a + 1) if end != "EOF" else len(s)
s = s[:a] + frag.rstrip("\n") + "\n\n" + s[b:]
open(run, "w", encoding="utf-8").write(s)
print("spliced", sys.argv[1], a, b)
