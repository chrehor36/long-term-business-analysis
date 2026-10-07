import sys, re
from bs4 import BeautifulSoup

def clean(s):
    s = s.replace('\u00a0',' ').replace('\u2019',"'").replace('\u2014','-').replace('\u2013','-')
    s = re.sub(r'\s+',' ',s).strip()
    return s

def conv(path,out):
    html=open(path,encoding='utf-8',errors='replace').read()
    soup=BeautifulSoup(html,'lxml')
    for t in soup(['script','style']): t.decompose()
    lines=[]
    # replace tables with marker text
    for tbl in soup.find_all('table'):
        rows=[]
        for tr in tbl.find_all('tr'):
            cells=[clean(td.get_text(' ')) for td in tr.find_all(['td','th'])]
            cells=[c for c in cells if c not in ('',)]
            if cells: rows.append(' | '.join(cells))
        marker="\n<TABLE>\n"+"\n".join(rows)+"\n</TABLE>\n"
        tbl.replace_with(soup.new_string(marker))
    text=soup.get_text('\n')
    text=text.replace('\u00a0',' ').replace('\u2019',"'")
    outl=[]
    for ln in text.split('\n'):
        ln=re.sub(r'[ \t]+',' ',ln).strip()
        if ln: outl.append(ln)
    open(out,'w',encoding='utf-8').write('\n'.join(outl))
    print(out, len(outl),'lines')

conv(sys.argv[1],sys.argv[2])
