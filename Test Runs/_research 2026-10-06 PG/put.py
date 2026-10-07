"""Replace one section of the run file. Usage: python put.py "<heading prefix>" <section text file>
The section runs from the line starting with the heading prefix to the next line starting with '## ' (or '---')."""
import sys, os

RUN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "2026-10-06 Run - PG Procter & Gamble.md")
prefix, src = sys.argv[1], sys.argv[2]
lines = open(RUN, encoding="utf-8").read().split("\n")
start = next(i for i, l in enumerate(lines) if l.startswith(prefix))
end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ") or lines[i] == "---"), len(lines))
new = open(src, encoding="utf-8").read().rstrip("\n").split("\n") + [""]
lines[start:end] = new
open(RUN, "w", encoding="utf-8").write("\n".join(lines))
print("replaced lines", start + 1, "to", end, "with", len(new))
