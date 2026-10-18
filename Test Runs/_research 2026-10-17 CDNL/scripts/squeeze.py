# print a line range of a text file with table cells joined onto one line
import io; sys_ = __import__("sys"); sys_.stdout.reconfigure(encoding="utf-8", errors="replace")
import sys
p, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
L = open(p, encoding="utf-8").read().split("\n")[a-1:b]
out, buf = [], []
for s in L:
    t = s.strip()
    if t in ("|", ""): 
        continue
    if len(t) < 60:
        buf.append(t)
    else:
        if buf: out.append(" ".join(buf)); buf = []
        out.append(t)
if buf: out.append(" ".join(buf))
for o in out:
    o = o.replace(" | ", " ").replace("$ ", "$")
    print(o)
