import sys, re, html, urllib.request, time, os
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"identity"}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    for k in range(4):
        try:
            return urllib.request.urlopen(req,timeout=60).read()
        except Exception as e:
            print("retry",url,e); time.sleep(2)
    raise SystemExit("fail "+url)
def totext(b):
    s=b.decode('utf-8','replace')
    s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?is)<ix:header>.*?</ix:header>','',s)
    s=re.sub(r'(?i)<br\s*/?>','\n',s)
    s=re.sub(r'(?i)</(p|div|tr|li|h\d|table)>','\n',s)
    s=re.sub(r'(?i)</t[dh]>',' | ',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
import os
cik=os.environ.get("CIK","6951")
for arg in sys.argv[1:]:
    name,acc,doc=arg.split(',')
    if os.path.exists(name+'.txt'): continue
    url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
    t=totext(get(url)); open(name+'.txt','w',encoding='utf-8').write(f"SOURCE {url}\nACCESSION {acc}\n"+t)
    print(name,len(t)); time.sleep(0.3)
