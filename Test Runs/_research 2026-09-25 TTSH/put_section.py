"""Replace the run file's lines from the line-exact START heading (inclusive, or the '---' just above it if
back=1) up to (not including) the line-exact END heading, with the content of a section file."""
import sys
RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-25 Run - TTSH Tile Shop.md"
sec, start, end = sys.argv[1], sys.argv[2], sys.argv[3]
back = len(sys.argv) > 4 and sys.argv[4] == "back"
L = open(RUN, encoding="utf-8").read().split("\n")
s = [i for i, l in enumerate(L) if l.startswith(start)]
e = [i for i, l in enumerate(L) if l.startswith(end)]
assert len(s) == 1 and len(e) == 1 and s[0] < e[0], (s, e)
a = s[0] - 1 if back and L[s[0] - 1] == "---" else s[0]
new = open(sec, encoding="utf-8").read().rstrip("\n").split("\n")
L2 = L[:a] + new + L[e[0]:]
open(RUN, "w", encoding="utf-8", newline="\n").write("\n".join(L2))
print("replaced lines", a + 1, "to", e[0], "with", len(new))
