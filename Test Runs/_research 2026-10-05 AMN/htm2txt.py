import sys, re, html
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s): super().__init__(); s.out=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in("script","style"): s.skip+=1
        if t in("p","div","br","tr","li","h1","h2","h3","h4","table"): s.out.append("\n")
        if t in("td","th"): s.out.append(" | ")
    def handle_endtag(s,t):
        if t in("script","style"): s.skip-=1
    def handle_data(s,d):
        if not s.skip: s.out.append(d)
src=open(sys.argv[1],encoding="utf-8",errors="ignore").read()
p=P(); p.feed(src)
t="".join(p.out).replace("\xa0"," ")
t=re.sub(r"[ \t]+"," ",t); t=re.sub(r"\n\s*\n+","\n",t)
open(sys.argv[2],"w",encoding="utf-8").write(t); print(sys.argv[2], len(t))
