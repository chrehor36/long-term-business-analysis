# Collapse the pipe-fragmented text of an EDGAR filing into one line per table row.
# usage: python rows.py FILE START END   (line numbers in the raw text)
import sys, re
sys.stdout.reconfigure(encoding="utf-8")
f, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
L = open(f, encoding="utf-8").read().split("\n")[a-1:b]
out, cur = [], None
num = re.compile(r"^[\s|$%()—,.\-\d]*$")
for x in L:
    s = x.strip()
    if not s or s == "|": continue
    if num.match(s):
        if cur is not None: cur.append(s.replace("|", "").strip())
    else:
        if cur is not None: out.append(cur)
        cur = [s.rstrip("|").strip()]
if cur: out.append(cur)
for r in out:
    vals = [v for v in r[1:] if v and v != "$"]
    print(r[0], "|", " ".join(vals))
