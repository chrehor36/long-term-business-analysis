import sys, glob, re
sys.path.insert(0, ".")
from _scratch_GIS_lib import load
pat = sys.argv[2]
for f in sorted(glob.glob(sys.argv[1])):
    s, lmap = load(f)
    for m in re.finditer(pat, s, re.I):
        print(f, lmap[m.start()], "::", s[max(0, m.start()-250):m.end()+200].replace("\n", " "))
        print()
