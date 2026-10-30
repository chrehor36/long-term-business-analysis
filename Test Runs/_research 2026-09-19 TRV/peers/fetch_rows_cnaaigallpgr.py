# table-row-aware HTML-to-text: one line per <tr>, cells joined by ' | ', empty cells dropped.
import json, sys, re, html, os
sys.path.insert(0,'.')
from fetch10k import get
def cell(s):
    s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s).replace('\xa0',' ')
    return re.sub(r'\s+',' ',s).strip()
def totext(b):
    t=b.decode('utf-8','ignore')
    t=re.sub(r'(?is)<(script|style).*?</\1>','',t)
    t=re.sub(r'(?is)<ix:header>.*?</ix:header>','',t)
    def row(m):
        cells=[cell(c) for c in re.findall(r'(?is)<t[dh][^>]*>(.*?)</t[dh]>',m.group(0))]
        cells=[c for c in cells if c not in ('','$','%',')')]
        return '\n'+' | '.join(cells)+'\n'
    t=re.sub(r'(?is)<tr[^>]*>.*?</tr>',row,t)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</h\d>','\n',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    return t
if __name__=='__main__':
    # args: tk cik acc fy docname suffix
    tk,cik,acc,fy,doc,suf,fd=(sys.argv[1:8]+[""])[:7]
    u=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
    t=totext(get(u))
    fn=f"raw/{tk}_10K_FY{fy}{suf}.txt"
    open(fn,'w',encoding='utf-8').write(f"SOURCE: 10-K filed {fd} document {doc} accession {acc} url {u}\n"+t)
    print('wrote',fn,len(t))
