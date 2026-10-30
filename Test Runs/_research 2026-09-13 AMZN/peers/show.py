"""show.py FILE START END  -> collapse a line range, dropping empty table cells.
   show.py FILE -g REGEX [N]  -> print collapsed context of N lines after each match."""
import sys, re

def collapse(lines):
    out = []
    for l in lines:
        s = l.replace("|", " ").strip()
        if not s:
            continue
        out.append(s)
    txt = " ".join(out)
    return re.sub(r"\s+", " ", txt)

f = sys.argv[1]
L = open(f, encoding="utf-8", errors="replace").read().split("\n")
if sys.argv[2] == "-g":
    n = int(sys.argv[4]) if len(sys.argv) > 4 else 40
    mx = int(sys.argv[5]) if len(sys.argv) > 5 else 20
    k = 0
    for i, l in enumerate(L):
        if re.search(sys.argv[3], l, re.I):
            print(f"@{i+1}:", collapse(L[i:i+n])[:3000])
            print()
            k += 1
            if k >= mx:
                break
else:
    a, b = int(sys.argv[2]), int(sys.argv[3])
    print(collapse(L[a-1:b]))
