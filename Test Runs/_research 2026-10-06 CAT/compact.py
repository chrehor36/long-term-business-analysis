"""Print a line range of a text extract with table cells joined. python compact.py file start end"""
import sys, re
lines = open(sys.argv[1], encoding="utf-8").read().split("\n")[int(sys.argv[2]) - 1:int(sys.argv[3])]
s = " ".join(l.strip() for l in lines)
s = s.replace("​", "")
s = re.sub(r"(\|\s*)+", "| ", s)
s = re.sub(r"\s+", " ", s)
print(s)
