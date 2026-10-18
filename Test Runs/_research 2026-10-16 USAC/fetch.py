import sys, urllib.request, gzip, os, re, html
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip'}
def get(url):
    r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60)
    b=r.read()
    if r.headers.get('Content-Encoding')=='gzip': b=gzip.decompress(b)
    return b
def text(b):
    s=b.decode('utf-8','replace')
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',s)
    s=re.sub(r'(?i)</td>|</th>',' | ',s)
    s=re.sub(r'<[^>]+>',' ',s)
    s=html.unescape(s)
    s=re.sub(r'[ \t\xa0]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
if __name__=='__main__':
    url,out=sys.argv[1],sys.argv[2]
    b=get(url)
    if out.endswith('.txt') and (url.endswith('.htm') or url.endswith('.html')):
        open(out,'w',encoding='utf-8').write(text(b))
    else:
        open(out,'wb').write(b)
    print(out, len(b))
