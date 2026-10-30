import warnings; from bs4 import XMLParsedAsHTMLWarning; warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
import sys, json, requests, os, re, time
H={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def get(url):
    for i in range(4):
        r=requests.get(url,headers=H,timeout=60)
        if r.status_code==200: return r
        time.sleep(1+i)
    r.raise_for_status()
def submissions(cik):
    cik=str(int(cik)).zfill(10)
    j=get(f'https://data.sec.gov/submissions/CIK{cik}.json').json()
    out=[]
    def add(rec):
        for f,d,a,p,desc in zip(rec['form'],rec['filingDate'],rec['accessionNumber'],rec['primaryDocument'],rec['primaryDocDescription']):
            out.append((f,d,a,p,desc))
    add(j['filings']['recent'])
    for fl in j['filings'].get('files',[]):
        add(get('https://data.sec.gov/submissions/'+fl['name']).json())
    return out
def html2txt(h):
    from bs4 import BeautifulSoup
    s=BeautifulSoup(h,'lxml')
    for t in s(['script','style']): t.decompose()
    txt=s.get_text('\n')
    txt=re.sub(r'\n\s*\n+','\n',txt)
    return txt
def doc(cik,acc,prim,out):
    url=f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/{prim}'
    r=get(url)
    t=html2txt(r.content) if prim.lower().endswith(('htm','html')) else r.text
    open(out,'w',encoding='utf-8').write(t)
    return len(t)
if __name__=='__main__':
    cmd=sys.argv[1]
    if cmd=='list':
        forms=set(sys.argv[3].split(','))
        for f in submissions(sys.argv[2]):
            if f[0] in forms: print('|'.join(f))
    elif cmd=='doc':
        print(doc(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]))
