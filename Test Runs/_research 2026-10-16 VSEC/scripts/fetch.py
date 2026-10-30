import sys, urllib.request, gzip, os, re, html
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip'}
def get(url):
    r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60)
    d=r.read()
    if r.headers.get('Content-Encoding')=='gzip': d=gzip.decompress(d)
    return d
def strip(b):
    t=b.decode('utf-8','ignore')
    t=re.sub(r'(?is)<(script|style).*?</\1>','',t)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
    t=re.sub(r'(?i)</td>|</th>',' | ',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t)
    t=re.sub(r'\n\s*\n+','\n',t)
    return t
if __name__=='__main__':
    url,out=sys.argv[1],sys.argv[2]
    d=get(url)
    if out.endswith('.txt'): open(out,'w',encoding='utf-8').write(strip(d))
    else: open(out,'wb').write(d)
    print(out, len(d))
