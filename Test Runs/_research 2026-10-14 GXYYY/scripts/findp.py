import sys, fitz
sys.stdout.reconfigure(encoding='utf-8')
d=fitz.open(sys.argv[1])
for i,p in enumerate(d):
    t=p.get_text()[:400].upper()
    for h in sys.argv[2:]:
        if h.upper() in t: print(i,h)
