import sys, re
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.out=[]; s.skip=0; s.intd=0; s.cell=[]; s.row=None
    def handle_starttag(s,t,a):
        if t in ("script","style"): s.skip+=1
        if t=="tr": s.row=[]
        elif t in ("td","th"): s.intd+=1; s.cell=[]
        elif t in ("p","div","br","h1","h2","h3","h4","li","table") and not s.intd: s.out.append("\n")
    def handle_endtag(s,t):
        if t in ("script","style"): s.skip-=1
        if t in ("td","th") and s.intd:
            s.intd-=1
            c=re.sub(r"\s+"," ","".join(s.cell)).strip()
            if s.row is not None and c: s.row.append(c)
        if t=="tr" and s.row is not None:
            r=" | ".join(s.row)
            # glue "$" and "%" and ")" cells
            r=re.sub(r"\$ \| ","$",r); r=re.sub(r" \| (%|\))", r"\1", r)
            s.out.append("\n"+r+"\n"); s.row=None
    def handle_data(s,d):
        if s.skip: return
        if s.intd: s.cell.append(d)
        else: s.out.append(d)
for f in sys.argv[1:]:
    raw=open(f,encoding="utf-8",errors="replace").read()
    p=P(); p.feed(raw)
    t="".join(p.out).replace("\xa0"," ")
    t=re.sub(r"[ \t]+"," ",t); t=re.sub(r"\n\s*\n+","\n",t)
    open(f.rsplit(".",1)[0]+".txt","w",encoding="utf-8").write(t)
    print(f, len(t))
