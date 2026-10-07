import sys, re, html
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.out=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in ('script','style'): s.skip+=1
        if t in ('p','div','tr','br','li','h1','h2','h3','h4','table'): s.out.append('\n')
        if t in ('td','th'): s.out.append(' | ')
    def handle_endtag(s,t):
        if t in ('script','style'): s.skip-=1
    def handle_data(s,d):
        if not s.skip: s.out.append(d)
raw=open(sys.argv[1],'rb').read().decode('utf-8','ignore')
raw=re.sub(r'(?is)<ix:header>.*?</ix:header>','',raw)
p=P(); p.feed(raw)
t=''.join(p.out).replace('\xa0',' ')
t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
open(sys.argv[2],'w',encoding='utf-8').write(t); print(sys.argv[2], len(t))
