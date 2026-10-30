"""Search the cached filing texts for regex patterns; print each distinct sentence-length hit per file.
Usage: python -I grepall.py <cachedir> <regex> [files...]
"""
import re, sys, os

cache = sys.argv[1]
pat = re.compile(sys.argv[2], re.I)
files = sys.argv[3:] or sorted(f[:-4] for f in os.listdir(cache) if f.endswith(".txt"))
for f in files:
    t = open(os.path.join(cache, f + ".txt"), encoding="utf-8").read()
    seen = set()
    print("===", f)
    for m in pat.finditer(t):
        s = max(0, t.rfind(".", 0, m.start()) + 1)
        e = t.find(". ", m.end())
        e = len(t) if e < 0 else e + 1
        frag = " ".join(t[s:e].split())[:600]
        if frag not in seen:
            seen.add(frag)
            print("  -", frag)
