# replace a "*(pending)*" section of the run file with the text in a section file: patch.py <heading-start> <section-file>
import sys
p = "Test Runs/2026-10-23 Run - NEE NextEra Energy.md"
head, secfile = sys.argv[1], sys.argv[2]
s = open(p, encoding="utf-8").read()
body = open(secfile, encoding="utf-8").read().rstrip("\n") + "\n"
i = s.index(head)
j = s.index("*(pending)*\n", i)
line_end = s.index("\n", i)
assert j == line_end + 1, "section is not pending"
s = s[:i] + body + s[j + len("*(pending)*\n"):]
open(p, "w", encoding="utf-8").write(s)
print("patched", head)
