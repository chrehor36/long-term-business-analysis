"""Verify that each quoted phrase occurs in the given text file, whitespace-normalised. usage: python qcheck.py file 'phrase' ..."""
import sys, re
t = re.sub(r"\s+", " ", open(sys.argv[1], encoding="utf-8", errors="ignore").read().replace("’", "'").replace("“", '"').replace("”", '"'))
for p in sys.argv[2:]:
    q = re.sub(r"\s+", " ", p.replace("’", "'"))
    i = t.find(q)
    print("FOUND" if i >= 0 else "MISSING", "|", q[:90])
