import sys, re, os
src = sys.argv[1]
s = open(src, encoding="utf-8").read()
s = s.replace("\n", " ")
s = re.sub(r"\s*\|\s*", " ", s)
s = re.sub(r"\s+", " ", s)
s = re.sub(r"(?<=[.;:]) (?=[A-Z])", "\n", s)
open(src.replace(".txt", ".flat"), "w", encoding="utf-8").write(s)
