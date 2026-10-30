import sys,re
from bs4 import BeautifulSoup
for fn in sys.argv[1:]:
    s=open(fn,encoding='utf-8',errors='replace').read()
    soup=BeautifulSoup(s,'lxml')
    for t in soup(['script','style']): t.decompose()
    for ix in soup.find_all(re.compile('^ix:header$')): ix.decompose()
    for tr in soup.find_all('tr'):
        cells=[re.sub(r'\s+',' ',td.get_text(' ')).strip() for td in tr.find_all(['td','th'])]
        cells=[c for c in cells if c and c not in ('$','%',')','(')]
        tr.replace_with(soup.new_string('\n[ROW] '+' | '.join(cells)+'\n'))
    txt=soup.get_text('\n')
    lines=[re.sub(r'[ \t\xa0]+',' ',l).strip() for l in txt.split('\n')]
    out=[]
    for l in lines:
        if not l or l=='[ROW]': continue
        out.append(l)
    # merge short fragments
    open(fn.replace('.htm','.clean.txt'),'w',encoding='utf-8').write('\n'.join(out))
    print(fn,len(out))
