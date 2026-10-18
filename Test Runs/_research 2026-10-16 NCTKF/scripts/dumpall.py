import sys,io,pymupdf as fitz
fn=sys.argv[1]; out=sys.argv[2]
d=fitz.open(fn)
with open(out,'w',encoding='utf-8') as f:
  for pg,p in enumerate(d):
    ws=p.get_text("words"); rows={}
    for w in ws: rows.setdefault(round((w[1]+w[3])/2/3),[]).append(w)
    f.write(f"===== page {pg}\n")
    for k in sorted(rows):
        r=sorted(rows[k],key=lambda w:w[0]); line=""; lastx=0
        for w in r:
            gap=int((w[0]-lastx)/5)
            line+=(" "*max(1,gap) if line else " "*int(w[0]/5))+w[4]; lastx=w[2]
        f.write(line+"\n")
