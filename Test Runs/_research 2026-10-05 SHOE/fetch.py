import sys, json, urllib.request, gzip, re, html, os, time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip'}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    r=urllib.request.urlopen(req,timeout=60).read()
    try: r=gzip.decompress(r)
    except Exception: pass
    return r
def totext(b):
    s=b.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'(?i)<br\s*/?>','\n',s)
    s=re.sub(r'(?i)</(p|div|tr|li|h\d|table)>','\n',s)
    s=re.sub(r'(?i)</t[dh]>',' | ',s)
    s=re.sub(r'<[^>]+>',' ',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
cik=sys.argv[1]
for spec in sys.argv[2:]:
    acc,doc,name=spec.split(',')
    url=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
    if os.path.exists(name): continue
    try:
        t=totext(get(url)); open(name,'w',encoding='utf-8').write(t); print(name,len(t))
    except Exception as e: print('FAIL',name,url,e)
    time.sleep(0.3)
