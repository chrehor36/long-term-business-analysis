"""grab.py FILE PATTERN [AFTER_CHARS] [MAX_HITS] - flatten a filing text and print each hit with context.
Reading aid only; the text printed is the filed text, flattened."""
import re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
fn, pat = sys.argv[1], sys.argv[2]
after = int(sys.argv[3]) if len(sys.argv) > 3 else 600
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 5
raw = open(os.path.join(HERE, fn), encoding="utf-8").read()
flat = " ".join(l.strip() for l in raw.split("\n") if l.strip() not in ("", "|"))
flat = re.sub(r" \| ", " ", flat)
flat = re.sub(r"\s+", " ", flat).replace("( ", "(").replace(" )", ")")
n = 0
for m in re.finditer(pat, flat, flags=re.I):
    print("--", m.start(), ":", flat[max(0, m.start() - 80): m.start() + after])
    n += 1
    if n >= mx:
        break
print("hits shown", n)
