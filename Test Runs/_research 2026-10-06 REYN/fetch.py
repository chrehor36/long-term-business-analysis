import sys, json, urllib.request, gzip, re, html, os
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip'}
def get(url):
    r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60)
    d=r.read()
    if r.headers.get('Content-Encoding')=='gzip': d=gzip.decompress(d)
    return d
def totext(b):
    s=b.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',s)
    s=re.sub(r'(?i)</t[dh]>',' | ',s)
    s=re.sub(r'<[^>]+>',' ',s)
    s=html.unescape(s)
    s=re.sub(r'[ \t\xa0]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
if __name__=='__main__':
    cmd=sys.argv[1]
    if cmd=='subs':
        cik=sys.argv[2]
        d=json.loads(get(f'https://data.sec.gov/submissions/CIK{int(cik):010d}.json'))
        json.dump(d,open(f'sub_{cik}.json','w'))
        r=d['filings']['recent']
        for i in range(len(r['form'])):
            if len(sys.argv)<4 or r['form'][i] in sys.argv[3].split(','):
                print(r['form'][i],r['filingDate'][i],r['accessionNumber'][i],r['primaryDocument'][i],r.get('reportDate',[''])[i])
    elif cmd=='doc':
        url,out=sys.argv[2],sys.argv[3]
        open(out,'w',encoding='utf-8').write(totext(get(url)))
        print('ok',out,os.path.getsize(out))
    elif cmd=='facts':
        cik=sys.argv[2]
        open(f'facts_{cik}.json','wb').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{int(cik):010d}.json'))
        print('ok')
