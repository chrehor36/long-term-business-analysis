import sys, urllib.request, gzip, re, html, time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip'}
def get(url):
    r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60)
    b=r.read()
    if r.headers.get('Content-Encoding')=='gzip': b=gzip.decompress(b)
    return b.decode('utf-8','replace')
def totext(h):
    h=re.sub(r'(?is)<(script|style).*?</\1>','',h)
    h=re.sub(r'(?is)<ix:header>.*?</ix:header>','',h)
    h=re.sub(r'(?i)</(p|div|tr|br|h\d|li|table)>','\n',h)
    h=re.sub(r'(?i)<br\s*/?>','\n',h)
    h=re.sub(r'(?i)</t[dh]>',' | ',h)
    h=re.sub(r'<[^>]+>','',h)
    h=html.unescape(h).replace('\xa0',' ')
    h=re.sub(r'[ \t]+',' ',h)
    h=re.sub(r'\n\s*\n+','\n',h)
    return h
for arg in sys.argv[1:]:
    cik,acc,doc,name=arg.split(',')
    url=f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{doc}'
    try:
        t=totext(get(url)); open(name,'w',encoding='utf-8').write(f'SOURCE {url}\nACCESSION {acc}\n'+t); print(name,len(t))
    except Exception as e: print('FAIL',name,e)
    time.sleep(0.3)
