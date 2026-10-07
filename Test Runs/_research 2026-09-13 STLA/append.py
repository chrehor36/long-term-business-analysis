"""Append a section file to the run file. usage: python append.py <section.md>"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.join(HERE, "..", "2026-09-13 Run - STLA Stellantis.md")
sec = open(sys.argv[1], encoding="utf-8").read()
cur = open(RUN, encoding="utf-8").read()
first = sec.strip().splitlines()[0]
if first in cur:
    raise SystemExit("section heading already present: " + first)
with open(RUN, "a", encoding="utf-8") as f:
    if not cur.endswith("\n"):
        f.write("\n")
    f.write(sec)
print("appended", first, len(sec))
