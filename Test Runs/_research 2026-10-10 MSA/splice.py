"""Replace the run file's text from the heading that starts with argv[1] up to (not including) the heading that
starts with argv[2] by the contents of argv[3]. A plain text splice; used to write each question as it closes."""
import sys
p = "C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-10-10 Run - MSA MSA Safety.md"
s = open(p, encoding="utf-8").read()
a = s.index(sys.argv[1])
b = s.index(sys.argv[2], a + 1)
new = open(sys.argv[3], encoding="utf-8").read()
if not new.endswith("\n\n"):
    new = new.rstrip("\n") + "\n\n"
open(p, "w", encoding="utf-8").write(s[:a] + new + s[b:])
print("spliced", len(new), "chars")
