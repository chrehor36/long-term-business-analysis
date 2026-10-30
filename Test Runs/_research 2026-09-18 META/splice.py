import sys
# usage: python splice.py <section_file> <start_marker> <end_marker>
# replaces the run file text from start_marker (inclusive) to end_marker (exclusive) with the section file
p = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-18 Run - META Meta Platforms.md"
t = open(p, encoding="utf-8").read()
sec, a, b = sys.argv[1], sys.argv[2], sys.argv[3]
s = t.index(a)
e = t.index(b, s)
new = open(sec, encoding="utf-8").read()
if not new.endswith("\n"):
    new += "\n"
t = t[:s] + new + "\n" + t[e:]
open(p, "w", encoding="utf-8").write(t)
print("spliced", sec, "at", s, "to", e, "len", len(t))
