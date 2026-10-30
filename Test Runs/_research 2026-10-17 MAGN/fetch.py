import sys, os, re, time, urllib.request, html
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def get(url):
    for i in range(4):
        try:
            req=urllib.request.Request(url,headers=UA)
            return urllib.request.urlopen(req,timeout=60).read()
        except Exception as e:
            print('retry',e); time.sleep(3)
    raise SystemExit('fail '+url)
def strip(b):
    t=b.decode('utf-8','ignore')
    t=re.sub(r'(?is)<(script|style).*?</\1>',' ',t)
    t=re.sub(r'(?is)<ix:header>.*?</ix:header>',' ',t)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
    t=re.sub(r'(?i)</td>|</th>',' | ',t)
    t=re.sub(r'<[^>]+>',' ',t)
    t=html.unescape(t)
    t=re.sub(r'[ \t\xa0]+',' ',t)
    t=re.sub(r'\n\s*\n+','\n',t)
    return t
cik, acc, doc, name = sys.argv[1:5]
url=f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{doc}'
b=get(url)
open(os.path.join('cache',name),'w',encoding='utf-8').write(strip(b))
print(name, len(b))
