import sys, os, time, json, urllib.request, re, html
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def get(url, out=None):
    if out and os.path.exists(out):
        return open(out,'rb').read()
    req=urllib.request.Request(url,headers=UA)
    for i in range(5):
        try:
            d=urllib.request.urlopen(req,timeout=60).read(); break
        except Exception as e:
            print('retry',e,file=sys.stderr); time.sleep(2)
    time.sleep(0.15)
    if out:
        os.makedirs(os.path.dirname(out) or '.',exist_ok=True); open(out,'wb').write(d)
    return d
def text(htmlb):
    s=htmlb.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>',"\n",s)
    s=re.sub(r'(?i)</td>',' | ',s)
    s=re.sub(r'<[^>]+>',' ',s)
    s=html.unescape(s)
    s=re.sub(r'[ \t\xa0]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
if __name__=='__main__':
    url,out=sys.argv[1],sys.argv[2]
    d=get(url, out+'.raw' if not out.endswith('.json') else out)
    if not out.endswith('.json'):
        open(out,'w',encoding='utf-8').write(text(d))
    print('ok',len(d))
