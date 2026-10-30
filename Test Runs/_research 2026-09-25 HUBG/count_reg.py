import re, sys
L = open(sys.argv[1], encoding="utf-8").read().split("\n")
h = [i for i, l in enumerate(L) if l.rstrip("\r") == "## COMPLETED FROM THE QUEUE"]
e = [i for i, l in enumerate(L) if l.startswith("## THE WRITE-EARLY PROTOCOL")]
assert len(h) == 1 and len(e) == 1, (h, e)
ent = [(h[0] + i + 1, l[:110]) for i, l in enumerate(L[h[0]:e[0]]) if re.match(r"^- \*\*", l)]
print("heading line", h[0] + 1, "end line", e[0] + 1, "entries", len(ent))
for x in ent[-3:]: print(x)
print("HUBG entries:", [x for x in ent if "HUBG" in x[1]])
