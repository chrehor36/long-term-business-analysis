# Stitch the run file: written parts + the template remainder from a marker. Run: python assemble.py "<marker>" part1.md part2.md ...
import sys, io
T = open(r"C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/_TEMPLATE - Company Run.md", encoding="utf-8").read()
OUT = r"C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-09-18 Run - SMCI Super Micro Computer.md"
marker = sys.argv[1]
parts = [open(p, encoding="utf-8").read().rstrip() + "\n" for p in sys.argv[2:]]
rest = T[T.index(marker):] if marker != "NONE" else ""
body = "\n".join(parts) + ("\n" + rest if rest else "")
open(OUT, "w", encoding="utf-8", newline="\n").write(body)
print("wrote", len(body), "chars")
