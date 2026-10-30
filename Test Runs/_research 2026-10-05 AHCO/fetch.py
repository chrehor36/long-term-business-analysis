import sys, json, re, time, urllib.request, html
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"identity"}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    return urllib.request.urlopen(req,timeout=60).read()
def totext(b):
    s=b.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?i)<br\s*/?>','\n',s)
    s=re.sub(r'(?i)</(p|div|tr|li|h\d)>','\n',s)
    s=re.sub(r'(?i)</t[dh]>',' | ',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s)
    s=re.sub(r'[ \t\xa0]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
cik='1725255'
for arg in sys.argv[1:]:
    acc,doc,name=arg.split(',')
    url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
    try:
        t=totext(get(url)); open(name,'w',encoding='utf-8').write(t); print(name,len(t))
    except Exception as e: print('FAIL',name,e)
    time.sleep(0.3)
