import sys, os, json, re, time, urllib.request
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
HERE=os.path.dirname(os.path.abspath(__file__)); CACHE=os.path.join(HERE,"cache")
def get(url, name=None):
    p=os.path.join(CACHE, name or re.sub(r'[^A-Za-z0-9._-]','_',url)[-150:])
    if os.path.exists(p): return open(p,encoding='utf-8',errors='replace').read()
    for i in range(4):
        try:
            raw=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60).read(); break
        except Exception as e:
            print('retry',e); time.sleep(3)
    t=raw.decode('utf-8','replace'); open(p,'w',encoding='utf-8').write(t); time.sleep(0.2); return t
def text(html):
    html=re.sub(r'(?is)<(script|style).*?</\1>',' ',html)
    html=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',html)
    html=re.sub(r'(?i)</td>|</th>',' | ',html)
    t=re.sub(r'<[^>]+>',' ',html)
    import html as H; t=H.unescape(t)
    t=re.sub(r'[ \t\xa0]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    return t
if __name__=="__main__":
    cmd=sys.argv[1]
    if cmd=="subs":
        cik=sys.argv[2]
        j=json.loads(get(f"https://data.sec.gov/submissions/CIK{cik}.json",f"subs_{cik}.json"))
        r=j['filings']['recent']
        forms=set(sys.argv[3].split(',')) if len(sys.argv)>3 else None
        for i in range(len(r['form'])):
            if forms is None or r['form'][i] in forms:
                print(r['filingDate'][i], r['form'][i], r['accessionNumber'][i], r['primaryDocument'][i], r.get('reportDate',[''])[i])
        for f in j['filings'].get('files',[]): print('OLDER', f['name'], f['filingFrom'], f['filingTo'])
    elif cmd=="older":
        j=json.loads(get(f"https://data.sec.gov/submissions/{sys.argv[2]}",sys.argv[2]))
        forms=set(sys.argv[3].split(','))
        for i in range(len(j['form'])):
            if j['form'][i] in forms: print(j['filingDate'][i], j['form'][i], j['accessionNumber'][i], j['primaryDocument'][i], j['reportDate'][i])
    elif cmd=="doc":
        cik, acc, doc, out = sys.argv[2:6]
        url=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
        h=get(url, acc+"_"+doc)
        t=text(h) if doc.endswith(('htm','html')) else h
        open(os.path.join(CACHE,out),'w',encoding='utf-8').write(t); print(out, len(t))
    elif cmd=="index":
        cik, acc = sys.argv[2:4]
        url=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/index.json"
        j=json.loads(get(url, acc+"_index.json"))
        for it in j['directory']['item']: print(it['name'], it.get('size'))
