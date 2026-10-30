import sys, re, html, time, urllib.request, gzip
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip'}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    r=urllib.request.urlopen(req,timeout=60).read()
    try: r=gzip.decompress(r)
    except Exception: pass
    return r.decode('utf-8','replace')
def totext(h):
    h=re.sub(r'(?is)<(script|style).*?</\1>',' ',h)
    h=re.sub(r'(?is)<ix:header>.*?</ix:header>',' ',h)
    h=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>',"\n",h)
    h=re.sub(r'(?i)</td>|</th>'," | ",h)
    h=re.sub(r'<[^>]+>','',h)
    h=html.unescape(h).replace('\xa0',' ')
    h=re.sub(r'[ \t]+',' ',h)
    h=re.sub(r'\n\s*\n+','\n',h)
    return h
cik='1590976'
for arg in sys.argv[1:]:
    acc,doc,out=arg.split(',')
    url=f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{doc}'
    t=totext(get(url))
    open(out,'w',encoding='utf-8').write(f'SOURCE: {url}\nACCESSION: {acc}\n'+t)
    print(out,len(t)); time.sleep(0.3)
