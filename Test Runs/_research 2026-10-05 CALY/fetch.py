import sys, re, html, urllib.request, time, os
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    return urllib.request.urlopen(req,timeout=60).read().decode('utf-8','ignore')
def totext(h):
    h=re.sub(r'(?is)<(script|style).*?</\1>','',h)
    h=re.sub(r'(?is)<ix:header>.*?</ix:header>','',h)
    h=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',h)
    h=re.sub(r'(?i)</td>|</th>',' | ',h)
    h=re.sub(r'<[^>]+>','',h)
    h=html.unescape(h).replace('\xa0',' ')
    h=re.sub(r'[ \t]+',' ',h)
    h=re.sub(r'\n\s*\n+','\n',h)
    return h
cik=sys.argv[1]
for arg in sys.argv[2:]:
    acc,doc,name=arg.split(',')
    url=f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{doc}'
    if os.path.exists(name): print('have',name); continue
    t=totext(get(url))
    open(name,'w',encoding='utf-8').write(f'SOURCE {url}\nACCESSION {acc}\n'+t)
    print(name,len(t)); time.sleep(0.3)
