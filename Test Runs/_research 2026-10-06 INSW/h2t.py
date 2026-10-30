import sys,re
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.o=[]; s.skip=0; s.tab=0
    def handle_starttag(s,t,a):
        if t in('script','style'): s.skip+=1
        if t=='table': s.tab+=1; s.o.append('\n')
        if t=='tr': s.o.append('\n')
        elif t in('td','th'): s.o.append(' | ')
        elif t in('p','div','br','li','h1','h2','h3','h4') and not s.tab: s.o.append('\n')
    def handle_endtag(s,t):
        if t in('script','style'): s.skip-=1
        if t=='table': s.tab=max(0,s.tab-1); s.o.append('\n')
    def handle_data(s,d):
        if not s.skip: s.o.append(d.replace(chr(10)," ") if s.tab else d)
def conv(src,dst):
    t=open(src,encoding='utf-8',errors='ignore').read()
    p=P(); p.feed(t)
    x=''.join(p.o).replace('\xa0',' ').replace('​','')
    x=re.sub(r'[ \t]+',' ',x)
    x=re.sub(r'\|(\s*\|)+','|',x)
    x=re.sub(r'\$ \|','$',x)
    x=re.sub(r'\n\s*\n+','\n',x)
    open(dst,'w',encoding='utf-8').write(x)
if __name__=='__main__': conv(sys.argv[1],sys.argv[2])
