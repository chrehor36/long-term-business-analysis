"""Replace a template section of the TSM run file with a filled section file.
Usage: python splice.py <section_file> <start_marker> <end_marker>
Everything from start_marker (inclusive) up to end_marker (exclusive) is replaced by the file.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "..", "2026-09-13 Run - TSM Taiwan Semiconductor.md")
sec, start, end = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(P, encoding="utf-8").read()
new = open(os.path.join(HERE, sec), encoding="utf-8").read().rstrip("\n") + "\n\n"
a = t.index(start)
b = t.index(end, a + 1)
t2 = t[:a] + new + t[b:]
open(P, "w", encoding="utf-8").write(t2)
print("spliced", sec, len(t), "->", len(t2))
