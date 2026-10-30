import sys,urllib.request,re,html,time,os
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def get(url):
    for i in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60).read()
        except Exception as e:
            print('retry',e); time.sleep(3)
def totext(b):
    s=b.decode('utf-8','replace')
    s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?is)<ix:header>.*?</ix:header>','',s)
    s=re.sub(r'(?i)</(p|div|tr|li|h\d|table)>','\n',s)
    s=re.sub(r'(?i)<br\s*/?>','\n',s)
    s=re.sub(r'(?i)</t[dh]>',' | ',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
outdir=sys.argv[1]
for spec in sys.argv[2:]:
    name,acc,doc=spec.split('|')
    url=f"https://www.sec.gov/Archives/edgar/data/1587732/{acc.replace('-','')}/{doc}"
    b=get(url)
    open(os.path.join(outdir,name+'.txt'),'w',encoding='utf-8').write(totext(b))
    print(name,len(b)); time.sleep(0.4)
