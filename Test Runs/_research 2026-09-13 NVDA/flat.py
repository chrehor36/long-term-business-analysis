"""Flatten a broken-line filed statement (FY2017/FY2019 10-K renderer splits cells) for reading. Transcription aid only."""
import re, sys
f, head, stop = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(f, encoding="utf-8").read()
i = [m.start() for m in re.finditer(head, t)][-1]
j = t.find(stop, i)
s = t[i:j]
s = re.sub(r"\s*\|\s*", " | ", s)
s = re.sub(r"\s+", " ", s)
s = re.sub(r"(\|\s*)+", "| ", s)
s = re.sub(r" (?=[A-Z][a-z])", "\n", s)
print(s)
