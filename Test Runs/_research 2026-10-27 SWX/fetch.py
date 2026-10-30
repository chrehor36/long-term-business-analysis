import sys, os, re, time, urllib.request, html
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def get(acc, doc, out):
    cik='1692115'
    url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
    p=os.path.join('cache',out)
    if not os.path.exists(p):
        req=urllib.request.Request(url,headers=UA)
        data=urllib.request.urlopen(req).read()
        open(p,'wb').write(data); time.sleep(0.3)
    raw=open(p,'rb').read().decode('utf-8','ignore')
    t=re.sub(r'(?is)<(script|style).*?</\1>',' ',raw)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
    t=re.sub(r'(?i)</td>|</th>',' | ',t)
    t=re.sub(r'<[^>]+>',' ',t)
    t=html.unescape(t)
    t=re.sub(r'[ \t\xa0]+',' ',t)
    t=re.sub(r'\n\s*\n+','\n',t)
    open(os.path.join('cache',out.rsplit('.',1)[0]+'.txt'),'w',encoding='utf-8').write(t)
    print(out, len(t))
for line in sys.argv[1:]:
    acc,doc,out=line.split(',')
    get(acc,doc,out)
