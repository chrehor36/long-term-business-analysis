import sys, urllib.request, re, html, os
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def get(url,out):
    req=urllib.request.Request(url,headers=UA)
    raw=urllib.request.urlopen(req,timeout=120).read().decode('utf-8','replace')
    t=re.sub(r'(?is)<(script|style).*?</\1>',' ',raw)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
    t=re.sub(r'(?i)</td>|</th>',' | ',t)
    t=re.sub(r'<[^>]+>',' ',t)
    t=html.unescape(t).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t)
    t=re.sub(r'\n\s*\n+','\n',t)
    open(out,'w',encoding='utf-8').write(t)
    print(out,len(t))
if __name__=='__main__':
    get(sys.argv[1],sys.argv[2])
