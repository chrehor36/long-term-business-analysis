import sys, os, re, time, urllib.request, html
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"identity"}
def get(url):
    for k in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60).read()
        except Exception as e:
            print("retry",e); time.sleep(2)
    raise SystemExit("fail "+url)
def strip(b):
    t=b.decode('utf-8','replace')
    t=re.sub(r'(?is)<(script|style).*?</\1>','',t)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
    t=re.sub(r'(?i)</td>',' | ',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    return t
cik,acc,doc,out=sys.argv[1:5]
url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
b=get(url); open(os.path.join('cache',out),'w',encoding='utf-8').write(strip(b)); print(out,len(b))
