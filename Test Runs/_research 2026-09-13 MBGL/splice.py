"""Splice a section file into the run file, replacing from one heading up to (not including) the next.
usage: python splice.py <section_file> "<start heading>" "<end heading>" """
import sys
RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - MBGL Mobility Global.md"
sec, start, end = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(RUN, encoding="utf-8").read()
a = s.index(start)
b = s.index(end, a + len(start))
new = open(sec, encoding="utf-8").read()
if not new.endswith("\n"):
    new += "\n"
s = s[:a] + new + "\n" + s[b:]
open(RUN, "w", encoding="utf-8").write(s)
print("spliced", sec, len(new), "chars; file now", len(s))
