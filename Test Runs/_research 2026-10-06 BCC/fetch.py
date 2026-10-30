import json, sys, time, urllib.request, os, re, html
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"identity"}
def get(url):
    for i in range(4):
        try:
            r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60)
            return r.read()
        except Exception as e:
            print("retry",url,e,file=sys.stderr); time.sleep(2)
    raise SystemExit("fail "+url)
def subs(cik):
    cik=str(cik).zfill(10)
    d=json.loads(get(f"https://data.sec.gov/submissions/CIK{cik}.json"))
    rows=[]
    def add(f):
        for a,fo,dt,doc,rd in zip(f['accessionNumber'],f['form'],f['filingDate'],f['primaryDocument'],f['reportDate']):
            rows.append((dt,fo,a,doc,rd))
    add(d['filings']['recent'])
    for x in d['filings'].get('files',[]):
        add(json.loads(get("https://data.sec.gov/submissions/"+x['name'])))
    return d['name'],rows
def text(url):
    b=get(url).decode('utf-8','replace')
    b=re.sub(r'(?is)<(script|style).*?</\1>',' ',b)
    b=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',b)
    b=re.sub(r'(?i)</td>|</th>',' | ',b)
    b=re.sub(r'<[^>]+>',' ',b)
    b=html.unescape(b).replace('\xa0',' ')
    b=re.sub(r'[ \t]+',' ',b); b=re.sub(r'\n\s*\n+','\n',b)
    return b
if __name__=="__main__":
    cmd=sys.argv[1]
    if cmd=="subs":
        name,rows=subs(sys.argv[2]); forms=sys.argv[3].split(',') if len(sys.argv)>3 else None
        print(name)
        for r in sorted(rows):
            if not forms or r[1] in forms: print(*r,sep=' | ')
    elif cmd=="doc":
        cik,acc,doc,out=sys.argv[2:6]
        url=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
        t=text(url); open(out,'w',encoding='utf-8').write(t); print(out,len(t))
