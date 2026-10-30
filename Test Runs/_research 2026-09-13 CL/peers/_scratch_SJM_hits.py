import sys, glob, re
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
for pat in sys.argv[2:]:
    for f in sorted(glob.glob(sys.argv[1])):
        s=open(f,encoding="utf-8").read()
        L=s.split("\n")
        n=len(re.findall(pat,s,re.I))
        lines=[i for i,l in enumerate(L) if re.search(pat,l,re.I)]
        print(pat, f, "matches", n, "lines", lines[:30])
