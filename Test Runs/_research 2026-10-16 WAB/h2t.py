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
for a in range(1,len(sys.argv),2):
    p=P(); p.feed(open(sys.argv[a],encoding="utf-8",errors="ignore").read())
    t="".join(p.o); t=re.sub(r"[ \t\xa0]+"," ",t); t=re.sub(r"\n\s*\n+","\n",t)
    open(sys.argv[a+1],"w",encoding="utf-8").write(t)
