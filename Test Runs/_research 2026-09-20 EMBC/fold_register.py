import re, os
q = r"C:\Users\chreh\OneDrive\Documents\BRK\Screens\WATCHLIST RUN QUEUE.md"
e = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-20 EMBC\_register_entry.md"
lines = open(q, encoding="utf-8").read().split("\n")

starts = [i for i, l in enumerate(lines) if l.startswith("## COMPLETED FROM THE QUEUE")]
ends   = [i for i, l in enumerate(lines) if l.startswith("## THE WRITE-EARLY PROTOCOL")]
assert len(starts) == 1, starts
a = starts[0]; b = [x for x in ends if x > a][0]
before = sum(1 for l in lines[a:b] if re.match(r"^- \*\*", l))
assert before == 138, before
assert sum(1 for l in lines if "EMBC" in l) == 0, "EMBC already present"

entry = open(e, encoding="utf-8").read().rstrip("\n").split("\n")
lines = lines[:a+1] + entry + lines[a+1:]

starts = [i for i, l in enumerate(lines) if l.startswith("## COMPLETED FROM THE QUEUE")]
ends   = [i for i, l in enumerate(lines) if l.startswith("## THE WRITE-EARLY PROTOCOL")]
a = starts[0]; b = [x for x in ends if x > a][0]
after = sum(1 for l in lines[a:b] if re.match(r"^- \*\*", l))
assert after == before + 1, (before, after)

open(q, "w", encoding="utf-8").write("\n".join(lines))
print("register entries before:", before, " after:", after)
print("slice now lines", a+1, "to", b+1)

# roster strike: wave 7 done file
d = r"C:\Users\chreh\OneDrive\Documents\BRK\Screens\_daily\_wave7_done.txt"
txt = open(d, encoding="utf-8").read() if os.path.exists(d) else ""
print("wave7_done before:", repr(txt.split("\n")[-3:]), "lines:", len([x for x in txt.split("\n") if x.strip()]))
