import sys, os, re, json
sys.path.insert(0,'tools')
import sources as S
from html.parser import HTMLParser

R = 'Test Runs/_research 2026-09-19 SOFI/'
CIK = '1818874'

class T(HTMLParser):
    def __init__(self):
        super().__init__(); self.out=[]; self.skip=0
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style'): self.skip+=1
        if tag in ('p','div','tr','br','table','h1','h2','h3','li'): self.out.append('\n')
        if tag in ('td','th'): self.out.append(' | ')
    def handle_endtag(self, tag):
        if tag in ('script','style') and self.skip: self.skip-=1
    def handle_data(self, d):
        if not self.skip: self.out.append(d)

def totext(html):
    p=T(); p.feed(html)
    t=''.join(p.out)
    t=t.replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t)
    t=re.sub(r'\n\s*\n+','\n',t)
    return t

def grab(acc, doc, name):
    a=acc.replace('-','')
    url=f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{doc}'
    h=S._get(url, headers=S.SEC_UA)
    open(R+name+'.txt','w',encoding='utf-8').write(totext(h))
    print(name, len(h), '->', os.path.getsize(R+name+'.txt'))

def index(acc):
    a=acc.replace('-','')
    j=json.loads(S._get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json', headers=S.SEC_UA))
    return [(i['name'], i.get('size')) for i in j['directory']['item']]

if __name__=='__main__':
    for arg in sys.argv[1:]:
        parts=arg.split(':')
        if parts[0]=='idx':
            print(parts[1]); [print('   ',n,s) for n,s in index(parts[1])]
        else:
            grab(parts[0], parts[1], parts[2])
