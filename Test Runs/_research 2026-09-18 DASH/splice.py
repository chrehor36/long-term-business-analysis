# replace the text between two headings in the run file with the content of a file
import sys, re
run = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-18 Run - DASH DoorDash.md"
start, end, src = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(run, encoding="utf-8").read()
new = open(src, encoding="utf-8").read().rstrip("\n") + "\n\n"
i = t.index(start); j = t.index(end, i + len(start)) if end != "EOF" else len(t)
t = t[:i] + new + t[j:]
open(run, "w", encoding="utf-8", newline="\n").write(t)
print("spliced", len(new), "chars")
