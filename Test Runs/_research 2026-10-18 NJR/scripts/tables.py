import sys,re,warnings
warnings.filterwarnings('ignore')
from bs4 import BeautifulSoup
f=sys.argv[1]; kw=[k.lower() for k in sys.argv[2].split('|')]; maxn=int(sys.argv[3]) if len(sys.argv)>3 else 50
s=BeautifulSoup(open(f,'rb').read(),'lxml')
n=0
for i,t in enumerate(s.find_all('table')):
    rows=[]
    for tr in t.find_all('tr'):
        cells=[re.sub(r'\s+',' ',td.get_text(' ',strip=True)) for td in tr.find_all(['td','th'])]
        cells=[c for c in cells if c and c not in ('$',')','%')]
        if cells: rows.append(' | '.join(cells))
    txt='\n'.join(rows)
    if all(k in txt.lower() for k in kw):
        print(f'=== table {i}'); print(txt); n+=1
        if n>=maxn: break
