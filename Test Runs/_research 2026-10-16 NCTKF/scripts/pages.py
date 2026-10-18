import sys,io,fitz
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
fn=sys.argv[1]; pat=sys.argv[2].lower()
d=fitz.open(fn)
for i,p in enumerate(d):
    t=p.get_text()
    if pat in t.lower(): print(i, t.strip().split('\n')[-1][:40].replace('\n',' '))
