import sys, urllib.request, re, html, os
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"identity"}
def get(url,out):
    if os.path.exists(out): return
    req=urllib.request.Request(url,headers=UA)
    data=urllib.request.urlopen(req,timeout=120).read()
    open(out,'wb').write(data)
def totext(src,dst):
    s=open(src,'rb').read().decode('utf-8','replace')
    s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?is)<ix:header>.*?</ix:header>','',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',s)
    s=re.sub(r'(?i)</td>|</th>',' | ',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
    open(dst,'w',encoding='utf-8').write(s)
cik='922224'
for arg in sys.argv[1:]:
    acc,doc,name=arg.split(',')
    url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
    out=f"cache/{name}.htm"
    get(url,out); totext(out,f"cache/{name}.txt")
    print(name, os.path.getsize(f"cache/{name}.txt"))
