import sys, urllib.request, re, html, os, time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def get(acc, doc, name):
    cik='1111711'; a=acc.replace('-','')
    url=f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{doc}'
    raw=urllib.request.urlopen(urllib.request.Request(url,headers=UA)).read().decode('utf-8','replace')
    t=re.sub(r'(?is)<(script|style).*?</\1>',' ',raw)
    t=re.sub(r'(?i)<ix:header>.*?</ix:header>',' ',t,flags=re.S)
    t=re.sub(r'(?i)</(p|div|tr|li|h\d|table)>','\n',t)
    t=re.sub(r'(?i)<br\s*/?>','\n',t)
    t=re.sub(r'(?i)</t[dh]>',' | ',t)
    t=re.sub(r'<[^>]+>','',t); t=html.unescape(t)
    t=re.sub(r'[ \t\xa0]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(os.path.join('cache',name),'w',encoding='utf-8').write(t)
    print(name,len(t)); time.sleep(0.3)
for line in sys.argv[1:]:
    acc,doc,name=line.split(',')
    get(acc,doc,name)
