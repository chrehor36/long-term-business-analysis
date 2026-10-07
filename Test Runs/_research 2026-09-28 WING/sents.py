import re, sys, glob
import sys; sys.stdout.reconfigure(encoding="utf-8")
pat = re.compile(sys.argv[1], re.I)
files = sys.argv[2:] if len(sys.argv) > 2 else sorted(glob.glob('cache/k20*.txt')) + ['cache/q2603.txt', 'cache/q2606.txt', 'cache/ipo424b4.txt']
for fn in files:
    t = open(fn, encoding='utf-8').read()
    t = re.sub(r'\s+', ' ', t)
    seen = set()
    for s in re.split(r'(?<=[.;])\s+(?=[A-Z(•])', t):
        if pat.search(s) and s not in seen:
            seen.add(s)
            print(f'[{fn[6:-4]}]', s[:900])
