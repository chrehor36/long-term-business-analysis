import sys, re, html
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s): super().__init__(); s.out=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in('script','style'): s.skip+=1
        if t in('p','div','br','tr','li','h1','h2','h3','h4','table'): s.out.append('\n')
        if t in('td','th'): s.out.append(' | ')
    def handle_endtag(s,t):
        if t in('script','style'): s.skip-=1
    def handle_data(s,d):
        if not s.skip: s.out.append(d)
for f in sys.argv[1:]:
    raw=open(f,encoding='utf-8',errors='replace').read()
    raw=re.sub(r'<ix:header>.*?</ix:header>','',raw,flags=re.S)
    p=P(); p.feed(raw)
    t=''.join(p.out).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(f.rsplit('.',1)[0]+'.txt','w',encoding='utf-8').write(t)
    print(f, len(t))
