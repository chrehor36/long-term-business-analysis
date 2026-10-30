import sys, json, urllib.request, os, time, re, html
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def get(url):
    for i in range(5):
        try:
            r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60)
            return r.read()
        except Exception as e:
            print('retry',e,file=sys.stderr); time.sleep(3)
    raise SystemExit('fail '+url)
def text(b):
    s=b.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',s)
    s=re.sub(r'(?i)</td>',' | ',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s)
    s=re.sub(r'[ \t\xa0]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
if __name__=='__main__':
    cmd=sys.argv[1]
    if cmd=='list':
        d=json.loads(get('https://data.sec.gov/submissions/CIK0001121484.json'))
        r=d['filings']['recent']
        for i in range(len(r['form'])):
            if r['form'][i] in sys.argv[2].split(','):
                print(r['filingDate'][i],r['form'][i],r['accessionNumber'][i],r['primaryDocument'][i],r['reportDate'][i])
    elif cmd=='doc':
        acc,doc,out=sys.argv[2],sys.argv[3],sys.argv[4]
        url=f'https://www.sec.gov/Archives/edgar/data/1121484/{acc.replace("-","")}/{doc}'
        open(out,'w',encoding='utf-8').write(text(get(url)))
        print(out, os.path.getsize(out))
    elif cmd=='raw':
        print(get(sys.argv[2]).decode('utf-8','ignore')[:int(sys.argv[3]) if len(sys.argv)>3 else 5000])
