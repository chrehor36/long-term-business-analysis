import sys, json, os, time, urllib.request, re, html
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def get(url, out=None):
    p=os.path.join('cache', out) if out else None
    if p and os.path.exists(p): return open(p,'rb').read()
    r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60).read()
    time.sleep(0.2)
    if p: open(p,'wb').write(r)
    return r
def text(b):
    s=b.decode('utf-8','replace')
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',s)
    s=re.sub(r'(?i)</td>|</th>',' | ',s)
    s=re.sub(r'<[^>]+>',' ',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
if __name__=='__main__':
    cmd=sys.argv[1]
    if cmd=='subs':
        d=json.loads(get('https://data.sec.gov/submissions/CIK0000928340.json','subs.json'))
        r=d['filings']['recent']
        for i in range(len(r['form'])):
            if r['form'][i] in ('10-K','10-Q','DEF 14A','8-K','10-K/A','S-3','S-8','424B5','8-K/A'):
                print(r['form'][i],r['filingDate'][i],r['accessionNumber'][i],r['primaryDocument'][i],r.get('items',['']*9999)[i])
    elif cmd=='doc':
        acc,doc,out=sys.argv[2],sys.argv[3],sys.argv[4]
        url='https://www.sec.gov/Archives/edgar/data/928340/%s/%s'%(acc.replace('-',''),doc)
        b=get(url,out+'.htm')
        open(os.path.join('cache',out+'.txt'),'w',encoding='utf-8').write(text(b))
        print(len(b))
