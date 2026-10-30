import re, sys
sys.stdout.reconfigure(encoding="utf-8")
f, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
lines = open(f, encoding="utf-8").read().split("\n")[a - 1:b]
t = " ".join(lines)
t = re.sub(r"[   \xa0]", " ", t)
toks = [x.strip() for x in t.split("|")]
out, cur = [], []
for x in toks:
    x = re.sub(r"\s+", " ", x)
    if x in ("", "$", "—$", "¥"):
        continue
    if x == ")" and cur:
        cur[-1] = cur[-1] + ")"
        continue
    if re.search(r"[A-Za-z]{2,}", x):
        if cur:
            out.append(" | ".join(cur))
        cur = [x]
    else:
        cur.append(x)
if cur:
    out.append(" | ".join(cur))
w = int(sys.argv[4]) if len(sys.argv) > 4 else 400
for o in out:
    print(o[:w])
