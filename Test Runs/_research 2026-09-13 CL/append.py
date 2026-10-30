"""Append a section file to the run file, optionally replacing a placeholder. Usage: python append.py section.md [placeholder]"""
import sys
RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - CL Colgate-Palmolive.md"
sec = open(sys.argv[1], encoding="utf-8").read()
t = open(RUN, encoding="utf-8").read()
if len(sys.argv) > 2 and sys.argv[2] in t:
    t = t.replace(sys.argv[2], "")
t = t.rstrip("\n") + "\n\n" + sec.rstrip("\n") + "\n"
open(RUN, "w", encoding="utf-8").write(t)
print("appended", len(sec), "chars; run file now", len(t))
