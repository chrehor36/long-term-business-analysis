import sys, re, html, urllib.request, os, time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
CIK='945114'
def get(acc, doc, out):
    cik=CIK
    url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
    req=urllib.request.Request(url,headers=UA)
    raw=urllib.request.urlopen(req).read().decode('utf-8','replace')
    t=re.sub(r'(?is)<(script|style).*?</\1>','',raw)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
    t=re.sub(r'(?i)</td>',' | ',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t)
    t=re.sub(r'\n\s*\n+','\n',t)
    open(os.path.join('cache',out),'w',encoding='utf-8').write(t)
    print(out,len(t))
    time.sleep(0.3)
for a in sys.argv[1:]:
    acc,doc,out=a.split(',')
    get(acc,doc,out)
