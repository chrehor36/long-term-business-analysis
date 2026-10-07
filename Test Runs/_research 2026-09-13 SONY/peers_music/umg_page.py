import pymupdf, sys
pdf=sys.argv[1]
doc=pymupdf.open(pdf)
for n in sys.argv[2:]:
    p=doc[int(n)-1]
    print("=====PAGE",n, p.rect)
    # split into left/right columns by x, sort blocks by y
    words=p.get_text("words")
    mid=p.rect.width/2
    for side,cond in (("LEFT",lambda w:w[0]<mid),("RIGHT",lambda w:w[0]>=mid)):
        lines={}
        for w in words:
            if cond(w):
                key=(round(w[3]/3),)
                lines.setdefault(key,[]).append(w)
        print("---",side)
        for k in sorted(lines):
            ws=sorted(lines[k],key=lambda w:w[0])
            print(" ".join(w[4] for w in ws))
