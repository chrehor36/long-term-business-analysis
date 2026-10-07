import sys, re, html, time, urllib.request
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    return urllib.request.urlopen(req,timeout=60).read().decode('utf-8','replace')
def totext(h):
    h=re.sub(r'(?is)<(script|style).*?</\1>','',h)
    h=re.sub(r'(?is)<ix:header>.*?</ix:header>','',h)
    h=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',h)
    h=re.sub(r'(?i)</td>',' | ',h)
    h=re.sub(r'<[^>]+>','',h)
    h=html.unescape(h).replace('\xa0',' ')
    h=re.sub(r'[ \t]+',' ',h)
    h=re.sub(r'\n\s*\n+','\n',h)
    return h
for arg in sys.argv[1:]:
    acc,doc,out=arg.split(',')
    url=f"https://www.sec.gov/Archives/edgar/data/1350593/{acc.replace('-','')}/{doc}"
    t=totext(get(url))
    open(out,'w',encoding='utf-8').write(t)
    print(out,len(t))
    time.sleep(0.3)
