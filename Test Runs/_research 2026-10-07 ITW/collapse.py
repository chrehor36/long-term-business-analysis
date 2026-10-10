# Print a collapsed window of a cached filing text around the n-th occurrence of a keyword (table cells joined).
import re, sys, os
f, kw = sys.argv[1], sys.argv[2]
n = int(sys.argv[3]) if len(sys.argv) > 3 else 0
before = int(sys.argv[4]) if len(sys.argv) > 4 else 20
after = int(sys.argv[5]) if len(sys.argv) > 5 else 300
L = open(os.path.join(os.path.dirname(__file__), "cache", f), encoding="utf-8").read().split("\n")
hits = [i for i, l in enumerate(L) if kw.lower() in l.lower()]
print("hits:", hits[:40])
if hits:
    i = hits[min(n, len(hits) - 1)]
    s = " ".join(t.strip() for t in L[max(0, i - before):i + after])
    s = s.replace("​", " ")
    s = re.sub(r"(\s*\|\s*)+", " | ", s)
    s = re.sub(r"\s+", " ", s)
    sys.stdout.buffer.write(s[:7000].encode("utf-8", "replace") + b"\n")
