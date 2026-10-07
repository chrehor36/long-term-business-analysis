import sys, json, urllib.request, gzip, os, re, html
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip, deflate'}
def get(url):
    r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60)
    b=r.read()
    if r.headers.get('Content-Encoding')=='gzip': b=gzip.decompress(b)
    return b
def totext(b):
    t=b.decode('utf-8','ignore')
    t=re.sub(r'(?is)<(script|style).*?</\1>',' ',t)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
    t=re.sub(r'(?i)</t[dh]>',' | ',t)
    t=re.sub(r'<[^>]+>',' ',t)
    t=html.unescape(t)
    t=re.sub(r'[ \t\xa0]+',' ',t)
    t=re.sub(r'\n\s*\n+','\n',t)
    return t
if __name__=='__main__':
    cmd=sys.argv[1]
    if cmd=='sub':
        cik=sys.argv[2]
        b=get(f'https://data.sec.gov/submissions/CIK{int(cik):010d}.json')
        open(sys.argv[3],'wb').write(b)
    elif cmd=='doc':
        b=get(sys.argv[2]); open(sys.argv[3],'w',encoding='utf-8').write(totext(b))
    elif cmd=='raw':
        b=get(sys.argv[2]); open(sys.argv[3],'wb').write(b)
