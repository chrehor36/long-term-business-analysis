import sys, json, urllib.request, time, os, re, html
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def get(url):
    for i in range(4):
        try:
            r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60)
            return r.read()
        except Exception as e:
            print('retry',url,e,file=sys.stderr); time.sleep(2)
    raise SystemExit('fail '+url)
def text(url,out):
    b=get(url).decode('utf-8','replace')
    t=re.sub(r'(?is)<(script|style).*?</\1>','',b)
    t=re.sub(r'\s+',' ',t)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
    t=re.sub(r'(?i)</td>',' | ',t)
    t=re.sub(r'<[^>]+>','',t); t=html.unescape(t)
    t=re.sub(r'[ \t\xa0]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(out,'w',encoding='utf-8').write(t); print(out,len(t))
if __name__=='__main__':
    if sys.argv[1]=='sub':
        d=json.loads(get('https://data.sec.gov/submissions/CIK0000789460.json'))
        json.dump(d,open('sub.json','w'))
        r=d['filings']['recent']
        for i in range(len(r['form'])):
            if r['form'][i] in ('10-K','10-Q','DEF 14A','8-K','10-K/A'):
                print(r['form'][i],r['filingDate'][i],r['accessionNumber'][i],r['primaryDocument'][i],r.get('items',['']*9999)[i])
        print(d.get('filings',{}).get('files'))
    else:
        text(sys.argv[1],sys.argv[2])
