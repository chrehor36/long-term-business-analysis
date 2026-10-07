import pymupdf, sys, re
pdf=sys.argv[1]; pats=[re.compile(p,re.I) for p in sys.argv[2:]]
doc=pymupdf.open(pdf)
for i,p in enumerate(doc):
    # sentence-level: join blocks
    for b in p.get_text("blocks"):
        t=re.sub(r'\s+',' ',b[4]).strip()
        for pt in pats:
            if pt.search(t):
                print(f"[p{i+1}] {t[:1500]}\n"); break
