import re, sys, os
sys.stdout.reconfigure(encoding="utf-8")
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
pat = re.compile(sys.argv[1], re.I)
for f in sys.argv[2:]:
    t = open(os.path.join(D, f + ".flat.txt"), encoding="utf-8").read().replace("​", "")
    print("===", f)
    for s in re.split(r"(?<=[a-z0-9\)%])\.\s+(?=[A-Z])|\n", t):
        if pat.search(s):
            print("  *", s.strip()[:900])
