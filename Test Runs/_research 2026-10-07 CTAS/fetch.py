import sys, requests, time, os, re, html
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip, deflate'}
def get(url):
    for i in range(4):
        r=requests.get(url,headers=UA,timeout=60)
        if r.status_code==200: return r
        time.sleep(1+i)
    r.raise_for_status()
def text(url,out):
    r=get(url); t=r.text
    t=re.sub(r'(?is)<(script|style).*?</\1>',' ',t)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
    t=re.sub(r'(?i)</td>|</th>',' | ',t)
    t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t)
    t=re.sub(r'[ \t\xa0]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(out,'w',encoding='utf-8').write(t); print(out,len(t))
if __name__=='__main__':
    if sys.argv[1]=='json':
        open(sys.argv[3],'w',encoding='utf-8').write(get(sys.argv[2]).text); print('ok')
    else: text(sys.argv[2],sys.argv[3])
