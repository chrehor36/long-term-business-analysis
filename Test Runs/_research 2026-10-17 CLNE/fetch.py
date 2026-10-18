import sys, os, json, urllib.request, gzip, re, html
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip'}
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'cache')
def get(url, name=None):
    name = name or re.sub(r'[^A-Za-z0-9._-]','_',url)[-120:]
    p=os.path.join(D,name)
    if os.path.exists(p): return open(p,'rb').read()
    r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60)
    b=r.read()
    if r.headers.get('Content-Encoding')=='gzip': b=gzip.decompress(b)
    open(p,'wb').write(b); return b
def text(url,name=None):
    b=get(url,name).decode('utf-8','replace')
    b=re.sub(r'(?is)<(script|style).*?</\1>',' ',b)
    b=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',b)
    b=re.sub(r'(?i)</td>',' | ',b)
    b=re.sub(r'<[^>]+>',' ',b); b=html.unescape(b)
    b=re.sub(r'[ \t\xa0]+',' ',b); b=re.sub(r'\n\s*\n+','\n',b)
    return b
if __name__=='__main__':
    cmd=sys.argv[1]
    if cmd=='subs':
        j=json.loads(get('https://data.sec.gov/submissions/CIK%s.json'%sys.argv[2],'subs_%s.json'%sys.argv[2]))
        r=j['filings']['recent']
        n=int(sys.argv[3]) if len(sys.argv)>3 else 60
        forms=sys.argv[4].split(',') if len(sys.argv)>4 else None
        for i in range(len(r['form'])):
            if forms and r['form'][i] not in forms: continue
            print(r['filingDate'][i],r['form'][i],r['accessionNumber'][i],r['primaryDocument'][i],r['items'][i] if 'items' in r else '')
            n-=1
            if n<=0: break
    elif cmd=='doc':
        cik,acc,doc=sys.argv[2:5]
        url='https://www.sec.gov/Archives/edgar/data/%d/%s/%s'%(int(cik),acc.replace('-',''),doc)
        t=text(url, acc+'_'+doc)
        out=os.path.join(D,acc+'_'+doc+'.txt'); open(out,'w',encoding='utf-8').write(t); print(out,len(t))
