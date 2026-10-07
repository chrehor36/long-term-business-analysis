import json,sys,os,time,re,html,urllib.request
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    for k in range(4):
        try:
            return urllib.request.urlopen(req,timeout=60).read()
        except Exception as e:
            print('retry',url,e); time.sleep(2)
    raise SystemExit('fail '+url)
def text(b):
    s=b.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',s)
    s=re.sub(r'(?i)</td>',' | ',s)
    s=re.sub(r'<[^>]+>',' ',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
if __name__=='__main__':
    acc,doc,out=sys.argv[1],sys.argv[2],sys.argv[3]
    url='https://www.sec.gov/Archives/edgar/data/64472/%s/%s'%(acc.replace('-',''),doc)
    b=get(url); open(out,'w',encoding='utf-8').write(text(b)); print(out,len(b))
    time.sleep(0.3)
