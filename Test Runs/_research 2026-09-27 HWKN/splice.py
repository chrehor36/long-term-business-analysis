import sys, io
# usage: splice.py <start-heading-prefix> <end-heading-prefix> <bodyfile>
# replaces the lines from the line starting with start (inclusive) to the line starting with end (exclusive)
F = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-27 Run - HWKN Hawkins.md"
start, end, body = sys.argv[1], sys.argv[2], sys.argv[3]
lines = open(F, encoding="utf-8").read().split("\n")
si = [i for i, l in enumerate(lines) if l.startswith(start)]
ei = [i for i, l in enumerate(lines) if l.startswith(end)]
assert len(si) == 1, ("start", si)
assert len(ei) >= 1, ("end", ei)
e = [i for i in ei if i > si[0]][0]
b = open(body, encoding="utf-8").read().rstrip("\n").split("\n")
out = lines[:si[0]] + b + [""] + lines[e:]
open(F, "w", encoding="utf-8").write("\n".join(out))
print("spliced", si[0], e, len(b))
