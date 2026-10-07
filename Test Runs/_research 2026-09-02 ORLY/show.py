#!/usr/bin/env python3
"""Slice/grep a converted 10-K text file, ASCII-safe for a cp1252 console."""
import sys, os, re

OUT = os.path.dirname(os.path.abspath(__file__))

def clean(s):
    s = s.replace("​", "").replace(" ", " ")
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("—", "--").replace("–", "-")
    s = re.sub(r"\n\s*\|\s*\n", " | ", s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.encode("ascii", "replace").decode("ascii")

def load(name):
    p = os.path.join(OUT, name)
    return open(p, encoding="utf-8").read()

if __name__ == "__main__":
    cmd = sys.argv[1]
    name = sys.argv[2]
    t = load(name)
    if cmd == "slice":
        a, b = int(sys.argv[3]), int(sys.argv[4])
        print(clean(t[a:b]))
    elif cmd == "find":
        pat = sys.argv[3]
        before = int(sys.argv[4]) if len(sys.argv) > 4 else 200
        after = int(sys.argv[5]) if len(sys.argv) > 5 else 600
        n = 0
        for m in re.finditer(pat, t, re.I):
            n += 1
            print("\n@@@ %d @@@" % m.start())
            print(clean(t[max(0, m.start() - before):m.start() + after]))
            if n > 25:
                print("... more matches suppressed")
                break
        if n == 0:
            print("NO MATCH for", pat)
    elif cmd == "len":
        print(len(t))
