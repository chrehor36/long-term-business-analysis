import pymupdf, sys
for name in ["UMG_AR_2025","UMG_AR_2024"]:
    doc=pymupdf.open("cache/"+name+".pdf")
    out=[]
    for i,p in enumerate(doc):
        words=p.get_text("words"); mid=p.rect.width/2
        for cond in (lambda w:w[0]<mid, lambda w:w[0]>=mid):
            lines={}
            for w in words:
                if cond(w): lines.setdefault(round(w[3]/3),[]).append(w)
            for k in sorted(lines):
                out.append(" ".join(w[4] for w in sorted(lines[k],key=lambda w:w[0])))
        out.append(f"=== page {i+1}")
    open(name+".cols.txt","w",encoding="utf-8").write("\n".join(out))
    print(name,len(out))
