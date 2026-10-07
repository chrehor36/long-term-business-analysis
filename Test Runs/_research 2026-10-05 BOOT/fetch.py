import sys, re, html, urllib.request, time, os
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    with urllib.request.urlopen(req,timeout=60) as r:
        b=r.read()
    return b.decode('utf-8','replace')
def totext(h):
    h=re.sub(r'(?is)<(script|style).*?</\1>','',h)
    h=re.sub(r'(?i)<br\s*/?>','\n',h)
    h=re.sub(r'(?i)</(p|div|tr|li|h\d|table)>','\n',h)
    h=re.sub(r'(?i)</t[dh]>',' | ',h)
    h=re.sub(r'<[^>]+>','',h)
    h=html.unescape(h).replace('\xa0',' ')
    h=re.sub(r'[ \t]+',' ',h)
    h=re.sub(r'\n\s*\n+','\n',h)
    return h
cik='1610250'
for arg in sys.argv[1:]:
    acc,doc,out=arg.split(',')
    url=f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{doc}'
    t=totext(get(url))
    open(out,'w',encoding='utf-8').write(f'SOURCE {url}\nACCESSION {acc}\n'+t)
    print(out,len(t))
    time.sleep(0.3)
