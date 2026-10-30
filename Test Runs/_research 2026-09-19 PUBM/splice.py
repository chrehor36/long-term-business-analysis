# Replace a section of the run file between two heading markers with the content of a file.
import sys, io
run = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-19 Run - PUBM PubMatic.md"
start, end, src = sys.argv[1], sys.argv[2], sys.argv[3]
t = io.open(run, encoding="utf-8").read()
i = t.index(start); j = t.index(end, i + len(start)) if end != "EOF" else len(t)
new = io.open(src, encoding="utf-8").read().rstrip("\n") + "\n\n"
t = t[:i] + new + t[j:]
io.open(run, "w", encoding="utf-8", newline="\n").write(t)
print("spliced", src, len(new))
