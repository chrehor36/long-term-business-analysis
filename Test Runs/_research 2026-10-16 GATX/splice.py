# Splice a drafted section into the run file: replaces the text between two markers.
# usage: python -I splice.py <draft file> <start marker> <end marker>
import sys
RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-16 Run - GATX GATX Corporation.md"
draft, a, b = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(RUN, encoding="utf-8").read()
new = open(draft, encoding="utf-8").read()
i = s.index(a)
j = s.index(b, i + len(a)) if b != "EOF" else len(s)
s = s[:i] + new + s[j:]
open(RUN, "w", encoding="utf-8", newline="\n").write(s)
print("spliced", len(new), "chars between", repr(a[:30]), "and", repr(b[:30]))
