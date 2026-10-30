import pymupdf, sys
pdf, kw = sys.argv[1], sys.argv[2:]
doc=pymupdf.open(pdf)
for i,p in enumerate(doc):
    t=p.get_text("text")
    if all(k.lower() in t.lower() for k in kw):
        print("PAGE",i+1)
