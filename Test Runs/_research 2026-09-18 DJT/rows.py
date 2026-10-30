import re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
fn, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
L = open(fn, encoding="utf-8").read().split("\n")[a-1:b]
out = []; cur = ""
num = re.compile(r"^[\s\|\$\(\)\-–—%\*,\.\d]*$")
for l in L:
    s = l.strip().strip("|").strip()
    if not s: continue
    if num.match(s) and cur:
        cur += " " + s.replace("|","").replace(" ","")
    else:
        if cur: out.append(cur)
        cur = s
out.append(cur)
print("\n".join(out))
