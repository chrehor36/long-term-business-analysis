# print page text reconstructed by rows (words grouped by y)
import sys,io,fitz
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
fn=sys.argv[1]
d=fitz.open(fn)
for pg in sys.argv[2:]:
    p=d[int(pg)]
    ws=p.get_text("words")
    rows={}
    for w in ws:
        key=round((w[1]+w[3])/2/3)
        rows.setdefault(key,[]).append(w)
    print(f"===== page {pg}")
    for k in sorted(rows):
        r=sorted(rows[k],key=lambda w:w[0])
        line=""; lastx=0
        for w in r:
            gap=int((w[0]-lastx)/5)
            line+=(" "*max(1,gap) if line else " "*int(w[0]/5))+w[4]; lastx=w[2]
        print(line)
