import sys, re, html
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s): super().__init__(); s.o=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in("script","style"): s.skip+=1
        if t in("p","div","tr","br","li","h1","h2","h3","h4","table"): s.o.append("\n")
        if t in("td","th"): s.o.append(" | ")
    def handle_endtag(s,t):
        if t in("script","style"): s.skip-=1
    def handle_data(s,d):
        if not s.skip: s.o.append(d)
src,out=sys.argv[1],sys.argv[2]
raw=open(src,encoding="utf-8",errors="replace").read()
raw=re.sub(r"<ix:header>.*?</ix:header>","",raw,flags=re.S)
p=P(); p.feed(raw)
t="".join(p.o).replace("\xa0"," ")
t=re.sub(r"[ \t]+"," ",t); t=re.sub(r"\n\s*\n+","\n",t)
open(out,"w",encoding="utf-8").write(t); print(out,len(t))
