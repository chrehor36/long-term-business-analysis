# Fetch SEC filings for the GPOR run (and peers). Saves raw HTML and a text version in this folder.
import sys, os, re, json, time, urllib.request, html
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
HERE=os.path.dirname(os.path.abspath(__file__))
def get(url):
    req=urllib.request.Request(url,headers=UA)
    for i in range(4):
        try:
            with urllib.request.urlopen(req,timeout=60) as r: return r.read()
        except Exception as e:
            print('retry',url,e); time.sleep(2+i*3)
    raise SystemExit('failed '+url)
def subs(cik):
    p=os.path.join(HERE,f'sub_{cik}.json')
    if os.path.exists(p): return json.load(open(p))
    j=json.loads(get(f'https://data.sec.gov/submissions/CIK{int(cik):010d}.json'))
    json.dump(j,open(p,'w')); return j
def filings(cik, forms):
    j=subs(cik); r=j['filings']['recent']; out=[]
    for i,f in enumerate(r['form']):
        if f in forms: out.append((r['filingDate'][i],f,r['accessionNumber'][i],r['primaryDocument'][i],r['reportDate'][i]))
    for extra in j['filings'].get('files',[]):
        p=os.path.join(HERE,'sub_'+extra['name'])
        if not os.path.exists(p): open(p,'wb').write(get('https://data.sec.gov/submissions/'+extra['name']))
        rr=json.load(open(p))
        for i,f in enumerate(rr['form']):
            if f in forms: out.append((rr['filingDate'][i],f,rr['accessionNumber'][i],rr['primaryDocument'][i],rr['reportDate'][i]))
    return sorted(out)
def totext(b):
    s=b.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',s)
    s=re.sub(r'(?i)</td>|</th>',' | ',s)
    s=re.sub(r'<[^>]+>',' ',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
    return s
def save(cik, acc, doc, name):
    out=os.path.join(HERE,name)
    if os.path.exists(out): return out
    url=f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/{doc}'
    b=get(url); open(out,'w',encoding='utf-8').write(totext(b)); time.sleep(0.3); return out
if __name__=='__main__':
    cik=sys.argv[1]; forms=sys.argv[2].split(',')
    for f in filings(cik,forms): print(*f)
