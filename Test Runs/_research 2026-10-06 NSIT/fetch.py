import sys, json, urllib.request, os, time, re, html
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
def get(url, out=None):
    if out and os.path.exists(out): return open(out,'rb').read()
    for i in range(3):
        try:
            r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60).read(); break
        except Exception as e:
            print('retry',e,file=sys.stderr); time.sleep(2)
    if out: open(out,'wb').write(r)
    time.sleep(0.15)
    return r
def text(htmlb):
    s=htmlb.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',s)
    s=re.sub(r'(?i)</td>|</th>',' | ',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
    return s
if __name__=='__main__':
    cmd=sys.argv[1]
    if cmd=='sub':
        cik=sys.argv[2]; tk=sys.argv[3]
        d=json.loads(get(f'https://data.sec.gov/submissions/CIK{int(cik):010d}.json',f'{tk}_sub.json'))
        r=d['filings']['recent']
        for i in range(len(r['form'])):
            if r['form'][i] in sys.argv[4].split(','):
                print(r['form'][i],r['filingDate'][i],r['reportDate'][i],r['accessionNumber'][i],r['primaryDocument'][i])
        for f in d['filings'].get('files',[]): print('OLDER',f['name'],f['filingFrom'],f['filingTo'])
    elif cmd=='older':
        name=sys.argv[2]
        d=json.loads(get('https://data.sec.gov/submissions/'+name,name))
        for i in range(len(d['form'])):
            if d['form'][i] in sys.argv[3].split(','):
                print(d['form'][i],d['filingDate'][i],d['reportDate'][i],d['accessionNumber'][i],d['primaryDocument'][i])
    elif cmd=='doc':
        cik,acc,doc,out=sys.argv[2:6]
        url=f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/{doc}'
        b=get(url,out+'.htm')
        open(out+'.txt','w',encoding='utf-8').write(text(b))
        print(out, len(b))
    elif cmd=='idx':
        cik,acc=sys.argv[2:4]
        b=get(f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/index.json')
        for it in json.loads(b)['directory']['item']: print(it['name'],it.get('size'))
