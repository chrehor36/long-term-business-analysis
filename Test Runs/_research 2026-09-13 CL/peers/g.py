"""grep helper: python g.py GLOB PATTERN [ctx] [maxhits]  |  python g.py FILE --lines START END"""
import sys, re, glob, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if len(sys.argv) > 2 and sys.argv[2] == "--lines":
    L = open(sys.argv[1], encoding="utf-8").read().split("\n")
    a, b = int(sys.argv[3]), int(sys.argv[4])
    for i in range(a, min(b, len(L))):
        print(i, L[i][:1500])
    sys.exit()
pat = re.compile(sys.argv[2], re.I)
ctx = int(sys.argv[3]) if len(sys.argv) > 3 else 0
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 40
for f in sorted(glob.glob(sys.argv[1])):
    L = open(f, encoding="utf-8").read().split("\n")
    hits = [i for i, l in enumerate(L) if pat.search(l)]
    print(f"=== {f}: {len(hits)} hits")
    last = -1
    for i in hits[:mx]:
        for j in range(max(0, i - ctx, last + 1), min(len(L), i + ctx + 1)):
            print(j, L[j][:1200])
        last = i + ctx
        if ctx:
            print("--")
