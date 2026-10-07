import sys, re, os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
# usage: kwic.py FILESTEM "regex" [before] [after] [maxhits] [skip]
D = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(D, sys.argv[1] + ".txt"), encoding="utf-8").read()
t = re.sub(r"\s*\n\s*", " ", t)
t = re.sub(r"(\|\s*)+\|", "|", t)
t = re.sub(r"\$\s*\|\s*", "$", t)
pat = re.compile(sys.argv[2], re.I)
b = int(sys.argv[3]) if len(sys.argv) > 3 else 100
a = int(sys.argv[4]) if len(sys.argv) > 4 else 400
mx = int(sys.argv[5]) if len(sys.argv) > 5 else 10
skip = int(sys.argv[6]) if len(sys.argv) > 6 else 0
n = 0; k = 0
for mm in pat.finditer(t):
    k += 1
    if k <= skip: continue
    s = max(0, mm.start() - b); e = min(len(t), mm.end() + a)
    print(f"--- #{k} @{mm.start()}")
    print(t[s:e])
    n += 1
    if n >= mx: break
print("hits shown", n, "total>=", k)
