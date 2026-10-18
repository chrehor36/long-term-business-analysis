import sys, re, html, time, urllib.request, os
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def get(url):
    for i in range(5):
        try:
            return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60).read()
        except Exception as e:
            print('retry',e); time.sleep(2)
def strip(b):
    t=b.decode('utf-8','ignore')
    t=re.sub(r'(?is)<(script|style).*?</\1>','',t)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
    t=re.sub(r'(?i)</td>|</th>',' | ',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    return t
for arg in sys.argv[1:]:
    p=arg.split(","); acc,doc,name=p[:3]
    cik=int(p[3]) if len(p)>3 else (int(acc.split("-")[0]) if not acc.startswith("0001193125") else 1767042)
    url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
    b=get(url); open('cache/'+name+'.htm','wb').write(b)
    open('cache/'+name+'.txt','w',encoding='utf-8').write(strip(b))
    print(name,len(b)); time.sleep(0.3)
