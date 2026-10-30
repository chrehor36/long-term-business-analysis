import urllib.request, os, re, sys, json, time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def get(url, binary=False):
    r=urllib.request.Request(url, headers=UA)
    for i in range(4):
        try:
            return urllib.request.urlopen(r,timeout=90).read()
        except Exception as e:
            print('retry',i,e); time.sleep(3)
    raise SystemExit('fail '+url)
def strip(html):
    s=html.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'(?is)<br[^>]*>','\n',s)
    s=re.sub(r'(?is)</(p|div|tr|h1|h2|h3|li|table)>','\n',s)
    s=re.sub(r'(?is)</t[dh]>',' | ',s)
    s=re.sub(r'(?s)<[^>]+>',' ',s)
    import html as H
    s=H.unescape(s)
    s=re.sub(r'[ \t\xa0]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
if __name__=='__main__':
    url,out=sys.argv[1],sys.argv[2]
    b=get(url)
    if out.endswith('.json'):
        open(out,'wb').write(b)
    else:
        open(out,'w',encoding='utf-8').write(strip(b))
    print(out, os.path.getsize(out))
