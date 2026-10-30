# Replace the run file's text between two headings with the contents of a section file.
# usage: python splice.py section_file "start heading prefix" "end heading prefix"
import sys
p = r"C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-10-12 Run - ITOCY ITOCHU Corporation.md"
sec, a, b = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(p, encoding="utf-8").read()
new = open(sec, encoding="utf-8").read()
i = s.index(a)
j = s.index(b, i + 1)
s = s[:i] + new.rstrip("\n") + "\n\n" + s[j:]
open(p, "w", encoding="utf-8").write(s)
print("spliced", len(new), "chars between", a[:20], "and", b[:20])
