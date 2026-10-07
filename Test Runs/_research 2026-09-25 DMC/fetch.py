import sys, urllib.request, time, re, html, os
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"identity"}
def get(url):
    for i in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60).read()
        except Exception as e:
            print("retry",e); time.sleep(2)
    raise SystemExit("fail "+url)
def totext(b):
    s=b.decode('utf-8','replace')
    s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',s)
    s=re.sub(r'(?i)</td>',' | ',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
if __name__=="__main__":
    url,out=sys.argv[1],sys.argv[2]
    b=get(url)
    if out.endswith('.txt'):
        open(out,'w',encoding='utf-8').write(totext(b))
    else:
        open(out,'wb').write(b)
    print(out,len(b))
