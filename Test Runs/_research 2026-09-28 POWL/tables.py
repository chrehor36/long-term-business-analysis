# flatten a filing so each table row is one line: cells joined by ' | ', empty cells dropped
import re, os, sys, json, html as H
from fetch import get
def flat(b):
    s=b.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'(?is)<ix:header>.*?</ix:header>',' ',s)
    out=[]
    # split into tables and non-table text
    pos=0
    for m in re.finditer(r'(?is)<table.*?</table>', s):
        pre=s[pos:m.start()]; pos=m.end()
        t=re.sub(r'(?is)</(p|div|h\d|li)>|<br[^>]*>','\n',pre); t=re.sub(r'(?s)<[^>]+>',' ',t)
        out.append(H.unescape(t))
        for tr in re.findall(r'(?is)<tr.*?</tr>', m.group(0)):
            cells=[H.unescape(re.sub(r'(?s)<[^>]+>',' ',c)) for c in re.findall(r'(?is)<t[dh][^>]*>(.*?)</t[dh]>', tr)]
            cells=[re.sub(r'[\s\xa0]+',' ',c).strip() for c in cells]
            cells=[c for c in cells if c not in ('','$','%',')')]
            if cells: out.append(' | '.join(cells))
    t=re.sub(r'(?is)</(p|div|h\d|li)>|<br[^>]*>','\n',s[pos:]); t=re.sub(r'(?s)<[^>]+>',' ',t); out.append(H.unescape(t))
    txt='\n'.join(out)
    txt=re.sub(r'[ \t\xa0]+',' ',txt); txt=re.sub(r'\n\s*\n+','\n',txt)
    return txt
if __name__=='__main__':
    rows=[l.split() for l in open('annual_list.txt')]
    for rep, form, fd, acc, doc, cik in rows:
        if form!='10-K': continue
        out=f'cache/t{rep[:4]}.txt'
        if os.path.exists(out): continue
        raw=f'cache/raw{rep[:4]}.htm'
        if os.path.exists(raw): b=open(raw,'rb').read()
        else:
            b=get(f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/{doc}'); open(raw,'wb').write(b)
        open(out,'w',encoding='utf-8').write(flat(b)); print(out)
