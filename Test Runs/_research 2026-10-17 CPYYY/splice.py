# splice a section file into the run file: replace text from the line starting with START up to (not including) END
import sys
run = "Test Runs/2026-10-17 Run - CPYYY Centrica.md"
sec, start, end = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(run, encoding="utf-8").read()
new = open(sec, encoding="utf-8").read()
i = s.index(start)
j = s.index(end, i + 1) if end != "EOF" else len(s)
s = s[:i] + new.rstrip("\n") + "\n\n" + s[j:]
open(run, "w", encoding="utf-8").write(s)
print("spliced", sec, len(new))
