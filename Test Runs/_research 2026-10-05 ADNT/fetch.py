import sys, urllib.request, json, os, re, time, html
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
def get(url):
    r=urllib.request.Request(url,headers=UA)
    for i in range(3):
        try:
            return urllib.request.urlopen(r,timeout=60).read()
        except Exception as e:
            print("retry",e,file=sys.stderr); time.sleep(2)
    raise
def totext(b):
    s=b.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'(?i)<br\s*/?>','\n',s)
    s=re.sub(r'(?i)</(p|div|tr|li|h\d|table)>','\n',s)
    s=re.sub(r'(?i)</t[dh]>',' | ',s)
    s=re.sub(r'<[^>]+>',' ',s)
    s=html.unescape(s)
    s=re.sub(r'[ \t\xa0]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
if __name__=="__main__":
    url,out=sys.argv[1],sys.argv[2]
    b=get(url)
    if out.endswith('.txt'):
        open(out,'w',encoding='utf-8').write(totext(b))
    else:
        open(out,'wb').write(b)
    print(out, len(b))
