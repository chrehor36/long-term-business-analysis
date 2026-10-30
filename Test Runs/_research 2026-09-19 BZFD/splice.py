# Replace a section of the run file between two marker headings with the content of a research .md file.
# usage: python splice.py <section.md> <start-marker> <end-marker>
import sys
RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-19 Run - BZFD BuzzFeed.md"
sec, start, end = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(RUN, encoding="utf-8").read()
new = open(sec, encoding="utf-8").read()
i = t.index(start)
j = t.index(end, i + len(start))
t = t[:i] + new.rstrip("\n") + "\n\n" + t[j:]
open(RUN, "w", encoding="utf-8").write(t)
print("spliced", sec, "between", repr(start[:40]), "and", repr(end[:40]), "->", len(t))
