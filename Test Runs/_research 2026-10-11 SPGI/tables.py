"""Print HTML table rows compactly. Usage: tables.py FILE [grep-regex] """
import sys,re,html,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
t=open(sys.argv[1],'rb').read().decode('utf-8','replace')
pat=re.compile(sys.argv[2],re.I) if len(sys.argv)>2 else None
for tr in re.findall(r'(?is)<tr.*?</tr>',t):
    cells=[]
    for td in re.findall(r'(?is)<t[dh][^>]*>(.*?)</t[dh]>',tr):
        s=html.unescape(re.sub(r'<[^>]+>',' ',td)).replace('\xa0',' ')
        s=re.sub(r'\s+',' ',s).strip()
        if s and s not in ('$',')','%'): cells.append(s)
    line=' | '.join(cells).replace('( ','(').replace(' |)',')')
    if line and (not pat or pat.search(line)): print(line)
