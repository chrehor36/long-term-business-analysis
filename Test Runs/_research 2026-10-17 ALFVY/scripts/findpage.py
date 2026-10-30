import sys, site; sys.path.append(site.getusersitepackages()); sys.stdout.reconfigure(encoding="utf-8")
import fitz
f = sys.argv[1]; pats = sys.argv[2:]
d = fitz.open(f)
for i in range(d.page_count):
    t = d[i].get_text()
    if all(p.lower() in t.lower() for p in pats):
        print(i + 1)
