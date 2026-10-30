import sys
# usage: splice.py <section-file> <start-marker> <end-marker>
# replaces the run file text from start-marker (inclusive) to end-marker (exclusive) with the section file
p = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-18 Run - D Dominion Energy.md"
sec = open(sys.argv[1], encoding="utf-8").read()
t = open(p, encoding="utf-8").read()
s = t.index(sys.argv[2])
e = t.index(sys.argv[3], s + 1) if sys.argv[3] != "END" else len(t)
t = t[:s] + sec + t[e:]
open(p, "w", encoding="utf-8").write(t)
print("ok", s, e)
