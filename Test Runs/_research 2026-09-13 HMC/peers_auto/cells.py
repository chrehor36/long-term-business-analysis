"""Collapse a stripped filing text into a stream of non-empty cells and print windows
around anchor strings. Transcription aid only: prints what is in the file.
usage: python cells.py FILE ANCHOR [before] [after] [maxhits]"""
import re, sys

f, anchor = sys.argv[1], sys.argv[2]
before = int(sys.argv[3]) if len(sys.argv) > 3 else 5
after = int(sys.argv[4]) if len(sys.argv) > 4 else 40
maxhits = int(sys.argv[5]) if len(sys.argv) > 5 else 10
txt = open(f, encoding="utf-8", errors="replace").read()
raw = re.split(r"[|\n]", txt)
cells = []
for c in raw:
    c = " ".join(c.split())
    if not c:
        continue
    if c == ")" and cells:
        cells[-1] = cells[-1] + ")"
        continue
    cells.append(c)
hits = [i for i, c in enumerate(cells) if anchor in c]
print(f"{len(hits)} hits for {anchor!r}")
for i in hits[:maxhits]:
    print("-----", i)
    print(" | ".join(cells[max(0, i - before): i + after]))
