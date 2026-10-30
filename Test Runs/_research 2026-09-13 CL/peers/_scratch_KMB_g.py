import sys, re, glob
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
pat = re.compile(sys.argv[2], re.I); w=int(sys.argv[3]) if len(sys.argv)>3 else 200
for f in sorted(glob.glob(sys.argv[1])):
    L = open(f, encoding="utf-8").read().split("\n")
    hits=[i for i,l in enumerate(L) if pat.search(l)]
    print(f"=== {f}: {len(hits)}")
    for i in hits: print(i, L[i][:w])
