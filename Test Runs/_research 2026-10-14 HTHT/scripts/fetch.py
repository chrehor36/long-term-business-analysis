import sys, os, json, time, urllib.request, re, html
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
D=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"cache")
def get(url, name=None):
    p=os.path.join(D,name) if name else None
    if p and os.path.exists(p): return open(p,'rb').read()
    for i in range(4):
        try:
            r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60).read(); break
        except Exception as e:
            print('retry',e,file=sys.stderr); time.sleep(3)
    else: raise SystemExit('fail '+url)
    if p: open(p,'wb').write(r)
    time.sleep(0.3)
    return r
def text(b):
    s=b.decode('utf-8','replace')
    s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',s)
    s=re.sub(r'(?i)</td>|</th>',' | ',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s)
    s=re.sub(r'[ \t\xa0]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
if __name__=='__main__':
    cmd=sys.argv[1]
    if cmd=='subs':
        b=get('https://data.sec.gov/submissions/CIK0001483994.json','subs.json')
        j=json.loads(b); r=j['filings']['recent']
        for i in range(len(r['form'])):
            if r['form'][i] in ('20-F','6-K','20-F/A','F-3ASR','424B2','424B5','S-8','SC 13G','SC 13D'):
                print(r['filingDate'][i], r['form'][i], r['accessionNumber'][i], r['primaryDocument'][i], r.get('primaryDocDescription',['']*9999)[i])
        print(j['filings'].get('files'))
    elif cmd=='doc':
        url=sys.argv[2]; name=sys.argv[3]
        b=get(url,name)
        t=text(b); open(os.path.join(D,name+'.txt'),'w',encoding='utf-8').write(t); print(len(t))
    elif cmd=='idx':
        acc=sys.argv[2]; a=acc.replace('-','')
        b=get(f'https://www.sec.gov/Archives/edgar/data/1483994/{a}/index.json',f'idx_{a}.json')
        j=json.loads(b)
        for it in j['directory']['item']: print(acc, it['name'], it.get('size'))
