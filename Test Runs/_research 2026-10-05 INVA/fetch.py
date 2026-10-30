import sys, json, time, urllib.request, gzip, re, html
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip'}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    for i in range(4):
        try:
            r=urllib.request.urlopen(req,timeout=60); d=r.read()
            if r.headers.get('Content-Encoding')=='gzip': d=gzip.decompress(d)
            time.sleep(0.15); return d
        except Exception as e:
            print('retry',e,file=sys.stderr); time.sleep(2)
    raise
def text(url,out):
    d=get(url).decode('utf-8','ignore')
    t=re.sub(r'(?is)<(script|style).*?</\1>','',d)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
    t=re.sub(r'(?i)</td>|</th>',' | ',t)
    t=re.sub(r'<[^>]+>','',t); t=html.unescape(t)
    t=re.sub(r'[ \t\xa0]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(out,'w',encoding='utf-8').write(t); print(out,len(t))
if __name__=='__main__':
    if sys.argv[1]=='json':
        open(sys.argv[3],'wb').write(get(sys.argv[2])); print('ok')
    else: text(sys.argv[2],sys.argv[3])
