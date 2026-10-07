import sys, os, json, time, urllib.request, gzip, re, html
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"gzip"}
def get(url, out=None):
    if out and os.path.exists(out): return open(out,'rb').read()
    req=urllib.request.Request(url,headers=UA)
    for i in range(4):
        try:
            r=urllib.request.urlopen(req,timeout=60); d=r.read()
            if r.headers.get('Content-Encoding')=='gzip': d=gzip.decompress(d)
            break
        except Exception as e:
            print('retry',e,file=sys.stderr); time.sleep(2)
    else: raise SystemExit('fail '+url)
    time.sleep(0.2)
    if out: open(out,'wb').write(d)
    return d
def totext(b):
    s=b.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',s)
    s=re.sub(r'(?i)</td>',' | ',s)
    s=re.sub(r'<[^>]+>',' ',s)
    s=html.unescape(s)
    s=re.sub(r'[ \t\xa0]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
if __name__=='__main__':
    cmd=sys.argv[1]
    if cmd=='sub':
        cik=sys.argv[2].zfill(10)
        d=json.loads(get(f'https://data.sec.gov/submissions/CIK{cik}.json',f'sub_{cik}.json'))
        r=d['filings']['recent']
        print(d['name'], d.get('formerNames'))
        forms=set(sys.argv[3].split(',')) if len(sys.argv)>3 else None
        for i in range(len(r['form'])):
            if forms is None or r['form'][i] in forms:
                print(r['filingDate'][i], r['form'][i], r['accessionNumber'][i], r['primaryDocument'][i], r.get('items',['']*9999)[i])
        for f in d['filings'].get('files',[]): print('OLDER',f)
    elif cmd=='doc':
        cik,acc,doc,out=sys.argv[2:6]
        url=f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/{doc}'
        b=get(url,out+'.raw')
        open(out,'w',encoding='utf-8').write(totext(b))
        print(out, len(b))
    elif cmd=='url':
        url,out=sys.argv[2:4]
        b=get(url,out+'.raw'); open(out,'w',encoding='utf-8').write(totext(b)); print(out,len(b))
