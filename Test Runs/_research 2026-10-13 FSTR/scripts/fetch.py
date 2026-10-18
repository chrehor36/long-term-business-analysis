import sys, re, html, urllib.request, os, time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def get(url):
    for i in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60).read()
        except Exception as e:
            time.sleep(2)
    raise SystemExit('fail '+url)
def strip(b):
    t=b.decode('utf-8','replace')
    t=re.sub(r'(?is)<(script|style).*?</\1>','',t)
    t=re.sub(r'(?is)<ix:header>.*?</ix:header>','',t)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
    t=re.sub(r'(?i)</td>|</th>',' | ',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t)
    t=re.sub(r'\n\s*\n+','\n',t)
    return t
outdir=sys.argv[1]
for spec in sys.argv[2:]:
    parts=spec.split(","); name,acc,doc=parts[:3]; cik=parts[3] if len(parts)>3 else "352825"
    url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
    b=get(url)
    open(os.path.join(outdir,name+'.txt'),'w',encoding='utf-8').write(strip(b))
    print(name,len(b))
    time.sleep(0.3)
