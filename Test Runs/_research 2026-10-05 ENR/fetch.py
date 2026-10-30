import urllib.request, json, sys, os, re, gzip, html
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip'}
D=os.path.dirname(os.path.abspath(__file__))
def get(url):
    r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60)
    b=r.read()
    if r.headers.get('Content-Encoding')=='gzip': b=gzip.decompress(b)
    return b
def text(url,out):
    b=get(url).decode('utf-8','replace')
    t=re.sub(r'(?is)<(script|style).*?</\1>','',b)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
    t=re.sub(r'(?i)</td>',' | ',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(os.path.join(D,out),'w',encoding='utf-8').write(t)
    print(out,len(t))
if __name__=='__main__':
    cmd=sys.argv[1]
    if cmd=='subs':
        cik=sys.argv[2]; j=json.loads(get(f'https://data.sec.gov/submissions/CIK{cik}.json'))
        json.dump(j,open(os.path.join(D,f'sub_{cik}.json'),'w'))
        f=j['filings']['recent']
        for i in range(len(f['form'])):
            if f['form'][i] in sys.argv[3].split(','):
                print(f['form'][i],f['filingDate'][i],f['accessionNumber'][i],f['primaryDocument'][i],f['reportDate'][i])
    elif cmd=='doc':
        text(sys.argv[2],sys.argv[3])
    elif cmd=='facts':
        cik=sys.argv[2]; b=get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json'); open(os.path.join(D,f'facts_{cik}.json'),'wb').write(b); print(len(b))
